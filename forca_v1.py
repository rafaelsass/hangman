# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import string

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		
		
	# Método para adivinhar a letra
	def guess(self, letter=''):
		while True:
			self.letter = input("guess a letter: ")
			if len(self.letter) == 1 and self.letter.isalpha():
				break
			print("Enter a valid character")


		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if all([letters in self.right_guesses for letters in self.word]):
			return True

	# Método para não mostrar a letra no board
	def hide_word(self):
		
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self, right_guesses=[], wrong_guesses=[]):
		self.right_guesses = right_guesses
		self.wrong_guesses = wrong_guesses
		while True:
			if all([self.letter in self.word, self.letter not in self.right_guesses,
					self.letter not in self.wrong_guesses]):
				self.right_guesses.append(self.letter)
				break
			elif all([self.letter not in self.word, self.letter not in self.right_guesses,
					  self.letter not in self.wrong_guesses]):
				self.wrong_guesses.append(self.letter)
				break
			else:
				print("Enter a different character!")
				self.guess()
		try:
			print(board[len(self.wrong_guesses)])
		except IndexError:
			pass
		print("Right guesses: %s \nWrong guesses: %s" % (self.right_guesses, self.wrong_guesses))


		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
	game = Hangman(rand_word())

	while True:
    	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
		game.guess()

		# Verifica o status do jogo
		game.print_game_status()

		# De acordo com o status, imprime mensagem na tela para o usuário
		if game.hangman_won():
			print ('\nParabéns! Você venceu!!')
			print('\nFoi bom jogar com você! Agora vá estudar!\n')
			break
		else:
			print ('\nGame over! Você perdeu.')
			print ('A palavra era ' + game.word)


# Executa o programa		
if __name__ == "__main__":
	main()

