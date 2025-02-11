import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PyQt6.uic import loadUi
from immich import Immich


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/mainWindow.ui", self)

        self.immich = Immich()  # Initialize Immich API handler
        self.files = []

        self.addPhotosButton.clicked.connect(self.open_add_photos_dialog)
        self.uploadButton.clicked.connect(self.upload_files)

    def open_add_photos_dialog(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Photos", "", "Images (*.png *.jpg *.jpeg)")
        if files:
            self.files.extend(files)
            for file in files:
                self.fileList.addItem(QListWidgetItem(file))

    def upload_files(self):
        for file_path in self.files:
            success = self.immich.upload_file(file_path)
            if success:
                print(f"✅ Uploaded: {file_path}")
            else:
                print(f"❌ Failed: {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
