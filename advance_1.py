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
#Casas de Howards preguntas
#Pregunta 1.1
print("A. ¿Cual de estas caracteriticas crees que te define mejor?")
print("1) Lealtad ")
print("2) Inteligencia ")
print("3) Ambición")
print("4) Valentia ")
def pregunta_11 (respuesta_11, cont):
    if (respuesta_11 == 1):
        cont=cont+30
        return(cont, "Mas treinta")
    elif (respuesta_11 == 2):
        cont=cont+20
        return(cont, "Mas veinte")
    elif (respuesta_11 == 3):
        cont=cont+10
        return(cont, "Mas diez")
    elif (respuesta_11 == 4):
        cont=cont+40
        return(cont,"Mas cuarenta")    
respuesta_11=int (input())
cont=0
cont,texto=pregunta_11(respuesta_11,cont)
print (texto)
#Pregunta 2.1
print("B. ¿Donde preferirias que tu dormitorio estuviese?")
print("1) En las mazmorras ")
print("2) En la torre del castillo")
print("3) Cerca de la cocina ")
print ("4) En el centro del castillo")
def pregunta_12 (respuesta_12, cont):
    if (respuesta_12 == 1):
        cont=cont+10
        return(cont, "Mas diez")
    elif (respuesta_12 == 2):
        cont=cont+20
        return(cont, "Mas veinte")
    elif (respuesta_12 == 3):
        cont=cont+30
        return(cont, "Mas treinta")
    elif (respuesta_12 == 4):
        cont=cont+40
        return(cont,"Mas cuarenta")    
respuesta_12=int (input())
cont,texto=pregunta_12(respuesta_12,cont)
print (texto)
#Pregunta 3.1
print("C. ¿Cuál de estas asignaturas escogerias?")
print("1) Posiciones ")
print("2) Transformaciones")
print("3) Historia de la magia")
print ("4) Astronomia")
def pregunta_13 (respuesta_13, cont):
    if (respuesta_13 == 1):
        cont=cont+30
        return(cont, "Mas treinta")
    elif (respuesta_13 == 2):
        cont=cont+10
        return(cont, "Mas diez")
    elif (respuesta_13 == 3):
        cont=cont+40
        return(cont, "Mas cuarenta")
    elif (respuesta_13 == 4):
        cont=cont+20
        return(cont,"Mas veinte")    
respuesta_13=int (input())
cont,texto=pregunta_13(respuesta_13,cont)
print (texto)
#Pregunta 4.1
print("D. ¿Alguna vez has copiado?")
print("1) Si, todos lo hacen ")
print("2) NO")
def pregunta_14 (respuesta_14, cont):
    if (respuesta_14 == 1):
        cont=cont+10
        return(cont, "Mas diez")
    elif (respuesta_14 == 2):
        cont=cont+40
        return(cont, "Mas cuarenta")
respuesta_14=int (input())
cont,texto=pregunta_14(respuesta_14,cont)
print (texto)
#Pregunta 5.1
print("E. ¿Que color te gusta mas?")
print("1) Rojo")
print("2) Amarillo")
print("3) Azul")
print("4) Verde")
def pregunta_15 (respuesta_15, cont):
    if (respuesta_15 == 1):
        cont=cont+40
        return(cont, "Mas cuarenta")
    elif (respuesta_15 == 2):
        cont=cont+30
        return(cont, "Mas treinta")
    elif (respuesta_15 == 3):
        cont=cont+20
        return(cont, "Mas veinte")
    elif (respuesta_15 == 4):
        cont=cont+10
        return(cont,"Mas diez")    
respuesta_15=int (input())
cont,texto=pregunta_15(respuesta_15,cont)
print (texto)
#Pregunta 6.1
print("F. Si jujugaras Quidditch ¿Cuál crees que seria tu rol en el equipo?")
print("1) Cazador/a")
print("2) Golpeador/a")
print("3) Guardian/a")
print("4) Buscador/a")
def pregunta_16 (respuesta_16, cont):
    if (respuesta_16 == 1):
        cont=cont+30
        return(cont, "Mas treinta")
    elif (respuesta_16 == 2):
        cont=cont+10
        return(cont, "Mas diez")
    elif (respuesta_16 == 3):
        cont=cont+40
        return(cont, "Mas cuarenta")
    elif (respuesta_16 == 4):
        cont=cont+20
        return(cont,"Mas veinte")    
respuesta_16=int (input())
cont,texto=pregunta_16(respuesta_16,cont)
print (texto)
#Pregunta 7.1
print("G. Te miras en el espejo de oesed y ves tu futuro ¿Cómo te ves?")
print("1) Con mucho dinero")
print("2) Rodeado de mis seres queridos")
print("3) Siendo alguien importante en howards")
print("4) Viviendo una increible aventura")
def pregunta_17 (respuesta_17, cont):
    if (respuesta_17 == 1):
        cont=cont+10
        return(cont, "Mas diez")
    elif (respuesta_17 == 2):
        cont=cont+30
        return(cont, "Mas treinta")
    elif (respuesta_17 == 3):
        cont=cont+20
        return(cont, "Mas veinte")
    elif (respuesta_17 == 4):
        cont=cont+40
        return(cont,"Mas cuarenta")    
respuesta_17=int (input())
cont,texto=pregunta_17(respuesta_17,cont)
print (texto)
#Pregunta 8.1
print("H.¿Que harias una vez terminaste tus estudios de Howards?")
print("1) Tendria una familiaTendria una familia")
print("2) Rodeado de mis seres queridos")
print("3) Siendo alguien importante en howards")
print("4) Viviendo una increible aventura")
def pregunta_18 (respuesta_18, cont):
    if (respuesta_18 == 1):
        cont=cont+10
        return(cont, "Mas diez")
    elif (respuesta_18 == 2):
        cont=cont+30
        return(cont, "Mas treinta")
    elif (respuesta_18 == 3):
        cont=cont+20
        return(cont, "Mas veinte")
    elif (respuesta_18 == 4):
        cont=cont+40
        return(cont,"Mas cuarenta")    
respuesta_18=int (input())
cont,texto=pregunta_18(respuesta_18,cont)
print (texto)
#Casa de Howards segun tus puntuaciones
while cont>=80 and cont<=110:
    print("Slidering")
    cont=0
while cont>=120 and cont<=180:
    print ("Ravenclaw")
    cont=0
while cont>=190 and cont<=250:
    print ("Hupperfugh")
    cont=0
while cont>=260 and cont<=320:
    print ("Grifindor")
    cont=0


