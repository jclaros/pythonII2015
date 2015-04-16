__author__ = 'jonathan'


class Animal:
    _nombre = None
    _altura = 0
    _peso = 0
    _sonido = 0

    def __init__(self, nombre, altura, peso, sonido):
        self._nombre = nombre
        self._altura = altura
        self._peso = peso
        self._sonido = sonido

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura

    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso

    def get_sonido(self):
        return self._sonido

    def set_sonido(self, sonido):
        self._sonido = sonido

    def to_string(self):
        return "Hola mi nombre es: {}, mi peso es: {}, mido: {}, y digo: {}".format(
            self._nombre,
            self.get_peso(),
            self.get_altura(),
            self.get_sonido()
        )



#animal = Animal("Tom", 20, 7, "miau")
#print(animal.to_string())

class Perro(Animal):
    __responsable = ""

    def __init__(self, nombre, altura, peso, sonido, responsable):
        self.__responsable = responsable
        super(Perro, self).__init__(nombre, altura, peso, sonido)

    def get_responsable(self):
        return self.__responsable

    def set_responsable(self, responsable):
        self.__responsable = responsable

    def to_string(self):
        return super(Perro, self).to_string() + " y mi dueño es: {}".format(self.__responsable)




perro1 = Perro("Choco", 40, 10, "guau", "Jon")
print(perro1.to_string())




#http://ctabustracker.com/bustime/map/getBusesForRouteAll.jsp







