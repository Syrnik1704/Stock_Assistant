import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

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

# tutaj napisz swój kod


if __name__ == "__main__":

    app = QApplication(sys.argv)

    home_window = Home()
    home_window.show()

    sys.exit(app.exec_())
