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
pytest test_cantidad_vendida.py -v --tb=short --log-cli-level=INFO --html=report_cantidad_vendida.html --self-contained-html

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

# Caso 1: Determinar el valor más alto en la columna 'cantidad_vendida'
def test_max_value_in_amount_sold(load_data):
    '''Caso de prueba 1: Determinar cuál es el valor más alto registrado en la columna 'cantidad_vendida'.'''
    data = load_data
    data['cantidad_vendida'] = pd.to_numeric(data['cantidad_vendida'], errors='coerce')
    max_value = data['cantidad_vendida'].max()
    logger.info(f"El valor más alto en la columna 'cantidad_vendida' es: {max_value}")
    assert max_value > 0, "El valor más alto en 'cantidad_vendida' debe ser positivo."

@pytest.mark.parametrize("expected_count", [4958])
def test_exact_value_more_hight(load_data, expected_count):
    '''Caso 2: Asegurarse de que el valor más alto en la columna cantidad_vendida es 4958'''
    data = load_data
    data['cantidad_vendida'] = pd.to_numeric(data['cantidad_vendida'], errors='coerce')
    max_value = data['cantidad_vendida'].max()
    if max_value == expected_count:
        logger.info(f"Efectivamente el valor más alto en la columna 'cantidad_vendida' es: {max_value}")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {max_value}.")
        assert max_value == expected_count, (f"Se esperaba el valor {expected_count}, pero se encontró {max_value}.")

# Caso 3: Determinar el valor más bajo en la columna 'cantidad_vendida'
def test_min_value_in_amount_sold(load_data):
    '''Caso de prueba 3: Determinar cuál es el valor más bajo registrado en la columna 'cantidad_vendida'.'''
    data = load_data
    data['cantidad_vendida'] = pd.to_numeric(data['cantidad_vendida'], errors='coerce')
    min_value = data['cantidad_vendida'].min()
    logger.info(f"El valor más bajo en la columna 'cantidad_vendida' es: {min_value}")
    assert min_value >= 0, "El valor más bajo en 'cantidad_vendida' no debe ser negativo."

@pytest.mark.parametrize("expected_count", [1])
def test_exact_value_lower(load_data, expected_count):
    '''Caso 4: Asegurarse de que el valor más bajo en la columna cantidad_vendida es 1'''
    data = load_data
    data['cantidad_vendida'] = pd.to_numeric(data['cantidad_vendida'], errors='coerce')
    min_value = data['cantidad_vendida'].min()
    if min_value == expected_count:
        logger.info(f"Efectivamente se encontró que el valor más bajo en la columna 'cantidad_vendida' es: {min_value}")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {min_value}.")
        assert min_value == expected_count, (f"Se esperaba el valor {expected_count}, pero se encontró {min_value}.")

# Caso de prueba 5: Contar cuántos registros tienen valores positivos en la columna cantidad_vendida.
def test_count_positive_values_in_amount_sold(load_data):
    '''Caso de prueba 5: Contar cuántos registros tienen valores positivos en la columna cantidad_vendida.'''
    data = load_data
    positive_values = data['cantidad_vendida'].apply(lambda x: pd.to_numeric(x, errors='coerce') > 0)
    positive_count = positive_values.sum()
    logger.info(f"Registros con valores positivos: {positive_count}")
    assert positive_count >= 0, "El conteo de valores positivos no es correcto."

# Caso de prueba 6: Asegurarse de que en la columna 'cantidad_vendida' la cantidad de registros positvios son: 6120
@pytest.mark.parametrize("expected_count", [6120])
def test_exact_count_positive_values_in_amount_sold(load_data, expected_count):
    '''Caso de prueba 6: Asegurarse de que en la columna 'cantidad_vendida' la cantidad de registros positvios son: 6120'''
    data = load_data
    positive_values = data['cantidad_vendida'].apply(lambda x: pd.to_numeric(x, errors='coerce') > 0)
    positive_count = positive_values.sum()
    if positive_count == expected_count:
        logger.info(f"Efectivamente los registros con valores positivos en la columna cantidad_vendida son : {positive_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {positive_count}.")
        assert positive_count == expected_count, (f"Se esperaba que los valores positivos fuesen {expected_count}, pero se encontraron {positive_count}.")

def test_count_negative_values_in_amount_sold(load_data):
    '''Caso de prueba 7: Contar cuántos registros tienen valores negativos en la columna cantidad_vendida.'''
    data = load_data
    negative_values = data['cantidad_vendida'].apply(lambda x: pd.to_numeric(x, errors='coerce') < 0)
    negative_count = negative_values.sum()
    logger.info(f"Registros con valores negativos: {negative_count}")
    assert negative_count >= 0, "El conteo de valores negativos no es correcto."

