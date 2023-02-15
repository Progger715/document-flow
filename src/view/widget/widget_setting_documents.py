from PyQt5 import QtCore, QtGui, QtWidgets

from src.view.dialog_window import dialog_add_document
from src.controller import controller_main_window as controller


class WidgetDocuments(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.data_about_documents = None
        self.dialog_window = None
        self.setObjectName("MainWindow")
        self.resize(895, 605)
        self.setupUi()
        self.show()

    def setupUi(self):
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
        self.pushButton_home.clicked.connect(self.fill_in_table)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.clicked.connect(self.press_button_add_document)
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
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(877, 498))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 230, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 230, 154);\n"
                                       "border-radius: 10;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        # self.tableWidget.setRowCount(0)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
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
        self.pushButton_delete.setText(_translate("MainWindow", "удалить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Входящий №"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Исходящий №"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Исходящая дата"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Тип документа"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Дата загрузки"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Автор"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Связанные документы"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Скачать"))

    def press_button_add_document(self):
        print("pushed_button_add_document")
        self.dialog_window = dialog_add_document.DialogAddDocument(self)

    def press_button_refresh(self):
        self.data_about_documents = controller.get_about_documents()
        self.fill_in_table()

    def fill_in_table(self):
        # print("widget\n", self.data_about_documents)
        if self.data_about_documents is None:
            self.dialog_window = QtWidgets.QDialog()
            return
        self.tableWidget.setRowCount(len(self.data_about_documents))
        number_row = 0
        for row in self.data_about_documents:
            # print("row = ", row)
            self.tableWidget.setItem(number_row, 0, QtWidgets.QTableWidgetItem(row[1]))  # Установка имени
            self.tableWidget.setItem(number_row, 1, QtWidgets.QTableWidgetItem(row[2]))  # Установка входящего номера
            self.tableWidget.setItem(number_row, 2, QtWidgets.QTableWidgetItem(row[3]))  # Установка исходящего номера
            self.tableWidget.setItem(number_row, 3, QtWidgets.QTableWidgetItem(str(row[4])))  # Установка исходящей даты
            self.tableWidget.setItem(number_row, 4, QtWidgets.QTableWidgetItem(row[5]))  # Установка типа документа
            self.tableWidget.setItem(number_row, 5, QtWidgets.QTableWidgetItem(str(row[6])))  # Установка даты загрузки
            self.tableWidget.setItem(number_row, 6,
                                     QtWidgets.QTableWidgetItem("Иван Иванович Иванов"))  # Установка автора
            self.tableWidget.setItem(number_row, 7,
                                     QtWidgets.QTableWidgetItem(" "))  # Установка связанных документов

            button_downlad = QtWidgets.QPushButton(f"скачать")
            button_downlad.setStyleSheet("background-color: rgb(255, 210, 76);\n"
                                         "padding: 5;\n"
                                         "border-radius:5px;\n"
                                         "border: 1 solid black;\n"
                                         "")
            button_downlad.setObjectName(f"{row[0]}")
            button_downlad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            button_downlad.clicked.connect(
                lambda ch, id_document=row[0], name_file=row[1]: self.press_button_download(id_document, name_file))

            self.tableWidget.setCellWidget(number_row, 8, button_downlad)  # Установка кнопки скачать
            number_row += 1
        print("init table finished")

    def press_button_download(self, id_document: int, name_file: str):
        self.dialog_window = QtWidgets.QFileDialog()
        path_to_save = f"{self.dialog_window.getExistingDirectory()}/{name_file}"
        controller.download_document(id_document, path_to_save)


if __name__ == "__main__":
    import sys

    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = WidgetDocuments()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_()

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = WidgetDocuments()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())
