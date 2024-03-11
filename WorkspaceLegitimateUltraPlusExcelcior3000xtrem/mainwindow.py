import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

class UiLoader(QUiLoader):
    def __init__(self, parent=None):
        super(UiLoader, self).__init__(parent)

    def load_ui(self, ui_file_path):
        ui_file = QFile(ui_file_path)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open {ui_file_path}: {ui_file.errorString()}")
            sys.exit(-1)
        window = self.load(ui_file)
        ui_file.close()
        if not window:
            print(f"Error loading UI file.")
            sys.exit(-1)
        return window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loader = UiLoader()
    window = loader.load_ui("form.ui")
    window.show()
    sys.exit(app.exec())
