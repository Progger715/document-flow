from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView

from src.view.widget import my_tree_widget

import src.controller.controller_main_window as controller


class TreeHierarchy(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.id_departments_for_delete = []
        self.departments_for_added = []
        self.depth_lvl = None
        self.list_hierarchy = []
        self.list_departments = []
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.treeWidget = my_tree_widget.MyTreeWidget()  # QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.init_tree_widget()

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.button_save = QtWidgets.QPushButton(self.frame_3)
        self.button_save.setFont(font)
        self.button_save.pressed.connect(self.button_save_press)
        self.button_save.setObjectName("button_save")

        self.button_add_row = QtWidgets.QPushButton(self.frame_3)
        self.button_add_row.setFont(font)
        self.button_add_row.pressed.connect(self.button_add_row_press)
        self.button_add_row.setObjectName("button_add_row")

        self.button_delte_row = QtWidgets.QPushButton(self.frame_3)
        self.button_delte_row.setFont(font)
        self.button_delte_row.pressed.connect(self.button_delete_row_press)
        self.button_delte_row.setObjectName("button_delete_row")

        self.horizontalLayout.addWidget(self.button_save)
        self.horizontalLayout.addWidget(self.button_add_row)
        self.horizontalLayout.addWidget(self.button_delte_row)

        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Номер отдела"))
        self.treeWidget.header().setResizeContentsPrecision(QHeaderView.ResizeToContents)
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Название отдела"))

        self.button_save.setText(_translate("MainWindow", "сохранить изменения"))
        self.button_add_row.setText(_translate("MainWindow", "добавить элемент"))
        self.button_delte_row.setText(_translate("MainWindow", "удалить элемент"))

    def button_save_press(self):
        for i in range(self.treeWidget.topLevelItemCount()):  # количество элементов верхнего уровня
            item = self.treeWidget.topLevelItem(i)  # элемент верхнего уровня, находящийся по индексу
            # print(item.text(0))  # текст элемента в указанном столбце
            self.__add_new_departments()
            self.__delete_departments()

            self.tree(item)
            # print("departments:\n", self.list_departments)
            # print(self.list_hierarchy)
            controller.save_hierarchy(self.list_hierarchy)
            controller.update_data_departments(self.list_departments)
            print("save success")

    def __add_new_departments(self):
        for item in self.departments_for_added:
            id_added_department = controller.add_department(name_department=item.text(1),
                                                            number_department=int(item.text(0)))
            item.setText(2, str(id_added_department))

    def __delete_departments(self):
        for id_department in self.id_departments_for_delete:
            controller.delete_department(id_department=int(id_department))

    def button_add_row_press(self):
        item_for_added = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_for_added.setFlags(
            QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        item_for_added.setText(0, "0")
        item_for_added.setText(1, "новое название")
        item_for_added.setText(2, "111")
        self.treeWidget.addTopLevelItem(item_for_added)
        self.departments_for_added.append(item_for_added)

    def button_delete_row_press(self):
        selected_elements = self.treeWidget.selectedItems()
        print(selected_elements, type(selected_elements))
        for element in selected_elements:
            element.removeChild(element)
            self.id_departments_for_delete.append(element.text(2))
            print(element.text(0), element.text(1))

    def tree(self, item):
        text = item.text(0)
        # print(f"{text}", end="\t")
        self.list_departments.append((item.text(0), item.text(1), int(item.text(2))))
        record_for_db = [0, 0]
        if item.parent() is not None:
            record_for_db[1] = item.parent().text(2)
            # print(f"\tparent: {item.parent().text(0)}", end="\t")
        else:
            record_for_db[1] = None
            # print(f"\tparent: null", end="\t")
        record_for_db[0] = item.text(2)
        self.list_hierarchy.append(record_for_db)
        # print("id = ", item.text(2))
        # print(record_for_db, "\n")
        count_children = item.childCount()
        for index_child in range(count_children):
            self.tree(item.child(index_child))

    def init_tree_widget(self):
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_0.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_2 = QtWidgets.QTreeWidgetItem(item_1)
        # item_2.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_2 = QtWidgets.QTreeWidgetItem(item_1)
        # item_2.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_2 = QtWidgets.QTreeWidgetItem(item_1)
        # item_2.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1.setFlags(
        #     QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsDragEnabled)
        hierarchy = controller.get_hierarchy()
        self.treeWidget.addTopLevelItem(
            hierarchy[1]["item"])  # элемент под 1-ым индексом всегда будет главным (так сохраняется в базе данных)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = TreeHierarchy()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())
