import pytest
import pandas as pd
import logging

'''
@uthor: José Luis García Quinayás
date: 02/12/2024
github: https://github.com/iamjosel
contacto: iamjoseluisg@gmail.com
'''

'''
para ejecutar los casos

1. comando para generar el reporte de los casos de prueba ejecutados
pytest --html=report.html --self-contained-html

2. comando para ver los que pasaron, fallaron y logs
pytest -v --tb=short --log-cli-level=INFO

3. comando para ver los que pasaron, fallaron, logs y reporte html
pytest test_total_venta.py -v --tb=short --log-cli-level=INFO --html=report_total_venta.html --self-contained-html

'''

# Configurar logging para pytest en la consola
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función para cargar los datos
@pytest.fixture
def load_data():
    # Cargar los datos desde el archivo Excel
    data = pd.read_excel("O:/productos/ventas1.xlsx")
    return data

# Caso 1: Determinar el valor más alto en la columna 'total_venta'
def test_max_value_in_total_sale(load_data):
    '''Caso de prueba 1: Determinar cuál es el valor más alto registrado en la columna 'total_venta'.'''
    data = load_data
    data['total_venta'] = pd.to_numeric(data['total_venta'], errors='coerce')
    max_value = data['total_venta'].max()
    logger.info(f"El valor más alto en la columna 'total_venta' es: {max_value}")
    assert max_value > 0, "El valor más alto en 'total_venta' debe ser positivo."

@pytest.mark.parametrize("expected_count", [22914.7])
def test_exact_value_more_hight(load_data, expected_count):
    '''Caso 2: Asegurarse de que el valor más alto en la columna total_venta es 22914.7'''
    data = load_data
    data['total_venta'] = pd.to_numeric(data['total_venta'], errors='coerce')
    max_value = data['total_venta'].max()
    if max_value == expected_count:
        logger.info(f"Efectivamente el valor más alto en la columna 'total_venta' es: {max_value}")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {max_value}.")
        assert max_value == expected_count, (f"Se esperaba el valor {expected_count}, pero se encontró {max_value}.")

# Caso 3: Determinar el valor más bajo en la columna 'total_venta'
def test_min_value_in_total_sale(load_data):
    '''Caso de prueba 3: Determinar cuál es el valor más bajo registrado en la columna 'total_venta'.'''
    data = load_data
    data['total_venta'] = pd.to_numeric(data['total_venta'], errors='coerce')
    min_value = data['total_venta'].min()
    logger.info(f"El valor más bajo en la columna 'total_venta' es: {min_value}")
    assert min_value >= 0, "El valor más bajo en 'total_venta' no debe ser negativo."

@pytest.mark.parametrize("expected_count", [-4104288.13])
def test_exact_value_lower(load_data, expected_count):
    '''Caso 4: Asegurarse de que el valor más bajo en la columna total_venta es -4104288.13'''
    data = load_data
    data['total_venta'] = pd.to_numeric(data['total_venta'], errors='coerce')
    min_value = data['total_venta'].min()
    if min_value == expected_count:
        logger.info(f"Efectivamente se encontró que el valor más bajo en la columna 'total_venta' es: {min_value}")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {min_value}.")
        assert min_value == expected_count, (f"Se esperaba el valor {expected_count}, pero se encontró {min_value}.")

# Caso de prueba 5: Contar cuántos registros tienen valores positivos en la columna total_venta.
def test_count_positive_values_in_total_sale(load_data):
    '''Caso de prueba 5: Contar cuántos registros tienen valores positivos en la columna total_venta.'''
    data = load_data
    positive_values = data['total_venta'].apply(lambda x: pd.to_numeric(x, errors='coerce') > 0)
    positive_count = positive_values.sum()
    logger.info(f"Registros con valores positivos: {positive_count}")
    assert positive_count >= 0, "El conteo de valores positivos no es correcto."

