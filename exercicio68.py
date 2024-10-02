import random

def cria_tabuleiro():
    """Cria um tabuleiro vazio para o Jogo da Velha."""
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    return tabuleiro

def imprime_tabuleiro(tabuleiro):
    """Imprime o tabuleiro do Jogo da Velha."""
    print("---------")
    for linha in tabuleiro:
        print("|", end="")
        for coluna in linha:
            print(coluna, end="|")
        print("\n---------")

def verifica_vitoria(tabuleiro, jogador):
    """Verifica se o jogador ganhou."""
    
    for linha in range(3):
        if tabuleiro[linha][0] == jogador and tabuleiro[linha][1] == jogador and tabuleiro[linha][2] == jogador:
            return True
            
    for coluna in range(3):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True
    
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def verifica_empate(tabuleiro):
    """Verifica se houve empate."""
    for linha in tabuleiro:
        for coluna in linha:
            if coluna == " ":
                return False
    return True

def jogador_faz_jogada(tabuleiro, jogador):
    """Permite que o jogador faça sua jogada."""
    while True:
        try:
            linha = int(input(f"Jogador {jogador}, escolha a linha (1-3): ")) - 1
            coluna = int(input(f"Jogador {jogador}, escolha a coluna (1-3): ")) - 1
            if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador
                break
            else:
                print("Posição inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 3.")

def computador_faz_jogada(tabuleiro, jogador):
    """Faz a jogada do computador."""
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            break

def main():
    """Função principal do jogo da velha."""
    tabuleiro = cria_tabuleiro()
    jogador_atual = "X"
    fim_jogo = False

    print("Bem-vindo ao Jogo da Velha!")
    imprime_tabuleiro(tabuleiro)

    while not fim_jogo:
        if jogador_atual == "X":
            jogador_faz_jogada(tabuleiro, jogador_atual)
        else:
            computador_faz_jogada(tabuleiro, jogador_atual)

        imprime_tabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, jogador_atual):
            print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
            fim_jogo = True
        elif verifica_empate(tabuleiro):
            print("Empate!")
            fim_jogo = True

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    main()