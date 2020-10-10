def imprime_matriz(mat):
    for linea in mat:
        for col in linea:
            print(col, "" ,end="" )
        print ()
def pregunta (respuesta, correcta, cont):
    if (respuesta == correcta):
        cont=cont+1
        return(cont, "Verdadero")
    else :
        return(cont, "Falso")
def fan(promedio):
    if (promedio <= 20):
        print("Te hace falta ver mas Harry Potter")
    elif (promedio == 40):
        print("Sabes lo basico")
    elif (promedio >= 60 and promedio <= 80):
        print("Casi perfecto, verlas de nuevo no te haria mal")
    elif (promedio ==100):
        print("Wow eres un master")
def pregunta_1 (respuesta, correcta1, correcta2, correcta3, correcta4, cont):
    if (respuesta == correcta1):
        cont=cont+10
        return(cont, "Mas diez")
    elif (respuesta == correcta2):
        cont=cont+20
        return(cont, "Mas veinte")
    elif (respuesta== correcta3):
        cont=cont+30
        return(cont, "Mas treinta")
    elif (respuesta== correcta4):
        cont=cont+40
        return(cont,"Mas cuarenta")  
def casa(cont):
    if (cont>=80 and cont<=110):
        print("Slidering")
    elif (cont>=120 and cont<=180):
        print ("Ravenclaw")
    elif (cont>=190 and cont<=250):
        print ("Hupperfugh")
    elif (cont>=260 and cont<=320):
        print ("Grifindor")
#Pregunta 1  
matriz=[["A. ¿Cómo logra Harry respirar bajo el agua durante la segunda tarea del Torneo de los Tres Magos?"],
        ["1) Se transfigura en un tiburón"], 
        ["2) Besa a una sirena"],
        ["3) Él come gillyweed"],
        ["4) Él realiza un encanto de cabeza de burbuja"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta=3
cont=0
cont,texto=pregunta(respuesta, correcta,cont)
print (texto)
#pregunta 2
matriz=[["B. ¿Cómo se llama la tienda de bromas de Fred y George?"],
        ["1) Emporio de bromas Weasley"], 
        ["2) Weasleys 'Wizard Wheezes"],
        ["3) Fred & George's Wonder Emporium "],
        ["4) Tienda de bromas de Zonko"]]

imprime_matriz(matriz)
respuesta=int (input())
correcta=2
cont,texto=pregunta(respuesta, correcta,cont)
print (texto)
#pregunta 3
matriz=[["C. ¿Cuál de estos NO es una de las maldiciones imperdonables?"],
        ["1) Sectumsempra"], 
        ["2) Maldición Cruciatus"],
        ["3) Avada Kedavra "],
        ["4) Maldición Imperius"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta=1
cont,texto=pregunta(respuesta, correcta,cont)
print (texto)
#pregunta 4
matriz=[["D. ¿Quién interpretó a Lord Voldemort en las películas?"],
        ["1) Jeremy Irons"], 
        ["2) Tom Hiddleston"],
        ["3) Gary Oldman "],
        ["4) Ralph Fiennes"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta=4
cont,texto=pregunta(respuesta, correcta,cont)
print (texto)
#pregunta 5
matriz=[["E. ¿Quién vigila la entrada a la sala común de Gryffindor?"],
        ["1) La dama gris"], 
        ["2) La señora gorda"],
        ["3) El fraile gordo"],
        ["4) El barón sangriento"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta=2
cont,texto=pregunta(respuesta, correcta,cont)
print (texto) 
promedio=(cont*100)/5
print (promedio)
print(fan(promedio))
print()
#Casas de Howards preguntas
#Pregunta 1.1
matriz=[["A. ¿Cual de estas caracteriticas crees que te define mejor?"],
        ["1) Lealtad "], 
        ["2) Inteligencia "],
        ["3) Ambición"],
        ["4) Valentia "]]
imprime_matriz(matriz)
respuesta=int (input())
correcta1=3
correcta2=2
correcta3=1
correcta4=4
cont=0
cont,texto=pregunta_1(respuesta, correcta1, correcta2, correcta3, correcta4, cont)
print (texto)
#Pregunta 2.1
matriz=[["B. ¿Donde preferirias que tu dormitorio estuviese?"],
        ["1) En las mazmorras "], 
        ["2) En la torre del castillo"],
        ["3) Cerca de la cocina "],
        ["4) En el centro del castillo"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta1=1
correcta2=2
correcta3=3
correcta4=4
cont,texto=pregunta_1(respuesta, correcta1, correcta2, correcta3, correcta4, cont)
print (texto)
#Pregunta 3.1
matriz=[["C. ¿Cuál de estas asignaturas escogerias?"],
        ["1) Posiciones "], 
        ["2) Transformaciones"],
        ["3) Historia de la magia"],
        ["4) Astronomia"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta1=2
correcta2=4
correcta3=1
correcta4=3
cont,texto=pregunta_1(respuesta, correcta1, correcta2, correcta3, correcta4, cont)
print (texto)
#Pregunta 4.1
matriz=[["D. ¿Alguna vez has copiado?"],
        ["1) Si, todos lo hacen "], 
        ["2) NO"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta1=1
correcta2=4
correcta3=3
correcta4=2
cont=0
cont,texto=pregunta_1(respuesta, correcta1, correcta2, correcta3, correcta4, cont)
print (texto)
#Pregunta 5.1
matriz=[["E. ¿Que color te gusta mas?"],
        ["1) Rojo"], 
        ["2) Amarillo"],
        ["3) Azul"],
        ["4) Verde"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta1=4
correcta2=3
correcta3=2
correcta4=1
cont,texto=pregunta_1(respuesta, correcta1, correcta2, correcta3, correcta4, cont)
print (texto)
#Pregunta 6.1
matriz=[["F. Si jujugaras Quidditch ¿Cuál crees que seria tu rol en el equipo?"],
        ["1) Cazador/a"], 
        ["2) Golpeador/a"],
        ["3) Guardian/a"],
        ["4) Buscador/a"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta1=2
correcta2=4
correcta3=1
correcta4=3
cont,texto=pregunta_1(respuesta, correcta1, correcta2, correcta3, correcta4, cont)
print (texto)
#Pregunta 7.1
matriz=[["G. Te miras en el espejo de oesed y ves tu futuro ¿Cómo te ves?"],
        ["1) Con mucho dinero"], 
        ["2) Rodeado de mis seres queridos"],
        ["3) Siendo alguien importante en howards"],
        ["4) Viviendo una increible aventura"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta1=1
correcta2=3
correcta3=2
correcta4=4
cont,texto=pregunta_1(respuesta, correcta1, correcta2, correcta3, correcta4, cont)
print (texto)
#Pregunta 8.1
matriz=[["H.¿Que harias una vez terminaste tus estudios de Howards?"],
        ["1) Tendria una familia"], 
        ["2) Me uniria al ministerio de magia"],
        ["3) Seguiria estudiando"],
        ["4) Me iria de viaje"]]
imprime_matriz(matriz)
respuesta=int (input())
correcta1=1
correcta2=3
correcta3=2
correcta4=4
cont,texto=pregunta_1(respuesta, correcta1, correcta2, correcta3, correcta4, cont)
print (texto)
#Casa de Howards segun tus puntuaciones
print(cont)
print(casa(cont))


