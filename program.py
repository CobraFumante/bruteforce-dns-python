import sys

from __methods__ import Methods

class Program():
    def __init__(self):
        self.method = ""
        self.methods = ["1","2","3"]
        self.host = ""
        
    def main(self):
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
              '        ███████▄░░░░░░░░░░░▄███████')
        self.method = input(" " * 9 + "> Choose which of methods do you wanna use <\n"
        "[1] Reverse-DNS\n[2] Brute DNS with list default\n[3] DNS Brute-Force with a file\n>> ")
        if self.method not in self.methods:
            print("[!] Method not found!")
            
    def run(self):
        if self.method == "1":
            dns = Methods()
            dns.host()
            dns.dnsreverse()
        elif self.method == "2":
            dns = Methods()
            dns.host()
            dns.getdnsbyhost()
        elif self.method == "3":
            dns = Methods()
            dns.hostwordlist()
            dns.file()
            dns.dnsbywordlist()
            
    def tag(self):
        while True:
            self.tag = input(r"Do you wanna continue? [s/n\n]: ") # não iria aparecer o n (apague esse comentario)
            if self.tag.lower() == "n":
                print('Bye Bye')
                sys.exit() #creio que fica mais bonito assim (apague esse comentario)
            elif self.tag.lower() == "s":
                self.main() #creio que fica mais bonito assim (apague esse comentario)
                self.run() #creio que fica mais bonito assim (apague esse comentario)
            else:
                print("Error.. We not has this option here")

program = Program()
program.main()
program.run()
program.tag()
