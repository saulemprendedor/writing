---
title: "El cuello de botella se corrió dos veces"
slug: el-cuello-de-botella
series: dev-genius
episode: 4
date: 2026-08-09
status: published
lang: es
summary: "Automatizar una etapa no acelera el sistema: mueve la restricción. Y por qué nadie del equipo tuvo que aprender una herramienta nueva."
banner: banner.png
---

# El cuello de botella se corrió dos veces

Empecé por donde dolía: la **implementación**. Es la etapa visible, la que todo el mundo quiere automatizar primero. Y funcionó.

Entonces el problema se mudó hacia arriba.

## Primero: la definición

Con la implementación resuelta, lo que frenaba la línea era la **definición**. Un ticket ambiguo no se vuelve menos ambiguo porque quien lo implementa sea rápido: o el agente construye con precisión la cosa equivocada, o se detiene a preguntar y la tarea queda esperando a un humano.

Había automatizado la etapa veloz y dejado intacta la que decide si esa velocidad sirve de algo.

Así que la definición también había que modelarla: que el agente investigue el código antes de escribir el ticket, que redacte alcance y criterios de aceptación, y que plantee sus dudas al equipo antes de tocar una línea. No es un paso previo al trabajo — es parte del trabajo.

## Después: la certificación

Con eso resuelto, el cuello se corrió otra vez. Ahora hacia abajo.

La línea empezó a producir y las tareas se apilaron esperando **certificación de QA**. Es el resultado natural de acelerar todo lo anterior: el trabajo terminado se acumula frente a la única etapa que no tocaste. Y un backlog de cosas esperando que alguien las valide no es mejor que un backlog de cosas por hacer. Solo cambió de lugar.

Ahí apareció la pregunta que debí haberme hecho mucho antes: **si el sandbox ya levanta el entorno completo para implementar el ticket, ¿por qué no sirve para certificarlo?** El ambiente está montado, con los repositorios corriendo y una URL navegable. La distancia entre *acá se escribió el código* y *acá se prueba el caso* era cero, y yo la estaba tratando como si fueran dos mundos distintos.

La lección me costó dos vueltas: **automatizar una etapa no acelera el sistema, mueve la restricción.** Si no perseguís adónde se fue, lo único que construiste es un embudo más rápido apuntando al mismo tapón.

## Nadie tuvo que aprender una herramienta nueva

Hay una segunda parte de esto, que es la que decide si algo así se adopta o queda de adorno.

Cada fase de la línea tiene su propia dinámica y su propia herramienta. La definición vive en el tracker. Las dudas se resuelven conversando en Slack. El código y la revisión pasan por GitHub. El QA se hace abriendo un navegador.

La tentación es construir una interfaz propia: un panel donde se controle todo, prolijo, con el flujo entero a la vista. Ahí es donde mueren la mayoría de estos proyectos — no por capacidad técnica, sino porque obligan al equipo a mudarse. Una herramienta que exige mudanza compite contra el trabajo real, y el trabajo real gana siempre.

Hice lo contrario: el agente entra en cada fase por la puerta que ya estaba abierta. El ticket se escribe en el tracker que el equipo ya usaba, con su formato. Las dudas llegan al hilo donde esa conversación ya ocurría. El Pull Request aparece en GitHub como cualquier otro y se revisa igual que cualquier otro. El ambiente de QA es una URL que se abre en el navegador.

Nadie cambió de herramienta. Lo que cambió es cuánta operación manual hace cada uno dentro de ella.

Ese detalle es el que decide la adopción: **el equipo no siente que está usando una IA. Siente que el mismo trabajo tiene menos pasos.** No hubo capacitación, ni migración, ni un período de acostumbrarse al sistema nuevo. Desde el primer día se trabajaba distinto sin haber aprendido nada.

Una vez que sabés dónde está el cuello de botella, el trabajo no es reemplazar esa etapa. Es automatizar sus puntos de fricción **sin sacarla de donde vive**.

En el último artículo van los números, y el hallazgo que no esperaba.

---

*Cuarto artículo de una serie de cinco.*
