# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Sun May 26 18:08:45 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(945, 723)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/assets/img/logos/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background: #eee;\n"
"background-image: url(:/img/assets/img/logos/logo_transparent.png);\n"
"background-repeat: no-repeat;\n"
"background-position: bottom left;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.event_log = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.event_log.sizePolicy().hasHeightForWidth())
        self.event_log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.event_log.setFont(font)
        self.event_log.setReadOnly(True)
        self.event_log.setBackgroundVisible(False)
        self.event_log.setObjectName("event_log")
        self.verticalLayout_2.addWidget(self.event_log)
        self.chart_container = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.chart_container.sizePolicy().hasHeightForWidth())
        self.chart_container.setSizePolicy(sizePolicy)
        self.chart_container.setObjectName("chart_container")
        self.verticalLayout_2.addWidget(self.chart_container)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.execve_count = QtWidgets.QLineEdit(self.centralwidget)
        self.execve_count.setReadOnly(True)
        self.execve_count.setObjectName("execve_count")
        self.gridLayout_4.addWidget(self.execve_count, 4, 1, 1, 1)
        self.exit_count = QtWidgets.QLineEdit(self.centralwidget)
        self.exit_count.setReadOnly(True)
        self.exit_count.setObjectName("exit_count")
        self.gridLayout_4.addWidget(self.exit_count, 5, 1, 1, 1)
        self.syscall_count = QtWidgets.QLineEdit(self.centralwidget)
        self.syscall_count.setReadOnly(True)
        self.syscall_count.setObjectName("syscall_count")
        self.gridLayout_4.addWidget(self.syscall_count, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.monitoring_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.monitoring_radio.setEnabled(False)
        self.monitoring_radio.setStyleSheet("color:black;")
        self.monitoring_radio.setCheckable(True)
        self.monitoring_radio.setObjectName("monitoring_radio")
        self.horizontalLayout.addWidget(self.monitoring_radio)
        self.not_monitoring_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.not_monitoring_radio.setEnabled(False)
        self.not_monitoring_radio.setStyleSheet("color:black;")
        self.not_monitoring_radio.setCheckable(True)
        self.not_monitoring_radio.setChecked(True)
        self.not_monitoring_radio.setObjectName("not_monitoring_radio")
        self.horizontalLayout.addWidget(self.not_monitoring_radio)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)
        self.fork_count = QtWidgets.QLineEdit(self.centralwidget)
        self.fork_count.setReadOnly(True)
        self.fork_count.setObjectName("fork_count")
        self.gridLayout_4.addWidget(self.fork_count, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.profile_count = QtWidgets.QLineEdit(self.centralwidget)
        self.profile_count.setReadOnly(True)
        self.profile_count.setObjectName("profile_count")
        self.gridLayout_4.addWidget(self.profile_count, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 29))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuExport = QtWidgets.QMenu(self.menu_File)
        self.menuExport.setObjectName("menuExport")
        self.menu_Settings = QtWidgets.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Actions = QtWidgets.QMenu(self.menubar)
        self.menu_Actions.setObjectName("menu_Actions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionebpH_Help = QtWidgets.QAction(MainWindow)
        self.actionebpH_Help.setObjectName("actionebpH_Help")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/assets/img/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon1)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Start_Monitoring = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/assets/img/icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Start_Monitoring.setIcon(icon2)
        self.action_Start_Monitoring.setObjectName("action_Start_Monitoring")
        self.action_Stop_Monitoring = QtWidgets.QAction(MainWindow)
        self.action_Stop_Monitoring.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/assets/img/icons/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Stop_Monitoring.setIcon(icon3)
        self.action_Stop_Monitoring.setObjectName("action_Stop_Monitoring")
        self.action_View_Modify_Profile = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/assets/img/icons/browser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_View_Modify_Profile.setIcon(icon4)
        self.action_View_Modify_Profile.setObjectName("action_View_Modify_Profile")
        self.action_Force_Save_Profiles = QtWidgets.QAction(MainWindow)
        self.action_Force_Save_Profiles.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/assets/img/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Force_Save_Profiles.setIcon(icon5)
        self.action_Force_Save_Profiles.setObjectName("action_Force_Save_Profiles")
        self.action_Preferences = QtWidgets.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")
        self.actionExport_Logs = QtWidgets.QAction(MainWindow)
        self.actionExport_Logs.setObjectName("actionExport_Logs")
        self.actionExport_Statistics = QtWidgets.QAction(MainWindow)
        self.actionExport_Statistics.setObjectName("actionExport_Statistics")
        self.menuExport.addAction(self.actionExport_Logs)
        self.menuExport.addAction(self.actionExport_Statistics)
        self.menu_File.addAction(self.action_Force_Save_Profiles)
        self.menu_File.addAction(self.menuExport.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Settings.addAction(self.action_Preferences)
        self.menu_Help.addAction(self.actionebpH_Help)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_About)
        self.menu_Actions.addAction(self.action_Start_Monitoring)
        self.menu_Actions.addAction(self.action_Stop_Monitoring)
        self.menu_Actions.addSeparator()
        self.menu_Actions.addAction(self.action_View_Modify_Profile)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Actions.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Start_Monitoring)
        self.toolBar.addAction(self.action_Stop_Monitoring)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_View_Modify_Profile)
        self.toolBar.addAction(self.action_Force_Save_Profiles)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Quit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "ebpH", None, -1))
        self.event_log.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "ebpH event log", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "ebpH Log", None, -1))
        self.execve_count.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.exit_count.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.syscall_count.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.monitoring_radio.setText(QtWidgets.QApplication.translate("MainWindow", "Yes", None, -1))
        self.not_monitoring_radio.setText(QtWidgets.QApplication.translate("MainWindow", "No", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Currently Monitoring?", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Execves", None, -1))
        self.fork_count.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Exits", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Total System Calls", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Forks", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Active Profiles", None, -1))
        self.profile_count.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "ebpH Statistics", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menuExport.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Export", None, -1))
        self.menu_Settings.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Settings", None, -1))
        self.menu_Help.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Help", None, -1))
        self.menu_Actions.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Monitoring", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.action_About.setText(QtWidgets.QApplication.translate("MainWindow", "&About ebpH", None, -1))
        self.actionebpH_Help.setText(QtWidgets.QApplication.translate("MainWindow", "ebpH &Help", None, -1))
        self.actionebpH_Help.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+H", None, -1))
        self.action_Quit.setText(QtWidgets.QApplication.translate("MainWindow", "&Quit", None, -1))
        self.action_Quit.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Exit the application", None, -1))
        self.action_Quit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.action_Start_Monitoring.setText(QtWidgets.QApplication.translate("MainWindow", "&Start Monitoring", None, -1))
        self.action_Start_Monitoring.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Start monitoring processes", None, -1))
        self.action_Start_Monitoring.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+M", None, -1))
        self.action_Stop_Monitoring.setText(QtWidgets.QApplication.translate("MainWindow", "&Stop Monitoring", None, -1))
        self.action_Stop_Monitoring.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Stop monitoring processes", None, -1))
        self.action_Stop_Monitoring.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+M", None, -1))
        self.action_View_Modify_Profile.setText(QtWidgets.QApplication.translate("MainWindow", "View/Modify &Profile", None, -1))
        self.action_View_Modify_Profile.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, -1))
        self.action_Force_Save_Profiles.setText(QtWidgets.QApplication.translate("MainWindow", "Force &Save Profiles", None, -1))
        self.action_Force_Save_Profiles.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.action_Preferences.setText(QtWidgets.QApplication.translate("MainWindow", "&Preferences", None, -1))
        self.actionExport_Logs.setText(QtWidgets.QApplication.translate("MainWindow", "Export &Logs", None, -1))
        self.actionExport_Logs.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+E, Ctrl+L", None, -1))
        self.actionExport_Statistics.setText(QtWidgets.QApplication.translate("MainWindow", "Export &Statistics", None, -1))
        self.actionExport_Statistics.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+E, Ctrl+S", None, -1))

import resources_rc
