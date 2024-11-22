from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTableWidgetItem, QMessageBox
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

        self.spinBox.valueChanged.connect(self.create_table_move_location_A)

        self.spinBox_2.valueChanged.connect(self.create_table_move_location_A)

        self.spinBox_3.valueChanged.connect(self.create_table_move_location_B)

        self.spinBox_4.valueChanged.connect(self.create_table_move_location_B)

        self.pushButton_17.clicked.connect(self.set_orign_A)
        
        self.pushButton_19.clicked.connect(self.set_orign_B)

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # self.pushButton_5.click()

        self.tableWidget_2.itemChanged.connect(lambda: print("Item Changed"))

        # Setting up the initial row and column
        self.row_A = 0
        self.col_A = 0
        self.row_B = 0
        self.col_B = 0

        self.timer1 = QTimer()
        self.timer1.setSingleShot(True)
        self.timer1.setInterval(1000)
        self.timer1.timeout.connect(self.send_table_data)
        self.timer1.start()

        try:
            with open('Config/Data.toml', 'r') as file:
                data = toml.load(file)
                self.spinBox.setValue(data["A_Row"])
                self.spinBox_2.setValue(data["A_Col"])
                self.doubleSpinBox.setValue(data["A_Height"])
                self.doubleSpinBox_2.setValue(data["A_Width"])
                self.spinBox_3.setValue(data["B_Row"])
                self.spinBox_4.setValue(data["B_Col"])
                self.doubleSpinBox_3.setValue(data["B_Height"])
                self.doubleSpinBox_4.setValue(data["B_Width"])
                self.label_28.setText(f'{data["A_x_origin"]}')
                self.label_29.setText(f'{data["A_y_origin"]}')
                self.label_31.setText(f'{data["A_z_origin"]}')
                self.label_34.setText(f'{data["A_t_origin"]}')
                self.label_37.setText(f'{data["B_x_origin"]}')
                self.label_39.setText(f'{data["B_y_origin"]}')
                self.label_41.setText(f'{data["B_z_origin"]}')
                self.label_43.setText(f'{data["B_t_origin"]}')
                
                # Sending the table info to the MainWindow
                # self.table_signal.emit(f"A:table:{data['A_Row']}:{data['A_Col']}")
                # self.table_signal.emit(f"B:table:{data['B_Row']}:{data['B_Col']}")
                self.table_signal.emit(f"A:table:2:3")
                # print(data)
        except Exception as e:
            print("This is an error ->> ", e)


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

    def send_table_data(self):
        row_B = self.spinBox_3.value()
        col_B = self.spinBox_4.value()

        self.table_signal.emit(f"B:table:{row_B}:{col_B}")

        row_A = self.spinBox.value()
        col_A = self.spinBox_2.value()
        
        self.table_signal.emit(f"A:table:{row_A}:{col_A}")

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
        x_origin = float(self.label_28.text())
        y_origin = float(self.label_29.text())
        z_origin = float(self.label_31.text())
        t_origin = float(self.label_34.text())

        x_new = x_origin - self.col_A * self.doubleSpinBox_2.value()
        y_new = y_origin - self.row_A * self.doubleSpinBox.value() 
        url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{x_new}, 'y':{y_new}, 'z':{z_origin}, 't':{t_origin}, 'spd':{0.5}" + "}"
        response = requests.get(url)
        time.sleep(0.5)
        if self.col_A <= self.tableWidget_2.columnCount():
            item = QTableWidgetItem("X")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget_2.setItem(self.row_A,self.col_A, item)
            self.table_signal.emit(f"A:change:{self.row_A}:{self.col_A}")
            print(self.row_A, self.col_A)
            self.col_A= self.col_A + 1
            if self.col_A >= self.tableWidget_2.columnCount():
                self.col_A = 0
                self.row_A += 1
        else:
            self.col_A += 1
        
        if (self.row_A >= self.tableWidget_2.rowCount()):
            self.tableWidget_2.clearContents()
            self.row_A = 0
            self.col_A = 0
            self.tableWidget_2.emit("A:reset")
            
        url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{x_new}, 'y':{y_new}, 'z':{z_origin}, 't':{t_origin-0.5}, 'spd':{0.5}" + "}"
        response = requests.get(url)
        print("opening")
    
    def play_move_B(self):
        x_origin = float(self.label_37.text())
        y_origin = float(self.label_39.text())
        z_origin = float(self.label_41.text())
        t_origin = float(self.label_43.text())

        x_new = x_origin - self.col_B * self.doubleSpinBox_4.value()
        y_new = y_origin + self.row_B * self.doubleSpinBox_3.value() 
        url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{x_new}, 'y':{y_new}, 'z':{z_origin}, 't':{t_origin}, 'spd':{0.5}" + "}"
        response = requests.get(url)
        time.sleep(0.5)
        if self.col_B <= self.tableWidget_3.columnCount():
            item = QTableWidgetItem("X")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget_3.setItem(self.row_B, self.col_B, item)
            self.table_signal.emit(f"B:change:{self.row_B}:{self.col_B}")
            print(self.row_B, self.col_B)
            if self.col_B >= self.tableWidget_3.columnCount():
                self.col_B = 0
                self.row_B += 1
            else:
                self.col_B += 1

        if (self.row_B >= self.tableWidget_3.rowCount()):
            self.row_B = 0
            self.col_B = 0
            self.tableWidget_3.clearContents()
            self.table_signal.emit("B:reset")
        
        url = "http://" + "192.168.4.1" + "/js?json=" + "{" +f"'T':104, 'x':{x_new}, 'y':{y_new}, 'z':{z_origin}, 't':{t_origin-0.5}, 'spd':{0.5}" + "}"
        response = requests.get(url)
        print("opening")

    def save_data(self):
        lst = []
        for i in range(0, self.tableWidget.rowCount()):
            row_list = []
            for j in range(0, self.tableWidget.columnCount()):
                item = float(self.tableWidget.item(i, j).text())
                row_list.append(item)
            lst.append(row_list)
        
        config = {}

        config["A_Row"] = self.spinBox.value()
        config["A_Col"] = self.spinBox_2.value()
        config["A_Width"] = self.doubleSpinBox_2.value()
        config["A_Height"] = self.doubleSpinBox.value()
        config["A_x_origin"] = float(self.label_28.text())
        config["A_y_origin"] = float(self.label_29.text())
        config["A_z_origin"] = float(self.label_31.text())
        config["A_t_origin"] = float(self.label_34.text())

        config["B_Row"] = self.spinBox_3.value()
        config["B_Col"] = self.spinBox_4.value()
        config["B_Width"] = self.doubleSpinBox_4.value()
        config["B_Height"] = self.doubleSpinBox_3.value()
        config["B_x_origin"] = float(self.label_37.text())
        config["B_y_origin"] = float(self.label_39.text())
        config["B_z_origin"] = float(self.label_41.text())
        config["B_t_origin"] = float(self.label_43.text())

        try:
            # Saving the path details
            with open("Path.txt", "w+") as file:
                writer = csv.writer(file, delimiter=";", lineterminator="\n")
                for item in lst:
                    writer.writerow(item)

            # Saving the move details   
            with open("Config/Data.toml", "w+") as file:
                toml.dump(config, file)
            
            self.popup.show_pop_up("Data Saved Successfully !!", "Success !!")
        except Exception as e:
            print(e)
    
    def create_table_move_location_A(self):
        row = self.spinBox.value()
        col = self.spinBox_2.value()

        self.tableWidget_2.setRowCount(row)
        self.tableWidget_2.setColumnCount(col)

        self.table_signal.emit(f"A:table:{row}:{col}")
    
    def create_table_move_location_B(self):
        row = self.spinBox_3.value()
        col = self.spinBox_4.value()

        self.tableWidget_3.setRowCount(row)
        self.tableWidget_3.setColumnCount(col)
        self.table_signal.emit(f"B:table:{row}:{col}")

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

    def set_orign_A(self):
        x = float(self.label_2.text())
        y = float(self.label_4.text())
        z = float(self.label_8.text())
        t = float(self.label_10.text())

        self.label_28.setText(f"{x}")
        self.label_29.setText(f"{y}")
        self.label_31.setText(f"{z}")
        self.label_34.setText(f"{t}")
    
    def set_orign_B(self):
        x = float(self.label_2.text())
        y = float(self.label_4.text())
        z = float(self.label_8.text())
        t = float(self.label_10.text())

        self.label_37.setText(f"{x}")
        self.label_39.setText(f"{y}")
        self.label_41.setText(f"{z}")
        self.label_43.setText(f"{t}")

    def run(self):
        # Connecting to plc
        plc_device  = plc.Type3E("192.168.250.3", port=1200)
        try:
            plc_device.connect("192.168.250.3", 1200)
            connected = True
            self.conn_event_handler.emit("PLC:Connected")
        except Exception as e:
            print(e)
            self.conn_event_handler.emit("PLC:Disconnected")
            connected = False

        while self.pushButton_5.isChecked():
            try:
                url = "http://" + "192.168.4.1" + "/js?json=" + "{'T':105}"
                response = requests.get(url, timeout=2)
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
                    plc_device.connect("192.168.250.3", 1200)
                    connected = True
                except Exception as e:
                    print(e)
                    connected = False

            try:
                command = plc_device.batch_read("D800", read_size=1, data_type=DT.UWORD)[0].value
                self.plc_signal.emit(f"Command:{command}")
                if command == 1:
                    self.play_commands_A()
                    plc_device.batch_write("D800", values=[0], data_type=DT.UWORD)
                if command == 2:
                    self.play_commands_B()
                    plc_device.batch_write("D800", values=[0], data_type=DT.UWORD)
                
                lvdt_value_1 = plc_device.batch_read("D5000", read_size=1, data_type=DT.FLOAT)[0].value
                lvdt_value_2 = plc_device.batch_read("D5002", read_size=1, data_type=DT.FLOAT)[0].value
                diff = plc_device.batch_read("D5004", read_size=1, data_type=DT.FLOAT)[0].value

                part_A = plc_device.batch_read("D5006", read_size=1, data_type=DT.UWORD)[0].value
                part_B = plc_device.batch_read("D5008", read_size=1, data_type=DT.UWORD)[0].value
                Ng = plc_device.batch_read("D5010", read_size=1, data_type=DT.UWORD)[0].value


                self.plc_signal.emit(f"LVDT:{lvdt_value_1}:{lvdt_value_2}:{diff}")
                self.plc_signal.emit(f"Counter:{part_A}:{part_B}:{Ng}")

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

    def open_robo_teach_window(self):
        self._window_password.showWindow()
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
                self.pushButton.setStyleSheet("background-color:green;border:2px dashed black;")
            elif command_split[1] == "Disconnected":
                self.pushButton.setStyleSheet("background-color:red;border:2px dashed black;")
        
        if command_split[0] == "Robo":
            if command_split[1] == "Connected":
                self.pushButton.setStyleSheet("background-color:green;border:2px dashed black;")
            elif command_split[1] == "Disconnected":
                self.pushButton.setStyleSheet("background-color:red;border:2px dashed black;")

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

if __name__ == "__main__":
    app = QApplication()
    window = MyApp()
    window.show()
    app.exec()