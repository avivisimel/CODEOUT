import sys, time, os

def typewirter(messege):
    for char in messege:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

def printsaup(what):
    if what == "doorplace":
        print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░██░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░
            """)
        if what == "hourafter":
            print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒███████▒████▒███████▒████▒███▒▒▒▒▒████▒██▒▒▒█▒▒▒▒▒
▒█▒▒▒▒▒█▒█▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒█▒█▒▒▒▒▒█▒▒█▒█▒█▒▒█▒▒▒▒▒
▒███████▒███▒▒▒▒▒█▒▒▒▒███▒▒██▒▒▒▒▒▒████▒█▒▒█▒█▒▒▒▒▒
▒█▒▒▒▒▒█▒█▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒█▒█▒▒▒▒▒█▒▒█▒█▒▒▒██▒▒▒▒▒
▒█▒▒▒▒▒█▒█▒▒▒▒▒▒▒█▒▒▒▒████▒█▒█▒▒▒▒▒█▒▒█▒█▒▒▒▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒██▒▒▒██▒▒▒█████▒▒▒██▒▒▒▒▒██▒██████▒▒▒▒▒████▒▒▒▒▒▒▒
▒██▒▒▒██▒██▒▒▒▒▒██▒██▒▒▒▒▒██▒██▒▒▒▒██▒▒▒████▒▒▒▒▒▒▒
▒██▒▒▒██▒██▒▒▒▒▒██▒██▒▒▒▒▒██▒██▒▒▒▒██▒▒▒████▒▒▒▒▒▒▒
▒███████▒██▒▒▒▒▒██▒██▒▒▒▒▒██▒██████▒▒▒▒▒████▒▒▒▒▒▒▒
▒██▒▒▒██▒██▒▒▒▒▒██▒██▒▒▒▒▒██▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒██▒▒▒██▒██▒▒▒▒▒██▒██▒▒▒▒▒██▒██▒▒██▒▒▒▒▒████▒▒▒▒▒▒▒
▒██▒▒▒██▒▒▒█████▒▒▒▒▒█████▒▒▒██▒▒▒▒██▒▒▒████▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                """)
            if what == "LetterToNumber":
                print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░███████████████████░░█░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░A=1░░░░░░░░░░░░N=14░░█░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░B=2░░░░░░░░░░░░O=15░░█░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░C=3░░░░░░░░░░░░P=16░█░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░D=4░░░░░░░░░░░░Q=17░█░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░E=5░░░░░░░░░░R=18░█░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░F=6░░░░░░░░░░S=19░   █░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░G=7░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░H=8░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░I=9▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█▒J=10▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█▒▒K=11▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█▒▒L=12▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█▒▒▒M=13▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█▒▒███████████████████▒▒█░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

                """)

clear = lambda: os.system('cls')

print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

>
""")
time.sleep(0.8)
clear()
print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░████████ ██ ░░░░░██ ██ ██ ░░░░░██ ░███ ███ ░█ ░░░░░░░░░░░░░░░░
░░██ ░░░██ ██ ░░░░░██ ██ ██ ░░░░░██ ░███ █ █ █ █ ░░░░░░░░░░░░░░░
░░██ ░░░██ ██ ░░░░░██ ██ ██ ░░░░░██ ░█ ░░██ ░█ █ ░████▒█████▒██ 
░░████████ ██ ░░░░░██ ██ ██ ░░░░░██ ░█ ░░█ █ ░█ ░░░██▒██ ██▒██ ░
░░██ ░░░██ ██ ░░░░░██ ██ ██ ░░░░░██ ░░░░░░░░░░░░░░░░▒██ ░░▒██ ░░
░░██ ░░░██ ░░██ ░██ ░░██ ░░██ ░██ ░░░██ ░██ █ █ ░░░░░░░░░░░░░░░░
░░██ ░░░██ ░░░░██ ░░░░██ ░░░░██ ░░░░░█ █ ██ █ █ ░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█ █ █ ░█ █ ░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██ ░██ ░█ ░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

