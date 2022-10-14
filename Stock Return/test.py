import quickchart
import numpy as np
import pandas as pd
import openpyxl
from openpyxl.chart import Reference, LineChart, Series
from openpyxl.chart.axis import DateAxis
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import datetime

# Assign spreadsheet filename to `file`
file = 'StockInvestment.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
# print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')

# print(df1.head)

mydata = df1['Amount ($) Inflation Adjusted']
mydate = df1['Date']



wb = openpyxl.load_workbook('StockInvestment.xlsx')
sheet = wb.active

# Data for plotting
values = Reference(sheet,
                   min_col=5,
                   max_col=5,
                   min_row=1,
                   max_row=871)

# Create object of LineChart class
chart = LineChart()
chart.add_data(values, titles_from_data=True)
dates = Reference(sheet, min_col=7, min_row=2, max_row=871)
chart.set_categories(dates)
chart.y_axis.crossAx = 500

# Use DateAxis class for X axis
chart.x_axis = DateAxis(crossAx=500)
chart.x_axis.number_format = 'mm-yy'
chart.x_axis.majorTimeUnit = "months"

# set the title of the chart
chart.title = "Inflation Adjusted S&P 500 Index Value"
# set the title of the x-axis
chart.x_axis.title = "Date"

# set the title of the y-axis
chart.y_axis.title = "Index Value"

# the top-left corner of the chart
# is anchored to cell F2 .
sheet.add_chart(chart, "A1")

# save the file
wb.save("wb2.xlsx")

mylabel = df1.Date[0:2]

chart = quickchart.QuickChart()
chart.width = 1024
chart.height = 512
chart.config = {
    "type": "bar",
    "data": {
        "labels": [mylabel[0],mylabel[1]],
        "datasets": [{
            "label": "Test",
            "data": [mydata[0],mydata[1]]
        }]
    }
}

# Get the url...
image_url = chart.get_url()

# Or write to disk...
chart.to_file('/temp/mychart.png')

x = mydate
y = mydata

#calculate equation for trendline
x_1 = pd.to_datetime(x).astype(np.int64)
z = np.polyfit(x_1, y, 1)
p = np.poly1d(z)

#calculate equation for exponentical trendline
m = np.polyfit(x_1, np.log(y), 1)
a = np.exp(m[1])
b = m[0]

y_fitted = a * np.exp(b * x_1)

figure(figsize=(9, 6), dpi=200)
plt.plot(x,y,'g',linewidth=2)
plt.title("Inflation Adjusted S&P 500 Index Value", fontsize=18, fontweight='bold')
plt.xlabel("Date", fontweight='bold')
plt.ylabel("Index Value", fontweight='bold')
plt.grid(axis='y')
#plt.plot(x,p(x_1))
plt.plot(x,y_fitted,'b-',linewidth=1)

plt.show()










