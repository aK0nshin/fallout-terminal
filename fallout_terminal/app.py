from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QCursor, QPixmap, QFont, QBitmap, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QSizePolicy

import sys

from fallout_terminal.palette import palette
from fallout_terminal.screens.hack import HackScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('assets:hack.png'))
        self.setWindowTitle("РОБКО Индастриз(ТМ)")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(HackScreen())

    def resizeEvent(self, event: QtGui.QResizeEvent):
        main_font = QFont("Roboto", round(self.width() / 40), QFont.Weight.Normal)
        main_font.setStyleHint(QFont.StyleHint.Monospace)
        app.setFont(main_font)

        cursor_pixmap = QIcon('assets:fallout_cursor_v2.svg').pixmap(136)
        cursor_pixmap = cursor_pixmap.scaled(round(self.width() / 30), round(self.width() / 30),
                                             QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        app.setOverrideCursor(QCursor(cursor_pixmap, True, True))


QtCore.QDir.addSearchPath('assets', '../assets/')
app = QApplication(sys.argv)
app.setPalette(palette)

window = MainWindow()
# window.showFullScreen()
window.resize(800, 600)
width_size = window.width() / 40

window.show()

app.exec()
