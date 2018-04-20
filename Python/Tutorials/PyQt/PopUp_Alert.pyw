import sys, time
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5 import QtWidgets, QtGui

def app_structure():
    label_window.setGeometry(220,60,1000,600)
    font = QtGui.QFont()
    font.setPointSize(48)
    font.setBold(True)
    message = "GET UP!!\n"*5 + " It is time to take a break!\n Go walk a little bit!"
    alert_label = QtWidgets.QLabel(label_window)
    alert_label.setText(message)
    alert_label.setFont(font)

# initialize the PyQt application and window
app = QtWidgets.QApplication(sys.argv)
label_window = QtWidgets.QWidget()

# initialize the current time and the time list to activate the widget
time_now = tuple((QTime.currentTime().hour(), QTime.currentTime().minute()))
time_list = [tuple((hour, 2)) for hour in range(8, 17)]

# if the current time is not in the time_list the program waits
while (time_now not in time_list):
    # time.sleep(10)
    # print('debugger')
    time.sleep(10)
else:
    print('right timming!')
    # time.sleep(10)
    app_structure()
    label_window.show()
    time.sleep(5)
    label_window.hide()
    app.exec_()
# runs the program indefinetly
# app.exec_()


# alert_label.setWordWrap(True)
# alert_label.setText(("<font color=blue size=72><b>" + message + "<\b><\font>"))

# label_window.show()
# label_window.show()
# time.sleep(2)
# label_window.hide()
# time.sleep(2)
# label_window.show()
# if correct time arguments were given the variable due is updated with the given time
# otherwise, it takes the current time.
# defines the alert message and the message in case of any error
# try:
#     due = QTime.currentTime()
#     message = "Get Up!!"
#     if len(sys.argv) < 2:
#         raise ValueError
#     hours, mins = sys.argv[1].split(":")
#     due = QTime(int(hours), int(mins))
#     if not due.isValid():
#         raise ValueError
#     if len(sys.argv) > 2:
#         message = " ".join(sys.argv[2:])
# except ValueError:
#     message = "Usage: PopUp_Alert.pyw HH:MM"

# hours, mins = (11,29)
# due = QTime(int(hours), int(mins))
# message = "Get UP!"
# # executes the while loop to wait for the correct time
# while QTime.currentTime() not in due:
#     # sleeps for 20 seconds
#     time.sleep(5)
# else:
#     # defines the GUI widgets
#     # QLabel can accept HTML text, so we use it to define the font color and size
#     msg_label = QLabel("<font color=blue size=72><b>" + message + "<\b><\font>")
#     msg_label.setWindowFlags(Qt.SplashScreen)
#     msg_label.show()
#     # set up to show the app for only 60000 mili seconds
#     QTimer.singleShot(30000, app.quit)
#     app.exec_()

# defines the GUI widgets
# QLabel can accept HTML text, so we use it to define the font color and size
# message = "GET UP!! \n"*10
# msg_label = QLabel("<font color=red size=72><b>" + message + "<\b><\font>")
# msg_label.setWindowFlags(Qt.SplashScreen)
#
# time_now = tuple((QTime.currentTime().hour(), QTime.currentTime().minute()))
# time_list = [tuple((hour, 2)) for hour in range(8, 17)]
# msg_label.show()
#
# while (time_now not in time_list):
#     msg_label.hide()
#     time.sleep(10)
#     QTimer.singleShot(10000, app.quit)
# else:
#     msg_label.show()
#     time.sleep(10)
#
# app.exec_()
# for time_value in time_list:
#     print(time_value.hour())
# print(QTime(12, 11))
