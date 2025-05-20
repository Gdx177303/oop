Bot do konwersji walut na Discord


Opis:

Bot Discorda umożliwiający przeliczanie walut oraz automatyczne wysyłanie aktualnych kursów USD względem EUR, PLN i UAH.

Komendy:

!przelicz <kwota> <z_waluty> <na_walute>
Opis: Przelicza z jednej waluty na inną.

Przykład: !przelicz 100 USD PLN
Odpowiedź: 100 USD = 400.00 PLN (wraz z aktualnym kursem)

Automatyczna aktualizacja:

Co godzinę bot wysyła wiadomość z aktualnymi kursami walut (USD → EUR, PLN, UAH) na zdefiniowany kanał Discorda.

Konfiguracja:

Wymagane zmienne środowiskowe w .env:
--------------------------------------
env

DISCORD_TOKEN=<TOKEN_BOTA_DISCORD>

EXCHANGE_RATE_API_KEY=<KLUCZ_API_Z_EXCHANGERATE-API>

CHANNEL_ID=<ID_KANAŁU_DISCORDA>

--------------------------------------

Pliki:

main.py – logika bota Discorda i obsługa komend.

currency_api.py – komunikacja z API kursów walut.

config.py – ładowanie danych konfiguracyjnych z .env.
