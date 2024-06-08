'''
EJERCICIO 3: CREAR UN JUEGO DE FUSION

se consiste en crear personajes, un juego y que esos personajes se fusionen para formar personajes mas poderosos

para ello debemos cambiar el comportamiento del operador (+) para cuando los personajes se fusionen, salga
un nuevo personaje con habilidades mejoradas

una posible formula: el promedio de las habilidades de ambos al cuadrado
'''

#creo clase
class Personaje:
    def __init__ (self,nombre,fuerza,velocidad):
        #definimos los atributos de instancia
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    #Representamos el objeto
    def __repr__(self):
        return f'{self.nombre}, (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'

    #Metodo para habilitar la suma
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + '-' + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34) #=> Para el promedio, sumar los factores y dividirlos por la cant del mismo
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        #retornamos el personaje con sus nuevas habilidades
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    
thanos = Personaje('Thanos',90,40)
hulk = Personaje('Hulk',70,50)

fusion = thanos + hulk
print(fusion)


#OTRO EJERCICIO DE FUSION PERO DE SUELDOS XD
