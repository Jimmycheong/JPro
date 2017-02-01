import sys
from PyQt5.QtWidgets import (QApplication, 
														 QDialog,
														 QLineEdit,
														 QShortcut,
														 qApp,
														 QLabel,
														 QPushButton,
														 QComboBox,
															)
from PyQt5.QtGui import QKeySequence
from dbcreation import Models
from main2 import Main
from dbcreation import ProductionQueue

class Dialog(QDialog): 

	def __init__(self): 
		super().__init__()

		self.initdiagUI()

	def initdiagUI(self):
		exitShortcut = QShortcut(QKeySequence('Ctrl+W'),self, qApp.quit)

		self.main = Main()
		all_models = self.main.session.query(Models).all()

		label_model = QLabel('Model',self)
		label_model.move(40, 50)

		self.combo = QComboBox(self)
		for model in all_models: 
			self.combo.addItem(model.name)
		self.combo.move(180, 50)

		label_orderquantity = QLabel('Order Quantity',self)
		label_orderquantity.move(40, 100)

		self.oq_input = QLineEdit('',self)
		self.oq_input.move(180, 100)

		self.error_message = QLabel('',self)
		self.error_message.move(180, 130)

		btn_submit = QPushButton('Submit Order', self)
		btn_submit.move(180,150)
		btn_submit.clicked.connect(self.submittodb)

		self.setFixedSize(350,200)
		self.setWindowTitle('Input Dialog')
		self.show()		

	def submittodb(self): 
		#print ('Inside label: ', self.oq_input.text())
		if self.oq_input.text().isdigit():
			instance = ProductionQueue(model=self.combo.currentText(), 
																	order_quantity = self.oq_input.text())
			self.main.session.add(instance)
			self.main.session.commit()
			self.close()
		else: 
			self.error_message.setText('Please enter an integer only')
			self.error_message.adjustSize()
			self.error_message.setStyleSheet("color:red")


if __name__ == '__main__' : 

	app = QApplication(sys.argv)
	dialog = Dialog()
	sys.exit(app.exec_())