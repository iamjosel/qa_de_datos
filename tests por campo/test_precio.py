import pytest
import pandas as pd
import logging

'''
@uthor: José Luis García Quinayás
date: 30/11/2024
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
pytest test_precio.py -v --tb=short --log-cli-level=INFO --html=report_campo_precio.html --self-contained-html

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

# Caso 1: Determinar el valor más alto en la columna 'precio'
def test_max_value_in_price(load_data):
    '''Caso de prueba 1: Determinar cuál es el valor más alto registrado en la columna 'precio'.'''
    data = load_data
    data['precio'] = pd.to_numeric(data['precio'], errors='coerce')
    max_value = data['precio'].max()
    logger.info(f"El valor más alto en la columna 'precio' es: {max_value}")
    assert max_value > 0, "El valor más alto en 'precio' debe ser positivo."

@pytest.mark.parametrize("expected_count", [849.91])
def test_exact_value_more_hight(load_data, expected_count):
    '''Caso 2: Asegurarse de que el valor más alto en la columna precio es 849.91'''
    data = load_data
    data['precio'] = pd.to_numeric(data['precio'], errors='coerce')
    max_value = data['precio'].max()
    if max_value == expected_count:
        logger.info(f"Efectivamente el valor más alto en la columna 'precio' es: {max_value}")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {max_value}.")
        assert max_value == expected_count, (f"Se esperaba el valor {expected_count}, pero se encontró {max_value}.")

# Caso 3: Determinar el valor más bajo en la columna 'precio'
def test_min_value_in_price(load_data):
    '''Caso de prueba 3: Determinar cuál es el valor más bajo registrado en la columna 'precio'.'''
    data = load_data
    data['precio'] = pd.to_numeric(data['precio'], errors='coerce')
    min_value = data['precio'].min()
    logger.info(f"El valor más bajo en la columna 'precio' es: {min_value}")
    assert min_value >= 0, "El valor más bajo en 'precio' no debe ser negativo."

@pytest.mark.parametrize("expected_count", [-844.33])
def test_exact_value_lower(load_data, expected_count):
    '''Caso 4: Asegurarse de que el valor más bajo en la columna precio es 844.33'''
    data = load_data
    data['precio'] = pd.to_numeric(data['precio'], errors='coerce')
    min_value = data['precio'].min()
    if min_value == expected_count:
        logger.info(f"Efectivamente se encontró que el valor más bajo en la columna 'precio' es: {min_value}")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {min_value}.")
        assert min_value == expected_count, (f"Se esperaba el valor {expected_count}, pero se encontró {min_value}.")

# Caso de prueba 5: Contar cuántos registros tienen valores positivos en la columna precio.
def test_count_positive_values_in_price(load_data):
    '''Caso de prueba 5: Contar cuántos registros tienen valores positivos en la columna precio.'''
    data = load_data
    positive_values = data['precio'].apply(lambda x: pd.to_numeric(x, errors='coerce') > 0)
    positive_count = positive_values.sum()
    logger.info(f"Registros con valores positivos: {positive_count}")
    assert positive_count >= 0, "El conteo de valores positivos no es correcto."

# Caso de prueba 6: Asegurarse de que en la columna 'precio' la cantidad de registros positvios son: 5368
@pytest.mark.parametrize("expected_count", [5368])
def test_exact_count_positive_values_in_price(load_data, expected_count):
    '''Caso de prueba 6: Asegurarse de que en la columna 'precio' la cantidad de registros positvios son: 5368'''
    data = load_data
    positive_values = data['precio'].apply(lambda x: pd.to_numeric(x, errors='coerce') > 0)
    positive_count = positive_values.sum()
    if positive_count == expected_count:
        logger.info(f"Efectivamente los registros con valores positivos en la columna precio son : {positive_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {positive_count}.")
        assert positive_count == expected_count, (f"Se esperaba que los valores positivos fuesen {expected_count}, pero se encontraron {positive_count}.")

def test_count_negative_values_in_price(load_data):
    '''Caso de prueba 7: Contar cuántos registros tienen valores negativos en la columna precio.'''
    data = load_data
    negative_values = data['precio'].apply(lambda x: pd.to_numeric(x, errors='coerce') < 0)
    negative_count = negative_values.sum()
    logger.info(f"Registros con valores negativos: {negative_count}")
    assert negative_count >= 0, "El conteo de valores negativos no es correcto."

#Caso de prueba 8: Asegurarse de que en la columna 'precio' la cantidad de registros negativos son: 492
@pytest.mark.parametrize("expected_count", [492])
def test_count_exact_negative_values_in_price(load_data, expected_count):
    '''Caso de prueba 8: Asegurarse de que en la columna 'precio' la cantidad de registros negativos son: 492'''
    data = load_data
    negative_values = data['precio'].apply(lambda x: pd.to_numeric(x, errors='coerce') < 0)
    negative_count = negative_values.sum()
    if negative_count == expected_count:
        logger.info(f"Efectivamente los registros con valores positivos en la columna precio son: {negative_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {negative_count}.")
        assert negative_count == expected_count, (f"Se esperaba que los valores positivos fuesen {expected_count}, pero se encontraron {negative_count}.")

# Caso 9: Confirmar que no existan valores nulos o vacíos en 'precio'
def test_no_null_or_empty_values_in_price(load_data):
    '''Caso de prueba 9: Contar cuántos registros vacíos hay en la columna precio.'''
    data = load_data
    null_or_empty_count = data['precio'].isna().sum()
    logger.info(f"Valores nulos o vacíos en 'precio': {null_or_empty_count}")
    assert null_or_empty_count == 0, "Se encontraron valores nulos o vacíos en 'precio'."

@pytest.mark.parametrize("expected_count", [35])
def test_count_exact_or_empty_values_null_in_price(load_data, expected_count):
    '''Caso de prueba 10: Asegurarse de que en la columna 'precio' la cantidad de registros vacíos son: 35'''
    data = load_data
    null_or_empty_count = data['precio'].isna().sum()
    if null_or_empty_count == expected_count:
        logger.info(f"Efectivamente los registros vacíos en la columna precio son: {null_or_empty_count}")
    else:
        logger.error(f"Error: Se esperaban {expected_count}, pero se encontraron {null_or_empty_count}.")
        assert null_or_empty_count == expected_count, (f"Se esperaba que los valores vacíos fuesen {expected_count}, pero se encontraron {null_or_empty_count}.")

# Caso 11: Confirmar valores negativos en 'precio'
def test_negative_values_in_price(load_data):
    '''Caso de prueba 11: Comprobar que existen registros con valores negativos en la columna 'precio'.'''
    data = load_data
    negative_count = data['precio'][data['precio'] < 0].count()
    logger.info(f"Número de valores negativos en 'precio': {negative_count}")
    assert negative_count > 0, "No se encontraron valores negativos en 'precio'."

# Caso 12: Confirmar que no hay valores negativos en 'precio'
def test_no_negative_values_in_price(load_data):
    '''Caso de prueba 12: Confirmar que no hay registros con valores negativos en la columna 'precio'.'''
    data = load_data
    negative_count = data['precio'][data['precio'] < 0].count()
    logger.info(f"Valores negativos encontrados en 'precio': {negative_count}")
    assert negative_count == 0, "Se encontraron valores negativos en 'precio', pero no deberían existir."

# Caso 13: Confirmar que todos los valores en 'precio' son numéricos
def test_all_numeric_values_in_price(load_data):
    '''Caso de prueba 13: Confirmar que todos los valores en la columna 'precio' son numéricos.'''
    data = load_data
    non_numeric_count = data['precio'].apply(lambda x: not isinstance(x, (int, float))).sum()
    logger.info(f"Valores no numéricos en 'precio' son: {non_numeric_count}")
    assert non_numeric_count == 0, "Se encontraron valores no numéricos en 'precio'."

# Caso de prueba 14: Confirmar que todos los valores en la columna precio son numéricos.
def test_all_values_are_numeric_in_price(load_data):
    '''Caso de prueba 14: Confirmar que todos los valores en la columna precio son numéricos.'''
    data = load_data
    non_numeric_values = data['precio'].sum()
    logger.info(f"Registros no numéricos en 'precio' son: {non_numeric_values}")
    assert non_numeric_values == 0, f"Se encontraron {non_numeric_values} valores no numéricos en la columna precio."

# Caso de prueba 15: Contar cuántos registros son de tipo de dato cadena de texto en la columna precio.
def test_count_text_values_in_price(load_data):
    '''Caso de prueba 15: Contar cuántos registros son tipo de dato cadena de texto en la columna precio.'''
    data = load_data
    text_values = data['precio'].apply(lambda x: isinstance(x, str) and not x.isnumeric()).sum()
    logger.info(f"La cantidad de registros con cadenas de texto en 'precio' son: {text_values}")
    assert text_values >= 0, "El conteo de cadenas de texto no es correcto."

# Caso de prueba 16: Asegurarse de que 6085 registros son tipo de dato cadena de texto en la columna precio.
@pytest.mark.parametrize("expected_count", [6085])
def test_count_exact_text_values_in_price(load_data, expected_count):
    '''Caso de prueba 16: Asegurarse de que 6085 registros son tipo de dato cadena de texto en la columna precio.'''
    data = load_data
    text_values = data['precio'].apply(lambda x: isinstance(x, str) and not x.isnumeric()).sum()
    if text_values == expected_count:
        logger.info(f"Efectivamente la cantidad de registros con cadenas de texto en 'precio' son: {text_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero los registros con tipo de dato cadena de texto son: {text_values}")
        assert text_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {text_values}.")

# Caso de prueba 17: Contar cuántos registros tienen valores entre 100 y 200 en la columna precio.
def test_count_values_between_100_and_200_in_price(load_data):
    '''Caso de prueba 17: Contar cuántos registros tienen valores entre 100 y 200 en la columna precio.'''
    data = load_data
    in_range_values = data['precio'].apply(lambda x: 100 <= pd.to_numeric(x, errors='coerce') <= 200).sum()
    logger.info(f"Registros con valores entre 100 y 200 en 'precio': {in_range_values}")
    assert in_range_values >= 0, "El conteo de valores entre 100 y 200 no es correcto."

# Caso de prueba 18: Asegurarse de que 923 registros tienen valores entre 100 y 200 en la columna precio.
@pytest.mark.parametrize("expected_count", [923])
def test_count_exact_values_between_100_and_200_in_price(load_data, expected_count):
    '''Caso de prueba 18: Asegurarse de que 923 registros tienen valores entre 100 y 200 en la columna precio.'''
    data = load_data
    in_range_values = data['precio'].apply(lambda x: 100 <= pd.to_numeric(x, errors='coerce') <= 200).sum()
    if in_range_values == expected_count:
        logger.info(f"Efectivamente, los registros con valores entre 100 y 200 en 'precio': {in_range_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero los registros de valores entre 100 y 200 son: {in_range_values}")
        assert in_range_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {in_range_values}.")

# Caso de prueba 19: Contar cuántos registros empiezan con $ en la columna precio.
def test_values_starting_with_dollar_in_price(load_data):
    '''Caso de prueba 19: Contar cuántos registros empiezan con $ en la columna precio.'''
    data = load_data
    dollar_start_values = data['precio'].astype(str).str.startswith('$').sum()
    logger.info(f"La cantidad de registros que empiezan con $ en 'precio' son: {dollar_start_values}")
    assert dollar_start_values > 0, "No se encontraron registros que comienzan con $ en la columna precio."

# Caso de prueba 20: Asegurarse de que 225 registros empiezan con $ en la columna precio.
@pytest.mark.parametrize("expected_count", [225])
def test_values_exact_starting_with_dollar_in_price(load_data, expected_count):
    '''Caso de prueba 20: Asegurarse de que 225 registros empiezan con $ en la columna precio.'''
    data = load_data
    dollar_start_values = data['precio'].astype(str).str.startswith('$').sum()
    if dollar_start_values == expected_count:
        logger.info(f"Efectivamente, los registros que empiezan con $ en 'precio': {dollar_start_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero la cantidad de registros que empiezan con $ son: {dollar_start_values}")
        assert dollar_start_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {dollar_start_values}.")

# Caso de prueba 21: Contar cuántos registros empiezan con - en la columna precio.
def test_values_starting_with_minus_in_price(load_data):
    '''Caso de prueba 21: Contar cuántos registros empiezan con - en la columna precio.'''
    data = load_data
    minus_start_values = data['precio'].astype(str).str.startswith('-').sum()
    logger.info(f"La cantidad de registros que empiezan con - en 'precio' son: {minus_start_values}")
    assert minus_start_values > 0, "No se encontraron registros que comienzan con - en la columna precio."

# Caso de prueba 22: Asegurarse de que 492 registros empiezan con - en la columna precio.
@pytest.mark.parametrize("expected_count", [492])
def test_values_exact_starting_with_minus_in_price(load_data, expected_count):
    '''Caso de prueba 22: Asegurarse de que 492 registros empiezan con - en la columna precio.'''
    data = load_data
    minus_start_values = data['precio'].astype(str).str.startswith('-').sum()
    if minus_start_values == expected_count:
        logger.info(f"Efectivamente, los registros que empiezan con - en 'precio': {minus_start_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero la cantidad de registros que empiezan con - son: {minus_start_values}")
        assert minus_start_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {minus_start_values}.")

# Caso de prueba 23: Contar cuántos registros tienen valores que comienzan con - en la columna precio.
def test_count_values_starting_with_minus_in_price_total(load_data):
    '''Caso de prueba 23: Contar cuántos registros tienen valores que comienzan con - en la columna precio.'''
    data = load_data
    minus_start_values = data['precio'].astype(str).str.contains('-').sum()
    logger.info(f"La cantidad de registros que comienzan con - en 'precio': {minus_start_values}")
    assert minus_start_values >= 0, "El conteo de valores que comienzan con - no es correcto."

# Caso de prueba 24: Asegurarse de que 507 registros empiezan con - en la columna precio.
@pytest.mark.parametrize("expected_count", [507])
def test_values_exact_begin_with_minus_in_price_total(load_data, expected_count):
    '''Caso de prueba 24: Asegurarse de que 507 registros empiezan con - en la columna precio.'''
    data = load_data
    minus_start_values = data['precio'].astype(str).str.contains('-').sum()
    if minus_start_values == expected_count:
        logger.info(f"Efectivamente, los registros que empiezan con - en 'precio': {minus_start_values}")
    else:
        logger.error(f"Error: se esperaban {expected_count} registros, pero la cantidad de registros que empiezan con - son: {minus_start_values}")
        assert minus_start_values == expected_count, (f"Se esperaba que el número de registros fuesen {expected_count}, pero se encontraron: {minus_start_values}.")

@pytest.mark.parametrize(
    "test_name, validation_function, expected_value",
    [
        # Caso 2: Valor más alto en la columna 'precio'
        ("Valor más alto", lambda data: pd.to_numeric(data['precio'], errors='coerce').max(), 849.91),
        
        # Caso 4: Valor más bajo en la columna 'precio'
        ("Valor más bajo", lambda data: pd.to_numeric(data['precio'], errors='coerce').min(), -844.33),
        
        # Caso 6: Registros positivos en la columna 'precio'
        ("Registros positivos 1", lambda data: pd.to_numeric(data['precio'], errors='coerce').gt(0).sum(), 5368),
                    
        # Caso 12: Registros negativos en la columna 'precio'
        ("Sin valores negativos", lambda data: pd.to_numeric(data['precio'], errors='coerce').lt(0).sum(), 492),
             
        # Caso 16: Registros string en la columna 'precio'
        ("Registros como string", lambda data: data['precio'].apply(lambda x: isinstance(x, str)).sum(), 6085),
        
        # Caso 18: Valores entre 100 y 200 en la columna 'precio'
        ("Valores entre 100 y 200", lambda data: pd.to_numeric(data['precio'], errors='coerce').between(100, 200).sum(), 923),
        
        # Caso 20: Valores que empiezan con '$' en la columna 'precio'
        ("Empiezan con $", lambda data: data['precio'].astype(str).str.startswith('$').sum(), 225),
        
        # Caso 22: Valores que empiezan con '-' en la columna 'precio'
        ("Empiezan con - (492 registros)", lambda data: data['precio'].astype(str).str.startswith('-').sum(), 492),
        
        # Caso 24: Valores que contienen '-' en la columna 'precio'
        ("Empiezan con - (507 registros)", lambda data: data['precio'].astype(str).str.contains('-').sum(), 507),
    ]
)
def test_validations(load_data, test_name, validation_function, expected_value):
    '''Validaciones parametrizadas para diferentes casos en la columna 'precio'.'''
    data = load_data
    result = validation_function(data)
    if result == expected_value:
        logger.info(f"{test_name}: Validación exitosa. Resultado esperado y obtenido: {result}")
    else:
        logger.error(f"{test_name}: Error. Se esperaba {expected_value}, pero se encontró {result}")
    assert result == expected_value, f"{test_name}: Se esperaba {expected_value}, pero se encontró {result}."
