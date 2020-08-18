import os
import random
from colorama import Fore, Back, Style

replay = "s"
jogadas = 0
player = 2 # 1 = CPU - 2 = Jogador
max_jogadas = 9
vitoria = False
velha = [
	[" "," "," "],
	[" "," "," "],
	[" "," "," "],
]

def Tela():
	global velha
	global jogadas
	os.system("cls")
	print("     0   1   2")
	print("0:   " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
	print("   -------------")
	print("1:   " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
	print("   -------------")
	print("2:   " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
	print("   -------------")
	#modificar para um for
	print("Jogadas = " +  Fore.GREEN + str(jogadas) + Fore.RESET)

def PlayerPlay():
	global jogadas
	global player
	global max_jogadas
	if player == 2 and jogadas < max_jogadas:
		try:
			l = int(input("Linha..: "))
			c = int(input("Coluna.: "))
			while velha[l][c] != " ":
				l = int(input("Linha..: "))
				c = int(input("Coluna.: "))
			velha[l][c] = "X"
			player = 1
			jogadas += 1
		except:
			print("Jogada inválida!")
			os.system("pause")
			#vitoria = False

def CpuPlay():
	global jogadas
	global player
	global max_jogadas
	if player == 1 and jogadas < max_jogadas:
		l = random.randrange(0,3)
		c = random.randrange(0,3)
		while velha[l][c] != " ":
			l = random.randrange(0,3)
			c = random.randrange(0,3)
		velha[l][c] = "O"
		jogadas += 1
		player = 2

def VerificarVitoria():
	global velha
	vitoria = False
	simbolos = ["X","O"]
	for s in simbolos:
		vitoria = False
		i_l = i_c = 0
		while i_l < 3:
			soma = 0
			i_c = 0
			while i_c < 3 :
				if (velha[i_l][i_c]==s) :
					soma += 1
				i_c += 1
			if soma == 3:
				vitoria = s
				break
			i_l += 1
		if vitoria != False:
			break
		i_l = i_c = 0
		while i_c < 3:
			soma = 0
			i_l = 0
			while i_l < 3 :
				if (velha[i_l][i_c]==s) :
					soma += 1
				i_l += 1
			if soma == 3:
				vitoria = s
				break
			i_c += 1
		if vitoria != False:
			break
		soma = 0
		i_d = 0
		while i_d < 3:
			if (velha[i_d][i_d]==s) :
					soma += 1
			i_d += 1
		if soma == 3:
			vitoria = s
			break
		soma = 0
		i_d1 = 0
		i_d2 = 2
		while i_d2 >= 0:
			if (velha[i_d1][i_d2]==s) :
					soma += 1
			i_d1 += 1
			i_d2 -= 1
		if soma == 3:
			vitoria = s
			break
	return vitoria

def Redefinir():
	global velha
	global jogadas
	global player
	global max_jogadas
	global vitoria
	jogadas = 0
	player = 2
	max_jogadas = 9
	vitoria = False
	velha = [
		[" "," "," "],
		[" "," "," "],
		[" "," "," "],
	]

while replay == "s":
	while True:
		Tela()
		PlayerPlay()
		CpuPlay()
		Tela()
		Vitoria = VerificarVitoria()
		if Vitoria != False or jogadas >= max_jogadas:
			break
	print(Fore.BLUE + "------- FIM DE JOGO -------")
	if Vitoria == "X" or Vitoria == "O":
		print(Fore.YELLOW + "** Resultado : Jogador " + Vitoria + " **")
	else:
		print("** Empate **")
	replay = input(Fore.GREEN + "Deseja jogar novamente? [S/N]: " + Fore.RESET).lower()
	Redefinir()

print(Fore.RED + "Obrigado por jogar!!!" + Fore.RESET)
