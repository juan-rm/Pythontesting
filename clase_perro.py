class Perro():
    def __init__(self, nombre, edad):
        """definicion de la funcion"""
        self.nombre = nombre
        self.edad = edad
    
    def rollover(self):
        print("El perro de nombre " + self.nombre + " Da la vuelta sobre si mismo")

    def salto(self):
        print("El perro de nombre " + self.nombre + "salta")


perrito = Perro("archie" , 12)

print("el nombre de mi perro es " +  perrito.nombre.title())
perrito.rollover()