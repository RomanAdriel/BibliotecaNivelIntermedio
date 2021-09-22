"""
Módulo PRINCIPAL:

    Este módulo se encarga de inicializar el sistema, creando la base de datos y abriendo la consola.
    El programa inicia desde este punto.
"""
from vistas import Login
from modelo import ConectorDB

if __name__ == '__main__':

    crear_base = ConectorDB()
    email_validado = Login().login()
    Login().menu(email_validado)
