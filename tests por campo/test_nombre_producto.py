import pandas as pd
import pytest
import re
import logging

'''
@uthor: José Luis García Quinayás
date: 22/11/2024
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
pytest test_nombre_producto.py -v --tb=short --log-cli-level=INFO --html=report_campo_nombre_producto.html --self-contained-html

'''

# Configuración del logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def load_data():
    '''Carga los datos desde el archivo especificado.'''
    file_path = "O:/productos/ventas1.xlsx"
    data = pd.read_excel(file_path)
    return data

# Caso de prueba 1: Identificar registros con caracteres especiales en nombre_producto
def test_find_special_characters(load_data):
    '''Caso de prueba 1: Identificar si hay registros con caracteres especiales en la columna nombre_producto.'''
    data = load_data
    special_chars = data['nombre_producto'].apply(lambda x: bool(re.search(r'[^A-Za-z0-9\s]', str(x))))
    logger.info(f"Registros con caracteres especiales encontrados: {special_chars.sum()}")
    assert special_chars.any(), "No se encontraron caracteres especiales en nombre_producto."

# Caso de prueba 2: Contar registros con caracteres especiales en nombre_producto
def test_count_special_characters(load_data):
    '''Caso de prueba 2: Contar los registros con caracteres especiales en la columna nombre_producto.'''
    data = load_data
    special_chars = data['nombre_producto'].apply(lambda x: bool(re.search(r'[^A-Za-z0-9\s]', str(x))))
    logger.info(f"Total de registros con caracteres especiales: {special_chars.sum()}")
    assert special_chars.sum() >= 0, "Error en el conteo de caracteres especiales."

# Caso de prueba 3: Validar cantidad de registros con caracteres especiales en nombre_producto
@pytest.mark.parametrize("expected_count", [1341])  # Cambia 50 al valor esperado real
def test_validate_special_count(load_data, expected_count):
    '''Caso de prueba 3: Validar si la cantidad de registros con caracteres especiales en nombre_producto corresponde a un valor específico (n).'''
    data = load_data
    # Identificar caracteres especiales usando una expresión regular
    special_pattern = re.compile(r'[^a-zA-Z0-9\s]')  # Caracteres especiales: no alfanuméricos y no espacios
    special_count = data['nombre_producto'].apply(lambda x: bool(special_pattern.search(x)) if isinstance(x, str) else False).sum()
    
    # Log de resultados
    logger.info(f"Registros con caracteres especiales: {special_count} (esperados: {expected_count})")
    
    # Validar que la cantidad de registros coincide con el valor esperado
    assert special_count == expected_count, (f"Se esperaban {expected_count} registros con caracteres especiales, pero se encontraron {special_count}.")

# Caso de prueba 4: Identificar registros con el valor 'Teclado'
def test_find_teclado(load_data):
    '''Caso de prueba 4: Identificar registros en la columna nombre_producto con el valor "Teclado".'''
    data = load_data
    teclado_records = data['nombre_producto'].str.contains('Teclado', na=False)
    logger.info(f"Registros con 'Teclado' encontrados: {teclado_records.sum()}")
    assert teclado_records.any(), "No se encontraron registros con el valor 'Teclado'."

# Caso de prueba 5: Contar registros con el valor 'Teclado'
def test_count_teclado(load_data):
    '''Caso de prueba 5: Contar cuántos registros tienen el valor "Teclado".'''
    data = load_data
    teclado_count = data['nombre_producto'].str.contains('Teclado', na=False).sum()
    logger.info(f"Total de registros con el valor 'Teclado': {teclado_count}")
    assert teclado_count >= 0, "Error en el conteo de 'Teclado'."

