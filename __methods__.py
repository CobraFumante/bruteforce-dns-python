import socket
import dns
import re

class Methods():

    def __init__(self): #vc precisa de um __init__ cara, é convenção e ajuda mt
        self.file = '' #file that user will input
        self.host = '' #host of the target example: google.com, www.google.com, google
        self.hostw = ''
        self.subdomains = ["ns1", "ns2", "www", "ftp", "admin", "intranet", "ww2"] # melhor vc criar uma wordlist ou baixar na internet para ficar mais completo(apague esse comentário)
        self.subdomainwordlist = ''
        
    def file(self):
        self.file = input("File name: ")
        
    def host(self):
        self.host = input("Host: ")
        if "www." in self.host:
            self.host = self.host[4:]
            pass
        if ".com" not in self.host:
            self.host = self.host + ".com"
            pass
            
    def hostwordlist(self):
        self.hostw = input("Host: ")
        if self.hostw.isdigit():
            self.hostw = dnsreverse(self.host)
        else:
            pass
        
    def dnsreverse(self):
        try:
            print(socket.gethostbyaddr(self.host)) #Não seria um return aqui?, a variavel self.hostw vai fica NONE amanhã falo com vc e vejo um pouco melhor(apague esse comentario)
        except socket.herror: 
            return "[!] HOST NOT FOUND "
        except socket.gaierror:
            pass
        
    def getdnsbyhost(self): #troquei por item para ficar mais bonito e coloquei a lista no __init__ (apague esse comentário)
        for item in self.subdomains: 
            DNS = item + "." + self.host
            try:
                print(DNS + ":" + socket.gethostbyname(DNS.lower())) #acho que tem uma maneira mais elegante de fazer isso, amanhã vejo (apague esse comentario)
            except socket.gaierror:
                print(f"[!] {subdomain} NOT FOUND ")
                
    def dnsbywordlist(self):
        try:
            with open(self.file) as self.file:
                self.subdomainwordlist = self.file.readlines()
                for item in self.subdomainwordlist:
                    DNS = item.strip("\n") + "." + self.hostw
                    try: 
                        print(DNS + ":" + socket.gethostbyname(DNS))
                    except socket.gaierror:
                        print("[!] HOST NOT FOUND ")
                        exit()
                        pass
        except FileNotFoundError:
            print('[!] FILE NOT FOUND [!]')
