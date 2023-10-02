from modules.webhook import *
from modules.tokenstuff import *

import os
import time
from os import system

sent = 0

system("title Discord Tools")


def main():
    # Printing the options available
    print(main_banner)
    option = input()
    os.system("cls") 

    # First option is the spamming module
    if option == "0":
        print(banner)
        spam(sent)

    # Second one is the deleting module
    elif option == "1":
        print(banner)
        delete()
        ENTR()
        main()

    elif option == "2":
        print(banner)
        info()
        ENTR()
        main()

    elif option == "3":
        loginTool()
        ENTR()
        main()


main()
