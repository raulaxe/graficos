import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.plot(x_values, y_values)
plt.title("POTENCIA DE 3", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squares of Values", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize= 14)
plt.axis([0,7, 0, 150.0])
plt.show()