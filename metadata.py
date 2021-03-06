# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import eyed3
import os, stat

class Ui_Dialog:
    def __init__(self, filename):
        self.path = filename
        self.audiofile = eyed3.load(self.path)
        global audioobject
        audioobject = eyed3.load(filename)
        self.artist_name = self.audiofile.tag.artist
        self.album_name = self.audiofile.tag.album
        self.song_title = self.audiofile.tag.title
        self.release_date = str(self.audiofile.tag.release_date)
        self.publisher = self.audiofile.tag.publisher
        self.pathfull = self.path

    def images_path_mp3(self):
        self.data_img = ''
        for image in self.audiofile.tag.images:
            image_file = open("{0} - {1}({2}).jpg".format(self.artist_name, self.album_name, image.picture_type), "wb")
            image_file.write(image.image_data)
            self.data_img = (f"{self.artist_name} - {self.album_name}({image.picture_type}).jpg")
            image_file.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        Dialog.setMinimumSize(QtCore.QSize(700, 500))
        Dialog.setMaximumSize(QtCore.QSize(700, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);\n""")

        self.label_metadata = QtWidgets.QLabel(Dialog)
        self.label_metadata.setGeometry(QtCore.QRect(290, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_metadata.setFont(font)
        self.label_metadata.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_metadata.setObjectName("label_metadata")

        self.label_artist = QtWidgets.QLabel(Dialog)
        self.label_artist.setGeometry(QtCore.QRect(10, 80, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_artist.setFont(font)
        self.label_artist.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_artist.setObjectName("label_artist")
        self.lineEdit_artist = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_artist.setGeometry(QtCore.QRect(90, 80, 181, 20))
        self.lineEdit_artist.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_artist.setObjectName("lineEdit_artist")

        self.label_album = QtWidgets.QLabel(Dialog)
        self.label_album.setGeometry(QtCore.QRect(10, 140, 71, 21))
        self.label_album.setFont(font)
        self.label_album.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_album.setObjectName("label_album")
        self.lineEdit_album = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_album.setGeometry(QtCore.QRect(90, 140, 181, 20))
        self.lineEdit_album.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_album.setObjectName("lineEdit_album")

        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(10, 200, 71, 21))
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setObjectName("label_title")
        self.lineEdit_title = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_title.setGeometry(QtCore.QRect(90, 200, 181, 20))
        self.lineEdit_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_title.setObjectName("lineEdit_title")
        
        self.label_release = QtWidgets.QLabel(Dialog)
        self.label_release.setGeometry(QtCore.QRect(10, 260, 71, 21))
        self.label_release.setFont(font)
        self.label_release.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_release.setObjectName("label_release")
        self.lineEdit_release = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_release.setGeometry(QtCore.QRect(90, 260, 181, 20))
        self.lineEdit_release.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_release.setObjectName("lineEdit_release")

        self.label_publisher = QtWidgets.QLabel(Dialog)
        self.label_publisher.setGeometry(QtCore.QRect(10, 320, 71, 21))
        self.label_publisher.setFont(font)
        self.label_publisher.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_publisher.setObjectName("label_publisher")
        self.lineEdit_publisher = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_publisher.setGeometry(QtCore.QRect(90, 320, 181, 20))
        self.lineEdit_publisher.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")

        self.label_mp3img = QtWidgets.QLabel(Dialog)
        self.label_mp3img.setGeometry(QtCore.QRect(310, 60, 371, 351))
        self.label_mp3img.setFont(font)
        self.label_mp3img.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_mp3img.setText("")
        self.images_path_mp3()
        if self.data_img != '':
            self.label_mp3img.setPixmap(QtGui.QPixmap(self.data_img)) #change picture here
            os.remove(self.data_img)
        else:
            self.label_mp3img.setPixmap(QtGui.QPixmap(''))
        self.label_mp3img.setObjectName("label_mp3img")

        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(280, 440, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(85, 255, 0);\n""border-radius: 10px;")
        self.pushButton_save.setObjectName("pushButton_save")

        self.pushButton_changepic = QtWidgets.QPushButton(Dialog)
        self.pushButton_changepic.setGeometry(QtCore.QRect(120, 370, 91, 23))
        self.pushButton_changepic.setStyleSheet("background-color: rgb(34, 56, 255);\n""color: rgb(255, 255, 255);")
        self.pushButton_changepic.setObjectName("pushButton_changepic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_save.clicked.connect(self.save_clicked)
        self.pushButton_changepic.clicked.connect(self.changepic_clicked)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_artist.setText(_translate("Dialog", "Artist"))
        self.label_album.setText(_translate("Dialog", "Album"))
        self.label_title.setText(_translate("Dialog", "Title"))
        self.label_metadata.setText(_translate("Dialog", "METADATA"))
        self.label_release.setText(_translate("Dialog", "Release"))
        self.label_publisher.setText(_translate("Dialog", "Publisher"))
        self.pushButton_save.setText(_translate("Dialog", "SAVE"))
        self.pushButton_changepic.setText(_translate("Dialog", "Change Picture"))
        self.lineEdit_artist.setText(_translate("Dialog", self.artist_name))
        self.lineEdit_album.setText(_translate("Dialog", self.album_name))
        self.lineEdit_title.setText(_translate("Dialog", self.song_title))
        self.lineEdit_release.setText(_translate("Dialog", self.release_date))
        self.lineEdit_publisher.setText(_translate("Dialog", self.publisher))

    def save_clicked(self):
        self.audiofile.tag.artist = self.lineEdit_artist.text()
        self.audiofile.tag.album = self.lineEdit_album.text()
        self.audiofile.tag.title = self.lineEdit_title.text()
        self.audiofile.tag.release_date = self.lineEdit_release.text()
        self.audiofile.tag.publisher = self.lineEdit_publisher.text()
        os.chmod(self.path, stat.S_IRWXO)
        os.chmod(self.path, stat.S_IRWXU)
        self.audiofile.tag.save()
        print("Metadata Update Successfully!")

    
    def changepic_clicked(self):
        file_changepic = QFileDialog.getOpenFileName(None, "mp3 image", "", "image (*.jpg *.png *.jpeg)")

        if file_changepic != ('', ''):
            path_changepic = file_changepic[0]
            image_data_changepic = open(path_changepic,"r+b").read()
            if path_changepic.endswith('.jpg') or path_changepic.endswith('.jpg'):
                self.audiofile.tag.images.set(3, image_data_changepic, "images/jpg")
            elif path_changepic.endswith('.png'):
                self.audiofile.tag.images.set(3, image_data_changepic, "images/png")
            self.audiofile.tag.save()
            self.images_path_mp3()
            self.label_mp3img.setPixmap(QtGui.QPixmap(self.data_img))
            os.remove(self.data_img)
        else:
            print("No picture selected!")

    