import matplotlib.pyplot as plt

x_value = range(1,5000)
y_value = [x**2 for x in x_value]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Greens, s=10)

ax.ticklabel_format(style='plain')
plt.show()