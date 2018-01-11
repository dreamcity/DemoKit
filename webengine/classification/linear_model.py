# -*- coding=utf8 -*-
import matplotlib
matplotlib.use('Agg')

import numpy as np
import sklearn.datasets
import matplotlib.pyplot as plt
import sklearn.linear_model

class LinearModel(object):
	"""docstring for LinearModel"""
	def __init__(self):
		super(LinearModel, self).__init__()
		np.random.seed(0)
		self.data , self.model = sklearn.datasets.make_moons(200, noise=0.30)

	def plot_decision_boundary(self,predict_func, data, label):
		"""画出结果图

		Args:
			pred_func (callable): 预测函数
			data (numpy.ndarray): 训练数据集合
			label (numpy.ndarray): 训练数据标签
		"""
		x_min, x_max = data[:, 0].min() - .5, data[:, 0].max() + .5
		y_min, y_max = data[:, 1].min() - .5, data[:, 1].max() + .5
		h = 0.01

		xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

		Z = predict_func(np.c_[xx.ravel(), yy.ravel()])
		Z = Z.reshape(xx.shape)

		plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
		plt.scatter(data[:, 0], data[:, 1], c=label, cmap=plt.cm.Spectral)
		plt.savefig('./webapp/static/tmp/common_result.jpg')
			
	def run_linear_model(self):
		clf = sklearn.linear_model.LogisticRegressionCV()
		clf.fit(self.data , self.model)
		self.plot_decision_boundary(lambda x: clf.predict(x), self.data , self.model)
		return None
