"""
Script para leer el CSV de data y almacenar en la base de datos
"""
import csv
from base_datos import conn

cursor = conn.cursor()

with open('./data/info.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    # ignorar la primera fila del CSV que contiene los nombres de las columnas
    next(data)
    for row in data:
        nombre = row[0]
        apellido = row[1]
        cedula = row[2]
        edad = int(row[3])
        cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
        VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)
        cursor.execute(cadena_sql)

conn.commit()
cursor.close()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()