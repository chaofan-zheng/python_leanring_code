from matplotlib import pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values)
plt.show()