>
""")
time.sleep(2)
clear()
print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░███ ███░█ ░░█ ██ ███ ██ ██ ░░░░██ ░█ █ ░█ ░░░░░░░░░░░░░░░░░░░░░
░█ █ █ █ █ ░░█ █ ░█ █ █ ░█ █ ░░░█ █░█ █ ░  ░░░░░░░░░░░░░░░░░░░░░
░███ █ █ █ ░░█ ██ ███ ██ █ █ ░░░██ ░███ ░░░░░░░░░░░░░░░░░░░░░░░░
░█ ░░█ █ █ █ █ █ ░██ ░█ ░█ █ ░░░█ █░░█ ░░░░░░░░░░░░░░░░░░░░░░░░░
░█ ░░███ ░█ █ ░██ █ █ ██ ██ ░░░░██ ░░█ ░░█ ░░░░░░░░░░░░░░░░░░░░░
░  ░░░   ░ ░ ░░░   ░ ░░░░░  ░░░░░  ░░  ░░  ░░░░░░░░░░░░░░░░░░░░░
░████████ ██  ░░░░██ ██████████ ██  ░██ ░██████  ██  ░░░░██  ░░░
░██  ░░██ ██  ░░░░██  ░░░██  ░░░██  ░██ ██    ██ ███  ░░░██  ░░░
░██  ░░██  ███  ███  ░░░░██  ░░░██  ░██ ██  ░░██ ████  ░░██  ░░░
░████████   ██████  ░░░░░██  ░░░███████ ██  ░░██ ██ ██  ░██  ░░░
░██  ░░░░░░░░░██  ░░░░░░░██  ░░░██   ██ ██  ░░██ ██  ██  ██  ░░░
░██  ░░░░░░░░░██  ░░░░░░░██  ░░░██  ░██ ██  ░░██ ██  ░██ ██  ░░░
░██  ░░░░░░░░░██  ░░░░░░░██  ░░░██  ░██  ██████  ██  ░░████  ░░░
░░   ░░░░░░░░░░   ░░░░░░░░   ░░░░   ░    ░           ░░░     ░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

>
""")
time.sleep(2)
clear()
print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░█████╗░░█████╗░██████╗░███████╗░█████╗░██╗░░░██╗████████╗░░░░░░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░░░██║╚══██╔══╝░░░░░░
██║░░╚═╝██║░░██║██║░░██║█████╗░░██║░░██║██║░░░██║░░░██║░░░░░░░░░
██║░░██╗██║░░██║██║░░██║██╔══╝░░██║░░██║██║░░░██║░░░██║░░░░░░░░░
╚█████╔╝╚█████╔╝██████╔╝███████╗╚█████╔╝╚██████╔╝░░░██║░░░░░░░░░
░╚════╝░░╚════╝░╚═════╝░╚══════╝░╚════╝░░╚═════╝░░░░╚═╝░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
Commands:░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
-start░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
-quit░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░Warning: The Game Has NO saves Mabye in the future░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")


def game():
    def say(who, what):
        print("[" + who + "]", what)

    clear()
    print("chatting with - greg")
    time.sleep(1)
    say("greg", "yo what's up?")
    time.sleep(4)
    say("you", "i'm fine.")
    time.sleep(4)
    say("greg", "i cracked a new game.")
    time.sleep(4)
    say("you", "what is it called?")
    time.sleep(4)
    say("greg", "Stuck At Uknown Place")
    time.sleep(5)
    say("you", "can you send me the crack??")
    time.sleep(4)
    say("greg", "sure")
    time.sleep(6)
    say("gerg", """
    ┏━━━━━━━━━━━━━━━━━━━━┓  
    ┃ SAUP.1.0.1.zip [↓] ┃
    ┗━━━━━━━━━━━━━━━━━━━━┛
    """)
    time.sleep(5)
    clear()
    print("""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  
    ┃ Downloading - SAUP.1.0.1.zip ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)
    time.sleep(6)
    clear()
    print("""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  
    ┃ Succssusfuly Downloaded - SAUP.1.0.1.zip [Open] ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)
    time.sleep(3)
    clear()
    print("""
    - Data [Open Folder]
    - Textures [Open Folder]
    - SeSaEngine [Open Folder]
    - SeSaAntiCrash.exe [Open]
    - SAUP.exe [Open] <        
    """)
    time.sleep(3)
    print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━┓  
        ┃ Opening... - SAUP.exe ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    clear()
    printsaup("doorplace")
    time.sleep(1)
    typewirter("""
WHAT?! WHAT IS THIS PLACE?!
HOW DID I GOT HERE?!
WHY IS THERE NO WINDOWS?! I WANNA SEE THE OUTSIDE WORLD!
I GOT SOO MANY QUESTIONS!!
AND OF COURSE,
I GONNA SAY ALL OF THEM!
AND HOW CAN WE DO THIS WITHOUT
ANSWERS THAT I TOOTALY GONNA GET!""")
    time.sleep(1)
    clear()
    printsaup("hourafter")
    time.sleep(1)
    typewirter("""
DONE!
were's my answers?
:(
I expected to get answers :(
but i didn't
WHY??
idk ask the dev of the game
let's just get out of here.
    """)
    time.sleep(1)
    clear()
    printsaup("doorplace")
    typewirter("""
alright,
let's finish this fast, here is a list of the commands that you can use:""")
    typewirter("""
1- LetterToNumber - Opens A script with letters and what they = to
2- right - look right
3- left - look left
""")

    def SaupCommand():
        command = input(">")
        if command == "LetterToNumber" or command == "right" or command == "left":
            if command == "LetterToNumber":
                printsaup("LetterToNumber")
                SaupCommand()
            if command == "right":
                printsaup("right")
                print("Enter Code:")
                code = input(">")
                if code == "PUAI":
                    print("THAT WAS THE RIGHT CODE!!!!111!")
                else:
                    print("TOO BAD, THAT WAS THE WORNG CODE")
                SaupCommand()
            if command == "left":
                printsaup("left")
                SaupCommand()
        else:
            print("Invailed Command")
    SaupCommand()

    time.sleep(10)


def command_menu():
    command_line = input(">")
    if command_line == "start":
        game()
    else:
        if command_line == "quit":
            print("Closing...")
        else:
            print("Error: Command Doesn't exist. please enter a existing command.")
            command_menu()


command_menu()
