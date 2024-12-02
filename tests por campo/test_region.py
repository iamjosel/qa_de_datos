import pandas as pd
import pytest
import logging

'''@uthor: José Luis García Quinayás
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
pytest test_region.py -v --tb=short --log-cli-level=INFO --html=report_region.html --self-contained-html

'''

# Configurar logging para pytest en la consola
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def load_data():
    '''Carga los datos desde el archivo Excel especificado.'''
    # Cargar el archivo
    file_path = "O:/productos/ventas1.xlsx"
    data = pd.read_excel(file_path)
    return data

special_char = ['Ã³', 'Ã©', 'Ã¡', 'Ã']
regions = ['Centro', 'Este', 'Norte', 'Oeste', 'Sur' ]

# Caso de prueba 1: Identificar registros con caracteres especiales en 'region'
def test_find_special_characters(load_data):
    '''Caso de prueba 1: Identificar registros con caracteres especiales en la columna "region".'''
    data = load_data
    special_characters = data['region'].str.contains('|'.join(special_char), na=False)
    special_count = special_characters.sum()
    logger.info(f"Total de registros con caracteres especiales: {special_count}")
    assert special_count > 0, "No se encontraron registros con caracteres especiales"

# Caso de prueba 2: Verificar que haya exactamente 0 registros con caracteres especiales
@pytest.mark.parametrize("expected_count", [0])
def test_exact_special_characters_count(load_data, expected_count):
    '''Caso de prueba 2: Verificar que haya exactamente 0 registros con caracteres especiales en "region".'''
    data = load_data
    special_count = data['region'].str.contains('|'.join(special_char), na=False).sum()
    if special_count == expected_count:
        logger.info(f"Efectivamente hay {special_count} registros con caracteres especiales en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {special_count}.")
        assert special_count == expected_count, f"Se esperaban {expected_count} registros con caracteres especiales, pero se encontraron {special_count}"

