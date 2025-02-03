import psycopg2
from db import config
import checkPartnerData

class Database():
    def __init__(self):
        self.connection = self.connect_db()

    def connect_db(self):
        try:
            connection = psycopg2.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.db_name
            )
            print("Соединение с базой данных установлено")
            return connection
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
            return None

    def take_partner_information(self):
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT partners_type, partners_name, partners_director, partners_email, partners_phone, partners_ur_adress, partners_inn, partners_rate
            FROM partners_import
            """

            cursor.execute(query)
            partners = [
                {
                    "type": row[0],
                    "name": row[1],
                    "director": row[2],
                    "email": row[3],
                    "phone": row[4],
                    "ur_adress": row[5],
                    "inn": row[6],
                    "rate": row[7]
                }
                for row in cursor.fetchall()
            ]
            cursor.close()
            return partners
        except Exception as e:
            return []

    def sale_sum(self, partners_name : str):
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()

            query = f"""
            select sum(partner_products_count)
            from partner_products_import
            where partner_name_fk = '{partners_name}'
            """
            cursor.execute(query, {partners_name})

            sales_data = [
                {
                    "procent": row[0]
                }
                for row in cursor.fetchall()
            ]

            cursor.close()
            return sales_data

        except Exception as e:
            return []

    def partner_add_function(self, partners_data: dict):
        if not self.connection:
            return False
        if not checkPartnerData.main_func(partners_data):
            return False
        try:
            cursor = self.connection.cursor()
            query = f'''
            INSERT INTO partners_import
            Values (%s, %s, %s, %s, %s, %s, %s, %s)
            '''
            values = (
                partners_data["type"],
                partners_data["name"],
                partners_data["director"],
                partners_data["mail"],
                partners_data["phone"],
                partners_data["ur_addr"],
                partners_data["inn"],
                partners_data["rate"],
            )

            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Партнер добавлен")
            return True
        except Exception:
            return False


    def update_partner_info_func(self, partner_name: str, partner_data: dict):
        ''' Функция обновления инфмации партнера '''

        if not self.connection:
            return False
        if not checkPartnerData.main_func(partner_data):
            return False
        try:
            cursor = self.connection.cursor()

            query = f'''
            Update partners_import
            set
            partners_type = '{partner_data["type"]}',
            partners_name = '{partner_data["name"]}',
            partners_phone = '{partner_data["phone"]}',
            partners_inn = '{partner_data["inn"]}',
            partners_rate = '{partner_data["rate"]}',
            partners_ur_adress = '{partner_data["ur_addr"]}',
            partners_email = '{partner_data["mail"]}',
            partners_director = '{partner_data["director"]}'
            
            where partners_name = '{partner_name}';
            '''

            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    def take_current_partner_info(self, partner_name: str):
        if not self.connection:
            return []

        try:
            cursor = self.connection.cursor()
            query = f'''
            SELECT partners_name, partners_phone, partners_type, partners_email,
            partners_ur_adress, partners_inn, partners_rate, partners_director
            FROM partners_import
            where partners_name = '{partner_name}'
            '''

            cursor.execute(query)

            partner_data = []
            for row in cursor.fetchall():
                partner_data.append({
                    "name": row[0].strip(),
                    "phone": row[1].strip(),
                    "type": row[2].strip(),
                    "mail": row[3].strip(),
                    "ur_addr": row[4].strip(),
                    "inn": row[5].strip(),
                    "rate": row[6],
                    "director": row[7].strip(),
                })
            cursor.close()
            return partner_data

        except Exception:
            return []

    def get_history(self, partnername: str):
        if not self.connection:
            print("Нет соединения с базой данных.")
            return []

        try:
            cursor = self.connection.cursor()
            query = """
                    SELECT 
                        p.product_import_name AS productname,
                        pr.partners_name AS partnername,
                        h.partner_products_count AS quantity,
                        h.partners_sale_date AS saledate
                    FROM 
                        partner_products_import h
                    JOIN 
                        products_import p ON h.partner_product_name_fk = p.product_import_name
                    JOIN 
                        partners_import pr ON h.partner_name_fk = pr.partners_name
                    WHERE 
                        pr.partners_name = %s;
                """

            cursor.execute(query, (partnername,))
            history = [
                {
                    "productname": row[0].strip(),
                    "partnername": row[1].strip(),
                    "quantity": row[2],
                    "saleDate": row[3]
                }
                for row in cursor.fetchall()
            ]

            cursor.close()
            return history
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            return []