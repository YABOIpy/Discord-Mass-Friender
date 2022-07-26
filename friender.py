import httpx, threading, random, os

os.system("cls||clear")
def friender(token,userid):

    count = 0
    while True:
        try:
            proxylist =  open("input/proxies.txt", "r").read().splitlines()
            proxy = random.choice(proxylist)
            proxies = {
                "http://": f"http://{proxy}",
                "https://": f"http://{proxy}",
            }
            headers = {
                "Authorization": token,
                "accept": "*/*",
                "accept-language": "en-US", 
                "connection": "keep-alive",
                "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT": "1",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "referer": "https://discord.com/channels/@me",
                "TE": "Trailers",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
    
            with httpx.Client(proxies=proxies) as client:
                while True:
                    x = client.put(f'https://discord.com/api/v9/users/@me/relationships/{userid}', headers=headers, json={}, timeout=100)
                    if x == 200:
                        count =+ 1
                        print(f"\033[32m[>] Token Friended\033[39m {count}")
                    else:
                        print("\033[31m[>] Error")
                    
                    
        except Exception as e:
            print("\033[31m[>] Something Whent Wrong")
            

        
userid = input("\033[33m[\033[39m>\033[33m] User ID\033[39m: ")
tokens = open("input/tokens.txt", "r").read().splitlines()
for token in tokens:
    threading.Thread(target=friender, args=(token, userid)).start()
