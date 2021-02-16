import time
import sys
import socket
from datetime import datetime
import os
import hashlib
import requests
import re
import whois

def m():
	menu = input('''
---------------------------------------------
Hello friend, escolha uma das opçoes abaixo
---------------------------------------------
---------------------------------------------
| [1]Portscanner ==> Python                 |
| [2]Hash cracker ==> Python                |
| [3]Brute force diretórios ==> Python      |
| [4]Brute force subdomínios ==> Python     |
| [5]Banner grabbing ==> Python             |                    
| [6]Localizar IP ==> Python                |
| [7]Brute force em ftp ==> Python          |
| [8]Whois ==> Python                       |
| [9]Proucurar exploits ==> Python          |                   
| [!]Avisos                                 |
| [0]Sair do progama                        |
---------------------------------------------
[ψ]Sua opção ==> ''')
	 
	if menu == '0':
		print('[-]Você escolheu sair do progama')
		sair()

	elif menu == '1':
		print('[-]Você escolheu usar o Portscanner')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		portscanner()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '2':
		print('[-]Você escolheu usar o hash cracker')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		hashcracker()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '3':
		print('[-]Você escolheu usar o brute force em diretórios')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		bfdir()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '4':
		print('[-]Você escolheu usar o brute force em subdomínios')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		sub()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '5':
		print('[-]Você escolheu usar o banner grabbing')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		bg()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '6':
		print('[-]Você escolheu usar o localizador de ip')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		localip()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '7':
		print('[-]Você escolheu usar o brute force em ftp')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		ftp()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '8':
		print('[-]Você escolheu usar o whois')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		w()
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '9':
		print('[-]Você escolheu usar o buscador de exploits')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		e()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		m()

	elif menu == '!':
		print('[-]Todas essas ferramentas foram progamadas em python')
		time.sleep(1.4)
		print('[-]Não me resposabilizo por nenhuma atitude')
		time.sleep(1.4)
		print('[-]Não use para fins ilegais!')
		print('\n')
		print('[-]Voltando pro menu...')
		m()

def sair():
	print('Quer mesmo sair?')
	time.sleep(1.45)
	print('Não me deixe...')
	time.sleep(1)
	print('Até mais...')
	sys.exit(1)

def portscanner():
	now = datetime.now()
	x = now.hour
	y = now.minute

	print('''
   ████▀░░░░░░░░░░░░░░░░░▀████
   ███│░░░░░░░░░░░░░░░░░░░│███
   ██▌│░░░░░░░░░░░░░░░░░░░│▐██
   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██       --------------------------- 
   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██            [-]SharKScanner[-]
   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██       --------------------------
   ██▌░│██████▌░░░▐██████│░▐██  
   ███░│▐███▀▀░░▄░░▀▀███▌│░███
   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
   ████▄─┘██▌░░░░░░░▐██└─▄████
   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
   ███████▄░░░░░░░░░░░▄███████
	''')
	ip = input('[-]IP alvo ==> ')
	print('---------------------------------------------')
	print('[-]Realizando varredura em ==>', ip)
	print('[-]Scan inicializado às:',x,':',y)
	print('---------------------------------------------')
	time.sleep(2)
	print('================SharkScanner================')

	for porta in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s1 = s.connect_ex((ip, porta))
		if s1 == 0:
			b = print('[>]Porta aberta ===>', porta)
			s.close()

	time.sleep(2.5)
	print('============================================')
	print('[+]Scan finalizado')

def hashcracker():
	time.sleep(2)
	print('''
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"               [+]SharKHash[+]
        $$$u       u$u       u$$$           O melhor hash cracker da historia
        $$$u      u$$$u      u$$$                progamado por sharkroot  
         "$$$$uu$$$   $$$uu$$$$"               github: github.com/wirecalvo
          "$$$$$$$"   "$$$$$$$"       Quebramos md5, sha1, sha256, sha224, sha384 e sha512!
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"


	''')
	print('=======================================================================================================')
	time.sleep(2)
	th = input('Tipo de hash => ')
	h = input("Hash => ")
	time.sleep(1)
	wl = input("Wordlist => ")
	time.sleep(2)
	os.system(['clear', 'cls'][os.name == 'nt'])
	print('Agora deixe o trabalho duro com agente')
	time.sleep(1.5)
	print('''
███████╗    ██╗  ██╗     █████╗     ██████╗     ██╗  ██╗            ██╗  ██╗     █████╗     ███████╗    ██╗  ██╗
██╔════╝    ██║  ██║    ██╔══██╗    ██╔══██╗    ██║ ██╔╝            ██║  ██║    ██╔══██╗    ██╔════╝    ██║  ██║
███████╗    ███████║    ███████║    ██████╔╝    █████╔╝             ███████║    ███████║    ███████╗    ███████║
╚════██║    ██╔══██║    ██╔══██║    ██╔══██╗    ██╔═██╗             ██╔══██║    ██╔══██║    ╚════██║    ██╔══██║
███████║    ██║  ██║    ██║  ██║    ██║  ██║    ██║  ██╗            ██║  ██║    ██║  ██║    ███████║    ██║  ██║
╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝            ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚══════╝    ╚═╝  ╚═╝
                                                                                                                
	''')
	if th == "md5":
		hashtype = hashlib.md5
	elif th == "sha1":
		hashtype = hashlib.sha1
	elif th == "sha224":
		hashtype = hashlib.sha224
	elif th == "sha256":
		hashtype = hashlib.sha256
	elif th == "sha384":
		hashtype = hashlib.sha384
	elif th == "sha512":
		hashtype = hashlib.sha512

	print('Aceita uma fanta laranja?')

	for palavra in wl:
		hc = hashtype(palavra.strip().encode('utf-8')).hexdigest()
		st = time.time()
		time.sleep(2)
		print("Testando senha ->", palavra)
		time.sleep(2)
		if h == hc:
			print('Senha quebrada:', palavra)
			exit()
		else:
			print('Não achamos a senha, tente uma wordlist melhor')

