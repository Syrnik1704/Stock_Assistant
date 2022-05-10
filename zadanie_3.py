import yfinance as yf

'''
Chcemy napisać funkcję, która obliczy i zwróci maksymalną i minimalną wartość korelacji między akcjami spółek Big Five. 
Przygotowano szkielet programu. Napisz funkcję find_correlation tak aby realizowała następujące kroki:
    - zaciągnięcie za pomocą modułu yfinance danych giełdowych dla listy tickerów (argument funckcji) od dnia 1 stycznia 2022 roku.
    - obliczenie procentowych zmian ceny zamknięcia dla rozpatrywanego okresu.
    - obliczenie korelacji z wyniku powyższego kroku (warto skorzystać z gotowej funkcji)
    - usunięcie duplikatów (warto najpierw skorzystać z funkcji unstack() aby powiązać indeksy kolumn i wierszy (kolejnych tickerów) ze sobą)
    - usunięcie wiersza z autokorelacją - wartości 1.00 (szukaj go pod max indexem (idxmax()) 
    - stworzenia 2 elementowego słownika gdzie kluczami są pary dla których wartość korelacji jest min i max a wartościami min i max wartości korelacji (skorzystaj z podpowiedzi z poprzedniego korku aby znaleźć właściwe pary)
Po uruchomieniu programu powinien pokazać się wykres, który przedstawia zmiany wartości zaiwestowanego 1$ w okresie 6 miesięcy. 
Powodzenia!
'''

def find_correlation(tickers):
    # tutaj napisz swój kod
    pass


if __name__ == "__main__":

    big_five = ['GOOG', 'AMZN', 'AAPL', 'FB', 'MSFT']
    data = find_correlation(big_five)
    print(data)
