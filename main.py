from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Random_forest import RandomForest
from PyQt5.QtWidgets import QMessageBox
from linear_regression_model import SimpleLinearRegression
from ann import ANN
from pages.about import Ui_About
from pages.wall import Ui_Wall
from pages.position import Ui_Position
from pages.width import Ui_width
import math


def print_parameter(position, velocity, angle, depth, width):
    print(f"position = {position}\n"
          f"velocity = {velocity}\n"
          f"angle= {angle}\n"
          f"depth= {depth}\n"
          f"width= {width}")


class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #Button Proceed
        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setGeometry(QtCore.QRect(200, 300, 93, 28))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 591, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("graphic/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 18))
        self.menubar.setObjectName("menubar")

        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")

        self.actionWall = QtWidgets.QAction(MainWindow)
        self.actionWall.setObjectName("actionWall")
        self.menuInfo.addAction(self.actionWall)
        self.menubar.addAction(self.menuInfo.menuAction())

        self.actionPosition = QtWidgets.QAction(MainWindow)
        self.actionPosition.setObjectName("actionPosition")
        self.menuInfo.addAction(self.actionPosition)
        self.menubar.addAction(self.menuInfo.menuAction())

        self.actionWidth = QtWidgets.QAction(MainWindow)
        self.actionWidth.setObjectName("actionWidth")
        self.menuInfo.addAction(self.actionWidth)
        self.menubar.addAction(self.menuInfo.menuAction())

        self.menuSourceCode = QtWidgets.QMenu(self.menubar)
        self.menuSourceCode.setObjectName("menuSourceCode")
        self.menubar.addAction(self.menuSourceCode.menuAction())

        self.menuContact_us = QtWidgets.QMenu(self.menubar)
        self.menuContact_us.setObjectName("menuContact_us")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.menuContact_us.addAction(self.actionContact)
        self.menubar.addAction(self.menuContact_us.menuAction())

        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Drop list to select Meta Model
        self.select_model = QtWidgets.QComboBox(self.centralwidget)
        self.select_model.setGeometry(QtCore.QRect(200, 250, 200, 25))
        self.select_model.setObjectName("select_model")
        self.select_model.addItem("Linear Regression")
        self.select_model.addItem("Random Forest")
        self.select_model.addItem("ANN")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Crashbox Meta Models")
        MainWindow.setWindowIcon(QtGui.QIcon('graphic/icon.png'))

        self.proceed.setText(_translate("MainWindow", "Proceed"))
        self.proceed.clicked.connect(self.take_inputs)

        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionAbout.setText(_translate("MainWindow", "About us"))
        self.actionAbout.triggered.connect(self.openAbout)

        self.menuContact_us.setTitle(_translate("MainWindow", "Contact us"))
        self.actionContact.setText(_translate("MainWindow", "Email"))

        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionWall.setText(_translate("MainWindow", "Velocity and Angle"))
        self.actionPosition.setText(_translate("MainWindow", "Position"))
        self.actionWidth.setText(_translate("MainWindow", "Width"))

        self.actionWall.triggered.connect(self.openWall)
        self.actionPosition.triggered.connect(self.openPosition)
        self.actionWidth.triggered.connect(self.openWidth)

        self.menuSourceCode.setTitle(_translate("MainWindow", "Source Code"))

    def take_inputs(self):
        position, done1 = QtWidgets.QInputDialog.getInt(
            self, 'Input Dialog', 'Enter Position:')
        velocity, done2 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter velocity:')
        angle, done3 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter angle:')
        depth, done4 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter depth:')
        width, done5 = QtWidgets.QInputDialog.getInt(
            self, 'Input Dialog', 'Enter width:')

        if 0 < position <= 39 and 12 <= velocity <= 15 and 0 <= angle <= 3\
                and 0 <= depth <= 4 and width in (1, 2, 3):
            # Showing confirmation message along
            # with information provided by user.
            if self.select_model.currentText() == "Random Forest":
                result = RandomForest.predict(position, velocity, angle, depth,
                                              width)
                result = math.ceil(result)
                print_parameter(position, velocity, angle, depth, width)
                print("random forest")
                print(result)
                self.pop_resultant_force(result, position, velocity, angle, depth, width)
                self.proceed.setText("Predict another set of Parameter")
                self.proceed.adjustSize()
            elif self.select_model.currentText() == "Linear Regression":
                result = SimpleLinearRegression.predict(position,
                                                        velocity,
                                                        angle,
                                                        depth,
                                                        width)
                result = math.ceil(result)
                print("model = linear regression")
                print(result)
                self.pop_resultant_force(result, position, velocity, angle, depth, width)
                self.proceed.setText("Predict another set of Parameter")
                self.proceed.adjustSize()
            elif self.select_model.currentText() == "ANN":
                result = ANN.predict(position,
                                     velocity,
                                     angle,
                                     depth,
                                     width,
                                     )
                result = math.ceil(result)
                print(result)
                self.pop_resultant_force(result, position, velocity, angle, depth, width)
                self.proceed.setText("Predict another set of Parameter")
                self.proceed.adjustSize()
        else:
            self.pop_err_parameter()
            self.proceed.adjustSize()


    def pop_resultant_force(self, result, position, velocity, angle, depth, width):
        msg = QMessageBox()
        msg.setWindowTitle("Result")
        msg.setText(f"Algorithm = {self.select_model.currentText()}\n"
                    f"Position = {position}\n"
                    f"Velocity = {velocity}   [Km/H]\n"
                    f"Angle = {angle}        [degree]\n"
                    f"Depth = {depth}        [mm]\n"
                    f"Width = {width}           [elements]\n\n"
                    f"Resultant Force = {result} [N]")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    @staticmethod
    def pop_err_parameter():
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Parameter Input was not Successful")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort)
        msg.setDetailedText("Position must be between 1 and 39 \n"
                            "Velocity must be between 12 and 15 Km\H \n"
                            "Angle must be between 0 and 3 Degree \n"
                            "Depth must be between 0 and 4 mm \n"
                            "Width can only be 1, 2 or 3")
        x = msg.exec_()

    @staticmethod
    def pop_err_model_selection():
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Please Select the Model before Proceeding...")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort)
        x = msg.exec_()

    def openAbout(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_About()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWall(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Wall()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPosition(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Position()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWidth(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_width()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
