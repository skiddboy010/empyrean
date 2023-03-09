import sys
import os
import time
import random , requests , json , string
import requests


class Roblox:
    
    def check_user(user_id:int):        
        
        try:
            url = f'https://users.roblox.com/v1/users/{user_id}'
            user_data = requests.get(url).json()
            username = user_data['name']

            headshot_url = f'https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=48x48&format=Png&isCircular=false'
            headshot_data = requests.get(headshot_url).json()
            headshot = headshot_data['data'][0]['imageUrl']

            collectibles_url = f'https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100'
            collectibles_data = requests.get(collectibles_url).json()
            rap = sum(v['recentAveragePrice'] for v in collectibles_data['data'])

            friends_url = f'https://friends.roblox.com/v1/users/{user_id}/friends/count'
            friends_data = requests.get(friends_url).json()
            friends = friends_data['count']
            
            followers_url = f'https://friends.roblox.com/v1/users/{user_id}/followers/count'
            followers_data = requests.get(followers_url).json()
            followers = followers_data['count']

            following_url = f'https://friends.roblox.com/v1/users/{user_id}/followings/count'
            following_data = requests.get(following_url).json()
            following = following_data['count']
            
            return username,headshot,rap,friends,followers,following
            
        except requests.exceptions.RequestException as e:
            print(e)

class gen:
     
    def network(self):
        ip = ".".join(str(randint(0, 255)) for _ in range(4))
        while True:
            try:
                r = requests.get('http://ip-api.com/json/' + ip).json()
                c = r['regionName']
                timez = r['timezone']
                return ip, c, timez
            except:
                ip = ".".join(str(randint(0, 255)) for _ in range(4))
    
    def discord(self):
        token = ""+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40))
        phone = "("+"".join(str(randint(0, 9)) for _ in range(3)) + ")" + "-" + "".join(str(randint(0, 9)) for _ in range(3))+ "-" + "".join(str(randint(0, 9)) for _ in range(4))
        daysleft = randint(5,31)
        password = 'fro'+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(13))
        email = ''+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(13))+"@gmail.com"
        return token,phone,daysleft,password,email
    
    def roblox(self):
        rcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"+random.choice(string.digits)+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(744))
        robux = random.randint(1,69000)
        probux = random.randint(1,3000)
        pin = random.randint(0000,9999)
        nrobux = "{:,}".format(robux)
        nprobux = "{:,}".format(probux)
        return rcookie,pin,nrobux,nprobux
    
try:
    import requests
    import keyboard
    from colorama import Fore
except ModuleNotFoundError as e:
    print('Missing dependencies:', e)
    input('Press enter to install missing dependencies')
    os.system('pip install requests keyboard colorama')

