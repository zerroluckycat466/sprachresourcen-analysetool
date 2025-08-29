import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    # Lädt die Daten aus einer CSV-Datei
    return pd.read_csv(file_path)


def analyze_data(data):
    # Führt eine einfache Analyse durch und gibt die Struktur der Daten zurück
    return data.describe()


def visualize_data(data):
    # Erstellt ein einfaches Histogramm der ersten numerischen Spalte
    plt.hist(data.iloc[:, 0], bins=30)
    plt.title('Histogramm der ersten numerischen Spalte')
    plt.xlabel('Werte')
    plt.ylabel('Häufigkeit')
    plt.show()


if __name__ == '__main__':
    file_path = input('Geben Sie den Pfad zur CSV-Datei ein: ')
    data = load_data(file_path)
    print(analyze_data(data))
    visualize_data(data)