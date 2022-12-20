import requests
from colorama import Fore

def subli(x,y):
    print(Fore.CYAN,'\n*********Scanning Started********\n',Fore.GREEN)
    for item in y:
        url = f"https://{item}.{x}"
        try:
            print(Fore.YELLOW,url,Fore.GREEN)
            requests.get(url,timeout=10)
            print(Fore.RED +'[Working]-->',Fore.RESET,f'{url}',Fore.GREEN)
        except requests.ConnectionError:
            pass
    print(Fore.CYAN,'\n********Scanning Finished********',Fore.GREEN)
    return"""
    \nThanks for using this basic Python Subdomain and VHOST scanner.
    
    For more fine results refer to:\n
    https://github.com/OWASP/Amass
    https://github.com/aboul3la/Sublist3r   
    """
with open('Note.txt','r') as file2:
    var3 = file2.read()
print(Fore.GREEN,f'\n{var3}')

if __name__ == '__main__':

    var2 = input(Fore.CYAN+'Enter your target: ')
    
    path = input(Fore.BLUE + 'Enter File Path: ' + Fore.RESET)
    with open(f'{path}', 'r') as file:
        var = file.read()
        sub_dom = var.splitlines()
    print(subli(var2, sub_dom))
