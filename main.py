from PyQt6.QtCore import QRegularExpression
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QCursor, QPainter,  QColor, QBitmap, QRegularExpressionValidator
'''
本文件为软件的第一个窗口，实现了用户登录的功能。
由于PyQt6的某些不兼容问题，本文件将ui和功能的实现放在了一起。
'''

class loginWidget(QtWidgets.QWidget):
    mainWidgetMoveFlag = False  # 设置主界面除去子控件以外的其他地方能否移动
    subWidgetMoveFlag = False  # 这个变量由子窗口进行管理。不应该在此类中被修改。

    def __init__(self, mainWidgetMoveFlag, subWidgetMoveFlag):
        super().__init__()
        self.mainWidgetMoveFlag = mainWidgetMoveFlag
        self.mainWidgetMoveFlag = mainWidgetMoveFlag
        self.subWidgetMoveFlag = subWidgetMoveFlag
        self.canMoveFlag = False
        self.setupUi()
        self.show()

    def setupUi(self):
        '''首先初始化主界面，一个透明的widget。'''
        self.resize(1243, 701)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("border-radius:20px;")
        effect_shadow_style(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        '''设置标签，在标签上设置图片'''
        self.pictureLable = QtWidgets.QLabel(self)
        self.pictureLable.setGeometry(0, -3, 1243, 701)
        p = QPixmap('login4.png')
        self.pictureLable.setPixmap(p)
        self.pictureLable.resize(self.size())
        self.pictureLable.setStyleSheet("border-radius:20px;")

        '''垂直布局'''
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(810, 260, 231, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        '''请登录标签'''
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
        QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color :rgb(45,163,140);\n"
        "font: 25pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        '''用户名标签'''
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("color :rgb(45,163,140);\n"
        "font: 290 13pt \"微软雅黑 Light\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        '''用户名输入框'''
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        regx=QRegularExpression("[1-9][0-9]+$")
        validator=QRegularExpressionValidator(regx,self.lineEdit)
        self.lineEdit.setValidator(validator)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(14)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "border-color:rgb(45,163,140);\n"
            "border-radius:10px;\n"
            "height:30;\n"
            "background-color: rgb(217,217,217);\n"
            "selection-background-color: rgb(202, 228, 255);"
        )
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(6)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        '''密码标签'''
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("color :rgb(45,163,140);\n"
        "font: 290 13pt \"微软雅黑 Light\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        '''密码输入框'''
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(
        "font: 15pt \"Tahoma\";\n"
        "border-color:rgb(45,163,140);\n"
        "border-radius:10px;\n"
        "height:25;\n"
        "border:2px;\n"
        "background-color: rgb(217,217,217);\n"
        "selection-background-color: rgb(202, 228, 255);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(15)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)

        '''空标签，显示登录的结果（失败）'''
        self.resultLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.resultLable.setText("")
        self.resultLable.setObjectName("resultLable")
        self.verticalLayout.addWidget(self.resultLable)

        '''空标签'''
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        '''确定按钮'''
        self.nextButton = QtWidgets.QPushButton(self)
        self.nextButton.setGeometry(QtCore.QRect(935, 530, 115, 31))
        self.nextButton.setStyleSheet("background-color: rgb(78, 185, 155);\n"
        "color:rgb(255，255，255);\n"
        "font: 290 14pt \"微软雅黑 Light\";\n"
        "height:35;\n"
        "border-radius:10px;\n"
        "padding:2px 4px;\n"
        "border-style: outset; \n"
        "border-width: 2px; \n"
        "border-color: gray;\n"
        "")
        self.nextButton.setObjectName("nextButton")

        '''退出按钮'''
        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setGeometry(QtCore.QRect(810, 530, 115, 31))
        self.exitButton.setStyleSheet("\n"
        "color:rgb(255，255，255);\n"
        "font: 290 14pt \"微软雅黑 Light\";\n"
        "height:35;\n"
        "background-color: rgb(236, 65, 65);\n"
        "border-radius:10px;\n"
        "padding:2px 4px;\n"
        "border-style: outset; \n"
        "border-width: 2px; \n"
        "border-color: gray;\n")
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(self.close)

        '''成绩管理系统'''
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(500, 80, 350, 60))
        self.label.setStyleSheet("color :rgb(144,206,195);\n"
        "font: 30pt \"黑体\";")
        self.label.setObjectName("label")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-weight:700;\">请登录:</span></p></body></html>"))
        self.label_3.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-weight:700;\">用户名：</span></p></body></html>"))
        self.label_4.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-weight:700;\">密码：</span></p></body></html>"))
        self.nextButton.setText(_translate("Form", "确定"))
        self.exitButton.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form",
            "<html><head/><body><p><span style=\" font-weight:700;\">成绩管理系统</span></p></body></html>"))

    def mousePressEvent(self, evt):
        '''可以自定义canMove_Flag = True需要满足的条件'''
        '''subWidgetMoveFlag子窗口被点击的瞬间，就被子窗口设置，值为子窗口是否允许拖动'''
        if (self.subWidgetMoveFlag == True or self.mainWidgetMoveFlag == True):
            # canMoveFlag被设置成Ture，标志着一个拖动过程的开始。mouseMoveEvent函数就是用这个去判断是否在拖动。
            self.canMoveFlag = True
            self.window_origin_x = self.x()
            self.window_origin_y = self.y()
            self.mouse_origin_x = QCursor.pos().x()
            self.mouse_origin_y = QCursor.pos().y()

    def mouseMoveEvent(self, evt):
        '''通过一个if语句的判断，只能在canMoveFlag = True时才可以单击鼠标左键拖动这个widget'''
        if (self.canMoveFlag == True):
            self.mouse_des_x = QCursor.pos().x()
            self.mouse_des_y = QCursor.pos().y()
            self.window_des_x = self.window_origin_x + self.mouse_des_x - self.mouse_origin_x
            self.window_des_y = self.window_origin_y + self.mouse_des_y - self.mouse_origin_y
            self.move(self.window_des_x, self.window_des_y)

    def mouseReleaseEvent(self, evt):
        '''subWidgetMoveFlag在释放的瞬间，被设置成False，意味着一个拖动过程的结束'''
        self.canMoveFlag = False
        self.subWidgetMoveFlag = False

    def paintEvent(self, a0: QtGui.QPaintEvent):
        bitmap = QBitmap(self.size())
        bitmap.fill()
        painter = QPainter(bitmap)
        painter.begin(self)
        painter.setPen(Qt.GlobalColor.red)
        painter.setBrush(Qt.GlobalColor.red)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.drawRoundedRect(bitmap.rect(), 30, 30)
        painter.end()
        self.setMask(bitmap)


def effect_shadow_style(widget):
    effect_shadow = QtWidgets.QGraphicsDropShadowEffect(widget)
    effect_shadow.setOffset(20, 20)  # 偏移
    effect_shadow.setBlurRadius(128)  # 阴影半径
    effect_shadow.setColor(QColor(148,148,148))  # 阴影颜色
    widget.setGraphicsEffect(effect_shadow)
    widget.setContentsMargins(1, 1, 1, 1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginWid = loginWidget(True, False)
    loginWid.setupUi()
    sys.exit(app.exec())
