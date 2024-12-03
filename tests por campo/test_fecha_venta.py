import logging
import pandas as pd
import pytest
from datetime import datetime

'''
@uthor: José Luis García Quinayás
date: 21/11/2024
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
pytest test_fecha_venta.py -v --tb=short --log-cli-level=INFO --html=report_campo_fecha_venta.html --self-contained-html

'''

# Configurar logging para pytest en la consola
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar los datos desde el archivo XLSX
@pytest.fixture
def load_data():
    """Cargar datos del archivo ventas1.xlsx"""
    file_path = "O:/productos/ventas1.xlsx"
    return pd.read_excel(file_path)

# Caso de prueba 1: Localizar y contar los registros con el formato YYYY-MM-DD
def test_find_valid_dates(load_data):
    '''Caso de prueba 1: Localizar y contar los registros que cumplen con el formato de fecha YYYY-MM-DD.'''
    # Filtrar registros con el formato correcto
    data = load_data
    valid_dates = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is not pd.NaT)
    # Verificar cuántos cumplen el formato
    assert valid_dates.sum() > 0, "No se encontraron registros con el formato YYYY-MM-DD"

# Caso 2: Determinar el número total de registros que cumplen con el formato YYYY-MM-DD
def test_count_dates_yyyy_mm_dd(load_data):
    '''Caso de prueba 2: Determinar el número total de registros que cumplen con el formato YYYY-MM-DD.'''
    data = load_data
    valid_dates_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is not pd.NaT).sum()
    logger.info(f"Total de registros con formato YYYY-MM-DD: {valid_dates_count}")
    assert valid_dates_count > 0, "No se encontraron registros con formato YYYY-MM-DD"    

# Caso de prueba 3: Verificar si hay exactamente 5835 registros con el formato YYYY-MM-DD
#@pytest.mark.skip
@pytest.mark.parametrize("expected_count", [5835])  # En el [] se coloca el número obtenido en el caso 2
def test_exact_valid_dates_count(load_data, expected_count):
    '''Caso de prueba 3: Verificar si hay exactamente n registros con el formato YYYY-MM-DD.'''
    # Contar registros válidos
    data = load_data
    valid_dates_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is not pd.NaT).sum()
    # Comparar con el valor esperado
    assert valid_dates_count == expected_count, f"Se esperaban {expected_count} fechas válidas, pero se encontraron {valid_dates_count}"

# Caso de prueba 4: Localizar registros que utilicen el formato de fecha DD/MM/YYYY
def test_find_ddmmyyyy_dates(load_data):
    '''Caso de prueba 4: Localizar registros que utilicen el formato de fecha DD/MM/YYYY.'''
    # Filtrar registros con el formato DD/MM/YYYY
    data = load_data
    ddmmyyyy_dates = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%d/%m/%Y', errors='coerce') is not pd.NaT)
    # Verificar que existan registros
    assert ddmmyyyy_dates.sum() > 0, "No se encontraron registros con el formato DD/MM/YYYY"

# Caso 5: Determinar la cantidad de registros con el formato de fecha DD/MM/YYYY
def test_count_dates_dd_mm_yyyy(load_data):
    '''Caso de prueba 5: Determinar la cantidad de registros con el formato de fecha DD/MM/YYYY.'''
    data = load_data
    valid_dd_mm_yyyy_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%d/%m/%Y', errors='coerce') is not pd.NaT).sum()
    logger.info(f"Total de registros con formato DD/MM/YYYY: {valid_dd_mm_yyyy_count}")
    assert valid_dd_mm_yyyy_count >= 0, "No se encontraron registros con formato DD/MM/YYYY"

# Caso de prueba 6: Verificar si existen 234 registros con el formato DD/MM/YYYY
#@pytest.mark.skip
@pytest.mark.parametrize("expected_count", [234])  # En el [] se coloca el número obtenido en el caso 5
def test_exact_ddmmyyyy_dates_count(load_data, expected_count):
    '''Caso de prueba 6: Verificar si existen n registros con el formato DD/MM/YYYY.'''
    # Contar registros válidos
    data = load_data
    ddmmyyyy_dates_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%d/%m/%Y', errors='coerce') is not pd.NaT).sum()
    # Comparar con el valor esperado
    assert ddmmyyyy_dates_count == expected_count, f"Se esperaban {expected_count} fechas válidas, pero se encontraron {ddmmyyyy_dates_count}"

# Caso de prueba 7: Localizar y contar los registros que contengan el texto 'Fecha desconocida'
def test_find_unknown_dates(load_data):
    '''Caso de prueba 7: Localizar y contar los registros que contengan el texto 'Fecha desconocida'.'''
    # Filtrar registros con 'Fecha desconocida'
    data = load_data
    unknown_dates = data['fecha_venta'].dropna().str.contains('Fecha desconocida', na=False)
    # Verificar que existan registros
    assert unknown_dates.sum() > 0, "No se encontraron registros con el texto 'Fecha desconocida'"

