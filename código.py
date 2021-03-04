import time
import sys
import socket
from datetime import datetime
import os
import hashlib
import requests
import re
import whois
import json

preto = "\033[1;30m"
vermelho = "\033[1;31m"
verde = "\033[1;32m"
amarelo = "\033[1;33m"
azul = "\033[1;34m"
cyan = "\033[1;36m"

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
| [7]Whois ==> Python                       |
| [8]Proucurar exploits ==> Python          |                   
| [9]Enumerar users wordpress ==> Python    |
| [!]Avisos                                 |
| [C]Contribuidores                         |
| [0]Sair do progama                        |
---------------------------------------------
shark@framework:~$ ''')
	if menu != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" and "!" and "C" and "0":
		print("[!]Escolha uma opção válida!")
		m()
	elif menu == '0':
		print('[-]Você escolheu sair do progama')
		sair()

	elif menu == '1':
		print('[-]Você escolheu usar o Portscanner')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		os.system('clear')
		portscanner()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(15)
		os.system('clear')
		m()

	elif menu == '2':
		print('[-]Você escolheu usar o hash cracker')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		os.system('clear')
		hashcracker()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(15)
		os.system('clear')
		m()

	elif menu == '3':
		print('[-]Você escolheu usar o brute force em diretórios')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		os.system('clear')
		bfdir()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(15)
		os.system('clear')
		m()

	elif menu == '4':
		print('[-]Você escolheu usar o brute force em subdomínios')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		os.system('clear')
		sub()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(15)
		os.system('clear')
		m()

	elif menu == '5':
		print('[-]Você escolheu usar o banner grabbing')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		os.system('clear')
		bg()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(15)
		os.system('clear')
		m()

	elif menu == '6':
		print('[-]Você escolheu usar o localizador de ip')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		os.system('clear')
		localip()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(15)
		os.system('clear')
		m()

	elif menu == '7':
		print('[-]Você escolheu usar o whois')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		os.system('clear')
		w()
		print('[-]Voltando pro menu...')
		time.sleep(15)
		os.system('clear')
		m()

	elif menu == '8':
		print('[-]Você escolheu usar o buscador de exploits')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(1.5)
		os.system('clear')
		e()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(15)
		os.system('clear')
		m()

	elif menu == '9':
		print('[-]Você escolheu usar o Enumerador de usuários')
		time.sleep(1)
		print('[-]Carregando...')
		time.sleep(15)
		os.system('clear')
		wd()
		print('\n')
		print('[-]Voltando pro menu...')
		time.sleep(2)
		os.system('clear')
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
	elif menu == 'C':
		print('Contribuidores com o projeto:')
		time.sleep(2)
		print('[-]Luizin   discord --> luizin#1706')
		print('[-]ChaosHunter  discord --> mateusin#6060 ')
		print('Obrigado por toda a ajuda! =)')
		print('Discord para hackers e progamadores ==> https://discord.gg/8N9VGcAK')
		print('[-]Voltando ao menu...')
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

	print(vermelho, '''
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
	print('[-]Scan inicializado às: ',x,'-',y)
	print('---------------------------------------------')
	time.sleep(2)
	print('================SharkScanner================')
	try:
		for porta in range(1, 65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s1 = s.connect_ex((ip, porta))
			if s1 == 0:
				b = print('[>]Porta aberta ===>', porta)
				s.close()

		time.sleep(2.5)
		print('============================================')
		print('[+]Scan finalizado')

	except ConnectionRefusedError:
		print("[-]Não foi possível se conectar ao servidor")

def hashcracker():
	time.sleep(2)
	print('=======================================================================================================')
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
	th = input(' [-]Tipo de hash => ')
	time.sleep(1)
	h = input(" [-]Hash => ")
	time.sleep(1)
	wl = input(" [-]Wordlist => ")
	time.sleep(2)

	try:
		wl = open(wl, "r")
	except:
		print(' [!]Arquivo não encontrado')
		time.sleep(1)
		print('Saindo do progama...')
		sys.exit(1)

	os.system(['clear', 'cls'][os.name == 'nt'])

	if th == "md5":
		hashtype=hashlib.md5
	elif th == "sha1":
		hashtype=hashlib.sha1
	elif th == "sha224":
		hashtype=hashlib.sha224
	elif th == "sha256":
		hashtype=hashlib.sha256
	elif th == "sha384":
		hashtype=hashlib.sha384
	elif th == "sha512":
		hashtype=hashlib.sha512

	print('====================[-]SharKHash[-]====================')
	time.sleep(1.5)

	for palavra in wl:
		hc = hashtype(palavra.strip().encode('utf-8')).hexdigest()
		time.sleep(2)
		print('[+]Testando senha ===>', palavra)
		time.sleep(2)
		if h == hc:
			print('Senha descriptografada ==>', palavra)
			sys.exit(1)

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

	try:
		for diretorio in ve:
			link = f"http://{url}/{diretorio}"
			r = requests.get(link)
			if r.status_code == 200:
				print('[-]', link, '==> 200')
			else:
				print('[-]', link, '==> 404 ou 403')
	except:
		print("[-]Não foi possível se conectar")

def sub():
	print(cyan, '''
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
	try:
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
	except:
		print("[-]Não foi possível se conectar")

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
	try:
		time.sleep(1.5)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s1 = s.connect((ip, int(porta)))
		print('[-]Conectando em ==> ', ip, ':', porta)
		time.sleep(1.75)
		s2 = s.recv(1024)
		print('[-]Banner ==> ', s2)
	except ConnectionRefusedError:
		print("[-]Não foi possível se conectar ao servidor")

def localip():
	print('''
                                                    
 ___  | |__     __ _   _ __  | | __ (_)  _ __  
/ __| | '_ \   / _` | | '__| | |/ / | | | '_ \ 
\__ \ | | | | | (_| | | |    |   <  | | | |_) |
|___/ |_| |_|  \__,_| |_|    |_|\_\ |_| | .__/ 
                                        |_|   
	''')
	try:
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
	except:
		print("[-]Não foi possível se conectar")

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
	os.system('clear')
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
	if menu != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" and "10":
		print("Escolha uma opção válida")

	elif a == '1':
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

def wd():
	print('''
 ___    ___   _ __    _   _   _ __ ___  
/ __|  / _ \ | '_ \  | | | | | '_ ` _ \                       [-]SENUM[-]
\__ \ |  __/ | | | | | |_| | | | | | | |      [+]Script para enumerar usuários do wordpress[+]
|___/  \___| |_| |_|  \__,_| |_| |_| |_|
	''')

	link = input("[-]Site alvo ==> ")
	url = f"https://{link}/wp-json/wp/v2/users"
	r = json.loads(requests.get(url).text)

	try:
		print("--------------------------------------")
		print("Usuário ==> ", r[0]["name"])
		print("Usuário ==> ", r[1]["name"])
		print("Usuário ==> ", r[2]["name"])
		print("Usuário ==> ", r[3]["name"])
		print("Usuário ==> ", r[4]["name"])
		print("Usuário ==> ", r[5]["name"])
		print("Usuário ==> ", r[6]["name"])
		print("Usuário ==> ", r[7]["name"])
		print("Usuário ==> ", r[8]["name"])
		print("Usuário ==> ", r[9]["name"])
		print("Usuário ==> ", r[10]["name"])
		print("--------------------------------------")
	except IndexError:
		print('--------------------------------------')
		print("[+]Todos os usuários enumerados")

os.system('clear')
print(vermelho, '[-]Carregando...')
time.sleep(2)
print(azul, '''
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

