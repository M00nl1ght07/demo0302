import pandas as pd
import psycopg2
from config import *
from db.database import Database

def partners_import(table_name: str, database):
    df = pd.read_excel("../excel/" + table_name, engine='openpyxl')
    query = """INSERT INTO partners_import VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    cursor = database.cursor()
    for line in df.itertuples():
        partners_type = line._1
        partners_name = line._2
        partners_director = line.Директор
        partners_email = line._4
        partners_phone = line._5
        partners_ur_adress = line._6
        partners_inn = line.ИНН
        partners_rate = line.Рейтинг

        values = (partners_type,
                  partners_name,
                  partners_director,
                  partners_email,
                  partners_phone,
                  partners_ur_adress,
                  partners_inn,
                  partners_rate)
        cursor.execute(query, values)

    database.commit()
    cursor.close()

def product_type_import(table_name: str, database):
    query = """INSERT INTO product_type_import VALUES (%s, %s)"""
    df = pd.read_excel("../excel/" + table_name, engine='openpyxl')
    cursor = database.cursor()
    for line in df.itertuples():
        product_type_name = line._1
        product_type_kef = line._2

        values = (product_type_name,
                  product_type_kef)

        cursor.execute(query, values)

    database.commit()
    cursor.close()


def products_import(table_name: str, database):
    query = """INSERT INTO products_import VALUES (%s, %s, %s, %s)"""
    df = pd.read_excel("../excel/" + table_name, engine='openpyxl')
    cursor = database.cursor()
    for line in df.itertuples():
        products_import_name_fk = line._1
        product_import_name = line._2
        products_import_articul = line.Артикул
        products_minimal_cost = line._4

        values = (products_import_name_fk,
                  product_import_name,
                  products_import_articul,
                  products_minimal_cost)
        cursor.execute(query, values)

    database.commit()
    cursor.close()


def partner_products_import(table_name: str, database):
    query = """INSERT INTO partner_products_import VALUES (%s, %s, %s, %s)"""
    df = pd.read_excel("../excel/" + table_name, engine='openpyxl')
    cursor = database.cursor()
    for line in df.itertuples():
        partner_product_name_fk = line.Продукция
        partner_name_fk = line._2
        partner_products_count = line._3
        partners_sale_date = line._4

        values = (partner_product_name_fk,
                  partner_name_fk,
                  partner_products_count,
                  partners_sale_date)
        cursor.execute(query, values)

    database.commit()
    cursor.close()

def material_type_import(table_name: str, database):
    query = """INSERT INTO material_type_import VALUES (%s, %s)"""
    df = pd.read_excel("../excel/" + table_name, engine='openpyxl')
    cursor = database.cursor()
    for line in df.itertuples():
        material_type = line._1
        material_percent_brack = line._2

        values = (material_type,
                  material_percent_brack)
        cursor.execute(query, values)

    database.commit()
    cursor.close()

def insert_table():
    database = Database().connect_db()

    partners_import("Partners_import.xlsx", database)
    product_type_import("Product_type_import.xlsx", database)
    products_import("Products_import.xlsx", database)
    partner_products_import("Partner_products_import.xlsx", database)
    material_type_import("Material_type_import.xlsx", database)

insert_table()