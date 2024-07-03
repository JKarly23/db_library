from db.connection import connection
from db.data import categorias,categorias_libros,comentarios_libro
import datetime
import random


class Library:
    
    def modificar_id(self,cursor) -> None:
        try:
            cursor.execute("SELECT reseña_id FROM reseñas ORDER BY reseña_id ASC")
            reseñas = cursor.fetchall()
            cont = 1
            for u in reseñas:
                reseñas_id = u[0]
                cursor.execute("UPDATE reseñas SET reseña_id = %s WHERE reseña_id = %s", (cont, reseñas_id))
                cont += 1
            connection.commit()
        except Exception as e:
            print({"Error": e})
                 
    def categorias(self, cursor) -> None:
        cont: int = 0
        try:
            for nombre in categorias:
                cursor.execute("SELECT COUNT(*) FROM categorias WHERE nombre = %s", (nombre,))
                if cursor.fetchone()[0] == 0:
                    cursor.execute("INSERT INTO categorias (nombre) VALUES (%s)", (nombre,))
                    cont += 1
            connection.commit()        
            print(f"{cont} categorías insertadas.")
        except Exception as e:
            print({"Error": e})

    def libros(self, cursor) -> None:
        try:
            fecha_inicio = datetime.date(1900, 1, 1)
            fecha_fin = datetime.date(2023, 12, 31)
            cont_categoria = 1
            for categoria, libros in categorias_libros.items():
                for nombre_libro in libros:
                    nombre, autor = nombre_libro.split(" - ")
                    diferencia_dias = (fecha_fin - fecha_inicio).days
                    dias_aleatorios = random.randint(0, diferencia_dias)
                    fecha_publicacion = fecha_inicio + datetime.timedelta(days=dias_aleatorios)
                    
                    cursor.execute("INSERT INTO libros (titulo, autor, fecha_publicacion, precio, stock, categoria_id) VALUES (%s, %s, %s, %s, %s, %s)",
                                   (nombre.strip(), autor.strip(), fecha_publicacion, random.randint(200, 1200), cont_categoria, cont_categoria))
                    
                cont_categoria += 1
                
            connection.commit()
            print("Libros insertados correctamente.")
        
        except Exception as e:
            print(f"Ha ocurrido un error durante la inserción de libros: {e}")
            
    def ventas(self,cursor) -> None:
        try:
            fecha_inicio = datetime.date(2000, 1, 1)
            fecha_fin = datetime.date(2024, 7, 3)
            cursor.execute("Select vendedor_id from vendedores")
            vendedor = cursor.fetchall()
            for i in vendedor:
                diferencia_dias = (fecha_fin - fecha_inicio).days
                dias_aleatorios = random.randint(0, diferencia_dias)
                fecha_venta = fecha_inicio + datetime.timedelta(days=dias_aleatorios)
                id = int(i[0])
                cursor.execute("INSERT INTO ventas (vendedor_id, fecha_venta, total) VALUES (%s,%s,%s)",
                           (id,fecha_venta,random.randint(3,6)))
            connection.commit()             
        except Exception as e:
            print({"Error": e})    
    
    def compra(self, cursor) -> None: 
        try:
            cursor.execute("SELECT fecha_venta FROM ventas")
            fechas = cursor.fetchall()
            fechas_venta = [fecha[0] for fecha in fechas]

            for i in range(1,500):
                 # Obtener la cantidad total de libros vendidos en una fecha
                cursor.execute("SELECT total FROM ventas WHERE fecha_venta = %s", (fechas_venta[i],))
                total = cursor.fetchone()[0] 
                if total is None:
                    total = 0

                cursor.execute("INSERT INTO compras (comprador_id, fecha_compra, total) VALUES (%s, %s, %s)",
                           (i, fechas_venta[i], total))
        
            connection.commit()
            print("Inserción de compras completada.")

        except Exception as e:
            print(f"Error al procesar compras: {e}")
            connection.rollback()
            
    def resenna(self, cursor) -> None:
        
        try:
            fecha_inicio = datetime.date(2000, 1, 1)
            fecha_fin = datetime.date(2024, 7, 3)
            
            cursor.execute("SELECT user_id FROM compradores")
            users = cursor.fetchall()
            user_id = [user[0] for user in users]

            cursor.execute("SELECT libro_id FROM libros")
            libros = cursor.fetchall()
            libros_id = [libro[0] for libro in libros]

            for id in user_id:                
                diferencia_dias = (fecha_fin - fecha_inicio).days
                dias_aleatorios = random.randint(0, diferencia_dias)
                fecha = fecha_inicio + datetime.timedelta(days=dias_aleatorios)

                calificacion = random.randint(1, 4)
                comentario = comentarios_libro[calificacion]  

                cursor.execute("INSERT INTO reseñas (libro_id, user_id, calificacion, comentario, fecha) VALUES (%s, %s, %s, %s, %s)",
                           (random.choice(libros_id), id, calificacion, comentario, fecha))

            connection.commit()
            print("Reseñas insertadas correctamente.")

        except Exception as e:
            print({"Error": e})

    def detalles_compra(self, cursor) -> None:
        try:
            cursor.execute("SELECT libro_id FROM libros")
            libros = cursor.fetchall()
            libros_id = [libro[0] for libro in libros]

            for i in range(2, 500):
                libro = random.choice(libros_id)
                cantidad = random.randint(1, 10)  

                cursor.execute("SELECT precio FROM libros WHERE libro_id = %s", (libro,))
                precio = cursor.fetchone()

                if precio is None:
                    print(f"No se encontró el precio para el libro con ID {libro}.")
                    continue

                precio_unitario = precio[0] * cantidad  

                cursor.execute("INSERT INTO detallescompra (compra_id, libro_id, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)",
                           ((i), libro, cantidad, precio_unitario))

            connection.commit()
            print("Detalles de compra insertados correctamente.")
        except Exception as e:
            print({"error": e})

    def detalles_ventas(self, cursor) -> None:
        
        try:
            cursor.execute("SELECT libro_id FROM libros")
            libros = cursor.fetchall()
            libros_id = [libro[0] for libro in libros]

            for i in range(1, 500):
                libro = random.choice(libros_id)
                cantidad = random.randint(1, 10)  

                cursor.execute("SELECT precio FROM libros WHERE libro_id = %s", (libro,))
                precio = cursor.fetchone()

                if precio is None:
                    print(f"No se encontró el precio para el libro con ID {libro}.")
                    continue

                precio_unitario = precio[0] * cantidad  

                cursor.execute("INSERT INTO detallesventa (venta_id, libro_id, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)",
                           ((i), libro, cantidad, precio_unitario))

            connection.commit()
            print("Detalles de venta insertados correctamente.")
        except Exception as e:
            print({"error": e})
        
                      
       
             
