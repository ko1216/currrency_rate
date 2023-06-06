from src.funcs import get_currency_rate, save_to_json
from datetime import datetime


def main():
    while True:
        currency = input('Введите название валюты (USD или EUR): ')
        if currency not in ('USD', 'EUR'):
            print('Некорректный код')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f'Курс {currency} к рублю: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Выберите действие: 1 - продолжить, 2 - выйти')
        if choice == '1':
            continue
        elif choice == '2':
            quit()
        else:
            print('Некорректный ввод')


if __name__ == '__main__':
    main()
