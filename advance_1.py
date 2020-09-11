#pregunta 1
print("A. ¿Cómo logra Harry respirar bajo el agua durante la segunda tarea del Torneo de los Tres Magos?")
print("1) Se transfigura en un tiburón")
print("2) Besa a una sirena")
print("3) Él come gillyweed")
print("4) Él realiza un encanto de cabeza de burbuja")
def pregunta_1 (respuesta_1, cont):
    if (respuesta_1 == 3):
        cont=cont+1
        return(cont, "Verdadero")
    elif (respuesta_1 != 3):
        return(cont, "Falso")
respuesta_1=int (input())
cont=0
cont,texto=pregunta_1(respuesta_1,cont)
print (texto)
#pregunta 2
print("B. ¿Cómo se llama la tienda de bromas de Fred y George?")
print("1) Emporio de bromas Weasley")
print("2) Weasleys 'Wizard Wheezes")
print("3) Fred & George's Wonder Emporium ")
print("4) Tienda de bromas de Zonko")
def pregunta_2 (respuesta_2, cont):
    if (respuesta_2 == 2):
        cont=cont+1
        return(cont, "Verdadero")
    elif (respuesta_2 != 2):
        return(cont, "Falso")
respuesta_2=int (input())
cont,texto=pregunta_2(respuesta_2,cont)
print (texto)
#pregunta 3
print("C. ¿Cuál de estos NO es una de las maldiciones imperdonables?")
print("1) Sectumsempra")
print("2) Maldición Cruciatus")
print("3) Avada Kedavra ")
print("4) Maldición Imperius")
def pregunta_3 (respuesta_3, cont):
    if (respuesta_3 == 1):
        cont=cont+1
        return(cont, "Verdadero")
    elif (respuesta_3 != 1):
        return(cont, "Falso")
respuesta_3=int (input())
cont,texto=pregunta_3(respuesta_3,cont)
print (texto)
#pregunta 4
print("D. ¿Quién interpretó a Lord Voldemort en las películas?")
print("1) Jeremy Irons")
print("2) Tom Hiddleston")
print("3) Gary Oldman ")
print("4) Ralph Fiennes")
def pregunta_4 (respuesta_4, cont):
    if (respuesta_4 == 4):
        cont=cont+1
        return(cont, "Verdadero")
    elif (respuesta_4 != 4):
        return(cont, "Falso")
respuesta_4=int (input())
cont,texto=pregunta_4(respuesta_4,cont)
print (texto)
#pregunta 5
print("E. ¿Quién vigila la entrada a la sala común de Gryffindor?")
print("1) La dama gris")
print("2) La señora gorda")
print("3) El fraile gordo")
print("4) El barón sangriento")
def pregunta_5 (respuesta_5, cont):
    if (respuesta_5 == 2):
        cont=cont+1
        return(cont, "Verdadero")
    elif (respuesta_5 != 2):
        return(cont, "Falso")
respuesta_5=int (input())
cont,texto=pregunta_5(respuesta_5,cont)
print (texto)
#funciones #operaciones  
def fan(promedio):
    if (promedio == 20):
        print("Te hace falta ver mas Harry Potter")
    elif (promedio == 40):
        print("Sabes lo basico")
    elif (promedio == 80):
        print("Casi perfecto, verlas de nuevo no te haria mal")
    elif (promedio ==100):
        print("Wow eres un master")
promedio=(cont*100)/5
print (promedio)
print(fan(promedio))
                   
                   
