import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# set chart tittle and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square Value", fontsize=12)

# Set size of tick lables
# plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()