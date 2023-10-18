import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from src.controller import controller_main_window as controller
from pathlib import Path

from src.view import window_superadmin
from src.view import window_user
from src.view import window_admin


class HandlerWindowLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(HandlerWindowLogin, self).__init__()
        self.window_client = None
        self.information_window = None
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(341, 296)
        self.setMinimumSize(QtCore.QSize(500, 470))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        path_to_images = Path(Path().cwd(), "pictures")
        print(path_to_images)

        icon = QtGui.QIcon()
        print(str(Path(path_to_images, "logo.png")))
        icon.addPixmap(QtGui.QPixmap(str(Path(path_to_images, "logo.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "background-color: qconicalgradient(cx:1, cy:0, angle:0,"
            " stop:0 rgba(0, 0, 0, 255), stop:1 rgba(100, 187, 250, 255));\n"
            "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("text-align: center;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(230, 170))
        self.frame.setMaximumSize(QtCore.QSize(800, 800))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setAcceptDrops(True)
        self.frame.setStyleSheet("background-color: rgb(70, 132, 176);\n"
                                 "width: 60%;\n"
                                 "margin-left: 30%;\n"
                                 "margin-right: 30%;\n"
                                 "border-radius: 12px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(-1, 10, 10, -1)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(2440, 1280))
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
                                 "text-align: center;\n"
                                 "color: rgb(0, 0, 255);height:40%;font-size:15vh;")
        self.label.setText("")
        pixmap = QtGui.QPixmap(str(Path(path_to_images, "logo2.png")))
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.line_login = QtWidgets.QLineEdit(self.frame)
        self.line_login.setClearButtonEnabled(True)
        self.line_login.setMaximumSize(QtCore.QSize(700, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_login.setFont(font)
        self.line_login.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "height:25%;\n"
                                      "border: 2px solid white;\n"
                                      "border-radius: 12px;\n"
                                      "font-family:\'Montserrat\';\n"
                                      "font-size:11pt")
        self.line_login.setText("")
        self.line_login.setAlignment(QtCore.Qt.AlignCenter)
        self.line_login.setPlaceholderText("Логин")
        self.line_login.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.line_login.setClearButtonEnabled(False)
        self.line_login.setObjectName("line_login")
        self.verticalLayout.addWidget(self.line_login)

        self.line_password = QtWidgets.QLineEdit(self.frame)
        self.line_password.setClearButtonEnabled(True)
        self.line_password.setMaximumSize(QtCore.QSize(700, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_password.setFont(font)
        self.line_password.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "height:25%;\n"
                                         "font-family:\'Montserrat\';\n"
                                         "font-size:11pt;\n"
                                         "border: 2px solid white;\n"
                                         "border-radius: 12px;")
        self.line_password.setText("")
        self.line_password.setPlaceholderText("Пароль")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setAlignment(QtCore.Qt.AlignCenter)
        self.line_password.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.line_password)

        self.hBox = QtWidgets.QHBoxLayout()
        self.radio_user = QtWidgets.QRadioButton('пользователь')
        self.radio_user.setMinimumSize(150, 10)
        self.radio_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radio_user.setChecked(True)
        self.radio_admin = QtWidgets.QRadioButton('админ')
        self.radio_admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hBox.addWidget(self.radio_user)
        self.hBox.addWidget(self.radio_admin)
        self.verticalLayout.addLayout(self.hBox)

        self.button_login = QtWidgets.QPushButton(self.frame)
        self.button_login.clicked.connect(self.button_login_press)
        self.button_login.setShortcut(QtGui.QKeySequence("Return"))  # нажата клавиша enter
        self.button_login.setMaximumSize(QtCore.QSize(700, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_login.setFont(font)
        self.button_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_login.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "height:25%;\n"
                                        "font-family:\'Montserrat\';\n"
                                        "font-size: 11pt;\n"
                                        "border: 2px solid white;\n"
                                        "border-radius: 12px;")
        self.button_login.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.button_login)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ДБ_Архив"))
        # self.label.setWhatsThis(
        #     _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.button_login.setText(_translate("MainWindow", "Войти"))

    def button_login_press(self):
        role = None
        if self.radio_user.isChecked():
            role = 'user'
        if self.radio_admin.isChecked():
            role = 'admin'
        input_login = self.line_login.text()
        input_password = self.line_password.text()

        if input_password == "":
            self.information_window = QtWidgets.QMessageBox.critical(self, "Ошибка ввода пароля", "Введите пароль!")
            return

        result_checking = controller.check_login(input_login, input_password, role)
        self.create_window(data_window=result_checking)

    def create_window(self, data_window: str):
        """
        method create window role authorized client or QMessageBox.critical with information about error login
        :param data_window: str
        :return:
        """
        if data_window == 'superAdmin':
            print("current = super admin")
            self.window_client = window_superadmin.WindowSuperAdmin()
            self.close()
        elif data_window == 'admin':
            print("current = admin")
            self.window_client = window_admin.WindowAdmin()
            self.close()
        elif data_window == 'user':
            print("current = user")
            self.window_client = window_user.WindowUser()
            self.close()
        else:
            self.clear_password_line()
            self.information_window = QtWidgets.QMessageBox.critical(self, "Ошибка ввода", data_window)

    def clear_password_line(self):
        self.line_password.setText('')
        self.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = HandlerWindowLogin()
    application.show()

    sys.exit(app.exec())
    # test_main()