# Caso de prueba 6: Validar cantidad de registros con el valor 'Teclado'
@pytest.mark.parametrize("expected_count", [655])  # Cambia 50 al valor esperado real
def test_validate_teclado_count(load_data, expected_count):
    '''Caso de prueba 6: Validar si la cantidad de registros con el nombre "Teclado" corresponde a un valor específico (n).'''
    data = load_data
    teclado_count = data['nombre_producto'].str.contains('Teclado', na=False).sum()
    logger.info(f"Registros con 'Teclado': {teclado_count} (esperados: {expected_count})")
    assert teclado_count == expected_count, f"Se esperaban {expected_count} 'Teclado', pero se encontraron {teclado_count}."

# Caso de prueba 7: Identificar registros con el valor 'Mouse'
def test_find_mouse(load_data):
    '''Caso de prueba 7: Identificar registros en la columna nombre_producto con el valor "Mouse".'''
    data = load_data
    mouse_records = data['nombre_producto'].str.contains('Mouse', na=False)
    logger.info(f"Registros con 'Mouse' encontrados: {mouse_records.sum()}")
    assert mouse_records.any(), "No se encontraron registros con el valor 'Mouse'."

# Caso de prueba 8: Contar registros con el valor 'Mouse'
def test_count_mouse(load_data):
    '''Caso de prueba 8: Contar cuántos registros tienen el valor "Mouse".'''
    data = load_data
    mouse_count = data['nombre_producto'].str.contains('Mouse', na=False).sum()
    logger.info(f"Total de registros con el valor 'Mouse': {mouse_count}")
    assert mouse_count >= 0, "Error en el conteo de 'Mouse'."

# Caso de prueba 9: Validar cantidad de registros con el valor 'Mouse'
@pytest.mark.parametrize("expected_count", [718])  # Cambia 30 al valor esperado real
def test_validate_mouse_count(load_data, expected_count):
    '''Caso de prueba 9: Validar si la cantidad de registros con el nombre "Mouse" corresponde a un valor específico (n).'''
    data = load_data
    mouse_count = data['nombre_producto'].str.contains('Mouse', na=False).sum()
    logger.info(f"Registros con 'Mouse': {mouse_count} (esperados: {expected_count})")
    assert mouse_count == expected_count, f"Se esperaban {expected_count} 'Mouse', pero se encontraron {mouse_count}."

# Caso de prueba 10: Identificar registros con el valor 'Auriculares'
def test_find_auriculares(load_data):
    """Caso de prueba 10: Identificar registros con el valor 'Auriculares' en la columna nombre_producto."""
    data = load_data
    auriculares_records = data['nombre_producto'].str.contains('Auriculares', na=False)
    logger.info(f"Registros con 'Auriculares' encontrados: {auriculares_records.sum()}")
    assert auriculares_records.any(), "No se encontraron registros con el valor 'Auriculares'."

# Caso de prueba 11: Contar registros con el valor 'Auriculares'
def test_count_auriculares(load_data):
    """Caso de prueba 11: Contar registros con el valor 'Auriculares'."""
    data = load_data
    auriculares_count = data['nombre_producto'].str.contains('Auriculares', na=False).sum()
    logger.info(f"Total de registros con el valor 'Auriculares': {auriculares_count}")
    assert auriculares_count >= 0, "Error en el conteo de 'Auriculares'."

# Caso de prueba 12: Validar cantidad de registros con el valor 'Auriculares'
@pytest.mark.parametrize("expected_count", [643])  # Cambia 30 al valor esperado real
def test_validate_auriculares_count(load_data, expected_count):
    '''Caso de prueba 12: Validar si la cantidad de registros con el nombre "Auriculares" corresponde a un valor específico (n).'''
    data = load_data
    auriculares_count = data['nombre_producto'].str.contains('Auriculares', na=False).sum()
    logger.info(f"Registros con 'Auriculares': {auriculares_count} (esperados: {expected_count})")
    assert auriculares_count == expected_count, f"Se esperaban {expected_count} 'Auriculares', pero se encontraron {auriculares_count}."

