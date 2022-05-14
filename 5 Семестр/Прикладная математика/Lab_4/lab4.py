from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

l = 7.23
u = 4.9

x = []
y = []


def rhs(s, v):
	kz = (v[1] + 2 * v[2] + 3 * v[3] + 4 * (v[4] + v[5])) / 4
	kp = (v[3] + 2 * v[2] + 3 * v[1] + 4 * v[0]) / 4

	x.append(kz)
	y.append(kp)

	return [-l * v[0] + u * v[1],
			l * v[0] - (u + l) * v[1] + 2 * u * v[2],
			l * v[1] - (2 * u + l) * v[2] + 3 * u * v[3],
			l * v[2] - (3 * u + l) * v[3] + 4 * u * v[4],
			l * v[3] - (4 * u + l) * v[4] + 4 * u * v[5],
			l * v[4] - 4 * u * v[5]]


res = solve_ivp(rhs, (0, 10), [1, 0, 0, 0, 0, 0])
print(res)

plt.plot(res.t, res.y.T)
print(res.y.T)
plt.show()

plt.plot(x)
plt.plot(y)
plt.show()
