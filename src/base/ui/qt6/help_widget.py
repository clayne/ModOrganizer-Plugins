# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\base\ui\help_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_helpTabWidget(object):
    def setupUi(self, helpTabWidget):
        helpTabWidget.setObjectName("helpTabWidget")
        helpTabWidget.resize(449, 391)
        self.verticalLayout = QtWidgets.QVBoxLayout(helpTabWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.helpText = QtWidgets.QTextBrowser(parent=helpTabWidget)
        self.helpText.setObjectName("helpText")
        self.verticalLayout.addWidget(self.helpText)
        self.linksWidget = QtWidgets.QWidget(parent=helpTabWidget)
        self.linksWidget.setObjectName("linksWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.linksWidget)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.docsButton = QtWidgets.QPushButton(parent=self.linksWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.docsButton.sizePolicy().hasHeightForWidth())
        self.docsButton.setSizePolicy(sizePolicy)
        self.docsButton.setText("")
        self.docsButton.setIconSize(QtCore.QSize(24, 24))
        self.docsButton.setFlat(True)
        self.docsButton.setObjectName("docsButton")
        self.horizontalLayout.addWidget(self.docsButton)
        self.nexusButton = QtWidgets.QPushButton(parent=self.linksWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nexusButton.sizePolicy().hasHeightForWidth())
        self.nexusButton.setSizePolicy(sizePolicy)
        self.nexusButton.setText("")
        self.nexusButton.setIconSize(QtCore.QSize(24, 24))
        self.nexusButton.setFlat(True)
        self.nexusButton.setObjectName("nexusButton")
        self.horizontalLayout.addWidget(self.nexusButton)
        self.discordButton = QtWidgets.QPushButton(parent=self.linksWidget)
        self.discordButton.setText("")
        self.discordButton.setIconSize(QtCore.QSize(24, 24))
        self.discordButton.setFlat(True)
        self.discordButton.setObjectName("discordButton")
        self.horizontalLayout.addWidget(self.discordButton)
        self.githubButton = QtWidgets.QPushButton(parent=self.linksWidget)
        self.githubButton.setText("")
        self.githubButton.setIconSize(QtCore.QSize(24, 24))
        self.githubButton.setFlat(True)
        self.githubButton.setObjectName("githubButton")
        self.horizontalLayout.addWidget(self.githubButton)
        self.patreonButton = QtWidgets.QPushButton(parent=self.linksWidget)
        self.patreonButton.setText("")
        self.patreonButton.setIconSize(QtCore.QSize(24, 24))
        self.patreonButton.setFlat(True)
        self.patreonButton.setObjectName("patreonButton")
        self.horizontalLayout.addWidget(self.patreonButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.linksWidget)

        self.retranslateUi(helpTabWidget)
        QtCore.QMetaObject.connectSlotsByName(helpTabWidget)

    def retranslateUi(self, helpTabWidget):
        _translate = QtCore.QCoreApplication.translate
        helpTabWidget.setWindowTitle(_translate("helpTabWidget", "Form"))
