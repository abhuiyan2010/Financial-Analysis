import numpy as np

# Set a seed for the random number generator so we get the same random numbers each time
np.random.seed(20210706)

# Create fake x-data
x = np.arange(10)
# Create fake y-data
a = 4.5
b = 0.5
c = 0
y = a * np.exp(b * x) + c  # Use the second formulation from above
y = y + np.random.normal(scale=np.sqrt(np.max(y)), size=len(x))  # Add noise

# Fit a polynomial of degree 1 (a linear function) to the data
p = np.polyfit(x, np.log(y), 1)


# Convert the polynomial back into an exponential
a = np.exp(p[1])
b = p[0]
x_fitted = np.linspace(np.min(x), np.max(x), 100)
y_fitted = a * np.exp(b * x_fitted)

import matplotlib.pyplot as plt

ax = plt.axes()
ax.scatter(x, y, label='Raw data')
ax.plot(x_fitted, y_fitted, 'k', label='Fitted curve')
ax.set_title('Using polyfit() to fit an exponential function')
ax.set_ylabel('y-Values')
ax.set_ylim(0, 500)
ax.set_xlabel('x-Values')
ax.legend()

plt.show()