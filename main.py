import sys
import socket
from dns.query import tcp
from colorama import *
import colorama
from mcstatus import MinecraftServer
from cymruwhois import Client

def _input(text):
    variable = input(f"{Fore.GREEN}{text}\n[{Fore.CYAN}-{Fore.GREEN}]>{Fore.RESET} ")
    return variable

def printInformation(text):
    print(f"{Fore.GREEN}{colorama.Style.BRIGHT}\x1b[3m({Fore.CYAN}info{Fore.GREEN})\033[0m {text}")

def printError(text):
    print(f"{Fore.RED}{colorama.Style.BRIGHT}\x1b[3m({Fore.YELLOW}error{Fore.RED})\033[0m {text}")

def printCustom(text1, text2):
    print(f"{Fore.RED}{colorama.Style.BRIGHT}\x1b[3m({Fore.YELLOW}{text1}{Fore.RED})\033[0m {text2}")

printCustom("starting", "rangefinder coded by @kl3sshydra on telegram")
printCustom("starting", "sto arrubbando qualche range...\n")

def ipinfo(ip):
    
    if 'aternos.me' in LISTA[x]:
        return 'aternos'
    else:
        c=Client()
        r=c.lookup(ip)
        return 'https://ipinfo.io/AS'+r.asn+' -> '+r.owner


if len(sys.argv) != 2 or sys.argv[1] == 'help':
    printError(f'''
utilizzo:
python3 {sys.argv[0]} [opzioni]

opzioni:
- 'mclist'
- 'minecraftmp-main'
- 'minecraftmp-customurl' [customurl]

        ''')

    sys.exit()

LISTA = list()

printCustom('opzione', 'opzione selezionata: '+sys.argv[1])

try:
    import requests
except:
    printError("errore: la libreria request non è installata! esegui: \npip install requests\noppure:\npip3 install requests")
    sys.exit()

if sys.argv[1] == 'mclist':
    url = "https://mcl.ist"
    req = requests.get(url, 'html.parser')
    testo = req.text
    counter = 0
    printInformation("\nserver trovati su [https://mcl.ist]:\n")
    thing = True
    while thing:
        try:
            host = testo.split("/server/")[counter].split("span")[0].split(":")[0]
            if (counter > 2):
                print("- "+host)
                LISTA.append(host)
            counter = counter+1
        except:
            thing = False



if sys.argv[1] == 'minecraftmp-main':
    url = sys.argv[3]
    req = requests.get(url, 'html.parser')
    testo = req.text
    counter = 0
    printInformation("\nserver trovati su [https://minecraft-mp.com]:\n")
    thing = True
    while thing:
        try:
            host = testo.split("strong")[counter].split("img s")[0].split(">")[1].split("</td")[0].split("</")[0].split("\n")[0].split("#")[0]
            if (host != "" and counter > 4 and host != "<br/" and host != "204" and host != "<i class=\"fa fa-thumbs-o-up\" aria-hidden=\"true\"" and host != "Our website is made possible by displaying online advertisements to our visitors." and host != "Minecraft-mp.com" and host != "." and host != " is not affiliated with Minecraft and Mojang AB.<br/" and host != "		"):
                print("- "+host)
                LISTA.append(host)
            counter = counter+1
        except:
            thing = False


# resoconto degli ip
print("\necco a te un report di tutti gli ip trovati:\n")
for x in range(len(LISTA)):
    try:
        a = socket.gethostbyname(LISTA[x])
        print(a+' -> '+str(ipinfo(a)))
    except socket.gaierror:
        pass

print('\n! fine esecuzione\n')
sys.exit()
