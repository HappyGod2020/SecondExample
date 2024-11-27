import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.drawing_area = self.findChild(QtWidgets.QWidget, "drawingArea")

        self.add_circle_button = self.findChild(QtWidgets.QPushButton, "addCircleButton")
        self.add_circle_button.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        x = random.randint(0, self.drawing_area.width() - 50)
        y = random.randint(0, self.drawing_area.height() - 50)
        diameter = random.randint(10, 100)
        self.circles.append((x, y, diameter))
        self.drawing_area.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for x, y, diameter in self.circles:
            painter.setBrush(QColor("yellow"))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, diameter, diameter)

        painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
