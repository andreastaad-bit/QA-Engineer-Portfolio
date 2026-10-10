# Digital Wallet — Deposit & Transaction QA

## 1. Información general del proyecto

**Nombre del proyecto:** Digital Wallet — Deposit & Transaction QA  
**Especialidad:** Quality Assurance (QA) — Pruebas funcionales manuales  
**Tipo de proyecto:** Proyecto independiente de portafolio  
**Aplicación evaluada:** Escenario ficticio de una billetera digital  
**Estado:** Pruebas ejecutadas y defectos documentados  

### Fuente del proyecto

Este proyecto utiliza un escenario ficticio de una aplicación de billetera digital, diseñado a partir de mi familiaridad con aplicaciones que he utilizado anteriormente.

El proyecto no está enfocado en ninguna plataforma comercial específica. Los requisitos, escenarios, datos de prueba y resultados documentados corresponden a una práctica independiente de QA desarrollada con fines educativos y profesionales.

No se utilizaron requisitos internos, datos privados, credenciales, capturas de pantalla ni documentación confidencial de plataformas de terceros.

### Enlaces del proyecto

**Repositorio de GitHub:**

https://github.com/andreastaad-bit/QA-Engineer-Portfolio/tree/main/Digital%20Wallet%20%E2%80%94%20Deposit%20%26%20Transaction%20QA

**Medio de publicación:** GitHub.

El repositorio de GitHub es el medio utilizado para publicar y presentar este proyecto. No existe una aplicación desplegada ni una plataforma independiente asociada a esta práctica.

---

## 2. Objetivo

Evaluar el flujo funcional de depósitos y transacciones de una billetera digital ficticia, desde el inicio de una operación hasta la actualización del saldo y su registro en el historial.

El objetivo es identificar posibles defectos relacionados con la validación de montos, el procesamiento de depósitos, la disponibilidad de los fondos, los estados de las transacciones y la consistencia de la información presentada al usuario.

El flujo ideal también contempla verificar las notificaciones por correo electrónico y el tiempo que tarda el dinero en reflejarse en la cartera digital, siempre que estos comportamientos puedan comprobarse en el entorno de prueba disponible.

---

## 3. Plan de trabajo

### Paso 1. Análisis y definición de requisitos

- Definir los requisitos funcionales del escenario ficticio.
- Identificar las reglas de validación de montos.
- Establecer los límites mínimos y máximos permitidos.
- Definir los estados posibles de las transacciones.
- Determinar las condiciones esperadas para actualizar el saldo y registrar las operaciones en el historial.

### Paso 2. Diseño de pruebas y preparación de datos

- Diseñar casos de prueba positivos y negativos.
- Aplicar partición de equivalencias y análisis de valores límite.
- Preparar datos para depósitos válidos e inválidos.
- Identificar los riesgos asociados al procesamiento de transacciones.
- Organizar los casos de prueba y los datos necesarios para su ejecución.

### Paso 3. Ejecución de pruebas funcionales

- Ejecutar los casos de prueba definidos.
- Verificar las validaciones de entrada.
- Comprobar el comportamiento de los depósitos y las transacciones.
- Revisar la información registrada y los resultados observados.
- Documentar los casos aprobados y fallidos.

### Paso 4. Documentación y análisis de defectos

- Registrar los defectos encontrados.
- Documentar los pasos para reproducir cada defecto.
- Comparar los resultados esperados con los resultados actuales.
- Asignar severidad y prioridad según el impacto potencial.
- Relacionar los defectos con los casos de prueba correspondientes.

### Paso 5. Evaluación de resultados y conclusiones

- Consolidar los resultados de la ejecución.
- Revisar la cobertura de los requisitos incluidos en los casos de prueba.
- Analizar los riesgos identificados.
- Documentar las limitaciones de la ejecución.
- Proponer pruebas adicionales para futuras iteraciones.

---

## 4. Preguntas clave de QA

Durante el análisis del flujo de depósitos se plantearon las siguientes preguntas:

1. **¿El dinero se refleja automáticamente al realizar un depósito?**

   Se busca verificar si el saldo se actualiza de acuerdo con el procesamiento de la transacción y si existe consistencia entre el monto depositado, el estado de la operación y el saldo disponible.

2. **¿El dinero está disponible para utilizarse dentro de la plataforma en cuanto se refleja en la cartera digital?**

   Se busca distinguir entre la visualización del saldo y la disponibilidad efectiva de los fondos para realizar otras operaciones.

3. **¿La plataforma permite realizar múltiples depósitos en un periodo inferior a 24 horas?**

   Se busca comprobar si los depósitos consecutivos pueden procesarse de manera independiente y si cada operación mantiene su propio registro y actualización de saldo.

