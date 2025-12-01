

# **INFORME DE REQUERIMIENTO FUNCIONAL Y TÉCNICO**

## **Sistema de Gestión de Eventos Adversos y Seguridad del Paciente**

---

## **1. Introducción**

El presente documento describe los requerimientos funcionales, no funcionales y de integración para la implementación de un sistema informático destinado al registro, análisis y gestión de **eventos adversos**, **incidentes**, **casi fallas** y otros eventos relacionados con la seguridad del paciente.

El diseño y alcance del sistema se fundamenta en el **modelo de datos relacional** proporcionado, el cual define las entidades clave: pacientes, ingresos, eventos, catálogos de clasificación y módulos de análisis y acciones de mejora.

---

## **2. Objetivo del Sistema**

Implementar una solución integral que permita:

* Registrar eventos de seguridad del paciente.
* Clasificar los eventos según tipo y severidad.
* Asociar el evento con el ingreso clínico y datos del paciente.
* Realizar análisis y documentar acciones correctivas.
* Hacer seguimiento al avance de las acciones de mejora.
* Generar reportes e indicadores para comités y dirección.

---

## **3. Alcance**

El sistema abarca desde el registro del evento hasta su cierre definitivo. Incluye:

* Catálogos configurables (tipo de evento, severidad OMS).
* Gestión del paciente y episodios de ingreso.
* Registro del evento con detalles clínicos y administrativos.
* Análisis causa raíz y metodologías similares.
* Registro y seguimiento de acciones de mejora.
* Reportes operativos y estratégicos.

---

# **4. Modelo de Datos (Base del Sistema)**

El sistema está estructurado sobre las siguientes tablas:

### **4.1. Catálogos**

1. **tipo_evento**

   * Define categorías del evento (caídas, medicación, IAAS, etc.).

2. **severidad**

   * Define severidad OMS A–I (incidente → daño grave).

### **4.2. Paciente e Ingreso**

3. **paciente**

   * Información básica del paciente.

4. **ingreso**

   * Episodios clínicos asociados a un paciente.

### **4.3. Evento**

5. **evento**

   * Registro detallado del evento adverso o incidente.
   * Relaciona:

     * ingreso
     * tipo_evento
     * severidad

### **4.4. Análisis y acciones**

6. **analisis_evento**

   * Documenta análisis (RCA, 5 Porqués, Ishikawa, AMFE).

7. **accion_mejora**

   * Acciones correctivas o preventivas asociadas al evento.

---

# **5. Requerimientos Funcionales (Basados en el Modelo de Datos)**

## **5.1. Módulo de Catálogos**

### **Tipos de Evento**

* RF-01: Administrar catálogo de tipos de eventos (tabla: *tipo_evento*).
* RF-02: Permitir CRUD para nombre y descripción.

### **Severidad**

* RF-03: Administrar catálogo de severidad OMS A–I (tabla: *severidad*).
* RF-04: No permitir códigos duplicados.

---

## **5.2. Módulo de Pacientes e Ingresos**

### **Pacientes**

* RF-05: Registrar pacientes con identificación, nombre, sexo y fecha de nacimiento (tabla: *paciente*).
* RF-06: Permitir búsqueda por número de documento.

### **Ingresos**

* RF-07: Registrar episodios de atención asociados a un paciente (tabla: *ingreso*).
* RF-08: Registrar servicio, cama y estado (activo, egresado).
* RF-09: Impedir ingresos sin paciente válido (FK obligatoria).

---

## **5.3. Módulo de Reporte de Eventos**

Basado directamente en la tabla **evento**.

* RF-10: Registrar un evento adverso asociado a un ingreso.
* RF-11: Capturar tipo de evento y severidad (FK obligatorias).
* RF-12: Registrar:

  * fecha del evento
  * descripción
  * detectado por
  * usuario que reporta
* RF-13: Clasificar el evento según tres campos binarios:

  * es_incidente
  * es_evento_adverso
  * es_casi_falla
