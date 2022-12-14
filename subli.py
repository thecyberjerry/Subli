import requests
from colorama import Fore

def subli(x,y):
    print(Fore.CYAN,'\n*********Scanning Started********\n',Fore.GREEN)
    for item in y:
        url = f"https://{item}.{x}"
        try:
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

print(Fore.GREEN,"""
******************NOTE FROM DEVELOPER  [MUST READ]******************

Please keep in mind the following points before using this Script:

1. Please use the default list.txt provided in our Github Repository or refer to:
                https://github.com/danielmiessler/SecLists
                
2. If using list other than default provided than paste the txt file in this python file directory renaming file to list.txt.

3. Please Enter the Target in the provided format. For example: google.com,bing.com,target.com

4. Last but not least it will only find subdomains available on https connection.

""")
if __name__ == '__main__':

    var2 = input('Enter your target: ')

    with open('list.txt','r') as file:
        var = file.read()
        sub_dom = var.splitlines()
    print(subli(var2, sub_dom))
