from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QDialog, QGridLayout, QLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import code

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

import random
class Window(QWidget):
    def __init__(self):
        self.checker = False

        QWidget.__init__(self)
        self.resize(600, 600)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)
        self.filePath=''
        self.fileName="Select File"
        self.checker=0
        self.mainLayout()

    def on_button_Send_clicked(self):

        print("c0")
        self.filePath = QFileDialog.getOpenFileName(self, "Create Graph", "~", "Dataset Files (*.csv *.xls)")[0]
        self.fileName = self.filePath.split("/")[-1] + "  (Select Another File)"
        print("c1")

        self.data = code.get_accuracy(self.filePath)


        print("c2")
        if self.checker==0:
            self.checker=1
            self.mainLayout2()
        else:
            self.checker=0
            self.mainLayout()



    def mainLayout(self):
        layout = QVBoxLayout()

        button_Exit = QPushButton("Exit")
        button_Exit.setFont(QFont('Arial', 15))
        button_Exit.clicked.connect(QCoreApplication.instance().quit)

        labelTextTitle = QLabel("Bangla Intelligent ChatBot")
        labelTextTitle.setFont(QFont('Arial', 18))

        self.figure = plt.figure()
        self.figure.set_facecolor("none")
        self.canvas = FigureCanvas(self.figure)

        button_Send = QPushButton(self.fileName)
        button_Send.setFont(QFont('Arial', 15))
        button_Send.clicked.connect(self.on_button_Send_clicked)
        print("p1")
        self.plot()
        print("p2")

        layout.addWidget(self.canvas)
        layout.addWidget(button_Send)
        layout.addWidget(button_Exit)

        self.setLayout(layout)

    def mainLayout2(self):
        layout = QVBoxLayout()

        button_Exit = QPushButton("Exit")
        button_Exit.setFont(QFont('Arial', 15))
        button_Exit.clicked.connect(QCoreApplication.instance().quit)

        labelTextTitle = QLabel("Bangla Intelligent ChatBot")
        labelTextTitle.setFont(QFont('Arial', 18))

        self.figure = plt.figure()
        self.figure.set_facecolor("none")
        self.canvas = FigureCanvas(self.figure)

        button_Send = QPushButton(self.fileName)
        button_Send.setFont(QFont('Arial', 15))
        button_Send.clicked.connect(self.on_button_Send_clicked)

        print("p1")
        self.plot()
        print("p2")

        layout.addWidget(self.canvas)
        layout.addWidget(button_Send)
        layout.addWidget(button_Exit)

        self.setLayout(layout)

    def plot(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_title("Graph : K vs Accuracy")
        ax.set_ylabel('Accuracy')
        ax.set_xlabel('Value Of K')

        if self.filePath!='':
            ax.plot(self.data[:,0],self.data[:,1], '*-')
        self.canvas.draw()

        # For Set Layout
    def setLayout(self, layout):
        print("s1")
        self.clearLayout()
        print("s2")
        QWidget.setLayout(self, layout)

    def clearLayout(self):
        if self.layout() is not None:
            old_layout = self.layout()
            for i in reversed(range(old_layout.count())):
                old_layout.itemAt(i).widget().setParent(None)
            import sip
            sip.delete(old_layout)


app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())