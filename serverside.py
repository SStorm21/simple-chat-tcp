import socket
import threading
import os
from colorama import Fore,Style
print(Fore.RED+"""               ▄   ▄
               █▀█▀█       
               █▄█▄█
                ███  ▄▄
                ████▐█ █
Simple tcp chat ████   █   
                ▀▀▀▀▀▀▀  
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""+Style.RESET_ALL)
host = input(Fore.GREEN+"Insert server host ip (ur machine ip) > "+Style.RESET_ALL)
port = input(Fore.GREEN+"Insert the server Port(9099/5555 etc) > "+Style.RESET_ALL)
port = int(port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

owner = input(Fore.GREEN+"start the server?(yes\\no) > "+Style.RESET_ALL)
if owner.lower() =="no":
        quit()
else :
        owner.lower() == "yes"
        os.system("cls")
        pass

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)

            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(Style.BRIGHT+f'{nickname} left the chat!'.encode('ascii')+Style.RESET_ALL)
            nicknames.remove(nickname)  
            break

def receive():
    while True:
        client, address = server.accept()
        print('Connected to ' + str(address))

        client.send('nick'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)  
        clients.append(client) 

        print(Fore.LIGHTGREEN_EX+'user nick name : ' + nickname +Style.RESET_ALL)
        broadcast(Fore.BLUE+'{nickname} Joined the chat! '+Style.RESET_ALL.encode('ascii'))
        client.send('connected!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print(Fore.YELLOW+'Server is listening...'+Style.RESET_ALL)
receive()


