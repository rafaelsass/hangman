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
			self.letter = input("guess a letter: ").lower()
			if len(self.letter) == 1 and self.letter.isalpha():
				break
			print("Enter a valid character")


		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
	    if self.hangman_won():
	        return True
	    else:
	        try:
	            board[len(self.wrong_guesses)]
	            return False
	        except IndexError:
	            return True
		
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if all([letters in self.right_guesses for letters in self.word]):
			return True

	# Método para não mostrar a letra no board
	def hide_word(self, space =['']):
		self.space = (['_ ']*len(self.word))
		if self.letter in self.word:
			if self.word.count(self.letter) > 1:
				


		for right_letter in self.right_guesses:
			self.space[self.word.index(right_letter)] = right_letter
		print(tuple(self.space))
		
		
		
		
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
	    print("tries left: %s \n" %(7-len(self.wrong_guesses)))

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    while True:
        # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
        game.guess()

        # Verifica o status do jogo
        game.print_game_status()
        game.hide_word()
  #      game.hide_word()

        # De acordo com o status, imprime mensagem na tela para o usuário
        if game.hangman_over():
            if game.hangman_won():
                print('\nParabéns! Você venceu!!')
                print('\nFoi bom jogar com você! Agora vá estudar!\n')
                
            else:
                print('\nGame over! Você perdeu.')
                print('A palavra era ' + game.word)
            break


# Executa o programa		
if __name__ == "__main__":
	main()