def bfdir():
	print('''
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(                      
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.                         [+]Brute force em diretórios[+]
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb                             [+]Feito por SHARK[+]
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
	''')

	time.sleep(1.5)
	url = input('[-]Domínio alvo ==> ')
	time.sleep(2)
	wl = input('[-]Wordlist ==> ')
	time.sleep(2)
	file = open(wl, "r")
	ver = file.read()
	ve = ver.splitlines()

	print('\n')
	print('[+]Proucurando por diretórios em -->', url)
	time.sleep(2.75)

	for diretorio in ve:
        	link = f"http://{url}/{diretorio}"
        	r = requests.get(link)
        	if r.status_code == 200:
                	print('[-]', link, '==> 200')
        	else:
                	print('[-]', link, '==> 404 ou 403')


def sub():
	print('''
          _,.-----.,_
       ,-~           ~-.
      ,^___           ___^.
    /~"   ~"   .   "~   
   Y  ,--._    I    _.--.  
    | Y     ~-. | ,-~     Y |                [+]SuBBrute[+]
    | |        }:{        | |    [+]Brute force em subdomínios feito port sharkroot[+]
    j l       / | \       ! l
 .-~  (__,.--" .^. "--.,__)  ~-.
(           / / | \ \           )
 \.____,   ~  \/"\/  ~   .____,/
  ^.____                 ____.^
     | |T ~\  !   !  /~ T| |
     | |l   _ _ _ _ _   !| |
     | l \/V V V V V V\/ j |
     l  \ \|_|_|_|_|_|/ /  !
      \  \[T T T T T TI/  /
       \  `^-^-^-^-^-^'  /
        \               /
         \.           ,/
           "^-.___,-^"


	''')
	time.sleep(1.5)

	dom = input( "\033[35mDomínio alvo => ")
	time.sleep(0.4)
	wl = input( "Wordlist => ")
	arq = open(wl, "r")
	dns = arq.read()
	subdom = dns.splitlines()
	time.sleep(2)
	print('\n')
	print('[+]Proucurando por subdomínios em -->', dom)
	time.sleep(2.75)
	print("===========================$===========================")
	time.sleep(1.5)

	for subdomain in subdom:
		if subdomain != True:
			link = f"http://{subdomain}.{dom}"

			try:
				requests.get(link)
			except requests.ConnectionError:
				pass
		else:
			print('[-]Subdomínio encontrado ===>', link)
	time.sleep(2)
	print('===========================$===========================')
	print('\n')
	print('[$]Scan Encerrado[$]')

def bg():
	ip = input('[-]IP alvo ==> ')
	porta = input('[-]Porta ==> ')
	time.sleep(1)
	print('''
 _                              _     
| |__     __ _   _ __    __ _  | |__  
| '_ \   / _` | | '__|  / _` | | '_ \ 
| |_) | | (_| | | |    | (_| | | |_) |
|_.__/   \__, | |_|     \__,_| |_.__/ 
         |___/                        
	''')
	time.sleep(1.5)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s1 = s.connect((ip, int(porta)))
	print('[-]Conectando em ==> ', ip, ':', porta)
	time.sleep(1.75)
	s2 = s.recv(1024)
	print('[-]Banner ==> ', s2)

