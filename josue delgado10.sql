/*Eliminación Condicional*
- _Enunciado:_ Borrar todos los envíos con estado 'Pending'.
- _Requerimientos:_
  1. Usar `DELETE FROM`.
  2. ¡NO OLVIDAR el `WHERE status = 'Pending'`! ⚠️*/

  DELETE FROM Shipments
  WHERE status = 'pending';