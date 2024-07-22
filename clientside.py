import os
import socket
import threading
from colorama import Fore,Style
print(Fore.LIGHTMAGENTA_EX+"""     
          へ  
        ૮ - ՛ つ  ClientSide
        /  ⁻៸      (˚ˎ 。7   
    乀 (ˍ, ل        |、˜〵  
▀▀▀▀▀▀▀▀▀▀▀▀        じしˍ,) ノ    
"""+Style.RESET_ALL)
nickname = input(Fore.LIGHTBLUE_EX+'Enter your nickname: '+Style.RESET_ALL)

host = input(Fore.LIGHTMAGENTA_EX+"server ip > "+Style.RESET_ALL)
port = input(Fore.LIGHTMAGENTA_EX+"port number > "+Style.RESET_ALL)
os.system("cls")
ask = input(Fore.LIGHTBLUE_EX+"are u sure the address are right?\n server ip : "+host+" \n port number: "+port+"\n(yes\\no) >"+Style.RESET_ALL)
if ask.lower() =="yes":
    pass
else:
    ask.lower()=="no"
    print("quit!")
    quit()

port = int(port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'nick':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('Error')
            client.close()
            break
def write():
    while True:
        print(Fore.LIGHTBLUE_EX)
        message = f'{Fore.LIGHTMAGENTA_EX+nickname+Fore.LIGHTBLUE_EX}: {input(" > ")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


