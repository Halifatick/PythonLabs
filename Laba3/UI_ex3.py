# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 761, 511))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.file_open_action = QtWidgets.QAction(MainWindow)
        self.file_open_action.setObjectName("file_open_action")
        self.log_export_action = QtWidgets.QAction(MainWindow)
        self.log_export_action.setObjectName("log_export_action")
        self.log_add_action = QtWidgets.QAction(MainWindow)
        self.log_add_action.setObjectName("log_add_action")
        self.log_check_action = QtWidgets.QAction(MainWindow)
        self.log_check_action.setObjectName("log_check_action")
        self.menu.addAction(self.file_open_action)
        self.menu_2.addAction(self.log_export_action)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.log_add_action)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.log_check_action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лаба3_зад3"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "логи"))
        self.file_open_action.setText(_translate("MainWindow", "Открыть файлик"))
        self.log_export_action.setText(_translate("MainWindow", "Экспорируем..."))
        self.log_add_action.setText(_translate("MainWindow", "Закинуть в лог"))
        self.log_check_action.setText(_translate("MainWindow", "Вывести на экран логи"))
