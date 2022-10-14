import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# Assign spreadsheet filename to `file`
file = 'StockInvestment.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df = xl.parse('Sheet2')

Years = df['Year']
Investment = df['Amount ($) Inflation Adjusted']
AnnaulizedReturn = df['Annualized Return']
CPIData = df['CPI']

CPI = 23.5
df.at[0, 'CPI'] = CPI

def CalculateROI(StartIndex, EndIndex, InitialInvestment):
    TotalInvestment = 0

    for i in range (StartIndex,EndIndex,1):
        InvestmentValues[i] = InitialInvestment
        TotalInvestment = TotalInvestment + InvestmentValues[i] * CPIData[StartIndex] / CPIData[i]
        for j in range (i,EndIndex):
            InvestmentValues[i] = InvestmentValues[i] * (1 + AnnaulizedReturn[j])
        #print(InvestmentValues[i])

    TotalReturn = sum(InvestmentValues) * CPIData[StartIndex] / CPIData[EndIndex - 1]

    #print(TotalReturn)
    #print(TotalInvestment)

    AnnualizedROI = ((TotalReturn/TotalInvestment)**(1/InvestmentLength) - 1)*100
    #print(AnnualizedROI)

    return AnnualizedROI

InvestmentStart = 1950
InvestmentEnd = 2012
InvestmentLength = 10
ROIValues_10 = np.empty(72, dtype=object)

for i in range(InvestmentStart, InvestmentEnd):
    InvestmentValues = [0] * 72
    InitialInvestment = 100

    StartIndex = i - InvestmentStart
    EndIndex = StartIndex + InvestmentLength

    ROIValues_10[i-InvestmentStart] = CalculateROI(StartIndex, EndIndex, InitialInvestment)

print(ROIValues_10)

InvestmentStart = 1950
InvestmentEnd = 2002
InvestmentLength = 20
ROIValues_20 = np.empty(72, dtype=object)

for i in range(InvestmentStart, InvestmentEnd):
    InvestmentValues = [0] * 72
    InitialInvestment = 100

    StartIndex = i - InvestmentStart
    EndIndex = StartIndex + InvestmentLength

    ROIValues_20[i-InvestmentStart] = CalculateROI(StartIndex, EndIndex, InitialInvestment)

print(ROIValues_20)

InvestmentStart = 1950
InvestmentEnd = 1992
InvestmentLength = 30
ROIValues_30 = np.empty(72, dtype=object)

for i in range(InvestmentStart, InvestmentEnd):
    InvestmentValues = [0] * 72
    InitialInvestment = 100

    StartIndex = i - InvestmentStart
    EndIndex = StartIndex + InvestmentLength

    ROIValues_30[i-InvestmentStart] = CalculateROI(StartIndex, EndIndex, InitialInvestment)

print(ROIValues_30)

x = np.arange(1950,2022,1)
w = ROIValues_10
y = ROIValues_20
z = ROIValues_30

figure(figsize=(9, 6), dpi=100)
plt.plot(x,w,linewidth=0.5,label="10 Year Return on Investment")
plt.plot(x,y,linewidth=1,label="20 Year Return on Investment")
plt.plot(x,z, linewidth=2,label="30 Year Return on Investment")
plt.legend(loc='upper left')
plt.ylim(-5, 15)

plt.title("10, 20 and 30 Years Rate of Return", fontweight='bold')
plt.xlabel("Year", fontweight='bold')
plt.ylabel("Rate of Return %", fontweight='bold')
plt.grid(axis='y')

#plt.show()

print(len(ROIValues_10))








