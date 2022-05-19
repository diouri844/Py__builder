# get started with GUI tools by PYQt5
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QLineEdit,QFileDialog,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Modules import Config_Window
import sys



class My_manager(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Pyqt5 Project Manager 1.0 ")
        self.setWindowIcon(QIcon("Images/icons8-manager-99.png"))
        self.background_color ="#FAFAFA"
        self.text_color = "#004268"
        #set window resaizbale attr to false :
        self.setFixedSize(1200,400)
        self.move(100,60)
        # add widget : 
        self.main_logo = QLabel(self)
        self.main_logo.setPixmap(QPixmap("Images/icons8-manager-99.png"))
        self.main_title = QLabel(self)
        self.main_title.setText("Create Your Project By click !")
        self.btn_start = QPushButton(self)
        self.btn_start.setText("Start Building Now")
        self.btn_start.clicked.connect(self.start)
        #place widget in the main window :
        self.main_logo.move(300,100)
        self.main_title.move(420,120)
        self.btn_start.move(680,200)
        # add css style :
        self.setStyleSheet("""
        background-color:"#FAFAFA";
        padding:5px;
        """)
        self.main_title.setStyleSheet("""
        background-color:"#FAFAFA";
        color:"#004268";
        font-size:30px;
        """)
        self.btn_start.setStyleSheet("""
        color:"#FAFAFA";
        background-color:"#004268";
        font-size:15px;
        padding:10px;
        border-radius: 15px;
        """)
    def start(self):
        self.config_window = Config_Window()
        self.config_window.start()
        return

if __name__ == "__main__":
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)
    my_instance = My_manager()
    my_instance.show()
    app.exec_()