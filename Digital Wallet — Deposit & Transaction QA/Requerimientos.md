
# Digital Wallet — Deposit & Transaction QA

## 1. Descripción del sistema

El sistema representa una billetera digital que permite al usuario realizar depósitos y consultar el estado de sus transacciones.

El alcance de este proyecto se concentra en el flujo de **depósito**, desde el ingreso del monto hasta la actualización del balance y el registro de la operación en el historial.

> **Nota:** Los valores, reglas y comportamientos definidos en este documento son ficticios y fueron creados exclusivamente para este proyecto de portafolio. No representan requisitos de ninguna plataforma real.

---

## 2. Requisitos funcionales

### 2.1 Inicio de un depósito

**DEP-001**
El usuario debe poder iniciar un depósito desde la sección correspondiente de la billetera.

**DEP-002**
El sistema debe permitir al usuario ingresar un monto para el depósito.

**DEP-003**
El campo de monto debe aceptar valores numéricos positivos.

**DEP-004**
El sistema debe aceptar montos con hasta **2 posiciones decimales**.

**DEP-005**
El sistema no debe permitir continuar con un campo de monto vacío.

---

### 2.2 Límites del depósito

Para este proyecto se establece:

* Monto mínimo permitido: **10.00 unidades**
* Monto máximo permitido: **10,000.00 unidades**

**DEP-006**
El sistema debe aceptar un depósito de exactamente **10.00 unidades**.

**DEP-007**
El sistema debe rechazar depósitos inferiores a **10.00 unidades**.

**DEP-008**
El sistema debe aceptar un depósito de exactamente **10,000.00 unidades**.

**DEP-009**
El sistema debe rechazar depósitos superiores a **10,000.00 unidades**.

---

### 2.3 Validación del monto

**DEP-010**
El sistema debe rechazar valores iguales a cero.

**DEP-011**
El sistema debe rechazar valores negativos.

**DEP-012**
El sistema debe rechazar formatos de monto que no sean numéricos.

**DEP-013**
El sistema debe rechazar valores que excedan las 2 posiciones decimales.

**DEP-014**
Cuando el monto ingresado no sea válido, el sistema debe mostrar un mensaje indicando que el valor debe corregirse antes de continuar.

**DEP-015**
Cuando el monto ingresado sea inferior al mínimo permitido, el sistema debe informar que no cumple con el monto mínimo.

**DEP-016**
Cuando el monto ingresado sea superior al máximo permitido, el sistema debe informar que excede el límite permitido.

---

### 2.4 Procesamiento del depósito

**DEP-017**
Cuando un depósito válido sea procesado correctamente, el sistema debe generar una transacción asociada a la operación.

**DEP-018**
Cada depósito debe tener un identificador único de transacción.

**DEP-019**
Una transacción de depósito debe tener uno de los siguientes estados:

* Pending
* Completed
* Failed
* Cancelled

**DEP-020**
Un depósito con estado **Completed** debe incrementar el balance disponible por el monto correspondiente.

**DEP-021**
Un depósito con estado **Pending** no debe incrementar el balance disponible hasta que la transacción sea completada.

**DEP-022**
Un depósito con estado **Failed** no debe incrementar el balance disponible.

**DEP-023**
Un depósito con estado **Cancelled** no debe incrementar el balance disponible.

---

### 2.5 Balance

**BAL-001**
El balance disponible debe reflejar únicamente los depósitos que hayan sido completados.

**BAL-002**
El monto acreditado al balance debe corresponder al monto confirmado de la transacción.

**BAL-003**
El sistema no debe acreditar dos veces el mismo depósito.

**BAL-004**
Si una transacción no se completa correctamente, el balance no debe modificarse como si la operación hubiera sido exitosa.

**BAL-005**
Después de completar un depósito, el nuevo balance debe corresponder al balance anterior más el monto acreditado.

**Regla:**

`Nuevo balance = Balance anterior + depósito completado`

---

### 2.6 Historial de transacciones

**HIS-001**
Cada depósito procesado debe aparecer en el historial de transacciones.

**HIS-002**
El registro del depósito debe mostrar como mínimo:

* Identificador de transacción
* Tipo de operación
* Monto
* Estado
* Fecha y hora

**HIS-003**
El monto mostrado en el historial debe corresponder al monto de la transacción.

**HIS-004**
El estado mostrado en el historial debe corresponder al estado actual de la transacción.

**HIS-005**
Una misma transacción no debe aparecer duplicada en el historial.

**HIS-006**
Cuando una transacción cambie de estado, el historial debe reflejar el estado actualizado.

---

### 2.7 Múltiples depósitos

**MUL-001**
El usuario debe poder realizar más de un depósito de manera independiente.

**MUL-002**
Cada depósito debe generar su propia transacción.

**MUL-003**
Los depósitos completados deben acumularse correctamente en el balance.

**MUL-004**
El sistema debe mantener registros independientes para cada transacción.

**MUL-005**
El procesamiento de un nuevo depósito no debe modificar incorrectamente las transacciones anteriores.

---

## 3. Reglas de consistencia

**CON-001**
El monto mostrado durante el proceso de depósito debe coincidir con el monto registrado en la transacción.

**CON-002**
El monto de la transacción debe coincidir con el monto utilizado para actualizar el balance.

**CON-003**
El monto mostrado en el historial debe coincidir con el monto de la transacción.

**CON-004**
El estado de la transacción debe ser consistente entre el proceso, el historial y el resultado final.

**CON-005**
Una operación completada no debe generar más de una acreditación al balance.

---

## 4. Fuera del alcance

Para mantener el proyecto enfocado, no se probarán:

* Retiros
* Transferencias entre usuarios
* Compra/venta de activos
* KYC o verificación de identidad
* Métodos de pago bancarios específicos
* Integraciones con bancos
* Blockchain o redes externas
* Seguridad de infraestructura
* Pruebas de carga o performance
* Pruebas de penetración
* Aplicación móvil nativa
* Administración interna de usuarios

Estas funcionalidades podrían formar parte de futuras iteraciones del proyecto.

---

## 5. Supuestos del proyecto

Los siguientes elementos son decisiones de diseño creadas para permitir la ejecución de las pruebas:

| Elemento                    | Regla                                           |
| --------------------------- | ----------------------------------------------- |
| Monto mínimo                | 10.00                                           |
| Monto máximo                | 10,000.00                                       |
| Decimales permitidos        | 2                                               |
| Estados                     | Pending, Completed, Failed, Cancelled           |
| Identificador               | Único por transacción                           |
| Balance                     | Se actualiza únicamente con depósitos Completed |
| Depósitos múltiples         | Permitidos                                      |
| Duplicación de acreditación | No permitida                                    |