#Caso de prueba 8: Asegurarse de que en la columna 'cantidad_vendida' la cantidad de registros negativos son: 0
@pytest.mark.parametrize("expected_count", [0])
def test_count_exact_negative_values_in_amount_sold(load_data, expected_count):
    '''Caso de prueba 8: Asegurarse de que en la columna 'cantidad_vendida' la cantidad de registros negativos son: 0'''
    data = load_data
    negative_values = data['cantidad_vendida'].apply(lambda x: pd.to_numeric(x, errors='coerce') < 0)
    negative_count = negative_values.sum()
    if negative_count == expected_count:
        logger.info(f"Efectivamente los registros con valores negativos en la columna cantidad_vendida son: {negative_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {negative_count}.")
        assert negative_count == expected_count, (f"Se esperaba que los valores positivos fuesen {expected_count}, pero se encontraron {negative_count}.")

# Caso 9: Confirmar que no existan valores nulos o vacíos en 'cantidad_vendida'
def test_no_null_or_empty_values_in_amount_sold(load_data):
    '''Caso de prueba 9: Contar cuántos registros vacíos hay en la columna cantidad_vendida.'''
    data = load_data
    null_or_empty_count = data['cantidad_vendida'].isna().sum()
    logger.info(f"Valores nulos o vacíos en 'cantidad_vendida': {null_or_empty_count}")
    assert null_or_empty_count == 0, "Se encontraron valores nulos o vacíos en 'cantidad_vendida'."

@pytest.mark.parametrize("expected_count", [0])
def test_count_exact_or_empty_values_null_in_amount_sold(load_data, expected_count):
    '''Caso de prueba 10: Asegurarse de que en la columna 'cantidad_vendida' la cantidad de registros vacíos son: 0'''
    data = load_data
    null_or_empty_count = data['cantidad_vendida'].isna().sum()
    if null_or_empty_count == expected_count:
        logger.info(f"Efectivamente los registros vacíos en la columna cantidad_vendida son: {null_or_empty_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {null_or_empty_count}.")
        assert null_or_empty_count == expected_count, (f"Se esperaba que los valores vacíos fuesen {expected_count}, pero se encontraron {null_or_empty_count}.")

# Caso 11: Confirmar valores negativos en 'cantidad_vendida'
def test_negative_values_in_amount_sold(load_data):
    '''Caso de prueba 11: Comprobar que existen registros con valores negativos en la columna 'cantidad_vendida'.'''
    data = load_data
    negative_count = data['cantidad_vendida'][data['cantidad_vendida'] < 0].count()
    logger.info(f"Número de valores negativos en 'cantidad_vendida': {negative_count}")
    assert negative_count > 0, "No se encontraron valores negativos en 'cantidad_vendida'."

# Caso 12: Confirmar que no hay valores negativos en 'cantidad_vendida'
def test_no_negative_values_in_amount_sold(load_data):
    '''Caso de prueba 12: Confirmar que no hay registros con valores negativos en la columna 'cantidad_vendida'.'''
    data = load_data
    negative_count = data['cantidad_vendida'][data['cantidad_vendida'] < 0].count()
    logger.info(f"Valores negativos encontrados en 'cantidad_vendida': {negative_count}")
    assert negative_count == 0, "Se encontraron valores negativos en 'cantidad_vendida', pero no deberían existir."

# Caso 13: Confirmar que todos los valores en 'cantidad_vendida' son numéricos
def test_all_numeric_values_in_amount_sold(load_data):
    '''Caso de prueba 13: Confirmar que todos los valores en la columna 'cantidad_vendida' son numéricos.'''
    data = load_data
    non_numeric_count = data['cantidad_vendida'].apply(lambda x: not isinstance(x, (int, float))).sum()
    logger.info(f"Valores no numéricos en 'cantidad_vendida' son: {non_numeric_count}")
    assert non_numeric_count == 0, "Se encontraron valores no numéricos en 'cantidad_vendida'."

'''# Caso de prueba 14: Confirmar que todos los valores en la columna cantidad_vendida son numéricos.
def test_all_values_are_numeric_in_amount_sold(load_data):
    #Caso de prueba 14: Confirmar que todos los valores en la columna cantidad_vendida son numéricos.
    data = load_data
    non_numeric_values = data['cantidad_vendida'].sum()
    logger.info(f"Registros no numéricos en 'cantidad_vendida' son: {non_numeric_values}")
    assert non_numeric_values == 0, f"Se encontraron {non_numeric_values} valores no numéricos en la columna cantidad_vendida."'''

# Caso de prueba 15: Contar cuántos registros son de tipo de dato cadena de texto en la columna cantidad_vendida.
def test_count_text_values_in_amount_sold(load_data):
    '''Caso de prueba 15: Contar cuántos registros son tipo de dato cadena de texto en la columna cantidad_vendida.'''
    data = load_data
    text_values = data['cantidad_vendida'].apply(lambda x: isinstance(x, str) and not x.isnumeric()).sum()
    logger.info(f"La cantidad de registros con cadenas de texto en 'cantidad_vendida' son: {text_values}")
    assert text_values >= 0, "El conteo de cadenas de texto no es correcto."

