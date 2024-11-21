from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTableWidgetItem
from PySide6.QtCore import Qt, Signal, Slot, Qt, QThread, QProcess
from Mainwindow import Ui_MainWindow
from AddRecipeWindow import Ui_AddRecipe
from MappingWindow import Ui_MappingWindow
from PasswordWidnow import Ui_PasswordWindow
from RoboTeach import Ui_MainWindow as RoboTeachWindow
from popup import Ui_popup
import toml
import time
from threading import Thread
import requests
import json
import csv
import pymelsec as plc
from pymelsec.constants import DT

class Robo_teach_window(RoboTeachWindow, QMainWindow):
     
    dataSignal = Signal(dict)
    plc_signal = Signal(int)

    play_list = []

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Setting up the variables
        self.runThread = True

        self.pushButton_5.clicked.connect(lambda : Thread(target=self.run).start())

        self.pushButton_2.clicked.connect(self.add_location_to_table)

        self.pushButton_4.clicked.connect(self.play_commands)

        self.pushButton_8.clicked.connect(self.delete_row_data)

        self.pushButton_9.clicked.connect(self.save_table)

        self.dataSignal.connect(self.commandHandler)
        
        self.plc_signal.connect(self.command_handler_plc)

        self.spinBox.valueChanged.connect(self.create_table_move_location_A)

        self.spinBox_2.valueChanged.connect(self.create_table_move_location_A)

        self.spinBox_3.valueChanged.connect(self.create_table_move_location_B)

        self.spinBox_4.valueChanged.connect(self.create_table_move_location_B)

        self.setFixedSize(self.width()+100, self.height()+100)

        # Regeistring popup
        self.popup = Window_Popup()

        try:
            with open("Path.txt") as file:
                reader = csv.reader(file, delimiter=";")
                for row in reader:
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                    for i ,value in enumerate(row):
                        item = QTableWidgetItem(f"{value}")
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.tableWidget.setItem(self.tableWidget.rowCount()-1, i, item)
        except Exception as e:
            print(e)

    def delete_row_data(self):
        selected_indices = self.tableWidget.selectedIndexes()
        if len(selected_indices) > 1:
            self.popup.show_pop_up("Please Select Only One Index", "Error!!")
        else:
            row = selected_indices[0].row()
            self.tableWidget.removeRow(row)

    def add_location_to_table(self):
        x = float(self.label_2.text())
        y = float(self.label_4.text())
        z = float(self.label_8.text())
        t = float(self.label_10.text())
        speed = 0.5
        delay = 0.5

        no_of_rows = self.tableWidget.rowCount() + 1
        self.tableWidget.setRowCount(no_of_rows)

        lst = [x, y, z, t, speed, delay]

        for key, i in enumerate(lst):
            item = QTableWidgetItem(f"{i}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setItem(no_of_rows-1, key, item)

    def play_commands(self):
        lst = []
        for i in range(self.tableWidget.rowCount()):
            for col in range(0, self.tableWidget.columnCount()):
                item = float(self.tableWidget.item(i, col).text())
                lst.append(item)
            
            url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{lst[0]}, 'y':{lst[1]}, 'z':{lst[2]}, 't':{lst[3]}, 'spd':{lst[4]}" + "}"
            response = requests.get(url)
            time.sleep(lst[5])
            lst.clear()
        
    def save_table(self):
        lst = []
        for i in range(0, self.tableWidget.rowCount()):
            row_list = []
            for j in range(0, self.tableWidget.columnCount()):
                item = float(self.tableWidget.item(i, j).text())
                row_list.append(item)
            lst.append(row_list)
        
        print(lst)

        with open("Path.txt", "w+") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            for item in lst:
                writer.writerow(item)
    
    def create_table_move_location_A(self):
        row = self.spinBox.value()
        col = self.spinBox_2.value()

        self.tableWidget_2.setRowCount(row)
        self.tableWidget_2.setColumnCount(col)
    
    def create_table_move_location_B(self):
        row = self.spinBox_3.value()
        col = self.spinBox_4.value()

        self.tableWidget_3.setRowCount(row)
        self.tableWidget_3.setColumnCount(col)

    @Slot(dict)
    def commandHandler(self, data: dict):
        try:
            self.label_2.setText(f'{data["x"]}')
            self.label_4.setText(f'{data["y"]}')
            self.label_8.setText(f'{data["z"]}')
            self.label_10.setText(f'{data["t"]}')
        except Exception as e:
            ...
    
    @Slot(int)
    def command_handler_plc(self, command:int):
        self.label_13.setText(command)

    def run(self):
        # Connecting to plc
        plc_device  = plc.Type3E("192.168.250.3", port=1200)
        try:
            plc_device.connect("192.168.250.3", 1200)
            connected = True
        except Exception as e:
            print(e)
            connected = False

        while self.pushButton_5.isChecked():
            url = "http://" + "192.168.4.1" + "/js?json=" + "{'T':105}"
            response = requests.get(url)
            data = response.text
            try:
                if data != '{"T":105}':
                    json_data = json.loads(data)
                    self.dataSignal.emit(json_data)
            except Exception as e:
                ...

            if self.pushButton.isChecked():
                url = "http://" + "192.168.4.1" + "/js?json=" + "{'T':210, 'cmd':1}"
                response = requests.get(url)
                self.pushButton.setChecked(False)
            
            if self.pushButton_6.isChecked():
                url = "http://" + "192.168.4.1" + "/js?json=" + "{'T':210, 'cmd':0}"
                response = requests.get(url)
                self.pushButton_6.setChecked(False)

            if self.pushButton_10.isChecked():
                url = "http://" + "192.168.4.1" + "/js?json=" + "{'T':100}"
                response = requests.get(url)
                self.pushButton_10.setChecked(False)

            # if not connected:
            #     try:
            #         plc_device.connect("192.168.250.3", 1200)
            #         connected = True
            #     except Exception as e:
            #         print(e)
            #         connected = False

            # command = plc_device.batch_read("D800", read_size=1, data_type=DT.UWORD)[0].value
            # self.plc_signal.emit(command)
            # if command == 1:
            #     self.play_commands()
            #     plc_device.batch_write("D800", values=[0], data_type=DT.UWORD)

    def closeEvent(self, event):
        self.pushButton_5.setChecked(False)
        return super().closeEvent(event)


