
import requests

# Hacer la solicitud GET a la API
url = 'https://dummy.restapiexample.com/api/v1/employees'
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()

    # Cantidad de empleados
    cantidad_empleados = len(data['data'])

    # Calcular promedio de salario
    salarios = [emp['employee_salary'] for emp in data['data']]
    promedio_salario = sum(salarios) / cantidad_empleados

    # Calcular promedio de edad
    edades = [emp['employee_age'] for emp in data['data']]
    promedio_edad = sum(edades) / cantidad_empleados

    # Salario mínimo y máximo
    salario_minimo = min(salarios)
    salario_maximo = max(salarios)

    # Edad mínima y máxima
    edad_minima = min(edades)
    edad_maxima = max(edades)

    # Mostrar los resultados
    print(f"Cantidad de empleados: {cantidad_empleados}")
    print(f"Promedio de salario: {promedio_salario:.2f}")
    print(f"Promedio de edad: {promedio_edad:.2f}")
    print(f"Salario mínimo: {salario_minimo}")
    print(f"Salario máximo: {salario_maximo}")
    print(f"Edad mínima: {edad_minima}")
    print(f"Edad máxima: {edad_maxima}")
else:
    print("No se pudo obtener los datos de la API")
