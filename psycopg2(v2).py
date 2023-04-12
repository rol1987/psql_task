import psycopg2


#Функция, создающая структуру БД (таблицы).
def new_table(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
    ID SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    surname VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    phone_number_1 VARCHAR(20),
    phone_number_2 VARCHAR(20),
    phone_number_3 VARCHAR(20),
    phone_number_4 VARCHAR(20)
    );
    """)
    
#Функция, позволяющая добавить нового клиента.
def add_client(cur, name, surname, email, phone_number_1, phone_number_2, phone_number_3, phone_number_4):
    cur.execute("""
    INSERT INTO clients(name, surname, email, phone_number_1, phone_number_2, phone_number_3, phone_number_4) VALUES(%s, %s, %s, %s, %s, %s, %s);
    """, (name, surname, email, phone_number_1, phone_number_2, phone_number_3, phone_number_4))
    
# Функция, позволяющая добавить телефон для существующего клиента.
def add_telephone_number(cur, tel_number, id):
    cur.execute("""
    UPDATE clients SET phone_number_3=%s WHERE id=%s and phone_number_3 = '';
    """, (tel_number, id))

# Функция, позволяющая изменить данные о клиенте.
def change_client(cur, name, surname, email, phone_number_1, phone_number_2, phone_number_3, phone_number_4, id):
    cur.execute("""
    UPDATE clients SET name=%s WHERE id=%s;
    """, (name, id))
    cur.execute("""
    UPDATE clients SET surname=%s WHERE id=%s;
    """, (surname, id))
    cur.execute("""
    UPDATE clients SET email=%s WHERE id=%s;
    """, (email, id))
    cur.execute("""
    UPDATE clients SET phone_number_1=%s WHERE id=%s;
    """, (phone_number_1, id))
    cur.execute("""
    UPDATE clients SET phone_number_2=%s WHERE id=%s;
    """, (phone_number_2, id))
    cur.execute("""
    UPDATE clients SET phone_number_3=%s WHERE id=%s;
    """, (phone_number_3, id))
    cur.execute("""
    UPDATE clients SET phone_number_4=%s WHERE id=%s;
    """, (phone_number_4, id))
   

#  Функция, позволяющая удалить телефон для существующего клиента.
def del_telephone_number(cur, id):
    cur.execute("""
    UPDATE clients SET phone_number_1=%s WHERE id=%s;
    """, ('', id))

# Функция, позволяющая удалить существующего клиента.
def del_client(cur, id, tel_number):
    cur.execute("""
    DELETE FROM clients WHERE id=%s and phone_number_3=%s;
    """, (id, tel_number))

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
def find_client(cur, name, phone_number, email):
    cur.execute("""
    SELECT id FROM clients WHERE (name like %s) and phone_number_1 like %s and email like %s;
    """, (name, phone_number, email))
    print(cur.fetchall())


if __name__ == "__main__":
    conn = psycopg2.connect(database = 'netology_db', user = 'postgres', password = '83FrkWrt')
    with conn.cursor() as cur:
        table = new_table(cur)
        cl = add_client(cur, 'Oleg', 'Olegov', 'xxx@yandex.ru', '+7929123123445', '+79976543210', '', '')
        tel = add_telephone_number(cur, "78978978", 44)
        change = change_client(cur, "Petr", "GAGARIN", 'gagarin@yandex.ru', '111', '222', '333', '444', 20) 
        del_tel_num = del_telephone_number(cur, 14)
        del_cl = del_client(cur, 44, '78978978')
        find_cl = find_client(cur, 'Petr', '%11%', '%gaga%')
    conn.commit()
    conn.close()