class Window_Popup(Ui_popup, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        # Setting up close action
        self.pushButton.clicked.connect(lambda : self.close())
    
    def show_pop_up(self, message:str, title:str):
        self.setWindowTitle(title)
        self.label.setText(message)
        self.show()

class Password_Window(Ui_PasswordWindow, QWidget):
    is_logged_in = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(309, 238)

        # setting up ui
        self.tabWidget_4.tabBar().hide()
        self.tabWidget_4.setCurrentIndex(0)

        # Show password in password input widgets
        self.checkBox.clicked.connect(self.show_password)

        # Password Change Window
        self.pushButton_3.clicked.connect(lambda : self.tabWidget_4.setCurrentIndex(1))
        self.pushButton_5.clicked.connect(lambda : self.tabWidget_4.setCurrentIndex(0))
        
        # Setting up actions
        self.pushButton.clicked.connect(self.validate_password)
        self.pushButton_4.clicked.connect(self.change_password)

        # Registring popup
        self._popup_window = Window_Popup()
    
    def show_password(self):
        if self.checkBox.isChecked():
            self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
    
    def showEvent(self, event):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit.setFocus()
        return super().showEvent(event)
    
    def showWindow(self):
        if not self.is_logged_in:
            self.show()

    def validate_password(self):
        with open("Config/user.toml", "r") as file:
            data = toml.load(file)

        if data["id"] == self.lineEdit.text():
            if data["password"] == self.lineEdit_2.text():
                self.is_logged_in = True
                self.close()
            else:
                self._popup_window.show_pop_up("Wrong Id or Password !!!", "Error !!!")
        else:
            self._popup_window.show_pop_up("Wrong Id or Password !!!", "Error !!!")

    def change_password(self):
        with open("Config/user.toml", "r") as file:
            data = toml.load(file)

        if self.lineEdit_3.text() == data["password"]:
            if self.lineEdit_4.text() == self.lineEdit_5.text():
                data["password"] = self.lineEdit_4.text()
                print(data)
                try:
                    with open("Config/user.toml", "w+") as file:
                        toml.dump(data, file)
                except Exception as e:
                    print(e)

                self._popup_window.show_pop_up("Password Changed Successfully", "Success !!!")
            else:
                self._popup_window.show_pop_up("New Password Does Not Match !!!", "Error !!!")
        else:
            self._popup_window.show_pop_up("Please Check Your Old Password !!!", "Error !!!")

class Add_Mapping(Ui_MappingWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(self.height(), self.width())

        # Regestring popup
        self._popup_window = Window_Popup()

class AddRecipeWindow(Ui_AddRecipe, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(self.width(), self.height())

        # Regesring popups
        self._popup_window = Window_Popup()
        
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Setting up actions of the of the menubar
        self.actionAdd_Recipe.triggered.connect(self.add_recipe)
        self.actionExit.triggered.connect(lambda: self.close())
        self.actionMapping.triggered.connect(self.add_mapping)
        self.actionLogout.triggered.connect(self.logout_app)

        # Registring the window
        self._window_add_recipe = AddRecipeWindow()
        self._window_add_mapping = Add_Mapping()
        self._window_password = Password_Window()
        self._pop_up_window = Window_Popup()

        # Setting up logout actions
        self.actionLogout.setDisabled(True)

        # Setting up fullscreen
        self.showMaximized()

    def add_recipe(self):
        self._window_password.show()
        if self._window_password.is_logged_in:
            self._window_add_recipe.show()
            self.actionLogout.setDisabled(False)
    
    def add_mapping(self):
        self._window_password.show()
        if self._window_password.is_logged_in:
            self._window_add_mapping.show()
            self.actionLogout.setDisabled(False)

    def logout_app(self):
        self._window_password.is_logged_in = False
        self.actionLogout.setDisabled(True)

if __name__ == "__main__":
    app = QApplication()
    window = Robo_teach_window()
    window.show()
    app.exec()