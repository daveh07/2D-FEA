# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1073, 772)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainContainer = QFrame(self.frame)
        self.MainContainer.setObjectName(u"MainContainer")
        self.MainContainer.setFrameShape(QFrame.NoFrame)
        self.MainContainer.setFrameShadow(QFrame.Plain)
        self.MainContainer.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.MainContainer)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.PlateRenderContainer = QFrame(self.MainContainer)
        self.PlateRenderContainer.setObjectName(u"PlateRenderContainer")
        self.PlateRenderContainer.setFrameShape(QFrame.NoFrame)
        self.PlateRenderContainer.setFrameShadow(QFrame.Plain)
        self.PlateRenderContainer.setLineWidth(0)

        self.horizontalLayout_14.addWidget(self.PlateRenderContainer)

        self.ToolBarContainer = QFrame(self.MainContainer)
        self.ToolBarContainer.setObjectName(u"ToolBarContainer")
        self.ToolBarContainer.setMaximumSize(QSize(70, 16777215))
        self.ToolBarContainer.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.ToolBarContainer.setFrameShape(QFrame.NoFrame)
        self.ToolBarContainer.setFrameShadow(QFrame.Plain)
        self.ToolBarContainer.setLineWidth(0)
        self.verticalLayout_22 = QVBoxLayout(self.ToolBarContainer)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.ToolBarContainer)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(70, 70))
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Plain)
        self.frame_34.setLineWidth(0)

        self.verticalLayout_22.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.ToolBarContainer)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(70, 70))
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Plain)
        self.frame_35.setLineWidth(0)
        self.verticalLayout_26 = QVBoxLayout(self.frame_35)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_35)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 50))
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(16, 79, 101);")

        self.verticalLayout_26.addWidget(self.pushButton)


        self.verticalLayout_22.addWidget(self.frame_35, 0, Qt.AlignHCenter)

        self.frame_36 = QFrame(self.ToolBarContainer)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(70, 70))
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Plain)
        self.frame_36.setLineWidth(0)
        self.verticalLayout_25 = QVBoxLayout(self.frame_36)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_36)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setMaximumSize(QSize(50, 50))
        self.pushButton_3.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(16, 79, 101);")

        self.verticalLayout_25.addWidget(self.pushButton_3)


        self.verticalLayout_22.addWidget(self.frame_36, 0, Qt.AlignHCenter)

        self.frame_37 = QFrame(self.ToolBarContainer)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(70, 70))
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Plain)
        self.frame_37.setLineWidth(0)
        self.verticalLayout_24 = QVBoxLayout(self.frame_37)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_37)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 50))
        self.pushButton_4.setMaximumSize(QSize(50, 50))
        self.pushButton_4.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(16, 79, 101);")

        self.verticalLayout_24.addWidget(self.pushButton_4)


        self.verticalLayout_22.addWidget(self.frame_37, 0, Qt.AlignHCenter)

        self.frame_38 = QFrame(self.ToolBarContainer)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(70, 70))
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Plain)
        self.frame_38.setLineWidth(0)
        self.verticalLayout_23 = QVBoxLayout(self.frame_38)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_38)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(50, 50))
        self.pushButton_5.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(16, 79, 101);")

        self.verticalLayout_23.addWidget(self.pushButton_5)


        self.verticalLayout_22.addWidget(self.frame_38, 0, Qt.AlignHCenter)

        self.frame_39 = QFrame(self.ToolBarContainer)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Plain)
        self.frame_39.setLineWidth(0)

        self.verticalLayout_22.addWidget(self.frame_39)


        self.horizontalLayout_14.addWidget(self.ToolBarContainer)


        self.verticalLayout_2.addWidget(self.MainContainer)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 140))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(350, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.frame_7.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(175, 0))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.frame_16.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.WidthInput = QLineEdit(self.frame_16)
        self.WidthInput.setObjectName(u"WidthInput")

        self.horizontalLayout_5.addWidget(self.WidthInput)


        self.horizontalLayout_4.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(175, 0))
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Plain)
        self.frame_17.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.frame_17)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.frame_17)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.frame_9.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_9)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(175, 0))
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Plain)
        self.frame_18.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_18)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.LengthInput = QLineEdit(self.frame_18)
        self.LengthInput.setObjectName(u"LengthInput")

        self.verticalLayout_6.addWidget(self.LengthInput)


        self.horizontalLayout_3.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(175, 0))
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Plain)
        self.frame_19.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frame_19)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_19)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_9.addWidget(self.label_2)


        self.horizontalLayout_3.addWidget(self.frame_19)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.frame_8.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(175, 0))
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.frame_20.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.frame_20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ThicknessInput = QLineEdit(self.frame_20)
        self.ThicknessInput.setObjectName(u"ThicknessInput")

        self.verticalLayout_7.addWidget(self.ThicknessInput)


        self.horizontalLayout_2.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_8)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(175, 0))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Plain)
        self.frame_21.setLineWidth(0)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_21)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_13.addWidget(self.label_3)

        self.frame_2 = QFrame(self.frame_21)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 0, 0, 5)
        self.RenderPlateBtn = QPushButton(self.frame_2)
        self.RenderPlateBtn.setObjectName(u"RenderPlateBtn")
        self.RenderPlateBtn.setMinimumSize(QSize(60, 50))
        self.RenderPlateBtn.setMaximumSize(QSize(85, 16777215))
        self.RenderPlateBtn.setStyleSheet(u"background-color: rgb(143, 240, 164);")
        self.RenderPlateBtn.setFlat(False)

        self.verticalLayout_10.addWidget(self.RenderPlateBtn)


        self.horizontalLayout_13.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.frame_21)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(350, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.frame_10.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_10)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(175, 0))
        self.frame_22.setMaximumSize(QSize(16777215, 30))
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Plain)
        self.frame_22.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 0, 10, 0)
        self.ElementTypeInput = QComboBox(self.frame_22)
        self.ElementTypeInput.addItem("")
        self.ElementTypeInput.addItem("")
        self.ElementTypeInput.setObjectName(u"ElementTypeInput")

        self.horizontalLayout_9.addWidget(self.ElementTypeInput)


        self.horizontalLayout_8.addWidget(self.frame_22)

        self.frame_25 = QFrame(self.frame_10)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(175, 0))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Plain)
        self.frame_25.setLineWidth(0)
        self.verticalLayout_11 = QVBoxLayout(self.frame_25)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.frame_25)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_11.addWidget(self.label_5)


        self.horizontalLayout_8.addWidget(self.frame_25)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Plain)
        self.frame_11.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_11)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(175, 0))
        self.frame_23.setMaximumSize(QSize(16777215, 30))
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Plain)
        self.frame_23.setLineWidth(0)
        self.verticalLayout_13 = QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 0, 10, 0)
        self.MeshSizeInput = QLineEdit(self.frame_23)
        self.MeshSizeInput.setObjectName(u"MeshSizeInput")

        self.verticalLayout_13.addWidget(self.MeshSizeInput)


        self.horizontalLayout_7.addWidget(self.frame_23)

        self.frame_26 = QFrame(self.frame_11)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(175, 0))
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Plain)
        self.frame_26.setLineWidth(0)
        self.verticalLayout_12 = QVBoxLayout(self.frame_26)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_4 = QLabel(self.frame_26)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_12.addWidget(self.label_4)


        self.horizontalLayout_7.addWidget(self.frame_26)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Plain)
        self.frame_12.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_12)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(175, 80))
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Plain)
        self.frame_24.setLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.frame_24)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.GenerateMeshBtn = QPushButton(self.frame_24)
        self.GenerateMeshBtn.setObjectName(u"GenerateMeshBtn")

        self.verticalLayout_14.addWidget(self.GenerateMeshBtn)

        self.toggleHoleBtn = QPushButton(self.frame_24)
        self.toggleHoleBtn.setObjectName(u"toggleHoleBtn")

        self.verticalLayout_14.addWidget(self.toggleHoleBtn)


        self.horizontalLayout_6.addWidget(self.frame_24, 0, Qt.AlignTop)

        self.frame_27 = QFrame(self.frame_12)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(175, 0))
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Plain)
        self.frame_27.setLineWidth(0)
        self.verticalLayout_21 = QVBoxLayout(self.frame_27)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.MaterialPropertiesInput = QComboBox(self.frame_27)
        self.MaterialPropertiesInput.addItem("")
        self.MaterialPropertiesInput.addItem("")
        self.MaterialPropertiesInput.setObjectName(u"MaterialPropertiesInput")

        self.verticalLayout_21.addWidget(self.MaterialPropertiesInput)


        self.horizontalLayout_6.addWidget(self.frame_27)


        self.verticalLayout_4.addWidget(self.frame_12)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(350, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(350, 16777215))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.frame_13.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_13)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Plain)
        self.frame_28.setLineWidth(0)
        self.verticalLayout_16 = QVBoxLayout(self.frame_28)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.SupportConditionsInput = QComboBox(self.frame_28)
        self.SupportConditionsInput.addItem("")
        self.SupportConditionsInput.addItem("")
        self.SupportConditionsInput.addItem("")
        self.SupportConditionsInput.addItem("")
        self.SupportConditionsInput.setObjectName(u"SupportConditionsInput")

        self.verticalLayout_16.addWidget(self.SupportConditionsInput)


        self.horizontalLayout_10.addWidget(self.frame_28)

        self.frame_31 = QFrame(self.frame_13)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Plain)
        self.frame_31.setLineWidth(0)
        self.verticalLayout_15 = QVBoxLayout(self.frame_31)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_31)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_15.addWidget(self.label_6)


        self.horizontalLayout_10.addWidget(self.frame_31)


        self.verticalLayout_5.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.frame_15.setLineWidth(0)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_15)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(175, 0))
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Plain)
        self.frame_30.setLineWidth(0)
        self.verticalLayout_17 = QVBoxLayout(self.frame_30)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.LoadInput = QLineEdit(self.frame_30)
        self.LoadInput.setObjectName(u"LoadInput")

        self.verticalLayout_17.addWidget(self.LoadInput)


        self.horizontalLayout_11.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.frame_15)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(175, 0))
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Plain)
        self.frame_29.setLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.frame_29)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_29)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_18.addWidget(self.label_7)


        self.horizontalLayout_11.addWidget(self.frame_29)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Plain)
        self.frame_14.setLineWidth(0)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_14)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(175, 0))
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Plain)
        self.frame_32.setLineWidth(0)
        self.verticalLayout_20 = QVBoxLayout(self.frame_32)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.comboBox_4 = QComboBox(self.frame_32)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_20.addWidget(self.comboBox_4)


        self.horizontalLayout_12.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_14)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(175, 0))
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Plain)
        self.frame_33.setLineWidth(0)
        self.verticalLayout_19 = QVBoxLayout(self.frame_33)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_33)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(153, 193, 241);")

        self.verticalLayout_19.addWidget(self.pushButton_2)


        self.horizontalLayout_12.addWidget(self.frame_33)


        self.verticalLayout_5.addWidget(self.frame_14)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Nodes", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Holes", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Width (m)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Length (m)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Thickness (m)", None))
        self.RenderPlateBtn.setText(QCoreApplication.translate("MainWindow", u"Render Plate", None))
        self.ElementTypeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Tri3", None))
        self.ElementTypeInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Quad4", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Element Type", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mesh Size", None))
        self.GenerateMeshBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Mesh", None))
        self.toggleHoleBtn.setText(QCoreApplication.translate("MainWindow", u"Add Opening", None))
        self.MaterialPropertiesInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Steel", None))
        self.MaterialPropertiesInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Concrete", None))

        self.SupportConditionsInput.setItemText(0, QCoreApplication.translate("MainWindow", u"1-Side Supported", None))
        self.SupportConditionsInput.setItemText(1, QCoreApplication.translate("MainWindow", u"2-Sides Supported", None))
        self.SupportConditionsInput.setItemText(2, QCoreApplication.translate("MainWindow", u"2-Sides Supported", None))
        self.SupportConditionsInput.setItemText(3, QCoreApplication.translate("MainWindow", u"4-Sides Supported", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Support Conditions", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Normal Pressure (kPa)", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Applied X Dir", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Applied Y Dir", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Applied Z Dir", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Run Analysis", None))
    # retranslateUi