# Caso de prueba 6: Asegurarse de que en la columna 'total_venta' la cantidad de registros positvios son: 5577
@pytest.mark.parametrize("expected_count", [5577])
def test_exact_count_positive_values_in_total_sale(load_data, expected_count):
    '''Caso de prueba 6: Asegurarse de que en la columna 'total_venta' la cantidad de registros positvios son: 5577'''
    data = load_data
    positive_values = data['total_venta'].apply(lambda x: pd.to_numeric(x, errors='coerce') > 0)
    positive_count = positive_values.sum()
    if positive_count == expected_count:
        logger.info(f"Efectivamente los registros con valores positivos en la columna total_venta son : {positive_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {positive_count}.")
        assert positive_count == expected_count, (f"Se esperaba que los valores positivos fuesen {expected_count}, pero se encontraron {positive_count}.")

def test_count_negative_values_in_total_sale(load_data):
    '''Caso de prueba 7: Contar cuántos registros tienen valores negativos en la columna total_venta.'''
    data = load_data
    negative_values = data['total_venta'].apply(lambda x: pd.to_numeric(x, errors='coerce') < 0)
    negative_count = negative_values.sum()
    logger.info(f"Registros con valores negativos: {negative_count}")
    assert negative_count >= 0, "El conteo de valores negativos no es correcto."

#Caso de prueba 8: Asegurarse de que en la columna 'total_venta' la cantidad de registros negativos son: 507
@pytest.mark.parametrize("expected_count", [507])
def test_count_exact_negative_values_in_total_sale(load_data, expected_count):
    '''Caso de prueba 8: Asegurarse de que en la columna 'total_venta' la cantidad de registros negativos son: 507'''
    data = load_data
    negative_values = data['total_venta'].apply(lambda x: pd.to_numeric(x, errors='coerce') < 0)
    negative_count = negative_values.sum()
    if negative_count == expected_count:
        logger.info(f"Efectivamente los registros con valores positivos en la columna total_venta son: {negative_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {negative_count}.")
        assert negative_count == expected_count, (f"Se esperaba que los valores positivos fuesen {expected_count}, pero se encontraron {negative_count}.")

# Caso 9: Confirmar que no existan valores nulos o vacíos en 'total_venta'
def test_no_null_or_empty_values_in_total_sale(load_data):
    '''Caso de prueba 9: Contar cuántos registros vacíos hay en la columna total_venta.'''
    data = load_data
    null_or_empty_count = data['total_venta'].isna().sum()
    logger.info(f"Valores nulos o vacíos en 'total_venta': {null_or_empty_count}")
    assert null_or_empty_count == 0, "Se encontraron valores nulos o vacíos en 'total_venta'."

@pytest.mark.parametrize("expected_count", [0])
def test_count_exact_or_empty_values_null_in_total_sale(load_data, expected_count):
    '''Caso de prueba 10: Asegurarse de que en la columna 'total_venta' la cantidad de registros vacíos son: 0'''
    data = load_data
    null_or_empty_count = data['total_venta'].isna().sum()
    if null_or_empty_count == expected_count:
        logger.info(f"Efectivamente los registros vacíos en la columna total_venta son: {null_or_empty_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {null_or_empty_count}.")
        assert null_or_empty_count == expected_count, (f"Se esperaba que los valores vacíos fuesen {expected_count}, pero se encontraron {null_or_empty_count}.")

# Caso 11: Confirmar valores negativos en 'total_venta'
def test_negative_values_in_total_sale(load_data):
    '''Caso de prueba 11: Comprobar que existen registros con valores negativos en la columna 'total_venta'.'''
    data = load_data
    negative_count = data['total_venta'][data['total_venta'] < 0].count()
    logger.info(f"Número de valores negativos en 'total_venta': {negative_count}")
    assert negative_count > 0, "No se encontraron valores negativos en 'total_venta'."

