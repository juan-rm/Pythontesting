class Coches():
    def __init__(self, marca,tipo):
        self.marca = marca
        self.tipo = tipo
        self.odometer = 0

    def actualizar_odometer(self):
        odometro = input("introduzca el valor del odometro actual ")
        odometro = int(odometro)
        if self.odometer < odometro:
            self.odometer = odometro
            print(f"el valor del odometro es {self.odometer}, valor actualizado")
        else:
            print("El valor introducido es menor que el del odometro, no es valido")

    def incrementar_odometer(self):
        odometro_1 = input("introduzca el incremento en el valor del odometro ")
        odometro_1 = int(odometro_1)
        self.odometer += odometro_1
        print(f"El nuevo valor del odometro es {self.odometer}")

class Coches_Electricos(Coches):
    def __init__(self, marca, tipo, tecnologia, battery):
        super().__init__(marca, tipo)
        self.tecnologia = tecnologia
        self.battery = battery

class Bateria():
     def __init__(self, potencia =150,duracion= 24):
        self.potencia = potencia
        self.duracion = duracion


#coche_nuevo = Coches("audi" , "A5")
#coche_nuevo.actualizar_odometer()
#coche_nuevo.incrementar_odometer()
bateria_tesla = Bateria(150, 24)
tesla = Coches_Electricos("tesla", "model3" , "electrico_puro",bateria_tesla)
#print(f"el nuevo coche que me he comprado es un {tesla.marca} y usa tecnologia {tesla.tecnologia}")
#tesla.actualizar_odometer()
print(f"la potencia de la bateria de mi coche {tesla.marca} es {tesla.battery.potencia}")