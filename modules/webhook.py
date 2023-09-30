# Importing Packages

import os
from os import system
from plugins.common import *

try:
    from dhooks import Webhook
except:
    os.system("py -m pip install dhooks")
    from dhooks import Webhook
try:
    from colorama import Fore, Style
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, Style


# Making a variable to count the amount of messages sent
sent = 0


# Getting the user to input the target webhook
print(banner)
print(Fore.LIGHTCYAN_EX + "Please input the webhook: " + Fore.RESET)
Webhook1 = input()


# Defining the webhook
hook = Webhook(Webhook1)
hook.get_info()
os.system("cls")


# Defining the first option which is the spamming module
def spam(sent):
    system("title Spamming Mode")
    print(Fore.LIGHTCYAN_EX + "Enter the message you would like to spam." + Fore.RESET)
    messageToSpam = input()
    os.system("cls")
    system("title Close the window in order to stop the spam.")
    hook.modify(name="Swift Spammer ONTOP")

    while True:
        hook.send(f"{messageToSpam}")
        sent = sent + 1
        print(Style.BRIGHT + Fore.GREEN + "Total messages sent:", sent)


# Defining the second option which is the deleting module
def delete():
    system("title Delete Mode")
    hook.send("This webhook is self destructing.")
    hook.delete()
    print(Style.BRIGHT + Fore.RED + "Successfully deleted the webhook!" + Fore.RESET)


def info():
    system("title Information Mode")
    # print(Fore.LIGHTCYAN_EX)
    print(Fore.LIGHTCYAN_EX + f"\nGUILD ID: {hook.guild_id}")
    print(f"CHANNEL ID: {hook.channel_id}")
    print(f"USERNAME: {hook.default_name}")
    print(f"PFP: {hook.default_avatar_url}\n\n")
