# Saúl Hernández — writing about building with AI

**English** · [Español](#saúl-hernández--escribiendo-sobre-construir-con-ia)

> *I'm a Tech Lead with 15 years building software, currently leading development
> teams at Chile's largest bus-travel platform. I write about building AI agent
> systems that ship real software — architecture decisions, what failed, and the
> numbers. Everything here is from production, not from a demo.*

---

This repository is what I write, and why.

I've spent 15 years building software. The last year went into a single
question: what does it take for an AI agent to write not demo code, but
software that reaches production — with a spec, tests, human review and
someone accountable when it breaks.

The answer wasn't a better model. It was a process.

What you'll find here isn't a collection of best practices. **It's the whole
road, with the failure up front:** my first attempt depreciated on its own, I
walked away from it, took a month without writing code, and came back from
another angle. I write with numbers I can defend and with the decisions I got
wrong before getting them right.

If this is your line of work, you're probably somewhere on the same road.

## Articles

Every article is written in Spanish first and then translated. Each entry
links to its other languages.

<!-- ARTICLES_EN:START -->

### DEV Genius — how I built an agent system that ships software

**1. [My first attempt with AI agents failed. The problem wasn't the model](dev-genius/01-el-primer-intento-fracaso/articulo.en.md)**  
A pilot built on agent orchestrators that helped and depreciated on its own. Why frozen knowledge was the real problem, and what I did after walking away from it.  
[Read it on LinkedIn](https://www.linkedin.com/pulse/mi-primer-intento-con-agentes-de-ia-fracas%C3%B3-el-era-modelo-hernandez-ikpqf/) (in Spanish) · 2026-08-09 · [Español](dev-genius/01-el-primer-intento-fracaso/articulo.es.md) · [Português](dev-genius/01-el-primer-intento-fracaso/articulo.pt.md)

**2. [Why a feature should live in a single thread](dev-genius/02-un-solo-hilo/articulo.en.md)**  
The idea that got the experiment off my laptop, and the architecture decision that holds it up: orchestrate the process, delegate the loop.  
[Read it on LinkedIn](https://www.linkedin.com/pulse/por-qu%C3%A9-una-feature-deber%C3%ADa-vivir-en-un-solo-hilo-saul-hernandez-aq8cc/) (in Spanish) · 2026-08-10 · [Español](dev-genius/02-un-solo-hilo/articulo.es.md) · [Português](dev-genius/02-un-solo-hilo/articulo.pt.md)

**3. [An agent that runs without asking for permissions: how to make it secure](dev-genius/03-correr-sin-permisos/articulo.en.md)**  
The five mitigations that turn a reckless idea into a defensible decision. None of them is about the model.  
[Read it on LinkedIn](https://www.linkedin.com/pulse/un-agente-que-corre-sin-pedir-permisos-c%C3%B3mo-se-hace-eso-hernandez-0fnqf/) (in Spanish) · 2026-08-11 · [Español](dev-genius/03-correr-sin-permisos/articulo.es.md) · [Português](dev-genius/03-correr-sin-permisos/articulo.pt.md)

**4. [The bottleneck moved twice](dev-genius/04-el-cuello-de-botella/articulo.en.md)**  
Automating one stage doesn't speed up the system: it moves the constraint. And why nobody on the team had to learn a new tool.  
[Read it on LinkedIn](https://www.linkedin.com/pulse/el-cuello-de-botella-se-corri%C3%B3-dos-veces-saul-hernandez-7wb0f/) (in Spanish) · 2026-08-13 · [Español](dev-genius/04-el-cuello-de-botella/articulo.es.md) · [Português](dev-genius/04-el-cuello-de-botella/articulo.pt.md)

<!-- ARTICLES_EN:END -->

## How it's organized

Each article lives in its own folder: one Markdown file per language, the
companion post, and the cover. The index above **isn't written by hand** — it
is generated from each article's own metadata by `scripts/build-index.py`, so
it can't fall out of date.

```
dev-genius/
└── 01-el-primer-intento-fracaso/
    ├── articulo.es.md   the text and its metadata — Spanish is the source
    ├── articulo.en.md   the English translation
    ├── articulo.pt.md   the Portuguese translation
    ├── post.md          the companion post
    └── banner.jpg       the cover, with the title already composed on it
```

What I haven't published yet lives on the `drafts` branch, not on `main`.
This one only holds what is already out.

---

# Saúl Hernández — escribiendo sobre construir con IA

[English](#saúl-hernández--writing-about-building-with-ai) · **Español**

> *Soy Tech Lead, llevo 15 años construyendo software y hoy dirijo equipos de
> desarrollo en la plataforma de viajes en bus más grande de Chile. Escribo
> sobre construir sistemas de agentes de IA que entregan software de verdad —
> decisiones de arquitectura, lo que falló y los números. Todo esto sale de
> producción, no de una demo.*

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

Cada artículo se escribe primero en español y después se traduce. Cada entrada
enlaza a sus otros idiomas.

<!-- ARTICLES:START -->

### DEV Genius — cómo construí un sistema de agentes que entrega software

**1. [Mi primer intento con agentes de IA fracasó. El problema no era el modelo](dev-genius/01-el-primer-intento-fracaso/articulo.es.md)**  
Un piloto con orquestadores de agentes que ayudaba y se depreciaba solo. Por qué el conocimiento congelado era el problema real, y qué hice después de abandonarlo.  
[Leerlo en LinkedIn](https://www.linkedin.com/pulse/mi-primer-intento-con-agentes-de-ia-fracas%C3%B3-el-era-modelo-hernandez-ikpqf/) · 2026-08-09 · [English](dev-genius/01-el-primer-intento-fracaso/articulo.en.md) · [Português](dev-genius/01-el-primer-intento-fracaso/articulo.pt.md)

**2. [Por qué una feature debería vivir en un solo hilo](dev-genius/02-un-solo-hilo/articulo.es.md)**  
La idea que sacó el experimento de mi laptop, y la decisión de arquitectura que la sostiene: orquestar el proceso y delegar el ciclo.  
[Leerlo en LinkedIn](https://www.linkedin.com/pulse/por-qu%C3%A9-una-feature-deber%C3%ADa-vivir-en-un-solo-hilo-saul-hernandez-aq8cc/) · 2026-08-10 · [English](dev-genius/02-un-solo-hilo/articulo.en.md) · [Português](dev-genius/02-un-solo-hilo/articulo.pt.md)

**3. [Un agente que corre sin pedir permisos: cómo se hace eso seguro](dev-genius/03-correr-sin-permisos/articulo.es.md)**  
Las cinco mitigaciones que convierten una idea imprudente en una decisión defendible. Ninguna es sobre el modelo.  
[Leerlo en LinkedIn](https://www.linkedin.com/pulse/un-agente-que-corre-sin-pedir-permisos-c%C3%B3mo-se-hace-eso-hernandez-0fnqf/) · 2026-08-11 · [English](dev-genius/03-correr-sin-permisos/articulo.en.md) · [Português](dev-genius/03-correr-sin-permisos/articulo.pt.md)

**4. [El cuello de botella se corrió dos veces](dev-genius/04-el-cuello-de-botella/articulo.es.md)**  
Automatizar una etapa no acelera el sistema: mueve la restricción. Y por qué nadie del equipo tuvo que aprender una herramienta nueva.  
[Leerlo en LinkedIn](https://www.linkedin.com/pulse/el-cuello-de-botella-se-corri%C3%B3-dos-veces-saul-hernandez-7wb0f/) · 2026-08-13 · [English](dev-genius/04-el-cuello-de-botella/articulo.en.md) · [Português](dev-genius/04-el-cuello-de-botella/articulo.pt.md)

<!-- ARTICLES:END -->

## Cómo está organizado

Cada artículo vive en su carpeta: un archivo Markdown por idioma, el post que
lo acompaña y la portada. El índice de arriba **no se escribe a mano**: se
genera desde los metadatos de cada artículo con `scripts/build-index.py`, así
no puede quedar desactualizado.

```
dev-genius/
└── 01-el-primer-intento-fracaso/
    ├── articulo.es.md   el texto y sus metadatos — el español es la fuente
    ├── articulo.en.md   la traducción al inglés
    ├── articulo.pt.md   la traducción al portugués
    ├── post.md          el post que lo acompaña
    └── banner.jpg       la portada, con el título ya compuesto
```

Lo que todavía no publiqué vive en la rama `drafts`, no en `main`. Acá solo
está lo que ya salió.

---

## Contacto · Contact

**saul@botsmith.ai** · [LinkedIn](https://www.linkedin.com/in/saulemprendedor) · [saul.botsmith.ai](https://saul.botsmith.ai)
