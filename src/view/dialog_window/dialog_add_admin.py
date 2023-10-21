from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QButtonGroup
from src.controller import controller_main_window as controller


class DialogWidgetAddAdmin(QDialog):
    def __init__(self, main_window):
        QDialog.__init__(self)
        self.dialog_window = None
        self.setModal(True)
        self.main_window = main_window
        self.setWindowTitle("Добавление админа")
        self.show()
        self.setupUi()

    def setupUi(self):
        self.show()
        self.setObjectName("Dialog_add_user")
        self.resize(550, 250)
        self.setMinimumSize(QtCore.QSize(320, 250))
        # self.setMaximumSize(QtCore.QSize(400, 380))
        self.setStyleSheet("background-color: rgb(146, 180, 236);")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setStyleSheet("")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.formLayout = QtWidgets.QFormLayout(self.main_frame)
        self.formLayout.setObjectName("formLayout")
        self.label_last_name = QtWidgets.QLabel(self.main_frame)

        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        style_for_line_edit = "border: 2px solid;\n" \
                              "border-color: rgb(255, 230, 154);\n" \
                              "border-radius: 5px;\n" \
                              "\n"

        self.label_last_name.setFont(font)
        self.label_last_name.setObjectName("label_last_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_last_name)

        self.lineEdit_last_name = QtWidgets.QLineEdit(self.main_frame)
        self.lineEdit_last_name.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit_last_name.setFont(font)
        self.lineEdit_last_name.setStyleSheet(style_for_line_edit)
        self.lineEdit_last_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_last_name)

        self.lineEdit_name = QtWidgets.QLineEdit(self.main_frame)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet(style_for_line_edit)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)

        self.label_patronymic = QtWidgets.QLabel(self.main_frame)
        self.label_patronymic.setFont(font)
        self.label_patronymic.setObjectName("label_patronymic")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_patronymic)

        self.lineEdit_patronymic = QtWidgets.QLineEdit(self.main_frame)
        self.lineEdit_patronymic.setObjectName("lineEdit_patronymic")
        self.lineEdit_patronymic.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_patronymic.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit_patronymic.setFont(font)
        self.lineEdit_patronymic.setStyleSheet(style_for_line_edit)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_patronymic)

        self.spacer = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, self.spacer)

        self.label_login = QtWidgets.QLabel(self.main_frame)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_login)

        self.lineEdit_login = QtWidgets.QLineEdit(self.main_frame)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_login.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_login.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setStyleSheet(style_for_line_edit)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_login)

        self.label_password = QtWidgets.QLabel(self.main_frame)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_password)

        self.lineEdit_password = QtWidgets.QLineEdit(self.main_frame)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet(style_for_line_edit)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)

        self.label_name = QtWidgets.QLabel(self.main_frame)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.verticalLayout.addWidget(self.main_frame)

        self.pushButton_save = QtWidgets.QPushButton(self)
        self.pushButton_save.pressed.connect(self.push_save)
        self.pushButton_save.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_save.setFont(font)
        self.pushButton_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_save.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                           "border-radius: 5px;\n"
                                           "\n"
                                           "")
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)

        self.pushButton_cancel = QtWidgets.QPushButton(self)
        self.pushButton_cancel.pressed.connect(self.push_cancel)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cancel.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                             "border-radius: 5px;\n"
                                             "\n"
                                             "")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.verticalLayout.addWidget(self.pushButton_cancel)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Добавление администратора")
        self.label_last_name.setText(_translate("Dialog_add_user", "Фамилия:"))
        self.label_patronymic.setText(_translate("Dialog_add_user", "Отчество:"))
        self.label_login.setText(_translate("Dialog_add_user", "Логин:"))
        self.label_password.setText(_translate("Dialog_add_user", "Пароль:"))
        self.label_name.setText(_translate("Dialog_add_user", "Имя:"))
        self.pushButton_save.setText(_translate("Dialog_add_user", "Сохранить"))
        self.pushButton_cancel.setText(_translate("Dialog_add_user", "Отмена"))

    def push_save(self):
        last_name = self.lineEdit_last_name.text()
        name = self.lineEdit_name.text()
        patronymic = self.lineEdit_patronymic.text()
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()
        try:
            controller.add_admin_in_database(last_name, name, patronymic, login, password)
            self.main_window.press_button_refresh()
            self.dialog_window = QtWidgets.QMessageBox().information(self, "Добавление администратора",
                                                                     f'Администратор "{last_name} {name} {patronymic}" '
                                                                     f'успешно добавлен в базу.')
            self.close()
        except Exception as ex:
            self.dialog_window = QtWidgets.QMessageBox().warning(self, "Добавление администратора",
                                                                 "Для добавления администратора заполните все поля! ")
            print("[ERROR] Не заполнены все поля\t", ex)

    def push_cancel(self):
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog_add_user = QtWidgets.QWidget()
    Dialog_add_user.show()

    Dialog_add_user.setWindowTitle("TRGGFFG")
    # print(Dialog_add_user.windowTitle())

    ui = DialogWidgetAddAdmin(Dialog_add_user)

    sys.exit(app.exec_())
