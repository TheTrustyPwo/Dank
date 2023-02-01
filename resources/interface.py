from PyQt5 import QtCore, QtGui, QtWidgets


class UI_DankMemerGrinder(object):
    def __init__(self, accounts):
        self.accounts = accounts

    def setupUi(self, DankMemerGrinder):
        DankMemerGrinder.setObjectName("DankMemerGrinder")
        DankMemerGrinder.resize(868, 535)
        self.central_widget = QtWidgets.QWidget(DankMemerGrinder)
        self.central_widget.setStyleSheet(
            "*{\n"
            "    border: none;\n"
            "    background-color: transparent;\n"
            "    color: #e8e6e3;\n"
            "}\n"
            "#central_widget{\n"
            "    background-color: #36393f;\n"
            "}\n"
            "QPushButton{\n"
            "    background-color: #42464d;;\n"
            "    border-radius: 15px;\n"
            "}\n"
            "#main_frame{\n"
            "    background-color: #2f3136;\n"
            "    border-radius: 20px;\n"
            "}\n"
            "QCheckBox::indicator:unchecked{\n"
            '    image: url(":/icons/icons/off-button.png");\n'
            '    width: "40px";\n'
            '    height: "40px";\n'
            "}\n"
            "QCheckBox::indicator:checked{\n"
            '    image: url(":/icons/icons/on-button.png");\n'
            '    width: "40px";\n'
            '    height: "40px";\n'
            "}\n"
            "\n"
            "QSpinBox{\n"
            "    background-color: #5c6066;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QSpinBox::up-button{\n"
            "    width: 20px;\n"
            "}\n"
            "QSpinBox::down-button{\n"
            "    width: 20px;\n"
            "}\n"
            "\n"
            "/* QScrollBar Vertical */\n"
            "QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #202225;\n"
            "    width: 14px;\n"
            "    margin: 15px 0 15px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            "\n"
            "QScrollBar::handle:vertical {    \n"
            "    background-color: #5865f2;\n"
            "    min-height: 30px;\n"
            "    border-radius: 7px;\n"
            "}\n"
            "QScrollBar::handle:vertical:hover{    \n"
            "    background-color: #525ee5;\n"
            "}\n"
            "QScrollBar::handle:vertical:pressed {    \n"
            "    background-color: #454fbf;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "    border: none;\n"
            "    background-color: #2f3136;\n"
            "    height: 15px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:vertical:hover {    \n"
            "    background-color: #525ee5;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed {    \n"
            "    background-color: #454fbf;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "    border: none;\n"
            "    background-color: #2f3136;\n"
            "    height: 15px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::add-line:vertical:hover {    \n"
            "    background-color: #525ee5;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed {    \n"
            "    background-color: #454fbf;\n"
            "}\n"
            "\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "    background: none;\n"
            "}\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "/* QScrollBar Horizontal */\n"
            "QScrollBar:horizontal {\n"
            "    height: 14px;\n"
            "    margin: 0 15px 0 15px;\n"
            "    border: 1px transparent #2A2929;\n"
            "    border-radius: 0px;\n"
            "    background-color: yellow;\n"
            "    border-radius: 7px;\n"
            "    background: #40444b;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal {\n"
            "    background-color: #5865f2;\n"
            "    min-width: 30px;\n"
            "    border-radius: 7px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal:hover{    \n"
            "    background-color: #525ee5;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed {    \n"
            "    background-color: #454fbf;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:horizontal {\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
            "    background: none;\n"
            "}"
        )
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QtCore.QSize(850, 65))
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.header_frame.setStyleSheet(
            "#header_frame{\n"
            "    background-color: #202225;\n"
            "    border-radius: 20px;\n"
            "}"
        )
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.header_frame)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 803, 72))
        self.scrollAreaWidgetContents.setStyleSheet(
            "QPushButton {\npadding: 0 5px 0 5px;\n}"
        )
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.add_account_frame = QtWidgets.QFrame(self.header_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.add_account_frame.sizePolicy().hasHeightForWidth()
        )
        self.add_account_frame.setSizePolicy(sizePolicy)
        self.add_account_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_account_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_account_frame.setObjectName("add_account_frame")
        self.verticalLayout_85 = QtWidgets.QVBoxLayout(self.add_account_frame)
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_85.setObjectName("verticalLayout_85")
        self.add_account_btn = QtWidgets.QPushButton(self.add_account_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.add_account_btn.sizePolicy().hasHeightForWidth()
        )
        self.add_account_btn.setSizePolicy(sizePolicy)
        self.add_account_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_account_btn.setStyleSheet("background-color : #00FFFFFF;")
        self.add_account_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/plus.png"), QtGui.QIcon.Active, QtGui.QIcon.On
        )
        self.add_account_btn.setIcon(icon1)
        self.add_account_btn.setIconSize(QtCore.QSize(25, 25))
        self.add_account_btn.setObjectName("add_account_btn")
        self.verticalLayout_85.addWidget(self.add_account_btn)
        self.minus_account_btn = QtWidgets.QPushButton(self.add_account_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.minus_account_btn.sizePolicy().hasHeightForWidth()
        )
        self.minus_account_btn.setSizePolicy(sizePolicy)
        self.minus_account_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minus_account_btn.setStyleSheet("background-color : #00FFFFFF;")
        self.minus_account_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/minus.png"), QtGui.QIcon.Active, QtGui.QIcon.On
        )
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/minus.svg"),
            QtGui.QIcon.Selected,
            QtGui.QIcon.Off,
        )
        self.minus_account_btn.setIcon(icon2)
        self.minus_account_btn.setIconSize(QtCore.QSize(25, 25))
        self.minus_account_btn.setObjectName("minus_account_btn")
        self.verticalLayout_85.addWidget(self.minus_account_btn)
        self.horizontalLayout_3.addWidget(self.add_account_frame)
        self.verticalLayout.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)
        self.main_frame = QtWidgets.QFrame(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMinimumSize(QtCore.QSize(850, 0))
        self.main_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu_widget = QtWidgets.QWidget(self.main_frame)
        self.side_menu_widget.setStyleSheet(
            "#side_menu_widget{\n"
            "    background-color: #202225;\n"
            "    border-radius: 20px;\n"
            "}"
        )
        self.side_menu_widget.setObjectName("side_menu_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu_widget)
        self.verticalLayout_2.setContentsMargins(6, 8, 6, 8)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttons = QtWidgets.QFrame(self.side_menu_widget)
        self.buttons.setMinimumSize(QtCore.QSize(150, 0))
        self.buttons.setMaximumSize(QtCore.QSize(150, 16777215))
        self.buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.buttons)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.home_btn = QtWidgets.QPushButton(self.buttons)
        self.home_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.home_btn.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.home_btn.setFont(font)
        self.home_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_btn.setStyleSheet("background-color: #5865f2;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QtCore.QSize(20, 20))
        self.home_btn.setObjectName("home_btn")
        self.verticalLayout_3.addWidget(self.home_btn)
        self.settings_btn = QtWidgets.QPushButton(self.buttons)
        self.settings_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.settings_btn.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.settings_btn.setFont(font)
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/settings.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.settings_btn.setIcon(icon2)
        self.settings_btn.setIconSize(QtCore.QSize(20, 20))
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout_3.addWidget(self.settings_btn)
        self.commands_btn = QtWidgets.QPushButton(self.buttons)
        self.commands_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.commands_btn.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.commands_btn.setFont(font)
        self.commands_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commands_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/commands.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.commands_btn.setIcon(icon3)
        self.commands_btn.setIconSize(QtCore.QSize(20, 20))
        self.commands_btn.setObjectName("commands_btn")
        self.verticalLayout_3.addWidget(self.commands_btn)
        self.auto_buy_btn = QtWidgets.QPushButton(self.buttons)
        self.auto_buy_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.auto_buy_btn.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.auto_buy_btn.setFont(font)
        self.auto_buy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/dollar.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.auto_buy_btn.setIcon(icon4)
        self.auto_buy_btn.setIconSize(QtCore.QSize(20, 20))
        self.auto_buy_btn.setObjectName("auto_buy_btn")
        self.verticalLayout_3.addWidget(self.auto_buy_btn)
        self.verticalLayout_2.addWidget(self.buttons, 0, QtCore.Qt.AlignTop)
        self.toggle = QtWidgets.QPushButton(self.side_menu_widget)
        self.toggle.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle.sizePolicy().hasHeightForWidth())
        self.toggle.setSizePolicy(sizePolicy)
        self.toggle.setMinimumSize(QtCore.QSize(0, 45))
        self.toggle.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toggle.setFont(font)
        self.toggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggle.setStyleSheet("background-color : #d83c3e")
        self.toggle.setObjectName("toggle")
        self.verticalLayout_2.addWidget(self.toggle)
        self.horizontalLayout.addWidget(self.side_menu_widget)
        self.main_menu_widget = QtWidgets.QStackedWidget(self.main_frame)
        self.main_menu_widget.setObjectName("main_menu_widget")
        self.horizontalLayout.addWidget(self.main_menu_widget)
        self.verticalLayout.addWidget(self.main_frame)
        DankMemerGrinder.setCentralWidget(self.central_widget)
        self.main_menu_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DankMemerGrinder)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DankMemerGrinder = QtWidgets.QMainWindow()
    ui = UI_DankMemerGrinder()
    ui.setupUi(DankMemerGrinder)
    DankMemerGrinder.show()
    sys.exit(app.exec_())
