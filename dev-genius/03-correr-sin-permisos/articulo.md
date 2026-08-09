---
title: "Un agente que corre sin pedir permisos: cómo se hace eso seguro"
slug: correr-sin-permisos
series: dev-genius
episode: 3
date: 2026-08-09
status: published
lang: es
summary: "Las cinco mitigaciones que convierten una idea imprudente en una decisión defendible. Ninguna es sobre el modelo."
banner: banner.png
---

# Un agente que corre sin pedir permisos: cómo se hace eso seguro

En el artículo anterior conté que el agente que escribe el código corre en modo headless dentro de un sandbox, dueño total de sus reintentos. Falta el detalle que suele hacer levantar una ceja: **corre sin pedir permisos.**

No pregunta antes de editar un archivo, ni antes de correr un comando. Y tiene que ser así: un permiso apretado en modo headless no protege nada, solo deja al agente clavado esperando una respuesta que nadie va a dar.

Suena temerario, y lo sería si estuviera solo. No lo está.

## Las cinco mitigaciones

**1 · El sandbox es la frontera.** Un cuarto desechable que se levanta para esa tarea y se destruye al terminar. Lo que pasa adentro se queda adentro. Ésta es la mitigación primaria: todas las demás asumen que ésta existe.

**2 · No tiene el token de GitHub.** El agente solo hace commits locales, que no requieren credencial. El push lo hace el orquestador después, desde afuera, con un token inyectado por comando y limitado a los repositorios que corresponden. Cuando el token entra en escena, el agente ya salió.

**3 · La red está restringida.** Salida denegada por defecto, con una lista corta de dominios permitidos: la API del modelo, el repositorio, los registros de paquetes. Sin salida no hay exfiltración, y eso vuelve mucho menos interesante cualquier cosa que el agente pudiera leer.

**4 · Una sola credencial en su entorno.** La del modelo, y nada más. No porque confíe en el agente, sino porque una credencial que no está no se puede filtrar.

**5 · Ningún Pull Request se mergea solo.** Un humano aprueba, siempre. Es la última barrera y la única que no depende de infraestructura.

## Lo que estas cinco tienen en común

Ninguna es sobre el modelo.

No hay un prompt pidiéndole que se porte bien, ni una lista de cosas que no debe hacer. Todas son restricciones del entorno: qué puede alcanzar, qué credenciales existen a su alrededor, y quién firma antes de que algo llegue a la rama principal.

Es la diferencia entre confiar y no necesitar confiar. Un prompt que pide buen comportamiento es una política; un sandbox sin salida de red es una garantía. Cuando podés elegir, elegís la segunda.

El sandbox aislado no es un detalle de infraestructura. **Es lo que convierte una idea imprudente en una decisión defendible** — y es lo que me permitió contarlo en una reunión sin que la conversación terminara ahí.

Con esto resuelto, la línea empezó a producir en serio. Y entonces apareció un problema que no había anticipado: el cuello de botella se movió de lugar. Dos veces.

---

*Tercer artículo de una serie de cinco.*
