from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6 import QtCore

# QtCore.QDir.addSearchPath('assets', '../assets/')
# font_id = QFontDatabase.addApplicationFont("assets:Roboto-Regular.ttf")
# families = QFontDatabase.applicationFontFamilies(font_id)
# main_font = QFont(families[0], 80)

main_font = QFont("Roboto", 20, QFont.Weight.Normal)
main_font.setStyleHint(QFont.StyleHint.Monospace)
# main_font.setWeight(18)
