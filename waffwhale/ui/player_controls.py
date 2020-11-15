# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/player_controls.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlayerControls(object):
    def setupUi(self, PlayerControls):
        PlayerControls.setObjectName("PlayerControls")
        PlayerControls.resize(978, 84)
        PlayerControls.setMinimumSize(QtCore.QSize(0, 84))
        PlayerControls.setMaximumSize(QtCore.QSize(16777215, 84))
        PlayerControls.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(PlayerControls)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(PlayerControls)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cover_art = QtWidgets.QPushButton(self.frame_2)
        self.cover_art.setMinimumSize(QtCore.QSize(84, 84))
        self.cover_art.setMaximumSize(QtCore.QSize(84, 84))
        self.cover_art.setText("")
        self.cover_art.setObjectName("cover_art")
        self.horizontalLayout_3.addWidget(self.cover_art)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.title = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.artist = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.artist.setFont(font)
        self.artist.setObjectName("artist")
        self.horizontalLayout_2.addWidget(self.artist)
        self.divider = QtWidgets.QLabel(self.frame)
        self.divider.setAlignment(QtCore.Qt.AlignCenter)
        self.divider.setObjectName("divider")
        self.horizontalLayout_2.addWidget(self.divider)
        self.album = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.album.setFont(font)
        self.album.setObjectName("album")
        self.horizontalLayout_2.addWidget(self.album)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.fav = QtWidgets.QPushButton(self.frame_2)
        self.fav.setMinimumSize(QtCore.QSize(44, 44))
        self.fav.setMaximumSize(QtCore.QSize(44, 44))
        self.fav.setText("")
        self.fav.setObjectName("fav")
        self.horizontalLayout_3.addWidget(self.fav)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.playlist = QtWidgets.QPushButton(self.frame_2)
        self.playlist.setMinimumSize(QtCore.QSize(44, 44))
        self.playlist.setMaximumSize(QtCore.QSize(44, 44))
        self.playlist.setText("")
        self.playlist.setObjectName("playlist")
        self.horizontalLayout_3.addWidget(self.playlist)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.hide = QtWidgets.QPushButton(self.frame_2)
        self.hide.setMinimumSize(QtCore.QSize(44, 44))
        self.hide.setMaximumSize(QtCore.QSize(44, 44))
        self.hide.setText("")
        self.hide.setObjectName("hide")
        self.horizontalLayout_3.addWidget(self.hide)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.prev = QtWidgets.QPushButton(self.frame_2)
        self.prev.setMinimumSize(QtCore.QSize(44, 44))
        self.prev.setMaximumSize(QtCore.QSize(44, 44))
        self.prev.setText("")
        self.prev.setObjectName("prev")
        self.horizontalLayout_3.addWidget(self.prev)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.play = QtWidgets.QPushButton(self.frame_2)
        self.play.setMinimumSize(QtCore.QSize(44, 44))
        self.play.setMaximumSize(QtCore.QSize(44, 44))
        self.play.setText("")
        self.play.setObjectName("play")
        self.horizontalLayout_3.addWidget(self.play)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.next = QtWidgets.QPushButton(self.frame_2)
        self.next.setMinimumSize(QtCore.QSize(44, 44))
        self.next.setMaximumSize(QtCore.QSize(44, 44))
        self.next.setText("")
        self.next.setObjectName("next")
        self.horizontalLayout_3.addWidget(self.next)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.mute = QtWidgets.QPushButton(self.frame_2)
        self.mute.setMinimumSize(QtCore.QSize(44, 44))
        self.mute.setMaximumSize(QtCore.QSize(44, 44))
        self.mute.setText("")
        self.mute.setObjectName("mute")
        self.horizontalLayout_3.addWidget(self.mute)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.volume = QtWidgets.QSlider(self.frame_2)
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setObjectName("volume")
        self.horizontalLayout_3.addWidget(self.volume)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.queue = QtWidgets.QPushButton(self.frame_2)
        self.queue.setMinimumSize(QtCore.QSize(44, 44))
        self.queue.setMaximumSize(QtCore.QSize(44, 44))
        self.queue.setText("")
        self.queue.setObjectName("queue")
        self.horizontalLayout_3.addWidget(self.queue)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(PlayerControls)
        QtCore.QMetaObject.connectSlotsByName(PlayerControls)

    def retranslateUi(self, PlayerControls):
        _translate = QtCore.QCoreApplication.translate
        PlayerControls.setWindowTitle(_translate("PlayerControls", "Form"))
        self.title.setText(_translate("PlayerControls", "Track Title"))
        self.artist.setText(_translate("PlayerControls", "Artist"))
        self.divider.setText(_translate("PlayerControls", " / "))
        self.album.setText(_translate("PlayerControls", "Album"))
