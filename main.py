from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTableWidgetItem
from PySide6.QtCore import Qt, Signal, Slot, Qt, QTimer
from Mainwindow import Ui_MainWindow
from AddRecipeWindow import Ui_AddRecipe
from MappingWindow import Ui_MappingWindow
from PasswordWidnow import Ui_PasswordWindow
from RoboTeach import Ui_MainWindow as RoboTeachWindow
from popup import Ui_popup
import toml
import time
from multiprocessing import Process
from threading import Thread
import requests
import json
import csv
import pymelsec as plc
from pymelsec.constants import DT
from socket import socket, AF_INET, SOCK_STREAM

def lst_to_str(lst:list, reverse = False):
    str1 = ""
    if not reverse:
        for item in lst:
            my_int = int(bin(item.value), base=2)
            string = my_int.to_bytes((my_int.bit_length() + 7) // 8, "big").decode()
            if string != " ":
                str1 = string + str1
        return str1[::-1]

def send_dl2_data():
    print("Google")
    dl2 = socket(AF_INET, SOCK_STREAM)
    dl2.settimeout(0.5)
    # try:
    #     dl2.connect(("192.168.250.100", 5002))
    #     connectToDL2 = True
    # except Exception as e:
    #     print("Unable to Connect to DL2 -- ", e)
    #     connectToDL2 = False

    connectToDL2 = False

    plc_device = plc.Type3E(host="192.168.3.250", port=1202)
    try:
        plc_device.connect("192.168.3.250", port=1202)
        plc_is_connected = True
    except Exception as e:
        print(e)
        plc_is_connected = False

    while True:
        # print(connectToDL2)
        if connectToDL2:
            try:
                dl2.sendall(b"M0\r\n")
                data = dl2.recv(1024).decode()
                # print(data)
                height_1 = int(data[3:13])/10000
                height_2 = int(data[14:])/10000
                plc_device.batch_write("D6000", [height_1, height_2], DT.FLOAT)
                # print("Sending")
                connectToDL2 = True
            except Exception as e:
                print(e)

        if not connectToDL2:
            try:
                print("Trying to Reconnect")
                dl2.connect(("192.168.3.100", 1210))
                connectToDL2 = True
            except Exception as e:
                print("This is the error ", e)
                connectToDL2 = False

        if not plc_is_connected:
            try:
                plc_device.connect("192.168.3.250", port=1202)
            except Exception as e:
                print(e)
    

class Robo_teach_window(RoboTeachWindow, QMainWindow):
     
    dataSignal = Signal(dict)
    plc_signal = Signal(str)
    conn_event_handler = Signal(str)
    table_signal = Signal(str)

    play_list = []

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Setting up the variables
        self.runThread = True

        self.pushButton_5.clicked.connect(lambda : Thread(target=self.run).start())

        self.pushButton_2.clicked.connect(self.add_location_to_table)

        self.pushButton_4.clicked.connect(self.play_commands_A)
        
        self.pushButton_7.clicked.connect(self.play_commands_B)

        self.pushButton_8.clicked.connect(self.delete_row_data)

        self.pushButton_9.clicked.connect(self.save_data)

        self.dataSignal.connect(self.commandHandler)
        
        self.plc_signal.connect(self.command_handler_plc)
        
        self.spinBox.valueChanged.connect(self.set_location_table_A)

        self.spinBox_2.valueChanged.connect(self.set_location_table_B)

        self.pushButton_3.clicked.connect(self.add_location_to_table_A)
        
        self.pushButton_11.clicked.connect(self.add_location_to_table_B)

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        self.pushButton_5.click()

        # Setting up the initial row and column
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_table_A_and_B)
        self.timer.setSingleShot(True)
        self.timer.start(1000)

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
            
            with open("location_A.txt") as file:
                reader = csv.reader(file, delimiter=";")
                for row in reader:
                    self.tableWidget_2.setRowCount(self.tableWidget_2.rowCount()+1)
                    # self.spinBox.setValue(self.spinBox.value() + 1)
                    for i ,value in enumerate(row):
                        item = QTableWidgetItem(f"{value}")
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.tableWidget_2.setItem(self.tableWidget_2.rowCount()-1, i, item)
            
            with open("location_B.txt") as file:
                reader = csv.reader(file, delimiter=";")
                for index, row in enumerate(reader):
                    self.tableWidget_3.setRowCount(self.tableWidget_3.rowCount()+1)
                    # self.spinBox_2.setValue(self.spinBox_2.value() + 1)
                    for i ,value in enumerate(row):
                        item = QTableWidgetItem(f"{value}")
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.tableWidget_3.setItem(self.tableWidget_3.rowCount()-1, i, item)

        except Exception as e:
            print(e)

    def update_table_A_and_B(self):
        self.spinBox.setValue(self.tableWidget_2.rowCount())
        self.spinBox_2.setValue(self.tableWidget_3.rowCount())

    def set_location_table_A(self):
        print("Running")
        self.comboBox.clear()
        self.tableWidget_2.setRowCount(self.spinBox.value())
        for i in range(self.spinBox.value()):
            self.comboBox.addItem(f"Location {i}")
            item = QTableWidgetItem(f"{i}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget_2.setItem(i, 0, item)
    
    def set_location_table_B(self):
        self.comboBox_3.clear()
        self.tableWidget_3.setRowCount(self.spinBox_2.value())
        for i in range(self.spinBox_2.value()):
            self.comboBox_3.addItem(f"Location {i}")
            item = QTableWidgetItem(f"{i}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget_3.setItem(i, 0, item)

    def add_location_to_table_A(self):
        index = self.comboBox.currentIndex()
        try:
            x = float(self.label_2.text())
            y = float(self.label_4.text())
            z = float(self.label_8.text())
            t = float(self.label_10.text())
        except Exception as e:
            print(e)
            x=1.0
            y=2.0
            z=3.0
            t=4.0

        lst = [x, y, z, t]

        for i in range(1, self.tableWidget_2.columnCount()):
            item = QTableWidgetItem(f"{lst[i-1]}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget_2.setItem(index, i, item)
    
    def add_location_to_table_B(self):
        index = self.comboBox_3.currentIndex()
        try:
            x = float(self.label_2.text())
            y = float(self.label_4.text())
            z = float(self.label_8.text())
            t = float(self.label_10.text())
        except Exception as e:
            print(e)
            x=1.0
            y=2.0
            z=3.0
            t=4.0

        lst = [x, y, z, t]

        for i in range(1, self.tableWidget_3.columnCount()):
            item = QTableWidgetItem(f"{lst[i-1]}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget_3.setItem(index, i, item)

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

    def play_commands_A(self):
       self.play_pick_up()
       self.play_move_A()
    
    def play_commands_B(self):
        self.play_pick_up()
        self.play_move_B()
    
    def play_pick_up(self):
        lst = []
        for i in range(self.tableWidget.rowCount()):
            for col in range(0, self.tableWidget.columnCount()):
                item = float(self.tableWidget.item(i, col).text())
                lst.append(item)
            
            url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{lst[0]}, 'y':{lst[1]}, 'z':{lst[2]}, 't':{lst[3]}, 'spd':{lst[4]}" + "}"
            response = requests.get(url)
            time.sleep(lst[5])
            lst.clear()
        
    def play_move_A(self):
        row = int(self.lineEdit_2.text())
        x = float(self.tableWidget_2.item(row, 1).text())
        y = float(self.tableWidget_2.item(row, 2).text())
        z = float(self.tableWidget_2.item(row, 3).text())
        t = float(self.tableWidget_2.item(row, 4).text())

        url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{x}, 'y':{y}, 'z':{z}, 't':{t}, 'spd':{0.25}" + "}"
        response = requests.get(url)
        time.sleep(2)
        url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{x}, 'y':{y}, 'z':{z}, 't':{t-0.5}, 'spd':{0.5}" + "}"
        response = requests.get(url)
        print("opening")
        new_row = row + 1
        if row >= self.spinBox.value():
            new_row = 0
        self.lineEdit_2.setText(f"{new_row}")
    
    def play_move_B(self):
        row = int(self.lineEdit.text())
        x = float(self.tableWidget_3.item(row, 1).text())
        y = float(self.tableWidget_3.item(row, 2).text())
        z = float(self.tableWidget_3.item(row, 3).text())
        t = float(self.tableWidget_3.item(row, 4).text())

        url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{x}, 'y':{y}, 'z':{z}, 't':{t}, 'spd':{0.25}" + "}"
        response = requests.get(url)
        time.sleep(2)
        url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{x}, 'y':{y}, 'z':{z}, 't':{t-0.5}, 'spd':{0.5}" + "}"
        response = requests.get(url)
        print("opening")
        new_row = row + 1
        if new_row >= self.spinBox_2.value():
            new_row = 0
        self.lineEdit.setText(f"{row+1}")

    def save_data(self):
        lst = []
        for i in range(0, self.tableWidget.rowCount()):
            row_list = []
            for j in range(0, self.tableWidget.columnCount()):
                item = float(self.tableWidget.item(i, j).text())
                row_list.append(item)
            lst.append(row_list)
        
        lst_points_A = []
        for i in range(0, self.tableWidget_2.rowCount()):
            row_list = []
            for j in range(0, self.tableWidget_2.columnCount()):
                item = float(self.tableWidget_2.item(i, j).text())
                row_list.append(item)
            lst_points_A.append(row_list)
        
        lst_points_B = []
        for i in range(0, self.tableWidget_2.rowCount()):
            row_list = []
            for j in range(0, self.tableWidget_3.columnCount()):
                print(i, j)
                item = float(self.tableWidget_3.item(i, j).text())
                row_list.append(item)
            lst_points_B.append(row_list)

        try:
            # Saving the path details
            with open("Path.txt", "w+") as file:
                writer = csv.writer(file, delimiter=";", lineterminator="\n")
                for item in lst:
                    writer.writerow(item)

            # Saving the move details   
            with open("location_A.txt", "w+") as file:
                writer = csv.writer(file, delimiter=";", lineterminator="\n")
                for item in lst_points_A:
                    writer.writerow(item)
            
            with open("location_B.txt", "w+") as file:
                writer = csv.writer(file, delimiter=";", lineterminator="\n")
                for item in lst_points_B:
                    writer.writerow(item)
            
            self.popup.show_pop_up("Data Saved Successfully !!", "Success !!")
        except Exception as e:
            print(e)

    @Slot(dict)
    def commandHandler(self, data: dict):
        try:
            self.label_2.setText(f'{data["x"]}')
            self.label_4.setText(f'{data["y"]}')
            self.label_8.setText(f'{data["z"]}')
            self.label_10.setText(f'{data["t"]}')
        except Exception as e:
            ...

    @Slot(str)
    def command_handler_plc(self, command:str):
        command_split = command.split(":")
        if command_split[0] == "Command":
            self.label_13.setText(command_split[1])

    def run(self):
        # Connecting to plc
        plc_device  = plc.Type3E("192.168.3.250", port=1200)
        try:
            plc_device.connect("192.168.3.250", 1200)
            connected = True
            self.conn_event_handler.emit("PLC:Connected")

        except Exception as e:
            print(e)
            self.conn_event_handler.emit("PLC:Disconnected")
            connected = False

        while self.pushButton_5.isChecked():
            try:
                url = "http://" + "192.168.4.1" + "/js?json=" + "{'T':105}"
                response = requests.get(url, timeout=0.2)
                if response.status_code == 200:
                    data = response.text
                    self.conn_event_handler.emit("Robo:Connected")
                    try:
                        if data != '{"T":105}':
                            json_data = json.loads(data)
                            self.dataSignal.emit(json_data)
                    except Exception as e:
                        ...
                else:
                    self.conn_event_handler.emit("Robo:Disconnected")
            except Exception as e:
                print(e)
                self.conn_event_handler.emit("Robo:Disconnected")

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

            if not connected:
                try:
                    plc_device.connect("192.168.3.250", 1200)
                    connected = True
                except Exception as e:
                    print(e)
                    connected = False

            try:
                lvdt_value_1 : float = plc_device.batch_read("D5000", read_size=1, data_type=DT.FLOAT)[0].value
                lvdt_value_2 : float = plc_device.batch_read("D5002", read_size=1, data_type=DT.FLOAT)[0].value
                diff : float = plc_device.batch_read("D5004", read_size=1, data_type=DT.FLOAT)[0].value
                # print(lvdt_value_1.__round__(3), lvdt_value_2.__round__(3), diff.__round__(3))

                part_A = plc_device.batch_read("D5006", read_size=1, data_type=DT.UWORD)[0].value
                part_B = plc_device.batch_read("D5008", read_size=1, data_type=DT.UWORD)[0].value
                Ng = plc_device.batch_read("D5010", read_size=1, data_type=DT.UWORD)[0].value
                over_size = plc_device.batch_read("D5012", read_size=1, data_type=DT.UWORD)[0].value

                part_status = lst_to_str(plc_device.batch_read("D5014", read_size=10, data_type=DT.UWORD))

                self.plc_signal.emit(f"LVDT:{lvdt_value_1.__round__(3)}:{lvdt_value_2.__round__(3)}:{diff.__round__(3)}")
                self.plc_signal.emit(f"Counter:{part_A}:{part_B}:{Ng}:{over_size}")
                self.plc_signal.emit(f"PartStatus: {part_status}")

                command = plc_device.batch_read("D800", read_size=1, data_type=DT.UWORD)[0].value
                self.plc_signal.emit(f"Command:{command}")
                if command == 1:
                    self.play_commands_A()
                    plc_device.batch_write("D800", values=[0], data_type=DT.UWORD)
                if command == 2:
                    self.play_commands_B()
                    plc_device.batch_write("D800", values=[0], data_type=DT.UWORD)

            except Exception as e:
                print(e)

    def closeEvent(self, event):
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
    
    def showWindow(self):
        if not self.is_logged_in:
            self.show()
        else:
            self.close()

    def validate_password(self):
        with open("Config/user.toml", "r") as file:
            data = toml.load(file)

        if data["id"] == self.lineEdit.text():
            if data["password"] == self.lineEdit_2.text():
                self.is_logged_in = True
                self._popup_window.show_pop_up("Now You can Acess The Features", "Sucess !!")
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

        self.process = Process(target=send_dl2_data)
        self.process.start()

        # Setting up actions of the of the menubar
        self.actionAdd_Recipe.triggered.connect(self.add_recipe)
        self.actionExit.triggered.connect(lambda: self.close())
        self.actionMapping.triggered.connect(self.add_mapping)
        self.actionLogout.triggered.connect(self.logout_app)
        self.actionTeach_Robo.triggered.connect(self.open_robo_teach_window)

        # Registring the window
        self._window_add_recipe = AddRecipeWindow()
        self._window_add_mapping = Add_Mapping()
        self._window_password = Password_Window()
        self._pop_up_window = Window_Popup()
        self._window_robo_teach = Robo_teach_window()

        # Connecting the robo teach window with the mainwindow
        self._window_robo_teach.conn_event_handler.connect(self.connection_handler)
        self._window_robo_teach.plc_signal.connect(self.handle_plc_signal)
        self._window_robo_teach.table_signal.connect(self.makeTable)

        # Setting up logout actions
        self.actionLogout.setDisabled(True)

        # Setting up fullscreen
        # self.showMaximized()

    @Slot(str)
    def handle_plc_signal(self, command:str):
        # print(command)
        command_split = command.split(":")
        match command_split[0]:
            case "LVDT":
                self.label_2.setText(command_split[1])
                self.label_7.setText(command_split[2])
                self.label_11.setText(command_split[3])
            case "Counter":
                self.label_8.setText(command_split[1])
                self.label_9.setText(command_split[2])
                self.label_10.setText(command_split[3])
                self.label_12.setText(command_split[4])
            case "PartStatus":
                self.label_6.setText(command_split[1])

    def open_robo_teach_window(self):
        # self._window_password.showWindow()
        self._window_password.is_logged_in = True
        if self._window_password.is_logged_in:
            self._window_robo_teach.show()

    def add_recipe(self):
        self._window_password.showWindow()
        if self._window_password.is_logged_in:
            self._window_add_recipe.show()
            self.actionLogout.setDisabled(False)
    
    def add_mapping(self):
        self._window_password.showWindow()
        if self._window_password.is_logged_in:
            self._window_add_mapping.show()
            self.actionLogout.setDisabled(False)
 
    def logout_app(self):
        self._window_password.is_logged_in = False
        self.actionLogout.setDisabled(True)
    
    @Slot(str)
    def connection_handler(self, command:str):
        command_split = command.split(":")
        if command_split[0] == "PLC":
            if command_split[1] == "Connected":
                self.pushButton.setStyleSheet("background-color:green;border:3px dashed black;")
            elif command_split[1] == "Disconnected":
                self.pushButton.setStyleSheet("background-color:red;border:3px dashed black;")
        
        # This is for my commit
        if command_split[0] == "Robo":
            if command_split[1] == "Connected":
                self.pushButton_2.setStyleSheet("background-color:green;border:3px dashed black;")
            elif command_split[1] == "Disconnected":
                self.pushButton_2.setStyleSheet("background-color:red;border:3px dashed black;")

    @Slot(str)
    def makeTable(self, command:str):
        # print(command)
        command_split = command.split(":")
        match command_split[0]:
            case "A":
                if command_split[1] == "table":
                    self.tableWidget.setRowCount(int(command_split[2]))
                    self.tableWidget.setColumnCount(int(command_split[3]))
                
                if command_split[1] == "change":
                    item = QTableWidgetItem("X")
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.tableWidget.setItem(int(command_split[2]), int(command_split[3]), item)
                
                if command_split[2] == "reset":
                    self.tableWidget.clearContents()
            
            case "B":
                if command_split[1] == "table":
                    self.tableWidget_2.setRowCount(int(command_split[2]))
                    self.tableWidget_2.setColumnCount(int(command_split[3]))

                if command_split[1] == "change":
                    item = QTableWidgetItem("X")
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.tableWidget_2.setItem(int(command_split[2]), int(command_split[3]), item)

                if command_split[2] == "reset":
                    self.tableWidget_2.clearContents()

    def closeEvent(self, event):
        self._window_robo_teach.pushButton_5.setChecked(False)
        self.process.terminate()

if __name__ == "__main__":
    app = QApplication()
    window = MyApp()
    window.show()
    app.exec()