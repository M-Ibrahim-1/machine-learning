from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Random_forest import RandomForest
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setGeometry(QtCore.QRect(160, 150, 93, 28))

        # For displaying confirmation message along with user's info.
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(170, 40, 201, 111))
        # Keeping the text of label empty initially.
        self.result_label.setText("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.select_model = QtWidgets.QComboBox(self.centralwidget)
        self.select_model.setGeometry(QtCore.QRect(80, 30, 251, 71))
        self.select_model.setObjectName("select_model")
        self.select_model.addItem("Linear Regression")
        self.select_model.addItem("Polynomial Regression")
        self.select_model.addItem("Random Forest")




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.proceed.setText(_translate("MainWindow", "Proceed"))
        self.proceed.clicked.connect(self.take_inputs)


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
                print(result)
                self.pop_resultant_force(result)
                self.proceed.setText("Predict another set of Parameter")
                self.proceed.adjustSize()
            if self.select_model.currentText() == "Linear Regression":
                pass


        else:
            self.pop_err_parameter()
            self.proceed.adjustSize()

    def pop_resultant_force(self, result):
        msg = QMessageBox()
        msg.setWindowTitle("Result")
        msg.setText(f'resultant force = {result}')
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
