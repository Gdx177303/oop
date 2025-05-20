import requests
from datetime import datetime

class CurrencyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}"
        self.cache = {}

    def pobierz_kursy(self, waluta_bazowa, waluty_docelowe):
        """Zwraca kursy walut z obsluga cache"""
        try:
            response = requests.get(f"{self.base_url}/latest/{waluta_bazowa}")
            data = response.json()
            
            if data.get('result') != 'success':
                raise Exception(data.get('error-type', 'Błąd API'))
                
            return {waluta: data['conversion_rates'][waluta] for waluta in waluty_docelowe}
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Blad polaczenia: {str(e)}")

    def konwertuj(self, kwota, z_waluty, na_walute):
        """Konwersja waluty z podstawowa obsluga bledow"""
        try:
            response = requests.get(f"{self.base_url}/pair/{z_waluty}/{na_walute}/{kwota}")
            data = response.json()
            
            if data.get('result') != 'success':
                raise Exception(data.get('error-type', 'Blad konwersji'))
                
            return {
                'przeliczona_kwota': data['conversion_result'],
                'kurs': data['conversion_rate']
            }
        except requests.exceptions.RequestException as e:
            raise Exception(f"Blad polaczenia: {str(e)}")