from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
from PySide6.QtCore import Qt
from Mainwindow import Ui_MainWindow
from AddRecipeWindow import Ui_AddRecipe
from MappingWindow import Ui_MappingWindow
from PasswordWidnow import Ui_PasswordWindow
from popup import Ui_popup
import toml

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

if __name__ == "__main__":
    app = QApplication()
    window = MyApp()
    window.show()
    app.exec()