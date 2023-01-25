import requests
import sys
import argparse
from colorama import Fore
import threading
import pyfiglet
banner = pyfiglet.figlet_format("Subli")
print(banner)

def subli(x, y):
    with open('readme.md','r') as file:
        var = file.read()
        print(var)
    print(Fore.CYAN, '\n*********Scanning Started********\n', Fore.GREEN)
    for item in y:
        url = f"https://{item}.{x}"
        try:
            print(Fore.YELLOW, url, Fore.GREEN)
            requests.get(url, timeout=10)
            print(Fore.RED + '[Working]-->', Fore.RESET, f'{url}', Fore.GREEN)
        except requests.ConnectionError:
            pass
        except requests.exceptions.InvalidURL:
            pass
        except KeyboardInterrupt as e:
            e = '\n KeyBoard Interrupt Detected Exiting...'
            print(e)
            sys.exit()
    print(Fore.CYAN, '\n********Scanning Finished********', Fore.GREEN)

parser=argparse.ArgumentParser(
    usage= '''subli.py -d example.com -f /path/to/file.txt''',
    description='''Subli a Subdomain Bruteforcer for beginners''',
    epilog="""Developer: @instagram.com/thecyberjerry""")
parser.add_argument('-d', '--domain', required=True, help='-d example.com')
parser.add_argument('-f', '--file', required=True, help='-f /path/to/file/file.txt')
args = parser.parse_args()
Target = vars(args)
with open(Target.get('file'), 'r') as file:
    var2 = file.read()
    x = var2.splitlines()
threading = threading.Thread(target=subli(Target.get('domain'),x))
threading.start()
