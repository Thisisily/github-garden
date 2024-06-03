from PyQt5.QtCore import pyqtSlot
from config import CONFIG
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import json

class AppLogic:
    def __init__(self, main_window):
        self.main_window = main_window

    @pyqtSlot()
    def saveConfig(self):
        if not self.main_window.tokenInput.text() or not self.main_window.repoInput.text():
            QMessageBox.warning(self.main_window, "Input Error", "Please enter both GitHub Token and Repository Name.")
            return
        CONFIG['github_token'] = self.main_window.tokenInput.text()
        CONFIG['repo_name'] = self.main_window.repoInput.text()
        QMessageBox.information(self.main_window, "Success", "Configuration saved successfully.")

    @pyqtSlot()
    def savePattern(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self.main_window, "Save Pattern", "", "JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                json.dump(self.main_window.canvas.grid, file)
            QMessageBox.information(self.main_window, "Success", "Pattern saved successfully.")

    @pyqtSlot()
    def loadPattern(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self.main_window, "Load Pattern", "", "JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.main_window.canvas.grid = json.load(file)
            self.main_window.canvas.update()
            QMessageBox.information(self.main_window, "Success", "Pattern loaded successfully.")

    @pyqtSlot()
    def load_commit_state(self):
        # Placeholder function to load the user's current commit state
        # In a real application, this would involve calling the GitHub API and retrieving commit data
        commit_state = "Mock Commit State: 50 commits"
        self.main_window.commitStateLabel.setText(f"Current Commit State: {commit_state}")
        QMessageBox.information(self.main_window, "Success", "Commit state loaded successfully.")
