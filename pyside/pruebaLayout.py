import sys
from PySide.QtGui import *
from PySide.QtCore import *

qt_app = QApplication(sys.argv)
 
class LayoutExample(QWidget):
    ''' An example of PySide/PyQt absolute positioning; the main window
    inherits from QWidget, a convenient widget for an empty
    window. '''

    def __init__(self):
    # Initialize the object as a QWidget and
    # set its title and minimum width
        QWidget.__init__(self)
        self.setWindowTitle('Dynamic Greeter')
        self.setMinimumWidth(400)

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        
        self.salutations = ['Ahoy', 'Good day', 'Hello', 'Heyo', 'Hi', 'Salutations', 'Wassup', 'Yo'] 
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)
    
        self.form_layout.addRow('&amp;Salutation:', self.salutation) 
        self.recipient = QLineEdit(self)
        self.recipient.setPlaceholderText('world') 
        self.form_layout.addRow('&amp;Recipient:', self.recipient)

        self.greeting = QLabel('', self)
        self.form_layout.addRow('Greeting:', self.greeting)

        self.layout.addLayout(self.form_layout)

        self.layout.addStretch(3)
        
        self.button_box = QHBoxLayout()
        self.button_box.addStretch(1)
        self.build_button = QPushButton('&amp;Build Greeting', self)
        self.button_box.addWidget(self.build_button)
        self.layout.addLayout(self.button_box)
        self.setLayout(self.layout)

    def run(self):
        self.show()
        qt_app.exec_()
app = LayoutExample()
app.run()
