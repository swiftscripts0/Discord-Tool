from colorama import Fore
import random
import requests
from time import sleep


heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

def CheckToken(token):
    url = 'https://discord.com/api/v9/users/@me'
    response = requests.get(url, headers=getheaders(token))
    if response.status_code == 200:
        print(f"{Fore.GREEN} <*> Valid Token.")
    else:
        print(f"\n{Fore.RED} <!> Invalid Token.")
        sleep(1)
        __import__("Xvirus").main()

main_banner = (
    Fore.LIGHTCYAN_EX
    + """
 _    _      _     _                 _      _____           _ 
| |  | |    | |   | |               | |    |_   _|         | |
| |  | | ___| |__ | |__   ___   ___ | | __   | | ___   ___ | |
| |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /   | |/ _ \ / _ \| |
\  /\  /  __/ |_) | | | | (_) | (_) |   <    | | (_) | (_) | |
 \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\   \_/\___/ \___/|_|

0. Spam webhook
1. Delete Webhook
2. Webhook Information
3. Token Stuff
"""
)


token_banner = (
    Fore.LIGHTCYAN_EX
    + """
 _    _      _     _                 _      _____           _ 
| |  | |    | |   | |               | |    |_   _|         | |
| |  | | ___| |__ | |__   ___   ___ | | __   | | ___   ___ | |
| |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /   | |/ _ \ / _ \| |
\  /\  /  __/ |_) | | | | (_) | (_) |   <    | | (_) | (_) | |
 \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\   \_/\___/ \___/|_|

0. Token Login
1. Token Information
"""
)


banner = (
    Fore.LIGHTCYAN_EX
    + """
 _    _      _     _                 _      _____           _ 
| |  | |    | |   | |               | |    |_   _|         | |
| |  | | ___| |__ | |__   ___   ___ | | __   | | ___   ___ | |
| |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /   | |/ _ \ / _ \| |
\  /\  /  __/ |_) | | | | (_) | (_) |   <    | | (_) | (_) | |
 \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\   \_/\___/ \___/|_|

"""
)


tokeninfotitle = (
    Fore.LIGHTCYAN_EX
    + """
                        ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██╗███╗   ██╗███████╗ ██████╗ 
                        ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██║████╗  ██║██╔════╝██╔═══██╗
                           ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██║██╔██╗ ██║█████╗  ██║   ██║
                           ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██║██║╚██╗██║██╔══╝  ██║   ██║
                           ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║██║██║ ╚████║██║     ╚██████╔╝
                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ \n
"""
)


def ENTR():
    input(Fore.LIGHTCYAN_EX + "Press Enter To Continue: ")
