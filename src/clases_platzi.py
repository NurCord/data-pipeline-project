import os
os.system("clear")

# Logs

name = "Platzi"
value = 3.43433232

print("___________Logs__________")
print("Valor de la variable {}".format(name))
print(f"Valor de la variable {name}")
print("Valor con dos decimales {:.2f}".format(value))

# Operaciones
a = 10
b = 3

print("___________Operaciones__________")
print("Suma: {}".format(a + b))
print("Resta: {}".format(a - b))
print("Multiplicación: {}".format(a * b))
print("División: {}".format(a / b))
print("División entera: {}".format(a // b))
print("Módulo: {}".format(a % b))
print("Potencia: {}".format(a ** b))

# Operadores booleanos

print("___________Operadores booleanos__________")
print("A es mayor que B ", a > b)
print("A es menor que B", a < b)
print("A es igual a B", a == b)
print("A es diferente a B", a != b)
print("A es mayor o igual que B", a >= b)
print("A es menor o igual que B", a <= b)

# Casteo de tipos

print("___________Casreo de tipos__________")
print("Cadena a entero: {}".format(int("123")))
print("Cadena a flotante: {}".format(float("3.14")))
print("Flotante a cadena: {}".format(str(value)))

# Condicionales

print("___________Condicionales__________")
age = 20
if age < 18:
    print("Eres menor de edad")
elif age == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")

# Ternario

print("___________Ternario__________")
is_adult = "Eres mayor de edad" if age >= 18 else "Eres menor de edad"
print(is_adult)

# Listas
print("___________Listas__________")

empty_list = []
print("Lista vacía:", empty_list)
list_with_lists = [[1, 2, 3], [4, 5, 6]]
print("Lista con listas:", list_with_lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:", matrix)

# Metodos de listas
print("___________Métodos de listas__________")

fruits = ["apple", "banana", "cherry"]

print("Longitud de fruits", len(fruits))
print("Primer elemento de fruits", fruits[0])
print("Último elemento de fruits", fruits[-1])
print("Sublista de fruits", fruits[1:3])

fruits.append("orange")
print("Lista de frutas después de añadir 'orange':", fruits)
fruits.insert(1, "kiwi")
print("Lista de frutas después de insertar 'kiwi':", fruits)
fruits.extend(["grape", "melon"])
print("Lista de frutas después de extender con 'grape' y 'melon':", fruits)
fruits.remove("banana")
print("Lista de frutas después de eliminar 'banana':", fruits)
last_fruit = fruits.pop()
print("Lista de frutas después de eliminar el último elemento:", fruits, last_fruit)
second_fruit = fruits.pop(1)
print("Lista de frutas después de eliminar el segundo elemento:", fruits, second_fruit)
print("Indice de 'cherry':", fruits.index("cherry"))

# Ordena la misma lista de frutas
fruits.sort()
print("Lista de frutas ordenada:", fruits)

fruits.sort(key=str.lower)
print("Lista de frutas ordenada sin importar mayúsculas/minúsculas:", fruits)

print("Count de 'apple':", fruits.count("apple"))

# Ordena la lista de frutas sin modificar la original
sorted_fruits = sorted(fruits)
print("Lista de frutas ordenada (sin modificar la original):", sorted_fruits)

fruits.clear()
print("Lista de frutas después de limpiar:", fruits)

lists_of_letters = ["a", "b", "c", "d", "e", "f", "g"]
print("Lista de letras:", lists_of_letters)
del lists_of_letters[3:]
print("Lista de letras después de eliminar el cuarto elemento:", lists_of_letters)

numbers = [1, 2, 3, 4, 5]

print("Lista de números:", numbers)
print("Suma de números:", sum(numbers))
print("Máximo número:", max(numbers))
print("Mínimo número:", min(numbers))
print("Longitud de números:", len(numbers))
# numbers[desde:hasta:paso] el paso por defecto es 1 va 1 a 1 por cada elemento
print("Lista de números de a dos:", numbers[::2])
print("Lista de números al revés:", numbers[::-1])

numbers = numbers + [6, 7, 8]
print("Agregar mas números:", numbers + [6, 7, 8])

# mas eficiente que el anterior a nivel de memoria
numbers += [9, 10]
print("Agregar más números con +=:", numbers)
print("Repetir lista de números:", numbers * 2)



