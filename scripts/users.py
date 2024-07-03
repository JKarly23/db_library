import random
import string
from db.data import usernames, user_type, list_special,calles,ciudades,paises
from db.connection import connection

class User:
    
    def modificar_id(self,cursor) -> None:
        try:
            cursor.execute("SELECT user_id FROM users ORDER BY user_id ASC")
            users = cursor.fetchall()
            cont = 1
            for u in users:
                user_id = u[0]
                cursor.execute("UPDATE users SET user_id = %s WHERE user_id = %s", (cont, user_id))
                cont += 1
            connection.commit()
        except Exception as e:
            print({"Error": e})

    def generar_password(self) -> str:
        caracteres:str = string.ascii_letters + string.digits
        longitud:int = random.randint(8, 12)
        password:str = ''.join(random.choices(caracteres, k=longitud))
        return password

    def llenar_users(self,cursor)-> None:
        cont:int = 0
        try:
            for i in range(120):
                username:str = random.choice(list_special)+ random.choice(usernames) + str(random.randint(1, 100))
                password:str = self.generar_password()
                email:str = f"{username}@gmail.com"
                tipo_user:str = random.choice(user_type)
              
                cursor.execute("SELECT username FROM users")
                usernameList = cursor.fetchall()
            
                if any(username in row for row in usernameList):
                    continue
                else:
                    cursor.execute('''INSERT INTO Users (username, password, email, user_type) VALUES (%s, %s, %s, %s)''',
                           (username, password, email, tipo_user))
                    cont += 1
            connection.commit()
        
        except Exception as e:
            print("Ha ocurrido un error:", e)
        
        else:
            print("Se insertaron ",cont, "nuevos usurios")

    def get_comprador(self,cursor) -> None:
        try:
            cursor.execute("SELECT user_id FROM USERS WHERE user_type = 'comprador'")
            compradores = cursor.fetchall()
            cont:int = 1
        
            for c in compradores:
                user_id = int(c[0]) 
                cursor.execute('''INSERT INTO compradores (comprador_id,user_id) VALUES (%s,%s)''', (cont,user_id,))
                cont += 1  
            connection.commit()  
        except Exception as e:
            print({"Error": e})

    def llenar_ciudades(self,cursor)-> None:
        try:
            for i in range(1,1013):
                cursor.execute('''INSERT INTO direcciones (user_id, calle, ciudad, pais) VALUES (%s, %s, %s, %s)''',
                           (i, random.choice(calles), random.choice(ciudades), random.choice(paises)))
            connection.commit()    
        except Exception as e:
            print({"Error":e})



    
    
    
    
 




