import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib.figure as figure
from matplotlib import patheffects
import numpy as np


# Визначення функцій
def target_func(x1, x2):
    return 1.1 * x1 + 0.7 * x2


def constraint1(x1, x2):
    return 72 - 0.18 * x1 - 0.09 * x2


def constraint2(x1, x2):
    return 56 - 0.08 * x1 - 0.28 * x2


# Побудова графіків
fig, ax = plt.subplots() # type:figure.Figure, axes.Axes

x1 = np.linspace(0, 700, 701)
x2 = np.linspace(0, 800, 801)
X1, X2 = np.meshgrid(x1, x2)

# Обмеження
Z1 = constraint1(X1, X2)
Z2 = constraint2(X1, X2)

C_Z1=ax.contour(X1, X2, Z1, levels=[0], colors='r')
C_Z2=ax.contour(X1, X2, Z2, levels=[0], colors='g')
plt.setp(C_Z2.collections, path_effects=[patheffects.withTickedStroke(angle=60, length=30)])
plt.setp(C_Z1.collections, path_effects=[patheffects.withTickedStroke(angle=135, length=30)])
h1,l1 = C_Z1.legend_elements()
h2,l1 = C_Z2.legend_elements()
plt.legend([h1[0], h2[0]], ['0.18 * x1 + 0.09 * x2 <= 72', '0.08 * x1 + 0.28 * x2 <= 56'])

ax.set_xlabel('x1')
ax.set_ylabel('x2')

# Цільова функція
Z = target_func(X1, X2)
CS_Z = ax.contour(X1, X2, Z, levels=[0, 400, 600, 800])
ax.clabel(CS_Z, inline=True, fontsize=10)


#Максимум цільової функції  у точці перетину '0.18 * x1 + 0.09 * x2 = 72 та '0.08 * x1 + 0.28 * x2 = 56
A = np.array([[0.18, 0.09],
             [0.08, 0.28]])
y = np.array([72, 56])

x = np.linalg.solve(A, y)
S_x1 = x[0]
S_x2 = x[1]

ax.axvline(x=S_x1, color='black')
ax.axhline(y=S_x2, color='black')

ax.set_title('Цільова функція - 1.1 * x1 + 0.7 * x2 \n' +
             'Максимум функції ' + str(round(target_func(S_x1, S_x2))) + ' у точці x1 = ' + str(round(S_x1)) +
             ', x2 = ' + str(round(S_x2)))

plt.savefig('figure.png', dpi=300)