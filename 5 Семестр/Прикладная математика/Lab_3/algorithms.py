import numpy as np
import matplotlib.pyplot as plt


def make_plot(pin_array, norm_array):
	fig, (value_dist, mse) = plt.subplots(2, sharex=True)

	value_dist.set_title("Значения распределения вероятностей")
	value_dist.plot(range(0, len(pin_array)), pin_array)

	mse.set_title("Среднеквадратичное отклонения")
	mse.plot(norm_array)

	plt.show()


# Численно
def find_limiting_distribution(pi0, P, max_iter=10, epsilon=0.000001):
	pin_array = []
	norm_array = []
	cur_pi = pi0

	for _ in range(max_iter):
		pin_array.append(cur_pi.tolist()[0])
		prev_pi = cur_pi
		cur_pi = cur_pi@P
		norm_array.append(np.linalg.norm(prev_pi - cur_pi))
		if norm_array[-1] < epsilon:
			break

	make_plot(pin_array, norm_array)

	return cur_pi


# Аналитически
def find_stationary_distribution(P):
	PT = P.T
	PT -= np.identity(len(P))
	PT = np.append(PT, [np.ones(len(PT))], axis=0)

	b = np.zeros((len(PT)))
	b[-1] = 1

	return np.linalg.lstsq(PT, b)[0]


if __name__ == '__main__':
	P = np.array([[0, 0.5, 0.5],
				  [0.25, 0.5, 0.25],
				  [0.25, 0.25, 0.5]])
	p0_1 = np.matrix([0, 0, 1])
	p0_2 = np.matrix([0.2, 0.5, 0.3])

	print(find_limiting_distribution(p0_1, P))
	print(find_limiting_distribution(p0_2, P))

	print(find_stationary_distribution(P))
	print()

	P = np.array([[0, 1],
				  [1, 0]])
	p0_1 = np.matrix([0.4, 0.6])
	print(find_limiting_distribution(p0_1, P))








	# P = np.array([[0.2, 0.7, 0.1],
	# 			  [0.9, 0.0, 0.1],
	# 			  [0.2, 0.8, 0.0]])
	# state = np.array([[1.0, 0.0, 0.0]])
	# # note: the matrix is row stochastic.
	# # A markov chain transition will correspond to left multiplying by a row vector.
	# Q = np.array([
	# 	[0.2, 0.7, 0.1],
	# 	[0.9, 0.0, 0.1],
	# 	[0.2, 0.8, 0.0]])
	#
	# # We have to transpose so that Markov transitions correspond to right multiplying by a column vector.  np.linalg.eig finds right eigenvectors.
	# evals, evecs = np.linalg.eig(P.T)
	# evec1 = evecs[:, np.isclose(evals, 1)]
	#
	# # Since np.isclose will return an array, we've indexed with an array
	# # so we still have our 2nd axis.  Get rid of it, since it's only size 1.
	# evec1 = evec1[:, 0]
	#
	# stationary = evec1 / evec1.sum()
	# print('asd')
	# print(stationary)
	# # eigs finds complex eigenvalues and eigenvectors, so you'll want the real part.
	# stationary = stationary.real
	#
	#
	#
	# A = np.append(P.T - np.identity(3), [[1, 1, 1]], axis=0)
	# b = np.array([0, 0, 0, 1]).T
	# # print(A)
	# # print(A.T)
	# # print(b)
	# # print(A.T@A)
	# # print(A.T@b)
	# print(np.linalg.solve(A.T@A, A.T@b))
