import mysql.connector
import pytest

def conectar_base_de_datos():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="products"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def contar_fechas_validas():
    conn = conectar_base_de_datos()
    if conn is None:
        return 0
    cursor = conn.cursor()
    query = """
    SELECT COUNT(*) 
    FROM `ventas` 
    WHERE fecha_venta REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$'
    """
    cursor.execute(query)
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado

def test_contar_fechas_formato_valido():
    cantidad_esperada = 5853  # Sustituye esto con el valor que esperas
    cantidad_obtenida = contar_fechas_validas()
    assert cantidad_obtenida == cantidad_esperada, f"Se esperaban {cantidad_esperada} registros, pero se encontraron {cantidad_obtenida}"
