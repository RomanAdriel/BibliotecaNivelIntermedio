"""Este módulo es el modelo que inicializa la base de datos"""
import mysql.connector
from datos import queries
from datos import mensajes
import sys

"""Esta la clase que inicializa la base de datos. Contiene dos funciones, una para levantar la base, la otra
para completarla con datos"""


class ConectorDB:
    """Esta la clase que inicializa la base de datos"""
    def __init__(
        self,

    ):
        self.conexion = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="DiplomaturaPython09!",
            auth_plugin="caching_sha2_password"
        )
        self.crear_db()
        self.rellenar_db()
        pass

    def crear_db(self):
        try:

            cursor = self.conexion.cursor()

            cursor.execute(queries["DROP_BASE"])

            cursor.execute(queries["CREAR_BASE"])

            cursor.execute(queries["USAR_BASE"])

            cursor.execute(queries["CREAR_TABLA"])

        except (ConnectionRefusedError, mysql.connector.errors.InterfaceError):
            sys.exit(mensajes["SERVIDOR_APAGADO"])

    def rellenar_db(self):
        try:

            cursor = self.conexion.cursor()

            query_valores = [
                ("1000-2000", "Crimen y Castigo", "Fyodor Dostoyevsky", 2014, "Alianza", "Español", "Tapa blanda", 100,
                 "roman", "roman"),
                ("1000-3000", "How The World Works", "Noam Chomsky", 2018, "Penguin", "Inglés", "Tapa blanda", 300,
                 "roman",
                 "roman"),
                ("1000-4000", "La Revolución Rusa (1891-1924)", "Orlando Figes", 2012, "Edhasa", "Español",
                 "Tapa blanda",
                 400, "roman", "roman"),
                ("1000-5000", "El Aleph", "Jorge Luis Borges", 2013, "De Bolsillo", "Español", "Tapa blanda", 200,
                 "roman",
                 "roman"),
                ("1000-6000", "Corazón de Perro", "Mihail Bulgakov", 2010, "Gutenberg", "Español", "Tapa dura", 600,
                 "roman", "roman"),
                ("1000-7000", "Aguafuertes Porteñas", "Roberto Arlt", 2008, "Edicol", "Español", "Tapa blanda", 150,
                 "roman", "roman"),
                ("1000-8000", "Madame Bovary", "Gustave Flaubert", 2007, "Tusquets", "Español", "Tapa blanda", 180,
                 "roman",
                 "roman"),
                ("1000-9000", "Leviatán", "Thomas Hobbes", 2009, "Fondo de Cultura Económica", "Español", "Tapa dura",
                 300,
                 "roman", "roman"),
                ("1000-1900", "El Lobo Estepario", "Hermann Hesse", 2005, "Losada", "Español", "e-book, azw3", 1000,
                 "roman", "roman"),
                ("1000-1800", "Cartero", "Charles Bukowski", 2014, "Octaedro", "Español", "Tapa blanda", 810, "roman",
                 "roman")]

            cursor.execute(queries["USAR_BASE"])

            cursor.executemany(queries["INSERTAR_LIBRO"], query_valores)
            self.conexion.commit()

        except (ConnectionRefusedError, mysql.connector.errors.InterfaceError):
            sys.exit(mensajes["SERVIDOR_APAGADO"])

    def crear_cursor(self):

        try:

            cursor = self.conexion.cursor()

            return cursor, self.conexion

        except (ConnectionRefusedError, mysql.connector.errors.InterfaceError):
            sys.exit(mensajes["SERVIDOR_APAGADO"])