Estas preguntas orientan el análisis funcional del proyecto. No todas deben considerarse respondidas de manera definitiva si no existe un caso de prueba ejecutado que permita verificar cada comportamiento.

---

## 5. Alcance de las pruebas

### 5.1. Depósitos

Se definieron escenarios relacionados con:

- Ingreso de montos válidos.
- Validación de montos mínimos y máximos.
- Rechazo de valores inferiores al mínimo.
- Rechazo de valores superiores al máximo.
- Ingreso de cero.
- Ingreso de valores negativos.
- Ingreso de datos no numéricos.
- Validación de números decimales.
- Campos vacíos.
- Procesamiento de depósitos consecutivos.
- Manejo de operaciones fallidas.
- Prevención de acreditaciones duplicadas.

### 5.2. Transacciones

Se contemplaron verificaciones relacionadas con:

- Creación de una transacción.
- Identificación única de cada operación.
- Estado de la transacción.
- Monto registrado.
- Actualización del saldo.
- Registro en el historial.
- Consistencia entre el monto depositado y el monto registrado.
- Manejo de operaciones exitosas y fallidas.
- Acumulación correcta de múltiples depósitos.

### 5.3. Disponibilidad de fondos y notificaciones

El flujo de negocio planteado también contempla:

- Verificar cuándo se refleja el dinero en la cartera digital.
- Comprobar cuándo los fondos están disponibles para su uso.
- Revisar las notificaciones de confirmación por correo electrónico.
- Comparar el tiempo de procesamiento con el comportamiento esperado.
- Verificar la consistencia entre la confirmación recibida y el estado de la transacción.

Estos puntos forman parte del objetivo funcional general. Su inclusión en el alcance no implica que todos hayan sido ejecutados o validados en esta iteración.

### 5.4. Límites del proyecto

Este proyecto se centra en pruebas funcionales manuales del flujo de depósitos.

No contempla, en esta iteración:

- Pruebas de rendimiento o carga.
- Pruebas de penetración o seguridad especializada.
- Integraciones reales con bancos.
- Validación de redes blockchain.
- Pruebas de transferencias entre usuarios.
- Pruebas de compra o venta de activos.
- Validación de procesos KYC.
- Administración interna de usuarios.
- Automatización de pruebas.

Estos escenarios podrían incorporarse en futuras iteraciones si se dispone de un entorno apropiado y de requisitos verificables.

---

## 6. Requisitos y reglas de negocio

Para estructurar las pruebas se definieron requisitos funcionales para una billetera digital ficticia.

Entre las reglas establecidas se encuentran:

| Elemento | Regla definida |
|---|---|
| Depósito mínimo | 10.00 |
| Depósito máximo | 10,000.00 |
| Precisión decimal | Hasta dos decimales |
| Monto cero | Debe rechazarse |
| Monto negativo | Debe rechazarse |
| Datos no numéricos | Deben rechazarse |
| Identificación de transacciones | Cada transacción debe tener un identificador único |
| Estados de transacción | Pending, Completed, Failed y Cancelled |
| Actualización del saldo | Solo los depósitos completados deben incrementar el saldo |
| Depósitos múltiples | Cada depósito debe procesarse de manera independiente |
| Prevención de duplicados | Una transacción no debe acreditarse más de una vez |
| Historial | Los datos registrados deben coincidir con la transacción correspondiente |

Los valores y las reglas anteriores son supuestos definidos para este proyecto de portafolio. No representan las condiciones de una plataforma comercial específica.

---

## 7. Trabajo realizado y decisiones técnicas

### 7.1. Análisis de requisitos

Se organizaron los requisitos funcionales para identificar las reglas de negocio que debían verificarse durante las pruebas.

Se prestó especial atención a la relación entre el monto ingresado, el procesamiento de la operación, el estado de la transacción, el saldo y el historial.

### 7.2. Diseño de casos de prueba

Se diseñaron y ejecutaron 20 casos de prueba funcionales.

Los escenarios abarcaron:

- Validación de montos.
- Límites de depósito.
- Datos inválidos.
- Procesamiento de operaciones.
- Identificación de transacciones.
- Manejo de depósitos consecutivos.
- Prevención de acreditaciones duplicadas.
- Disponibilidad de los métodos de depósito.
- Consistencia de los registros de transacciones.

### 7.3. Técnicas de prueba

Se utilizaron criterios de diseño de pruebas orientados a comprobar diferentes clases de entradas y comportamientos.

**Partición de equivalencias:** organización de las entradas en grupos válidos e inválidos, como montos permitidos, montos fuera de los límites y datos no numéricos.

**Análisis de valores límite:** verificación de los límites de depósito establecidos, incluidos el mínimo y el máximo permitidos y los valores que quedan fuera de esos límites.

**Pruebas negativas:** comprobación del rechazo de entradas inválidas y de comportamientos que no deberían producir una operación exitosa.

