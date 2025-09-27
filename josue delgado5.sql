/*Actualización de un Registro*
- _Enunciado:_ El cliente con id 2 (Ana García) cambió su email. ¡Actualízalo!
- _Requerimientos:_
  1. Usar `UPDATE`.
  2. Nuevo email: 'ana.g.nuevo@email.com'.
  3. Asegurarse de usar `WHERE customer_id = 2`.*/

  UPDATE Customers
  SELECT email = 'ana.g.nuevo@email.com'
  WHERE customer_id = 2;
