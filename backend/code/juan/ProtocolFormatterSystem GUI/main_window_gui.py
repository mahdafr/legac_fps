# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 782)
        MainWindow.setMinimumSize(QtCore.QSize(257, 92))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1342, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.captureWindow = QtWidgets.QDockWidget(MainWindow)
        self.captureWindow.setObjectName("captureWindow")
        self.dockWidgetContents_53 = QtWidgets.QWidget()
        self.dockWidgetContents_53.setObjectName("dockWidgetContents_53")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_53)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_3.setObjectName("label_3")
        self.captureWindow_list = QtWidgets.QListWidget(self.dockWidgetContents_53)
        self.captureWindow_list.setGeometry(QtCore.QRect(10, 30, 771, 551))
        self.captureWindow_list.setObjectName("captureWindow_list")
        self.captureWindow.setWidget(self.dockWidgetContents_53)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.captureWindow)
        self.FormatterWindow = QtWidgets.QDockWidget(MainWindow)
        self.FormatterWindow.setObjectName("FormatterWindow")
        self.dockWidgetContents_60 = QtWidgets.QWidget()
        self.dockWidgetContents_60.setObjectName("dockWidgetContents_60")
        self.label_8 = QtWidgets.QLabel(self.dockWidgetContents_60)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 241, 21))
        self.label_8.setObjectName("label_8")
        self.FormatterWindow_formatterList = QtWidgets.QListWidget(self.dockWidgetContents_60)
        self.FormatterWindow_formatterList.setGeometry(QtCore.QRect(10, 30, 371, 191))
        self.FormatterWindow_formatterList.setObjectName("FormatterWindow_formatterList")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.dockWidgetContents_60)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 240, 371, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.FormatterWindow_ProtocolName = QtWidgets.QTextEdit(self.horizontalLayoutWidget_4)
        self.FormatterWindow_ProtocolName.setObjectName("FormatterWindow_ProtocolName")
        self.horizontalLayout_3.addWidget(self.FormatterWindow_ProtocolName)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.FormatterWindow_filterName = QtWidgets.QTextEdit(self.horizontalLayoutWidget_4)
        self.FormatterWindow_filterName.setObjectName("FormatterWindow_filterName")
        self.horizontalLayout_3.addWidget(self.FormatterWindow_filterName)
        self.FormatterWindow_ruleList = QtWidgets.QListWidget(self.dockWidgetContents_60)
        self.FormatterWindow_ruleList.setGeometry(QtCore.QRect(10, 280, 371, 131))
        self.FormatterWindow_ruleList.setObjectName("FormatterWindow_ruleList")
        self.FormatterWindow_actionList = QtWidgets.QListWidget(self.dockWidgetContents_60)
        self.FormatterWindow_actionList.setGeometry(QtCore.QRect(10, 460, 371, 91))
        self.FormatterWindow_actionList.setObjectName("FormatterWindow_actionList")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.dockWidgetContents_60)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 560, 371, 32))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FormatterWindow_createRule = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.FormatterWindow_createRule.setObjectName("FormatterWindow_createRule")
        self.horizontalLayout_2.addWidget(self.FormatterWindow_createRule)
        self.FormatterWindow_deleteRule = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.FormatterWindow_deleteRule.setObjectName("FormatterWindow_deleteRule")
        self.horizontalLayout_2.addWidget(self.FormatterWindow_deleteRule)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.dockWidgetContents_60)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 420, 371, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.textEdit_4 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_5)
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_4.addWidget(self.textEdit_4)
        self.FormatterWindow.setWidget(self.dockWidgetContents_60)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.FormatterWindow)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.modeOfOperation_output = QtWidgets.QTextEdit(self.dockWidgetContents)
        self.modeOfOperation_output.setGeometry(QtCore.QRect(1210, 10, 121, 31))
        self.modeOfOperation_output.setObjectName("modeOfOperation_output")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(1080, 20, 121, 20))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label_4.setObjectName("label_4")
        self.Filter_Bar_input = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.Filter_Bar_input.setGeometry(QtCore.QRect(50, 10, 781, 31))
        self.Filter_Bar_input.setObjectName("Filter_Bar_input")
        self.Filter_Bar_Button = QtWidgets.QPushButton(self.dockWidgetContents)
        self.Filter_Bar_Button.setGeometry(QtCore.QRect(840, 10, 71, 31))
        self.Filter_Bar_Button.setObjectName("Filter_Bar_Button")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.label_9 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_10.setGeometry(QtCore.QRect(110, 20, 111, 16))
        self.label_10.setObjectName("label_10")
        self.Edit_Window_PacketNumber = QtWidgets.QTextEdit(self.dockWidgetContents_3)
        self.Edit_Window_PacketNumber.setGeometry(QtCore.QRect(60, 10, 41, 31))
        self.Edit_Window_PacketNumber.setObjectName("Edit_Window_PacketNumber")
        self.Edit_Window_PacketNumber2 = QtWidgets.QTextEdit(self.dockWidgetContents_3)
        self.Edit_Window_PacketNumber2.setGeometry(QtCore.QRect(230, 10, 41, 31))
        self.Edit_Window_PacketNumber2.setObjectName("Edit_Window_PacketNumber2")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_2.setObjectName("label_2")
        self.Edit_Window_FiledList = QtWidgets.QListWidget(self.dockWidgetContents_3)
        self.Edit_Window_FiledList.setGeometry(QtCore.QRect(10, 70, 261, 191))
        self.Edit_Window_FiledList.setObjectName("Edit_Window_FiledList")
        self.Edit_Window_filedAnnotation = QtWidgets.QTextEdit(self.dockWidgetContents_3)
        self.Edit_Window_filedAnnotation.setGeometry(QtCore.QRect(280, 150, 101, 31))
        self.Edit_Window_filedAnnotation.setObjectName("Edit_Window_filedAnnotation")
        self.Edit_Window_changeValueButton = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.Edit_Window_changeValueButton.setGeometry(QtCore.QRect(280, 100, 101, 32))
        self.Edit_Window_changeValueButton.setObjectName("Edit_Window_changeValueButton")
        self.Edit_Window_filedValue = QtWidgets.QTextEdit(self.dockWidgetContents_3)
        self.Edit_Window_filedValue.setGeometry(QtCore.QRect(280, 70, 104, 31))
        self.Edit_Window_filedValue.setObjectName("Edit_Window_filedValue")
        self.label_12 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_12.setGeometry(QtCore.QRect(280, 50, 41, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_13.setGeometry(QtCore.QRect(280, 130, 61, 16))
        self.label_13.setObjectName("label_13")
        self.Edit_Window_AnnotateButton = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.Edit_Window_AnnotateButton.setGeometry(QtCore.QRect(280, 180, 101, 32))
        self.Edit_Window_AnnotateButton.setObjectName("Edit_Window_AnnotateButton")
        self.label_14 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_14.setGeometry(QtCore.QRect(280, 210, 41, 16))
        self.label_14.setObjectName("label_14")
        self.Edit_Window_hideFiledButton = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.Edit_Window_hideFiledButton.setGeometry(QtCore.QRect(280, 230, 101, 32))
        self.Edit_Window_hideFiledButton.setObjectName("Edit_Window_hideFiledButton")
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionRestore = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRestore.setIcon(icon2)
        self.actionRestore.setObjectName("actionRestore")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName("actionClose")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon4)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon5)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon6)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon7)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon8)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFilter = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icons/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilter.setIcon(icon9)
        self.actionFilter.setObjectName("actionFilter")
        self.actionEditor = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Icons/editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditor.setIcon(icon10)
        self.actionEditor.setObjectName("actionEditor")
        self.actionScript = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Icons/script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScript.setIcon(icon11)
        self.actionScript.setObjectName("actionScript")
        self.actionHook = QtWidgets.QAction(MainWindow)
        self.actionHook.setObjectName("actionHook")
        self.actionComand_Line = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Icons/command.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionComand_Line.setIcon(icon12)
        self.actionComand_Line.setObjectName("actionComand_Line")
        self.actionHistorical_Copy = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Icons/historical.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistorical_Copy.setIcon(icon13)
        self.actionHistorical_Copy.setObjectName("actionHistorical_Copy")
        self.actionUser_Manual = QtWidgets.QAction(MainWindow)
        self.actionUser_Manual.setObjectName("actionUser_Manual")
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionRestore)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPaste)
        self.menuWindow.addAction(self.actionFilter)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionEditor)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionScript)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionHook)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionComand_Line)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionHistorical_Copy)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionFilter)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_File.setTitle(_translate("MainWindow", "&File "))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.label_3.setText(_translate("MainWindow", "Capture File"))
        self.label_8.setText(_translate("MainWindow", "Formatter List"))
        self.label_5.setText(_translate("MainWindow", "Rule for"))
        self.label_6.setText(_translate("MainWindow", "Based on"))
        self.FormatterWindow_createRule.setText(_translate("MainWindow", "Create Rule"))
        self.FormatterWindow_deleteRule.setText(_translate("MainWindow", "Delete Rule"))
        self.label_7.setText(_translate("MainWindow", "Construction of New Rule with"))
        self.label.setText(_translate("MainWindow", "Mode of Operation:"))
        self.label_4.setText(_translate("MainWindow", "Filter"))
        self.Filter_Bar_Button.setText(_translate("MainWindow", "Fiter"))
        self.label_9.setText(_translate("MainWindow", "Packet"))
        self.label_10.setText(_translate("MainWindow", "Content of Packet"))
        self.label_2.setText(_translate("MainWindow", "Name Filed"))
        self.Edit_Window_changeValueButton.setText(_translate("MainWindow", "Hide Filed"))
        self.label_12.setText(_translate("MainWindow", "Value"))
        self.label_13.setText(_translate("MainWindow", "Annotate"))
        self.Edit_Window_AnnotateButton.setText(_translate("MainWindow", "Annotate"))
        self.label_14.setText(_translate("MainWindow", "Hide"))
        self.Edit_Window_hideFiledButton.setText(_translate("MainWindow", "Hide Field"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionRestore.setText(_translate("MainWindow", "Restore"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionFilter.setText(_translate("MainWindow", "Filter"))
        self.actionEditor.setText(_translate("MainWindow", "Editor"))
        self.actionScript.setText(_translate("MainWindow", "Script"))
        self.actionHook.setText(_translate("MainWindow", "Hook"))
        self.actionComand_Line.setText(_translate("MainWindow", "Comand Line"))
        self.actionHistorical_Copy.setText(_translate("MainWindow", "Historical Copy"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))