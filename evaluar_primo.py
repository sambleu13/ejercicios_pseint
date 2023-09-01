def lee_num(texto):
    while True:
        try:
            num = int(input(f"Ingresa {texto}: "))
            return num
            #break #cuando se guarden los n1
        except ValueError:
            print("Ingresa sólo un número entero")

def ev_primo(num):
    if num == 1 or num == 2:
        return True
    else:
        for i in range(2,int(num/2)):
            if num % i == 0:
                return False
        return True

numero=lee_num("un número entero")

if ev_primo(numero):
    print(f"{numero} es número primo")
else:
    print(f"{numero} no es número primo.")


