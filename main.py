from db.connection import cursor
from scripts.libros import Library
from scripts.users import User



if __name__ == "__main__":
    
    #user:User = User()
    #user.llenar_users(cursor)
    #user.get_comprador(cursor)
    #user.modificar_id(cursor)
    #user.llenar_ciudades(cursor)
    
    library:Library = Library()
    #library.categorias(cursor)
    #library.modificar_id(cursor)
    #library.libros(cursor)
    #library.ventas(cursor)
    #library.compra(cursor)
    #library.resenna(cursor)
    #library.detalles_compra(cursor)
    library.detalles_ventas(cursor)
    
 