---
title: "Los números, y el hallazgo que no esperaba"
slug: los-numeros
series: dev-genius
episode: 5
date: 2026-08-09
status: draft
lang: es
summary: "Dos sprints medidos, y el dato que me sorprendió: el aumento fue parejo entre perfiles de distinto seniority."
banner: banner.png
---

# Los números, y el hallazgo que no esperaba

Cuatro artículos de decisiones de arquitectura no valen nada sin la parte que se puede discutir. Acá van los números, con su ventana de medición, para que puedan cuestionarse.

## Dos sprints en producción, tres desarrolladores usándolo

- **50 tareas** llevadas de la idea al merge
- **62 Pull Requests** con tests y ambiente de QA navegable
- **93%** llegó a revisión sin necesitar retrabajo
- **2,5 tareas por día hábil**, sostenido a lo largo de los dos sprints
- Cada tarea toca en promedio **más de un repositorio**: backend y frontend en la misma unidad de trabajo

## Por qué la meta era 3X

El objetivo nunca fue "usar IA". Era concreto y medible: **triplicar la capacidad de entrega del equipo sin contratar a nadie más.**

Ponerle un número a la meta cambió todas las decisiones de diseño. Un agente que escribe código elegante pero necesita a alguien mirándolo paso a paso no triplica nada: mueve el trabajo de lugar. Por eso el sistema no termina en *generó el código*. Termina con el PR abierto, los checks corriendo, la tarjeta movida y el hilo contando qué pasó.

**El primer sprint con el sistema en marcha cerró con dos desarrolladores entregando el doble de los puntos que habían comprometido**, medido contra su propio historial de sprints anteriores. No contra un promedio de industria ni contra una estimación optimista: contra lo que esas mismas dos personas venían entregando.

## El hallazgo

Pero el dato que más me interesa de ese sprint no es el múltiplo. Es que **el aumento fue parejo entre los dos, y tienen niveles de seniority distintos.**

Es lo contrario de lo que suele pasar con las herramientas de productividad, que amplifican a quien ya era rápido y dejan al resto donde estaba. Acá el que sube no es el individuo: **es el proceso.**

El agente hace siempre los mismos pasos — investiga antes de escribir, pregunta lo que no está claro, deja la especificación por escrito, corre los checks, abre el PR — y esos pasos son justamente los que un desarrollador con menos años todavía está incorporando. La herramienta no lo vuelve más experto. **Le presta el proceso de alguien que sí lo es.**

Un sprint y dos personas no son una muestra estadística. Son una señal. Pero es exactamente la señal que estaba buscando, porque significa que esto escala con el equipo y no con las estrellas del equipo.

## Lo que realmente aprendí

Empecé creyendo que el problema difícil era conseguir que el modelo escribiera buen código.

No lo es. Eso ya está resuelto.

Cuando generar una implementación se vuelve barato, lo caro pasa a ser todo lo que viene después: revisar, probar, resolver conflictos cuando cinco ramas tocan el mismo archivo, mantener el tablero al día, no perder el rastro de qué está esperando a quién. Hoy la mayor parte del sistema no es *la parte de IA*: son los procesos de fondo que cuidan la cola.

Pero el resultado que más me sorprende no es la velocidad. Es que hoy un desarrollador con una máquina que apenas abra Slack y un navegador entrega software con la calidad y el contexto que antes exigían años de casa. No porque el modelo lo vuelva más experto: porque el conocimiento que antes vivía en la cabeza de los seniors ahora está en el sistema, vivo, actualizándose con cada implementación.

Es exactamente lo contrario de donde empecé. Aquel primer piloto fracasó porque el conocimiento estaba congelado y seguía viviendo en las personas. Todo lo que vino después fue perseguir esa única cosa.

Construir con IA se parece mucho menos a entrenar un modelo y mucho más a diseñar una línea de producción. El modelo es una estación. El valor está en el resto de la línea.

Eso es DEV Genius: no una herramienta, sino la forma de armar esa línea alrededor del modelo. Es en lo que trabajo todos los días.

Si estás tratando de mover la IA de la prueba de concepto al trabajo real de tu equipo, escribime. Me interesa comparar notas — es un problema donde casi todos estamos aprendiendo al mismo tiempo.

---

*Último artículo de una serie de cinco.*
