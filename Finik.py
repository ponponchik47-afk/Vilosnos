import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
import re

console = Console()

banner = f"""
 _______                               __                   ________ __          __ __       __ 
|       \                             |  \                 |        \  \        |  \  \     |  
| ▓▓▓▓▓▓▓\ ______   ______   _______ _| ▓▓_    ______      | ▓▓▓▓▓▓▓▓\▓▓_______  \▓▓ ▓▓   __ \▓▓
| ▓▓__/ ▓▓/      \ /      \ /       \   ▓▓ \  /      \     | ▓▓__   |  \       \|  \ ▓▓  /  \  
| ▓▓    ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\  ▓▓▓▓▓▓▓\▓▓▓▓▓▓ |  ▓▓▓▓▓▓\    | ▓▓  \  | ▓▓ ▓▓▓▓▓▓▓\ ▓▓ ▓▓_/  ▓▓ ▓▓
| ▓▓▓▓▓▓▓| ▓▓   \▓▓ ▓▓  | ▓▓\▓▓    \  | ▓▓ __| ▓▓  | ▓▓    | ▓▓▓▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓ ▓▓   ▓▓| ▓▓
| ▓▓     | ▓▓     | ▓▓__/ ▓▓_\▓▓▓▓▓▓\ | ▓▓|  \ ▓▓__/ ▓▓    | ▓▓     | ▓▓ ▓▓  | ▓▓ ▓▓ ▓▓▓▓▓▓\| ▓▓
| ▓▓     | ▓▓      \▓▓    ▓▓       ▓▓  \▓▓  ▓▓\▓▓    ▓▓    | ▓▓     | ▓▓ ▓▓  | ▓▓ ▓▓ ▓▓  \▓▓\ ▓▓
 \▓▓      \▓▓       \▓▓▓▓▓▓ \▓▓▓▓▓▓▓    \▓▓▓▓  \▓▓▓▓▓▓      \▓▓      \▓▓\▓▓   \▓▓\▓▓\▓▓   \▓▓\▓▓

                               @Fell1ksx | @FreeBestSoft | Prosto Finiki
"""


def create_menu():
    services = [
        "[1] IP-Геолокация", "[2] Анализ номера", "[3] Email-разведка",
        "[4] Поиск по username", "[5] Яндекс-поиск", "[6] Соцсети сканер",
        "[7] Детекция VPN", "[8] Проверка утечек", "[9] WHOIS домена",
        "[10] Анализ метаданных", "[11] Поиск по фото", "[12] Скрипт-анализ",
        "[13] Банковский BIN", "[14] Крипто-кошельки", "[15] IMEI устройств",
        "[16] MAC-адрес устройств", "[17] История домена", "[18] SSL сертификаты",
        "[19] Отпечатки браузера", "[20] Darknet мониторинг", "[21] Telegram разведка",
        "[22] Instagram анализ", "[23] VKontakte сканер", "[24] WhatsApp детекция",
        "[25] Bitcoin транзакции", "[26] Ethereum анализ", "[27] Налоговые данные",
        "[28] Судебные дела", "[29] Патентный поиск", "[30] Товарные знаки",
        "[31] Авиаперелеты", "[32] Гостиничные брони", "[33] Аренда жилья",
        "[34] Автомобильные номера", "[35] Водительские права", "[36] Паспортные данные",
        "[37] Медицинские записи", "[38] Образовательные данные", "[39] Трудовой стаж",
        "[40] Кредитная история", "[41] Недвижимость поиск", "[42] Земельные участки",
        "[43] Корпоративные данные", "[44] Морские суда", "[45] Воздушные суда"
    ]

    layout = Layout()
    layout.split_column(
        Layout(Panel(banner, title="Prosto Finiki", style="bold cyan")),
        Layout(name="services")
    )
    layout["services"].split_row(
        Layout(Panel("\n".join(services[:15]), title="Prosto Finiki", style="green")),
        Layout(Panel("\n".join(services[15:30]), title="Prosto Finiki", style="yellow")),
        Layout(Panel("\n".join(services[30:45]), title="Prosto Finiki", style="red"))
    )

    console.print(layout)