* RF-14: Registrar estado del evento (pendiente, en análisis, cerrado).
* RF-15: Permitir adjuntar fecha de reporte.
* RF-16: Validar que un evento no se registre sin ingreso asociado.

### Lógica de negocio asociada al modelo:

* RF-17: El sistema debe impedir que un evento exista sin tipo y severidad.
* RF-18: El sistema debe permitir múltiples eventos por ingreso.

---

## **5.4. Módulo de Análisis del Evento**

Basado en **analisis_evento**.

* RF-19: Crear análisis vinculados a un evento.
* RF-20: Registrar tipo de análisis (RCA, AMFE, etc.).
* RF-21: Documentar:

  * causa primaria
  * causas contribuyentes
  * acciones inmediatas
  * acciones recomendadas
* RF-22: Registrar responsable y fecha de cierre.
* RF-23: Si se elimina un evento, sus análisis deben borrarse automáticamente (ON DELETE CASCADE).

---

## **5.5. Módulo de Acciones de Mejora**

Basado en **accion_mejora**.

* RF-24: Registrar acciones asociadas al evento.
* RF-25: Registrar responsable, fecha programada y fecha de ejecución.
* RF-26: Permitir cambiar estado según fechas (pendiente, retrasada, ejecutada).
* RF-27: Impedir acciones sin evento asociado.

---

## **5.6. Módulo de Reportes y Analítica**

* RF-28: Reporte de eventos por tipo, severidad, servicio, fecha.
* RF-29: Reporte de incidentes vs eventos adversos vs casi fallas.
* RF-30: Reporte de eventos por paciente e ingreso.
* RF-31: Dashboard general:

  * Total eventos
  * Eventos por mes
  * Severidad A–I
  * Top tipos de evento
* RF-32: Exportación de reportes a Excel, PDF y CSV.

---

# **6. Requerimientos No Funcionales**

## **6.1. Seguridad**

* RNF-01: Registro de usuarios reportantes con auditoría.
* RNF-02: Acceso bajo HTTPS.
* RNF-03: Cumplimiento de protección de datos personales.
* RNF-04: Integridad referencial asegurada por FK del modelo.

## **6.2. Rendimiento**

* RNF-05: Consultas rápidas sobre tablas de evento y análisis (< 2s).
* RNF-06: Índices en FK: ingreso_id, tipo_evento_id, severidad_id.

## **6.3. Disponibilidad**

* RNF-07: Base de datos tolerante a fallos.
* RNF-08: Respaldo diario de las tablas: evento, analisis_evento y accion_mejora.

## **6.4. Usabilidad**

* RNF-09: Formularios validados según el modelo (campos obligatorios).
* RNF-10: Interfaz adaptable a móvil.

---

# **7. Requerimientos de Integración**

* RI-01: Integración con sistema de historia clínica para obtener:

  * datos del paciente
  * datos del ingreso
* RI-02: APIs para consulta de eventos por comités.
* RI-03: Integración opcional con BI (Power BI o Metabase).

---

# **8. Flujo General del Proceso (Basado en el modelo relacional)**

1. Registrar paciente.
2. Registrar ingreso del paciente.
3. Registrar evento asociado al ingreso.
4. Clasificar evento (tipo_evento, severidad).
5. Registrar análisis del evento.
6. Registrar acciones de mejora.
7. Cerrar análisis.
8. Generar reportes.

Todo el proceso se soporta en relaciones FK entre tablas del modelo.

---

# **9. Riesgos**

* Captura insuficiente de datos clínicos en el evento.
* Registros incompletos de análisis o acciones.
* Falta de integración con datos del paciente.
* Resistencia del personal al reporte.

---

# **10. Conclusiones**

El modelo de datos proporcionado permite una gestión completa y estandarizada del proceso de seguridad del paciente. El sistema propuesto es escalable, robusto y garantiza trazabilidad completa desde el evento hasta su cierre.


