import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt  # Add this line

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calculator')

        # Create display
        self.display = QLineEdit(self)
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
        ]

        grid_layout = QGridLayout()
        for i, button_text in enumerate(buttons):
            button = QPushButton(button_text, self)
            button.clicked.connect(lambda _, text=button_text: self.on_click(text))
            grid_layout.addWidget(button, i // 4, i % 4)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid_layout)

        self.setLayout(layout)

    def on_click(self, value):
        if value == 'C':
            self.display.clear()
        elif value == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
