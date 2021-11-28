import os
import random
from itertools import chain, combinations

class SomaSubc:
  def __init__(self):
    self.main()

  # Retorna o powerset do conjunto
  def powerset(self,iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s) + 1))

  # Encontra o subset que satisfaz a soma de S = t
  def findSubset(self):
    string = f"Não existe subconjunto S cuja as somas dos elementos resulta em {self.valorBuscado}"
    color = bcolors.RED
    for subset in list(self.powerset(self.conjunto)):
      if sum(list(subset)) == self.valorBuscado:
        string = subset
        color = bcolors.GREEN
        break
    print(f"""
        S = {self.conjunto}
        t = {self.valorBuscado}
        {color}soma-subc = {string}{bcolors.ENDC}
        """)

  # Gera valores aleatórios para o conjunto S e o valor t
  def generateRandomValues(self):
    myarray = []
    value = random.randint(1, 50)
    myarray = random.sample(range(1, 9), random.randint(3, 8))
    return myarray, value

  # Processa o input do usuário para S e T
  def userInsert(self):
    rawS = input("Insira os valores do conjunto S separados por um espaço (Exemplo: 1 2 3 4 5)\n(Zero não pode ser uma opção)\nS = ")
    treatedS = rawS.split(" ")
    S = []
    s = 0
    for i in treatedS:
      try: 
        s = int(i)
      except:
        s = 0
      S.append(s)
    S = list(filter(lambda n: n != 0, S))
    print("S = ", S)
    v = 0
    while True:
      valor = input("Insira o valor de t\nt = ")
      try: 
        v = int(valor)
        break
      except:
        print("Você digitou um valor inválido.\nDigite novamente.")

    return S, v


  def iniciar(self, S, t):
    self.conjunto = S
    self.valorBuscado = t
    self.findSubset()
    input("\nPressione enter para voltar ao menu de escolha...")


  def main(self):
    print(f"{bcolors.MAGENTA}*** Bem vindo a SOMA-SUBC ***\n{bcolors.ENDC}")
    while True:
      print("""Escolha uma opção de execução:
      1 - Usar exemplo S = {1,3,6,9} e t = 13
      2 - Usar exemplo S = {1,5,7,9} e t = 4
      3 - Gerar S e t aleatórios
      4 - Inserir valores de S e T
      5 - Sair do programa
      """)

      choice = input("Digite o número de sua escolha: ")
      if choice == "1":
        self.iniciar([1,3,6,9], 13)
        os.system('cls' if os.name == 'nt' else 'clear')
      elif choice == "2":
        self.iniciar([1,5,7,9], 4)
        os.system('cls' if os.name == 'nt' else 'clear')
      elif choice == "3":
        s, t = self.generateRandomValues()
        self.iniciar(s, t)
        os.system('cls' if os.name == 'nt' else 'clear')
      elif choice == "4":
        s, t = self.userInsert()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.iniciar(s, t)
        os.system('cls' if os.name == 'nt' else 'clear')
      elif choice == "5":
        print("Obrigada por usar :D")
        return
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Valor inválido :(")

## -------------------------------------------------------------------- ##

# Classe de cores no terminal
class bcolors:
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

## -------------------------------------------------------------------- ##

if __name__ == "__main__":
  SomaSubc()