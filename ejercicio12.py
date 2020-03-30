oracion=input("Introduce una frase: ")
car=input("Introduce una letra")
a=0
for i in oracion:
    if i == car:
        a += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (car, a,oracion))