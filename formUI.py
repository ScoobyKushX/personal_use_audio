# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 409, 1891, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_musique = QtWidgets.QWidget()
        self.tab_musique.setObjectName("tab_musique")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.tab_musique)
        self.scrollArea_2.setGeometry(QtCore.QRect(-1, -1, 1891, 331))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1889, 329))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(parent=self.scrollAreaWidgetContents_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1860, -21, 20, 331))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.widget_soundcloud = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.widget_soundcloud.setGeometry(QtCore.QRect(1149, -11, 691, 311))
        self.widget_soundcloud.setObjectName("widget_soundcloud")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_soundcloud)
        self.label_7.setGeometry(QtCore.QRect(0, 20, 211, 61))
        self.label_7.setStyleSheet("font: 22pt \"Yellowtail\";\n"
"selection-color: rgb(255, 0, 0);\n"
"color: rgb(85, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"")
        self.label_7.setObjectName("label_7")
        self.widget_playlist = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.widget_playlist.setGeometry(QtCore.QRect(9, 9, 1131, 311))
        self.widget_playlist.setObjectName("widget_playlist")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_playlist)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 211, 61))
        self.label_6.setStyleSheet("font: 22pt \"Yellowtail\";\n"
"selection-color: rgb(255, 0, 0);\n"
"color: rgb(85, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"")
        self.label_6.setObjectName("label_6")
        self.widget_generateur_accords = QtWidgets.QWidget(parent=self.widget_playlist)
        self.widget_generateur_accords.setGeometry(QtCore.QRect(800, 10, 331, 301))
        self.widget_generateur_accords.setObjectName("widget_generateur_accords")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_musique, "")
        self.tab_programmation = QtWidgets.QWidget()
        self.tab_programmation.setObjectName("tab_programmation")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_programmation)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 1871, 311))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_ide_realtime = QtWidgets.QWidget(parent=self.horizontalLayoutWidget_2)
        self.widget_ide_realtime.setObjectName("widget_ide_realtime")
        self.horizontalLayout_2.addWidget(self.widget_ide_realtime)
        self.widget_terminal = QtWidgets.QWidget(parent=self.horizontalLayoutWidget_2)
        self.widget_terminal.setObjectName("widget_terminal")
        self.horizontalLayout_2.addWidget(self.widget_terminal)
        self.tabWidget.addTab(self.tab_programmation, "")
        self.tab_montage_video = QtWidgets.QWidget()
        self.tab_montage_video.setObjectName("tab_montage_video")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(parent=self.tab_montage_video)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(-1, 9, 1891, 321))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_viewer_3d = QtWidgets.QWidget(parent=self.gridLayoutWidget_5)
        self.widget_viewer_3d.setObjectName("widget_viewer_3d")
        self.quickWidget = QtQuickWidgets.QQuickWidget(parent=self.widget_viewer_3d)
        self.quickWidget.setGeometry(QtCore.QRect(1309, 9, 571, 301))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(parent=self.widget_viewer_3d)
        self.openGLWidget_2.setGeometry(QtCore.QRect(899, 9, 401, 301))
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_viewer_3d)
        self.widget_6.setGeometry(QtCore.QRect(19, 29, 851, 271))
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_5.addWidget(self.widget_viewer_3d, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_montage_video, "")
        self.tab_AI = QtWidgets.QWidget()
        self.tab_AI.setObjectName("tab_AI")
        self.stackedWidgetAI = QtWidgets.QStackedWidget(parent=self.tab_AI)
        self.stackedWidgetAI.setGeometry(QtCore.QRect(629, 9, 1251, 311))
        self.stackedWidgetAI.setObjectName("stackedWidgetAI")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidgetAI.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidgetAI.addWidget(self.page_6)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_AI)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout.addWidget(self.comboBox_4)
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout.addWidget(self.comboBox_5)
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.comboBox_6 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.verticalLayout.addWidget(self.comboBox_6)
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.comboBox_7 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.verticalLayout.addWidget(self.comboBox_7)
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.comboBox_8 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox_8.setObjectName("comboBox_8")
        self.verticalLayout.addWidget(self.comboBox_8)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalSlider = QtWidgets.QSlider(parent=self.tab_AI)
        self.horizontalSlider.setGeometry(QtCore.QRect(130, 310, 481, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_13 = QtWidgets.QLabel(parent=self.tab_AI)
        self.label_13.setGeometry(QtCore.QRect(0, 310, 121, 16))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_AI, "")
        self.tab_perso = QtWidgets.QWidget()
        self.tab_perso.setObjectName("tab_perso")
        self.tabWidget.addTab(self.tab_perso, "")
        self.tab_jeux = QtWidgets.QWidget()
        self.tab_jeux.setObjectName("tab_jeux")
        self.tabWidget.addTab(self.tab_jeux, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 2, 1)
        self.progressBar = QtWidgets.QProgressBar(parent=self.gridLayoutWidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 5))
        self.progressBar.setBaseSize(QtCore.QSize(0, 0))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1891, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_4.setMinimumSize(QtCore.QSize(1280, 0))
        self.widget_4.setBaseSize(QtCore.QSize(0, 0))
        self.widget_4.setObjectName("widget_4")
        self.opengl3dvisual = QtWidgets.QOpenGLWidget(parent=self.widget_4)
        self.opengl3dvisual.setGeometry(QtCore.QRect(0, 10, 1281, 381))
        self.opengl3dvisual.setMinimumSize(QtCore.QSize(621, 0))
        self.opengl3dvisual.setObjectName("opengl3dvisual")
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(270, 810, 1249, 262))
        self.widget.setObjectName("widget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, -1, 421, 241))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.widget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(1090, 180, 160, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.gridLayoutWidget_3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(439, 9, 811, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 809, 249))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 211, 31))
        self.label_5.setStyleSheet("font: 22pt \"Yellowtail\";")
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_5.setScaledContents(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(780, 0, 21, 241))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_3.raise_()
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(19, 819, 254, 241))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalSlider_9 = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.gridLayout_4.addWidget(self.verticalSlider_9, 0, 1, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_4.addWidget(self.verticalSlider, 0, 0, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout_4.addWidget(self.verticalSlider_2, 0, 8, 1, 1)
        self.verticalSlider_4 = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.gridLayout_4.addWidget(self.verticalSlider_4, 0, 6, 1, 1)
        self.verticalSlider_8 = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider_8.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.gridLayout_4.addWidget(self.verticalSlider_8, 0, 2, 1, 1)
        self.verticalSlider_5 = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.gridLayout_4.addWidget(self.verticalSlider_5, 0, 5, 1, 1)
        self.verticalSlider_3 = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.gridLayout_4.addWidget(self.verticalSlider_3, 0, 7, 1, 1)
        self.verticalSlider_6 = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.gridLayout_4.addWidget(self.verticalSlider_6, 0, 4, 1, 1)
        self.verticalSlider_7 = QtWidgets.QSlider(parent=self.gridLayoutWidget_4)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.gridLayout_4.addWidget(self.verticalSlider_7, 0, 3, 1, 1)
        self.widget_5 = QtWidgets.QWidget(parent=Form)
        self.widget_5.setGeometry(QtCore.QRect(1550, 820, 351, 251))
        self.widget_5.setObjectName("widget_5")
        self.openGLWidget = QtWidgets.QOpenGLWidget(parent=self.widget_5)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, 351, 251))
        self.openGLWidget.setObjectName("openGLWidget")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.verticalScrollBar_2.sliderMoved['int'].connect(self.scrollArea_2.update) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Soundcloud Player"))
        self.label_6.setText(_translate("Form", "Playlist automatisée"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_musique), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_programmation), _translate("Form", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_montage_video), _translate("Form", "Page"))
        self.label_12.setText(_translate("Form", "TextLabel"))
        self.label_8.setText(_translate("Form", "TextLabel"))
        self.label_9.setText(_translate("Form", "TextLabel"))
        self.label_10.setText(_translate("Form", "TextLabel"))
        self.label_11.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.label_13.setText(_translate("Form", "Slider"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_AI), _translate("Form", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_perso), _translate("Form", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_jeux), _translate("Form", "Page"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "SCROLL AREA"))
from PySide6 import QtQuickWidgets