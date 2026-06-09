import matplotlib.pyplot as plt

# Data define kro
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots(figsize=(3.5, 3))

_ = ax.plot(x, y, 'rs-', label='label')
_ = ax.legend(frameon=False, loc=0, title='')

# Set axis labels, display in boldC:\Users\BQ2541WS\AppData\Local\Programs\Python\Python315\python.exe -m pip install matplotlib
ax.set_xlabel("X (unit)", fontweight="bold")
ax.set_ylabel("Y (unit)", fontweight="bold")

plt.show()
