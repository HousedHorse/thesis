# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profiledialog.ui',
# licensing of 'profiledialog.ui' applies.
#
# Created: Mon Sep  2 13:38:45 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ProfileDialog(object):
    def setupUi(self, ProfileDialog):
        ProfileDialog.setObjectName("ProfileDialog")
        ProfileDialog.resize(989, 703)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/assets/img/icons/browser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProfileDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(ProfileDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(ProfileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(ProfileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(ProfileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(ProfileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 487, 647))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 8, 2, 1, 1)
        self.train_count = LazyLineEdit(self.scrollAreaWidgetContents)
        self.train_count.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.train_count.setReadOnly(True)
        self.train_count.setObjectName("train_count")
        self.gridLayout_3.addWidget(self.train_count, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 10, 0, 1, 1)
        self.key = LazyLineEdit(self.scrollAreaWidgetContents)
        self.key.setReadOnly(True)
        self.key.setObjectName("key")
        self.gridLayout_3.addWidget(self.key, 1, 2, 1, 1)
        self.anomalies = LazyLineEdit(self.scrollAreaWidgetContents)
        self.anomalies.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.anomalies.setReadOnly(True)
        self.anomalies.setObjectName("anomalies")
        self.gridLayout_3.addWidget(self.anomalies, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 5, 0, 1, 1)
        self.syscalls = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.syscalls.setObjectName("syscalls")
        self.gridLayout_3.addWidget(self.syscalls, 7, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.normal_count = LazyLineEdit(self.scrollAreaWidgetContents)
        self.normal_count.setReadOnly(True)
        self.normal_count.setObjectName("normal_count")
        self.gridLayout_3.addWidget(self.normal_count, 6, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.verticalLayout, 7, 0, 1, 1)
        self.last_mod_count = LazyLineEdit(self.scrollAreaWidgetContents)
        self.last_mod_count.setReadOnly(True)
        self.last_mod_count.setObjectName("last_mod_count")
        self.gridLayout_3.addWidget(self.last_mod_count, 5, 2, 1, 1)
        self.comm = LazyLineEdit(self.scrollAreaWidgetContents)
        self.comm.setReadOnly(True)
        self.comm.setObjectName("comm")
        self.gridLayout_3.addWidget(self.comm, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.state = LazyLineEdit(self.scrollAreaWidgetContents)
        self.state.setReadOnly(True)
        self.state.setObjectName("state")
        self.gridLayout_3.addWidget(self.state, 2, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.reset_profile_button = QtWidgets.QPushButton(ProfileDialog)
        self.reset_profile_button.setObjectName("reset_profile_button")
        self.horizontalLayout.addWidget(self.reset_profile_button)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.profile_list = QtWidgets.QListView(ProfileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_list.sizePolicy().hasHeightForWidth())
        self.profile_list.setSizePolicy(sizePolicy)
        self.profile_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.profile_list.setObjectName("profile_list")
        self.gridLayout_2.addWidget(self.profile_list, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(ProfileDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ProfileDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ProfileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ProfileDialog)

    def retranslateUi(self, ProfileDialog):
        ProfileDialog.setWindowTitle(QtWidgets.QApplication.translate("ProfileDialog", "View/Modify Profiles", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ProfileDialog", "Details", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ProfileDialog", "Profiles", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("ProfileDialog", "Anomalies", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ProfileDialog", "Comm", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("ProfileDialog", "Train Count", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("ProfileDialog", "<html><head/><body><p>Normal<br/><span style=\" color:#ff0004;\">Anomaly</span></p></body></html>", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("ProfileDialog", "Normal Count", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("ProfileDialog", "Last Mod Count", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("ProfileDialog", "Key", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("ProfileDialog", "Recent\n"
"System Calls", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("ProfileDialog", "Profile State", None, -1))
        self.reset_profile_button.setText(QtWidgets.QApplication.translate("ProfileDialog", "Reset Profile", None, -1))

from ebpH.gui.lazy_line_edit import LazyLineEdit
from . import resources_rc
