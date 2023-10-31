import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a web view
        self.browser = QWebEngineView()

        # Set the central widget to the web view
        self.setCentralWidget(self.browser)

        # Create a toolbar
        self.toolbar = QToolBar()

        # Add a back button to the toolbar
        self.back_button = QPushButton("Back")
        self.toolbar.addWidget(self.back_button)

        # Add a forward button to the toolbar
        self.forward_button = QPushButton("Forward")
        self.toolbar.addWidget(self.forward_button)

        # Add a line edit to the toolbar for entering URLs
        self.url_edit = QLineEdit()
        self.toolbar.addWidget(self.url_edit)

        # Add the toolbar to the main window
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        # Connect the back and forward buttons to their respective functions
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)

        # Connect the line edit to the browser's URL changed signal
        self.url_edit.textChanged.connect(self.browser.setUrl)

        # Show the main window
        self.show()

    def navigate_to_url(self, url):
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_edit.setText(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