def yandex_search(query):
    try:
        url = f"https://yandex.ru/search/?text={query}&numdoc=5"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)

        pattern = r'<li class="serp-item">.*?<h2.*?><a.*?href="(.*?)".*?>(.*?)</a>.*?<div class="text-container">(.*?)</div>'
        matches = re.findall(pattern, response.text, re.DOTALL)

        results = []
        for match in matches:
            link = match[0]
            title = re.sub('<.*?>', '', match[1])
            desc = re.sub('<.*?>', '', match[2])
            results.append({"Название": title, "Описание": desc, "Ссылка": link})

        return results
    except:
        return []


def search_ip(ip):
    results = {}
    apis = [
        ("IPAPI.co", f"https://ipapi.co/{ip}/json/"),
        ("IP-API.com", f"http://ip-api.com/json/{ip}"),
        ("Abstract Intelligence",
         f"https://ip-intelligence.abstractapi.com/v1/?api_key=20bdf023c24f4e2587bdf1fcec924c10&ip_address={ip}"),
        ("Abstract Geolocation",
         f"https://ipgeolocation.abstractapi.com/v1/?api_key=20bdf023c24f4e2587bdf1fcec924c10&ip_address={ip}"),
        ("IPWho.org", f"https://api.ipwho.org/ip/{ip}?format=json"),
        ("IPSpeed.info", f"https://ipapi.ipspeed.info/?key=aI-zw79&ip={ip}")
    ]

    for name, url in apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"

    return results


def search_phone(phone):
    results = {}
    apis = [
        ("NumLookupAPI",
         f"https://api.numlookupapi.com/v1/validate/{phone}?apikey=num_live_wjd4V74gCwHHO4qoxYYEyYO9xBFblGx3twOy0BcU"),
        ("Abstract Validation",
         f"https://phonevalidation.abstractapi.com/v1/?api_key=9eb8826b744c4b6c8df2b61877071d63&phone={phone}"),
        ("Phone-Number-API", f"http://phone-number-api.com/json/?number={phone}")
    ]

    for name, url in apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"

    return results


def display_results(data, title):
    console.print(Panel.fit(f"[bold green]РЕЗУЛЬТАТЫ: {title}[/bold green]", style="red"))

    for service, result in data.items():
        if result != "Ошибка":
            panel_text = Text()
            panel_text.append(f"{service}:\n", style="yellow")
            panel_text.append(json.dumps(result, indent=2, ensure_ascii=False))
            console.print(Panel.fit(panel_text))
        else:
            console.print(Panel.fit(f"[red]❌ {service}: Ошибка API[/red]"))


console.clear()
create_menu()

choice = console.input("\n[bold red]Выберите: [/bold red]")

if choice == "1":
    target = console.input("[bold yellow]Введите IP адрес: [/bold yellow]")
    results = search_ip(target)
    display_results(results, f"IP {target}")

elif choice == "2":
    target = console.input("[bold yellow]Введите номер телефона: [/bold yellow]")
    results = search_phone(target)
    display_results(results, f"Телефон {target}")

elif choice == "5":
    target = console.input("[bold yellow]Введите запрос для Яндекс: [/bold yellow]")
    results = yandex_search(target)
    for result in results:
        console.print(Panel.fit(f"[yellow]Название:[/yellow] {result['Название']}\n"
                                f"[green]Описание:[/green] {result['Описание']}\n"
                                f"[blue]Ссылка:[/blue] {result['Ссылка']}"))

elif choice == "3":
        target = console.input("[bold yellow]Введите email адрес: [/bold yellow]")
        email_apis = [
            ("EmailRep", f"https://emailrep.io/{target}"),
            ("Hunter.io", f"https://api.hunter.io/v2/email-verifier?email={target}&api_key=YOUR_HUNTER_KEY"),
            ("Abstract Email",
             f"https://emailvalidation.abstractapi.com/v1/?api_key=9eb8826b744c4b6c8df2b61877071d63&email={target}")
        ]
        results = {}
        for name, url in email_apis:
            try:
                response = requests.get(url, timeout=10)
                results[name] = response.json()
            except:
                results[name] = "Ошибка"
        display_results(results, f"Email {target}")

