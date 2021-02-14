import time
import sys
import socket
from datetime import datetime
import os
import hashlib
import requests

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


print('[-]Carregando...')
time.sleep(2)
print('''
                     .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.                                [ψ]SHARK - FRAMEWORK 1.0[ψ]
              d$L  4.         4$$$$$$$$$$$$$$                          [-]Coleção de ferramentas para pentest[-]
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$      [!]A ferramenta está em fase beta, caso ache um erro ou sugestão entre em contato[!]   
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$                            [>]Discord ==> eduardor 《》#3429[<]
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

menu = input('''
---------------------------------------------
Hello friend, escolha uma das opçoes abaixo
---------------------------------------------
=========================================
[1]Portscanner ==> Python
[2]Hash cracker ==> Python
[3]Brute force diretórios ==> Python
[4]Brute force subdomínios ==> Python
=========================================
[ψ]Sua opção ==> ''')

if menu == '1':
	print('[-]Você escolheu usar o Portscanner')
	time.sleep(1)
	print('[-]Carregando...')
	time.sleep(1.5)
	portscanner()

elif menu == '2':
	print('[-]Você escolheu usar o hash cracker')
	time.sleep(1)
	print('[-]Carregando...')
	time.sleep(1.5)
	hashcracker()

elif menu == '3':
	print('[-]Você escolheu usar o brute force em diretórios')
	time.sleep(1)
	print('[-]Carregando...')
	time.sleep(1.5)
	bfdir()

elif menu == '4':
	print('[-]Você escolheu usar o brute force em subdomínios')
	time.sleep(1)
	print('[-]Carregando...')
	time.sleep(1.5)
	sub()
