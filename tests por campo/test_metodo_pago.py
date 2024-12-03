import pandas as pd
import pytest
import logging

'''
@uthor: José Luis García Quinayás
date: 03/12/2024
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
pytest test_metodo_pago.py -v --tb=short --log-cli-level=INFO --html=report_metodo_pago.html --self-contained-html

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

# Caso de prueba 1: Identificar registros con caracteres especiales en 'metodo_pago'
def test_find_special_characters(load_data):
    '''Caso de prueba 1: Identificar registros con caracteres especiales en la columna "metodo_pago".'''
    data = load_data
    special_characters = data['metodo_pago'].str.contains('|'.join(special_char), na=False)
    special_count = special_characters.sum()
    logger.info(f"Total de registros con caracteres especiales: {special_count}")
    assert special_count > 0, "No se encontraron registros con caracteres especiales"

# Caso de prueba 2: Verificar que haya exactamente 1577 registros con caracteres especiales
@pytest.mark.parametrize("expected_count", [1577])
def test_exact_special_characters_count(load_data, expected_count):
    '''Caso de prueba 2: Verificar que haya exactamente 1577 registros con caracteres especiales en "metodo_pago".'''
    data = load_data
    special_count = data['metodo_pago'].str.contains('|'.join(special_char), na=False).sum()
    if special_count == expected_count:
        logger.info(f"Efectivamente hay {special_count} registros con caracteres especiales en la columna 'metodo_pago'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {special_count}.")
        assert special_count == expected_count, f"Se esperaban {expected_count} registros con caracteres especiales, pero se encontraron {special_count}"

# Caso de prueba 3: Contar registros con el nombre "Efectivo"
def test_find_efectivo(load_data):
    '''Caso de prueba 3: Contar registros con el nombre "Efectivo" en la columna "metodo_pago".'''
    data = load_data
    efectivo_count = data['metodo_pago'].str.contains("Efectivo", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Efectivo': {efectivo_count}")
    assert efectivo_count > 0, "No se encontraron registros con el nombre 'Efectivo'"

# Caso de prueba 4: Confirmar que hay exactamente 1517 registros con "Efectivo"
@pytest.mark.parametrize("expected_count", [1517])
def test_exact_efectivo_count(load_data, expected_count):
    '''Caso de prueba 4: Confirmar que hay exactamente 1517 registros con "Efectivo" en "metodo_pago".'''
    data = load_data
    efectivo_count = data['metodo_pago'].str.contains("Efectivo", na=False).sum()
    if efectivo_count == expected_count:
        logger.info(f"Efectivamente hay {efectivo_count} registros con nombre 'Efectivo' en la columna 'metodo_pago'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {efectivo_count}.")
        assert efectivo_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {efectivo_count}"

# Caso de prueba 5: Contar registros con el nombre "PayPal"
def test_find_pay_pal(load_data):
    '''Caso de prueba 5: Contar registros con el nombre "PayPal" en la columna "metodo_pago".'''
    data = load_data
    pay_pal_count = data['metodo_pago'].str.contains("PayPal", na=False).sum()
    logger.info(f"Total de registros con el nombre 'PayPal': {pay_pal_count}")
    assert pay_pal_count > 0, "No se encontraron registros con el nombre 'PayPal'"

# Caso de prueba 6: Confirmar que hay exactamente 1523 registros con "PayPal"
@pytest.mark.parametrize("expected_count", [1523])
def test_exact_pay_pal_count(load_data, expected_count):
    '''Caso de prueba 6: Confirmar que hay exactamente 1523 registros con el nombre "PayPal".'''
    data = load_data
    pay_pal_count = data['metodo_pago'].str.contains("PayPal", na=False).sum()
    if pay_pal_count == expected_count:
        logger.info(f"Efectivamente hay {pay_pal_count} registros con nombre 'PayPal' en la columna 'metodo_pago'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {pay_pal_count}.")
        assert pay_pal_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {pay_pal_count}"

# Caso de prueba 7: Contar registros con el nombre "Tarjeta de CrÃ©dito"
def test_find_e(load_data):
    '''Caso de prueba 7: Contar registros con el nombre "Tarjeta de CrÃ©dito" en la columna "metodo_pago".'''
    data = load_data
    e_count = data['metodo_pago'].str.contains("Tarjeta de CrÃ©dito", na=False).sum()
    logger.info(f"Total de registros con el nombre 'Tarjeta de CrÃ©dito': {e_count}")
    assert e_count > 0, "No se encontraron registros con el nombre 'Tarjeta de CrÃ©dito'"

# Caso de prueba 8: Confirmar que hay exactamente 1577 registros con "Tarjeta de CrÃ©dito"
@pytest.mark.parametrize("expected_count", [1577])
def test_exact_e_count(load_data, expected_count):
    '''Caso de prueba 8: Confirmar que hay exactamente 1577 registros con el nombre "Tarjeta de CrÃ©dito".'''
    data = load_data
    e_count = data['metodo_pago'].str.contains("Tarjeta de CrÃ©dito", na=False).sum()
    if e_count == expected_count:
        logger.info(f"Efectivamente hay {e_count} registros con nombre 'Tarjeta de CrÃ©dito' en la columna 'metodo_pago'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {e_count}.")
        assert e_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {e_count}"

# Caso de prueba 9: Contar registros que contienen el nombre "Transferencia Bancaria"
def test_find_names_transfer_bank(load_data):
    '''Caso de prueba 9: Contar registros que contienen el nombre "Transferencia Bancaria" en la columna "metodo_pago".'''
    data = load_data
    transfer_bank = data['metodo_pago'].str.startswith("Transferencia Bancaria", na=False).sum()
    logger.info(f"Total de registros que contienen el nombre 'Transferencia Bancaria': {transfer_bank}")
    assert transfer_bank > 0, "No se encontraron registros que empiecen con la letra 'Transferencia Bancaria'"

# Caso de prueba 10: Confirmar que hay exactamente 1465 registros que empiezan con "Transferencia Bancaria"
@pytest.mark.parametrize("expected_count", [1465])
def test_exact_names_transfer_bank(load_data, expected_count):
    '''Caso de prueba 10: Confirmar que hay exactamente 1465 registros que empiezan con "Transferencia Bancaria".'''
    data = load_data
    transfer_bank = data['metodo_pago'].str.startswith("Transferencia Bancaria", na=False).sum()
    if transfer_bank == expected_count:
        logger.info(f"Efectivamente hay {transfer_bank} registros que comienzan con 'Transferencia Bancaria' en la columna 'metodo_pago'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {transfer_bank}.")
        assert transfer_bank == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {transfer_bank}"

# Caso de prueba 11: Contar registros vacíos en 'metodo_pago'
def test_count_empty_names(load_data):
    '''Caso de prueba 11: Contar registros vacíos en la columna "metodo_pago".'''
    data = load_data
    empty_names_count = data['metodo_pago'].isna().sum()
    logger.info(f"Total de registros vacíos en 'metodo_pago': {empty_names_count}")
    assert empty_names_count > 0, "No se encontraron registros vacíos"

# Caso de prueba 12: Confirmar que hay exactamente 38 registros vacíos en 'metodo_pago'
@pytest.mark.parametrize("expected_count", [38])
def test_exact_empty_names_count(load_data, expected_count):
    '''Caso de prueba 12: Confirmar que hay exactamente 38 registros vacíos en "metodo_pago".'''
    data = load_data
    empty_names_count = data['metodo_pago'].isna().sum()
    if empty_names_count == expected_count:
        logger.info(f"Efectivamente hay {empty_names_count} registros vacíos en la columna 'metodo_pago'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {empty_names_count}.")
        assert empty_names_count == expected_count, f"Se esperaban {expected_count} registros vacíos, pero se encontraron {empty_names_count}"

# Caso de prueba 13: Contar registros numéricos en 'metodo_pago'
def test_find_numeric_names(load_data):
    '''Caso de prueba 13: Contar registros numéricos en la columna "metodo_pago".'''
    data = load_data
    numeric_count = data['metodo_pago'].str.isnumeric().sum()
    logger.info(f"Total de registros numéricos en 'metodo_pago': {numeric_count}")
    assert numeric_count == 0, "Se encontraron registros numéricos en 'metodo_pago'"

# Caso de prueba 14: Confirmar que hay exactamente 0 registros numéricos en 'metodo_pago'
@pytest.mark.parametrize("expected_count", [0])
def test_exact_numeric_names_count(load_data, expected_count):
    '''Caso de prueba 14: Confirmar que hay exactamente 0 registros numéricos en "metodo_pago".'''
    data = load_data
    numeric_count = data['metodo_pago'].str.isnumeric().sum()
    if numeric_count == expected_count:
        logger.info(f"Efectivamente hay {numeric_count} registros numéricos en la columna 'metodo_pago'")
    else:
        logger.error(f"Error: Se esperaba el valor {expected_count}, pero se encontró {numeric_count}.")
        assert numeric_count == expected_count, f"Se esperaban {expected_count} registros numéricos, pero se encontraron {numeric_count}"

@pytest.mark.parametrize(
    "test_name, validation_function, expected_value",
    [
        #Casos con datos inválidos para trabajar con el parametrize

        # Caso 2: Asegurarse de que hay 1576 registros con caracteres especiales en 'metodo_pago'.
        ("Registros con caracteres especiales", 
         lambda data: data['metodo_pago'].str.contains('|'.join(special_char), na=False).sum(), 1576),
        
        # Caso 4: Confirmar que hay 1516 registros con el nombre 'Efectivo'.
        ("Registros con 'Efectivo'", lambda data: (data['metodo_pago'] == 'Efectivo').sum(), 1516),
        
        # Caso 6: Confirmar que hay 1522 registros que contienen el nombre 'PayPal'.
        ("Registros que contienen 'PayPal'", lambda data: data['metodo_pago'].str.contains('PayPal', na=False).sum(), 1522),
        
        # Caso 8: Confirmar que hay 1576 registros que contienen el nombre 'Tarjeta de CrÃ©dito'.
        ("Registros que contienen 'Tarjeta de CrÃ©dito'", lambda data: data['metodo_pago'].str.contains('Tarjeta de CrÃ©dito', na=False).sum(), 1576),
        
        # Caso 10: Confirmar que hay 1464 registros que contienen el nombre 'Transferencia Bancaria'.
        ("Registros que empiezan con 'Transferencia Bancaria'", lambda data: data['metodo_pago'].str.contains('Transferencia Bancaria', na=False).sum(), 1464),
        
        # Caso 12: Confirmar que hay 39 registros vacíos en 'metodo_pago'.
        ("Registros vacíos en 'metodo_pago'", lambda data: data['metodo_pago'].isna().sum(), 39),
        
        # Caso 18: Confirmar que hay 0 registros numéricos en 'metodo_pago'.
        ("Registros numéricos en 'metodo_pago'", lambda data: data['metodo_pago'].apply(lambda x: isinstance(x, (int, float))).sum(), 1),
    ]
)
def test_metodo_pago_validations(load_data, test_name, validation_function, expected_value):
    """Validaciones parametrizadas para la columna 'metodo_pago'."""
    data = load_data
    result = validation_function(data)
    if result == expected_value:
        print(f"{test_name}: Validación exitosa. Resultado esperado y obtenido: {result}")
    else:
        print(f"{test_name}: Error. Se esperaba {expected_value}, pero se encontró {result}")
    assert result == expected_value, f"{test_name}: Se esperaba {expected_value}, pero se encontró {result}."
