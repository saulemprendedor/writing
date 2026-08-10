---
title: "Mi primer intento con agentes de IA fracasó. El problema no era el modelo"
slug: el-primer-intento-fracaso
series: dev-genius
episode: 1
date: 2026-08-09
status: published
lang: es
summary: "Un piloto con orquestadores de agentes que ayudaba y se depreciaba solo. Por qué el conocimiento congelado era el problema real, y qué hice después de abandonarlo."
banner: banner.jpg
---

# Mi primer intento con agentes de IA fracasó. El problema no era el modelo

Hace un año arranqué un piloto, con el respaldo de la empresa, para construir herramientas autónomas de IA sobre el trabajo de desarrollo.

Un año después, dos desarrolladores del equipo entregaron el doble de los puntos que habían comprometido en un sprint — y el aumento no dependió de su seniority.

Entre esas dos cosas hubo un fracaso completo. Empiezo por ahí, porque es la parte que nadie cuenta.

## El piloto que se depreciaba solo

Usé lo que se usaba entonces: orquestadores de agentes, roles, herramientas encadenadas. Cada agente con su prompt, su responsabilidad y su lugar en la cadena.

Ayudaba. Y se depreciaba solo.

El problema no era el modelo ni el framework — los dos hacían lo que prometían. Era que el conocimiento que yo les daba estaba **congelado**. Cada agente sabía lo que yo había escrito en su prompt el día que lo escribí, y nada más.

Y la mayor parte de lo que hace falta para tocar un sistema real no está escrita en ninguna parte. Está en la cabeza de la gente: por qué esa tabla tiene un campo raro, qué se rompe si tocás ese servicio, qué se decidió hace dos años y por qué nadie lo revirtió. Ese conocimiento vive sobre todo en los seniors, y no se transfiere escribiendo un prompt más largo.

El sistema envejecía mientras el producto avanzaba. Cada semana sabía un poco menos del código sobre el que trabajaba.

Lo dejé.

## Un mes sin construir automatización

Me tomé un mes de reinicio. No dejé de trabajar: seguí sacando mis tickets como siempre, con Cursor y Claude Code, las herramientas de todos los días. Lo que frené fue construir — no escribí una línea más de automatización en ese mes.

Lo usé para leer y reenfocar. Fue el período en que Anthropic publicaba prácticamente todas las semanas, y me dediqué a entender qué estaba cambiando de verdad debajo del ruido.

La pregunta con la que volví era otra. No *cómo hago un agente más listo*, sino **cómo dejo de perder el conocimiento**.

## Documentación que no envejece

Encontré una forma de documentar el histórico de decisiones del negocio. No la documentación que nadie actualiza y que a los tres meses miente — sino el registro de *por qué* las cosas son como son: qué se decidió, contra qué alternativas y qué restricción lo motivó.

Y le agregué la pieza que lo cambia todo: **al terminar cada implementación, esa documentación se actualiza con el resultado.**

Es un detalle chico y es toda la diferencia. El conocimiento deja de ser una foto y pasa a ser un registro vivo. El contexto deja de ser una suposición mía sobre lo que el agente necesita saber, y pasa a ser algo que el propio trabajo mantiene al día.

## El experimento

Lo probé conmigo. En mi máquina, sobre mis tickets del día, sin contarle a nadie.

Los resultados fueron desproporcionados: la diferencia de tiempo entre un ticket chico y uno grande pasó a medirse en minutos, no en horas ni en días. No porque escribiera código más rápido — porque dejé de gastar el tiempo en reconstruir el contexto cada vez.

Pero seguía viviendo en mi laptop.

Que es donde vive casi todo lo que los desarrolladores construimos para nosotros mismos: la herramienta que te hace el doble de productivo y que nadie más usa, porque nunca salió de tu carpeta de scripts.

Sacarlo de ahí fue el problema siguiente. Y resultó ser un problema de diseño, no de código.

---

*Primer artículo de una serie de cinco sobre cómo construí un sistema de agentes que entrega software en producción.*

*Sigue en el capítulo 2: [Por qué una feature debería vivir en un solo hilo](https://saul.botsmith.ai/es/blog/un-solo-hilo).*
