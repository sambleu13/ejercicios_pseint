from time import sleep
from datetime import date
import math

def mayor_de_tres(n1,n2,n3):
    if n1 > n2:
        resultado = n1
    else:
        resultado = n2

    if n3 > resultado:
        resultado = n3
    
    return resultado

def ordenar_cinco(nums):
    tempo = len(nums)
    for i in range(tempo):
        #print(f"Numero {nums[i]} que se compara")
        for j in range(i+1,tempo):
            #print(f"Numero {nums[j]} con el que se compara")
            if nums[j] > nums[i]:
                #print(f"{nums[j]} es mayor que {nums[i]}")
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
    
    print("Los números ordenados de mayor a menor son:")

    for k in nums:
        print(f"{k}") #\n

def num_factorial(numfa):
    res = 1
    for i in range(1, numfa+1):
        res=res*i
    
    print(f"El factorial de {numfa} es {res}")

def lee_num(texto):
    while True:
        try:
            num = int(input(f"Ingresa {texto}: "))
            return num
            #break #cuando se guarden los n1
        except ValueError:
            print("Ingresa sólo un número entero")

def lee_num_dec(texto):
    while True:
        try:
            num = float(input(f"Ingresa {texto}: "))
            return num
            #break #cuando se guarden los n1
        except ValueError:
            print("Ingresa sólo un número decimal")

def log_in():
    print("Bienvenida")

    while True:
        try:
            nombre = str(input("Ingresa tu usuario: "))
            break #cuando se guarde
        except ValueError:
            print("Ingresa sólo letras")

    if nombre == "Samantha":
        while True:
            try:
                contra = str(input("Ingresa tu contraseña: "))
                break #cuando se guarde
            except ValueError:
                print("Ingresa sólo letras")

        if contra == "padawan":
            print("Acceso concedido.")
        else:
            print("Acceso denegado, contraseña incorrecta.")
    else:
        print("Usuario incorrecto.")

def dias_vividos():
    hoy = str(date.today())
    #print("Today's date:", hoy)
    dia_h=int(hoy[8:])
    mes_h=int(hoy[5:7])
    an_h=int(hoy[0:4])
    #print(f"hoy es {dia_h} de {mes_h} del {an_h}")
    #print(type(hoy))
    #print("Ingresa el día (formato DD) de tu nacimiento: ")
    dia_n = lee_num("el día de tu nacimiento en formato DD")
    #print("Ingresa el mes (formato MM) de tu nacimiento: ")
    mes_n = lee_num("el mes de tu nacimiento en formato MM")
    #print("Ingresa el año (formato AAAA) de tu nacimiento: ")
    an_n = lee_num("el año de tu nacimiento en formato AAAA")
    #print(dia_n,mes_n,an_n)
    #print(type(restar_meses(mes_h,an_h)))
    #print(restar_meses(mes_h,an_h))
    meses_h = restar_meses(mes_h,an_h) + dia_h
    meses_n = restar_meses(mes_n,an_n) + dia_n
    dias = 0
    c_b = 0

    if an_n < an_h:
        for i in range(an_n,an_h):
            if validar_bisiesto(i):
                dias=dias+366
                c_b=c_b+1
            else:
                dias=dias+365
        
        if (meses_h - meses_n) != 0:
            dias=dias+meses_h-meses_n
    elif an_h == an_n:
        dias=meses_h-meses_n
        
    print(f"Han transcurridos {dias} días transcurridos desde tu nacimiento hasta el día de hoy.")

def restar_meses(mes, ani):
    cm = 0
    for i in range(1,mes):
        #print(i)
        #print(type(i))
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            cm = cm + 31
        else:
            if i==2:
                if validar_bisiesto(ani):
                    cm=cm+29
                
                cm=cm+28
            else:
                cm=cm+30
    
    return cm

def validar_bisiesto (anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 4 == 0 and anio % 100 == 0):
        resultado = True
    else:
        resultado = False

    return resultado

def area_triangulo(b,h):
    area = (b*h) / 2
    return area

def vol_esfera(r):
    volumen = 4*math.pi*(r**3) / 3
    return volumen

def pares_impares(nums):
    tempo = len(nums)
    pares = 0
    impares = 0
    for i in range(tempo):
        if nums[i] % 2 == 0:
            pares = pares+1
        else:
            impares = impares+1

    if pares == 1:
        print(f"Se introdujeron {pares} número par y {impares} números impares")
    elif impares == 1:
        print(f"Se introdujeron {pares} números pares y {impares} número impar")
    else:
        print(f"Se introdujeron {pares} números pares y {impares} números impares")

def pos_negs(nums):
    tempo = len(nums)
    pos = 0
    negs = 0
    for i in range(tempo):
        if nums[i] >= 0:
            pos = pos+1
        else:
            negs = negs+1

    if pos == 0:
        print(f"Se introdujeron {negs} números negativos")    
    elif pos == 1:
        print(f"Se introdujeron {pos} número positivo y {negs} números negativos")
    elif negs == 0:
        print(f"Se introdujeron {pos} números positivos")
    elif negs == 1:
        print(f"Se introdujeron {pos} números positivos y {negs} número negativo")
    else:
        print(f"Se introdujeron {pos} números positivos y {negs} números negativos")

