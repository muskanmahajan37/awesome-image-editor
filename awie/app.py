def main():
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    from awie.mainwindow import MainWindow

    window = MainWindow()
    window.showMaximized()
    return app.exec_()
    
