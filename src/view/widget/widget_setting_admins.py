from PyQt5 import QtCore, QtGui, QtWidgets

from src.view.dialog_window import dialog_add_admin
from src.controller import controller_main_window as controller
from src.view.widget.my_table_widget_item import MyTableWidgetItem
from src.view.dialog_window import dialog_edit_admin
from src.view.dialog_window import dialog_select_period_registration


class WidgetSettingUsers(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.data_about_users = None
        self.dialog_window = None
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(895, 605)

        self.centralwidget = QtWidgets.QWidget(self)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: rgb(146, 180, 236);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_body = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_body.sizePolicy().hasHeightForWidth())
        self.frame_body.setSizePolicy(sizePolicy)
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_body)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_function = QtWidgets.QFrame(self.frame_body)
        self.frame_function.setStyleSheet("")
        self.frame_function.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_function.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_function.setObjectName("frame_function")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_function)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_home = QtWidgets.QPushButton(self.frame_function)
        self.pushButton_home.clicked.connect(self.press_button_home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_home.sizePolicy().hasHeightForWidth())
        self.pushButton_home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_home.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                           "padding: 5;\n"
                                           "border-radius:5px;\n"
                                           "border: 1 solid black;\n"
                                           "")
        self.pushButton_home.setObjectName("pushButton_home")
        self.horizontalLayout.addWidget(self.pushButton_home)

        self.pushButton_refresh = QtWidgets.QPushButton(self.frame_function)
        self.pushButton_refresh.clicked.connect(self.press_button_refresh)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_refresh.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                              "padding: 5;\n"
                                              "border-radius:5px;\n"
                                              "border: 1 solid black;\n"
                                              "")
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        self.line_edit_search = QtWidgets.QLineEdit(self.frame_function)
        self.line_edit_search.setPlaceholderText("введите запрос")
        self.line_edit_search.setToolTip("поле для поиска по таблице. По умолчанию поиск производится по всем полям")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_search.sizePolicy().hasHeightForWidth())
        self.line_edit_search.setSizePolicy(sizePolicy)
        self.line_edit_search.setMinimumSize(QtCore.QSize(150, 27))
        self.line_edit_search.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-radius:5px;")
        self.line_edit_search.setObjectName("lineEdit_search")
        self.horizontalLayout.addWidget(self.line_edit_search)

        self.pushButton_find = QtWidgets.QPushButton(self.frame_function)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_find.sizePolicy().hasHeightForWidth())
        self.pushButton_find.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_find.clicked.connect(self.press_button_search_admins)
        self.pushButton_find.setFont(font)
        self.pushButton_find.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_find.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                           "padding: 5;\n"
                                           "border-radius:5px;\n"
                                           "border: 1 solid black;\n"
                                           "")
        self.pushButton_find.setObjectName("pushButton_find")
        self.horizontalLayout.addWidget(self.pushButton_find)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.pushButton_period_search = QtWidgets.QPushButton(self.frame_function)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_period_search.sizePolicy().hasHeightForWidth())
        self.pushButton_period_search.clicked.connect(self.press_button_period)
        self.pushButton_period_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setBold(True)
        font.setPointSize(10)
        self.pushButton_period_search.setFont(font)
        self.pushButton_period_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_period_search.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                                    "padding: 5;\n"
                                                    "border-radius:5px;\n"
                                                    "border: 1 solid black;\n"
                                                    "")
        self.pushButton_period_search.setObjectName("pushButton_period_search")
        self.horizontalLayout.addWidget(self.pushButton_period_search, 0, QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.pushButton_add = QtWidgets.QPushButton(self.frame_function)
        self.pushButton_add.clicked.connect(self.press_button_add_admin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_add.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                          "padding: 5;\n"
                                          "border-radius:5px;\n"
                                          "border: 1 solid black;\n"
                                          "")
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)

        self.pushButton_edit = QtWidgets.QPushButton(self.frame_function)
        self.pushButton_edit.clicked.connect(self.press_button_edit_admin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_edit.sizePolicy().hasHeightForWidth())
        self.pushButton_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_edit.setFont(font)
        self.pushButton_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_edit.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                           "padding: 5;\n"
                                           "border-radius:5px;\n"
                                           "border: 1 solid black;\n"
                                           "")
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.horizontalLayout.addWidget(self.pushButton_edit)

        self.pushButton_delete = QtWidgets.QPushButton(self.frame_function)
        self.pushButton_delete.clicked.connect(self.press_button_delete)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_delete.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                             "padding: 5;\n"
                                             "border-radius:5px;\n"
                                             "border: 1 solid black;\n"
                                             "")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout.addWidget(self.pushButton_delete)
        self.verticalLayout_2.addWidget(self.frame_function)

        self.tableWidget = QtWidgets.QTableWidget(self.frame_body)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(877, 498))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.verticalScrollBar().setSingleStep(3)
        self.tableWidget.horizontalScrollBar().setSingleStep(3)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 230, 154);\n"
                                       "border-radius: 10;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout.addWidget(self.frame_body, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.press_button_refresh()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_home.setText(_translate("MainWindow", "главная"))
        self.pushButton_refresh.setText(_translate("MainWindow", "обновить"))
        self.pushButton_find.setText(_translate("MainWindow", "искать"))
        self.pushButton_period_search.setText(_translate("MainWindow", "период"))
        self.pushButton_add.setText(_translate("MainWindow", "добавить"))
        self.pushButton_edit.setText(_translate("MainWindow", "редактировать"))
        self.pushButton_delete.setText(_translate("MainWindow", "актив/деактив"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Логин"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Дата регистрации"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Роль"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Деактивирован"))

    def press_button_add_admin(self):
        self.dialog_window = dialog_add_admin.DialogWidgetAddAdmin(self)

    def press_button_refresh(self):
        self.pushButton_period_search.setText("период")
        self.data_about_users = controller.get_data_about_admins()
        self.fill_in_table(self.data_about_users)

    def press_button_home(self):
        self.pushButton_period_search.setText("период")
        self.fill_in_table(self.data_about_users)

    def fill_in_table(self, data_about_users):
        if data_about_users is None:
            return False
        if len(data_about_users) == 0:
            return False
        self.tableWidget.setRowCount(len(data_about_users))
        number_row = 0
        for row in data_about_users:
            name_item = MyTableWidgetItem(row.last_name)
            name_item.set_additional_data(int(row.id))  # Установка id

            self.tableWidget.setItem(number_row, 0, name_item)  # Установка фамилии
            self.tableWidget.setItem(number_row, 1, QtWidgets.QTableWidgetItem(row.name))  # Установка имени
            self.tableWidget.setItem(number_row, 2, QtWidgets.QTableWidgetItem(row.patronymic))  # Установка отчества
            self.tableWidget.setItem(number_row, 3, QtWidgets.QTableWidgetItem(row.login))  # Установка логина
            self.tableWidget.setItem(number_row, 4,
                                     QtWidgets.QTableWidgetItem(str(row.date_creating)))  # Установка даты регистрации

            role = "superAdmin" if row.super_admin_flag == True else "admin"
            self.tableWidget.setItem(number_row, 5, QtWidgets.QTableWidgetItem(role))  # Установка роли
            status_active = "" if row.active else "Деактивирован"
            self.tableWidget.setItem(number_row, 6, QtWidgets.QTableWidgetItem(status_active))  # Уст. статуса деакитива

            number_row += 1
        return True

    def press_button_delete(self):
        items = self.tableWidget.selectedItems()
        if len(items) != 7:
            self.dialog_window = QtWidgets.QMessageBox().warning(self, "Изменение статуса активности администратора",
                                                                 "Для изменения статуса активности администратора "
                                                                 "выделите всю строку (строка станет белой), щелкнув "
                                                                 "по номеру строки (крайний левый стоблец).")
            return

        if items[5].text() == "superAdmin":
            self.dialog_window = QtWidgets.QMessageBox().warning(self, "Попытка деактивации супер администратора",
                                                                 f'Невозможно деактивировать супер администратора!')
            return
        id_admin_for_delete = items[0].get_additional_data()
        controller.change_activation_status_admin(id_admin_for_delete)
        if items[6].text() == "":
            title = "Деактивация администратора"
            message = "успешно деактивирован"
        else:
            title = "Активация администратора"
            message = "успешно активирован"
        self.dialog_window = QtWidgets.QMessageBox()
        self.dialog_window.information(self, title,
                                       f'Администратор "{items[0].text()} {items[1].text()} {items[2].text()}" '
                                       f'{message}.')
        self.press_button_refresh()

    def press_button_edit_admin(self):
        items = self.tableWidget.selectedItems()
        if len(items) != 7:
            self.dialog_window = QtWidgets.QMessageBox().warning(self, "Редактирование администратора",
                                                                 "Для редактирования администратора выделите всю строку"
                                                                 " (строка станет белой), щелкнув по номеру строки "
                                                                 "(крайний левый стоблец).")
            return
        id_admin = items[0].get_additional_data()
        self.dialog_window = dialog_edit_admin.DialogWidgetEditAdmin(main_window=self, last_name=items[0].text(),
                                                                     name=items[1].text(),
                                                                     patronymic=items[2].text(),
                                                                     login=items[3].text(), id_admin=id_admin)

    def press_button_search_admins(self):
        self.pushButton_period_search.setText("период")
        self.result_searching = controller.search_admins(self.line_edit_search.text())

        if type(self.result_searching) != list:
            QtWidgets.QMessageBox().critical(self, "Ошибка поиска", f"В результате запроса возникла ошибка\n"
                                                                    f"([ERROR]{self.result_searching})")
            return
        flag_result = self.fill_in_table(self.result_searching)
        if not flag_result:
            QtWidgets.QMessageBox().information(self, "Результат поиска", f'По запросу "{self.line_edit_search.text()}"'
                                                                          f' не найдено результатов')

    def press_button_period(self):
        self.dialog_window = dialog_select_period_registration.DialogSelectPeriodRegistration(self, "admin")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = WidgetSettingUsers()
    sys.exit(app.exec_())
