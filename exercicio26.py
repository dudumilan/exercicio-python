def main():
    """
    Recebe dois números maiores que zero, calcula e mostra um elevado ao outro. O expoente deverá ser no máximo 10.
    """
    while True:
        try:
            base = int(input("Digite a base (um número maior que zero): "))
            expoente = int(input("Digite o expoente (um número maior que zero e no máximo 10): "))
            if base > 0 and expoente > 0 and expoente <= 10:
                break
            else:
                print("Os números devem ser maiores que zero e o expoente no máximo 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")

    resultado = base ** expoente
    print(f"{base} elevado a {expoente} é {resultado}")

if __name__ == "__main__":
    main()