elif choice == "4":
    target = console.input("[bold yellow]Введите username: [/bold yellow]")
    social_apis = [
        ("WhatsMyName", f"https://whatsmyname.app/api/v1/username/{target}"),
        ("Namechk", f"https://namechk.com/availability/{target}"),
        ("Social Analyzer", f"https://github.com/{target}")
    ]
    results = {}
    for name, url in social_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.text[:500] + "..." if len(response.text) > 500 else response.text
        except:
            results[name] = "Ошибка"
    display_results(results, f"Username {target}")

elif choice == "6":
    target = console.input("[bold yellow]Введите цель: [/bold yellow]")
    social_search = yandex_search(f"{target} site:vk.com OR site:instagram.com OR site:facebook.com")
    for result in social_search:
        console.print(Panel.fit(f"[yellow]Платформа:[/yellow] {result['Название']}\n"
                                f"[green]Информация:[/green] {result['Описание']}\n"
                                f"[blue]Ссылка:[/blue] {result['Ссылка']}"))

elif choice == "7":
    target = console.input("[bold yellow]Введите IP для проверки VPN: [/bold yellow]")
    vpn_apis = [
        ("IP2Proxy", f"https://api.ip2proxy.com/?ip={target}&key=F24D985D5D91131681A3D2030F0B07D5"),
        ("IPHub", f"http://iphub.info/api.php?ip={target}")
    ]
    results = {}
    for name, url in vpn_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json() if 'json' in response.headers.get('content-type', '') else response.text
        except:
            results[name] = "Ошибка"
    display_results(results, f"VPN Check {target}")

elif choice == "8":
    target = console.input("[bold yellow]Введите email/телефон для проверки утечек: [/bold yellow]")
    breach_apis = [
        ("HaveIBeenPwned", f"https://haveibeenpwned.com/api/v3/breachedaccount/{target}"),
        ("DeHashed", f"https://dehashed.com/api/search?query={target}")
    ]
    results = {}
    for name, url in breach_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json() if response.status_code == 200 else "Не найдено утечек"
        except:
            results[name] = "Ошибка"
    display_results(results, f"Breach Check {target}")

elif choice == "9":
    target = console.input("[bold yellow]Введите домен для WHOIS: [/bold yellow]")
    whois_apis = [
        ("Whois XML", f"https://www.whoisxmlapi.com/whoisserver/WhoisService?domainName={target}&outputFormat=JSON"),
        ("Whois Freaks", f"https://api.whoisfreaks.com/v1.0/whois?whois=live&domainName={target}")
    ]
    results = {}
    for name, url in whois_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"
    display_results(results, f"WHOIS {target}")
elif choice == "10":
    target = console.input("[bold yellow]Введите URL файла для анализа метаданных: [/bold yellow]")
    try:
        response = requests.get(target, timeout=15)
        metadata_info = {
            "Размер файла": f"{len(response.content)} байт",
            "Тип контента": response.headers.get('content-type', 'Неизвестно'),
            "Последнее изменение": response.headers.get('last-modified', 'Неизвестно'),
            "Сервер": response.headers.get('server', 'Неизвестно')
        }
        display_results({"Метаданные файла": metadata_info}, f"Метаданные {target}")
    except:
        console.print("[bold red]Ошибка загрузки файла[/bold red]")

elif choice == "11":
    target = console.input("[bold yellow]Введите URL изображения для обратного поиска: [/bold yellow]")
    reverse_image_apis = [
        ("Google Images", f"https://www.google.com/searchbyimage?image_url={target}"),
        ("Yandex Images", f"https://yandex.ru/images/search?url={target}&rpt=imageview")
    ]
    results = {}
    for name, url in reverse_image_apis:
        results[name] = f"Поиск по изображению: {url}"
    display_results(results, f"Reverse Image Search {target}")

elif choice == "12":
    target = console.input("[bold yellow]Введите URL для анализа скриптов: [/bold yellow]")
    try:
        response = requests.get(target, timeout=10)
        scripts = re.findall(r'<script[^>]*src="([^"]*)"', response.text)
        results = {"Найдено скриптов": len(scripts), "Скрипты": scripts[:10]}
        display_results({"Анализ скриптов": results}, f"Script Analysis {target}")
    except:
        console.print("[bold red]Ошибка анализа страницы[/bold red]")

