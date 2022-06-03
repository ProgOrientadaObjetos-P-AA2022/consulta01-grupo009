class Persona():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def nombre(self, valor):
        self.id = valor

    def id(self):
        return self.id

    def nombre(self, valor):
        self.nombre = valor

    def id(self):
        return self.nombre

    def __str__(self):
        return 'Nombre: ' + str(self.nombre)+print()+\
               ' Cedula: ' + str(self.id)



p1 = Persona(1189653585, 'Anthony Franco')
p2 = Persona(1175984565, 'Brayan Alvear')
print(p1)
print()
print(p2)
