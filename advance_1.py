#Operaciones con Operadores
cont_1=0
cont_2=0
cont_3=0
cont_4=0
cont_5=0
#pregunta 1
print("A. ¿Cómo logra Harry respirar bajo el agua durante la segunda tarea del Torneo de los Tres Magos?")
print("1) Se transfigura en un tiburón")
print("2) Besa a una sirena")
print("3) Él come gillyweed")
print("4) Él realiza un encanto de cabeza de burbuja")
respuesta_1=int (input())
if (respuesta_1 == 3):
     cont_1=cont_1+1
     print ("Verdadero")
elif (respuesta_1 != 3):
     print("Incorrecto")
#pregunta 2
print("B. ¿Cómo se llama la tienda de bromas de Fred y George?")
print("1) Emporio de bromas Weasley")
print("2) Weasleys 'Wizard Wheezes")
print("3) Fred & George's Wonder Emporium ")
print("4) Tienda de bromas de Zonko")
respuesta_2=int (input())
if (respuesta_2 == 2):
    cont_2=cont_2+1
    print ("Verdadero")
elif (respuesta_2 != 2):
    print("Incorrecto")

#pregunta 3
print("C. ¿Cuál de estos NO es una de las maldiciones imperdonables?")
print("1) Sectumsempra")
print("2) Maldición Cruciatus")
print("3) Avada Kedavra ")
print("4) Maldición Imperius")
respuesta_3=int (input())
if (respuesta_3 == 1):
    cont_3=cont_3+1
    print ("Verdadero")
elif (respuesta_3 != 1):
    print("Incorrecto")

#pregunta 4
print("D. ¿Quién interpretó a Lord Voldemort en las películas?")
print("1) Jeremy Irons")
print("2) Tom Hiddleston")
print("3) Gary Oldman ")
print("4) Ralph Fiennes")
respuesta_4=int (input())
if (respuesta_4 == 4):
    cont_4=cont_4+1
    print ("Verdadero")
elif (respuesta_3 != 4):
    print("Incorrecto")

#pregunta 5
print("E. ¿Quién vigila la entrada a la sala común de Gryffindor?")
print("1) La dama gris")
print("2) La señora gorda")
print("3) El fraile gordo")
print("4) El barón sangriento")
respuesta_5=int (input())
if (respuesta_5 == 2):
    cont_5=cont_5+1
    print ("Verdadero")
elif (respuesta_3 != 2):
    print("Incorrecto")
#funciones
def fan(promedio):
    if (promedio == 20):
        print("Te hace falta ver mas Harry Potter")
    elif (promedio == 40):
        print("Sabes lo basico")
    elif (promedio == 80):
        print("Casi perfecto, verlas de nuevo no te haria mal")
    elif (promedio ==100):
        print("Wow eres un master")

promedio=cont_1+cont_2+cont_3+cont_4+cont_5
promedio=(promedio*100)/5
print (promedio)

print(fan(promedio))
                   
                   