elif choice == "13":
    target = console.input("[bold yellow]Введите BIN банковской карты (первые 6 цифр): [/bold yellow]")
    bin_apis = [
        ("Binlist", f"https://lookup.binlist.net/{target}"),
        ("BIN Check", f"https://api.bincodes.com/bin/?format=json&api_key=9fc53b3db09ca830488d19546a4fc2a1/515735/&bin={target}")
    ]
    results = {}
    for name, url in bin_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"
    display_results(results, f"BIN Check {target}")

elif choice == "14":
    target = console.input("[bold yellow]Введите адрес крипто-кошелька: [/bold yellow]")
    crypto_apis = [
        ("Blockchain.com", f"https://blockchain.info/rawaddr/{target}"),
        ("Etherscan", f"https://api.etherscan.io/api?module=account&action=balance&address={target}"),
        ("BlockCypher", f"https://api.blockcypher.com/v1/btc/main/addrs/{target}")
    ]
    results = {}
    for name, url in crypto_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"
    display_results(results, f"Crypto Wallet {target}")

elif choice == "15":
    target = console.input("[bold yellow]Введите IMEI устройства: [/bold yellow]")
    imei_apis = [
        ("IMEI Info", f"https://www.imei.info/api/check/{target}"),
        ("IMEI Check", f"https://api.imeicheck.com/check?imei={target}")
    ]
    results = {}
    for name, url in imei_apis:
        results[name] = f"Проверка IMEI: {url}"
    display_results(results, f"IMEI Check {target}")

elif choice == "16":
    target = console.input("[bold yellow]Введите MAC-адрес: [/bold yellow]")
    mac_apis = [
        ("MAC Vendors", f"https://api.macvendors.com/{target}"),
        ("MAC Lookup", f"https://www.macaddress.io/api/v1?apiKey=01k4ne93zz9t8rj4x9wdp159fe01k4ne9vp9rghw4024yct7nz6qdbmqroxexn3d&output=json&search={target}")
    ]
    results = {}
    for name, url in mac_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.text
        except:
            results[name] = "Ошибка"
    display_results(results, f"MAC Lookup {target}")

elif choice == "17":
    target = console.input("[bold yellow]Введите домен для истории: [/bold yellow]")
    history_apis = [
        ("Whois History", f"https://api.whoishistory.org/domain/{target}"),
        ("Archive.org", f"https://archive.org/wayback/available?url={target}")
    ]
    results = {}
    for name, url in history_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"
    display_results(results, f"Domain History {target}")

elif choice == "18":
    target = console.input("[bold yellow]Введите домен для SSL анализа: [/bold yellow]")
    ssl_apis = [
        ("SSL Labs", f"https://api.ssllabs.com/api/v3/analyze?host={target}"),
        ("SSL Check", f"https://api.sslcheck.ru/check?host={target}")
    ]
    results = {}
    for name, url in ssl_apis:
        results[name] = f"SSL проверка: {url}"
    display_results(results, f"SSL Analysis {target}")

elif choice == "19":
    target = console.input("[bold yellow]Введите User-Agent для анализа: [/bold yellow]")
    fingerprint_apis = [
        ("UserAgent API", f"https://api.useragent.dev/parse/{target}"),
        ("WhatIsMyBrowser", f"https://api.whatismybrowser.com/api/v2/user_agent_parse?user_agent={target}")
    ]
    results = {}
    for name, url in fingerprint_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"
    display_results(results, f"Browser Fingerprint {target}")

elif choice == "20":
    target = console.input("[bold yellow]Введите запрос для Darknet: [/bold yellow]")
    darknet_apis = [
        ("Onion Search", f"https://ahmia.fi/search/?q={target}"),
        ("DarkSearch", f"https://darksearch.io/api/search?query={target}")
    ]
    results = {}
    for name, url in darknet_apis:
        results[name] = f"Darknet поиск: {url}"
    display_results(results, f"Darknet Search {target}")
    display_results(results, f"Darknet Search {target}")

