# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morph.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.set_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_label.sizePolicy().hasHeightForWidth())
        self.set_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.set_label.setFont(font)
        self.set_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.set_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.set_label.setScaledContents(False)
        self.set_label.setAlignment(QtCore.Qt.AlignCenter)
        self.set_label.setObjectName("set_label")
        self.verticalLayout.addWidget(self.set_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_0 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_0.sizePolicy().hasHeightForWidth())
        self.radio_0.setSizePolicy(sizePolicy)
        self.radio_0.setChecked(True)
        self.radio_0.setObjectName("radio_0")
        self.horizontalLayout.addWidget(self.radio_0)
        self.radio_1 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_1.sizePolicy().hasHeightForWidth())
        self.radio_1.setSizePolicy(sizePolicy)
        self.radio_1.setObjectName("radio_1")
        self.horizontalLayout.addWidget(self.radio_1)
        self.radio_2 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_2.sizePolicy().hasHeightForWidth())
        self.radio_2.setSizePolicy(sizePolicy)
        self.radio_2.setObjectName("radio_2")
        self.horizontalLayout.addWidget(self.radio_2)
        self.radio_3 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_3.sizePolicy().hasHeightForWidth())
        self.radio_3.setSizePolicy(sizePolicy)
        self.radio_3.setObjectName("radio_3")
        self.horizontalLayout.addWidget(self.radio_3)
        self.radio_4 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_4.sizePolicy().hasHeightForWidth())
        self.radio_4.setSizePolicy(sizePolicy)
        self.radio_4.setObjectName("radio_4")
        self.horizontalLayout.addWidget(self.radio_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.edit_comment = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_comment.setEnabled(True)
        self.edit_comment.setText("")
        self.edit_comment.setClearButtonEnabled(False)
        self.edit_comment.setObjectName("edit_comment")
        self.verticalLayout.addWidget(self.edit_comment)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_button.sizePolicy().hasHeightForWidth())
        self.prev_button.setSizePolicy(sizePolicy)
        self.prev_button.setObjectName("prev_button")
        self.gridLayout_3.addWidget(self.prev_button, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 3, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.image_label = ScaledLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QtCore.QSize(10, 10))
        self.image_label.setBaseSize(QtCore.QSize(0, 0))
        self.image_label.setFrameShape(QtWidgets.QFrame.Box)
        self.image_label.setLineWidth(1)
        self.image_label.setText("")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.horizontalLayout_3.addWidget(self.image_label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.button_wtf = QtWidgets.QPushButton(self.centralwidget)
        self.button_wtf.setObjectName("button_wtf")
        self.gridLayout_2.addWidget(self.button_wtf, 3, 0, 1, 1)
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setObjectName("next_button")
        self.gridLayout_2.addWidget(self.next_button, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.colour_label = QtWidgets.QLabel(self.centralwidget)
        self.colour_label.setAutoFillBackground(True)
        self.colour_label.setText("")
        self.colour_label.setAlignment(QtCore.Qt.AlignCenter)
        self.colour_label.setObjectName("colour_label")
        self.gridLayout.addWidget(self.colour_label, 4, 0, 1, 1)
        self.position_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_label.sizePolicy().hasHeightForWidth())
        self.position_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.position_label.setFont(font)
        self.position_label.setAlignment(QtCore.Qt.AlignCenter)
        self.position_label.setObjectName("position_label")
        self.gridLayout.addWidget(self.position_label, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setBaseSize(QtCore.QSize(0, 10))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.horizontalLayout_2.addWidget(self.progress_bar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.jump_box = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jump_box.sizePolicy().hasHeightForWidth())
        self.jump_box.setSizePolicy(sizePolicy)
        self.jump_box.setMaximumSize(QtCore.QSize(50, 16777215))
        self.jump_box.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.jump_box.setAutoFillBackground(True)
        self.jump_box.setObjectName("jump_box")
        self.horizontalLayout_2.addWidget(self.jump_box)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setEnabled(False)
        self.username_edit.setReadOnly(False)
        self.username_edit.setObjectName("username_edit")
        self.horizontalLayout_2.addWidget(self.username_edit)
        self.set_username_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_username_button.setObjectName("set_username_button")
        self.horizontalLayout_2.addWidget(self.set_username_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 20))
        self.menubar.setObjectName("menubar")
        self.menuLensrater = QtWidgets.QMenu(self.menubar)
        self.menuLensrater.setObjectName("menuLensrater")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave_and_Quit = QtWidgets.QAction(MainWindow)
        self.actionSave_and_Quit.setObjectName("actionSave_and_Quit")
        self.actionQuit_without_saving = QtWidgets.QAction(MainWindow)
        self.actionQuit_without_saving.setObjectName("actionQuit_without_saving")
        self.actionReset_scores = QtWidgets.QAction(MainWindow)
        self.actionReset_scores.setObjectName("actionReset_scores")
        self.menuLensrater.addAction(self.actionSave_and_Quit)
        self.menuLensrater.addAction(self.actionQuit_without_saving)
        self.menuLensrater.addAction(self.actionReset_scores)
        self.menubar.addAction(self.menuLensrater.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lensrater"))
        self.set_label.setText(_translate("MainWindow", "set name"))
        self.radio_0.setText(_translate("MainWindow", "Irregular"))
        self.radio_1.setText(_translate("MainWindow", "Elliptical"))
        self.radio_2.setText(_translate("MainWindow", "Disk"))
        self.radio_3.setText(_translate("MainWindow", "Disk+Bulge"))
        self.radio_4.setText(_translate("MainWindow", "Discard"))
        self.edit_comment.setPlaceholderText(_translate("MainWindow", "Comment here"))
        self.prev_button.setText(_translate("MainWindow", "Prev"))
        self.button_wtf.setText(_translate("MainWindow", "WTF?"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.position_label.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Jump to:"))
        self.label_2.setText(_translate("MainWindow", "User:"))
        self.username_edit.setText(_translate("MainWindow", "Username"))
        self.set_username_button.setText(_translate("MainWindow", "Set"))
        self.menuLensrater.setTitle(_translate("MainWindow", "Morphrater"))
        self.actionSave_and_Quit.setText(_translate("MainWindow", "Save and Quit"))
        self.actionQuit_without_saving.setText(_translate("MainWindow", "Quit without saving"))
        self.actionReset_scores.setText(_translate("MainWindow", "Reset scores"))
from scaledlabel import ScaledLabel
