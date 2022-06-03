class Persona:
    def __init__(self, n, s):
        self.nombre = n
        self.universidad = s

    def print_nombre(self):
        print()
        self.nombre

    def print_universidad(self):
        print()
        self.universidad

jorge = Persona('Anthony Franco', 'Universidad Tecnica Particular de Loja')

jorge.print_nombre()
jorge.print_universidad()