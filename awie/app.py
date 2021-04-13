def main():
    from PyQt5.QtGui import QPalette, QColor, QIcon
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import Qt
    import platform

    if platform.system() == 'Windows':
        import ctypes
        appid = 'iyadahmed.awesome.imageeditor.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    app = QApplication([])
    app.setWindowIcon(QIcon("./icons/app.png"))
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    from awie.mainwindow import MainWindow

    window = MainWindow()
    window.showMaximized()
    return app.exec_()