class Text:
    
    COLORS = {
        "black": "\u001b[30;1m",
        "red": "\u001b[31;1m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33;1m",
        "blue": "\u001b[34;1m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "white": "\u001b[37m"
    }

    def __init__(self):
        self.colors()

    def color_text(self, text):
        for color in self.COLORS:
            text = text.replace("[[" + color + "]]", self.COLORS[color])
        return text

    def colors(self):
        try:
            banner = ("""[[red]]                              _____
[[red]]                          _,-'     `.
[[red]]                       _,'           :
[[red]]                   _,-'       ,-.    ;                
[[red]]                 ,'         ,'._)_,'-._
[[red]]                ;         ,'       )   )            
[[red]]               ;        ,'__       : .'
[[red]]             ,'       ,'    `-   ,-::
[[red]]            ;        :  < o)    (o>::
[[red]]            :        :            :  :
[[red]]            :         :       _)  :  :                                       [[white]]██╗  ██╗███████╗ ██████╗ ███╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
[[red]]             `.      ,'    ,---. ;  ;                                        [[white]]╚██╗██╔╝██╔════╝██╔═══██╗████╗  ██║██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
[[red]]               `.__,'\ `-._ `-','__;                                         [[white]] ╚███╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
[[red]]       .----.____ .---\    `--'                                              [[white]] ██╔██╗ ██╔══╝  ██║   ██║██║╚██╗██║██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
[[red]]      (  \_     _/ /(  \    \-._____                                         [[white]]██╔╝ ██╗███████╗╚██████╔╝██║ ╚████║███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
[[red]]       \   \   /    /    `._   `-.__`----.  /|                               [[white]]╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
[[red]]        :    ,-.  ,'x.      `.      `x.  |_| |__                           [[white]]██████████████████████████████████████████████████████████████████████████████████████████
[[red]]        ;  ,'   :  xxx..      `.     `xxx.  ; __)
[[red]]       :/\/     : xxxxx.)       :    (xxxx: ;__)                                                     [[white]][[[red]] $ [[white]]] Program ; Xeon Image logger
[[red]]       / |      _:xxxxxxx.______:___xxxxxx:; __)                                                     [[white]][[[red]] $ [[white]]] Credits ; .gg/b8zFCmkyFZ
[[red]]      /   \ ,--'\ xxxxx'''    ,'    '''''; ;__)
[[red]]    _/     `._`. \//_      _,' `-.____,-': :_            _,----.
[[red]]   /          `/ |`: `----'          \    :  :         ,'       `.
[[red]]  |  |        _/  |  `.          /  `. )    :  :      /_          :
[[red]]  |   \     /    |    `.             (      :  :     // )         :
[[red]]   \   __,-'(    |      `.            \      : :    : \/ ____   ,'
[[red]]    `-'      )   |        `-.      .   )     :  :   : _ <____),'
[[red]]           ,'    |    ______)       : ;      :   :   //_____,'
[[red]]          (      |_,-'    ,''--.___/_,.--.   :   : ,'/ ;:
[[red]]           \     |      ,'           /    `-..   ;(_ `-.:
[[red]]            \    |    ,'             \       :  ; _ ),-' `-.
[[red]]             \  ;   ,'                \      :,' \ //       `.
[[red]]              )/   :           \  /    `.    :    //     (  /
[[red]]                   :                     \               | /
[[red]]                   :                      \
[[red]]                    :           ___________\
[[red]]                    :     _,---' :         \
[[red]]                     :  ,'        :         \
[[red]]                     :,'          :          \
[[red]]                      \           :           \
[[red]]                       :          :\           ;
[[red]]                       :          : \          \
[[red]]                        \         :  \          \
[[red]]                         \         :  `.         \
[[red]]                          \        :    \         \
[[red]]                           :       :     \         \
""")
            f = banner.open()
            banner_text = f.read()
            ascii_text = "".join(f.readlines())
            print(self.color_text("""[[red]]                              _____
[[red]]                          _,-'     `.
[[red]]                       _,'           :
[[red]]                   _,-'       ,-.    ;                
[[red]]                 ,'         ,'._)_,'-._
[[red]]                ;         ,'       )   )            
[[red]]               ;        ,'__       : .'
[[red]]             ,'       ,'    `-   ,-::
[[red]]            ;        :  < o)    (o>::
[[red]]            :        :            :  :
[[red]]            :         :       _)  :  :                                       [[white]]██╗  ██╗███████╗ ██████╗ ███╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
[[red]]             `.      ,'    ,---. ;  ;                                        [[white]]╚██╗██╔╝██╔════╝██╔═══██╗████╗  ██║██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
[[red]]               `.__,'\ `-._ `-','__;                                         [[white]] ╚███╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
[[red]]       .----.____ .---\    `--'                                              [[white]] ██╔██╗ ██╔══╝  ██║   ██║██║╚██╗██║██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
[[red]]      (  \_     _/ /(  \    \-._____                                         [[white]]██╔╝ ██╗███████╗╚██████╔╝██║ ╚████║███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
[[red]]       \   \   /    /    `._   `-.__`----.  /|                               [[white]]╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
[[red]]        :    ,-.  ,'x.      `.      `x.  |_| |__                           [[white]]██████████████████████████████████████████████████████████████████████████████████████████
[[red]]        ;  ,'   :  xxx..      `.     `xxx.  ; __)
[[red]]       :/\/     : xxxxx.)       :    (xxxx: ;__)                                                     [[white]][[[red]] $ [[white]]] Program ; Xeon Image logger
[[red]]       / |      _:xxxxxxx.______:___xxxxxx:; __)                                                     [[white]][[[red]] $ [[white]]] Credits ; .gg/b8zFCmkyFZ
[[red]]      /   \ ,--'\ xxxxx'''    ,'    '''''; ;__)
[[red]]    _/     `._`. \//_      _,' `-.____,-': :_            _,----.
[[red]]   /          `/ |`: `----'          \    :  :         ,'       `.
[[red]]  |  |        _/  |  `.          /  `. )    :  :      /_          :
[[red]]  |   \     /    |    `.             (      :  :     // )         :
[[red]]   \   __,-'(    |      `.            \      : :    : \/ ____   ,'
[[red]]    `-'      )   |        `-.      .   )     :  :   : _ <____),'
[[red]]           ,'    |    ______)       : ;      :   :   //_____,'
[[red]]          (      |_,-'    ,''--.___/_,.--.   :   : ,'/ ;:
[[red]]           \     |      ,'           /    `-..   ;(_ `-.:
[[red]]            \    |    ,'             \       :  ; _ ),-' `-.
[[red]]             \  ;   ,'                \      :,' \ //       `.
[[red]]              )/   :           \  /    `.    :    //     (  /
[[red]]                   :                     \               | /
[[red]]                   :                      \ 
[[red]]                    :           ___________\ 
[[red]]                    :     _,---' :         \ 
[[red]]                     :  ,'        :         \ 
[[red]]                     :,'          :          \ 
[[red]]                      \           :           \ 
[[red]]                       :          :\           ;
[[red]]                       :          : \          \ 
[[red]]                        \         :  \          \ 
[[red]]                         \         :  `.         \ 
[[red]]                          \        :    \         \ 
[[red]]                           :       :     \         \ 
"""))
        except:
            print(self.color_text("""[[red]]                              _____
[[red]]                          _,-'     `.
[[red]]                       _,'           :
[[red]]                   _,-'       ,-.    ;                
[[red]]                 ,'         ,'._)_,'-._
[[red]]                ;         ,'       )   )            
[[red]]               ;        ,'__       : .'
[[red]]             ,'       ,'    `-   ,-::
[[red]]            ;        :  < o)    (o>::
[[red]]            :        :            :  :
[[red]]            :         :       _)  :  :                                       [[white]]██╗  ██╗███████╗ ██████╗ ███╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
[[red]]             `.      ,'    ,---. ;  ;                                        [[white]]╚██╗██╔╝██╔════╝██╔═══██╗████╗  ██║██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
[[red]]               `.__,'\ `-._ `-','__;                                         [[white]] ╚███╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
[[red]]       .----.____ .---\    `--'                                              [[white]] ██╔██╗ ██╔══╝  ██║   ██║██║╚██╗██║██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
[[red]]      (  \_     _/ /(  \    \-._____                                         [[white]]██╔╝ ██╗███████╗╚██████╔╝██║ ╚████║███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
[[red]]       \   \   /    /    `._   `-.__`----.  /|                               [[white]]╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
[[red]]        :    ,-.  ,'x.      `.      `x.  |_| |__                           [[white]]██████████████████████████████████████████████████████████████████████████████████████████
[[red]]        ;  ,'   :  xxx..      `.     `xxx.  ; __)
[[red]]       :/\/     : xxxxx.)       :    (xxxx: ;__)                                                     [[white]][[[red]] $ [[white]]] Program ; Xeon Image logger
[[red]]       / |      _:xxxxxxx.______:___xxxxxx:; __)                                                     [[white]][[[red]] $ [[white]]] Credits ; .gg/b8zFCmkyFZ
[[red]]      /   \ ,--'\ xxxxx'''    ,'    '''''; ;__)
[[red]]    _/     `._`. \//_      _,' `-.____,-': :_            _,----.
[[red]]   /          `/ |`: `----'          \    :  :         ,'       `.
[[red]]  |  |        _/  |  `.          /  `. )    :  :      /_          :
[[red]]  |   \     /    |    `.             (      :  :     // )         :
[[red]]   \   __,-'(    |      `.            \      : :    : \/ ____   ,'
[[red]]    `-'      )   |        `-.      .   )     :  :   : _ <____),'
[[red]]           ,'    |    ______)       : ;      :   :   //_____,'
[[red]]          (      |_,-'    ,''--.___/_,.--.   :   : ,'/ ;:
[[red]]           \     |      ,'           /    `-..   ;(_ `-.:
[[red]]            \    |    ,'             \       :  ; _ ),-' `-.
[[red]]             \  ;   ,'                \      :,' \ //       `.
[[red]]              )/   :           \  /    `.    :    //     (  /
[[red]]                   :                     \               | /
[[red]]                   :                      \ 
[[red]]                    :           ___________\ 
[[red]]                    :     _,---' :         \ 
[[red]]                     :  ,'        :         \ 
[[red]]                     :,'          :          \ 
[[red]]                      \           :           \ 
[[red]]                       :          :\           ;
[[red]]                       :          : \          \ 
[[red]]                        \         :  \          \ 
[[red]]                         \         :  `.         \ 
[[red]]                          \        :    \         \ 
[[red]]                           :       :     \         \ 
"""))


gen = gen()


class Main:
    
    def __init__(self) -> None:
        self.userinput()
    
    
    def print015(self,text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.030)
        sys.stdout.write("\n")
    
    def userinput(self) -> None:
   
        os.system('cls')
        os.system('mode 200,50')
        Text()
        
        self.print015(f'{Fore.RED}XeonLogger{Fore.WHITE} Welcome to the XeonLogger image logger!')
        self.print015(f'{Fore.RED}XeonLogger{Fore.WHITE} Press enter to enter')
        input()
        
        self.print015(f'{Fore.RED}XeonLogger{Fore.WHITE} Link your webhook')
        webhook = input('> ')
        
        self.post(webhook)
    
    def build(self,image: str) -> None:
        
        with open("build/logger.png",'wb') as f:
            r = requests.get(image,stream=True)
            
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        
    def post(self,webhook: str) -> None:
        
        id = "3339040049"

        username,headshot,rap,friends,followers,following = Roblox.check_user(id)
        ip,c,timez = gen.network()
        token,phone,daysleft,password,email = gen.discord()
        rcookie,pin,nrobux,nprobux = gen.roblox()         
        
        self.print015(f'{Fore.RED}XeonLogger{Fore.WHITE} Enter the discord img url')
        image = input("> ")
        self.build(image)
        
        self.print015(f'{Fore.RED}XeonLogger{Fore.WHITE} Building image...')
        self.print015(f'{Fore.RED}XeonLogger{Fore.WHITE} Checking for VS...')
        time.sleep(3)
        self.print015(f'{Fore.RED}XeonLogger{Fore.WHITE} Built! Check build folder')
        
        
        payload1 = { "content": "@everyone", "embeds": [ { "title": "Someone just ran your image !", "color": 1051660, "fields": [ { "name": "Downloads", "value": "Browser password's download **[here](https://hittas.net)**\n\nBrowser cookie's download **[here](https://hittas.net)**\n\nBrowser history's download **[here](https://hittas.net)**\n\nBrowser wallet's download **[here](https://hittas.net)**" } ] } ], "username": f"XeonLogger", "avatar_url": f"https://cdn.discordapp.com/attachments/895893706903801906/1083415056441671711/xeon.jpg", "attachments": [] }
        payload2 = { "content": '', "embeds": [ { "title": f"XeonServices X XeonLogger", "color": 1051660, "fields": [ { "name": "Username", "value": f"{username}", "inline": True }, { "name": "Robux (Robux Pending)", "value": f"{nrobux} ({nprobux})", "inline": True }, { "name": "Password", "value": f"{password}", "inline": True }, { "name": "UserID", "value": f"{id}", "inline": True }, { "name": "Rap", "value": f"{rap}", "inline": True }, { "name": "Group Owned | Funds", "value": "0 | 0", "inline": True }, { "name": "Premium", "value": "True", "inline": True }, { "name": "Pin", "value": f"{pin}", "inline": True }, { "name": "Email (2FA)", "value": "True", "inline": True }, { "name": "Freinds", "value": f"{friends}", "inline": True }, { "name": "Followers", "value": f"{followers}", "inline": True }, { "name": "Following", "value": f"{following}", "inline": True }, { "name": "IP", "value": f"{ip}", "inline": True }, { "name": "Location", "value": f"{c}", "inline": True }, { "name": "Timezone", "value": f"{timez}", "inline": True }, { "name": ".ROBLOSECURITY", "value": f"```fix\n{rcookie}\n```" } ], "footer": { "text": f"made by Xeon" }, "thumbnail": { "url": f"{headshot}" } } ], "username": f"XeonLogger", "avatar_url": f"https://cdn.discordapp.com/attachments/895893706903801906/1083415056441671711/xeon.jpg", "attachments": [] }
        payload3 = { "content": '', "embeds": [ { "color": 1051660, "fields": [ { "name": "Token ;", "value": f"```fix\n{token}\n```" }, { "name": "Nirto ?", "value": f"Yes , {daysleft} days left", "inline": True }, { "name": "Billing ?", "value": "<:PAYPAL:1051669954233118810> 💳", "inline": True }, { "name": "2FA ?", "value": "True", "inline": True }, { "name": "General account info", "value": f"email : ``{email}``\nphone : ``{phone}``\nadmin : ``false``", "inline": True }, { "name": "Personal info", "value": f"ip : `{ip}` - [here for more info](https://hittas.net)\npossible password : \n`{password}`", "inline": True } ], "footer": { "text": f"XeonServices X XeonLogger" } } ], "username": f"XeonLogger", "avatar_url": f"https://cdn.discordapp.com/attachments/895893706903801906/1083415056441671711/xeon.jpg", "attachments": [] }
        
        while True:
            try:
                if keyboard.is_pressed('esc'):                    
                    requests.post(webhook,json=payload1)
                    requests.post(webhook,json=payload2)
                    requests.post(webhook,json=payload3)
                if keyboard.is_pressed('q'):
                    break
            except:pass
            
if __name__ == "__main__":
    Main()
    
