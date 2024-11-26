import pytest
import pandas as pd
import logging

'''
@uthor: José Luis García Quinayás
date: 25/11/2024
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
    '''Carga los datos del archivo Excel.'''
    file_path = "O:/productos/ventas1.xlsx"
    return pd.read_excel(file_path)

# Caso 1: Determinar el valor más alto en la columna 'precio'
def test_max_value_in_price(load_data):
    '''Caso de prueba 1: Determinar cuál es el valor más alto registrado en la columna 'precio'.'''
    data = load_data
    max_value = data['precio'].max()
    logger.info(f"El valor más alto en la columna 'precio' es: {max_value}")
    assert max_value > 0, "El valor más alto en 'precio' debe ser positivo."

# Caso 2: Determinar el valor más bajo en la columna 'precio'
def test_min_value_in_price(load_data):
    '''Caso de prueba 2: Determinar cuál es el valor más bajo registrado en la columna 'precio'.'''
    data = load_data
    min_value = data['precio'].min()
    logger.info(f"El valor más bajo en la columna 'precio' es: {min_value}")
    assert min_value >= 0, "El valor más bajo en 'precio' no debe ser negativo."

# Caso 3: Confirmar que hay valores positivos en la columna 'precio'
def test_positive_values_in_price(load_data):
    '''Caso de prueba 3: Confirmar que hay registros con valores positivos en la columna 'precio'.'''
    data = load_data
    positive_count = data['precio'][data['precio'] > 0].count()
    logger.info(f"Número de valores positivos en 'precio': {positive_count}")
    assert positive_count > 0, "No se encontraron valores positivos en 'precio'."

# Caso 4: Contar valores positivos en 'precio'
def test_count_positive_values_in_price(load_data):
    '''Caso de prueba 4: Contar cuántos registros tienen valores positivos en la columna 'precio'.'''
    data = load_data
    positive_count = data['precio'][data['precio'] > 0].count()
    logger.info(f"Registros con valores positivos en 'precio': {positive_count}")
    assert positive_count > 0, f"No se encontraron valores positivos en 'precio'."

# Caso 5: Confirmar que no existan valores positivos en 'precio'
def test_no_positive_values_in_price(load_data):
    '''Caso de prueba 5: Identificar si no existen registros con valores positivos en 'precio'.'''
    data = load_data
    positive_count = data['precio'][data['precio'] > 0].count()
    logger.info(f"Valores positivos encontrados en 'precio': {positive_count}")
    assert positive_count == 0, "Se encontraron valores positivos en 'precio', pero no deberían existir."

# Caso 6: Confirmar valores negativos en 'precio'
def test_negative_values_in_price(load_data):
    '''Caso de prueba 6: Comprobar que existen registros con valores negativos en la columna 'precio'.'''
    data = load_data
    negative_count = data['precio'][data['precio'] < 0].count()
    logger.info(f"Número de valores negativos en 'precio': {negative_count}")
    assert negative_count > 0, "No se encontraron valores negativos en 'precio'."

# Caso 7: Confirmar que no hay valores negativos en 'precio'
def test_no_negative_values_in_price(load_data):
    '''Caso de prueba 7: Confirmar que no hay registros con valores negativos en la columna 'precio'.'''
    data = load_data
    negative_count = data['precio'][data['precio'] < 0].count()
    logger.info(f"Valores negativos encontrados en 'precio': {negative_count}")
    assert negative_count == 0, "Se encontraron valores negativos en 'precio', pero no deberían existir."

# Caso 8: Contar valores negativos en 'precio'
def test_count_negative_values_in_price(load_data):
    '''Caso de prueba 8: Contar cuántos registros tienen valores negativos en la columna 'precio'.'''
    data = load_data
    negative_count = data['precio'][data['precio'] < 0].count()
    logger.info(f"Registros con valores negativos en 'precio': {negative_count}")
    assert negative_count > 0, "No se encontraron valores negativos en 'precio'."

# Caso 9: Confirmar que no existan valores nulos o vacíos en 'precio'
def test_no_null_or_empty_values_in_price(load_data):
    '''Caso de prueba 9: Confirmar que no existan valores nulos o vacíos en la columna 'precio'.'''
    data = load_data
    null_or_empty_count = data['precio'].isna().sum()
    logger.info(f"Valores nulos o vacíos en 'precio': {null_or_empty_count}")
    assert null_or_empty_count == 0, "Se encontraron valores nulos o vacíos en 'precio'."

# Caso 10: Confirmar que todos los valores en 'precio' son numéricos
def test_all_numeric_values_in_price(load_data):
    '''Caso de prueba 10: Confirmar que todos los valores en la columna 'precio' son numéricos.'''
    data = load_data
    non_numeric_count = data['precio'].apply(lambda x: not isinstance(x, (int, float))).sum()
    logger.info(f"Valores no numéricos en 'precio': {non_numeric_count}")
    assert non_numeric_count == 0, "Se encontraron valores no numéricos en 'precio'."

# Caso de prueba 10: Confirmar que todos los valores en la columna precio son numéricos.
def test_all_values_are_numeric_in_price(load_data):
    '''Caso de prueba 10: Confirmar que todos los valores en la columna precio son numéricos.'''
    data = load_data
    non_numeric_values = data['precio'].apply(lambda x: not pd.to_numeric(x, errors='coerce')).sum()
    logger.info(f"Registros no numéricos en 'precio': {non_numeric_values}")
    assert non_numeric_values == 0, f"Se encontraron {non_numeric_values} valores no numéricos en la columna precio."

# Caso de prueba 11: Contar cuántos registros tienen valores positivos en la columna precio.
def test_count_positive_values_in_price(load_data):
    '''Caso de prueba 11: Contar cuántos registros tienen valores positivos en la columna precio.'''
    data = load_data
    positive_values = data['precio'].apply(lambda x: pd.to_numeric(x, errors='coerce') > 0)
    positive_count = positive_values.sum()
    logger.info(f"Registros con valores positivos: {positive_count}")
    assert positive_count >= 0, "El conteo de valores positivos no es correcto."

# Caso de prueba 12: Contar cuántos registros tienen valores negativos en la columna precio.
def test_count_negative_values_in_price(load_data):
    '''Caso de prueba 12: Contar cuántos registros tienen valores negativos en la columna precio.'''
    data = load_data
    negative_values = data['precio'].apply(lambda x: pd.to_numeric(x, errors='coerce') < 0)
    negative_count = negative_values.sum()
    logger.info(f"Registros con valores negativos: {negative_count}")
    assert negative_count >= 0, "El conteo de valores negativos no es correcto."

# Caso de prueba 13: Contar cuántos registros contienen valores nulos o vacíos en la columna precio.
def test_count_null_or_empty_values_in_price(load_data):
    '''Caso de prueba 13: Contar cuántos registros contienen valores nulos o vacíos en la columna precio.'''
    data = load_data
    null_or_empty_values = data['precio'].isna().sum() + (data['precio'].astype(str).str.strip() == "").sum()
    logger.info(f"Registros nulos o vacíos en 'precio': {null_or_empty_values}")
    assert null_or_empty_values >= 0, "El conteo de valores nulos o vacíos no es correcto."

# Caso de prueba 14: Contar cuántos registros contienen cadenas de texto en la columna precio.
def test_count_text_values_in_price(load_data):
    '''Caso de prueba 14: Contar cuántos registros contienen cadenas de texto en la columna precio.'''
    data = load_data
    text_values = data['precio'].apply(lambda x: isinstance(x, str) and not x.isnumeric()).sum()
    logger.info(f"Registros con cadenas de texto en 'precio': {text_values}")
    assert text_values >= 0, "El conteo de cadenas de texto no es correcto."

# Caso de prueba 15: Contar cuántos registros tienen valores entre 100 y 200 en la columna precio.
def test_count_values_between_100_and_200_in_price(load_data):
    '''Caso de prueba 15: Contar cuántos registros tienen valores entre 100 y 200 en la columna precio.'''
    data = load_data
    in_range_values = data['precio'].apply(lambda x: 100 <= pd.to_numeric(x, errors='coerce') <= 200).sum()
    logger.info(f"Registros con valores entre 100 y 200 en 'precio': {in_range_values}")
    assert in_range_values >= 0, "El conteo de valores entre 100 y 200 no es correcto."

# Caso de prueba 16: Contar cuántos registros están entre 100 y 200 en la columna precio.
def test_count_values_within_100_and_200_in_price(load_data):
    '''Caso de prueba 16: Contar cuántos registros están entre 100 y 200 en la columna precio.'''
    data = load_data
    within_range_values = data['precio'].apply(lambda x: pd.to_numeric(x, errors='coerce')).between(100, 200).sum()
    logger.info(f"Registros entre 100 y 200 en 'precio': {within_range_values}")
    assert within_range_values >= 0, "El conteo de valores dentro del rango no es correcto."

# Caso de prueba 17: Comprobar que existen registros que empiezan con $ en la columna precio.
def test_values_starting_with_dollar_in_price(load_data):
    '''Caso de prueba 17: Comprobar que existen registros que empiezan con $ en la columna precio.'''
    data = load_data
    dollar_start_values = data['precio'].astype(str).str.startswith('$').sum()
    logger.info(f"Registros que empiezan con $ en 'precio': {dollar_start_values}")
    assert dollar_start_values > 0, "No se encontraron registros que comienzan con $ en la columna precio."

# Caso de prueba 18: Contar cuántos registros tienen valores que comienzan con $ en la columna precio.
def test_count_values_starting_with_dollar_in_price(load_data):
    '''Caso de prueba 18: Contar cuántos registros tienen valores que comienzan con $ en la columna precio.'''
    data = load_data
    dollar_start_values = data['precio'].astype(str).str.startswith('$').sum()
    logger.info(f"Registros que comienzan con $ en 'precio': {dollar_start_values}")
    assert dollar_start_values >= 0, "El conteo de valores que comienzan con $ no es correcto."

# Caso de prueba 19: Contar cuántos registros empiezan con $ en la columna precio.
def test_values_begin_with_dollar_in_price(load_data):
    '''Caso de prueba 19: Contar cuántos registros empiezan con $ en la columna precio.'''
    data = load_data
    dollar_start_values = data['precio'].astype(str).str.startswith('$').sum()
    logger.info(f"Registros que empiezan con $ en 'precio': {dollar_start_values}")
    assert dollar_start_values >= 0, "El conteo de registros que comienzan con $ no es correcto."

