import time

def media():
    while True: 
        media = 0
        try:
            for i in range(1, 4):
                n1 = float(input(f"\nDigite a {i}° nota: "))
                media += n1
            conta = media / 3 
            print(f"\nA média é: {conta:.2f}")
            choice = input("\nCalcular outra média? (S/N): ")
            if choice.upper() == 'N':
                break
        except:
            print("Erro, por favor digite apenas numeros")
            print("Reiniciando...\n")
            time.sleep(2)
            continue

media()
