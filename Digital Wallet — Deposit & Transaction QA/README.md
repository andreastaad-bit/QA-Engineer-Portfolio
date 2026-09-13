# Digital Wallet — Deposit & Transaction QA

## 📌 Descripción del proyecto

Este proyecto presenta una estrategia de **Quality Assurance (QA) para una aplicación de wallet digital**, enfocada principalmente en el flujo de depósitos y en la correcta gestión de las transacciones.

El objetivo es diseñar y documentar pruebas que permitan verificar que las operaciones financieras se procesen correctamente y que exista consistencia entre el monto ingresado, el estado de la transacción, el saldo de la cuenta y el historial de operaciones.

El proyecto fue desarrollado como una práctica independiente de QA y está orientado a demostrar habilidades de **pruebas funcionales, diseño de casos de prueba, pruebas exploratorias y análisis de riesgos**.

---

## 🎯 Objetivo

Evaluar los principales escenarios funcionales relacionados con los depósitos y las transacciones de una wallet digital, identificando posibles comportamientos incorrectos antes de que puedan afectar la experiencia del usuario o la integridad de la información mostrada.

Se busca validar principalmente que:

* Los depósitos acepten datos válidos.
* Los valores inválidos sean rechazados correctamente.
* Los límites permitidos sean respetados.
* Las transacciones tengan un estado correcto.
* El saldo se actualice de acuerdo con las operaciones realizadas.
* Las transacciones aparezcan correctamente en el historial.
* Una misma operación no sea procesada de manera duplicada.
* Los mensajes de validación proporcionen información clara al usuario.
* El sistema mantenga un comportamiento consistente ante diferentes escenarios y entradas.

---

## 🔍 Alcance de las pruebas

### Depósitos

Se probarán diferentes escenarios relacionados con el ingreso de fondos:

* Valores válidos.
* Valores mínimos y máximos.
* Valores por debajo y por encima de los límites.
* Cero.
* Valores negativos.
* Valores decimales.
* Campos vacíos.
* Datos con espacios.
* Múltiples depósitos consecutivos.
* Intentos repetidos de una misma operación.
* Cancelación de una operación.
* Comportamiento ante acciones inesperadas durante el proceso.

### Transacciones

Se verificará el comportamiento de las operaciones después de iniciar un depósito:

* Creación de la transacción.
* Estado de la transacción.
* Monto registrado.
* Fecha y hora.
* Actualización del saldo.
* Registro en el historial.
* Consistencia entre los detalles de la transacción y el saldo.
* Manejo de operaciones exitosas y fallidas.

### Validaciones

Se utilizarán diferentes tipos de datos para comprobar el comportamiento del sistema ante entradas válidas, inválidas y casos límite.

Entre las técnicas utilizadas se encuentran:

* **Partición de equivalencias**
* **Análisis de valores límite**
* **Pruebas negativas**
* **Pruebas exploratorias**
* **Pruebas basadas en riesgos**

---

## ⚠️ Priorización basada en riesgos

Debido a que una wallet digital maneja operaciones financieras, las pruebas se priorizarán de acuerdo con el impacto potencial de una falla.

| Prioridad | Ejemplos                                                                              |
| --------- | ------------------------------------------------------------------------------------- |
| Crítica   | Saldo incorrecto, depósito duplicado, monto incorrecto acreditado                     |
| Alta      | Estado incorrecto de una transacción, depósito no registrado, historial inconsistente |
| Media     | Validaciones incorrectas, manejo de decimales, mensajes de error                      |
| Baja      | Problemas menores de interfaz o contenido                                             |

La prioridad se utilizará para determinar qué escenarios deben recibir mayor atención durante las pruebas.

---

## 🧪 Tipos de pruebas

### Pruebas funcionales

Verificar que cada funcionalidad produzca el resultado esperado de acuerdo con los requisitos definidos para el proyecto.

### Pruebas negativas

Evaluar cómo responde el sistema ante información inválida o acciones no esperadas.

### Pruebas exploratorias

Explorar el flujo de depósitos y transacciones utilizando diferentes combinaciones de datos y acciones para detectar comportamientos inesperados.

### Pruebas de valores límite

Comprobar el comportamiento del sistema en los límites establecidos y alrededor de ellos.

### Pruebas basadas en riesgos

Priorizar los escenarios que podrían tener mayor impacto para el usuario o para la integridad de las operaciones.

---

## 📋 Entregables

El proyecto incluirá:

* Requisitos funcionales definidos para el escenario de prueba.
* Casos de prueba documentados.
* Datos de prueba.
* Sesiones de pruebas exploratorias.
* Matriz de riesgos.
* Reportes de defectos.
* Resumen de resultados.
* Documentación del proceso de QA.

---

## 🛠️ Herramientas

* **Excel** — Diseño y documentación de casos de prueba, datos de prueba y análisis.
* **Jira** — Documentación de defectos utilizando una estructura similar a un entorno profesional.
* **Git** — Control de versiones.
* **GitHub** — Almacenamiento y presentación del proyecto.

---

## 💡 Habilidades demostradas

Este proyecto demuestra experiencia práctica en:

* Pruebas funcionales.
* Diseño de casos de prueba.
* Pruebas exploratorias.
* Pruebas negativas.
* Análisis de valores límite.
* Partición de equivalencias.
* Análisis basado en riesgos.
* Diseño de datos de prueba.
* Identificación y documentación de defectos.
* Análisis de flujos transaccionales.
* Documentación de QA.
* Uso de Git y GitHub.

---

## 📁 Estructura del proyecto

```text
digital-wallet-qa/
│
├── README.md
│
├── requirements/
│   └── wallet-requirements.md
│
├── test-cases/
│   └── wallet-deposit-tests.xlsx
│
├── exploratory-testing/
│   └── exploratory-charters.xlsx
│
├── test-data/
│   └── deposit-test-data.xlsx
│
├── risk-analysis/
│   └── risk-matrix.xlsx
│
├── bug-reports/
│   └── README.md
│
└── test-summary/
    └── test-summary.md
```

---

## 🔐 Nota de confidencialidad

Este es un **proyecto independiente de portafolio** desarrollado con fines educativos y profesionales.

No contiene información confidencial, datos de usuarios, credenciales, capturas de pantalla, materiales propietarios, requisitos internos, casos de prueba privados ni defectos provenientes de plataformas, clientes o proyectos de terceros.

Los requisitos, escenarios, datos de prueba y documentación incluidos en este repositorio fueron desarrollados específicamente para este proyecto.
