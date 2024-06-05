"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""

class Persona:
    """
    Superclase Persona con apellidos, nombre y nif.

    Autor: Jorge Pradillo Hinterberger
    """
    apellidos = "Apellidos"
    nombre = "Nombre"
    nif = "11111111Z"

    def __init__(self):
        """
        Método constructor de la clase Persona. No recibe ni devuelve ningún parámetro.
        """
        pass

class Estudiante(Persona):
    """
    Clase estudiante que hereda de la clase persona. Además de los atributos de esta, también contiene el curso de la persona.

    Autor: Jorge Pradillo Hinterberger
    """
    curso = "Primaria"

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Método constructor de la clase estudiante.

        :param nif: Recibe el nif de la persona.
        :param curso: Recibe el curso de la persona.
        :param nombre: Recibe el nombre de la persona.
        :param apellidos: Recibe el apellido de la persona.
        """
        self.nif = nif
        self.curso = curso
        self.nombre = nombre
        self.apellidos = apellidos

    @property
    def nif(self):
        """
        Propiedad que almacena el nif de la persona.
        :return: El nif de la persona.
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Método que genera el nif de la persona.
        :param value: Recibe como valor el nif de la persona
        :return: Devuelve el valor que le hayamos dado.
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Propiedad que almacena el curso de la persona.
        :return: El curso de la persona.
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Método que genera el curso de la persona.
        :param value: Recibe como valor el curso de la persona.
        :return: Devuelve el valor que le hayamos dado.
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Propiedad que almacena el nombre de la persona.
        :return: El nombre de la persona.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Método que genera el nombre de la persona.
        :param value: Recibe como valor el nombre de la persona.
        :return: Devuelve el nombre de la persona.
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Propiedad que almacena el apellidos de la persona.
        :return: Los apellidos de la persona.
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Método que genera los apellidos de la persona.
        :param value: Recibe como valor los apellido de la persona.
        :return: Devuelve los apellido de la persona.
        """
        self.__apellidos = value