def localip():
	print('''
                                                    
 ___  | |__     __ _   _ __  | | __ (_)  _ __  
/ __| | '_ \   / _` | | '__| | |/ / | | | '_ \ 
\__ \ | | | | | (_| | | |    |   <  | | | |_) |
|___/ |_| |_|  \__,_| |_|    |_|\_\ |_| | .__/ 
                                        |_|   
	''')

	ip = input('[-]IP alvo ==> ')
	r = request = requests.get('http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'.format(ip))
	resposta = (r.json())
	time.sleep(2)
	print('[-]Trazendo informações de ==>', ip)
	time.sleep(1.5)

	print('=======================================================================')
	print('[-]',ip)
	print('[-]País ==>  {}'.format(resposta['country']))
	print('[-]Estado ==>  {}'.format(resposta['regionName']))
	print('[-]Cidade ==>  {}'.format(resposta['city']))
	print('[-]CEP aproximado ==> {}'.format(resposta['zip']))
	print('[-]Latitude ==> {}'.format(resposta['lat']))
	print('[-]Longitude ==>  {}'.format(resposta['lon']))
	print('[-]Organização ==>  {}'.format(resposta['org']))
	print('[-]Fuso Horário ==> {}'.format(resposta['timezone']))
	print('=======================================================================')

def ftp():
	print('''
 ____    _____   _____   ____  
/ ___|  |  ___| |_   _| |  _ \ 
\___ \  | |_      | |   | |_) |                    [+]SFTP[+]
 ___) | |  _|     | |   |  __/      [-]progama para fazer brute force em ftp[-]
|____/  |_|       |_|   |_|    
	''')

	time.sleep(2)
	ip = input('[-]IP => ')
	time.sleep(1.5)
	user = input('[-]Usuário => ')
	time.sleep(1.5)
	wl = input('[-]Wordlist => ')
	time.sleep(1.5)
	file = open(wl, "r")
	fileread = file.read()
	senha = fileread.splitlines()

	for s in senha:
		print('===============================================')
		print('[+]Testando com -> ', user, '-', s)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, 21))
		s.recv(1024)
		s.send("USER"+user+"\r\n")
		s.recv(1024)
		s.send("PASS"+s+"\r\n")
		resultado = s.recv(1024)
		s.send("QUIT\r\n")

		if re.search("230", resultado):
			print('[-]Senha encontrada ===>', s)
			break
		else:
			print('[-]Senha não encontrada')
def w():
	print('''
	 
\ \      / / | | | |  / _ \  |_ _| / ___| 
 \ \ /\ / /  | |_| | | | | |  | |  \___ \ 
  \ V  V /   |  _  | | |_| |  | |   ___) |
   \_/\_/    |_| |_|  \___/  |___| |____/ 
	''')

	d = input('[-]Domínio alvo ==> ')
	c = whois.whois(d)
	time.sleep(2)
	print('[-]Trazendo informações de ==>',d)
	time.sleep(2)
	print(c.text)

def e():
	a = input('''
================================
[+]Exploits[+]

[1]CMS
[2]RootKit
[3]RCE
[4]Escalação de privilégios
[5]Wordpress
[6]FTP
[7]SSH
[8]Linux
[9]Windows
[10]Mac OS
================================
[+]Sua opção ==> ''')

	if a == '1':
		print('[-]Buscando exploits CMS...')
		time.sleep(2)
		os.system("searchsploit CMS")

	elif a == '2':
		print('[-]Buscando exploits RootKit...')
		time.sleep(2)
		os.system("searchsploit rootkit")

	elif a == '3':
		print('[-]Buscando exploits para RCE...')
		time.sleep(2)
		os.system("searchsploit remote code execution")

	elif a == '4':
		print('[-]Buscando exploits para Escalação de privilégios...')
		time.sleep(2)
		os.system("searchsploit privilege")

	elif a == '5':
		print('[-]Buscando exploits para Wordpress...')
		time.sleep(2)
		os.system("searchsploit wordpress")

	elif a == '6':
		print('[-]Buscando exploits para FTP...')
		time.sleep(2)
		os.system("searchsploit ftp")

	elif a == '7':
		print('[-]Buscando exploits para ssh...')
		time.sleep(2)
		os.system("searchsploit ssh")

	elif a == '8':
		print('[-]Buscando exploits para linux...')
		time.sleep(2)
		os.system("searchsploit linux")

	elif a == '9':
		print('[-]Buscando exploits para windows...')
		time.sleep(2)
		os.system("searchsploit windows")

	elif a == '10':
		print('[-]Buscando exploits para Mac...')
		time.sleep(2)
		os.system("searchsploit macos")


print('[-]Carregando...')
time.sleep(2)
print('''
                     .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.                                [ψ]SHARK - FRAMEWORK 2.0[ψ]
              d$L  4.         4$$$$$$$$$$$$$$                          [-]Coleção de ferramentas para pentest[-]
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$                              [>]Discord ==> eduardor 《》#3429[<]
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$                          
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            """""                              "$$$"

''')
time.sleep(2)

m()
