from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path

from src.view.widget import widget_setting_admins
from src.view.widget import widget_setting_documents
from src.view.widget import widget_setting_users
from src.view.widget import widget_setting_departments
from src.view import window_login


class WindowSuperAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowSuperAdmin, self).__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1110, 706)
        self.setMinimumSize(900, 706)
        path_to_images = Path(Path().cwd(), "pictures")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str(Path(path_to_images, "logo.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: rgb(146, 180, 236);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_head = QtWidgets.QFrame(self.centralwidget)
        self.frame_head.setStyleSheet("padding: 0;")
        self.frame_head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_head.setObjectName("frame_head")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_head)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_data = QtWidgets.QFrame(self.frame_head)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        self.frame_data.setFont(font)
        self.frame_data.setStyleSheet("")
        self.frame_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_data.setObjectName("frame_data")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_data)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(520, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_departament = QtWidgets.QLabel(self.frame_data)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_departament.setFont(font)
        self.label_departament.setObjectName("label_departament")
        self.horizontalLayout_3.addWidget(self.label_departament)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        self.button_logout = QtWidgets.QPushButton(self.frame_data)
        self.button_logout.clicked.connect(self.logout)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_logout.setFont(font)
        self.button_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_logout.setStyleSheet("padding: 5;\n"
                                         "border-radius:5px;\n"
                                         "border: 1 solid black;\n"
                                         "")
        self.button_logout.setObjectName("button_logout")
        self.horizontalLayout_3.addWidget(self.button_logout)
        self.verticalLayout.addWidget(self.frame_data)

        self.frame_selection_mode = QtWidgets.QFrame(self.frame_head)
        self.frame_selection_mode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_selection_mode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_selection_mode.setObjectName("frame_selection_mode")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_selection_mode)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_mode = QtWidgets.QLabel(self.frame_selection_mode)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_mode.setFont(font)
        self.label_mode.setStyleSheet("")
        self.label_mode.setObjectName("label_mode")
        self.horizontalLayout_2.addWidget(self.label_mode)

        self.button_mode_setting_documents = QtWidgets.QPushButton(self.frame_selection_mode)
        self.button_mode_setting_documents.pressed.connect(self.set_0_page_documents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_mode_setting_documents.sizePolicy().hasHeightForWidth())
        self.button_mode_setting_documents.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_setting_documents.setFont(font)
        self.button_mode_setting_documents.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_mode_setting_documents.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                                         "padding: 5;\n"
                                                         "border-radius:5px;\n"
                                                         "border: 1 solid black;\n"
                                                         "")
        self.button_mode_setting_documents.setObjectName("button_mode_documents")
        self.horizontalLayout_2.addWidget(self.button_mode_setting_documents)

        self.button_mode_setting_user = QtWidgets.QPushButton(self.frame_selection_mode)
        self.button_mode_setting_user.pressed.connect(self.set_2_page_users)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_setting_user.setFont(font)
        self.button_mode_setting_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_mode_setting_user.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                                    "padding: 5;\n"
                                                    "border-radius:5px;\n"
                                                    "border: 1 solid black;\n"
                                                    "")
        self.button_mode_setting_user.setObjectName("button_mode_setting_user")
        self.horizontalLayout_2.addWidget(self.button_mode_setting_user)

        self.button_mode_setting_admin = QtWidgets.QPushButton(self.frame_selection_mode)
        self.button_mode_setting_admin.pressed.connect(self.set_1_page_admin)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_setting_admin.setFont(font)
        self.button_mode_setting_admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_mode_setting_admin.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                                     "padding: 5;\n"
                                                     "border-radius:5px;\n"
                                                     "border: 1 solid black;\n"
                                                     "")
        self.button_mode_setting_admin.setObjectName("button_mode_setting_admin")
        self.horizontalLayout_2.addWidget(self.button_mode_setting_admin)

        self.button_mode_setting_hierarchy = QtWidgets.QPushButton(self.frame_selection_mode)
        self.button_mode_setting_hierarchy.pressed.connect(self.set_3_page_hierarchy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_mode_setting_hierarchy.sizePolicy().hasHeightForWidth())
        self.button_mode_setting_hierarchy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_setting_hierarchy.setFont(font)
        self.button_mode_setting_hierarchy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_mode_setting_hierarchy.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                                         "padding: 5;\n"
                                                         "border-radius:5px;\n"
                                                         "border: 1 solid black;\n"
                                                         "")
        self.button_mode_setting_hierarchy.setObjectName("button_mode_setting_hierarchy")
        self.horizontalLayout_2.addWidget(self.button_mode_setting_hierarchy)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_selection_mode)

        self.verticalLayout_3.addWidget(self.frame_head)
        self.frame_body = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.frame_body.sizePolicy().hasHeightForWidth())
        self.frame_body.setSizePolicy(sizePolicy)
        self.frame_body.setStyleSheet("padding: 0px;\n"
                                      "margin: 0px;\n")
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_body)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_body)
        self.stackedWidget.acceptDrops()
        self.stackedWidget.setObjectName("stackedWidget")

        self.widget_settings_documents = widget_setting_documents.WidgetDocuments()
        self.stackedWidget.addWidget(self.widget_settings_documents)

        self.widget_settings_users = widget_setting_admins.WidgetSettingUsers()
        self.stackedWidget.addWidget(self.widget_settings_users)

        self.widget_settings_admins = widget_setting_users.WidgetSettingUser()
        self.stackedWidget.addWidget(self.widget_settings_admins)

        self.treeWidget = widget_setting_departments.TreeHierarchy()
        self.stackedWidget.addWidget(self.treeWidget)

        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_3.addWidget(self.frame_body)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Documents (Super Admin mode)"))
        self.label_departament.setText(_translate("MainWindow", "SUPER ADMIN"))
        self.button_logout.setText(_translate("MainWindow", "выйти"))
        self.label_mode.setText(_translate("MainWindow", "Режим работы:"))

        self.button_mode_setting_documents.setText(_translate("MainWindow", "настройка документов"))
        self.button_mode_setting_user.setText(_translate("MainWindow", "настройка пользователей"))
        self.button_mode_setting_admin.setText(_translate("MainWindow", "настройка админов"))
        self.button_mode_setting_hierarchy.setText(_translate("MainWindow", "настройка иерархии"))

    def set_0_page_documents(self):  # correct
        self.stackedWidget.setCurrentIndex(0)

    def set_1_page_admin(self):
        self.stackedWidget.setCurrentIndex(1)

    def set_2_page_users(self):
        self.stackedWidget.setCurrentIndex(2)

    def set_3_page_hierarchy(self):  # correct
        self.stackedWidget.setCurrentIndex(3)

    def logout(self):
        self.login = window_login.HandlerWindowLogin()
        self.login.show()
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = WindowSuperAdmin()
    sys.exit(app.exec_())
