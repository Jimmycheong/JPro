import sys 
from PyQt5.QtWidgets import (QApplication, 
														 QMainWindow,
														 QTabWidget,
														 QShortcut,
														 qApp,
															)
from PyQt5.QtGui import QKeySequence
from pbox import PBox
from ibox import IBox

class App(QMainWindow): 
	
	def __init__(self):
		super().__init__() 

		self.tabs = QTabWidget()
		self.setCentralWidget(self.tabs)
		
		self.pbox = PBox()
		self.tabs.addTab(self.pbox, 'Order Queue / 生产队列')

		self.ibox = IBox()
		self.tabs.addTab(self.ibox, 'Inventory / 库存 ')		

		self.setGeometry(0,0,640,440)
		self.setWindowTitle('JPro')
#		self.setStyleSheet('background-color: #444444')
		self.show()

		#===##===##===##===##===#
		#Shortcuts 
		#===##===##===##===##===#
		exitShortcut = QShortcut(QKeySequence('Ctrl+W'),self, qApp.quit)

if __name__ == '__main__' : 

	app = QApplication(sys.argv)
	main = App()
	sys.exit(app.exec_())