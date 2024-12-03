import pytest
import pandas as pd
import logging
import re

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
pytest test_categoria.py -v --tb=short --log-cli-level=INFO --html=report_campo_categoria.html --self-contained-html

'''

# Cargar datos desde el archivo Excel
@pytest.fixture
def load_data():
    '''Carga los datos desde el archivo ventas1.xlsx'''
    file_path = "O:/productos/ventas1.xlsx"  # Ruta del archivo
    data = pd.read_excel(file_path)
    return data

# Configurar logging para pytest
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Caso de prueba 1: Identificar registros con caracteres especiales en 'categoria'
def test_find_special_characters_in_categoria(load_data):
    '''Caso de prueba 1: Identificar registros con caracteres especiales en la columna categoria.'''
    data = load_data
    special_characters = data['categoria'].apply(lambda x: bool(re.search(r'[^A-Za-z0-9\s]', str(x))))
    special_count = special_characters.sum()
    logger.info(f"Total de registros con caracteres especiales: {special_count}")
    assert special_count >= 0, "No se encontraron registros con caracteres especiales en la columna 'categoria'"

# Caso de prueba 2: Contar registros con caracteres especiales en 'categoria'
def test_count_special_characters_in_categoria(load_data):
    '''Caso de prueba 2: Contar los registros con caracteres especiales en la columna categoria.'''
    data = load_data
    special_characters = data['categoria'].apply(lambda x: bool(re.search(r'[^A-Za-z0-9\s]', str(x))))
    special_count = special_characters.sum()
    logger.info(f"Total de registros con caracteres especiales: {special_count}")
    assert special_count >= 0, "No se encontraron registros con caracteres especiales en la columna 'categoria'"

# Caso de prueba 3: Validar que hay exactamente 3398 registros con caracteres especiales
def test_exact_special_characters_count(load_data):
    '''Caso de prueba 3: Validar que hay exactamente 3398 registros con caracteres especiales en 'categoria'.'''
    data = load_data
    special_characters = data['categoria'].apply(lambda x: bool(re.search(r'[^A-Za-z0-9\s]', str(x))))
    special_count = special_characters.sum()
    logger.info(f"Registros esperados con caracteres especiales: {special_count}")
    assert special_count == 3398, f"Se encontraron {special_count}, pero se esperaban 3398 registros."

#@pytest.mark.skip
# Caso de prueba 4: Identificar registros sin caracteres especiales en la columna `categoria`.
def test_find_non_special_characters(load_data):
    '''Caso de prueba 4: Identificar registros sin caracteres especiales en la columna `categoria`.'''
    # Cargar los datos
    data = load_data
    # Filtrar registros sin caracteres especiales
    non_special_characters = data['categoria'].dropna().str.contains(r'^[a-zA-Z0-9\s]+$', regex=True) 
    # Registrar resultados
    non_special_characters_count = non_special_characters.sum()
    logger.info(f"Total de registros sin caracteres especiales en 'categoria': {non_special_characters_count}")
    # Validar que existan registros
    assert non_special_characters_count >= 0, "No se encontraron registros sin caracteres especiales en 'categoria'."

#@pytest.mark.skip
# Caso de prueba 5: Contar registros sin caracteres especiales en la columna `categoria`.
def test_count_non_special_characters(load_data):
    '''Caso de prueba 5: Contar registros sin caracteres especiales en la columna `categoria`.'''
    # Cargar los datos
    data = load_data
    # Contar registros sin caracteres especiales
    non_special_characters_count = data['categoria'].dropna().str.contains(r'^[a-zA-Z0-9\s]+$', regex=True).sum()
    # Registrar resultados
    logger.info(f"Total de registros sin caracteres especiales en 'categoria': {non_special_characters_count}") 
    # Validar el resultado
    assert non_special_characters_count >= 0, "No se encontraron registros sin caracteres especiales en 'categoria'."

#@pytest.mark.skip
# Caso de prueba 6: Validar que hay exactamente 2686 registros sin caracteres especiales.
@pytest.mark.parametrize("expected_count", [2686])  # Parametrizar con el número esperado
def test_exact_non_special_characters(load_data, expected_count):
    '''Caso de prueba 6: Validar que hay exactamente 2686 registros sin caracteres especiales.'''
    # Cargar los datos
    data = load_data
    # Contar registros sin caracteres especiales
    non_special_characters_count = data['categoria'].dropna().str.contains(r'^[a-zA-Z0-9\s]+$', regex=True).sum()  
    # Registrar resultados
    logger.info(f"Total de registros sin caracteres especiales: {non_special_characters_count}") 
    # Verificar que coincida con el número esperado
    assert non_special_characters_count == expected_count, (f"Se esperaban {expected_count} registros, pero se encontraron {non_special_characters_count}.")

#@pytest.mark.skip
# Caso de prueba 7: Identificar registros en 'categoria' con el valor "Audio".
def test_find_audio_in_category(load_data):
    '''Caso de prueba 7: Identificar registros en 'categoria' con el valor "Audio".'''
    data = load_data
    audio_records = data[data['categoria'].str.strip().str.contains('Audio', case=False, na=False)]
    logger.info(f"Registros con valor 'Audio': {len(audio_records)}")
    assert len(audio_records) >= 0, "No se encontraron registros con el valor 'Audio'."

#@pytest.mark.skip
# Caso de prueba 8: Contar registros en 'categoria' con el valor "Audio".
def test_count_audio_in_category(load_data):
    '''Caso de prueba 8: Contar registros en 'categoria' con el valor "Audio".'''
    data = load_data
    audio_count = data['categoria'].str.strip().str.contains('Audio', case=False, na=False).sum()
    logger.info(f"Cantidad de registros con valor 'Audio': {audio_count}")
    assert audio_count >= 0, "No se encontraron registros con el valor 'Audio'."

#@pytest.mark.skip
# Caso de prueba 9: Validar que hay exactamente 655 registros con el valor "Audio".
@pytest.mark.parametrize("expected_count", [655])
def test_validate_audio_count(load_data, expected_count):
    '''Caso de prueba 9: Validar que hay exactamente 655 registros con el valor "Audio".'''
    data = load_data
    audio_count = data['categoria'].str.strip().str.contains('Audio', case=False, na=False).sum()
    logger.info(f"Total de registros con valor 'Audio': {audio_count}")
    assert audio_count == expected_count, (f"Se esperaban {expected_count} registros con el valor 'Audio', pero se encontraron {audio_count}.")

def test_find_office_category(load_data):
    '''Caso de prueba 10: Identificar si existen registros en la columna 'categoria' con el valor 'Oficina'.'''
    data = load_data
    office_records = data[data['categoria'].str.strip().str.contains('Oficina', case=False, na=False)]
    logger.info(f"Registros con el valor 'Oficina' en 'categoria': {len(office_records)}")
    assert len(office_records) > 0, "No se encontraron registros con la categoría 'Oficina'."

def test_count_office_category(load_data):
    '''Caso de prueba 11: Contar cuántos registros existen en la columna 'categoria' con el valor 'Oficina'.'''
    data = load_data
    office_count = data['categoria'].str.strip().str.contains('Oficina', case=False, na=False).sum()
    logger.info(f"Total de registros con la categoría 'Oficina': {office_count}")
    assert office_count >= 0, "No se encontraron registros con la categoría 'Oficina'."

@pytest.mark.parametrize("expected_count", [624])
def test_validate_office_category_count(load_data, expected_count):
    '''Caso de prueba 12: Validar si la cantidad de registros con la categoría 'Oficina' corresponde a 624.'''
    data = load_data
    office_count = data['categoria'].str.strip().str.contains('Oficina', case=False, na=False).sum()
    logger.info(f"Registros que contienen 'Oficina': {office_count}")
    assert office_count == expected_count, (f"Se esperaban {expected_count} registros con 'Oficina', pero se encontraron {office_count}.")
 
#@pytest.mark.skip
def test_find_categories_starting_with_f(load_data):
    '''Caso de prueba 13: Identificar registros en la columna 'categoria' que comienzan con la letra 'F'.'''
    data = load_data
    f_records = data['categoria'].str.lower().str.startswith('f', na=False).sum()
    logger.info(f"Registros que comienzan con 'F': {f_records.sum()}")
    assert f_records.sum() >= 0, "No se encontraron registros que comiencen con 'F'."

#@pytest.mark.skip
def test_count_categories_starting_with_f(load_data):
    '''Caso de prueba 14: Contar los registros en la columna 'categoria' que comienzan con la letra 'F'.'''
    data = load_data
    f_count = data['categoria'].str.lower().str.startswith('f', na=False).sum()
    logger.info(f"Total de registros que comienzan con 'F': {f_count}")
    assert f_count >= 0, "No se encontraron registros que comiencen con 'F'."

#pytest.mark.skip
@pytest.mark.parametrize("expected_count", [670])
def test_validate_f_starting_count(load_data, expected_count):
    '''Caso de prueba 15: Validar si la cantidad de registros que comienzan con 'F' corresponde a 670.'''
    data = load_data
    f_count = data['categoria'].str.lower().str.startswith('f', na=False).sum()
    logger.info(f"Registros que comienzan con 'F': {f_count}")
    assert f_count == expected_count, (f"Se esperaban {expected_count} registros que comiencen con 'F', pero se encontraron {f_count}.")

#@pytest.mark.skip
def test_find_categories_starting_with_a(load_data):
    '''Caso de prueba 16: Identificar registros en la columna ‘categoria’ comienzan con la letra ‘A’.'''
    data = load_data
    a_records = data['categoria'].str.lower().str.startswith('a', na=False).sum()
    logger.info(f"Registros que comienzan con 'a': {a_records.sum()}")
    assert a_records.sum() > 0, "No se encontraron registros que comiencen con 'a'."

#@pytest.mark.skip
def test_count_categories_starting_with_a(load_data):
    '''Caso de prueba 17: Contar los registros en la columna 'categoria' que comienzan con la letra 'a'.'''
    data = load_data
    a_count = data['categoria'].str.lower().str.startswith('a', na=False).sum()
    logger.info(f"Total de registros que comienzan con 'a': {a_count}")
    assert a_count > 0, "No se encontraron registros que comiencen con 'a'."

#@pytest.mark.skip
@pytest.mark.parametrize("expected_count", [2062])
def test_validate_a_starting_count(load_data, expected_count):
    '''Caso de prueba 18: Validar si la cantidad de registros que comienzan con 'a' corresponde a 2062.'''
    data = load_data
    a_count_two = data['categoria'].str.lower().str.startswith('a', na=False).sum()
    logger.info(f"Registros que comienzan con 'a': {a_count_two}")
    assert a_count_two == expected_count, (f"Se esperaban {expected_count} registros que comiencen con 'a', pero se encontraron {a_count_two}.")

#@pytest.mark.skip
# Caso de prueba 19: Validar que no haya valores vacíos o nulos en la columna 'categoria'.
def test_detect_null_or_empty_values_in_category(load_data):
    '''Caso de prueba 19: Validar que existan valores vacíos o nulos en la columna 'categoria'.'''
    data = load_data
    # Contar valores nulos o vacíos
    null_or_empty_count = data['categoria'].isna().sum() + data['categoria'].str.strip().eq("").sum()
    logger.info(f"Valores nulos o vacíos encontrados en 'categoria': {null_or_empty_count}")  
    # Verificar que existan valores nulos o vacíos (caso positivo si existen)
    assert null_or_empty_count > 0, "No se encontraron valores nulos o vacíos en 'categoria', se esperaba al menos uno."

#@pytest.mark.skip
@pytest.mark.parametrize("expected_count", [36])
def test_validate_null_category_count(load_data, expected_count):
    '''Caso de prueba 20: Validar si la cantidad de registros vacíos o nulos en 'categoria' corresponde a 36.'''
    data = load_data
    null_count = data['categoria'].isnull().sum()
    logger.info(f"Registros vacíos o nulos en 'categoria': {null_count}")
    assert null_count == expected_count, (f"Se esperaban {expected_count} registros nulos, pero se encontraron {null_count}.")

# Caso 21: Identificar registros en `categoria` que contienen exclusivamente `Ã`
def test_find_categories_with_char_ao_two(load_data):
    '''Caso 21: Identificar registros en la columna `categoria` que contienen el carácter `Ã`.'''
    data = load_data
    contains_char_ao = data['categoria'].apply(lambda x: 'FotografÃ­a' in x if isinstance(x, str) else False)
    logger.info(f"Registros con el carácter `Ã` en `categoria`: {contains_char_ao.sum()}")
    assert contains_char_ao.sum() > 0, "No se encontraron registros con el carácter `Ã` en `categoria`."

# Caso 22: Contar registros en `categoria` que contienen exclusivamente `Ã`
def test_count_categories_with_char_ao_two(load_data):
    '''Caso 22: Contar los registros en `categoria` que contienen el carácter `Ã`.'''
    data = load_data
    count_char_ao = data['categoria'].apply(lambda x: 'FotografÃ­a' in x if isinstance(x, str) else False).sum()
    logger.info(f"Total de registros con el carácter `Ã` en `categoria`: {count_char_ao}")
    assert count_char_ao > 0, "No se encontraron registros con el carácter `Ã` en `categoria`."

@pytest.mark.parametrize("expected_count", [670])  # Ajusta el número esperado
def test_validate_category_case_insensitive_ao_count(load_data, expected_count):
    '''Caso adicional: Validar la cantidad de registros con el término `fotografÃ­a` (minúsculas y mayúsculas).'''
    data = load_data   
    # Contar registros que contienen 'fotografÃ­a' en minúsculas
    count_lowercase = data['categoria'].apply(lambda x: 'fotografÃ­a' in str(x).strip()).sum()
    # Contar registros que contienen 'FotografÃ­a' en mayúsculas
    count_uppercase = data['categoria'].apply(lambda x: 'FotografÃ­a' in str(x).strip()).sum()
    # Sumar ambos casos
    total_count = count_lowercase + count_uppercase
    
    logger.info(f"Registros con `fotografÃ­a` en minúsculas: {count_lowercase}")
    logger.info(f"Registros con `FotografÃ­a` en mayúsculas: {count_uppercase}")
    logger.info(f"Total de registros con `fotografÃ­a` (insensible a mayúsculas): {total_count}")
    
    # Verificar si la suma total corresponde al valor esperado
    assert total_count == expected_count, (f"Se esperaban {expected_count} registros, pero se encontraron {total_count}.")

# Caso 23: Identificar registros en `categoria` que contienen exclusivamente `Ã³`
def test_find_categories_with_char_ao(load_data):
    '''Caso 23: Identificar registros en la columna `categoria` que contienen el carácter `Ã³`.'''
    data = load_data
    contains_char_ao = data['categoria'].apply(lambda x: 'Ã³' in x if isinstance(x, str) else False)
    logger.info(f"Registros con el carácter `Ã³` en `categoria`: {contains_char_ao.sum()}")
    assert contains_char_ao.sum() > 0, "No se encontraron registros con el carácter `Ã³` en `categoria`."

# Caso 24: Contar registros en `categoria` que contienen exclusivamente `Ã³`
def test_count_categories_with_char_ao(load_data):
    '''Caso 24: Contar los registros en `categoria` que contienen el carácter `Ã³`.'''
    data = load_data
    count_char_ao = data['categoria'].apply(lambda x: 'Ã³' in x if isinstance(x, str) else False).sum()
    logger.info(f"Total de registros con el carácter `Ã³` en `categoria`: {count_char_ao}")
    assert count_char_ao > 0, "No se encontraron registros con el carácter `Ã³` en `categoria`."

# Caso 25: Validar si el número de registros en `categoria` con `Ã³` corresponde a 2728
@pytest.mark.parametrize("expected_count", [2728])
def test_validate_category_char_ao_count(load_data, expected_count):
    '''Caso 25: Validar si la cantidad de registros en `categoria` con el carácter `Ã³` corresponde a 2728.'''
    data = load_data
    count_char_ao = data['categoria'].apply(lambda x: 'Ã³' in x if isinstance(x, str) else False).sum()
    logger.info(f"Registros con el carácter `Ã³` en `categoria`: {count_char_ao}")
    assert count_char_ao == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {count_char_ao}."

# Caso general para validar palabras específicas o letras iniciales en nombre_producto, para casos que van a tomar estado 'failed', lo mismo que se hace en casos anteriores como 3,6,9,12,15,18,21,24,27

@pytest.mark.parametrize("test_case, column, filter_condition, expected_count", [
    ("Caso failed 1", "categoria", lambda x: x.strip() == "Accesorios", 1407),  # Registros con "Accesorios"
    ("Caso failed 2", "categoria", lambda x: x.strip() == "Audio", 655),  # Registros con "Audio"
    ("Caso failed 3", "categoria", lambda x: x.strip() == "ComputaciÃ³n", 1376),  # Registros con "ComputaciÃ³n"
    ("Caso failed 4", "categoria", lambda x: x.strip() == "ElectrÃ³nica", 1352),  # Registros con "ElectrÃ³nica"
    ("Caso failed 5", "categoria", lambda x: x.strip() == "FotografÃ­a", 670),  # Registros con "FotografÃ­a"
    ("Caso failed 6", "categoria", lambda x: x.strip() == "Oficina", 624),  # Registros con "Oficina"
    ("Caso failed 7", "categoria", lambda x: x.startswith("F"), 670),       # Registros que comienzan con "F"
    ("Caso failed 8", "categoria", lambda x: x.startswith("A"), 2062),      # Registros que comienzan con "A"
])

#@pytest.mark.skip
def test_validate_exact_count_failed(load_data, test_case, column, filter_condition, expected_count):
    '''
    Función unificada para validar la cantidad exacta de registros en diferentes casos de prueba.
    '''
    data = load_data
    # Filtrar registros según la condición proporcionada
    count = data[column].dropna().apply(filter_condition).sum()
    logger.info(f"{test_case}: Se encontraron {count} registros que cumplen la condición en la columna '{column}'.")  
    # Validar el número de registros
    assert count == expected_count, (f"{test_case}: Se esperaban {expected_count} registros, pero se encontraron {count}.")