# Caso de prueba 13: Contar registros que comienzan con 'A'
def test_count_starts_with_a(load_data):
    """Caso de prueba 13: Contar registros en nombre_producto que comienzan con 'A'."""
    data = load_data
    starts_with_a = data['nombre_producto'].str.startswith('A', na=False)
    logger.info(f"Registros que comienzan con 'A': {starts_with_a.sum()}")
    assert starts_with_a.sum() >= 0, "Error al contar registros que comienzan con 'A'."

# Caso de prueba 14: Validar número específico de registros que comienzan con 'A'
@pytest.mark.parametrize("expected_count", [643])  # Cambia 100 al valor esperado real
def test_validate_starts_with_a_count(load_data, expected_count):
    """Caso de prueba 14: Validar número específico de registros que comienzan con 'A'."""
    data = load_data
    starts_with_a = data['nombre_producto'].str.startswith('A', na=False).sum()
    logger.info(f"Registros que comienzan con 'A': {starts_with_a} (esperados: {expected_count})")
    assert starts_with_a == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {starts_with_a}."

# Caso de prueba 15: Contar registros que comienzan con 'E'
def test_count_starts_with_e(load_data):
    """Caso de prueba 15: Contar registros en nombre_producto que comienzan con 'E'."""
    data = load_data
    starts_with_e = data['nombre_producto'].str.startswith('e', na=False)
    logger.info(f"Registros que comienzan con 'E': {starts_with_e.sum()}")
    assert starts_with_e.sum() >= 0, "Error al contar registros que comienzan con 'E'."

# Caso de prueba 16: Validar número específico de registros que comienzan con 'E'
@pytest.mark.parametrize("expected_count", [21])  # Cambia 100 al valor esperado real
def test_validate_starts_with_e_count(load_data, expected_count):
    """Caso de prueba 16: Validar número específico de registros que comienzan con 'E'."""
    data = load_data
    starts_with_e = data['nombre_producto'].str.startswith('e', na=False).sum()
    logger.info(f"Registros que comienzan con 'E': {starts_with_e} (esperados: {expected_count})")
    assert starts_with_e == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {starts_with_e}."

# Caso de prueba 17: Contar registros que comienzan con 'T'
def test_count_starts_with_t_mayus(load_data):
    """Caso de prueba 17: Contar registros en nombre_producto que comienzan con 'T'."""
    data = load_data
    starts_with_t_mayus = data['nombre_producto'].str.startswith('T', na=False)
    logger.info(f"Registros que comienzan con 'T': {starts_with_t_mayus.sum()}")
    assert starts_with_t_mayus.sum() >= 0, "Error al contar registros que comienzan con 'T'."

# Caso de prueba 18: Validar número específico de registros que comienzan con 'T'
@pytest.mark.parametrize("expected_count", [2671])  # Cambia 100 al valor esperado real
def test_validate_starts_with_t_count_mayus(load_data, expected_count):            
    """Caso de prueba 18: Validar número específico de registros que comienzan con 'T'."""
    data = load_data
    starts_with_t_mayus = data['nombre_producto'].str.startswith('T', na=False).sum()
    logger.info(f"Registros que comienzan con 'T': {starts_with_t_mayus} (esperados: {expected_count})")
    assert starts_with_t_mayus == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {starts_with_t_mayus}."

# Caso de prueba 19: Contar registros que comienzan con 'S'
def test_count_starts_with_s(load_data):
    """Caso de prueba 19: Contar registros en nombre_producto que comienzan con 'S'."""
    data = load_data
    starts_with_s = data['nombre_producto'].str.startswith('s', na=False)
    logger.info(f"Registros que comienzan con 'S': {starts_with_s.sum()}")
    assert starts_with_s.sum() >= 0, "Error al contar registros que comienzan con 'S'."

