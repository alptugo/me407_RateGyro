import threading as th
import serial.tools.list_ports as lp
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import GUI
import serial
import sys
#imported the necessary libraries



there_is_instance=0
continuing=1
text=""
class my_signal(qtc.QObject):
    updated=qtc.pyqtSignal(int)

    def init(self, useEmit):
        super(my_signal, self).__init__()
        self.some_string=some_string
        self.useEmit=useEmit

class Foo(qtc.QObject):#we define a signal to send to air main thread, as PyQt5 doesn't let us (with a stable way)
    #to directly call another a widgets method from another thread. So we emit a signal on our other thread to activate
    #the method on the main thread.

    # Define a new signal called 'trigger' that has no arguments.
    trigger = qtc.pyqtSignal()

    def connect_and_emit_trigger(self, some_string):
        # Connect the trigger signal to a slot.
        self.trigger.connect(instance.pseudo_lambda)

        # Emit the signal.
        self.trigger.emit()

    def handle_trigger(self):
        # Show that the slot has been called.

        print("trigger signal received")
def input_():#This function constantly reads inputs from serial
    global serial_line
    global first
    global second
    global third
    serial_line = serial.Serial(port)  # initializes serial.Serial object
    while continuing==1:#this is set so the function will loop in its thread(will declared bellow), and when the
        #GUI is closed, this thread would end too, with the change of continuing.
        #ser=input("act like a serial\n")#this is commented out to try the code on console for debugging
        #ser = serial_line.readline(10).decode("utf-8")
        sock=sock_line.read(3)#we read 3 bytes from serial
        first=bin(ser[0])#we get the first byte
        second=bin(ser[1])
        third=bin(ser[2])
        ser=bin(int.from_bytes(ser,"big"))
        #print("i am ser", ser)#kept for debugging over console
        print("i am int ser", ser)
        if there_is_instance:#this checks if the instance is initialized
            some_signal=Foo()
            instance.first=first#we set the first attribute of our instance to first (binary str converted from first byte)
            instance.second=second
            instance.third=third
            some_signal.connect_and_emit_trigger("spanish inquisition")#we emit our signal to the main thread that
            #does indeed expects it


thread_input=th.Thread(target=input_)#we define a thread to constantly read the serial, running parallel to our GUI.

thread_input.start()
app = qtw.QApplication(sys.argv)
instance=GUI.MyApp(serial_line)#we initialize our GUI
there_is_instance=1#we state that we initalized our GUI, enabling the start of the if in the while loop on the thread.
#without useing this, instance methods on thread could run before we initialized the instance, giving instance not found error.
instance.show()#the code stays on this line while the GUI is open
there_is_instance = 1
sys.exit(app.exec_())
continuing=0#when we close the GUI, we set this variable to 0, in order to finalize the waiting thread
# (the thread may need one last input to properly close)