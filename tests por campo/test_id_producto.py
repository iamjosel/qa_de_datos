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
pytest test_id_producto.py -v --tb=short --log-cli-level=INFO --html=report_campo_id_producto.html --self-contained-html

'''

# Configurar logging para pytest en la consola
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def load_data():
    """Carga los datos desde el archivo Excel."""
    return pd.read_excel("O:/productos/ventas1.xlsx")

# '''Caso de prueba 1: Identificar qué valores en la columna id_producto son únicos.'''
def test_unique_values_in_id_producto(load_data):
    """Caso de prueba 1: Identificar valores únicos en id_producto."""
    # Identificar valores únicos
    unique_values = load_data['id_producto'].dropna().unique()
    print(f"Unique values: {unique_values}")
    assert len(unique_values) > 0  # Asegurarse de que existen valores únicos

# '''Caso de prueba 2: Contar cuántos valores únicos existen en la columna id_producto.'''
def test_count_unique_values_in_id_producto(load_data):
    """Caso de prueba 2: Contar valores únicos en id_producto."""
    # Contar valores únicos
    unique_count = load_data['id_producto'].dropna().nunique()
    print(f"Total unique values: {unique_count}")
    assert unique_count > 0  # Asegurarse de que el conteo es mayor a 0

# '''Caso de prueba 3: Confirmar que el número de valores únicos coincide con un valor específico (n).'''
def test_specific_count_unique_values(load_data):
    """Caso de prueba 3: Validar número específico de valores únicos."""
    n = 1716  # Aquí coloca el número específico esperado
    unique_count = load_data['id_producto'].dropna().nunique()
    print(f"Expected: {n}, Found: {unique_count}")
    assert unique_count == n  # Cambia 'n' por el valor que desees comparar

# '''Caso de prueba 4: Identificar qué registros tienen valores duplicados en la columna id_producto.'''
def test_duplicated_values_in_id_producto(load_data):
    """Caso de prueba 4: Identificar valores duplicados en id_producto."""
    duplicated = load_data[load_data['id_producto'].duplicated(keep=False)]
    print(f"Duplicated records:\n{duplicated}")
    assert not duplicated.empty  # Asegurarse de que existen duplicados

# '''Caso de prueba 5: Contar cuántos valores duplicados existen en la columna id_producto.'''
def test_count_duplicated_values(load_data):
    """Caso de prueba 5: Contar valores duplicados en id_producto."""
    duplicate_count = load_data['id_producto'].duplicated(keep=False).sum()
    print(f"Duplicate count: {duplicate_count}")
    assert duplicate_count > 0  # Asegurarse de que existen duplicados

# '''Caso de prueba 6: Confirmar que el número de valores duplicados coincide con un valor específico (n).'''
def test_specific_count_duplicated_values(load_data):
    """Caso de prueba 6: Validar número específico de duplicados."""
    n = 4404  # Aquí coloca el número específico esperado
    duplicate_count = load_data['id_producto'].duplicated(keep=False).sum()
    print(f"Expected: {n}, Found: {duplicate_count}")
    assert duplicate_count == n  # Cambia 'n' por el valor que desees comparar

# '''Caso de prueba 7: Comprobar que no existan registros nulos o vacíos en la columna id_producto.'''
def test_no_null_values_in_id_producto(load_data):
    """Caso de prueba 7: Validar que no existan valores nulos o vacíos."""
    null_count = load_data['id_producto'].isnull().sum()
    print(f"Null count: {null_count}")
    assert null_count == 0  # Asegurarse de que no hay nulos

# '''Caso de prueba 8: Asegurar que todos los valores de la columna id_producto sean numéricos.'''
def test_numeric_values_in_id_producto(load_data):
    """Caso de prueba 8: Validar que todos los valores sean numéricos."""
    non_numeric = load_data[~load_data['id_producto'].apply(lambda x: str(x).isdigit())]
    print(f"Non-numeric records:\n{non_numeric}")
    assert non_numeric.empty  # Asegurarse de que no hay valores no numéricos

# '''Caso de prueba 9: Asegurar que duplicados estén vinculados al mismo nombre_producto.'''
def test_duplicates_linked_to_same_name(load_data):
    """Caso de prueba 9: Validar que duplicados estén asociados al mismo nombre_producto."""
    duplicates = load_data[load_data['id_producto'].duplicated(keep=False)]
    mismatch = duplicates.groupby('id_producto')['nombre_producto'].nunique().gt(1)
    print(f"Duplicates with mismatched names:\n{duplicates[mismatch]}")
    assert mismatch.sum() == 0  # Asegurarse de que no hay inconsistencias

# '''Caso de prueba 10: Verificar que no existan registros con valores negativos en id_producto.'''
def test_no_negative_values_in_id_producto(load_data):
    """Caso de prueba 10: Validar que no hay valores negativos."""
    negative_values = load_data[load_data['id_producto'] < 0]
    print(f"Negative values:\n{negative_values}")
    assert negative_values.empty  # Asegurarse de que no hay negativos

# '''Caso de prueba 11: Asegurar que todos los valores sean positivos en id_producto.'''
def test_all_positive_values_in_id_producto(load_data):
    """Caso de prueba 11: Validar que todos los valores sean positivos."""
    non_positive = load_data[load_data['id_producto'] <= 0]
    print(f"Non-positive values:\n{non_positive}")
    assert non_positive.empty  # Asegurarse de que todos sean positivos

# Caso de prueba: Detectar cuántos id_producto tienen una cantidad específica de repeticiones
def test_detect_repetition_counts(load_data):
    '''Caso de prueba: Detectar cuántos id_producto tienen una cantidad específica de repeticiones.'''
    data = load_data
    repetition_counts = data['id_producto'].value_counts()
    repetition_summary = repetition_counts.value_counts()  # Frecuencia de cada cantidad de repeticiones
    logger.info(f"Resumen de repeticiones detectadas: \n{repetition_summary}")
    assert not repetition_summary.empty, "No se detectaron repeticiones en los id_producto."

# Caso de prueba con pytest.mark.parametrize: Validar las cantidades detectadas
@pytest.mark.parametrize("repetition, expected_count", [
    (1, 4404),  # 4404 id_producto se repiten exactamente 1 vez
    (2, 1346),  # 1346 id_producto se repiten exactamente 2 veces
    (3, 309),   # 309 id_producto se repiten exactamente 3 veces
    (4, 53),    # 53 id_producto se repiten exactamente 4 veces
    (5, 5),     # 5 id_producto se repiten exactamente 5 veces
    (6, 2),     # 2 id_producto se repiten exactamente 6 veces
    (7, 1)      # 1 id_producto se repite exactamente 7 veces
])

def test_validate_repetition_counts(load_data, repetition, expected_count):
    '''Caso de prueba: Validar las cantidades detectadas de id_producto para cada repetición.'''
    data = load_data
    repetition_counts = data['id_producto'].value_counts()
    actual_count = repetition_counts.value_counts().get(repetition, 0)  # Cuántos valores tienen la repetición esperada
    logger.info(f"{actual_count} id_producto se repiten exactamente {repetition} veces (esperado: {expected_count}).")
    assert actual_count == expected_count, (
        f"Se esperaban {expected_count} id_producto con {repetition} repeticiones, pero se encontraron {actual_count}."
    )