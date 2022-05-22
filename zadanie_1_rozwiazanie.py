import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QTextEdit

'''
Chcemy stworzyć prostą dwuoknową aplikację GUI.
Część implementacji jest już gotowa. Po uruchomieniu programu otworzy się okno 'Home'.
Zobacz jak ono wygląda, a następnie dokończ aplikację tak by realizowała następujące funckcjonalności:
    - po kliknięciu przycisku open_button powinno otworzyć się nowe okno o tytule 'Okno powitania'.
    - okno powinno zawierać pole tekstowe w którym użytkownik może wprowadzać ciągi znakowe.
    - okno powinno zawierać przycisk po którego kliknięciu na górze okna pojawi się wiadomość 'Cześć [test z pola tekstowego]!'.
    - jeżeli przycisk zostanie kliknięty a pole tekstowe jest puste, w centrum okna ma pojawić się wiadomość 'Podaj swoje imię:'
Powodzenia!
(pamiętaj o odpowiednich importach)
'''

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Home")

        self.open_button = QPushButton(self)
        self.open_button.setText("Otwórz okno powitania!")
        self.open_button.setGeometry(150, 230, 200, 40)

        hello_window = HelloWindow()

        self.open_button.clicked.connect(lambda: hello_window.show())


class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(700, 100, 500, 500)
        self.setWindowTitle("Okno powitania")

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(50, 50, 400, 50)

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(200, 400, 100, 30)
        self.button_2.setText("Kliknij!")

        self.text_edit_2 = QTextEdit(self)
        self.text_edit_2.setGeometry(100, 200, 300, 40)

        self.button_2.clicked.connect(self.update_label_2)

    def update_label_2(self):
        if self.text_edit_2.toPlainText() == '':
            self.label_2.setText("Podaj swoje imię:")
        else:
            self.label_2.setText("Cześć " + self.text_edit_2.toPlainText() + "!")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    home_window = Home()
    home_window.show()

    sys.exit(app.exec_())