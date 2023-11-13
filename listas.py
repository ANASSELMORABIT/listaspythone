# numeros=[] # crear una lista 
# for i in range (1,21):# crear una lista 
#     numeros.append(i)# crear una lista 
# print(numeros[2])#El tercer número 
# print(numeros[0:5])#Los primeros cinco números. 
# print(numeros[0:len(numeros)//2])# la primera mitad de la lista.
# print(numeros[15:len(numeros)])#Los últimos cinco números. 
# print(numeros[len(numeros):0])
# print("la lista origin:",numeros)
# numeros.reverse()                  #la lista inverse
# print("la lista inverse:",numeros) # la lista inverse
# print(numeros[2])#el tercer número por la cola.

# X=input("ingresar una palabra:")
# while "m" not in X:
#     print("no has introducido la palabra correcta")
#     X=input("ingresar una palabra:")
# print("has introducido la palabra correcta")
# Num_us=int(input("ingresa un numero :"))
# numeros=[]
# while Num_us>0:
#     X=Num_us % 10
#     numeros.append(X)
#     Num_us=Num_us // 10
# print("la lista:")
# print(numeros)
# print("el máximo:")
# print(max(numeros))
# print("el minimo:")
# print(min(numeros))
# print("la suma:")
# print(sum(numeros))
#c
# def caracter(X):
#     new_liste=list(X)
#     for indice,valor in enumerate(new_liste):
#         print(f"Indice:{indice},Valor:{valor}")
#     return
# frace=input("introduza una frase:")
# caracter(frace)
#nuevo_lista=[2**i for i in range(29)]
# print(nuevo_lista)

# Mostrar el horario
# def rellanCalendario():
#     horario = [
#     ["Lunes", "", "", "", "", "", ""],
#     ["Martes", "", "", "", "", "", ""],
#     ["Miércoles", "", "", "", "", "",""],
#     ["Jueves", "", "", "", "", "", ""],
#     ["Viernes", "", "", "", "", "", ""]
# ]
#     for i,dia in enumerate(horario):
#         for j in range(1,len(dia)):
#             asignatura=input(f"Ingrese la asignatura para {dia[0]} - Hora {j}:")
#             horario[i][j]=asignatura
#     return horario
# calendria=rellanCalendario()
# for i in calendria:
#     print(i)
def valido(correo):
    if "@" in correo and "." in correo:
        return True
    else:
        return False
def separar(correo):
    partes=correo.split("@")
    first=partes[0]
    second_third=partes[1].split(".")
    second=second_third[0]
    third=second_third[1]
    return first,second,third
listas_correos=[
    "anasselmorabit797@gmail.com",
    "albert@gmail.com",
    "juancarlos.com",
    "albert@gmail",
    "albert@gmail.com",
    "albertorodriguez@gmail.com",
    "pepalvaro",
    "anasselmorabit797@gmail.com",
    "albertorodriguez@gmail.com",
    "ANASS ELMORABIT"
]
correos_validos=[]
for indice,correo in enumerate(listas_correos):
    print(f"correos numero {indice+1} :{correo}")
    if valido(correo):
        primero,segundo,tersero=separar(correo)
        print(f"{primero} / {segundo} / {tersero}")
        correos_validos.append(correo)
    else:
        print("Correo no válido: se eliminará de la lista")
print("\nLista de correos válidos:")
for i, correo_valido in enumerate(correos_validos, start=1):
    print(f"Correo número {i}: {correo_valido}")
lista_copia=[]
for correo in correos_validos:
    if correo not in lista_copia:
        lista_copia.append(correo)
print("Los correos Validos:")
for indice,correo in enumerate(lista_copia,start=1):
    print(f"Correo número {indice}: {correo}")       