# Caso de prueba 20: Validar número específico de registros que comienzan con 'S'
@pytest.mark.parametrize("expected_count", [14])  # Cambia 100 al valor esperado real
def test_validate_starts_with_s_count(load_data, expected_count):
    """Caso de prueba 20: Validar número específico de registros que comienzan con 'S'."""
    data = load_data
    starts_with_s = data['nombre_producto'].str.startswith('s', na=False).sum()
    logger.info(f"Registros que comienzan con 'S': {starts_with_s} (esperados: {expected_count})")
    assert starts_with_s == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {starts_with_s}."

# Caso de prueba 21: Contar registros que comienzan con 'M'
def test_count_starts_with_m(load_data):
    """Caso de prueba 21: Contar registros en nombre_producto que comienzan con 'M'."""
    data = load_data
    starts_with_m = data['nombre_producto'].str.startswith('M', na=False)
    logger.info(f"Registros que comienzan con 'M': {starts_with_m.sum()}")
    assert starts_with_m.sum() >= 0, "Error al contar registros que comienzan con 'M'."

# Caso de prueba 22: Validar número específico de registros que comienzan con 'M'
@pytest.mark.parametrize("expected_count", [718])  # Cambia 100 al valor esperado real
def test_validate_starts_with_m_count(load_data, expected_count):
    """Caso de prueba 22: Validar número específico de registros que comienzan con 'M'."""
    data = load_data
    starts_with_m = data['nombre_producto'].str.startswith('M', na=False).sum()
    logger.info(f"Registros que comienzan con 'M': {starts_with_m} (esperados: {expected_count})")
    assert starts_with_m == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {starts_with_m}."

# Caso de prueba: Contar registros que comienzan con 't'
def test_count_starts_with_t_minus(load_data):
    """Caso de prueba: Contar registros en nombre_producto que comienzan con 't'."""
    data = load_data
    starts_with_t_minus = data['nombre_producto'].str.startswith('t', na=False)
    logger.info(f"Registros que comienzan con 't': {starts_with_t_minus.sum()}")
    assert starts_with_t_minus.sum() >= 0, "Error al contar registros que comienzan con 't'."

# Caso de prueba Validar número específico de registros que comienzan con 't'
@pytest.mark.parametrize("expected_count", [14])  # Cambia 100 al valor esperado real
def test_validate_starts_with_t_count_minus(load_data, expected_count):
    """Caso de prueba Validar número específico de registros que comienzan con 't'."""
    data = load_data
    starts_with_t_minus = data['nombre_producto'].str.startswith('t', na=False).sum()
    logger.info(f"Registros que comienzan con 't': {starts_with_t_minus} (esperados: {expected_count})")
    assert starts_with_t_minus == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {starts_with_t_minus}."

# Caso de prueba 23: Verificar registros nulos o vacíos en nombre_producto
def test_null_or_empty_nombre_producto(load_data):
    """Caso de prueba 23: Verificar si hay registros nulos o vacíos en nombre_producto."""
    data = load_data
    null_or_empty = data['nombre_producto'].isnull() | (data['nombre_producto'] == '')
    logger.info(f"Registros nulos o vacíos en nombre_producto: {null_or_empty.sum()}")
    assert null_or_empty.sum() == 0, "Se encontraron registros nulos o vacíos en nombre_producto."

# Caso de prueba 24: Verificar que nombre_producto no contenga valores numéricos
def test_nombre_producto_no_numbers(load_data):
    """Caso de prueba 24: Asegurar que nombre_producto no contenga valores numéricos."""
    data = load_data
    contains_numbers = data['nombre_producto'].apply(lambda x: bool(re.search(r'\d', str(x))))
    logger.info(f"Registros con números en nombre_producto: {contains_numbers.sum()}")
    assert contains_numbers.sum() == 0, "Se encontraron valores numéricos en nombre_producto."

