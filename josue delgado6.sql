/*Selección con Múltiples Filtros*
- _Enunciado:_ Encontrar clientes de México que tengan más de 30 años.
- _Requerimientos:_
  1. Usar `WHERE`.
  2. Combinar las dos condiciones con `AND`.*/

  SELECT * FROM Customers where country = 'mexico' and age > 30;