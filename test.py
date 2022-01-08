from src.Fuzzy import Fuzzy
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

fuzz = Fuzzy()

# plot membership function
fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize = [6, 20])

ax1.plot(fuzz.x_arriving_green_light, fuzz.arriving_green_light_few, 'r', linewidth=2, label='few')
ax1.plot(fuzz.x_arriving_green_light, fuzz.arriving_green_light_small, 'g', linewidth=2, label='small')
ax1.plot(fuzz.x_arriving_green_light, fuzz.arriving_green_light_medium, 'b', linewidth=2, label='medium')
ax1.plot(fuzz.x_arriving_green_light, fuzz.arriving_green_light_many, 'y', linewidth=2, label='many')
ax1.legend()
ax1.set_xticks(np.arange(0, 13, 1))
ax1.set_xlabel('x')
ax1.set_ylabel('u(x)')
ax1.set_title('Arrival')

ax2.plot(fuzz.x_behind_red_light, fuzz.behind_red_light_few, 'r', linewidth=2, label='few')
ax2.plot(fuzz.x_behind_red_light, fuzz.behind_red_light_small, 'g', linewidth=2, label='small')
ax2.plot(fuzz.x_behind_red_light, fuzz.behind_red_light_medium, 'b', linewidth=2, label='medium')
ax2.plot(fuzz.x_behind_red_light, fuzz.behind_red_light_many, 'y', linewidth=2, label='many')
ax2.legend()
ax2.set_xticks(np.arange(0, 35, 2))
ax2.set_xlabel('x')
ax2.set_ylabel('u(x)')
ax2.set_title('Queue')

ax3.plot(fuzz.x_extension, fuzz.extension_zero, 'r', linewidth=2, label='zero')
ax3.plot(fuzz.x_extension, fuzz.extension_short, 'g', linewidth=2, label='short')
ax3.plot(fuzz.x_extension, fuzz.extension_medium, 'b', linewidth=2, label='medium')
ax3.plot(fuzz.x_extension, fuzz.extension_long, 'y', linewidth=2, label='long')
ax3.legend()
ax3.set_xticks(np.arange(-9, 10, 1))
ax3.set_xlabel('x')
ax3.set_ylabel('u(x)')
ax3.set_title('Extension')
plt.show()

# list all possible inputs and compute inference store in csv
output = []

x1 = np.arange(0, 13, 1)
x2 = np.arange(0, 35, 1)

for green in x1:
    for red in x2:
        output.append([green, red, fuzz.get_extension(green, red, 0)])

arr = np.array(output)
np.savetxt("test_output.csv", arr, delimiter=",")


# 3d plot of inputs and output
z = []
def f(x, y):
    return fuzz.get_extension(x, y, 0)

z = np.array(z)
x = np.linspace(0, 12)
y = np.linspace(0, 34)
X, Y = np.meshgrid(x, y)
Z = np.vectorize(f)(X, Y)

plt.figure(figsize=(20,20))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('Fuzzy Inference')
ax.set_xticks(np.arange(0, 13, 1))
ax.set_xlabel('Arrival')
ax.set_yticks(np.arange(0, 35, 2))
ax.set_ylabel('Queue')
ax.set_zticks(np.arange(-8, 7, 1))
ax.set_zlabel('Extension')
plt.show()