# Caso de prueba 25: Contar registros con el carácter especial 'Ã¡'
def test_count_special_characters_o(load_data):
    """Caso de prueba 25: Contar registros con el carácter especial 'Ã¡'."""
    data = load_data
    contains_special_char_o = data['nombre_producto'].str.contains('Ã¡', na=False)
    logger.info(f"Registros con el carácter especial 'Ã¡': {contains_special_char_o.sum()}")
    assert contains_special_char_o.sum() >= 0, "Error al contar registros con 'Ã¡'."

# Caso de prueba 26: Contar registros con el carácter especial 'Ã©'
def test_count_special_characters_dot(load_data):
    """Caso de prueba 26: Contar registros con el carácter especial 'Ã©'."""
    data = load_data
    contains_special_char_dot = data['nombre_producto'].str.contains('Ã©', na=False)
    logger.info(f"Registros con el carácter especial 'Ã©': {contains_special_char_dot.sum()}")
    assert contains_special_char_dot.sum() >= 0, "Error al contar registros con 'Ã©'."

# Caso general para validar palabras específicas o letras iniciales en nombre_producto, para casos que van a tomar estado 'passed' y 'failed' 
@pytest.mark.parametrize(
    "filter_type, filter_value, expected_count",
    [
        ("word", "Teclado", 655),  # Colocar la cantidad esperada real
        ("word", "Mouse", 718),  # Colocar la cantidad esperada real
        ("word", "Auriculares", 643),  # Colocar la cantidad esperada real
        ("letter", "A", 643),          # Colocar la cantidad esperada real
        ("letter", "e", 21),           # Colocar la cantidad esperada real
        ("letter", "T", 2671),           # Colocar la cantidad esperada real
        ("letter", "s", 14),           # Colocar la cantidad esperada real
        ("letter", "M", 718),           # Colocar la cantidad esperada real
        ("special", "Ã¡", 672),         # Colocar la cantidad esperada real
        ("special", "Ã©", 669),         # Colocar la cantidad esperada real
        #datos errados para que arroje casos con estado 'failed'
        ("word", "Teclado", 55),  # Colocar la cantidad esperada real
        ("word", "Mouse", 18),  # Colocar la cantidad esperada real
        ("word", "Auriculares", 43),  # Colocar la cantidad esperada real
        ("letter", "A", 43),          # Colocar la cantidad esperada real
        ("letter", "e", 1),           # Colocar la cantidad esperada real
        ("letter", "T", 671),           # Colocar la cantidad esperada real
        ("letter", "s", 4),           # Colocar la cantidad esperada real
        ("letter", "M", 18),           # Colocar la cantidad esperada real
        ("special", "Ã¡", 72),         # Colocar la cantidad esperada real
        ("special", "Ã©", 69),         # Colocar la cantidad esperada real
    ],
)
def test_filter_nombre_producto(load_data, filter_type, filter_value, expected_count):
    """
    Caso general: Validar palabras específicas, letras iniciales o caracteres especiales en nombre_producto.
    - filter_type: Tipo de filtro ('word', 'letter', 'special').
    - filter_value: Valor del filtro (palabra, letra o carácter especial).
    - expected_count: Cantidad esperada de coincidencias.
    """
    data = load_data

    if filter_type == "word":
        # Filtrar por palabra específica
        filtered = data['nombre_producto'].str.contains(filter_value, na=False)
    elif filter_type == "letter":
        # Filtrar por letra inicial
        filtered = data['nombre_producto'].str.startswith(filter_value, na=False)
    elif filter_type == "special":
        # Filtrar por carácter especial
        filtered = data['nombre_producto'].str.contains(filter_value, na=False)
    else:
        pytest.fail(f"Tipo de filtro desconocido: {filter_type}")

    # Contar coincidencias
    count = filtered.sum()
    logger.info(f"Filtro '{filter_value}' ({filter_type}): {count} coincidencias (esperadas: {expected_count})")
    assert count == expected_count, f"Se esperaban {expected_count} coincidencias, pero se encontraron {count}."
