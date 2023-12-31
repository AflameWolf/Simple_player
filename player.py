# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Simple_player(object):

    def horizontalSlider_reg(self):
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(0, 120, 350, 22))
        self.horizontalSlider.setStyleSheet("\n"
                                            "background-color: rgb(0, 0, 0);\n"
                                            "border: 4px solid #7922CC;\n"
                                            "border-color: rgb(220, 152, 107);\n"
                                            "border-radius:2px;")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
    def dial_volume_reg(self):
        self.dial_volume = QtWidgets.QDial(self.centralwidget)
        self.dial_volume.setGeometry(QtCore.QRect(20, 20, 50, 64))
        self.dial_volume.setObjectName("dial_volume")
    def label_v0_reg(self):
        self.label_v0 = QtWidgets.QLabel(self.centralwidget)
        self.label_v0.setGeometry(QtCore.QRect(20, 70, 16, 16))
        self.label_v0.setStyleSheet("background-color: rgb(139, 139, 139);\n"
                                    "border: 1px solid #7922CC;\n"
                                    "border-radius:2px;")
        self.label_v0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v0.setObjectName("label_v0")
    def label_v100_reg(self):
        self.label_v100 = QtWidgets.QLabel(self.centralwidget)
        self.label_v100.setGeometry(QtCore.QRect(50, 70, 21, 16))
        self.label_v100.setStyleSheet("background-color: rgb(139, 139, 139);\n"
                                      "border: 1px solid #7922CC;\n"
                                      "border-radius:2px;")
        self.label_v100.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v100.setObjectName("label_v100")
    def layoutWidget_reg(self):
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 150, 181, 31))
        self.layoutWidget.setObjectName("layoutWidget")

    def horizontalLayout_reg(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

    def pushButton_time_back_reg(self):
        self.pushButton_time_back = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_time_back.setFont(font)
        self.pushButton_time_back.setStyleSheet("background-color: rgb(231, 169, 62);\n"
                                                "border-radius: 8px;")
        self.pushButton_time_back.setAutoDefault(False)
        self.pushButton_time_back.setObjectName("pushButton_time_back")
        self.horizontalLayout.addWidget(self.pushButton_time_back)
    def pushButton_stop_play_reg(self):
        self.pushButton_stop_play = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_stop_play.setFont(font)
        self.pushButton_stop_play.setStyleSheet("background-color: rgb(231, 169, 62);\n"
                                                "border-radius: 8px;")
        self.pushButton_stop_play.setAutoDefault(False)
        self.pushButton_stop_play.setObjectName("pushButton_stop_play")
        self.horizontalLayout.addWidget(self.pushButton_stop_play)
    def pushButton_time_forward_reg(self):
        self.pushButton_time_forward = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_time_forward.setFont(font)
        self.pushButton_time_forward.setStyleSheet("background-color: rgb(231, 169, 62);\n"
                                                   "border-radius: 8px;")
        self.pushButton_time_forward.setAutoDefault(False)
        self.pushButton_time_forward.setObjectName("pushButton_time_forward")
        self.horizontalLayout.addWidget(self.pushButton_time_forward)
    def pushButton_choice_track_reg(self):
        self.pushButton_choice_track = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choice_track.setGeometry(QtCore.QRect(110, 20, 221, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_choice_track.setFont(font)
        self.pushButton_choice_track.setStyleSheet("background-color: rgb(216, 73, 73);\n"
                                                   "border-radius: 8px;")
        self.pushButton_choice_track.setObjectName("pushButton_choice_track")
    def label_track_name_reg(self):
        self.label_track_name = QtWidgets.QLabel(self.centralwidget)
        self.label_track_name.setGeometry(QtCore.QRect(110, 59, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_track_name.setFont(font)
        self.label_track_name.setObjectName("label_track_name")

    def setupUi(self, Simple_player):
        Simple_player.setObjectName("Simple_player")
        Simple_player.resize(350, 191)
        Simple_player.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.centralwidget = QtWidgets.QWidget(Simple_player)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider_reg()
        self.dial_volume_reg()
        self.label_v0_reg()
        self.label_v100_reg()
        self.layoutWidget_reg()
        self.horizontalLayout_reg()
        self.pushButton_time_back_reg()
        self.pushButton_stop_play_reg()
        self.pushButton_time_forward_reg()
        self.pushButton_choice_track_reg()
        self.label_track_name_reg()


        self.layoutWidget.raise_()
        self.horizontalSlider.raise_()
        self.label_v0.raise_()
        self.label_v100.raise_()
        self.dial_volume.raise_()
        self.pushButton_choice_track.raise_()
        self.label_track_name.raise_()
        Simple_player.setCentralWidget(self.centralwidget)
        self.retranslateUi(Simple_player)
        QtCore.QMetaObject.connectSlotsByName(Simple_player)

        """Доп история"""
        self.app = QtWidgets.QApplication([])
        self.media_player = QMediaPlayer()
        self.add_func()
    def retranslateUi(self, Simple_player):
        _translate = QtCore.QCoreApplication.translate
        Simple_player.setWindowTitle(_translate("Simple_player", "MainWindow"))
        self.label_v0.setText(_translate("Simple_player", "0"))
        self.label_v100.setText(_translate("Simple_player", "100"))
        self.pushButton_time_back.setText(_translate("Simple_player", "<"))
        self.pushButton_stop_play.setText(_translate("Simple_player", "||"))
        self.pushButton_time_forward.setText(_translate("Simple_player", ">"))
        self.pushButton_choice_track.setText(_translate("Simple_player", "Выбор музыки"))
        self.label_track_name.setText(_translate("Simple_player", "Имя трека"))

    def add_func(self):
        self.pushButton_choice_track.clicked.connect(self.choice_track)
        self.pushButton_time_forward.clicked.connect(self.time_forward)
        self.pushButton_time_back.clicked.connect(self.time_back)
        self.pushButton_stop_play.clicked.connect(self.stop_or_play)
        self.horizontalSlider.sliderReleased.connect(self.set_music_slider_position)
        """Настройки громкости при изменении позиции"""
        self.dial_volume.sliderMoved.connect(self.set_volume)
        """При изменении длинны трека отсылаем сигнал"""
        self.media_player.durationChanged.connect(self.get_media_player_duration)
        self.media_player.positionChanged.connect(self.set_slider_position)

    def choice_track(self):
        self.wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.label_track_name.setText(self.wb_patch[self.wb_patch.rfind("/")+1::])
        self.url = QUrl.fromLocalFile(self.wb_patch)
        self.content = QMediaContent(self.url)
        self.play_music(self.content)

    def play_music(self,content):
        self.media_player.setMedia(content)
        self.dial_volume.setSliderPosition(self.media_player.volume())
        self.media_player.play()

    def get_media_player_duration(self):
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.media_player.duration())

    def time_forward(self):
        self.media_player.setPosition(self.media_player.position()+5*1000)
    def time_back(self):
        self.media_player.setPosition(self.media_player.position()-5*1000)

    def stop_or_play(self):
        i = self.media_player.state()
        if i ==1:
            self.media_player.pause()
            self.pushButton_stop_play.setText(">")
        else:
            self.media_player.play()
            self.pushButton_stop_play.setText("||")

    def set_slider_position(self):
        self.horizontalSlider.setSliderPosition(self.media_player.position())

    def set_music_slider_position(self):
        self.media_player.setPosition(self.horizontalSlider.value())

    def set_volume(self):
        self.media_player.setVolume(self.dial_volume.value())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Simple_player = QtWidgets.QMainWindow()
    ui = Ui_Simple_player()
    ui.setupUi(Simple_player)
    Simple_player.show()
    sys.exit(app.exec_())



