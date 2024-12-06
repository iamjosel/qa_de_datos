import pandas as pd
import pytest
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
pytest test_nombre_cliente.py -v --tb=short --log-cli-level=INFO --html=report_nombre_cliente.html --self-contained-html

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

# Caso de prueba 1: Identificar registros con caracteres especiales en 'nombre_cliente'
def test_find_special_characters(load_data):
    '''Caso de prueba 1: Identificar registros con caracteres especiales en la columna "nombre_cliente".'''
    data = load_data
    special_characters = data['nombre_cliente'].str.contains('|'.join(special_char), na=False)
    special_count = special_characters.sum()
    logger.info(f"Total de registros con caracteres especiales: {special_count}")
    assert special_count > 0, "No se encontraron registros con caracteres especiales"

# Caso de prueba 2: Verificar que haya exactamente 5316 registros con caracteres especiales
@pytest.mark.parametrize("expected_count", [5316])
def test_exact_special_characters_count(load_data, expected_count):
    '''Caso de prueba 2: Verificar que haya exactamente 5316 registros con caracteres especiales en "nombre_cliente".'''
    data = load_data
    special_count = data['nombre_cliente'].str.contains('|'.join(special_char), na=False).sum()
    if special_count == expected_count:
        logger.info(f"Efectivamente hay {special_count} registros con caracteres especiales en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {special_count}.")
        assert special_count == expected_count, f"Se esperaban {expected_count} registros con caracteres especiales, pero se encontraron {special_count}"

