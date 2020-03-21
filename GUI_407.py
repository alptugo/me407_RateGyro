import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5 import uic
#imported the necessary libraries

qtDesignerFile = "untitled.ui"  # Enter file here.
#we give the destination of our .ui file
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtDesignerFile)
#we define the window and base class for pyqt5

class MyApp(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, channel):#our class needs a channel object(either a serial.Serial or socket.socket object)
        # to send the data
        qtw.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.channel=channel
        self.degreeButton0.clicked.connect(lambda:self.degreeSlider.setValue(-90))#radio button changes slider
        self.degreeButton1.clicked.connect(lambda:self.degreeSlider.setValue(-45))
        self.degreeSlider.valueChanged.connect(self.degree_sender)#when slider changes, it calls degree_sender method.
        self.releaseButton.clicked.connect(self.stop_func)#when the button is pressed it calls stop_func method
    def degree_sender(self):
        self.degreeLabel.setText(str(self.degreeSlider.value()))#current slider value is shown on the label
        temp=str(self.degreeSlider.value()+90)+"\n"
        self.channel.write(temp.encode("utf-8"))#current slider value is sent to serial as encoded string
        #between 0 and 180
        #print(temp.encode("utf-8"))#this is left for console debugging
    def stop_func(self):
        temp=str(181)+"\n"
        self.channel.write(temp.encode("utf-8"))#181 is sent to serial as encoded string
        #print("181")
class ClientGUI(MyApp):#this function inherites from our previous class, but we change the pyserial
    #.write() method to socket .sendall() method.
    def __init__(self, channel):
        super().__init__(channel)
    def degree_sender(self):
        self.degreeLabel.setText(str(self.degreeSlider.value()))
        temp=str(self.degreeSlider.value()+90)+"\n"
        self.channel.sendall(temp.encode("utf-8"))
        #print(temp)
    def stop_func(self):
        self.channel.sendall("181\n".encode("utf-8"))
        #print(bytes([self.degreeSlider.value()+90]))
