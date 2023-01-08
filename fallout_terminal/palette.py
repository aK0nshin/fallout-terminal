from PyQt6.QtGui import QPalette, QColor

palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor('black'))
palette.setColor(QPalette.ColorRole.WindowText, QColor('green'))
palette.setColor(QPalette.ColorRole.Base, QColor('black'))
palette.setColor(QPalette.ColorRole.AlternateBase, QColor('black'))
palette.setColor(QPalette.ColorRole.ToolTipBase, QColor('black'))
palette.setColor(QPalette.ColorRole.ToolTipText, QColor('green'))
palette.setColor(QPalette.ColorRole.Text, QColor('green'))
palette.setColor(QPalette.ColorRole.Button, QColor('black'))
palette.setColor(QPalette.ColorRole.ButtonText, QColor('green'))
palette.setColor(QPalette.ColorRole.BrightText, QColor('green'))
palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.ColorRole.HighlightedText, QColor('green'))