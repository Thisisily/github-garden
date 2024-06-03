from PyQt5.QtWidgets import QGridLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

def create_form_layout(main_window):
    formLayout = QGridLayout()

    main_window.tokenInput = QLineEdit(main_window)
    main_window.tokenInput.setPlaceholderText('Enter your GitHub Token')
    main_window.tokenInput.setStyleSheet("padding: 10px; font-size: 14px; background-color: #333; color: #fff; border: 1px solid #555;")
    formLayout.addWidget(QLabel("GitHub Token:", main_window), 0, 0)
    formLayout.addWidget(main_window.tokenInput, 0, 1)

    main_window.repoInput = QLineEdit(main_window)
    main_window.repoInput.setPlaceholderText('Enter your Repository Name')
    main_window.repoInput.setStyleSheet("padding: 10px; font-size: 14px; background-color: #333; color: #fff; border: 1px solid #555;")
    formLayout.addWidget(QLabel("Repository Name:", main_window), 1, 0)
    formLayout.addWidget(main_window.repoInput, 1, 1)

    submitButton = QPushButton('Submit', main_window)
    submitButton.clicked.connect(main_window.saveConfig)
    submitButton.setStyleSheet("""
        QPushButton {
            padding: 10px; 
            font-size: 14px; 
            background-color: #4CAF50; 
            color: white; 
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #3e8e41;
            transform: scale(0.98);
        }
    """)
    formLayout.addWidget(submitButton, 2, 1, alignment=Qt.AlignRight)
    return formLayout

def create_commit_state_layout(main_window):
    commitStateLayout = QVBoxLayout()

    main_window.commitStateLabel = QLabel("Current Commit State: Not Loaded", main_window)
    main_window.commitStateLabel.setStyleSheet("padding: 10px; font-size: 14px; background-color: #333; color: #fff; border: 1px solid #555;")
    commitStateLayout.addWidget(main_window.commitStateLabel)

    loadCommitStateButton = QPushButton('Load Commit State', main_window)
    loadCommitStateButton.clicked.connect(main_window.load_commit_state)  # Connect to the method directly
    loadCommitStateButton.setStyleSheet("""
        QPushButton {
            padding: 10px; 
            font-size: 14px; 
            background-color: #2196F3; 
            color: white; 
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #1E88E5;
        }
        QPushButton:pressed {
            background-color: #1976D2;
            transform: scale(0.98);
        }
    """)
    commitStateLayout.addWidget(loadCommitStateButton)

    return commitStateLayout

def create_button_layout(main_window):
    buttonLayout = QHBoxLayout()

    clearButton = QPushButton('Clear Canvas', main_window)
    clearButton.clicked.connect(main_window.canvas.clearCanvas)
    clearButton.setStyleSheet("""
        QPushButton {
            padding: 10px; 
            font-size: 14px; 
            background-color: #f44336; 
            color: white; 
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #e53935;
        }
        QPushButton:pressed {
            background-color: #d32f2f;
            transform: scale(0.98);
        }
    """)
    buttonLayout.addWidget(clearButton)

    saveButton = QPushButton('Save Pattern', main_window)
    saveButton.clicked.connect(main_window.savePattern)
    saveButton.setStyleSheet("""
        QPushButton {
            padding: 10px; 
            font-size: 14px; 
            background-color: #2196F3; 
            color: white; 
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #1E88E5;
        }
        QPushButton:pressed {
            background-color: #1976D2;
            transform: scale(0.98);
        }
    """)
    buttonLayout.addWidget(saveButton)

    loadButton = QPushButton('Load Pattern', main_window)
    loadButton.clicked.connect(main_window.loadPattern)
    loadButton.setStyleSheet("""
        QPushButton {
            padding: 10px; 
            font-size: 14px; 
            background-color: #FFC107; 
            color: white; 
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #FFB300;
        }
        QPushButton:pressed {
            background-color: #FFA000;
            transform: scale(0.98);
        }
    """)
    buttonLayout.addWidget(loadButton)

    return buttonLayout
