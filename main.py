from random import choice

#Funções
def avaliarJogada(letra, palavra, palavra_oculta):
    if letra in (palavra.upper()) or (chute in palavra.lower()):
        print('\033[1;32mAcertou!\033[m')
        c=0
        for caractere in palavra:
            if letra == (caractere.upper()) or letra == (caractere.lower()):
                letra = caractere
                palavra_oculta[c] = letra
            c+=1
        return True
    else:
        print('\033[31;1mErrou!\033[m')
        return False


def compararPalavras(palavra, palavra_oculta):
    if ''.join(palavra_oculta) == palavra:
        print()
        print('-*' * 25)
        print('Você venceu! (*^_^*)'.center(50))
        print('-*' * 25)
        print(f'A palavra era "{palavra}"'.center(50))
        return True


def verificarHP(hp, palavra):
    if hp == 0:
        print()
        print('-*' * 25)
        print('Você foi enforcado! ಠ_ಠ'.center(50))
        print('-*' * 25)
        print(f'A palavra era "{palavra}"'.center(50))
        return True

# Abastecer um dicionário com muitas palavras
banco_de_palavras = {
    'alimento':['Banana', 'Macarrão', 'Iogurte', 'Pizza', 'Hamburguer', 'Milk-Shake'],
    'animal':['Capivara', 'Crocodilo', 'Gato', 'Cavalo', 'Rinoceronte', 'Tartaruga'],
    'país':['Brasil', 'Argentina', 'Alemanha', 'França', 'Austrália', 'Nova Zelândia'],
    'nome':['Leonardo Da Vinci', 'Aristóteles', 'Pitágoras', 'Jesus', 'Júlio César', 'Michelangelo']                         
}
'''As chaves dos dicionários representam a categoria dos valores da chave(que são as palavras)'''

# Criar uma interface
print('=-' * 20)
print('Jogo da Velha'.center(40))
print('-=' * 20)
print()
nome = input('Como você se chama? R= ').strip().title() #Tratamento de string
print()

#Escolher uma palavra aleatória do banco_de_palavras
sorteado = choice(list((banco_de_palavras.items()))) #Sorteia um item do dicionário
categoria = sorteado[0] #Atribui a key do item à variável categoria
palavra = choice(sorteado[1]) #Sorteia um elemento da lista e atribui à variável palavra

#Cria uma variável com a palavra censurada
palavra_oculta = []
for caractere in palavra:
    if caractere.isalpha():
        palavra_oculta.append('_')
    elif caractere.isspace():
        palavra_oculta.append('  ')

# Criar variáveis para contar as tentativas e armazenar a "vida" do jogador
tentativas = 0
vida = 10

#JOGO
ganhou = enforcou = False
print(f'Categoria da palavra é: {categoria}')
print()
while (not ganhou) and (not enforcou):
    print(' '.join(palavra_oculta))
    print()
    chute = str(input('==> Chute uma letra = ')).strip()
    tentativas+=1
    print()

    acertou = avaliarJogada(chute, palavra, palavra_oculta)
    if not acertou:
        vida-=1
        print(f'\033[1;33mHP= {vida}\033[m')

    ganhou = compararPalavras(palavra, palavra_oculta)
    enforcou = verificarHP(vida, palavra)
    print()
    
# Mostrar quadro com informações do usuário
print(f'\033[35;1mNome: {nome}\033[m')
print(f'\033[36;1mTentativas: {tentativas}\033[m')