# Caso de prueba 16: Asegurarse de que 0 registros son tipo de dato cadena de texto en la columna cantidad_vendida.
@pytest.mark.parametrize("expected_count", [0])
def test_count_exact_text_values_in_amount_sold(load_data, expected_count):
    '''Caso de prueba 16: Asegurarse de que 0 registros son tipo de dato cadena de texto en la columna cantidad_vendida.'''
    data = load_data
    text_values = data['cantidad_vendida'].apply(lambda x: isinstance(x, str) and not x.isnumeric()).sum()
    if text_values == expected_count:
        logger.info(f"Efectivamente la cantidad de registros con cadenas de texto en 'cantidad_vendida' son: {text_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero los registros con tipo de dato cadena de texto son: {text_values}")
        assert text_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {text_values}.")

# Caso de prueba 17: Contar cuántos registros tienen valores entre 1400 y 1700 en la columna cantidad_vendida.
def test_count_values_between_1400_and_1700_in_amount_sold(load_data):
    '''Caso de prueba 17: Contar cuántos registros tienen valores entre 1400 y 1700 en la columna cantidad_vendida.'''
    data = load_data
    in_range_values = data['cantidad_vendida'].apply(lambda x: 1400 <= pd.to_numeric(x, errors='coerce') <= 1700).sum()
    logger.info(f"Registros con valores entre 1400 y 1700 en 'cantidad_vendida': {in_range_values}")
    assert in_range_values >= 0, "El conteo de valores entre 1400 y 1700 no es correcto."

# Caso de prueba 18: Asegurarse de que 15 registros tienen valores entre 1400 y 1700 en la columna cantidad_vendida.
@pytest.mark.parametrize("expected_count", [15])
def test_count_exact_values_between_1400_and_1700_in_amount_sold(load_data, expected_count):
    '''Caso de prueba 18: Asegurarse de que 15 registros tienen valores entre 1400 y 1700 en la columna cantidad_vendida.'''
    data = load_data
    in_range_values = data['cantidad_vendida'].apply(lambda x: 1400 <= pd.to_numeric(x, errors='coerce') <= 1700).sum()
    if in_range_values == expected_count:
        logger.info(f"Efectivamente, los registros con valores entre 1400 y 1700 en 'cantidad_vendida': {in_range_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero los registros de valores entre 1400 y 1700 son: {in_range_values}")
        assert in_range_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {in_range_values}.")

@pytest.mark.parametrize(
    "test_name, validation_function, expected_value",
    [
        # Caso 2: Valor más alto en la columna 'cantidad_vendida'
        ("Valor más alto", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').max(), 4958),
        
        # Caso 4: Valor más bajo en la columna 'cantidad_vendida'
        ("Valor más bajo", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').min(), 1),
        
        # Caso 6: Registros positivos en la columna 'cantidad_vendida'
        ("Registros positivos 1", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').gt(0).sum(), 6120),
                    
        # Caso 12: Registros negativos en la columna 'cantidad_vendida'
        ("Sin valores negativos", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').lt(0).sum(), 0),
             
        # Caso 16: Registros string en la columna 'cantidad_vendida'
        ("Registros como string", lambda data: data['cantidad_vendida'].apply(lambda x: isinstance(x, str)).sum(), 0),
        
        # Caso 18: Valores entre 1400 y 1700 en la columna 'cantidad_vendida'
        ("Valores entre 1400 y 1700", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').between(1400, 1700).sum(), 15),    

        #casos failed para ver el mensaje de error     
        ("Valor más alto", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').max(), 495),
        ("Valor más bajo", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').min(), 1),
        ("Registros positivos 1", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').gt(0).sum(), 612),
        ("Sin valores negativos", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').lt(0).sum(), 1),
        ("Registros como string", lambda data: data['cantidad_vendida'].apply(lambda x: isinstance(x, str)).sum(), 1),
        ("Valores entre 1400 y 1700", lambda data: pd.to_numeric(data['cantidad_vendida'], errors='coerce').between(1400, 1700).sum(), 5),
    ]
)

def test_validations(load_data, test_name, validation_function, expected_value):
    '''Validaciones parametrizadas para diferentes casos en la columna 'cantidad_vendida'.'''
    data = load_data
    result = validation_function(data)
    if result == expected_value:
        logger.info(f"{test_name}: Validación exitosa. Resultado esperado y obtenido: {result}")
    else:
        logger.error(f"{test_name}: Error. Se esperaba {expected_value}, pero se encontró {result}")
    assert result == expected_value, f"{test_name}: Se esperaba {expected_value}, pero se encontró {result}."
