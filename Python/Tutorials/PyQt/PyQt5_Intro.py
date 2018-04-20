import sys, os
from PyQt5 import QtWidgets, QtGui

os.chdir(r'C:\Users\40000438\OneDrive - UNITEC SEMICONDUTORES SA\Felipe Oliveira\Estudos\Code\PyQt - Tutorial')
# function to create the application main window
def main_window():
    # aplication object that will run the event loops
    app = QtWidgets.QApplication(sys.argv)

    # create a top level window widget
    top_window = QtWidgets.QWidget()

    # give it an apropriate title
    top_window.setWindowTitle('PyQt5 Introduction tutorial')

    # set the dimensions of the window
    top_window.setGeometry(100, 100, 300, 300)

    # creates a label to be displayed in the top level window
    label_A = QtWidgets.QLabel(top_window)

    # sets the text for the label
    label_A.setText('Hello World!')

    # moves the label to a more appropriate place in the window
    label_A.move(100, 60)

    # creates a new label to display an image instead of a text
    label_B = QtWidgets.QLabel(top_window)
    label_B.setPixmap(QtGui.QPixmap('logo.png'))
    label_B.move(60, 80)

    # display the widged
    top_window.show()

    # runs a loop to continually display the widget
    sys.exit(app.exec_())

main_window()