elif choice == "21":
    target = console.input("[bold yellow]Введите username Telegram для анализа: [/bold yellow]")
    tg_apis = [
        ("Telegram OSINT", f"https://t.me/{target}"),
        ("TGStat", f"https://api.tgstat.ru/users/search?q={target}"),
        ("Lyzem", f"https://lyzem.com/search?q={target}")
    ]
    results = {}
    for name, url in tg_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = f"Найдено в Telegram: {url}" if response.status_code == 200 else "Не найдено"
        except:
            results[name] = "Ошибка"
    display_results(results, f"Telegram Search {target}")

elif choice == "22":
    target = console.input("[bold yellow]Введите username Instagram для анализа: [/bold yellow]")
    instagram_apis = [
        ("Instagram Profile", f"https://www.instagram.com/{target}/"),
        ("Picuki", f"https://www.picuki.com/profile/{target}"),
        ("ImgInn", f"https://imginn.com/{target}/")
    ]
    results = {}
    for name, url in instagram_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = f"Аккаунт существует: {url}" if response.status_code == 200 else "Аккаунт не найден"
        except:
            results[name] = "Ошибка"
    display_results(results, f"Instagram Search {target}")

elif choice == "23":
    target = console.input("[bold yellow]Введите ID или username VK для анализа: [/bold yellow]")
    vk_apis = [
        ("VK Profile", f"https://vk.com/{target}"),
        ("VK Watch", f"https://vkwatch.com/{target}"),
        ("VK Scanner", f"https://vk.com/foaf.php?id={target}")
    ]
    results = {}
    for name, url in vk_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = f"Профиль VK: {url}" if response.status_code == 200 else "Профиль не найден"
        except:
            results[name] = "Ошибка"
    display_results(results, f"VK Search {target}")

elif choice == "24":
    target = console.input("[bold yellow]Введите номер WhatsApp для проверки: [/bold yellow]")
    whatsapp_apis = [
        ("WhatsApp Check", f"https://wa.me/{target}"),
        ("Web WhatsApp", f"https://web.whatsapp.com/send?phone={target}"),
        ("WhatsApp API", f"https://api.whatsapp.com/send?phone={target}")
    ]
    results = {}
    for name, url in whatsapp_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = f"Номер WhatsApp: {url}" if response.status_code == 200 else "Номер не зарегистрирован"
        except:
            results[name] = "Ошибка"
    display_results(results, f"WhatsApp Check {target}")

elif choice == "25":
    target = console.input("[bold yellow]Введите адрес Bitcoin кошелька: [/bold yellow]")
    bitcoin_apis = [
        ("Blockchain.com", f"https://blockchain.info/rawaddr/{target}"),
        ("Blockchair", f"https://api.blockchair.com/bitcoin/dashboards/address/{target}"),
        ("Bitaps", f"https://api.bitaps.com/btc/v1/blockchain/address/{target}")
    ]
    results = {}
    for name, url in bitcoin_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"
    display_results(results, f"Bitcoin Analysis {target}")

elif choice == "26":
    target = console.input("[bold yellow]Введите адрес Ethereum кошелька: [/bold yellow]")
    ethereum_apis = [
        ("Etherscan", f"https://api.etherscan.io/api?module=account&action=balance&address={target}"),
        ("Ethplorer", f"https://api.ethplorer.io/getAddressInfo/{target}?apiKey=freekey"),
        ("Blockchair", f"https://api.blockchair.com/ethereum/dashboards/address/{target}")
    ]
    results = {}
    for name, url in ethereum_apis:
        try:
            response = requests.get(url, timeout=10)
            results[name] = response.json()
        except:
            results[name] = "Ошибка"
    display_results(results, f"Ethereum Analysis {target}")

elif choice == "27":
    target = console.input("[bold yellow]Введите ИНН для налоговой проверки: [/bold yellow]")
    tax_apis = [
        ("Налоговая РФ", f"https://service.nalog.ru/inn.do?inn={target}"),
        ("Checko", f"https://api.checko.ru/v2/company?inn={target}"),
        ("Focus", f"https://focus-api.kontur.ru/api3/req?inn={target}")
    ]
    results = {}
    for name, url in tax_apis:
        results[name] = f"Налоговая проверка: {url}"
    display_results(results, f"Tax Check {target}")

