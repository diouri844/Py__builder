from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QLineEdit,QFileDialog,QMessageBox,QComboBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os

class Config_Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Project setup ")
        self.setWindowIcon(QIcon("Images/icons8-manager-99.png"))
        self.background_color ="#FAFAFA"
        self.text_color = "#004268"
        #set window resaizbale attr to false :
        self.setFixedSize(500,700)
        self.move(250,0)
        # add widget : 
        # project name :
        self.project_name_label = QLabel(self)
        self.project_name_label.setText("Project Name :   ")
        self.project_name_entry = QLineEdit(self)
        #☺project folder :
        self.project_folder_label = QLabel(self)
        self.project_folder_label.setText("Project Folder :    ")
        self.project_folder_entry = QLineEdit(self)
        self.project_folder_entry.setReadOnly(True)
        self.project_folder_btn_select = QPushButton(self)
        self.project_folder_btn_select.setText("Select folder")
        self.project_folder_btn_select.clicked.connect(self.select_folder)
        #project type :
        self.project_type_label = QLabel(self)
        self.project_type_label.setText("Project Type :     ")
        self.project_type_liste = QComboBox(self)
        self.projcet_type_list_data = [
            "Desktop app Gui",
            "Desktop app console",
            "Web app"
        ]
        self.project_type_liste.addItems(self.projcet_type_list_data)
        self.project_type_liste.activated.connect(self.sub_liste_implement)
        #choice add files :
        self.project_type_meta_data = [
            ["Tkinter","PyQt5","Kivy","C#","JavaSwing","JavaFx"],
            ["Cpp","C","Java","Python","Go"],
            ["Html",'Css','Sass',"Js",'Ts']
        ]
        self.add_sup_files_label = QLabel(self)
        self.add_sup_files_label.setText("Add files to your project :   ")
        self.add_sup_files_liste = QComboBox(self)
        #self.add_sup_files_liste.addItems(self.project_type_meta_data[0])
        self.add_sup_files_liste.setEditable(False)
        #place widget in the main window :
        self.project_name_label.move(10,10)
        self.project_name_entry.move(20,40)
        self.project_folder_label.move(10,80)
        self.project_folder_entry.move(20,110)
        self.project_folder_btn_select.move(300,150)
        self.project_type_label.move(10,180)
        self.project_type_liste.move(20,210)
        self.add_sup_files_label.move(10,260)
        self.add_sup_files_liste.move(20,290)
        # add css style :
        self.setStyleSheet("""
        background-color:"#FAFAFA";
        padding:5px;
        """)
        self.project_name_label.setStyleSheet("""
        background-color:"#FAFAFA";
        color:"#004268";
        font-size:15px;
        """)
        self.project_name_entry.setStyleSheet("""
        font-size : 10px;
        width:350px;
        height:20px;
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
        self.project_folder_label.setStyleSheet("""
        background-color:"#FAFAFA";
        color:"#004268";
        font-size:15px;
        """)
        self.project_folder_entry.setStyleSheet("""
        font-size : 10px;
        width:350px;
        height:20px;
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
        self.project_folder_btn_select.setStyleSheet("""
        font-size : 12px;
        color:"#004268";
        border:1px solid #004268;
        border-radius: 5px;
        """)
        self.project_type_label.setStyleSheet("""
        background-color:"#FAFAFA";
        color:"#004268";
        font-size:15px;
        """)
        self.project_type_liste.setStyleSheet("""
        font-size : 10px;
        width:350px;
        height:20px;
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
        self.add_sup_files_label.setStyleSheet("""
        background-color:"#FAFAFA";
        color:"#004268";
        font-size:15px;
        """)
        self.add_sup_files_liste.setStyleSheet("""
        font-size : 10px;
        width:350px;
        height:20px;
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
    def sub_liste_implement(self):
        print("detected :)  ")
        return 
    def select_folder(self):
        # open select folder :
        path = os.path.expanduser("~")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec_():
            self.path = dlg.selectedFiles()[0]
            self.project_folder_entry.setText(self.path)
        return

    def start(self):
        self.show()
        return