# Caso 8: Determinar el número total de registros con el texto 'Fecha desconocida'
def test_count_unknown_dates(load_data):
    '''Caso de prueba 8: Determinar el número total de registros con el texto 'Fecha desconocida'.'''
    data = load_data
    unknown_dates_count = data['fecha_venta'].fillna('').str.contains('Fecha desconocida').sum()
    logger.info(f"Total de registros con 'Fecha desconocida': {unknown_dates_count}")
    assert unknown_dates_count >= 0, "No se encontraron registros con el texto 'Fecha desconocida'"

# Caso de prueba 9: Verificar si existen 4 registros con el texto 'Fecha desconocida'
#@pytest.mark.skip
@pytest.mark.parametrize("expected_count", [4])  # En el [] se coloca el número obtenido en el caso 8
def test_exact_unknown_dates_count(load_data, expected_count):
    '''Caso de prueba 9: Verificar si existen n registros con el texto 'Fecha desconocida'.'''
    # Contar registros con 'Fecha desconocida'
    data = load_data
    unknown_dates_count = data['fecha_venta'].dropna().str.contains('Fecha desconocida', na=False).sum()
    # Comparar con el valor esperado
    assert unknown_dates_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {unknown_dates_count}"

# Caso de prueba 10: Localizar registros con formatos de fecha diferentes al estándar YYYY-MM-DD
def test_find_non_standard_dates(load_data):
    '''Caso de prueba 10: Localizar registros con formatos de fecha diferentes al estándar YYYY-MM-DD.'''
    # Identificar registros que no cumplan el formato YYYY-MM-DD
    data = load_data
    non_standard_dates = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is pd.NaT)
    # Verificar que existan registros no estándar
    assert non_standard_dates.sum() > 0, "No se encontraron formatos de fecha no estándar"

# Caso 11: Determinar cuántos registros tienen un formato de fecha diferente a YYYY-MM-DD
def test_count_non_standard_dates(load_data):
    '''Caso de prueba 11: Determinar cuántos registros tienen un formato de fecha diferente a YYYY-MM-DD.'''
    data = load_data
    non_standard_dates_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is pd.NaT).sum()
    logger.info(f"Total de registros con formatos no estándar: {non_standard_dates_count}")
    assert non_standard_dates_count >= 0, "No se encontraron registros con formatos no estándar"

# Caso de prueba 12: Verificar si existen 238 registros con formatos distintos a YYYY-MM-DD
#@pytest.mark.skip
@pytest.mark.parametrize("expected_count", [238])  # En el [] se coloca el número obtenido en el caso 11
def test_exact_non_standard_dates_count(load_data, expected_count):
    '''Caso de prueba 12: Verificar si existen n registros con formatos distintos a YYYY-MM-DD.'''
    # Contar registros no estándar
    data = load_data
    non_standard_dates_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is pd.NaT).sum()
    # Comparar con el valor esperado
    assert non_standard_dates_count == expected_count, f"Se esperaban {expected_count} registros no estándar, pero se encontraron {non_standard_dates_count}"

# Caso de prueba 13: Localizar los registros en fecha_venta que estén vacíos o sean nulos
def test_find_empty_or_null_dates(load_data):
    '''Caso de prueba 13: Localizar los registros en fecha_venta que estén vacíos o sean nulos.'''
    # Identificar registros vacíos o nulos
    data = load_data
    empty_or_null_dates = data['fecha_venta'].isnull()
    # Verificar que existan registros vacíos o nulos
    assert empty_or_null_dates.sum() > 0, "No se encontraron registros vacíos o nulos en fecha_venta"

# Caso 14: Determinar la cantidad de registros vacíos o nulos en fecha_venta
def test_count_empty_or_null_dates(load_data):
    '''Caso de prueba 14: Determinar la cantidad de registros vacíos o nulos en fecha_venta.'''
    data = load_data
    empty_or_null_dates_count = data['fecha_venta'].isnull().sum()
    logger.info(f"Total de registros vacíos o nulos en fecha_venta: {empty_or_null_dates_count}")
    assert empty_or_null_dates_count >= 0, "No se encontraron registros vacíos o nulos en fecha_venta"

# Caso de prueba 15: Verificar si existen exactamente 47 registros vacíos o nulos en fecha_venta
#@pytest.mark.skip
@pytest.mark.parametrize("expected_count", [47])  # En el [] se coloca el número obtenido en el caso 14
def test_exact_empty_or_null_dates_count(load_data, expected_count):
    '''Caso de prueba 15: Verificar si existen exactamente n registros vacíos o nulos en fecha_venta.'''
    # Contar registros vacíos o nulos
    data = load_data
    empty_or_null_dates_count = data['fecha_venta'].isnull().sum()
    # Comparar con el valor esperado
    assert empty_or_null_dates_count == expected_count, f"Se esperaban {expected_count} registros vacíos o nulos, pero se encontraron {empty_or_null_dates_count}"