elif choice == "28":
    target = console.input("[bold yellow]Введите ФИО для поиска судебных дел: [/bold yellow]")
    court_apis = [
        ("Судебные дела", f"https://sudrf.ru/index.php?id=300&act=go_search&searchtype=fs&court_subj=0&fio={target}"),
        ("Правосудие", f"https://bsr.sudrf.ru/bigs/portal.html?name=Search&fio={target}"),
        ("СудАкт", f"https://sudact.ru/search/?q={target}")
    ]
    results = {}
    for name, url in court_apis:
        results[name] = f"Поиск судебных дел: {url}"
    display_results(results, f"Court Cases {target}")

elif choice == "29":
    target = console.input("[bold yellow]Введите название для патентного поиска: [/bold yellow]")
    patent_apis = [
        ("ФИПС", f"https://www1.fips.ru/iiss/search.xhtml?q={target}"),
        ("Google Patents", f"https://patents.google.com/?q={target}"),
        ("USPTO",
         f"https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1={target}")
    ]
    results = {}
    for name, url in patent_apis:
        results[name] = f"Патентный поиск: {url}"
    display_results(results, f"Patent Search {target}")

elif choice == "30":
    target = console.input("[bold yellow]Введите название для поиска товарных знаков: [/bold yellow]")
    trademark_apis = [
        ("Роспатент", f"https://new.fips.ru/registers-web/action?acName=searchTrademark&query={target}"),
        ("WIPO", f"https://www3.wipo.int/branddb/en/?q={target}"),
        ("EUIPO", f"https://euipo.europa.eu/eSearch/#basic/1+1+1+1/{target}")
    ]
    results = {}
    for name, url in trademark_apis:
        results[name] = f"Поиск товарных знаков: {url}"
    display_results(results, f"Trademark Search {target}")
elif choice == "31":
    target = console.input("[bold yellow]Введите номер рейса или маршрут: [/bold yellow]")
    flight_apis = [
        ("FlightRadar24", f"https://www.flightradar24.com/data/flights/{target}"),
        ("FlightStats", f"https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/{target}"),
        ("AviationStack", f"https://api.aviationstack.com/v1/flights?access_key=YOUR_KEY&flight_number={target}")
    ]
    results = {}
    for name, url in flight_apis:
        results[name] = f"Информация о рейсе: {url}"
    display_results(results, f"Flight Search {target}")

elif choice == "32":
    target = console.input("[bold yellow]Введите номер бронирования отеля: [/bold yellow]")
    hotel_apis = [
        ("Booking.com", f"https://www.booking.com/searchresults.ru.html?ss={target}"),
        ("Hotels.com", f"https://ru.hotels.com/search.do?q-destination={target}"),
        ("Tripadvisor", f"https://www.tripadvisor.ru/Search?q={target}")
    ]
    results = {}
    for name, url in hotel_apis:
        results[name] = f"Поиск бронирования: {url}"
    display_results(results, f"Hotel Booking {target}")

elif choice == "33":
    target = console.input("[bold yellow]Введите адрес для поиска аренды: [/bold yellow]")
    rental_apis = [
        ("Avito", f"https://www.avito.ru/rossiya?q={target}"),
        ("ЦИАН", f"https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&q={target}"),
        ("Яндекс.Недвижимость", f"https://realty.yandex.ru/moskva_i_moskovskaya_oblast/snyat/kvartira/?text={target}")
    ]
    results = {}
    for name, url in rental_apis:
        results[name] = f"Поиск аренды: {url}"
    display_results(results, f"Rental Search {target}")

elif choice == "34":
    target = console.input("[bold yellow]Введите госномер автомобиля: [/bold yellow]")
    car_apis = [
        ("Автокод", f"https://avtocod.ru/proverkaavto/{target}"),
        ("ГИБДД", f"https://гибдд.рф/check/auto/?num={target}"),
        ("VIN-Info", f"https://vin-info.com/check/{target}")
    ]
    results = {}
    for name, url in car_apis:
        results[name] = f"Проверка автомобиля: {url}"
    display_results(results, f"Car Check {target}")

