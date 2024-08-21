import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class HoverExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mouse Hover Change Icon Example')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Create a button
        button = QPushButton('Hover over me', self)

        # Set the cursor to a hand pointer when hovering over the button
        button.setCursor(Qt.PointingHandCursor)

        # Add the button to the layout
        layout.addWidget(button)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HoverExample()
    window.show()
    sys.exit(app.exec_())