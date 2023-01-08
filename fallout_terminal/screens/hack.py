from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class HackScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.main_layout.setContentsMargins(5, 5, 5, 5)
        # self.main_layout.setSpacing(3)
        self.setLayout(self.main_layout)

        self.first_line = QLabel('Добро пожаловать в сеть "РОБКО Индастриз(ТМ)"')
        self.main_layout.addWidget(self.first_line)
        self.second_line = QLabel('Ядер-Космопорт - кабинет администратора')
        self.main_layout.addWidget(self.second_line)
        self.main_layout.addWidget(QLabel('1' + '0' * 48 + '1'))

        # 50
        # 21
