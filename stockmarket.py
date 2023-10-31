import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a label for the stock ticker
        self.ticker_label = QLabel("Stock ticker:")

        # Create a text box for the stock ticker
        self.ticker_edit = QLineEdit()

        # Create a button to make a prediction
        self.predict_button = QPushButton("Predict")

        # Create a label for the predicted price
        self.prediction_label = QLabel("Predicted price:")

        # Create a text box for the predicted price
        self.prediction_edit = QLineEdit()

        # Set the layout of the main window
        layout = QVBoxLayout()
        layout.addWidget(self.ticker_label)
        layout.addWidget(self.ticker_edit)
        layout.addWidget(self.predict_button)
        layout.addWidget(self.prediction_label)
        layout.addWidget(self.prediction_edit)

        self.setLayout(layout)

        # Connect the predict button to the predict function
        self.predict_button.clicked.connect(self.predict)

    def predict(self):
        # Get the stock ticker from the text box
        ticker = self.ticker_edit.text()

        # Train a Prophet model on the closing price of the stock
        data = yf.download(ticker, period="1y")["Close"]
        model = Prophet()
        model.fit(data)

        # Make a prediction for the closing price of the stock on the next day
        future_price = model.predict(future_date="2023-10-31")

        # Display the predicted price in the text box
        self.prediction_edit.setText(str(future_price))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