# Caso 12: Confirmar que no hay valores negativos en 'total_venta'
def test_no_negative_values_in_total_sale(load_data):
    '''Caso de prueba 12: Confirmar que no hay registros con valores negativos en la columna 'total_venta'.'''
    data = load_data
    negative_count = data['total_venta'][data['total_venta'] < 0].count()
    logger.info(f"Valores negativos encontrados en 'total_venta': {negative_count}")
    assert negative_count == 0, "Se encontraron valores negativos en 'total_venta', pero no deberían existir."

# Caso 13: Confirmar que todos los valores en 'total_venta' son numéricos
def test_all_numeric_values_in_total_sale(load_data):
    '''Caso de prueba 13: Confirmar que todos los valores en la columna 'total_venta' son numéricos.'''
    data = load_data
    non_numeric_count = data['total_venta'].apply(lambda x: not isinstance(x, (int, float))).sum()
    logger.info(f"Valores no numéricos en 'total_venta' son: {non_numeric_count}")
    assert non_numeric_count == 0, "Se encontraron valores no numéricos en 'total_venta'."

'''# Caso de prueba 14: Confirmar que todos los valores en la columna total_venta son numéricos.
def test_all_values_are_numeric_in_total_sale(load_data):
    #Caso de prueba 14: Confirmar que todos los valores en la columna total_venta son numéricos.
    data = load_data
    non_numeric_values = data['total_venta'].sum()
    logger.info(f"Registros no numéricos en 'total_venta' son: {non_numeric_values}")
    assert non_numeric_values == 0, f"Se encontraron {non_numeric_values} valores no numéricos en la columna total_venta."'''

# Caso de prueba 15: Contar cuántos registros son de tipo de dato cadena de texto en la columna total_venta.
def test_count_text_values_in_total_sale(load_data):
    '''Caso de prueba 15: Contar cuántos registros son tipo de dato cadena de texto en la columna total_venta.'''
    data = load_data
    text_values = data['total_venta'].apply(lambda x: isinstance(x, str) and not x.isnumeric()).sum()
    logger.info(f"La cantidad de registros con cadenas de texto en 'total_venta' son: {text_values}")
    assert text_values >= 0, "El conteo de cadenas de texto no es correcto."

# Caso de prueba 16: Asegurarse de que 6120 registros son tipo de dato cadena de texto en la columna total_venta.
@pytest.mark.parametrize("expected_count", [6120])
def test_count_exact_text_values_in_total_sale(load_data, expected_count):
    '''Caso de prueba 16: Asegurarse de que 6120 registros son tipo de dato cadena de texto en la columna total_venta.'''
    data = load_data
    text_values = data['total_venta'].apply(lambda x: isinstance(x, str) and not x.isnumeric()).sum()
    if text_values == expected_count:
        logger.info(f"Efectivamente la cantidad de registros con cadenas de texto en 'total_venta' son: {text_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero los registros con tipo de dato cadena de texto son: {text_values}")
        assert text_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {text_values}.")

# Caso de prueba 17: Contar cuántos registros tienen valores entre 200 y 1200 en la columna total_venta.
def test_count_values_between_200_and_1200_in_total_sale(load_data):
    '''Caso de prueba 17: Contar cuántos registros tienen valores entre 200 y 1200 en la columna total_venta.'''
    data = load_data
    in_range_values = data['total_venta'].apply(lambda x: 200 <= pd.to_numeric(x, errors='coerce') <= 1200).sum()
    logger.info(f"Registros con valores entre 200 y 1200 en 'total_venta': {in_range_values}")
    assert in_range_values >= 0, "El conteo de valores entre 200 y 1200 no es correcto."

# Caso de prueba 18: Asegurarse de que 15 registros tienen valores entre 200 y 1200 en la columna total_venta.
@pytest.mark.parametrize("expected_count", [1607])
def test_count_exact_values_between_200_and_1200_in_total_sale(load_data, expected_count):
    '''Caso de prueba 18: Asegurarse de que 1607 registros tienen valores entre 200 y 1200 en la columna total_venta.'''
    data = load_data
    in_range_values = data['total_venta'].apply(lambda x: 200 <= pd.to_numeric(x, errors='coerce') <= 1200).sum()
    if in_range_values == expected_count:
        logger.info(f"Efectivamente, los registros con valores entre 200 y 1200 en 'total_venta': {in_range_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero los registros de valores entre 200 y 1200 son: {in_range_values}")
        assert in_range_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {in_range_values}.")

