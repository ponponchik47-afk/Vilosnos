import requests
import os
from colorama import init, Fore

print(Fore.GREEN + """
                                                                                                                                             


 __  __                      ____      _
|  \/  | ___   ___  _ __    / ___|__ _| |_
| |\/| |/ _ \ / _ \| '_ \  | |   / _` | __|
| |  | | (_) | (_) | | | | | |__| (_| | |_
|_|  |_|\___/ \___/|_| |_|  \____\__,_|\__|
    """)
class HttpWebNumber:
    def __init__(self) -> None:
        self.__check_number_link: str = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.__not_found_text: str = "Информация отсутствует"

    def __return_number_data(self, user_number: str) -> dict:
        try:
            response = requests.get(self.__check_number_link + user_number, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"})
            if response.ok:
                return response.json()
            else:
                return {"status_error": True}
        except requests.exceptions.ConnectionError:
            return {"status_error": True}

    def print_number_results(self) -> None:
        try:
            user_number = input('Введите номер телефона +79833170773: ').strip()
            if user_number:
                print("-Поиск данных..\n")
                number_data = self.__return_number_data(user_number=user_number)

                if number_data.get("limit", 1) <= 0:
                    print(f'-К сожалению, вы израсходовали все лимиты')
                    print(f'-Всего лимитов: {number_data.get("limit", self.__not_found_text)}')

                elif number_data.get("status_error") or number_data.get("error"):
                    print('-Данные не найдены\n')
                else:
                    country = number_data.get('country', {})
                    capital = number_data.get('capital', {})
                    region = number_data.get('region', {"autocod": self.__not_found_text, "name": self.__not_found_text, "okrug": self.__not_found_text})
                    other = number_data.get('0', {})

                    if country.get("country_code3") == 'UKR':
                        print(f'-Страна: Украина')
                    else:
                        print(f'-Страна: {country.get("name", self.__not_found_text)}, {country.get("fullname", self.__not_found_text)}')

                    print(f'-Город: {other.get("name", self.__not_found_text)}')
                    print(f'-Почтовый индекс: {other.get("post", self.__not_found_text)}')
                    print(f'-Код валюты: {country.get("iso", self.__not_found_text)}')
                    print(f'-Телефонные коды: {capital.get("telcod", self.__not_found_text)}')
                    print(f'-Гос. номер региона авто: {region.get("autocod", self.__not_found_text)}')
                    print(f'-Оператор: {other.get("oper", self.__not_found_text)}, {other.get("oper_brand", self.__not_found_text)}, {other.get("def", self.__not_found_text)}')
                    print(f'-Местоположение: {country.get("name", self.__not_found_text)}, {region.get("name", self.__not_found_text)}, {other.get("name", self.__not_found_text)}')
                    print(f'-Локация: {number_data.get("location", self.__not_found_text)}')
                    print(f'-Язык общения: {country.get("lang", self.__not_found_text).title()}, {country.get("langcod", self.__not_found_text)}')
                    print(f'-Край/Округ/Область: {region.get("name", self.__not_found_text)}, {region.get("okrug", self.__not_found_text)}')
                    print(f'-Столица: {capital.get("name", self.__not_found_text)}')
                    print(f'-Широта/Долгота: {other.get("latitude", self.__not_found_text)}, {other.get("longitude", self.__not_found_text)}')

                    print(f'-Проверьте эти ссылки:')
                    print(f'- https://www.instagram.com/accounts/password/reset - Поиск аккаунта в Instagram')
                    print(f'- https://api.whatsapp.com/send?phone={user_number}&text=Привет - Поиск номера в WhatsApp')
                    print(f'-https://facebook.com/login/identify - Поиск аккаунта FaceBook')
                    print(f'- https://www.linkedin.com/checkpoint/rp/request-password-reset - Поиск аккаунта Linkedin')
                    print(f'- https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink - Поиск аккаунта OK')
                    print(f'- https://twitter.com/account/begin_password_reset - Поиск аккаунта Twitter')
                    print(f'-https://viber://add?number={user_number} - Поиск номера в Viber')
                    print(f'-https://skype:{user_number}?call - Звонок на номер с Skype')
                    print(f'-https://t.me/{user_number} - Открыть аккаунт в Телеграмме')
                    print(f'-tel:{user_number} - Звонок на номер с телефона')

                    print(f'-Всего лимитов: {number_data.get("limit", self.__not_found_text)}')

                    input('-Чтобы завершить поиск, нажмите ENTER ')
                    
            else:
                print('-Ошибка, введите номер телефона!\n')

        except KeyboardInterrupt:
            print('\n[!] Вынужденная остановка работы!\n')
            

if __name__ == "__main__":
    checker = HttpWebNumber()
    checker.print_number_results()