**Pruebas funcionales:** comparación del comportamiento observado con los resultados esperados definidos para cada caso.

**Análisis basado en riesgos:** priorización de escenarios considerando el impacto potencial de errores en el saldo, las transacciones y la experiencia del usuario.

### 7.4. Ejecución y registro de resultados

Los casos de prueba se ejecutaron manualmente y se clasificaron según el resultado observado.

Los casos aprobados presentaron el comportamiento esperado durante la ejecución. Los casos fallidos se documentaron como defectos para facilitar su análisis y seguimiento.

### 7.5. Documentación de defectos

Se documentaron dos defectos funcionales.

Cada reporte identifica el escenario afectado y describe el comportamiento que debe investigarse.

**BUG-001 — Procesamiento de depósitos consecutivos**

Se observó que un segundo depósito no se procesaba correctamente después de completar un depósito anterior.

El defecto afecta el flujo de depósitos múltiples y puede impedir que el usuario complete operaciones consecutivas.

**BUG-002 — Disponibilidad de los métodos de depósito**

Se observó que los métodos de depósito no estaban disponibles directamente en la página principal del flujo, por lo que era necesario acceder a una sección adicional.

El defecto afecta la accesibilidad de las opciones de depósito y añade pasos de navegación para el usuario.

### 7.6. Análisis de riesgos

Se elaboró una matriz de riesgos para organizar los escenarios según su impacto potencial y su probabilidad cualitativa de ocurrencia.

Se consideraron especialmente relevantes los riesgos relacionados con:

- Exactitud del saldo.
- Integridad de las transacciones.
- Procesamiento de depósitos múltiples.
- Validación de montos.
- Trazabilidad de las operaciones.
- Disponibilidad de los métodos de depósito.

La matriz permite visualizar los escenarios que requieren mayor atención en futuras iteraciones y orientar la selección de pruebas de regresión.

---

## 8. Resultados de la ejecución

Se ejecutaron 20 casos de prueba funcionales.

| Resultado | Cantidad |
|---|---:|
| Casos ejecutados | 20 |
| Casos aprobados (PASS) | 18 |
| Casos fallidos (FAIL) | 2 |
| Porcentaje de aprobación | 90 % |
| Porcentaje de fallos | 10 % |

### Defectos identificados

| ID | Descripción | Severidad | Prioridad |
|---|---|---|---|
| BUG-001 | El segundo depósito no se procesa correctamente después de completar un depósito anterior. | Alta | Alta |
| BUG-002 | Los métodos de depósito no están disponibles directamente en la página principal. | Media | Media |

### Evaluación de los resultados

Durante la ejecución, 18 de los 20 casos de prueba presentaron el comportamiento esperado. Los dos casos fallidos permitieron identificar defectos relacionados con el procesamiento de depósitos consecutivos y la accesibilidad de los métodos de depósito.

Los resultados indican que los escenarios aprobados se comportaron de acuerdo con los criterios definidos durante la ejecución. Sin embargo, los defectos identificados requieren investigación y corrección antes de considerar validado el flujo completo.

El porcentaje de aprobación corresponde exclusivamente a los 20 casos ejecutados. No representa una garantía de que todas las funcionalidades de una billetera digital estén libres de defectos.

---

## 9. Priorización basada en riesgos

Debido a que el escenario involucra operaciones financieras, los riesgos se clasificaron según su impacto potencial en la integridad de las transacciones y en la experiencia del usuario.

| Nivel de riesgo | Ejemplos |
|---|---|
| Alto | Saldo incorrecto, depósito duplicado o monto acreditado incorrectamente |
| Medio | Estado de transacción incorrecto, depósito no procesado o historial inconsistente |
| Bajo | Problemas menores de presentación o contenido |

La clasificación sirve como guía para priorizar las pruebas. La severidad de un defecto describe su impacto, mientras que la prioridad indica la urgencia relativa con la que debería investigarse o corregirse.

La evaluación de probabilidad es cualitativa y se basa en el análisis del escenario; no representa una medición estadística.

---

## 10. Herramientas utilizadas

- **Microsoft Excel:** documentación de casos de prueba, datos de prueba y análisis de riesgos.
- **Markdown:** documentación de requisitos, reportes de defectos y resultados.
- **Git:** control de versiones.
- **GitHub:** publicación y organización de los entregables del proyecto.

Las herramientas se utilizaron para organizar la documentación y facilitar la trazabilidad entre requisitos, pruebas, defectos y resultados.

---

## 11. Entregables del proyecto

La documentación del proyecto se organiza en los siguientes componentes:

- README del proyecto.
- Requisitos funcionales.
- Casos de prueba.
- Datos de prueba.
- Cartas o sesiones de pruebas exploratorias.
- Matriz de riesgos.
- Reportes de defectos.
- Resumen de ejecución.
