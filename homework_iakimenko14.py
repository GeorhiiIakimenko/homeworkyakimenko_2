import requests


class CurrencyConverter:
    API_URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

    def __init__(self):
        self.currency_data = None

    def fetch_currency_data(self, my_date=None):
        url = self.API_URL
        if my_date:
            url += f'&date={my_date}'

        response = requests.get(url)
        self.currency_data = response.json()

    def write_to_file(self, file_name):
        if not self.currency_data:
            print('Помилка: Дані про курс валют відсутні.')
            return

        with open(file_name, 'w') as file:
            file.write(f'[{self.currency_data[0]["exchangedate"]}]\n')
            for index, currency in enumerate(self.currency_data, start=1):
                file.write(f'{index}. {currency["cc"]} to UAH: {currency["rate"]}\n')


converter = CurrencyConverter()
requested_date = input("Введіть дату (у форматі YYYYMMDD): ")
converter.fetch_currency_data(requested_date)

filename = 'currency.txt'
converter.write_to_file(filename)

print(f'Курс валют було записано у файл "{filename}".')