# Caso de prueba 3: Contar registros con el valor "Centro"
def test_find_centro(load_data):
    '''Caso de prueba 3: Contar registros con el valor "Centro" en la columna "region".'''
    data = load_data
    centro_count = data['region'].str.contains("Centro", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Centro': {centro_count}")
    assert centro_count > 0, "No se encontraron registros con el nombre 'Centro'"

# Caso de prueba 4: Confirmar que hay exactamente 1172 registros con "Centro"
@pytest.mark.parametrize("expected_count", [1172])
def test_exact_centro_count(load_data, expected_count):
    '''Caso de prueba 4: Confirmar que hay exactamente 1172 registros con "Centro" en "region".'''
    data = load_data
    centro_count = data['region'].str.contains("Centro", na=False).sum()
    if centro_count == expected_count:
        logger.info(f"Efectivamente hay {centro_count} registros con nombre 'Centro' en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {centro_count}.")
        assert centro_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {centro_count}"

# Caso de prueba 5: Contar registros con el valor "Este"
def test_find_este(load_data):
    '''Caso de prueba 5: Contar registros con el valor "Este" en la columna "region".'''
    data = load_data
    este_count = data['region'].str.contains("Este", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Este': {este_count}")
    assert este_count > 0, "No se encontraron registros con el nombre 'Este'"

# Caso de prueba 6: Confirmar que hay exactamente 1238 registros con "Este"
@pytest.mark.parametrize("expected_count", [1238])
def test_exact_este_count(load_data, expected_count):
    '''Caso de prueba 6: Confirmar que hay exactamente 1238 registros con "Este" en "region".'''
    data = load_data
    este_count = data['region'].str.contains("Este", na=False).sum()
    if este_count == expected_count:
        logger.info(f"Efectivamente hay {este_count} registros con nombre 'Este' en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {este_count}.")
        assert este_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {este_count}"

# Caso de prueba 7: Contar registros con el valor "Norte"
def test_find_norte(load_data):
    '''Caso de prueba 7: Contar registros con el valor "Norte" en la columna "region".'''
    data = load_data
    norte_count = data['region'].str.contains("Norte", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Norte': {norte_count}")
    assert norte_count > 0, "No se encontraron registros con el nombre 'Norte'"

# Caso de prueba 8: Confirmar que hay exactamente 1195 registros con "Norte"
@pytest.mark.parametrize("expected_count", [1195])
def test_exact_norte_count(load_data, expected_count):
    '''Caso de prueba 8: Confirmar que hay exactamente 1195 registros con "Norte" en "region".'''
    data = load_data
    norte_count = data['region'].str.contains("Norte", na=False).sum()
    if norte_count == expected_count:
        logger.info(f"Efectivamente hay {norte_count} registros con nombre 'Norte' en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {norte_count}.")
        assert norte_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {norte_count}"

# Caso de prueba 9: Contar registros con el valor "Oeste"
def test_find_oeste(load_data):
    '''Caso de prueba 9: Contar registros con el valor "Oeste" en la columna "region".'''
    data = load_data
    oeste_count = data['region'].str.contains("Oeste", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Oeste': {oeste_count}")
    assert oeste_count > 0, "No se encontraron registros con el nombre 'Oeste'"

# Caso de prueba 10: Confirmar que hay exactamente 1217 registros con "Oeste"
@pytest.mark.parametrize("expected_count", [1217])
def test_exact_oeste_count(load_data, expected_count):
    '''Caso de prueba 10: Confirmar que hay exactamente 1217 registros con "Oeste" en "region".'''
    data = load_data
    oeste_count = data['region'].str.contains("Oeste", na=False).sum()
    if oeste_count == expected_count:
        logger.info(f"Efectivamente hay {oeste_count} registros con nombre 'Oeste' en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {oeste_count}.")
        assert oeste_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {oeste_count}"

# Caso de prueba 11: Contar registros con el valor "Sur"
def test_find_sur(load_data):
    '''Caso de prueba 11: Contar registros con el valor "Sur" en la columna "region".'''
    data = load_data
    sur_count = data['region'].str.contains("Sur", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Sur': {sur_count}")
    assert sur_count > 0, "No se encontraron registros con el nombre 'Sur'"

# Caso de prueba 12: Confirmar que hay exactamente 1257 registros con "Sur"
@pytest.mark.parametrize("expected_count", [1257])
def test_exact_sur_count(load_data, expected_count):
    '''Caso de prueba 12: Confirmar que hay exactamente 1257 registros con "Sur" en "region".'''
    data = load_data
    sur_count = data['region'].str.contains("Sur", na=False).sum()
    if sur_count == expected_count:
        logger.info(f"Efectivamente hay {sur_count} registros con nombre 'Sur' en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {sur_count}.")
        assert sur_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {sur_count}"

# Caso de prueba 13: Contar registros vacíos en 'region'
def test_count_empty_names(load_data):
    '''Caso de prueba 13: Contar registros vacíos en la columna "region".'''
    data = load_data
    empty_names_count = data['region'].isna().sum()
    logger.info(f"Total de registros vacíos en 'region': {empty_names_count}")
    assert empty_names_count > 0, "No se encontraron registros vacíos"

# Caso de prueba 14: Confirmar que hay exactamente 41 registros vacíos en 'region'
@pytest.mark.parametrize("expected_count", [41])
def test_exact_empty_names_count(load_data, expected_count):
    '''Caso de prueba 14: Confirmar que hay exactamente 41 registros vacíos en "region".'''
    data = load_data
    empty_names_count = data['region'].isna().sum()
    if empty_names_count == expected_count:
        logger.info(f"Efectivamente hay {empty_names_count} registros vacíos en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {empty_names_count}.")
        assert empty_names_count == expected_count, f"Se esperaban {expected_count} registros vacíos, pero se encontraron {empty_names_count}"

# Caso de prueba 15: Contar registros con valores distintos a 'Centro', 'Este', 'Norte', 'Oeste', Sur
def test_all_regions(load_data):
    """
    Caso de prueba 15: Contar registros con valores distintos a 'Centro', 'Este', 'Norte', 'Oeste', 'Sur'
    """
    data = load_data    
    # Filtrar registros que NO están en la lista de regiones válidas
    invalid_regions = ~data['region'].isin(regions)
    # Contar cuántos registros cumplen la condición
    all_count_regions = invalid_regions.sum()
    logger.info(f"Total de registros con valores distintos a 'Centro', 'Este', 'Norte', 'Oeste', 'Sur': {all_count_regions}") 
    # Validar que haya al menos un registro con valores distintos
    assert all_count_regions > 0, "No se encontraron registros distintos a 'Centro', 'Este', 'Norte', 'Oeste', 'Sur'"

@pytest.mark.parametrize("expected_count", [41])
def test_exact_all_count_regions(load_data, expected_count):
    """
    Caso de prueba 16: Confirmar que hay exactamente 41 registros con valores distintos 
    a 'Centro', 'Este', 'Norte', 'Oeste', 'Sur' en la columna 'region'.
    """
    data = load_data
    # Filtrar registros que NO están en la lista de regiones válidas
    invalid_regions = ~data['region'].isin(regions)
    all_count_regions = invalid_regions.sum()  # Sumar los valores que no pertenecen a 'regions'
    
    if all_count_regions == expected_count:
        logger.info(f"Validación exitosa: Hay exactamente {all_count_regions} registros con regiones no válidas.")
    else:
        logger.error(f"Error: Se esperaba {expected_count} registros, pero se encontraron {all_count_regions}.")
        assert all_count_regions == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {all_count_regions}."

# Caso de prueba 17: Contar registros que contienen la letra e en la columna region
def test_letter_e(load_data):
    '''Caso de prueba 17: Contar registros que contienen la letra e en la columna region'''
    data = load_data
    null_count = data['region'].str.contains("e", na=False).sum()
    logger.info(f"Total de registros con el nombre 'e': {null_count}")
    assert null_count > 0, "No se encontraron registros que contienen la letra 'e'"

# Caso de prueba 18: Confirmar que hay exactamente 4822 registros que contienen la letra "e"
@pytest.mark.parametrize("expected_count", [4822])
def test_exact_letter_e(load_data, expected_count):
    '''Caso de prueba 18: Confirmar que hay exactamente 4822 registros que contienen la letra "e"'''
    data = load_data
    null_count = data['region'].str.contains("e", na=False).sum()
    if null_count == expected_count:
        logger.info(f"Efectivamente hay {null_count} registros que contienen la letra 'e' en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {null_count}.")
        assert null_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {null_count}"

# Caso de prueba 19: Contar registros que contienen la letra o en la columna region
def test_letter_o(load_data):
    '''Caso de prueba 19: Contar registros que contienen la letra o en la columna region'''
    data = load_data
    null_count = data['region'].str.contains("o", na=False).sum()
    logger.info(f"Total de registros con el nombre 'e': {null_count}")
    assert null_count > 0, "No se encontraron registros que contienen la letra 'e'"

# Caso de prueba 20: Confirmar que hay exactamente 2367 registros que contienen la letra "o"
@pytest.mark.parametrize("expected_count", [2367])
def test_exact_letter_o(load_data, expected_count):
    '''Caso de prueba 20: Confirmar que hay exactamente 2367 registros que contienen la letra "o"'''
    data = load_data
    null_count = data['region'].str.contains("o", na=False).sum()
    if null_count == expected_count:
        logger.info(f"Efectivamente hay {null_count} registros que contienen la letra 'o' en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {null_count}.")
        assert null_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {null_count}"

# Caso de prueba 21: Contar registros numéricos en 'region'
def test_find_numeric_names(load_data):
    '''Caso de prueba 21: Contar registros numéricos en la columna "region".'''
    data = load_data
    numeric_count = data['region'].str.isnumeric().sum()
    logger.info(f"Total de registros numéricos en 'region': {numeric_count}")
    assert numeric_count == 0, "Se encontraron registros numéricos en 'region'"

# Caso de prueba 22: Confirmar que hay exactamente 0 registros numéricos en 'region'
@pytest.mark.parametrize("expected_count", [0])
def test_exact_numeric_names_count(load_data, expected_count):
    '''Caso de prueba 22: Confirmar que hay exactamente 0 registros numéricos en "region".'''
    data = load_data
    numeric_count = data['region'].str.isnumeric().sum()
    if numeric_count == expected_count:
        logger.info(f"Efectivamente hay {numeric_count} registros numéricos en la columna 'region'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {numeric_count}.")
        assert numeric_count == expected_count, f"Se esperaban {expected_count} registros numéricos, pero se encontraron {numeric_count}"

# Casos parametrizados con valores fallidos para trabajar con parametrize
@pytest.mark.parametrize(
    "test_name, validation_function, expected_value",
    [
        # Caso 2: Registros con caracteres especiales
        ("Caracteres especiales en 'region'", lambda data: data['region'].str.contains('|'.join(special_char), na=False).sum(), 1),
        
        # Caso 4: Registros con el valor "Centro"
        ("Registros con valor 'Centro'", lambda data: (data['region'] == "Centro").sum(), 1171),
        
        # Caso 6: Registros con el valor "Este"
        ("Registros con valor 'Este'", lambda data: (data['region'] == "Este").sum(), 1237),
        
        # Caso 8: Registros con el valor "Norte"
        ("Registros con valor 'Norte'", lambda data: (data['region'] == "Norte").sum(), 1194),
        
        # Caso 10: Registros con el valor "Oeste"
        ("Registros con valor 'Oeste'", lambda data: (data['region'] == "Oeste").sum(), 1216),
        
        # Caso 12: Registros con el valor "Sur"
        ("Registros con valor 'Sur'", lambda data: (data['region'] == "Sur").sum(), 1256),
        
        # Caso 14: Registros vacíos en 'region'
        ("Registros vacíos en 'region'", lambda data: data['region'].isna().sum(), 40),
            
        # Caso 18: Registros que contienen la letra "e"
        ("Registros con la letra 'e'", lambda data: data['region'].str.contains("e", case=False, na=False).sum(), 4821),
        
        # Caso 20: Registros que contienen la letra "o"
        ("Registros con la letra 'o'", lambda data: data['region'].str.contains("o", case=False, na=False).sum(), 3583),
    ]
)
def test_region_cases(load_data, test_name, validation_function, expected_value):
    """
    Casos de prueba parametrizados para validar la columna 'region'.
    """
    data = load_data
    result = validation_function(data)
    if result == expected_value:
        logger.info(f"{test_name}: Validación exitosa. Resultado esperado y obtenido: {result}")
    else:
        logger.error(f"{test_name}: Error. Se esperaba {expected_value}, pero se encontró {result}.")
    assert result == expected_value, f"{test_name}: Se esperaba {expected_value}, pero se encontró {result}."