# Caso de prueba 3: Contar registros con el nombre "Miguel Torres"
def test_find_miguel_torres(load_data):
    '''Caso de prueba 3: Contar registros con el nombre "Miguel Torres" en la columna "nombre_cliente".'''
    data = load_data
    miguel_count = data['nombre_cliente'].str.contains("Miguel Torres", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Miguel Torres': {miguel_count}")
    assert miguel_count > 0, "No se encontraron registros con el nombre 'Miguel Torres'"

# Caso de prueba 4: Confirmar que hay exactamente 761 registros con "Miguel Torres"
@pytest.mark.parametrize("expected_count", [761])
def test_exact_miguel_torres_count(load_data, expected_count):
    '''Caso de prueba 4: Confirmar que hay exactamente 761 registros con "Miguel Torres" en "nombre_cliente".'''
    data = load_data
    miguel_count = data['nombre_cliente'].str.contains("Miguel Torres", na=False).sum()
    if miguel_count == expected_count:
        logger.info(f"Efectivamente hay {miguel_count} registros con nombre 'Miguel Torres' en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {miguel_count}.")
        assert miguel_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {miguel_count}"

# Caso de prueba 5: Contar registros con el nombre "Carlos"
def test_find_carlos(load_data):
    '''Caso de prueba 5: Contar registros con el nombre "Carlos" en la columna "nombre_cliente".'''
    data = load_data
    carlos_count = data['nombre_cliente'].str.contains("Carlos", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Carlos': {carlos_count}")
    assert carlos_count > 0, "No se encontraron registros con el nombre 'Carlos'"

# Caso de prueba 6: Confirmar que hay exactamente 747 registros con "Carlos"
@pytest.mark.parametrize("expected_count", [747])
def test_exact_carlos_count(load_data, expected_count):
    '''Caso de prueba 6: Confirmar que hay exactamente 747 registros con el nombre "Carlos".'''
    data = load_data
    carlos_count = data['nombre_cliente'].str.contains("Carlos", na=False).sum()
    if carlos_count == expected_count:
        logger.info(f"Efectivamente hay {carlos_count} registros con nombre 'Carlos' en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {carlos_count}.")
        assert carlos_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {carlos_count}"

# Caso de prueba 7: Contar registros con el nombre "Ana"
def test_find_ana(load_data):
    '''Caso de prueba 7: Contar registros con el nombre "Ana" en la columna "nombre_cliente".'''
    data = load_data
    ana_count = data['nombre_cliente'].str.contains("Ana", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Ana': {ana_count}")
    assert ana_count > 0, "No se encontraron registros con el nombre 'Ana'"

# Caso de prueba 8: Confirmar que hay exactamente 742 registros con "Ana"
@pytest.mark.parametrize("expected_count", [742])
def test_exact_ana_count(load_data, expected_count):
    '''Caso de prueba 8: Confirmar que hay exactamente 742 registros con el nombre "Ana".'''
    data = load_data
    ana_count = data['nombre_cliente'].str.contains("Ana", na=False).sum()
    if ana_count == expected_count:
        logger.info(f"Efectivamente hay {ana_count} registros con nombre 'Ana' en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {ana_count}.")
        assert ana_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {ana_count}"

# Caso de prueba 9: Contar registros que empiezan con la letra "J"
def test_find_names_starting_with_j(load_data):
    '''Caso de prueba 9: Contar registros que empiezan con la letra "J" en la columna "nombre_cliente".'''
    data = load_data
    names_with_j_count = data['nombre_cliente'].str.startswith("J", na=False).sum()
    logger.info(f"Total de registros que empiezan con la letra 'J': {names_with_j_count}")
    assert names_with_j_count > 0, "No se encontraron registros que empiecen con la letra 'J'"

# Caso de prueba 10: Confirmar que hay exactamente 743 registros que empiezan con "J"
@pytest.mark.parametrize("expected_count", [743])
def test_exact_names_starting_with_j(load_data, expected_count):
    '''Caso de prueba 10: Confirmar que hay exactamente 743 registros que empiezan con "J".'''
    data = load_data
    names_with_j_count = data['nombre_cliente'].str.startswith("J", na=False).sum()
    if names_with_j_count == expected_count:
        logger.info(f"Efectivamente hay {names_with_j_count} registros que comienzan con 'J' en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {names_with_j_count}.")
        assert names_with_j_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {names_with_j_count}"

# Caso de prueba 11: Contar registros vacíos en 'nombre_cliente'
def test_count_empty_names(load_data):
    '''Caso de prueba 11: Contar registros vacíos en la columna "nombre_cliente".'''
    data = load_data
    empty_names_count = data['nombre_cliente'].isna().sum()
    logger.info(f"Total de registros vacíos en 'nombre_cliente': {empty_names_count}")
    assert empty_names_count > 0, "No se encontraron registros vacíos"

# Caso de prueba 12: Confirmar que hay exactamente 43 registros vacíos en 'nombre_cliente'
@pytest.mark.parametrize("expected_count", [43])
def test_exact_empty_names_count(load_data, expected_count):
    '''Caso de prueba 12: Confirmar que hay exactamente 43 registros vacíos en "nombre_cliente".'''
    data = load_data
    empty_names_count = data['nombre_cliente'].isna().sum()
    if empty_names_count == expected_count:
        logger.info(f"Efectivamente hay {empty_names_count} registros vacíos en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {empty_names_count}.")
        assert empty_names_count == expected_count, f"Se esperaban {expected_count} registros vacíos, pero se encontraron {empty_names_count}"

# Caso de prueba 13: Contar registros con el carácter especial "Ã³"
def test_find_special_character_ao(load_data):
    '''Caso de prueba 13: Contar registros con el carácter especial "Ã³" en la columna "nombre_cliente".'''
    data = load_data
    ao_count = data['nombre_cliente'].str.contains("Ã³", na=False).sum()
    logger.info(f"Total de registros con el carácter especial 'Ã³': {ao_count}")
    assert ao_count > 0, "No se encontraron registros con el carácter especial 'Ã³'"

# Caso de prueba 14: Confirmar que hay exactamente 1544 registros con "Ã³"
@pytest.mark.parametrize("expected_count", [1544])
def test_exact_special_character_ao_count(load_data, expected_count):
    '''Caso de prueba 14: Confirmar que hay exactamente 1544 registros con el carácter especial "Ã³".'''
    data = load_data
    ao_count = data['nombre_cliente'].str.contains("Ã³", na=False).sum()
    if ao_count == expected_count:
        logger.info(f"Efectivamente hay {ao_count} registros que contienen el caracter especial Ã³ en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {ao_count}.")
        assert ao_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {ao_count}"

# Caso de prueba 15: Contar registros con el carácter especial "Ã©"
def test_find_special_character_ae(load_data):
    '''Caso de prueba 15: Contar registros con el carácter especial "Ã©" en la columna "nombre_cliente".'''
    data = load_data
    ae_count = data['nombre_cliente'].str.contains("Ã©", na=False).sum()
    logger.info(f"Total de registros con el carácter especial 'Ã©': {ae_count}")
    assert ae_count > 0, "No se encontraron registros con el carácter especial 'Ã©'"

# Caso de prueba 16: Confirmar que hay exactamente 743 registros con "Ã©"
@pytest.mark.parametrize("expected_count", [743])
def test_exact_special_character_ae_count(load_data, expected_count):
    '''Caso de prueba 16: Confirmar que hay exactamente 743 registros con el carácter especial "Ã©".'''
    data = load_data
    ae_count = data['nombre_cliente'].str.contains("Ã©", na=False).sum()
    if ae_count == expected_count:
        logger.info(f"Efectivamente hay {ae_count} registros que contienen el caracter especial Ã© en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {ae_count}.")
        assert ae_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {ae_count}"

# Caso de prueba 17: Contar registros numéricos en 'nombre_cliente'
def test_find_numeric_names(load_data):
    '''Caso de prueba 17: Contar registros numéricos en la columna "nombre_cliente".'''
    data = load_data
    numeric_count = data['nombre_cliente'].str.isnumeric().sum()
    logger.info(f"Total de registros numéricos en 'nombre_cliente': {numeric_count}")
    assert numeric_count == 0, "Se encontraron registros numéricos en 'nombre_cliente'"

# Caso de prueba 18: Confirmar que hay exactamente 0 registros numéricos en 'nombre_cliente'
@pytest.mark.parametrize("expected_count", [0])
def test_exact_numeric_names_count(load_data, expected_count):
    '''Caso de prueba 18: Confirmar que hay exactamente 0 registros numéricos en "nombre_cliente".'''
    data = load_data
    numeric_count = data['nombre_cliente'].str.isnumeric().sum()
    if numeric_count == expected_count:
        logger.info(f"Efectivamente hay {numeric_count} registros numéricos en la columna 'nombre_cliente'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {numeric_count}.")
        assert numeric_count == expected_count, f"Se esperaban {expected_count} registros numéricos, pero se encontraron {numeric_count}"

@pytest.mark.parametrize(
    "test_name, validation_function, expected_value",
    [
        #Casos con datos inválidos para trabajar con el parametrize

        # Caso 2: Asegurarse de que hay 5315 registros con caracteres especiales en 'nombre_cliente'.
        ("Registros con caracteres especiales", lambda data: data['nombre_cliente'].str.contains('|'.join(special_char), na=False).sum(), 5315),
        
        # Caso 4: Confirmar que hay 761 registros con el nombre 'Miguel Torres'.
        ("Registros con 'Miguel Torres'", lambda data: (data['nombre_cliente'] == 'Miguel Torres').sum(), 760),
        
        # Caso 6: Confirmar que hay 747 registros que contienen el nombre 'Carlos'.
        ("Registros que contienen 'Carlos'", lambda data: data['nombre_cliente'].str.contains('Carlos', na=False).sum(), 746),
        
        # Caso 8: Confirmar que hay 742 registros que contienen el nombre 'Ana'.
        ("Registros que contienen 'Ana'", lambda data: data['nombre_cliente'].str.contains('Ana', na=False).sum(), 741),
        
        # Caso 10: Confirmar que hay 743 registros que empiezan con la letra 'J'.
        ("Registros que empiezan con 'J'", lambda data: data['nombre_cliente'].str.startswith('J', na=False).sum(), 742),
        
        # Caso 12: Confirmar que hay 43 registros vacíos en 'nombre_cliente'.
        ("Registros vacíos en 'nombre_cliente'", lambda data: data['nombre_cliente'].isna().sum(), 42),
        
        # Caso 14: Confirmar que hay 797 registros con el carácter especial 'Ã³'.
        ("Registros con el carácter especial 'Ã³'", lambda data: data['nombre_cliente'].str.contains('Ã³', na=False).sum(), 796),
        
        # Caso 16: Confirmar que hay 743 registros con el carácter especial 'Ã©'.
        ("Registros con el carácter especial 'Ã©'", lambda data: data['nombre_cliente'].str.contains('Ã©', na=False).sum(), 742),
        
        # Caso 18: Confirmar que hay 0 registros numéricos en 'nombre_cliente'.
        ("Registros numéricos en 'nombre_cliente'", lambda data: data['nombre_cliente'].apply(lambda x: isinstance(x, (int, float))).sum(), 1),
    ]
)
def test_nombre_cliente_validations(load_data, test_name, validation_function, expected_value):
    """
    Validaciones parametrizadas para la columna 'nombre_cliente'.
    """
    data = load_data
    result = validation_function(data)
    if result == expected_value:
        print(f"{test_name}: Validación exitosa. Resultado esperado y obtenido: {result}")
    else:
        print(f"{test_name}: Error. Se esperaba {expected_value}, pero se encontró {result}")
    assert result == expected_value, f"{test_name}: Se esperaba {expected_value}, pero se encontró {result}."
