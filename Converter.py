import os 

os.system("pyside6-uic UI_Files/Mainwindow.ui -o Mainwindow.py")
os.system("pyside6-uic UI_Files/AddRecipeWindow.ui -o AddRecipeWindow.py")
os.system("pyside6-uic UI_Files/MappingWindow.ui -o MappingWindow.py")
os.system("pyside6-uic UI_Files/passwordWindow.ui -o PasswordWidnow.py")
os.system("pyside6-uic UI_Files/RoboTeach.ui -o RoboTeach.py")
os.system("pyside6-uic UI_Files/popup.ui -o popup.py")
os.system("pyside6-rcc UI_Files/assets.qrc -o assets_rc.py")