from src.Fuzzy import Fuzzy
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

fuzz = Fuzzy()
# ext0 = fuzz.get_extension(10, 11, 0)
# print(ext0)

# plt.plot(fuzz.x_arriving_green_light, fuzz.arriving_green_light_few, 'r', linewidth=2, label='few')
# plt.plot(fuzz.x_arriving_green_light, fuzz.arriving_green_light_small, 'g', linewidth=2, label='small')
# plt.plot(fuzz.x_arriving_green_light, fuzz.arriving_green_light_medium, 'b', linewidth=2, label='medium')
# plt.plot(fuzz.x_arriving_green_light, fuzz.arriving_green_light_many, 'y', linewidth=2, label='many')
# plt.legend()
# plt.xticks(np.arange(0, 17, 1))
# plt.show()

# plt.plot(fuzz.x_behind_red_light, fuzz.behind_red_light_few, 'r', linewidth=2, label='few')
# plt.plot(fuzz.x_behind_red_light, fuzz.behind_red_light_small, 'g', linewidth=2, label='small')
# plt.plot(fuzz.x_behind_red_light, fuzz.behind_red_light_medium, 'b', linewidth=2, label='medium')
# plt.plot(fuzz.x_behind_red_light, fuzz.behind_red_light_many, 'y', linewidth=2, label='many')
# plt.legend()
# plt.xticks(np.arange(0, 17, 1))
# plt.show()

# plt.plot(fuzz.x_extension, fuzz.extension_zero, 'r', linewidth=2, label='zero')
# plt.plot(fuzz.x_extension, fuzz.extension_short, 'g', linewidth=2, label='short')
# plt.plot(fuzz.x_extension, fuzz.extension_medium, 'b', linewidth=2, label='medium')
# plt.plot(fuzz.x_extension, fuzz.extension_long, 'y', linewidth=2, label='long')
# plt.legend()
# plt.xticks(np.arange(-9, 21, 1))
# plt.show()

output = []

x1 = np.arange(0, 13, 1)
x2 = np.arange(0, 35, 1)

for green in x1:
    for red in x2:
        output.append([green, red, fuzz.get_extension(green, red, 0)])

arr = np.array(output)
np.savetxt("test_output.csv", arr, delimiter=",")