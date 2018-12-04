import socket
import os
import sys

class Methods():

    def __init__(self): #vc precisa de um __init__ cara, é convenção e ajuda mt
        self.filelocation = '' #file that user will input
        self.file = ''
        self.host = ''
        self.subdomains = ["ns1", "ns2", "www", "ftp", "admin", "intranet", "ww2"] # melhor vc criar uma wordlist ou baixar na internet para ficar mais completo(apague esse comentário)
        self.subdomainwordlist = ''
        self.subdomainwordlistfile = ''
        self.choose = ''

    def welcome(self):
        print('\n'
              '        ████▀░░░░░░░░░░░░░░░░░▀████ \n'
              '        ███│░░==========================░░│███ \n'
              '        ██▌│░░PROGRAM DEVELOPED BY KAYAN░░│███ \n'
              '        ██░└┐░==========================░┌┘░██ \n'
              '        ██░░└┐░░░░░░░░░░░░░░░┌┘░░██ \n'
              '        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██ \n'
              '        ██▌░│██████▌░░░▐██████│░▐██ \n'
              '        ███░│▐███▀▀░░▄░░▀▀███▌│░███ \n'
              '        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██ \n'
              '        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n'
              '        ████▄─┘██▌░░░░░░░▐██└─▄████\n'
              '        █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n'
              '        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████ \n'
              '        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████ \n'
              '        ███████▄░░░░░░░░░░░▄███████\n')

        print('\n'
              '| |         /^\\/^\\      /*COBRA_FUMANTE*/\n'
              '\ |        |O__|  O|\n'
              '\\/____   /~     \_/ \\\n'
              ' \\____|__________/  \\\n'
              '        \_______      \\\n'
              '                `\\     \\                 \\\n'
              '                  |     |                  \\\n'
              '                 /      /                    \\\n'
              '                /     /                       \\\\\n'
              '              /      /                         \\ \\\n'
              '             /     /                            \\  \\\n'
              '           /     /             _----_            \\   \\\n'
              '          /     /           _-~      ~-_         |   |\n'
              '         (      (        _-~    _--_    ~-_     _/   |\n'
              '          \\      ~-____-~    _-~    ~-_    ~-_-~    /\n'
              '            ~-_           _-~          ~-_       _-~\n'
              '               ~--______-~                ~-___-~\n'
              '\n'
              '\n')

        self.choose = input('Choose the mode:\n'
                            '1 = [Default List (self.subdomains for more information)]\n'
                            '2 = [list BruteForce]\n')
        while self.choose not in ['1', '2']:
            print('no kidding me, men')
            self.choose = input('Choose the mode:\n'
                                '1 = [Default List (self.subdomains for more information)]\n'
                                '2 = [list BruteForce]\n')
        if self.choose == '1':
            self.host_function()
            self.dns_default_bruteforce()
        elif self.choose == '2':
            self.file_function()
            self.host_function()
            self.dns_bruteforce_wordlist()

    def file_function(self):
        self.filelocation = input("File name: ")
        while self.filelocation[-4:] != '.txt' or os.path.exists(self.filelocation) != True:
            print('User a valid file name')
            self.filelocation = input("File name: ")
        
    def host_function(self):
        self.host = input("Host: ")
        try:
            if self.host.replace('.', '').isdigit():
                self.host = socket.gethostbyaddr(self.host)
            else:
                if "www." in self.host:
                    self.host = self.host[4:]
                    pass
                if ".com" not in self.host:
                    self.host = self.host + ".com"
                    pass
            print(f'Host Ip: {socket.gethostbyname(self.host)}')
        except socket.herror:
            print('[!] HOST NOT FOUND ')
            sys.exit()
        except socket.gaierror:
            print('[!] HOST NOT FOUND OR CORRUPTED HOST')
            sys.exit()

    def dns_default_bruteforce(self): #troquei por item para ficar mais bonito e coloquei a lista no __init__ (apague esse comentário)
        for item in self.subdomains: 
            dns = item + "." + self.host
            try:
                print(f'{dns} : {socket.gethostbyname(dns)}') #acho que tem uma maneira mais elegante de fazer isso, amanhã vejo (apague esse comentario)
            except socket.herror:
                pass
            except socket.gaierror:
                pass
                
    def dns_bruteforce_wordlist(self):
        try:
            self.subdomainwordlistfile = open(self.filelocation, 'r')
            self.subdomainwordlist = self.subdomainwordlistfile.read().strip().split()
            for item in self.subdomainwordlist:
                dns = item + "." + self.host
                try:
                    print(f'{dns} : {socket.gethostbyname(dns)}')
                except socket.herror:
                    pass
                except socket.gaierror:
                    pass
        except FileNotFoundError:
            print('[!] FILE NOT FOUND [!]')


dnsbruteforce = Methods()
dnsbruteforce.welcome()