# Caso de prueba 16: Revisar que no haya fechas mayores a la actual
def test_no_future_dates(load_data):
    '''Caso de prueba 16: Revisar la columna fecha_venta para asegurarse de que no haya fechas mayores a la actual.'''
    # Filtrar fechas mayores a la actual
    data = load_data
    today = pd.Timestamp(datetime.now().date())
    future_dates = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, errors='coerce') > today)
    # Verificar que no existan fechas futuras
    assert future_dates.sum() == 0, "Se encontraron fechas mayores a la actual"

@pytest.mark.skip
# Caso de prueba: Validar si todos los datos en fecha_venta tienen el formato YYYY-MM-DD
def test_all_dates_in_standard_format(load_data):
    '''Caso de prueba: Validar si todos los datos en fecha_venta tienen el formato YYYY-MM-DD.'''
    # Cargar datos del archivo
    data = load_data
    
    # Verificar si todas las fechas cumplen el formato YYYY-MM-DD
    invalid_dates = data['fecha_venta'].dropna().apply(
        lambda x: not (isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is not pd.NaT))
    
    # Si hay fechas inválidas, generar un error
    assert invalid_dates.sum() == 0, f"Se encontraron {invalid_dates.sum()} fechas con formatos incorrectos"

'''Casos Negativos'''

# Caso de prueba 17: Verificar si hay exactamente 890 registros con el formato YYYY-MM-DD
@pytest.mark.parametrize("expected_count", [890])  # En el [] se coloca el número o valor esperado
def test_exact_valid_dates_count_error(load_data, expected_count):
    '''Caso de prueba 3: Verificar si hay exactamente n registros con el formato YYYY-MM-DD.'''
    # Contar registros válidos
    data = load_data
    valid_dates_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is not pd.NaT).sum()
    # Comparar con el valor esperado
    assert valid_dates_count == expected_count, f"Se esperaban {expected_count} fechas válidas, pero se encontraron {valid_dates_count}"

# Caso de prueba 18: Verificar si existen 300 registros con el formato DD/MM/YYYY
@pytest.mark.parametrize("expected_count", [300])  # En el [] se coloca el número o valor esperado
def test_exact_ddmmyyyy_dates_count_error(load_data, expected_count):
    '''Caso de prueba 6: Verificar si existen n registros con el formato DD/MM/YYYY.'''
    # Contar registros válidos
    data = load_data
    ddmmyyyy_dates_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%d/%m/%Y', errors='coerce') is not pd.NaT).sum()
    # Comparar con el valor esperado
    assert ddmmyyyy_dates_count == expected_count, f"Se esperaban {expected_count} fechas válidas, pero se encontraron {ddmmyyyy_dates_count}"

# Caso de prueba 19: Verificar si existen 55 registros con el texto 'Fecha desconocida'
@pytest.mark.parametrize("expected_count", [55])  # En el [] se coloca el número o valor esperado
def test_exact_unknown_dates_count_error(load_data, expected_count):
    '''Caso de prueba 9: Verificar si existen n registros con el texto 'Fecha desconocida'.'''
    # Contar registros con 'Fecha desconocida'
    data = load_data
    unknown_dates_count = data['fecha_venta'].dropna().str.contains('Fecha desconocida', na=False).sum()
    # Comparar con el valor esperado
    assert unknown_dates_count == expected_count, f"Se esperaban {expected_count} registros, pero se encontraron {unknown_dates_count}"

# Caso de prueba 20: Verificar si existen n registros con formatos distintos a YYYY-MM-DD
@pytest.mark.parametrize("expected_count", [333])  # En el [] se coloca el número o valor esperado
def test_exact_non_standard_dates_count_error(load_data, expected_count):
    '''Caso de prueba 12: Verificar si existen n registros con formatos distintos a YYYY-MM-DD.'''
    # Contar registros no estándar
    data = load_data
    non_standard_dates_count = data['fecha_venta'].dropna().apply(
        lambda x: isinstance(x, str) and pd.to_datetime(x, format='%Y-%m-%d', errors='coerce') is pd.NaT).sum()
    # Comparar con el valor esperado
    assert non_standard_dates_count == expected_count, f"Se esperaban {expected_count} registros no estándar, pero se encontraron {non_standard_dates_count}"

# Caso de prueba 21: Verificar si existen exactamente n registros vacíos o nulos en fecha_venta
@pytest.mark.parametrize("expected_count", [987])  # En el [] se coloca el número o valor esperado
def test_exact_empty_or_null_dates_count_error(load_data, expected_count):
    '''Caso de prueba 15: Verificar si existen exactamente n registros vacíos o nulos en fecha_venta.'''
    # Contar registros vacíos o nulos
    data = load_data
    empty_or_null_dates_count = data['fecha_venta'].isnull().sum()
    # Comparar con el valor esperado
    assert empty_or_null_dates_count == expected_count, f"Se esperaban {expected_count} registros vacíos o nulos, pero se encontraron {empty_or_null_dates_count}"