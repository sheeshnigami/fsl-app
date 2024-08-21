# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fslappwpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
import cv2
import sys


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)

        # Set up a timer to call update_frame regularly
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.update_frame)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
                                        "background-color : #C2E8FF\n"
                                        "}")
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.page_home = QtWidgets.QWidget()
        self.page_home.setStyleSheet("QWidget {\n"
                                        "background-color : #ffffff;\n"
                                        "border-radius : 25px;\n"
                                        "}")
        self.page_home.setObjectName("page_home")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 5, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_logo = QtWidgets.QLabel(self.page_home)
        self.label_logo.setMaximumSize(QtCore.QSize(200, 100))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("fslappcode/icons/logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_logo.setObjectName("label_logo")
        self.label_logo.setCursor(Qt.PointingHandCursor)
        
        self.horizontalLayout.addWidget(self.label_logo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 1)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.label_home = QtWidgets.QLabel(self.page_home)
        self.label_home.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Coolvetica Rg")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_home.setFont(font)
        self.label_home.setStyleSheet("QLabel {\n"
                                        "color : #192955\n"
                                        "}")
        self.label_home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home.setObjectName("label_home")
        
        self.horizontalLayout_4.addWidget(self.label_home)
        self.horizontalLayout_4.setStretch(0, 1)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.pushButton_translation = QtWidgets.QPushButton(self.page_home)
        self.pushButton_translation.setMinimumSize(QtCore.QSize(300, 300))
        self.pushButton_translation.setMaximumSize(QtCore.QSize(600, 600))
        self.pushButton_translation.setStyleSheet("QPushButton {\n"
                                                        "background-color : #C2E8FF;\n"
                                                        "border: none;\n"
                                                        "border-radius : 25px;\n"
                                                        "}\n"
                                                        "QPushButton:hover {\n"
                                                        "background-color : #A9D6FF;\n"
                                                        "}")
        self.pushButton_translation.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fslappcode/icons/Frame 17.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_translation.setIcon(icon)
        self.pushButton_translation.setIconSize(QtCore.QSize(290, 290))
        self.pushButton_translation.setObjectName("pushButton_translation")
        self.horizontalLayout_3.addWidget(self.pushButton_translation)
        self.pushButton_translation.setCursor(Qt.PointingHandCursor)
        
        self.pushButton_learn = QtWidgets.QPushButton(self.page_home)
        self.pushButton_learn.setMinimumSize(QtCore.QSize(300, 300))
        self.pushButton_learn.setMaximumSize(QtCore.QSize(600, 600))
        self.pushButton_learn.setStyleSheet("QPushButton{\n"
                                                "background-color: #C2E8FF;\n"
                                                "border: none;\n"
                                                "border-radius : 25px;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "background-color : #A9D6FF;\n"
                                                "}")
        self.pushButton_learn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("fslappcode/icons/Frame 13.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_learn.setIcon(icon1)
        self.pushButton_learn.setIconSize(QtCore.QSize(260, 260))
        self.pushButton_learn.setObjectName("pushButton_learn")
        self.pushButton_learn.setCursor(Qt.PointingHandCursor)
        
        self.horizontalLayout_3.addWidget(self.pushButton_learn)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 10)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label_translation = QtWidgets.QLabel(self.page_home)
        font = QtGui.QFont()
        font.setFamily("Coolvetica Rg")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_translation.setFont(font)
        self.label_translation.setStyleSheet("#label_translation{color : #192955;}")
        self.label_translation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_translation.setObjectName("label_translation")
        
        self.horizontalLayout_2.addWidget(self.label_translation)
        
        self.label_learn = QtWidgets.QLabel(self.page_home)
        font = QtGui.QFont()
        font.setFamily("Coolvetica Rg")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_learn.setFont(font)
        self.label_learn.setStyleSheet("#label_learn{color : #192955;}")
        self.label_learn.setAlignment(QtCore.Qt.AlignCenter)
        self.label_learn.setObjectName("label_learn")
        
        self.horizontalLayout_2.addWidget(self.label_learn)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(2, 5)
        
        self.stackedWidget.addWidget(self.page_home)
        
        self.page_translation = QtWidgets.QWidget()
        self.page_translation.setStyleSheet("QWidget {\n"
                                                "background-color : #ffffff;\n"
                                                "border-radius : 25px;\n"
                                                "}")
        self.page_translation.setObjectName("page_translation")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_translation)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, 5, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.label_logo_2 = QtWidgets.QLabel(self.page_translation)
        self.label_logo_2.setMaximumSize(QtCore.QSize(200, 100))
        self.label_logo_2.setText("")
        self.label_logo_2.setPixmap(QtGui.QPixmap("fslappcode/icons/logo.png"))
        self.label_logo_2.setScaledContents(True)
        self.label_logo_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_logo_2.setObjectName("label_logo_2")
        self.label_logo_2.setCursor(Qt.PointingHandCursor)
        
        self.horizontalLayout_5.addWidget(self.label_logo_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        self.label_translate = QtWidgets.QLabel(self.page_translation)
        self.label_translate.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Coolvetica Rg")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_translate.setFont(font)
        self.label_translate.setStyleSheet("QLabel {\n"
                                                "color : #192955\n"
                                                "}")
        self.label_translate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_translate.setObjectName("label_translate")
        
        self.horizontalLayout_7.addWidget(self.label_translate)
        
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        
        self.label_video = QtWidgets.QLabel(self.page_translation)
        self.label_video.setText("")
        self.label_video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video.setObjectName("label_video")
        
        self.horizontalLayout_9.addWidget(self.label_video)
        
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.setStretch(2, 5)
        
        self.stackedWidget.addWidget(self.page_translation)
        
        self.page_learn = QtWidgets.QWidget()
        self.page_learn.setStyleSheet("QWidget {\n"
                                        "background-color : #ffffff;\n"
                                        "border-radius : 25px;\n"
                                        "}")
        self.page_learn.setObjectName("page_learn")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_learn)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, 5, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.label_logo_3 = QtWidgets.QLabel(self.page_learn)
        self.label_logo_3.setMaximumSize(QtCore.QSize(200, 100))
        self.label_logo_3.setText("")
        self.label_logo_3.setPixmap(QtGui.QPixmap("fslappcode/icons/logo.png"))
        self.label_logo_3.setScaledContents(True)
        self.label_logo_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_logo_3.setObjectName("label_logo_3")
        self.label_logo_3.setCursor(Qt.PointingHandCursor)

        self.horizontalLayout_6.addWidget(self.label_logo_3)
        
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.horizontalLayout_6.addItem(spacerItem2)
        
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        
        self.label_home_2 = QtWidgets.QLabel(self.page_learn)
        self.label_home_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Coolvetica Rg")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_home_2.setFont(font)
        self.label_home_2.setStyleSheet("QLabel {\n"
                                                "color : #192955\n"
                                                "}")
        self.label_home_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home_2.setObjectName("label_home_2")
        
        self.horizontalLayout_8.addWidget(self.label_home_2)
        
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_learn1 = QtWidgets.QLabel(self.page_learn)
        self.label_learn1.setObjectName("label_learn1")
        
        self.gridLayout.addWidget(self.label_learn1, 0, 0, 1, 1)
        
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_4.setStretch(2, 5)
        
        self.stackedWidget.addWidget(self.page_learn)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        
        self.stackedWidget.setCurrentIndex(0)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to QImage
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qimg = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            # Display the image in the QLabel
            self.label_video.setPixmap(QPixmap.fromImage(qimg))
    
    def control_video(self):
        if not self.timer.isActive():
            # Start capturing and displaying video
            self.timer.start(30)
        else:
            # Stop the video
            self.timer.stop()

    def closeEvent(self, event):
        # Release the capture on close
        self.cap.release()
        event.accept()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_home.setText(_translate("MainWindow", "Translate and Learn Basic Filipino Sign Language"))
        self.label_translation.setText(_translate("MainWindow", "TRANSLATE"))
        self.label_learn.setText(_translate("MainWindow", "LEARN"))
        self.label_translate.setText(_translate("MainWindow", "Translate Basic Filipino Sign Language"))
        self.label_home_2.setText(_translate("MainWindow", "Learn Basic Filipino Sign Language"))
        self.label_learn1.setText(_translate("MainWindow", "Found Nothing.."))

    

# events
        self.pushButton_translation.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_translation.clicked.connect(lambda: self.control_video())
        self.pushButton_learn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.label_logo.mousePressEvent = lambda event: self.stackedWidget.setCurrentIndex(0)
        self.label_logo_2.mousePressEvent = lambda event: self.stackedWidget.setCurrentIndex(0)
        self.label_logo_3.mousePressEvent = lambda event: self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())