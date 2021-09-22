from vistas import Login
from modelo import ConectorDB

if __name__ == '__main__':

    crear_base = ConectorDB()
    email_validado = Login().login()
    Login().menu(email_validado)