elif choice == "35":
    target = console.input("[bold yellow]Введите номер водительского удостоверения: [/bold yellow]")
    license_apis = [
        ("ГИБДД Проверка", f"https://гибдд.рф/check/driver/?num={target}"),
        ("Дром", f"https://www.drom.ru/vin/?w={target}"),
        ("Auto.ru", f"https://auto.ru/-/ajax/vin-check/?vin={target}")
    ]
    results = {}
    for name, url in license_apis:
        results[name] = f"Проверка прав: {url}"
    display_results(results, f"Driver License {target}")

elif choice == "36":
    target = console.input("[bold yellow]Введите серию и номер паспорта: [/bold yellow]")
    passport_apis = [
        ("МВД Проверка", f"https://мвд.рф/services/check_passport/{target}"),
        ("ФМС", f"https://фмс.рф/proverka/{target}"),
        ("Госуслуги", f"https://www.gosuslugi.ru/10050/1/form/{target}")
    ]
    results = {}
    for name, url in passport_apis:
        results[name] = f"Проверка паспорта: {url}"
    display_results(results, f"Passport Check {target}")

elif choice == "37":
    target = console.input("[bold yellow]Введите ФИО для медицинского поиска: [/bold yellow]")
    medical_apis = [
        ("ЕМИАС", f"https://emias.info/patient/{target}"),
        ("Медицинский полис", f"https://www.ffoms.gov.ru/check/{target}"),
        ("Здоровая Россия", f"https://www.takzdorovo.ru/search/{target}")
    ]
    results = {}
    for name, url in medical_apis:
        results[name] = f"Медицинский поиск: {url}"
    display_results(results, f"Medical Search {target}")

elif choice == "38":
    target = console.input("[bold yellow]Введите ФИО для образовательного поиска: [/bold yellow]")
    education_apis = [
        ("Дипломы", f"https://obrnadzor.gov.ru/services/check-diplom/{target}"),
        ("Рособрнадзор", f"https://www.edu.ru/search/{target}"),
        ("ВУЗы России", f"https://vuzopedia.ru/search/{target}")
    ]
    results = {}
    for name, url in education_apis:
        results[name] = f"Образовательный поиск: {url}"
    display_results(results, f"Education Search {target}")

elif choice == "39":
    target = console.input("[bold yellow]Введите ФИО для поиска трудового стажа: [/bold yellow]")
    work_apis = [
        ("Пенсионный фонд", f"https://pfr.gov.ru/services/work-experience/{target}"),
        ("Трудовая книжка", f"https://www.gosuslugi.ru/10050/5/form/{target}"),
        ("Роструд", f"https://www.rostrud.gov.ru/check/{target}")
    ]
    results = {}
    for name, url in work_apis:
        results[name] = f"Поиск трудового стажа: {url}"
    display_results(results, f"Work History {target}")

elif choice == "40":
    target = console.input("[bold yellow]Введите ФИО для кредитной истории: [/bold yellow]")
    credit_apis = [
        ("БКИ", f"https://www.bki.ru/services/check/{target}"),
        ("НБКИ", f"https://www.nbki.ru/services/credit-history/{target}"),
        ("Центробанк", f"https://cbr.ru/credit/{target}")
    ]
    results = {}
    for name, url in credit_apis:
        results[name] = f"Кредитная история: {url}"
    display_results(results, f"Credit History {target}")
elif choice == "41":
    target = console.input("[bold yellow]Введите адрес для поиска недвижимости: [/bold yellow]")
    realty_apis = [
        ("Росреестр", f"https://rosreestr.gov.ru/wps/portal/p/cc_ib_portal_services/online_request/{target}"),
        ("Яндекс.Недвижимость", f"https://realty.yandex.ru/moskva_i_moskovskaya_oblast/kupit/kvartira/?text={target}"),
        ("ЦИАН", f"https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&q={target}")
    ]
    results = {}
    for name, url in realty_apis:
        results[name] = f"Поиск недвижимости: {url}"
    display_results(results, f"Real Estate {target}")

