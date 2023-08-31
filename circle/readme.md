# Circle

**Nota:** El archivo que contiene la clase debe llamarse `circle.py` y el nombre de la clase debe ser `Circle`.
   
1. **Inicialización `__init__(self,radius)`:** 
    - Al instanciar, el círculo debe aceptar un único parámetro: `radius`.
    - Si `radius` es <= 0, se debe lanzar una excepción `ValueError` indicando un error amigable al usuario e impidiendo la instanciación.
  
2. **Método `get_radius(self)`:** 
    - Este método retorna el radio del círculo.

3. **Método `set_radius(self,radius)`:** 
    - Este método permite modificar el radio del círculo.
    - Si se intenta establecer un valor <= 0, se debe lanzar una excepción `ValueError` y no permitir la modificación.
  
4. **Método `get_area(self)`:** 
    - Este método debe retornar el área del círculo basada en su radio.

5. **Método `get_perimeter(self)`:** 
    - Este método debe retornar el perímetro del círculo basado en su radio.

6. **Multiplicación `__mul__(self, n)`:** 
    - Multiplicar el objeto Circle por un número `n` (es decir, `Circle * n`) debe retornar un nuevo objeto Circle con su radio multiplicado por `n`.
    - No se debe permitir la multiplicación por números <= 0. Lanzar una excepción `ValueError` en ese caso.

7. **Representación `__str__(self)`:** 
    - Si imprimimos el objeto Circle, se debe mostrar una representación amigable para el usuario.
