---
title: "Por qué una feature debería vivir en un solo hilo"
slug: un-solo-hilo
series: dev-genius
episode: 2
date: 2026-08-09
status: draft
lang: es
summary: "La idea que sacó el experimento de mi laptop, y la decisión de arquitectura que la sostiene: orquestar el proceso y delegar el ciclo."
banner: banner.png
---

# Por qué una feature debería vivir en un solo hilo

En el artículo anterior conté cómo, después de un piloto fallido, encontré una forma de que el conocimiento del sistema dejara de envejecer. Funcionaba — y vivía en mi laptop.

La segunda pieza vino de una presentación de Salesforce sobre funcionalidades de IA dentro de Slack. Ahí me explotó la idea: **si el equipo entero ya vive en Slack, ¿por qué las herramientas del trabajo no están ahí?**

Y sobre todo: por qué una feature atraviesa cinco lugares distintos — idea, diseño, construcción, certificación, merge — en vez de vivir en **un solo hilo**, donde cualquiera puede leer la historia completa de principio a fin.

El desafío no era técnico, era de nivel. Las herramientas que pusiera en ese hilo tenían que ser **iguales o mejores** que las que cada área ya usaba. Si eran peores, nadie se mudaba — y con razón.

Así que llevé el experimento a Slack, y la implementación que corría en mi máquina pasó a sandboxes efímeros en la nube. Ahí apareció algo que no había ido a buscar: podía trabajar varias features **a la vez**.

## La decisión de arquitectura: el agente no maneja

La tentación cuando construís algo así es hacer un agente autónomo. Le das las herramientas, le explicás el objetivo y que se arregle.

Hice lo contrario. **El sistema es un orquestador explícito.** El flujo — reclamar la tarea, investigar el código, preguntar las dudas, escribir la especificación, implementar, correr los checks, abrir el PR — está codificado paso por paso. El modelo se invoca solo para las tareas atómicas donde realmente aporta: analizar, redactar, decidir. No decide qué viene después. Eso ya lo sé yo.

¿Por qué? Porque un agente autónomo es imposible de depurar. Cuando algo sale mal en el paso 7 de 12, querés poder mirar el paso 7. Con un flujo explícito hay traza: cada fase deja su rastro en el hilo de esa tarea. Cualquiera lo abre y ve qué investigó, qué preguntó y qué hizo.

La autonomía es seductora en la demo y cara en producción.

## La excepción que me hizo cambiar de opinión

Y sin embargo, hay un lugar donde delegué el control por completo.

La fase de escribir el código la orquestaba yo también: pedile al modelo que edite este archivo, corré el linter, si falla mandale el error, reintentá. Cientos de líneas coordinando un ciclo de implementar → verificar → corregir.

Un día caí en que estaba reimplementando a mano, y peor, algo que ya existía hecho bien: el ciclo agéntico de una herramienta de codificación real. Saqué toda esa orquestación y la reemplacé por un agente de codificación corriendo en modo headless **dentro del sandbox**, dueño total de sus reintentos. El orquestador quedó con una sola responsabilidad: leer el archivo de tareas cada pocos segundos y reflejar el progreso, de ⏳ a ✓.

Se fueron cientos de líneas. Y mejoró, porque adentro del sandbox el agente lee las convenciones del proyecto de forma nativa en lugar de recibirlas masticadas por mi prompt.

La regla que me llevé: **orquestá explícitamente el proceso, delegá el ciclo.** El proceso es tuyo porque es tu criterio de ingeniería. El ciclo de implementar-y-corregirse no lo es, y competir contra él es orgullo mal invertido.

A ese conjunto de principios terminé llamándolo **DEV Genius**. No es una herramienta: es la forma de armar la línea de trabajo alrededor del modelo.

Queda una pregunta incómoda, que es la del próximo artículo: ese agente corre **sin pedir permisos**. ¿Cómo se hace eso sin que sea una imprudencia?

---

*Segundo artículo de una serie de cinco.*
