#pregunta 1
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["A. ¿Cómo logra Harry respirar bajo el agua durante la segunda tarea del Torneo de los Tres Magos?"],
        ["1) Se transfigura en un tiburón"], 
        ["2) Besa a una sirena"],
        ["3) Él come gillyweed"],
        ["4) Él realiza un encanto de cabeza de burbuja"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["B. ¿Cómo se llama la tienda de bromas de Fred y George?"],
        ["1) Emporio de bromas Weasley"], 
        ["2) Weasleys 'Wizard Wheezes"],
        ["3) Fred & George's Wonder Emporium "],
        ["4) Tienda de bromas de Zonko"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["C. ¿Cuál de estos NO es una de las maldiciones imperdonables?"],
        ["1) Sectumsempra"], 
        ["2) Maldición Cruciatus"],
        ["3) Avada Kedavra "],
        ["4) Maldición Imperius"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["D. ¿Quién interpretó a Lord Voldemort en las películas?"],
        ["1) Jeremy Irons"], 
        ["2) Tom Hiddleston"],
        ["3) Gary Oldman "],
        ["4) Ralph Fiennes"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["E. ¿Quién vigila la entrada a la sala común de Gryffindor?"],
        ["1) La dama gris"], 
        ["2) La señora gorda"],
        ["3) El fraile gordo"],
        ["4) El barón sangriento"]]
imprime_matriz(matriz)
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
    if (promedio <= 20):
        print("Te hace falta ver mas Harry Potter")
    elif (promedio == 40):
        print("Sabes lo basico")
    elif (promedio >= 60 and promedio <= 80):
        print("Casi perfecto, verlas de nuevo no te haria mal")
    elif (promedio ==100):
        print("Wow eres un master")
promedio=(cont*100)/5
print (promedio)
print(fan(promedio))
print()
#Casas de Howards preguntas
#Pregunta 1.1
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["A. ¿Cual de estas caracteriticas crees que te define mejor?"],
        ["1) Lealtad "], 
        ["2) Inteligencia "],
        ["3) Ambición"],
        ["4) Valentia "]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["B. ¿Donde preferirias que tu dormitorio estuviese?"],
        ["1) En las mazmorras "], 
        ["2) En la torre del castillo"],
        ["3) Cerca de la cocina "],
        ["4) En el centro del castillo"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["C. ¿Cuál de estas asignaturas escogerias?"],
        ["1) Posiciones "], 
        ["2) Transformaciones"],
        ["3) Historia de la magia"],
        ["4) Astronomia"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["D. ¿Alguna vez has copiado?"],
        ["1) Si, todos lo hacen "], 
        ["2) NO"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["E. ¿Que color te gusta mas?"],
        ["1) Rojo"], 
        ["2) Amarillo"],
        ["3) Azul"],
        ["4) Verde"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["F. Si jujugaras Quidditch ¿Cuál crees que seria tu rol en el equipo?"],
        ["1) Cazador/a"], 
        ["2) Golpeador/a"],
        ["3) Guardian/a"],
        ["4) Buscador/a"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["G. Te miras en el espejo de oesed y ves tu futuro ¿Cómo te ves?"],
        ["1) Con mucho dinero"], 
        ["2) Rodeado de mis seres queridos"],
        ["3) Siendo alguien importante en howards"],
        ["4) Viviendo una increible aventura"]]
imprime_matriz(matriz)
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
def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "," ,end="" )
        print ()
matriz=[["H.¿Que harias una vez terminaste tus estudios de Howards?"],
        ["1) Tendria una familia"], 
        ["2) Me uniria al ministerio de magia"],
        ["3) Seguiria estudiando"],
        ["4) Me iria de viaje"]]
imprime_matriz(matriz)
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
def casa(cont):
    if (cont>=80 and cont<=110):
        print("Slidering")
    elif (cont>=120 and cont<=180):
        print ("Ravenclaw")
    elif (cont>=190 and cont<=250):
        print ("Hupperfugh")
    elif (cont>=260 and cont<=320):
        print ("Grifindor")
print(cont)
print(casa(cont))


