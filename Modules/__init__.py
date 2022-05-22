from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QLineEdit,QFileDialog,QMessageBox,QComboBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os

#------------------- functions -----------------------------------

def create_dir(path_dir,dir_name):
    try:
        os.mkdir(path=path_dir+"/"+str(dir_name), mode=777)
    except Exception as e:
        print("[Create Folder Error ] : "+str(e))
    return path_dir+"/"+str(dir_name)
def create_file_in_folder(path_dir,file_liste):
    pass
    return



def get_default_file(index):
    liste_resultats = [
        ['main.py','class.py'],
        ['main.java','extern_class.java'],
        ['main.c','biblio.c','biblio.h'],
        ['main.cpp',"biblio.cpp","biblio.hpp"],
        ['main.go','extern_services.go'],
        ['index.html','index.css','Using Javascript','Using Typescript','Using Bootstrap5']
    ]
    return liste_resultats[index]



#------------------------------------------------------------------





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
            "Python",
            "Java",
            "C",
            "Cpp",
            "Golang",
            "Web app (Html,Css,Js/Ts)"
        ]
        self.project_type_liste.addItems(self.projcet_type_list_data)
        #choice config  :
        self.add_user_config_label = QLabel(self)
        self.add_user_config_label.setText(" Project config  :   ")
        self.user_config_default = QPushButton(self)
        self.user_config_default.setText("Default config ")
        self.user_config_default.clicked.connect(self.configuration_default)
        self.user_config_personalised = QPushButton(self)
        self.user_config_personalised.setText("user config ")
        self.user_config_personalised.clicked.connect(self.personalized_config)
        #place widget in the main window :
        self.project_name_label.move(10,10)
        self.project_name_entry.move(20,40)
        self.project_folder_label.move(10,80)
        self.project_folder_entry.move(20,110)
        self.project_folder_btn_select.move(300,150)
        self.project_type_label.move(10,180)
        self.project_type_liste.move(20,210)
        self.add_user_config_label.move(10,260)
        self.user_config_default.move(20,290)
        self.user_config_personalised.move(150,290)
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
        self.add_user_config_label.setStyleSheet("""
        background-color:"#FAFAFA";
        color:"#004268";
        font-size:15px;
        """)
        self.user_config_default.setStyleSheet("""
        color:"#FAFAFA";
        background-color:"#004268";
        font-size:15px;
        border-radius: 5px;
        """)
        self.user_config_personalised.setStyleSheet("""
        font-size : 15px;
        color:"#004268";
        border:1px solid #004268;
        border-radius: 5px;
        """)
    def select_folder(self):
        # open select folder :
        path = os.path.expanduser("~")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec_():
            self.path = dlg.selectedFiles()[0]
            self.project_folder_entry.setText(self.path)
        return
    def configuration_default(self):
        #test all info :
        if len(self.project_folder_entry.text())!=0 and len(self.project_name_entry.text())!=0:
            print("Default config :)    ")
            project_name = self.project_name_entry.text()
            user_dir = self.project_folder_entry.text()
            project_type = self.project_type_liste.currentText()
            filse_to_create = get_default_file(self.projcet_type_list_data.index(project_type))
            created_folder = create_dir(user_dir, project_name)
            print(filse_to_create)
        return
    def personalized_config(self):
        if len(self.project_folder_entry.text())!=0 and len(self.project_name_entry.text())!=0:
            print("user config :)    ")
            user_dir = self.project_folder_entry.text()
            project_name = self.project_name_entry.text()
            created_folder = create_dir(user_dir, project_name)
            print("Project folder :  "+str(created_folder))
        return
    def start(self):
        self.show()
        return