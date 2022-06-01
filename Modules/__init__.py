from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QLineEdit,QFileDialog,QMessageBox,QComboBox,QListWidget
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
    for element in file_liste:
        try:
            current_file = open(str(path_dir)+"/"+str(element), mode="w") 
        except Exception as e:
            print("[file genrator error ]:  "+str(e))
        finally:
            current_file.close()
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

class popup(QWidget):
    def __init__(self,path_folder,parent_window):
        QWidget.__init__(self)
        self.project_path_dir = path_folder
        self.previous_task_window = parent_window
        self.setWindowTitle("Files setup ")
        self.setWindowIcon(QIcon("Images/icons8-manager-99.png"))
        self.background_color ="#FAFAFA"
        self.text_color = "#004268"
        self.setFixedSize(350,450)
        self.move(290,150)
        #add widget :
        self.title = QLabel(self)
        self.title.setText("Add files :   ")
        self.files_name_entry = QLineEdit(self)
        self.file_add_btn = QPushButton(self)
        self.file_add_btn.setText("Add !")
        self.file_add_btn.clicked.connect(self.add_to_setup)
        self.bnt_start_user_config = QPushButton(self)
        self.bnt_start_user_config.setText("Start !")
        self.bnt_start_user_config.clicked.connect(self.start_user_config)
        # filse liste :
        self.files_liste_to_add = QListWidget(self)
        # place widget in the main window :
        self.title.move(20,20)
        self.files_name_entry.move(40,55)
        self.file_add_btn.move(258,95)
        self.files_liste_to_add.move(40,130)
        self.bnt_start_user_config.move(250,350)
        # add css style :
        self.setStyleSheet("""
        background-color:"#FAFAFA";
        padding:5px;
        """)
        self.title.setStyleSheet("""
        background-color:"#FAFAFA";
        color:"#004268";
        font-size:15px;
        """)
        self.files_name_entry.setStyleSheet("""
        font-size : 12px;
        width:250px;
        height:15px;
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
        self.file_add_btn.setStyleSheet("""
        font-size : 12px;
        color:"#004268";
        border:1px solid #004268;
        border-radius: 5px;
        """)
        self.files_liste_to_add.setStyleSheet("""
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
        self.bnt_start_user_config.setStyleSheet("""
        font-size : 12px;
        color:"#FAFAFA";
        background-color:"#004268";
        border:1px solid #FAFAFA;
        border-radius: 5px;
        """)
    def add_to_setup(self):
        if len(self.files_name_entry.text())!=0:
            file_name= self.files_name_entry.text()
            self.user_folder_liste = [self.files_liste_to_add.item(i).text() for i in range(self.files_liste_to_add.count())]
            files_arr = file_name.split('/')
            if files_arr[0]=='':
                if not file_name in self.user_folder_liste:
                    self.files_liste_to_add.addItem(file_name)
                    self.files_name_entry.setText("")
                else:
                    self.files_name_entry.setText("")
            else:
                if not file_name in self.user_folder_liste:
                    self.files_liste_to_add.addItem(file_name)
                    self.files_name_entry.setText("")
                else:
                    self.files_name_entry.setText("")
        return
    def start_user_config(self):
        self.user_folder_liste = [self.files_liste_to_add.item(i).text() for i in range(self.files_liste_to_add.count())]
        folders_path_glo = []
        files_glo = []
        for element in self.user_folder_liste:
            custom_element = element.replace('/','',1)
            folder_to_create = []
            file_to_create = []
            #detect if custom_element is a files or a folder :
            for item in custom_element.split('/')[0:]:
                type_item = ''
                if len(item.split('.'))>1:
                    if not item in file_to_create:
                        file_to_create.append(custom_element)
                else:
                    if not item in folder_to_create:
                        folder_to_create.append(item)
                folders_path_glo.append(folder_to_create)
                files_glo.append(file_to_create)
        count = 0
        for folder in folders_path_glo:
            path_current = self.project_path_dir
            for item in folder:
                try:
                    os.mkdir(path_current+"/"+str(item),mode=777)
                except  Exception as e:
                    print("[ Error ] :  ( "+str(item)+" ) :=> "+str(e))
                path_current = path_current +"/"+str(item)
            try:
                path_current = self.project_path_dir +"/"+str(folder[0])
            except Exception as e:
                print("[ Error ]:  "+str(e))
            finally:
                for file_li in files_glo:
                        try:
                            current_file = open(self.project_path_dir+"/"+str(file_li[0]), mode="w") 
                            current_file.close()
                        except Exception as e:
                            print("[file genrator ]:  "+str(e))
                count += 1
        # folder setup completed : 
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Project Created  ! ") 
        msg.setInformativeText("Open project in vscode ?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgopen_vscode)
        msg.exec_()
        return
    def msgopen_vscode(self,i):
        if i.text() == "OK":
            #open folder in vscode:
            open_command = "code "+str(self.project_path_dir)
            os.system(open_command)
        self.close()
        self.previous_task_window.close()
        return
    def start(self):
        self.show()
        return





#-----------------------------------------------------------------

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
            project_name = self.project_name_entry.text()
            user_dir = self.project_folder_entry.text()
            project_type = self.project_type_liste.currentText()
            self.filse_to_create = get_default_file(self.projcet_type_list_data.index(project_type))
            self.created_folder = create_dir(user_dir, project_name)
            #create all files :
            create_file_in_folder(self.created_folder,self.filse_to_create)
            #popup ask if you want to open project in your vscode :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Project Created  ! ") 
            msg.setInformativeText("Open project in vscode ?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.buttonClicked.connect(self.msgopen_vscode)
            msg.exec_()
        return
    def msgopen_vscode(self,i):
        if i.text() == "OK":
            #open folder in explorer:
            open_command = "code "+str(self.created_folder)
            os.system(open_command)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Project Created  ! ") 
            msg.setInformativeText("Open Folder in explorer ?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.buttonClicked.connect(self.msgshow_folder)
            msg.exec_()
        return
    def msgshow_folder(self,i):
        if i.text() == "OK":
            os.startfile(self.created_folder)
        return
    def personalized_config(self):
        if len(self.project_folder_entry.text())!=0 and len(self.project_name_entry.text())!=0:
            user_dir = self.project_folder_entry.text()
            project_name = self.project_name_entry.text()
            self.created_folder = create_dir(user_dir, project_name)
            #popup to add files :
            self.my_files_setup = popup(self.created_folder,self)
            self.my_files_setup.start()
        return
    def start(self):
        self.show()
        return