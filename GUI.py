import sys 
from PyQt5.QtWidgets import (QApplication, 
															QWidget, 
															QLabel, 
															QTableWidget, 
															QTableWidgetItem,
															QVBoxLayout,
															QHBoxLayout,
															QPushButton,
															qApp,
															QShortcut,
															QDialog,
															QAbstractItemView,
															QGridLayout,
															QHeaderView,
															)
from PyQt5.QtGui import QKeySequence
from main2 import Main 
from dbcreation import Base, Models, ProductionQueue
import datetime

from dialog_new import Dialog as DBox

class GUI(QWidget): 

	def __init__(self): 
		super().__init__()

		self.initUI()

	def initUI(self): 
	
		#Shortcut to close window 
		exitShortcut = QShortcut(QKeySequence('Ctrl+W'),self, qApp.quit)

		vBox = QVBoxLayout()
		controlBox = QHBoxLayout()
		tableBox = QGridLayout()

		label1 = QLabel('Machine Production')

		#====##====##====##====##====#
		#SESSION EXTRACTION TO TABLE 
		#====##====##====##====##====#

		#Session instance creation 
		self.main = Main()

		#Extract all orders in the procedure queue
		self.all_orders = self.main.session.query(ProductionQueue).all()
		self.table_length = len(self.all_orders)
		print('origin table length: ', self.table_length)
		#Generate Table & Setting Column headers
		self.table = QTableWidget(len(self.all_orders),4,self)

		self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Model')) 
		self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Quantity'))
		self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Order Date'))

		'''
		Use QHeader Class to resize the tables
		'''
		order_header = self.table.horizontalHeader()
		order_header.setMinimumSectionSize(130)
		order_header.setSectionResizeMode(QHeaderView.Stretch)

		self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Expected completion'))

		self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

		print ('original selection: ', self.table.currentRow())

		# Iterating through all records 
		
		self.setData(self.all_orders)

		#====##====##====##====##====#
		#CONTROL PANEL 
		#====##====##====##====##====#

		btn_neworder = QPushButton('New', self)
		btn_neworder.clicked.connect(self.getDBox)

		btn_deleterecord = QPushButton('Delete', self)
		btn_deleterecord.clicked.connect(self.deleteRecord)

		controlBox.addWidget(btn_neworder)
		controlBox.addWidget(btn_deleterecord)

		#Adding table into VBoxLayout

		tableBox.addWidget(self.table)

		vBox.addWidget(label1)
		vBox.addLayout(tableBox)
		vBox.addLayout(controlBox)

		self.setLayout(vBox)

		self.setGeometry(0,0,640,440)
		self.setWindowTitle('GUI application')
		self.show()

		#====##====##====##====##====#
		#CONTROL PANEL 
		#====##====##====##====##====#

	'''
	getDBox: Brings up the Dialog Box from dialog_new
	'''
	def getDBox(self) : 
		dbox = DBox()
		dbox.exec()
		if dbox.oq_input.text(): 
			self.resetTable()

	'''
	resetTable(): 
	1. Clears the contents of the Table 
	2. Inserts an extra row 
	3. Updates the table with latest db data via query
	'''

	def resetTable(self):
		self.table.clearContents()
		latest_table =  len(self.main.session.query(ProductionQueue).all())
		self.table.insertRow(latest_table - 1)
		self.setData(self.main.session.query(ProductionQueue).all())

	'''
	setData(): 
	- Runs a loop to populate the table with the current database records 
	'''

	def setData(self, all_orders):
		row = 0 
		for order in all_orders: 
			self.table.setItem(row, 0, QTableWidgetItem(order.model))
			self.table.setItem(row, 1, QTableWidgetItem(str(order.order_quantity)))
			self.table.setItem(row, 2, QTableWidgetItem(str(order.order_time)))
			row += 1 

	'''
	deleteRecord(): 
	- Deletes the currently selected record from the table 
	- Use setCurrentCell() to ensure the current selection is reset to None
	'''			

	def deleteRecord(self):
		self.table.removeRow(self.table.currentRow())
		self.table.setCurrentCell(-1,-1) 
				
if __name__ == '__main__' : 

	app = QApplication(sys.argv)
	gui = GUI()
	sys.exit(app.exec_())