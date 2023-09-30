import os
import requests
from plugins.common import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

if not os.path.exists("chromedriver.exe"):
    res = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
    ver = res.text
    download_url = (
        "https://chromedriver.storage.googleapis.com/" + ver + "/chromedriver_win32.zip"
    )
    print(
        f"[ ERROR ] Driver not found \n1. please download latest chromedriver from this link and put .exe file in this directory \n2. make sure your chrome is updated \n[{download_url} ] "
    )
    exit()


def loginTool():
    request = requests.Session()
    token = input("Enter Token > ")

    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
    }

    def tokenLogin(token):
        src = request.get(
            "https://discord.com/api/v9/users/@me", headers=headers, timeout=10
        )
        if src.status_code == 403:
            print("Token Is Invalid")
        elif src.status_code == 401:
            print("Token Is Invalid")
        else:
            service = Service(executable_path="chromedriver.exe")
            opts = webdriver.ChromeOptions()
            opts.add_experimental_option("detach", True)
            driver = webdriver.Chrome(service=service, options=opts)
            script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 2500);
                }
                """
            driver.get("https://discord.com/login")
            driver.execute_script(script + f'\nlogin("{token}")')

    option1 = input()

    if option1 == "0":
        tokenLogin(token)
    
    elif option1 == '1':
        print('This feature is coming soon...')
