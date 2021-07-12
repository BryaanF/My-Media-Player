from PyQt5.QtWidgets import QApplication, QComboBox, QStackedWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog, QMenuBar
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QFont, QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
from PyQt5 import QtGui, QtWidgets
from metadata import Ui_Dialog
import eyed3
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # set pixmap for mp3 image
        self.label_mp3img = QtWidgets.QLabel()
        self.label_mp3img.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_mp3img.setObjectName("label_mp3img")

        # set window title and icon
        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('icon/play.png'))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.init_ui()
        
        self.show()


    def init_ui(self):
        #initiate filename (path file) to empty string
        self.pathfile = ''
        
        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        #create videowidget object
        videowidget = QVideoWidget()

        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)

        #Create edit metadata button
        editMetadata = QPushButton('Metadata')
        editMetadata.clicked.connect(self.edit_metadata)

        #create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)

        #create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        #adding dropdown menu combo box
        comboBox = QtWidgets.QComboBox(self)
        comboBox.addItem("Open File")
        comboBox.addItem("Metadata")
        comboBox.setFont(QFont('Open Sans', 12))
        comboBox.activated[str].connect(self.comboBox_action)

        #make stacked widget to accomodate image show or video show
        #image show is for mp3 file
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.label_mp3img)
        self.Stack.addWidget(videowidget)

        #create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)

        #set widgets in hbox layout format
        # hboxLayout.addWidget(openBtn)
        # hboxLayout.addWidget(editMetadata)
        hboxLayout.addWidget(comboBox)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)

        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.Stack)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)

        #setting layout in vertical manner
        self.setLayout(vboxLayout)

        #set video output of module media player refer from videowidget var
        #videowidget var itself is from QVideoWidget that work as widget
        self.mediaPlayer.setVideoOutput(videowidget)


        #media player signals to play and pause media
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)


    def comboBox_action(self, text):
        if text == "Open File":
            self.open_file()
        if text == "Metadata":
            self.edit_metadata()

    def open_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        
        if self.filename != '' and self.filename.endswith('.mp3'):
            self.setGeometry(350, 150, 400, 600)
            self.setMaximumWidth(400)
            self.setMinimumWidth(400)
            self.setMaximumHeight(500)
            self.setMinimumHeight(500)
            self.Stack.setCurrentIndex(0)
            audiofile = eyed3.load(self.filename)
            album_name = audiofile.tag.album
            artist_name = audiofile.tag.artist
            data_img = ''
            for image in audiofile.tag.images:
                image_file = open("{0} - {1}({2}).jpg".format(artist_name, album_name, image.picture_type), "wb")
                image_file.write(image.image_data)
                data_img = (f"{artist_name} - {album_name}({image.picture_type}).jpg")
                image_file.close()
            if data_img != '':
                self.label_mp3img.setPixmap(QtGui.QPixmap(data_img)) #change picture here
                os.remove(data_img)
            else:
                self.label_mp3img.setPixmap(QtGui.QPixmap('')) #change picture here
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            self.playBtn.setEnabled(True)
            self.pathfile = self.filename

        elif self.filename == '':
            print("No media selected!")

        else:
            self.setMaximumWidth(10000)
            self.setMaximumHeight(10000)
            self.label_mp3img.setPixmap(QtGui.QPixmap(''))
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            self.playBtn.setEnabled(True)
            self.setGeometry(400, 150, 700, 500)
            self.Stack.setCurrentIndex(1)
            self.pathfile = self.filename
    
    def edit_metadata(self):
        if self.pathfile != '' and self.pathfile.endswith('.mp3'):
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(None)))
            self.playBtn.setEnabled(False)
            self.label_mp3img.setPixmap(QtGui.QPixmap(''))
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog(self.pathfile)
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            print("The video format might be wrong or None")

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()


    def mediastate_changed(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
            )

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
            )

    def position_changed(self, position):
        self.slider.setValue(position)


    def duration_changed(self, duration):
        self.slider.setRange(0, duration)


    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())