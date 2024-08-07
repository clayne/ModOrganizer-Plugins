# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\plugin\rootbuilder\ui\rootbuilder_mode.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modeTabWidget(object):
    def setupUi(self, modeTabWidget):
        modeTabWidget.setObjectName("modeTabWidget")
        modeTabWidget.resize(450, 350)
        modeTabWidget.setMinimumSize(QtCore.QSize(450, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(modeTabWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.copyModeWidget = QtWidgets.QWidget(modeTabWidget)
        self.copyModeWidget.setObjectName("copyModeWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.copyModeWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.copyModeRadio = QtWidgets.QRadioButton(self.copyModeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.copyModeRadio.setFont(font)
        self.copyModeRadio.setObjectName("copyModeRadio")
        self.verticalLayout_6.addWidget(self.copyModeRadio)
        self.copyModeLabel = QtWidgets.QLabel(self.copyModeWidget)
        self.copyModeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.copyModeLabel.setWordWrap(True)
        self.copyModeLabel.setObjectName("copyModeLabel")
        self.verticalLayout_6.addWidget(self.copyModeLabel)
        self.verticalLayout.addWidget(self.copyModeWidget)
        self.linkModeWidget = QtWidgets.QWidget(modeTabWidget)
        self.linkModeWidget.setObjectName("linkModeWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.linkModeWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.linkModeRadio = QtWidgets.QRadioButton(self.linkModeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.linkModeRadio.setFont(font)
        self.linkModeRadio.setObjectName("linkModeRadio")
        self.verticalLayout_5.addWidget(self.linkModeRadio)
        self.linkModeLabel = QtWidgets.QLabel(self.linkModeWidget)
        self.linkModeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.linkModeLabel.setWordWrap(True)
        self.linkModeLabel.setObjectName("linkModeLabel")
        self.verticalLayout_5.addWidget(self.linkModeLabel)
        self.verticalLayout.addWidget(self.linkModeWidget)
        self.usvfsModeWidget = QtWidgets.QWidget(modeTabWidget)
        self.usvfsModeWidget.setObjectName("usvfsModeWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.usvfsModeWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.usvfsModeRadio = QtWidgets.QRadioButton(self.usvfsModeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.usvfsModeRadio.setFont(font)
        self.usvfsModeRadio.setObjectName("usvfsModeRadio")
        self.verticalLayout_4.addWidget(self.usvfsModeRadio)
        self.usvfsModeLabel = QtWidgets.QLabel(self.usvfsModeWidget)
        self.usvfsModeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.usvfsModeLabel.setWordWrap(True)
        self.usvfsModeLabel.setObjectName("usvfsModeLabel")
        self.verticalLayout_4.addWidget(self.usvfsModeLabel)
        self.verticalLayout.addWidget(self.usvfsModeWidget)
        self.usvfsLinkModeWidget = QtWidgets.QWidget(modeTabWidget)
        self.usvfsLinkModeWidget.setObjectName("usvfsLinkModeWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.usvfsLinkModeWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.usvfsLinkModeRadio = QtWidgets.QRadioButton(self.usvfsLinkModeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.usvfsLinkModeRadio.setFont(font)
        self.usvfsLinkModeRadio.setObjectName("usvfsLinkModeRadio")
        self.verticalLayout_2.addWidget(self.usvfsLinkModeRadio)
        self.usvfsLinkModeLabel = QtWidgets.QLabel(self.usvfsLinkModeWidget)
        self.usvfsLinkModeLabel.setScaledContents(False)
        self.usvfsLinkModeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.usvfsLinkModeLabel.setWordWrap(True)
        self.usvfsLinkModeLabel.setObjectName("usvfsLinkModeLabel")
        self.verticalLayout_2.addWidget(self.usvfsLinkModeLabel)
        self.verticalLayout.addWidget(self.usvfsLinkModeWidget)
        self.customModeWidget = QtWidgets.QWidget(modeTabWidget)
        self.customModeWidget.setObjectName("customModeWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.customModeWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.customModeRadio = QtWidgets.QRadioButton(self.customModeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.customModeRadio.setFont(font)
        self.customModeRadio.setObjectName("customModeRadio")
        self.verticalLayout_3.addWidget(self.customModeRadio)
        self.customModeLabel = QtWidgets.QLabel(self.customModeWidget)
        self.customModeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.customModeLabel.setWordWrap(True)
        self.customModeLabel.setObjectName("customModeLabel")
        self.verticalLayout_3.addWidget(self.customModeLabel)
        self.verticalLayout.addWidget(self.customModeWidget)

        self.retranslateUi(modeTabWidget)
        QtCore.QMetaObject.connectSlotsByName(modeTabWidget)

    def retranslateUi(self, modeTabWidget):
        _translate = QtCore.QCoreApplication.translate
        modeTabWidget.setWindowTitle(_translate("modeTabWidget", "Form"))
        self.copyModeRadio.setText(_translate("modeTabWidget", "Copy"))
        self.copyModeLabel.setText(_translate("modeTabWidget", "Copy mode will copy files in Root folders to the game folder during a build. On a clear, any changes will sync back to Mod Organizer and the copied files will be deleted."))
        self.linkModeRadio.setText(_translate("modeTabWidget", "Link"))
        self.linkModeLabel.setText(_translate("modeTabWidget", "Link mode will create links from files in Root folders to the game folder. On a clear, any changes will sync back to Mod Organizer and the links will be removed."))
        self.usvfsModeRadio.setText(_translate("modeTabWidget", "USVFS"))
        self.usvfsModeLabel.setText(_translate("modeTabWidget", "USVFS mode will use Mod Organizer\'s VFS to map files in Root folders to the game folder. This can be incompatible with some mods and requires Autobuild to function correctly."))
        self.usvfsLinkModeRadio.setText(_translate("modeTabWidget", "USVFS + Link"))
        self.usvfsLinkModeLabel.setText(_translate("modeTabWidget", "USVFS + Link mode will use Mod Organizer\'s VFS to map files in Root folders to the game folder. Links will be used for dll and exe files to improve compatibility. Requires Autobuild to function correctly."))
        self.customModeRadio.setText(_translate("modeTabWidget", "Custom"))
        self.customModeLabel.setText(_translate("modeTabWidget", "Custom mode allows you to specify your own rules for which files are deployed through copying, links or mapping through USVFS."))
