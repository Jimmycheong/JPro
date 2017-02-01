#====##====##====##====##====#
#====##====##====##====##====#
'''
INVENTORY: 

- The widget display the current inventory held in house 

'''
#====##====##====##====##====#
#====##====##====##====##====#

import sys 
import datetime
from PyQt5.QtWidgets import (QApplication, 
															QWidget, 
															QSizePolicy,
															QVBoxLayout,
															QHBoxLayout,
															)
from connect import Connect 
from dbcreation import Models

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class IBox(QWidget): 

	def __init__(self): 
		super().__init__()
		self.setGeometry(0,0,640,440)
		self.setWindowTitle('JPro')
#		self.setStyleSheet('background-color: #444444')


		self.bargraph = PlotCanvas(self, width=4, height=3)
		self.bargraph.move(0,0)

		iboxlayout = QHBoxLayout()
		iboxlayout.addWidget(self.bargraph)	
		self.setLayout(iboxlayout)
		self.show()


class PlotCanvas(FigureCanvas): 

	def __init__(self, parent, width=5,height=4,dpi=100):
		
		self.fig, self.axes = plt.subplots(figsize=(6,4))
		self.main = Connect()
		
		FigureCanvas.__init__(self,self.fig)
		self.setParent(parent)

		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
		self.plot()

	def plot(self): 
	
		models = [i.name for i in self.main.session.query(Models).all()]
		x = np.arange(len(models))
		quantity = [100,200,300,150]

		self.axes.bar(x,quantity, align='center', alpha=0.5, color='lightblue')
		plt.xticks(x,models)
		plt.ylabel('Stock')
		plt.title('Inventory')
		self.axes.margins(0.05)
		self.axes.set_ylim(bottom=0)
		self.fig.set_size_inches(3,4,forward=True)
		#plt.draw()


if __name__ == '__main__' : 

	app = QApplication(sys.argv)
	ibox = IBox()
	sys.exit(app.exec_())