import warnings
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFrame, QSizePolicy
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap, QIcon
from PyQt5.QtCore import Qt
from canvas import Canvas

# Suppress specific DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning, message="sipPyTypeDict() is deprecated")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Add margins around the main layout
        layout.setSpacing(20)  # Add spacing between widgets

        # Load pixelated font
        font_id = QFontDatabase.addApplicationFont('assets/press_start_2p.ttf')
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        pixel_font = QFont(font_family, 12)
        small_pixel_font = QFont(font_family, 10)  # Smaller font for weekdays

        # Calculate grid width
        grid_width = 1792  # Based on the calculated grid width from the Canvas class

        # Create a frame for the banner and canvas
        container = QFrame(self)
        container_layout = QVBoxLayout(container)
        container_layout.setAlignment(Qt.AlignCenter)  # Center the container layout
        container_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins from container layout
        container_layout.setSpacing(20)  # Adjust spacing between widgets in the container

        # Add banner
        banner = QLabel(container)
        banner.setAlignment(Qt.AlignCenter)
        banner.setPixmap(QPixmap('assets/banner.png').scaled(grid_width, 400, Qt.KeepAspectRatio))  # Set banner to the correct size
        container_layout.addWidget(banner, alignment=Qt.AlignCenter)

        # Add Canvas
        canvas_container = QFrame(container)
        canvas_container_layout = QVBoxLayout(canvas_container)
        canvas_container_layout.setAlignment(Qt.AlignCenter)
        canvas_container_layout.setContentsMargins(0, 0, 0, 0)
        canvas_container_layout.setSpacing(0)

        self.canvas = Canvas(canvas_container, small_pixel_font)  # Pass smaller font for weekdays
        self.canvas.setMinimumSize(grid_width, 400)  # Adjust the size of the canvas to match the banner width
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas_container_layout.addWidget(self.canvas, alignment=Qt.AlignCenter)
        container_layout.addWidget(canvas_container, alignment=Qt.AlignCenter)

        layout.addWidget(container, alignment=Qt.AlignCenter)

        # GitHub Token and Repository Input
        formLayout = QHBoxLayout()
        formLayout.setSpacing(20)  # Add spacing between input fields

        self.tokenInput = QLineEdit(self)
        self.tokenInput.setPlaceholderText('Enter your GitHub Token')
        self.tokenInput.setStyleSheet('QLineEdit { background-color: #333; color: #fff; padding: 10px; border-radius: 5px; }')
        self.tokenInput.setFont(pixel_font)
        formLayout.addWidget(self.tokenInput)

        self.repoInput = QLineEdit(self)
        self.repoInput.setPlaceholderText('Enter your Repository Name')
        self.repoInput.setStyleSheet('QLineEdit { background-color: #333; color: #fff; padding: 10px; border-radius: 5px; }')
        self.repoInput.setFont(pixel_font)
        formLayout.addWidget(self.repoInput)

        self.submitButton = QPushButton('Submit', self)
        self.submitButton.setStyleSheet('QPushButton { background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; } QPushButton:hover { background-color: #45a049; }')
        self.submitButton.setFont(pixel_font)
        formLayout.addWidget(self.submitButton)

        layout.addLayout(formLayout)

        # Add control buttons
        controlLayout = QHBoxLayout()
        controlLayout.setSpacing(20)  # Add spacing between control buttons

        self.clearButton = QPushButton('Clear Canvas', self)
        self.clearButton.setStyleSheet('QPushButton { background-color: #f44336; color: white; padding: 10px; border-radius: 5px; } QPushButton:hover { background-color: #da190b; }')
        self.clearButton.setFont(pixel_font)
        self.clearButton.clicked.connect(self.canvas.clearCanvas)
        controlLayout.addWidget(self.clearButton)

        self.saveButton = QPushButton('Save Pattern', self)
        self.saveButton.setStyleSheet('QPushButton { background-color: #2196F3; color: white; padding: 10px; border-radius: 5px; } QPushButton:hover { background-color: #0b7dda; }')
        self.saveButton.setFont(pixel_font)
        controlLayout.addWidget(self.saveButton)

        self.loadButton = QPushButton('Load Pattern', self)
        self.loadButton.setStyleSheet('QPushButton { background-color: #FF9800; color: white; padding: 10px; border-radius: 5px; } QPushButton:hover { background-color: #fb8c00; }')
        self.loadButton.setFont(pixel_font)
        controlLayout.addWidget(self.loadButton)

        layout.addLayout(controlLayout)

        self.setLayout(layout)
        self.setWindowTitle('GitHub Commit Painter')
        self.setFixedSize(grid_width + 80, 900)  # Adjusted window size to be larger than the container

        # Apply the pixelated font to the entire application
        self.setFont(pixel_font)
        self.setStyleSheet('QWidget { background-color: #222; color: white; }')

        # Set the window icon
        self.setWindowIcon(QIcon('assets/icon.png'))  # Ensure you have an 'icon.png' in the 'assets' folder

        self.show()
