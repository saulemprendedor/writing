# Saúl Hernández — escribiendo sobre construir con IA

> *I'm a Tech Lead with 15 years building software, currently leading development
> teams at Chile's largest bus-travel platform. I write in Spanish about building
> AI agent systems that ship real software — architecture decisions, what failed,
> and the numbers. Everything here is from production, not from a demo.*

---

Este repositorio es lo que escribo, y por qué.

Llevo 15 años construyendo software. El último año lo pasé en una sola pregunta:
qué hace falta para que un agente de IA no escriba código de demostración, sino
software que entra a producción — con especificación, tests, revisión humana y
alguien que se haga cargo cuando falla.

La respuesta no fue un modelo mejor. Fue un proceso.

Lo que vas a encontrar acá no es una colección de buenas prácticas. **Es el
recorrido completo, con el fracaso adelante:** mi primer intento se depreció
solo, lo abandoné, me tomé un mes sin escribir código, y volví por otro lado.
Escribo con los números que puedo defender y con las decisiones que tomé mal
antes de tomarlas bien.

Si te dedicás a esto, probablemente estés en alguna parte del mismo camino.

## Artículos

<!-- ARTICLES:START -->

### DEV Genius — cómo construí un sistema de agentes que entrega software

**1. [Mi primer intento con agentes de IA fracasó. El problema no era el modelo](dev-genius/01-el-primer-intento-fracaso/articulo.es.md)**  
Un piloto con orquestadores de agentes que ayudaba y se depreciaba solo. Por qué el conocimiento congelado era el problema real, y qué hice después de abandonarlo.  
[Leerlo en LinkedIn](https://www.linkedin.com/pulse/mi-primer-intento-con-agentes-de-ia-fracas%C3%B3-el-era-modelo-hernandez-ikpqf/) · 2026-08-09 · [English](dev-genius/01-el-primer-intento-fracaso/articulo.en.md)

**2. [Por qué una feature debería vivir en un solo hilo](dev-genius/02-un-solo-hilo/articulo.es.md)**  
La idea que sacó el experimento de mi laptop, y la decisión de arquitectura que la sostiene: orquestar el proceso y delegar el ciclo.  
[Leerlo en LinkedIn](https://www.linkedin.com/pulse/por-qu%C3%A9-una-feature-deber%C3%ADa-vivir-en-un-solo-hilo-saul-hernandez-aq8cc/) · 2026-08-10

**3. [Un agente que corre sin pedir permisos: cómo se hace eso seguro](dev-genius/03-correr-sin-permisos/articulo.es.md)**  
Las cinco mitigaciones que convierten una idea imprudente en una decisión defendible. Ninguna es sobre el modelo.  
[Leerlo en LinkedIn](https://www.linkedin.com/pulse/un-agente-que-corre-sin-pedir-permisos-c%C3%B3mo-se-hace-eso-hernandez-0fnqf/) · 2026-08-11

**4. [El cuello de botella se corrió dos veces](dev-genius/04-el-cuello-de-botella/articulo.es.md)**  
Automatizar una etapa no acelera el sistema: mueve la restricción. Y por qué nadie del equipo tuvo que aprender una herramienta nueva.  
[Leerlo en LinkedIn](https://www.linkedin.com/pulse/el-cuello-de-botella-se-corri%C3%B3-dos-veces-saul-hernandez-7wb0f/) · 2026-08-13

<!-- ARTICLES:END -->

## Cómo está organizado

Cada artículo vive en su carpeta, con el texto en Markdown y el post que lo
acompaña. El índice de arriba **no se escribe a mano**: se genera desde los
metadatos de cada artículo con `scripts/build-index.py`, así no puede quedar
desactualizado.

```
dev-genius/
└── 01-el-primer-intento-fracaso/
    ├── articulo.md      el texto y sus metadatos
    ├── post.md          el post que lo acompaña
    └── banner.jpg       la portada, con el título ya compuesto
```

Lo que todavía no publiqué vive en la rama `drafts`, no en `main`. Acá solo
está lo que ya salió.

## Contacto

**saul@botsmith.ai** · [LinkedIn](https://www.linkedin.com/in/saulemprendedor) · [saul.botsmith.ai](https://saul.botsmith.ai)