def incremento_sal():
    #print("Ingresa tu salario: ")
    salario = lee_num_dec("tu salario")
    inc = 0
    aux = 0
    if salario <= 15000:
        inc=salario*0.20
        aux=20
    else:
        inc=salario*0.15
        aux=15
    
    print(f"Tu salario de ${format(salario,'.2f')} pesos, incrementerá ${format(inc,'.2f')}, es decir, un {aux}%.")

def validar_palindromo():
    inv = ""
    j = 0
    while True:
        try:
            aux = str(input("Ingresa una palabra o frase a validar como palíndromo: "))
            break #cuando se guarde
        except ValueError:
            print("Ingresa sólo letras")
                
    temp = aux.replace(" ","")
    frase = temp.lower()

    for i in range(len(frase)):
        inv = inv+frase[i]
        #print(inv)

    for i in range(len(frase)):
        if frase[i] == inv[i]:
            j=j+1
    
    if j == len(frase):
        print(f"{aux} sí es palíndromo.")
    else:
        print(f"{aux} no es palíndromo.")

def cuanto_tiempo():
    vel = lee_num_dec("la velocidad en km/h")
    dis = lee_num_dec("la distancia en metros")
    temp = (dis/1000)/vel
    hora = math.trunc(temp)
    mins = round(((temp-hora)*60))
    if mins !=0 and hora == 1:
        print(f"Tomará {hora} hora y {mins} minutos.")
    elif mins !=0 and hora >= 1:
        print(f"Tomará {hora} horas y {mins} minutos.")
    elif mins == 0 and hora == 1:
        print(f"Tomará {hora} hora.")
    elif mins == 0 and hora > 1:
        print(f"Tomará {hora} horas.")
    elif mins == 0 and hora == 0:
        print("no tomará nada de tiempo.")
    else:
        print(f"Tomará {mins} minutos.")

while True:
    try:
        tipo = int(input("""
            Ingrese el tipo de operación a realizar:
                        
            Menú de opciones:
            
            1.- Mayor de tres numeros
            2.- Ordenar 5 números
            3.- Factorial
            4.- Login
            5.- Muestra nombre
            6.- Días vividos
            7.- Área triángulo
            8.- Volumen esfera
            9.- Pares e impares
            10.- Positivos y negativos
            11.- Incremento salarial
            12.- Tiempo de viaje
            13.- Validar año bisiesto
            14.- Validar palíndromo
            15.- Salir
            
        """))
        break #cuando se introduzca un número válido
    except ValueError:
        print("Ingresar una opción numérica únicamente")

if tipo == 1:
    n1 = lee_num("el primer número")
    n2 = lee_num("el segundo número")
    n3 = lee_num(" el tercer número")
    #mayor_de_tres(n1,n2,n3)
    print(f"El número mayor entre {n1}, {n2} y {n3} es: {mayor_de_tres(n1,n2,n3)}")

elif tipo == 2:
    numeros = []
    for i in range(1,6):
        #print(i)
        numeros.append(lee_num(f"el número {i}"))

    ordenar_cinco(numeros)

elif tipo == 3:
    nf = lee_num("un número")

    num_factorial(nf)

elif tipo == 4:
    sleep(1)

    log_in()

elif tipo == 5:

    while True:
        try:
            nom = str(input("Ingresa tu nombre: "))
            break #cuando se guarde
        except ValueError:
            print("Ingresa sólo letras")
            
    print(f"Hola, {nom}")

elif tipo == 6:
    dias_vividos()

elif tipo == 7:
    n1 = lee_num("la base")
    n2 = lee_num("la altura")
    print(f"El área del triángulo con base {n1}u y altura {n2}u es {area_triangulo(n1,n2)}u cuadradas")

elif tipo == 8:
    n1 = lee_num("el radio")
    print(f"El volumen de la esfera con radio {n1}u es {round(vol_esfera(n1),2)}u cúbicas")

elif tipo == 9:  
    numeros = []
    for i in range(1,11):
        numeros.append(lee_num(f"el número {i}"))
    
    pares_impares(numeros)

elif tipo == 10:  
    numeros = []
    for i in range(1,11):
        numeros.append(lee_num(f"el número {i}"))
    
    pos_negs(numeros)

elif tipo == 11:
    incremento_sal()

elif tipo == 12:
    cuanto_tiempo()

elif tipo == 13:
    n1 = lee_num("un año")
    if validar_bisiesto(n1):
        print(f"{n1} sí es bisiesto.")
    else:
        print(f"{n1} no es bisiesto.")

elif tipo == 14:
    validar_palindromo()

elif tipo == 15:
    print("Fin, hasta pronto.")

else:
    print("Opción no válida, intenta nuevamente o escribe 15 para salir.")