elif choice == "42":
    target = console.input("[bold yellow]Введите кадастровый номер участка: [/bold yellow]")
    land_apis = [
        ("Кадастровая карта", f"https://pkk.rosreestr.ru/api/features/1/{target}"),
        ("Росреестр Земля", f"https://rosreestr.gov.ru/wps/portal/online_request_land/{target}"),
        ("Геопортал", f"https://geoportal.ru/search/{target}")
    ]
    results = {}
    for name, url in land_apis:
        results[name] = f"Поиск земельного участка: {url}"
    display_results(results, f"Land Plot {target}")

elif choice == "43":
    target = console.input("[bold yellow]Введите ИНН или название компании: [/bold yellow]")
    corporate_apis = [
        ("ФНС", f"https://egrul.nalog.ru/search/{target}"),
        ("СПАРК", f"https://spark-interfax.ru/search/{target}"),
        ("Контур.Фокус", f"https://focus.kontur.ru/search/{target}")
    ]
    results = {}
    for name, url in corporate_apis:
        results[name] = f"Корпоративный поиск: {url}"
    display_results(results, f"Corporate Search {target}")

elif choice == "44":
    target = console.input("[bold yellow]Введите IMO или название судна: [/bold yellow]")
    marine_apis = [
        ("MarineTraffic", f"https://www.marinetraffic.com/ru/ais/details/ships/imo:{target}"),
        ("FleetMon", f"https://www.fleetmon.com/vessels/{target}"),
        ("VesselFinder", f"https://www.vesselfinder.com/vessels/{target}")
    ]
    results = {}
    for name, url in marine_apis:
        results[name] = f"Поиск морского судна: {url}"
    display_results(results, f"Marine Vessel {target}")

elif choice == "45":
    target = console.input("[bold yellow]Введите регистрационный номер ВС: [/bold yellow]")
    aircraft_apis = [
        ("FlightAware", f"https://flightaware.com/live/flight/{target}"),
        ("FlightRadar24", f"https://www.flightradar24.com/data/aircraft/{target}"),
        ("Planefinder", f"https://planefinder.net/flight/{target}")
    ]
    results = {}
    for name, url in aircraft_apis:
        results[name] = f"Поиск воздушного судна: {url}"
    display_results(results, f"Aircraft Search {target}")

else:
    console.print("[bold red]Неверный выбор![/bold red]")

console.print("\n[bold green]     Поиск завершен![/bold green]")

# Предложение продолжить работу
continue_search = console.input("\n[bold yellow]Хотите выполнить еще один поиск? (да/нет): [/bold yellow]")
if continue_search.lower() in ['да', 'д', 'yes', 'y', '',]:
    # Перезапуск меню
    console.clear()
    console.print(Panel.fit(banner, style="bold blue"))
    create_menu()

    choice = console.input("\n[bold red]Выберите: [/bold red]")

    if choice == "1":
        target = console.input("[bold yellow]Введите IP адрес: [/bold yellow]")
        results = search_ip(target)
        display_results(results, f"IP {target}")

    elif choice == "2":
        target = console.input("[bold yellow]Введите номер телефона: [/bold yellow]")
        results = search_phone(target)
        display_results(results, f"Телефон {target}")

    elif choice == "5":
        target = console.input("[bold yellow]Введите запрос для Яндекс: [/bold yellow]")
        results = yandex_search(target)
        for result in results:
            console.print(Panel.fit(f"[yellow]Название:[/yellow] {result['Название']}\n"
                                    f"[green]Описание:[/green] {result['Описание']}\n"
                                    f"[blue]Ссылка:[/blue] {result['Ссылка']}"))
    else:
        console.print("[bold red][/bold red]")

else:
    console.print("\n[bold red]Завершение работы Prosto Finiki...[/bold red]")
    console.print("[bold blue]До свидания! @Fell1ksx | @FreeBestSoft[/bold blue]")

# Финальное сообщение
console.print("\n" + "=" * 60)
console.print("[bold magenta]         - Поиск завершен[/bold magenta]")
console.print("[bold cyan]45 ахуенных модулей | Реальное время [/bold cyan]")
console.print("=" * 60)