# Caso de prueba 19: Contar cuántos registros tienen valores que comienzan con 'Total inconsistente' en la columna total_venta.
def test_count_values_with_total_in_total_sale(load_data):
    '''Caso de prueba 19: Contar cuántos registros tienen valores 'Total inconsistente' en la columna total_venta.'''
    data = load_data
    total_inconsistent_values = data['total_venta'].astype(str).str.contains('Total inconsistente').sum()
    logger.info(f"La cantidad de registros que comienzan con 'Total inconsistente en' 'total_venta': {total_inconsistent_values}")
    assert total_inconsistent_values >= 0, "El conteo de valores que comienzan con - no es correcto."

# Caso de prueba 20: Asegurarse de que 36 registros empiezan con 'Total inconsistente' en la columna total_venta.
@pytest.mark.parametrize("expected_count",  [36])
def test_values_exact_with_total_in_total_sale(load_data, expected_count):
    '''Caso de prueba 20: Asegurarse de que 36 registros tienen 'Total inconsiente' en la columna total_venta.'''
    data = load_data
    total_inconsistent_values = data['total_venta'].astype(str).str.contains('Total inconsistente').sum()
    if total_inconsistent_values == expected_count:
        logger.info(f"Efectivamente, los registros que empiezan con 'Total inconsistente' en 'total_venta': {total_inconsistent_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero la cantidad de registros que empiezan con 'Total inconsistente' son: {total_inconsistent_values}")
        assert total_inconsistent_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {total_inconsistent_values}.")

@pytest.mark.parametrize(
    "test_name, validation_function, expected_value",
    [
        # Caso 2: Valor más alto en la columna 'total_venta'
        ("Valor más alto", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').max(), 22914.7),
        
        # Caso 4: Valor más bajo en la columna 'total_venta'
        ("Valor más bajo", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').min(), -4104288.13),
        
        # Caso 6: Registros positivos en la columna 'total_venta'
        ("Registros positivos 1", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').gt(0).sum(), 5577),
                    
        # Caso 12: Registros negativos en la columna 'total_venta'
        ("Sin valores negativos", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').lt(0).sum(), 507),
             
        # Caso 16: Registros string en la columna 'total_venta'
        ("Registros como string", lambda data: data['total_venta'].apply(lambda x: isinstance(x, str)).sum(), 6120),
        
        # Caso 18: Valores entre 200 y 1200 en la columna 'total_venta'
        ("Valores entre 200 y 1200", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').between(200, 1200).sum(), 1607),    

        #casos failed para ver el mensaje de error     
        ("Valor más alto", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').max(), 22914.6),
        ("Valor más bajo", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').min(), -4104288.11),
        ("Registros positivos 1", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').gt(0).sum(), 5566 ),
        ("Sin valores negativos", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').lt(0).sum(), 506),
        ("Registros como string", lambda data: data['total_venta'].apply(lambda x: isinstance(x, str)).sum(), 6121),
        ("Valores entre 200 y 1200", lambda data: pd.to_numeric(data['total_venta'], errors='coerce').between(200, 1200).sum(), 1606),
    ]
)

def test_validations(load_data, test_name, validation_function, expected_value):
    '''Validaciones parametrizadas para diferentes casos en la columna 'total_venta'.'''
    data = load_data
    result = validation_function(data)
    if result == expected_value:
        logger.info(f"{test_name}: Validación exitosa. Resultado esperado y obtenido: {result}")
    else:
        logger.error(f"{test_name}: Error. Se esperaba {expected_value}, pero se encontró {result}")
    assert result == expected_value, f"{test_name}: Se esperaba {expected_value}, pero se encontró {result}."
