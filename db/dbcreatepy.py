import psycopg2
import config


def create_table_partners(connection_string):

    query = '''
    create table partners_import (
    partners_type nchar(3) not null,
    partners_name nchar(50) primary key not null,
    partners_director nchar(70) not null,
    partners_email nchar(100) not null,
    partners_phone nchar(13) not null,
    partners_ur_adress nchar(300) not null,
    partners_inn nchar(10) not null,
    partners_rate int not null
    );
    '''
    cursor_to_work_with_db = connection_string.cursor()

    cursor_to_work_with_db.execute(query)

    cursor_to_work_with_db.close()

    connection_string.commit()

def create_table_product_type(connection_string):
    query = '''
    create table product_type_import (
    product_type_name nchar(30) primary key not null,
    product_type_kef real not null
    );
    '''
    cursor_to_work_with_db = connection_string.cursor()

    cursor_to_work_with_db.execute(query)

    cursor_to_work_with_db.close()

    connection_string.commit()

def create_table_products(connection_string):
    query = '''
     create table products_import (
     products_import_name_fk nchar(50) not null,
     FOREIGN KEY (products_import_name_fk) REFERENCES product_type_import(product_type_name),
     product_import_name nchar(250) primary key not null,
     products_import_articul bigint not null,
     products_minimal_cost real not null
    );
    '''
    cursor_to_work_with_db = connection_string.cursor()

    cursor_to_work_with_db.execute(query)

    cursor_to_work_with_db.close()

    connection_string.commit()

def create_table_partner_products(connection_string):
    query = '''
    create table partner_products_import (
    partner_product_name_fk nchar(250) not null,
    FOREIGN KEY (partner_product_name_fk) REFERENCES products_import (product_import_name),
    partner_name_fk nchar(50) not null,
    FOREIGN KEY (partner_name_fk) REFERENCES partners_import (partners_name),
    partner_products_count bigint not null,
    partners_sale_date date not null
    );
    '''
    cursor_to_work_with_db = connection_string.cursor()

    cursor_to_work_with_db.execute(query)

    cursor_to_work_with_db.close()

    connection_string.commit()

def create_table_material_type(connection_string):
    query = '''
    create table material_type_import (
    material_type nchar(50) not null primary key,
    material_percent_brack nchar(7) not null
    );
    '''
    cursor_to_work_with_db = connection_string.cursor()

    cursor_to_work_with_db.execute(query)

    cursor_to_work_with_db.close()

    connection_string.commit()


def start():
    database_connection_string = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db_name
    )
    create_table_partners(database_connection_string)
    create_table_product_type(database_connection_string)
    create_table_products(database_connection_string)
    create_table_partner_products(database_connection_string)
    create_table_material_type(database_connection_string)
    print("DONE")


start()