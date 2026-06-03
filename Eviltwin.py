import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from datetime import datetime
import pytz
import urllib.parse
import re
import os
import json
import sys
import platform
import ipaddress
from telethon import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline
from telethon import errors
import webbrowser

webbrowser.open("https://t.me/Arasakaak")

BOLD = "\033[1m"
GREEN = "\033[32m"
RESET = "\033[0m"

USERSBOX_API_KEY = os.getenv("USERSBOX_API_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoxNzI1MTk2NzMwLCJhcHBfaWQiOjE3MjUxOTY3MzB9.qG_GQCdZqvUHSHd0yGpnPiUGKo-KRsgNnMo8ZDpRItg")
USERSBOX_API_HEADERS = {
    "Authorization": f"Bearer {USERSBOX_API_KEY}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}
HUDSONROCK_API_KEY = os.getenv("HUDSONROCK_API_KEY", "")
HUDSONROCK_API_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
if HUDSONROCK_API_KEY:
    HUDSONROCK_API_HEADERS["Authorization"] = f"Bearer {HUDSONROCK_API_KEY}"
LEAKCHECK_API_KEY = "49535f49545f5245414c4c595f4150495f4b4559"
LEAKCHECK_API_URL = "https://leakcheck.net/api/public"
OK_LOGIN_URL = 'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong'
OK_RECOVER_URL = 'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword'
TELEGRAM_API_ID = 21826549
TELEGRAM_API_HASH = 'c1a19f792cfd9e397200d16c7e448160'
TELEGRAM_SESSION = 'watcher.session'


BANNER = f"""
{BOLD}                                               
███████╗██╗   ██╗██╗██╗   ████████╗██╗    ██╗██╗███╗   ██╗
██╔════╝██║   ██║██║██║   ╚══██╔══╝██║    ██║██║████╗  ██║
█████╗  ██║   ██║██║██║█████╗██║   ██║ █╗ ██║██║██╔██╗ ██║
██╔══╝  ╚██╗ ██╔╝██║██║╚════╝██║   ██║███╗██║██║██║╚██╗██║
███████╗ ╚████╔╝ ██║███████╗ ██║   ╚███╔███╔╝██║██║ ╚████║
╚══════╝  ╚═══╝  ╚═╝╚══════╝ ╚═╝    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
by: @FigureNori                                                          
version: beta 
{RESET}
"""


class HttpWebNumber:
    def __init__(self):
        self.__check_number_link = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.__not_found_text = "Information not available"

    def __return_number_data(self, user_number):
        try:
            response = requests.get(self.__check_number_link + user_number, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"})
            if response.ok:
                return response.json()
            else:
                return {"status_error": True}
        except requests.exceptions.ConnectionError:
            return {"status_error": True}

    def get_number_data(self, user_number):
        if not user_number:
            return {"error": "Phone number not provided"}
        number_data = self.__return_number_data(user_number)
        if number_data.get("limit", 1) <= 0:
            return {"error": "All search limits have been exhausted", "limit": number_data.get("limit", self.__not_found_text)}
        elif number_data.get("status_error") or number_data.get("error"):
            return {"error": "Data not found"}
        else:
            return number_data


def get_phone_number_info(phone_number_str: str, lang: str = 'ru') -> dict:
    try:
        parsed_number = phonenumbers.parse(phone_number_str, None)
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{BOLD}Ошибка: Номер '{phone_number_str}' не является действительным.{RESET}")
            return None
        if not phonenumbers.is_possible_number(parsed_number):
            print(f"{BOLD}Ошибка: Номер '{phone_number_str}' не является возможным номером телефона.{RESET}")
            return None

        country_code = parsed_number.country_code
        national_number = parsed_number.national_number
        number_type = phonenumbers.number_type(parsed_number)
        geo_location = geocoder.description_for_number(parsed_number, lang)
        operator_name = carrier.name_for_number(parsed_number, lang)
        time_zones = timezone.time_zones_for_number(parsed_number)

        number_type_map = {
            phonenumbers.PhoneNumberType.MOBILE: "Мобильный",
            phonenumbers.PhoneNumberType.FIXED_LINE: "Стационарный",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Стационарный или мобильный",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Бесплатный",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Премиум",
            phonenumbers.PhoneNumberType.SHARED_COST: "С разделённой оплатой",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.UNKNOWN: "Неизвестный"
        }
        number_type_str = number_type_map.get(number_type, "Неизвестный")

        current_time = "Неизвестно"
        utc_offset = "UTC Неизвестно"
        if time_zones:
            tz_name = time_zones[0]
            try:
                tz = pytz.timezone(tz_name)
                now = datetime.now(tz)
                current_time = now.strftime('%Y-%m-%d %H:%M:%S')
                offset = tz.utcoffset(now)
                if offset is not None:
                    offset_seconds = offset.total_seconds()
                    hours_offset = int(offset_seconds // 3600)
                    minutes_offset = int((offset_seconds % 3600) // 60)
                    sign = '+' if offset_seconds >= 0 else '-'
                    utc_offset = f"UTC{sign}{abs(hours_offset):02}:{abs(minutes_offset):02}"
            except Exception:
                current_time = "Невозможно определить точное время"

        suspicious_prefixes = ["900", "901", "902"]
        phone_prefix = phone_number_str[1:4] if phone_number_str.startswith('+') else phone_number_str[:3]
        suspicious = phone_prefix in suspicious_prefixes

        return {
            "full_number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "country_code": country_code,
            "national_number": national_number,
            "is_valid": True,
            "number_type": number_type_str,
            "geo_location": geo_location if geo_location else "Неизвестно",
            "operator": operator_name if operator_name else "Неизвестен",
            "time_zones": list(time_zones) if time_zones else ["Неизвестно"],
            "current_time": current_time,
            "utc_offset": utc_offset,
            "suspicious": suspicious
        }
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"{BOLD}Ошибка парсинга номера '{phone_number_str}': {e}{RESET}")
        return None
    except Exception as e:
        print(f"{BOLD}Произошла неизвестная ошибка: {e}{RESET}")
        return None


async def check_usersbox(query):
    try:
        url = "https://api.usersbox.ru/v1/explain"
        headers = {'Authorization': f'Bearer {USERSBOX_API_KEY}'}
        params = {'q': query}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params, timeout=10) as response:
                if response.status == 429:
                    return {"error": "Превышен лимит запросов к UsersBox. Попробуйте позже."}
                data = await response.json()
                items = data.get('data', {}).get('items', [])
                if items:
                    result = {
                        "status": "found",
                        "data": []
                    }
                    databases = set()
                    collections = set()
                    for item in items:
                        db = item.get('source', {}).get('database', 'Unknown')
                        collection = item.get('source', {}).get('collection', 'Unknown')
                        count = item.get('hits', {}).get('count', 0)
                        databases.add(db)
                        collections.add(collection)
                        record = {
                            "database": db,
                            "collection": collection,
                            "count": count
                        }
                        for key, value in item.items():
                            if key not in ('source', 'hits'):
                                if isinstance(value, dict):
                                    for sub_key, sub_value in value.items():
                                        record[f"{key}_{sub_key}"] = sub_value
                                else:
                                    record[key] = value
                        result["data"].append(record)
                    result["databases"] = list(databases)
                    result["collections"] = list(collections)
                    return result
                return {
                    "status": "not found",
                    "note": f"Запрос {query} не найден в базах данных UsersBox."
                }
    except Exception as e:
        dork_query = f'from:{query} site:usersbox.ru' if '@' in query else f'"{query}" site:usersbox.ru'
        encoded_query = urllib.parse.quote_plus(dork_query)
        return {
            "error": f"Ошибка проверки UsersBox: {e}. Проверьте URL API или ключ.",
            "link": f"https://www.google.com/search?q={encoded_query}"
        }

async def check_hudsonrock(email):
    try:
        url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email?email={email}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=HUDSONROCK_API_HEADERS, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    if data and isinstance(data, dict):
                        return {
                            "status": "found",
                            "data": data
                        }
                    return {
                        "status": "not found",
                        "note": f"Email {email} не найден в утечках Hudson Rock."
                    }
                else:
                    return {
                        "error": f"Ошибка Hudson Rock: HTTP {response.status}",
                        "note": "Проверьте API-ключ (если требуется) или статус сервиса."
                    }
    except Exception as e:
        return {
            "error": f"Ошибка проверки Hudson Rock: {e}",
            "note": "Проверьте подключение или API-ключ (если требуется)."
        }

async def check_email_breaches(email):
    try:
        params = {"key": LEAKCHECK_API_KEY, "check": email}
        async with aiohttp.ClientSession() as session:
            async with session.get(LEAKCHECK_API_URL, params=params, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success", False):
                        if data.get("found", 0) > 0:
                            return {
                                "status": "found",
                                "data": data.get("result", []),
                                "note": f"Email {email} найден в {data.get('found')} утечках."
                            }
                        else:
                            return {
                                "status": "not found",
                                "note": f"Email {email} не найден в базах утечек LeakCheck."
                            }
                    else:
                        return {
                            "error": "Ошибка API LeakCheck",
                            "note": data.get("error", "Неизвестная ошибка")
                        }
                else:
                    return {
                        "error": f"Ошибка HTTP {response.status}",
                        "note": "Не удалось выполнить запрос к LeakCheck API."
                    }
    except Exception as e:
        return {
            "error": f"Ошибка проверки LeakCheck: {e}",
            "note": f"Проверьте вручную на Have I Been Pwned: https://haveibeenpwned.com/account/{email}"
        }

async def check_ip_breaches(ip):
    try:
        params = {"key": LEAKCHECK_API_KEY, "check": ip}
        async with aiohttp.ClientSession() as session:
            async with session.get(LEAKCHECK_API_URL, params=params, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success", False):
                        if data.get("found", 0) > 0:
                            return {
                                "status": "found",
                                "data": data.get("result", []),
                                "note": f"IP {ip} найден в {data.get('found')} утечках."
                            }
                        else:
                            return {
                                "status": "not found",
                                "note": f"IP {ip} не найден в базах утечек LeakCheck."
                            }
                    else:
                        return {
                            "error": "Ошибка API LeakCheck",
                            "note": data.get("error", "Неизвестная ошибка")
                        }
                else:
                    return {
                        "error": f"Ошибка HTTP {response.status}",
                        "note": "Не удалось выполнить запрос к LeakCheck API."
                    }
    except Exception as e:
        return {
            "error": f"Ошибка проверки LeakCheck: {e}",
            "note": "Проверьте подключение или API-ключ."
        }

async def check_ip_info(ip):
    try:
        url = f"https://ipapi.co/{ip}/json/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    return {
                        "status": "found",
                        "country": data.get("country_name", "Unknown"),
                        "city": data.get("city", "Unknown"),
                        "region": data.get("region", "Unknown"),
                        "isp": data.get("org", "Unknown"),
                        "latitude": data.get("latitude", "Unknown"),
                        "longitude": data.get("longitude", "Unknown"),
                        "timezone": data.get("timezone", "Unknown"),
                        "vpn_or_proxy": data.get("org", "").lower().find("vpn") != -1 or data.get("org", "").lower().find("proxy") != -1,
                        "tor": False,
                        "hosting": data.get("org", "").lower().find("host") != -1 or data.get("org", "").lower().find("cloud") != -1
                    }
                else:
                    return {
                        "status": "error",
                        "error": f"Ошибка запроса к ipapi.co: HTTP {response.status}"
                    }
    except Exception as e:
        return {
            "status": "error",
            "error": f"Ошибка проверки ipapi.co: {e}"
        }

async def intelx_search(phone):
    try:
        clean_phone = re.sub(r'[^0-9]', '', phone)
        if len(clean_phone) < 8:
            return {"status": "error", "note": "Номер слишком короткий для поиска"}
        
        path = f"{clean_phone[:2]}/{clean_phone[2:4]}/{clean_phone[4:6]}/{clean_phone[6:8]}.csv"
        url = f"https://data.intelx.io/saverudata/db2/dbpn/{path}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                content = (await response.text()).split("\n")
                if len(content) > 1:
                    result = {
                        "status": "found",
                        "data": []
                    }
                    headers = [h.strip().strip('"') for h in content[0].split(",")]
                    for line in content[1:]:
                        values = [v.strip().strip('"') for v in line.split(",")]
                        if any(clean_phone in v.lower() for v in values):
                            record = {}
                            for i, value in enumerate(values):
                                if value:
                                    record[headers[i]] = value
                            result["data"].append(record)
                    return result
                return {"status": "not found", "note": "Ничего не найдено"}
        return {"status": "error", "note": "Ошибка запроса"}
    except Exception as e:
        return {"status": "error", "note": f"Ошибка Intelx: {e}"}

async def defolt(number):
    try:
        async with aiohttp.ClientSession() as fin:
            async with fin.get(f"https://smsc.ru/sys/info.php?get_operator=1&login=kirahacker333&psw=Zangar5050!&phone={number}") as resp:
                resp = await resp.text()
                data = resp.split(', ')
                mcc = data[4].replace("mcc = ", "")
                mnc = data[5].replace("mnc = ", "")
                country = data[1].replace("country = ", "")
                operator = data[2].replace("operator = ", "")
                region = data[3].replace("region = ", "")
                
                if not region:
                    region = "неопределен"
                
                return {
                    "status": "found",
                    "country": country,
                    "region": region,
                    "operator": operator,
                    "mcc": mcc,
                    "mnc": mnc
                }
    except Exception as e:
        return {"status": "error", "error": f"Ошибка HLR: {e}"}

async def check_avito(phone):
    try:
        url = f'https://www.avito.ru/rossiya/telefony?q={phone}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}) as response:
                if response.status == 200:
                    text = await response.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    items = soup.find_all('div', {'data-marker': 'item'})
                    if items:
                        return {
                            "status": "found",
                            "note": "Аккаунт или объявления найдены на Avito",
                            "link": url
                        }
                    return {
                        "status": "not found",
                        "note": "Аккаунт или объявления не найдены на Avito",
                        "link": url
                    }
                return {
                    "status": "error",
                    "error": f"Ошибка запроса к Avito: HTTP {response.status}"
                }
    except Exception as e:
        return {
            "status": "error",
            "error": f"Ошибка проверки Avito: {e}",
            "note": "Проверьте подключение или доступность сервиса Avito",
            "link": url
        }

def check_okru_account(login_data):
    try:
        session = requests.Session()
        session.get(f'{OK_LOGIN_URL}&st.email={login_data}')
        request = session.get(OK_RECOVER_URL)
        root_soup = BeautifulSoup(request.content, 'html.parser')
        soup = root_soup.find('div', {'data-l': 'registrationContainer,offer_contact_rest'})
        
        if soup:
            account_info = soup.find('div', {'class': 'ext-registration_tx taCenter'})
            masked_email = soup.find('button', {'data-l': 't,email'})
            masked_phone = soup.find('button', {'data-l': 't,phone'})
            if masked_phone:
                masked_phone = masked_phone.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
            if masked_email:
                masked_email = masked_email.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
            if account_info:
                masked_name = account_info.find('div', {'class': 'ext-registration_username_header'})
                if masked_name:
                    masked_name = masked_name.get_text()
                account_info = account_info.findAll('div', {'class': 'lstp-t'})
                if account_info:
                    profile_info = account_info[0].get_text()
                    profile_registred = account_info[1].get_text()
                else:
                    profile_info = None
                    profile_registred = None
            else:
                return None

            return {
                'status': 'found',
                'masked_name': masked_name,
                'masked_email': masked_email,
                'masked_phone': masked_phone,
                'profile_info': profile_info,
                'profile_registred': profile_registred,
            }

        if root_soup.find('div', {'data-l': 'registrationContainer,home_rest'}):
            return {"status": "not associated"}
        return {"status": "error", "note": "Не удалось проверить OK.ru"}
    except requests.RequestException as e:
        return {"status": "error", "error": f"Ошибка проверки OK.ru: {e}"}

def check_vk_account(email):
    try:
        url = "https://vk.com/restore"
        data = {"email": email}
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.post(url, data=data, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup.find('div', {'class': 'restore_error'}):
            return {"status": "not associated"}
        return {"status": "possibly associated", "note": "VK может быть связан с этим email, проверьте вручную."}
    except requests.RequestException as e:
        return {"status": "error", "error": f"Ошибка проверки VK: {e}"}

def check_twitch_account(email):
    try:
        url = "https://www.twitch.tv/forgot-password"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        data = {"email": email}
        response = requests.post(url, data=data, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        error = soup.find('div', {'class': 'error'})
        if error and "not found" in error.text.lower():
            return {"status": "not associated"}
        return {"status": "possibly associated", "note": "Twitch может быть связан с этим email, проверьте вручную."}
    except requests.RequestException as e:
        return {"status": "error", "error": f"Ошибка проверки Twitch: {e}"}

def check_pinterest_account(email):
    try:
        url = "https://www.pinterest.com/password/reset/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        data = {"email": email}
        response = requests.post(url, data=data, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        error = soup.find('div', {'class': 'error'})
        if error and "not associated" in error.text.lower():
            return {"status": "not associated"}
        return {"status": "possibly associated", "note": "Pinterest может быть связан с этим email, проверьте вручную."}
    except requests.RequestException as e:
        return {"status": "error", "error": f"Ошибка проверки Pinterest: {e}"}

# Telegram tracking function
async def telegram_track(username):
    results = [f"{BOLD}OSINT-поиск в Telegram по имени пользователя: @{username}\n{RESET}"]
    if not os.path.isfile(TELEGRAM_SESSION):
        results.append(f"{BOLD}Ошибка:{RESET} {GREEN}Файл сессии Telegram ({TELEGRAM_SESSION}) не найден! Пожалуйста, создайте сессию сначала.{RESET}")
        print("\n".join(results))
        save_results(f"telegram_{username}", "\n".join(results))
        return

    client = TelegramClient(TELEGRAM_SESSION, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    try:
        await client.start()
    except Exception as e:
        results.append(f"{BOLD}Ошибка:{RESET} {GREEN}Ошибка подключения к сессии Telegram: {e}{RESET}")
        print("\n".join(results))
        save_results(f"telegram_{username}", "\n".join(results))
        return

    try:
        user = await client.get_entity(username)
    except Exception as e:
        results.append(f"{BOLD}Ошибка:{RESET} {GREEN}Ошибка получения данных пользователя: {e}{RESET}")
        await client.disconnect()
        print("\n".join(results))
        save_results(f"telegram_{username}", "\n".join(results))
        return

    id = user.id
    fname = user.first_name
    lname = user.last_name
    username = user.username
    photo = user.photo

    results.append(f"{BOLD}Результаты от Telegram:{RESET}")
    results.append(f"{BOLD}ID пользователя:{RESET} {GREEN}{id}{RESET}")
    results.append(f"{BOLD}Имя:{RESET} {GREEN}{fname}{RESET}")
    results.append(f"{BOLD}Фамилия:{RESET} {GREEN}{lname if lname else 'Не указана'}{RESET}")
    results.append(f"{BOLD}Имя пользователя:{RESET} {GREEN}@{username if username else 'Не указано'}{RESET}")
    results.append(f"{BOLD}Фото профиля:{RESET} {GREEN}{'Есть' if photo else 'Нет'}{RESET}")
    results.append("---")
    results.append(f"{BOLD}Начало отслеживания статуса... (Нажмите Ctrl+C для остановки){RESET}")

    logged_events = set()
    last_status_str = None
    last_username = username
    last_fname = fname
    last_lname = lname
    last_photo_id = photo.photo_id if photo else None

    try:
        while True:
            try:
                user = await client.get_entity(id)
            except Exception as e:
                error_msg = f"Ошибка получения данных пользователя: {e}"
                if error_msg not in logged_events:
                    results.append(f"{BOLD}Ошибка:{RESET} {GREEN}{error_msg}{RESET}")
                    logged_events.add(error_msg)
                    print(results[-1])
                await asyncio.sleep(5)
                continue

            now = datetime.now()
            current_username = user.username
            current_fname = user.first_name
            current_lname = user.last_name
            current_photo = user.photo
            current_photo_id = current_photo.photo_id if current_photo else None
            current_status = user.status

            # Check for username change
            if current_username != last_username:
                event = f"username_change_{last_username}_to_{current_username}"
                if event not in logged_events:
                    us_time = now.strftime("%H:%M:%S")
                    results.append(f"{BOLD}Изменение имени пользователя:{RESET} {GREEN}@{last_username} -> @{current_username} ({us_time}){RESET}")
                    logged_events.add(event)
                    print(results[-1])
                last_username = current_username

            # Check for first name change
            if current_fname != last_fname:
                event = f"fname_change_{last_fname}_to_{current_fname}"
                if event not in logged_events:
                    fname_time = now.strftime("%H:%M:%S")
                    results.append(f"{BOLD}Изменение имени:{RESET} {GREEN}{last_fname} -> {current_fname} ({fname_time}){RESET}")
                    logged_events.add(event)
                    print(results[-1])
                last_fname = current_fname

            # Check for last name change
            if current_lname != last_lname:
                event = f"lname_change_{last_lname}_to_{current_lname}"
                if event not in logged_events:
                    lname_time = now.strftime("%H:%M:%S")
                    results.append(f"{BOLD}Изменение фамилии:{RESET} {GREEN}{last_lname if last_lname else 'Не указана'} -> {current_lname if current_lname else 'Не указана'} ({lname_time}){RESET}")
                    logged_events.add(event)
                    print(results[-1])
                last_lname = current_lname

            # Check for profile picture changes
            if last_photo_id is None and current_photo_id is not None:
                event = "photo_added"
                if event not in logged_events:
                    av_time = now.strftime("%H:%M:%S")
                    results.append(f"{BOLD}Фото профиля:{RESET} {GREEN}Установлено фото ({av_time}){RESET}")
                    logged_events.add(event)
                    print(results[-1])
                last_photo_id = current_photo_id
            elif last_photo_id is not None and current_photo_id is None:
                event = "photo_removed"
                if event not in logged_events:
                    av_time = now.strftime("%H:%M:%S")
                    results.append(f"{BOLD}Фото профиля:{RESET} {GREEN}Фото удалено ({av_time}){RESET}")
                    logged_events.add(event)
                    print(results[-1])
                last_photo_id = current_photo_id
            elif last_photo_id is not None and current_photo_id is not None and current_photo_id != last_photo_id:
                event = f"photo_changed_{current_photo_id}"
                if event not in logged_events:
                    av_time = now.strftime("%H:%M:%S")
                    results.append(f"{BOLD}Фото профиля:{RESET} {GREEN}Фото изменено ({av_time}){RESET}")
                    logged_events.add(event)
                    print(results[-1])
                last_photo_id = current_photo_id

            # Check for status changes
            current_status_str = None
            if isinstance(current_status, UserStatusOnline):
                current_status_str = 'online'
            elif isinstance(current_status, UserStatusOffline):
                current_status_str = 'offline'
            else:
                current_status_str = 'unknown'

            if current_status_str != last_status_str:
                event = f"status_{current_status_str}"
                if event not in logged_events:
                    status_time = now.strftime("%H:%M:%S")
                    if current_status_str == 'online':
                        results.append(f"{BOLD}Статус:{RESET} {GREEN}@{username} онлайн ({status_time}){RESET}")
                    elif current_status_str == 'offline':
                        results.append(f"{BOLD}Статус:{RESET} {GREEN}@{username} оффлайн ({status_time}){RESET}")
                    else:
                        results.append(f"{BOLD}Статус:{RESET} {GREEN}@{username} статус неизвестен ({status_time}){RESET}")
                    logged_events.add(event)
                    print(results[-1])
                last_status_str = current_status_str

            await asyncio.sleep(1)

    except KeyboardInterrupt:
        results.append(f"{BOLD}Отслеживание остановлено пользователем{RESET}")
        await client.disconnect()
    except Exception as e:
        error_msg = f"Ошибка в процессе отслеживания: {e}"
        if error_msg not in logged_events:
            results.append(f"{BOLD}Ошибка:{RESET} {GREEN}{error_msg}{RESET}")
            logged_events.add(error_msg)
            print(results[-1])
        await client.disconnect()

    finally:
        final_results = "\n".join(results)
        print(final_results)
        save_results(f"telegram_{username}", final_results)

# Format results for console display with white labels and green values
def format_results(data, service_name):
    result = [f"{BOLD}Результаты от {service_name}:{RESET}"]
    if isinstance(data, str):
        result.append(f"{BOLD}Сообщение:{RESET} {GREEN}{data}{RESET}")
    elif data and "error" not in data:
        if isinstance(data, dict) and "status" in data:
            # Заменяем "found" на "Данные найдены"
            status = "Данные найдены" if data['status'] == "found" else "Данные не найдены" if data['status'] == "not found" else data['status']
            result.append(f"{BOLD}Статус:{RESET} {GREEN}{status}{RESET}")
            if "note" in data:
                result.append(f"{BOLD}Примечание:{RESET} {GREEN}{data['note']}{RESET}")
            if "databases" in data and "collections" in data:
                result.append(f"{BOLD}Найдено в базах данных:{RESET} {GREEN}{', '.join(data['databases'])}{RESET}")
                result.append(f"{BOLD}Найдено в коллекциях:{RESET} {GREEN}{', '.join(data['collections'])}{RESET}")
            if "data" in data:
                result.append(f"{BOLD}Найдено записей:{RESET} {GREEN}{len(data['data']) if isinstance(data['data'], list) else 1}{RESET}")
                if isinstance(data["data"], list):
                    for record in data["data"]:
                        if isinstance(record, str):
                            result.append(f"{BOLD}Информация:{RESET} {GREEN}{record}{RESET}")
                        elif isinstance(record, dict):
                            for key, value in record.items():
                                formatted_key = key.replace('_', ' ').title()
                                result.append(f"{BOLD}{formatted_key}:{RESET} {GREEN}{value}{RESET}")
                        result.append("---")
                elif isinstance(data["data"], dict):
                    for key, value in data["data"].items():
                        formatted_key = key.replace('_', ' ').title()
                        result.append(f"{BOLD}{formatted_key}:{RESET} {GREEN}{value}{RESET}")
                    result.append("---")
            if "link" in data:
                result.append(f"{BOLD}Ссылка для проверки:{RESET} {GREEN}{data['link']}{RESET}")
            # Специальная обработка для OK.ru для отображения данных аккаунта
            if service_name == "OK.ru" and data.get('status') == "found":
                result.append(f"{BOLD}Данные аккаунта OK.ru:{RESET}")
                for key in ['masked_name', 'masked_email', 'masked_phone', 'profile_info', 'profile_registred']:
                    if key in data and data[key]:
                        formatted_key = key.replace('_', ' ').title()
                        result.append(f"{BOLD}{formatted_key}:{RESET} {GREEN}{data[key]}{RESET}")
            if service_name == "IP Info":
                result.append(f"{BOLD}Страна:{RESET} {GREEN}{data.get('country', 'Unknown')}{RESET}")
                result.append(f"{BOLD}Город:{RESET} {GREEN}{data.get('city', 'Unknown')}{RESET}")
                result.append(f"{BOLD}Регион:{RESET} {GREEN}{data.get('region', 'Unknown')}{RESET}")
                result.append(f"{BOLD}Провайдер:{RESET} {GREEN}{data.get('isp', 'Unknown')}{RESET}")
                result.append(f"{BOLD}Широта:{RESET} {GREEN}{data.get('latitude', 'Unknown')}{RESET}")
                result.append(f"{BOLD}Долгота:{RESET} {GREEN}{data.get('longitude', 'Unknown')}{RESET}")
                result.append(f"{BOLD}Часовой пояс:{RESET} {GREEN}{data.get('timezone', 'Unknown')}{RESET}")
                result.append(f"{BOLD}VPN или Proxy:{RESET} {GREEN}{'Да' if data.get('vpn_or_proxy', False) else 'Нет'}{RESET}")
                result.append(f"{BOLD}Tor:{RESET} {GREEN}{'Да' if data.get('tor', False) else 'Нет'}{RESET}")
                result.append(f"{BOLD}Хостинг:{RESET} {GREEN}{'Да' if data.get('hosting', False) else 'Нет'}{RESET}")
        elif isinstance(data, dict):
            result.append(f"{BOLD}Статус:{RESET} {GREEN}Данные найдены{RESET}")
            for key, value in data.items():
                if value and key != 'status':
                    formatted_key = key.replace('_', ' ').title()
                    result.append(f"{BOLD}{formatted_key}:{RESET} {GREEN}{value}{RESET}")
    else:
        error_msg = data.get("error", f"Данные от {service_name} не найдены.") if data else f"Данные от {service_name} не найдены."
        result.append(f"{BOLD}Ошибка:{RESET} {GREEN}{error_msg}{RESET}")
        if data and "note" in data:
            result.append(f"{BOLD}Примечание:{RESET} {GREEN}{data['note']}{RESET}")
        if data and "link" in data:
            result.append(f"{BOLD}Ссылка для проверки:{RESET} {GREEN}{data['link']}{RESET}")
    result.append("")
    return "\n".join(result)

# Save results to file
def save_results(query, results):
    output_dir = "hunting"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    safe_query = re.sub(r'[^\w\-@.+]', '_', query)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"{safe_query}_{timestamp}.txt")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"OSINT Results for Query: {query}\n")
            f.write(f"Timestamp: {timestamp}\n\n")
            f.write(results)
        print(f"\n{BOLD}Результаты сохранены в {filename}{RESET}")
    except Exception as e:
        print(f"\n{BOLD}Не удалось сохранить результаты: {e}{RESET}")

# Clear console function
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Phone OSINT function
async def phone_osint(phone):
    results = [f"{BOLD}OSINT-поиск по номеру телефона: {phone}\n{RESET}"]

    # Валидация номера телефона
    try:
        parsed_number = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{BOLD}Ошибка: Недействительный номер телефона. Введите номер в международном формате (например, +1234567890).{RESET}")
            return
    except phonenumbers.phonenumberutil.NumberParseException:
        print(f"{BOLD}Ошибка: Номер телефона должен быть в международном формате (например, +1234567890).{RESET}")
        return

    # Проверка UsersBox
    usersbox_response = await check_usersbox(phone)
    results.append(format_results(usersbox_response, "UsersBox"))

    # Проверка Intelx
    intelx_response = await intelx_search(phone)
    results.append(format_results(intelx_response, "Intelx"))

    # Проверка OK.ru
    okru_response = check_okru_account(phone)
    results.append(format_results(okru_response, "OK.ru"))

    # Проверка Avito
    avito_response = await check_avito(phone)
    results.append(format_results(avito_response, "Avito"))

    # Проверка HLR информации
    hlr_response = await defolt(phone)
    results.append(f"{BOLD}Результаты HLR:{RESET}")
    if hlr_response.get("status") != "error":
        results.append(f"{BOLD}Статус:{RESET} {GREEN}Данные найдены{RESET}")
        results.append(f"{BOLD}Страна:{RESET} {GREEN}{hlr_response['country']}{RESET}")
        results.append(f"{BOLD}Регион:{RESET} {GREEN}{hlr_response['region']}{RESET}")
        results.append(f"{BOLD}Оператор:{RESET} {GREEN}{hlr_response['operator']}{RESET}")
        results.append(f"{BOLD}MCC:{RESET} {GREEN}{hlr_response['mcc']}{RESET}")
        results.append(f"{BOLD}MNC:{RESET} {GREEN}{hlr_response['mnc']}{RESET}")
    else:
        results.append(f"{BOLD}Ошибка:{RESET} {GREEN}{hlr_response['error']}{RESET}")
    results.append("")

    # Получение данных с htmlweb.ru
    http_web_checker = HttpWebNumber()
    number_data = http_web_checker.get_number_data(phone)
    results.append(f"{BOLD}Результаты от htmlweb.ru:{RESET}")
    if "error" not in number_data:
        country = number_data.get('country', {})
        capital = number_data.get('capital', {})
        region = number_data.get('region', {"autocod": "Unknown", "name": "Unknown", "okrug": "Unknown"})
        other = number_data.get('0', {})
        results.append(f"{BOLD}Статус:{RESET} {GREEN}Данные найдены{RESET}")
        if country.get("country_code3") == 'UKR':
            results.append(f"{BOLD}Страна:{RESET} {GREEN}Украина{RESET}")
        else:
            results.append(f"{BOLD}Страна:{RESET} {GREEN}{country.get('name', 'Unknown')}, {country.get('fullname', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Город:{RESET} {GREEN}{other.get('name', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Почтовый индекс:{RESET} {GREEN}{other.get('post', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Телефонные коды:{RESET} {GREEN}{capital.get('telcod', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Оператор:{RESET} {GREEN}{other.get('oper', 'Unknown')}, {other.get('oper_brand', 'Unknown')}, {other.get('def', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Местоположение:{RESET} {GREEN}{country.get('name', 'Unknown')}, {region.get('name', 'Unknown')}, {other.get('name', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Регион:{RESET} {GREEN}{number_data.get('location', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Штат/Округ:{RESET} {GREEN}{region.get('name', 'Unknown')}, {region.get('okrug', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Широта/Долгота:{RESET} {GREEN}{other.get('latitude', 'Unknown')}, {other.get('longitude', 'Unknown')}{RESET}")
        results.append(f"{BOLD}Лимиты поиска:{RESET} {GREEN}{number_data.get('limit', 'Unknown')}{RESET}")
    else:
        results.append(f"{BOLD}Ошибка:{RESET} {GREEN}{number_data.get('error', 'Ошибка получения данных с htmlweb.ru')}{RESET}")
    results.append("")

    # Получение данных с phoneradar.ru
    link = f"http://phoneradar.ru/phone/{phone}"
    results.append(f"{BOLD}Результаты от phoneradar.ru:{RESET}")
    try:
        response = requests.get(link, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            result = soup.find('tbody')
            if result:
                results.append(f"{BOLD}Статус:{RESET} {GREEN}Данные найдены{RESET}")
                lines = result.text.strip().split('\n')
                for line in filter(lambda x: x.strip(), lines):
                    parts = line.strip().split(':', 1)
                    if len(parts) == 2:
                        label, value = parts
                        results.append(f"{BOLD}{label.strip()}:{RESET} {GREEN}{value.strip()}{RESET}")
                    else:
                        results.append(f"{BOLD}Информация:{RESET} {GREEN}{line.strip()}{RESET}")
            else:
                results.append(f"{BOLD}Статус:{RESET} {GREEN}Данные не найдены{RESET}")
                results.append(f"{BOLD}Примечание:{RESET} {GREEN}Информация на phoneradar.ru не найдена.{RESET}")
        else:
            results.append(f"{BOLD}Ошибка:{RESET} {GREEN}Недействительный номер или phoneradar.ru временно недоступен.{RESET}")
    except requests.RequestException as e:
        results.append(f"{BOLD}Ошибка:{RESET} {GREEN}Ошибка подключения к phoneradar.ru: {e}{RESET}")
    results.append("")

    # Анализ номера телефона с использованием get_phone_number_info
    phone_info = get_phone_number_info(phone, lang='ru')
    results.append(f"{BOLD}Дополнительная информация о номере:{RESET}")
    if phone_info:
        results.append(f"{BOLD}Статус:{RESET} {GREEN}Данные найдены{RESET}")
        results.append(f"{BOLD}Полный номер:{RESET} {GREEN}{phone_info['full_number']}{RESET}")
        results.append(f"{BOLD}Код страны:{RESET} {GREEN}+{phone_info['country_code']}{RESET}")
        results.append(f"{BOLD}Национальный номер:{RESET} {GREEN}{phone_info['national_number']}{RESET}")
        results.append(f"{BOLD}Тип номера:{RESET} {GREEN}{phone_info['number_type']}{RESET}")
        results.append(f"{BOLD}Валидность номера:{RESET} {GREEN}{'Валидный' if phone_info['is_valid'] else 'Невалидный'}{RESET}")
        results.append(f"{BOLD}Местоположение:{RESET} {GREEN}{phone_info['geo_location']}{RESET}")
        results.append(f"{BOLD}Оператор:{RESET} {GREEN}{phone_info['operator']}{RESET}")
        results.append(f"{BOLD}Часовые пояса:{RESET} {GREEN}{', '.join(phone_info['time_zones'])}{RESET}")
        results.append(f"{BOLD}Текущее время в регионе:{RESET} {GREEN}{phone_info['current_time']} ({phone_info['utc_offset']}){RESET}")
        if phone_info['suspicious']:
            results.append(f"{BOLD}Предупреждение:{RESET} {GREEN}Номер с префиксом {phone[:4] if phone.startswith('+') else phone[:3]} может быть подозрительным (часто используется для мошенничества).{RESET}")
        else:
            results.append(f"{BOLD}Предупреждение:{RESET} {GREEN}Номер не показывает типичных признаков мошенничества.{RESET}")
    else:
        results.append(f"{BOLD}Ошибка:{RESET} {GREEN}Невозможно получить дополнительную информацию о номере.{RESET}")
    results.append("")

    # Генерация ссылок на социальные сети
    clean_phone = ''.join(filter(str.isdigit, phone)) if phone.startswith('+') else phone
    results.append(f"{BOLD}Ссылки на соцсети и мессенджеры:{RESET}")
    social_links = [
        ("Viber", f"https://viber.me/{clean_phone}"),
        ("WhatsApp", f"https://wa.me/{clean_phone}"),
        ("Telegram", f"https://t.me/{phone}"),
        ("Skype", f"skype:{phone}?call"),
        ("Snapchat", f"https://www.snapchat.com/add?phone={clean_phone}")
    ]
    vk_dork_query = f'site:vk.com "{phone}"'
    encoded_vk_query = urllib.parse.quote_plus(vk_dork_query)
    vk_dork_link = f"https://www.google.com/search?q={encoded_vk_query}"
    social_links.append(("VK (Dorking)", vk_dork_link))

    for platform, url in social_links:
        results.append(f"{BOLD}{platform}:{RESET} {GREEN}{url}{RESET}")
    results.append("")

    # Добавление цепочки поиска
    search_chain = f"""
{BOLD}┌───────────────────────────────────────────────────────────────────────────────┐{RESET}
{BOLD}│                              ПОИСК ИНФОРМАЦИИ ПО НОМЕРУ ТЕЛЕФОНА              │{RESET}
{BOLD}└───────────────────────────────────────────────────────────────────────────────┘{RESET}
                                      ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│       ВХОДНЫЕ ДАННЫЕ    │{RESET}
{BOLD}│  +───────────────────+  │{RESET}
{BOLD}│  | {phone.center(14)}|  │{RESET}
{BOLD}│  +───────────────────+  │{RESET}
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌──────────────────────────┐{RESET}
{BOLD}│   ВАЛИДАЦИЯ И ПАРСИНГ    │{RESET}
{BOLD}│ • Проверка формата       │{RESET}  ◄── Соответствие маске (E.164, национальный стандарт)
{BOLD}│ • Определение страны     │{RESET}  ◄── Код страны (+7, +1, +44 и т.д.)
{BOLD}│ • Идентификация оператора│{RESET}  ◄── По диапазонам номеров (МТС, Билайн, Verizon и др.)
{BOLD}└─────────────┬────────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│  ОТКРЫТЫЕ ИСТОЧНИКИ     │{RESET}
{BOLD}│ • Поиск в соцсетях:     │{RESET}  ◄── VK, Telegram, Facebook, Instagram (по номеру/username)
{BOLD}│ • Форумы и базы данных  │{RESET}  ◄── Blacklist, spam databases (Truecaller, NumBuster)
{BOLD}│ • Госуслуги/реестры*    │{RESET}  ◄── Если доступно (например, проверка через "Росреестр")
{BOLD}│ • Dark Web (при наличии │{RESET}  ◄── Анализ утечек (Have I Been Pwned, BreachDirectory)
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│  ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ  │{RESET}
{BOLD}│ • Поиск связанных email │{RESET}  ◄── Через обратный поиск (Google, Яндекс)
{BOLD}│ • Поиск в WHOIS         │{RESET}  ◄── Если номер привязан к домену
{BOLD}│ • Геолокация (LBS)*     │{RESET}  ◄── Примерное местоположение (по вышкам сотовой связи)
{BOLD}│ • История звонков*      │{RESET}  ◄── Если есть доступ к данным оператора (только по запросу)
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│   ФИНАЛЬНЫЙ ОТЧЕТ       │{RESET}
{BOLD}│ • Основная информация:  │{RESET}  ◄── Имя, регион, оператор
{BOLD}│ • Связанные аккаунты    │{RESET}  ◄── Соцсети, мессенджеры
{BOLD}│ • Угрозы и репутация    │{RESET}  ◄── Спам, мошенничество, blacklist
{BOLD}│ • Рекомендации          │{RESET}  ◄── Блокировка, осторожность, дальнейший мониторинг
{BOLD}└─────────────────────────┘{RESET}
"""
    results.append(search_chain)

   
    final_results = "\n".join(results)
    print(final_results)

   
    save_results(phone, final_results)



async def email_osint(email):
    results = [f"{BOLD}OSINT-поиск по email: {email}\n{RESET}"]
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        print(f"{BOLD}Ошибка: Недействительный формат email-адреса!{RESET}")
        return
    usersbox_response = await check_usersbox(email)
    results.append(format_results(usersbox_response, "UsersBox"))
    hudsonrock_response = await check_hudsonrock(email)
    results.append(format_results(hudsonrock_response, "Hudson Rock"))
    leakcheck_response = await check_email_breaches(email)
    results.append(format_results(leakcheck_response, "LeakCheck"))
    okru_response = check_okru_account(email)
    results.append(format_results(okru_response, "OK.ru"))
    vk_response = check_vk_account(email)
    results.append(format_results(vk_response, "VK"))
    twitch_response = check_twitch_account(email)
    results.append(format_results(twitch_response, "Twitch"))
    pinterest_response = check_pinterest_account(email)
    results.append(format_results(pinterest_response, "Pinterest"))
    dork_query = f'from:{email}'
    encoded_dork_query = urllib.parse.quote_plus(dork_query)
    dork_link = f"https://www.google.com/search?q={encoded_dork_query}"
    results.append(f"{BOLD}Google Dork для поиска следов email:{RESET}")
    results.append(f"{BOLD}Ссылка:{RESET} {GREEN}{dork_link}{RESET}")
    results.append("")


    search_chain = f"""
{BOLD}┌───────────────────────────────────────────────────────────────────────────────┐{RESET}
{BOLD}│                              ПОИСК ИНФОРМАЦИИ ПО EMAIL                        │{RESET}
{BOLD}└───────────────────────────────────────────────────────────────────────────────┘{RESET}
                                      ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│       ВХОДНЫЕ ДАННЫЕ    │{RESET}
{BOLD}│  +───────────────────+  │{RESET}
{BOLD}│  | {email.center(14)}|  │{RESET}
{BOLD}│  +───────────────────+  │{RESET}
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌──────────────────────────┐{RESET}
{BOLD}│   ВАЛИДАЦИЯ И ПАРСИНГ    │{RESET}
{BOLD}│ • Проверка формата       │{RESET}  ◄── Соответствие стандарту RFC 5322
{BOLD}│ • Проверка домена        │{RESET}  ◄── DNS-записи (MX, SPF, DKIM)
{BOLD}│ • Идентификация провайдера│{RESET} ◄── Gmail, Yahoo, Mail.ru и др.
{BOLD}└─────────────┬────────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│  ОТКРЫТЫЕ ИСТОЧНИКИ     │{RESET}
{BOLD}│ • Соцсети и платформы   │{RESET}  ◄── VK, OK.ru, Twitch, Pinterest
{BOLD}│ • Утечки данных         │{RESET}  ◄── Hudson Rock, LeakCheck, HIBP
{BOLD}│ • Google Dorking        │{RESET}  ◄── Поиск следов (from:{email})
{BOLD}│ • Форумы и базы данных  │{RESET}  ◄── UsersBox, BreachDirectory
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│  ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ  │{RESET}
{BOLD}│ • Связанные аккаунты    │{RESET}  ◄── Обратный поиск через соцсети
{BOLD}│ • WHOIS-проверка домена │{RESET}  ◄── Регистрационные данные домена
{BOLD}│ • Репутация email       │{RESET}  ◄── Проверка на спам/черные списки
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│   ФИНАЛЬНЫЙ ОТЧЕТ       │{RESET}
{BOLD}│ • Основная информация:  │{RESET}  ◄── Провайдер, статус домена
{BOLD}│ • Связанные аккаунты    │{RESET}  ◄── Соцсети, платформы
{BOLD}│ • Утечки данных         │{RESET}  ◄── Список утечек, если найдены
{BOLD}│ • Рекомендации          │{RESET}  ◄── Смена пароля, мониторинг
{BOLD}└─────────────────────────┘{RESET}
"""
    results.append(search_chain)

    # Вывод результатов
    final_results = "\n".join(results)
    print(final_results)
    save_results(email, final_results)

# IP OSINT function
async def ip_osint(ip):
    results = [f"{BOLD}OSINT-поиск по IP-адресу: {ip}\n{RESET}"]
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"{BOLD}Ошибка: Недействительный формат IP-адреса! Введите корректный IPv4 или IPv6 адрес.{RESET}")
        return
    usersbox_response = await check_usersbox(ip)
    results.append(format_results(usersbox_response, "UsersBox"))
    leakcheck_response = await check_ip_breaches(ip)
    results.append(format_results(leakcheck_response, "LeakCheck"))
    ip_info_response = await check_ip_info(ip)
    results.append(format_results(ip_info_response, "IP Info"))
    dork_query = f'"{ip}"'
    encoded_dork_query = urllib.parse.quote_plus(dork_query)
    dork_link = f"https://www.google.com/search?q={encoded_dork_query}"
    results.append(f"{BOLD}Google Dork для поиска следов IP:{RESET}")
    results.append(f"{BOLD}Ссылка:{RESET} {GREEN}{dork_link}{RESET}")
    results.append("")

    # Добавление цепочки поиска для IP
    search_chain = f"""
{BOLD}┌───────────────────────────────────────────────────────────────────────────────┐{RESET}
{BOLD}│                              ПОИСК ИНФОРМАЦИИ ПО IP-АДРЕСУ                    │{RESET}
{BOLD}└───────────────────────────────────────────────────────────────────────────────┘{RESET}
                                      ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│       ВХОДНЫЕ ДАННЫЕ    │{RESET}
{BOLD}│  +───────────────────+  │{RESET}
{BOLD}│  | {ip.center(14)}|  │{RESET}
{BOLD}│  +───────────────────+  │{RESET}
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌──────────────────────────┐{RESET}
{BOLD}│   ВАЛИДАЦИЯ И ПАРСИНГ    │{RESET}
{BOLD}│ • Проверка формата       │{RESET}  ◄── IPv4/IPv6 валидность
{BOLD}│ • Тип адреса             │{RESET}  ◄── Публичный/приватный, статический/динамический
{BOLD}│ • ASN/провайдер          │{RESET}  ◄── Определение ISP (ipapi.co, WHOIS)
{BOLD}└─────────────┬────────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│  ОТКРЫТЫЕ ИСТОЧНИКИ     │{RESET}
{BOLD}│ • Геолокация            │{RESET}  ◄── Страна, город, координаты (ipapi.co)
{BOLD}│ • Утечки данных         │{RESET}  ◄── LeakCheck, UsersBox
{BOLD}│ • WHOIS-записи          │{RESET}  ◄── Владелец сети, регистратор
{BOLD}│ • Google Dorking        │{RESET}  ◄── Поиск следов ("{ip}")
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│  ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ  │{RESET}
{BOLD}│ • Проверка VPN/Proxy    │{RESET}  ◄── Обнаружение анонимайзеров
{BOLD}│ • Проверка Tor          │{RESET}  ◄── Проверка на Tor exit nodes
{BOLD}│ • Репутация IP          │{RESET}  ◄── Черные списки, спам-базы
{BOLD}│ • Связанные домены      │{RESET}  ◄── Обратный поиск доменов
{BOLD}└─────────────┬───────────┘{RESET}
              ↓
{BOLD}┌─────────────────────────┐{RESET}
{BOLD}│   ФИНАЛЬНЫЙ ОТЧЕТ       │{RESET}
{BOLD}│ • Основная информация:  │{RESET}  ◄── Геолокация, провайдер
{BOLD}│ • Угрозы и репутация    │{RESET}  ◄── VPN, Tor, черные списки
{BOLD}│ • Связанные данные      │{RESET}  ◄── Утечки, домены
{BOLD}│ • Рекомендации          │{RESET}  ◄── Блокировка, мониторинг
{BOLD}└─────────────────────────┘{RESET}
"""
    results.append(search_chain)

    final_results = "\n".join(results)
    print(final_results)
    save_results(ip, final_results)


async def main_menu():
    while True:
        clear_console()
        print(BANNER)
        print(f"{BOLD}Hunter OSINT{RESET}")
        print(f"{GREEN}[{RESET}1{GREEN}]{RESET} {GREEN}<-->{RESET} Поиск по номеру телефона")
        print(f"{GREEN}[{RESET}2{GREEN}]{RESET} {GREEN}<-->{RESET} Поиск по почте")
        print(f"{GREEN}[{RESET}3{GREEN}]{RESET} {GREEN}<-->{RESET} Поиск по IP-адресу")
        print(f"{GREEN}[{RESET}4{GREEN}]{RESET} {GREEN}<-->{RESET} Отслеживание Telegram")
        print(f"{GREEN}[{RESET}5{GREEN}]{RESET} {GREEN}<-->{RESET} Выход")
        choice = input(f"\n{BOLD}└[@]HunterOsint-> {RESET}")

        if choice == "1":
            clear_console()
            phone = input(f"{BOLD}Введите номер телефона (например, +1234567890): {RESET}").strip()
            if phone:
                await phone_osint(phone)
                input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")
            else:
                print(f"{BOLD}Ошибка: Пожалуйста, введите номер телефона!{RESET}")
                input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")
        elif choice == "2":
            clear_console()
            email = input(f"{BOLD}Введите email-адрес (например, example@domain.com): {RESET}").strip()
            if email:
                await email_osint(email)
                input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")
            else:
                print(f"{BOLD}Ошибка: Пожалуйста, введите email-адрес!{RESET}")
                input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")
        elif choice == "3":
            clear_console()
            ip = input(f"{BOLD}Введите IP-адрес (например, 192.168.1.1): {RESET}").strip()
            if ip:
                await ip_osint(ip)
                input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")
            else:
                print(f"{BOLD}Ошибка: Пожалуйста, введите IP-адрес!{RESET}")
                input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")
        elif choice == "4":
            clear_console()
            username = input(f"{BOLD}Введите имя пользователя Telegram (без @): {RESET}").strip()
            if username:
                await telegram_track(username)
                input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")
            else:
                print(f"{BOLD}Ошибка: Пожалуйста, введите имя пользователя Telegram!{RESET}")
                input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")
        elif choice == "5":
            print(f"{BOLD}Выход из программы...{RESET}")
            break
        else:
            print(f"{BOLD}Недействительный выбор, попробуйте снова.{RESET}")
            input(f"\n{BOLD}Нажмите Enter для возврата в меню...{RESET}")

if __name__ == "__main__":
    asyncio.run(main_menu())
