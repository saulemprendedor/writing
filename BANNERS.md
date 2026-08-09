# Banners — especificación y prompts

Cada artículo lleva una imagen de portada. La coherencia entre las cinco importa
más que lo lindo de cada una: si se ven como una familia, la serie parece una
serie. Si cada una tiene su estilo, parecen cinco artículos sueltos.

---

## Formato común

| Parámetro | Valor |
|---|---|
| Medidas | **1920 × 1080 px** (16:9) — baja bien a los tamaños de LinkedIn |
| Fondo | Casi negro, `#0d1117` |
| Acento | Turquesa `#2dd4bf` — el mismo de `saul.botsmith.ai` y `devgenius.botsmith.ai` |
| Acentos secundarios | Verde `#3fb950`, ámbar `#d29922`, violeta `#a371f7` — con moderación |
| Estilo | Abstracto, técnico, sin personas, sin robots, sin cerebros de circuitos |
| Franja inferior | **20% de alto, vacía** — ahí va el pie de marca |

## El pie de marca va compuesto aparte

**No le pidas el texto al generador de imágenes.** Ningún modelo va a producir
exactamente el mismo pie cinco veces: cambia el interletrado, se come una tilde,
mueve el email dos píxeles. Y el pie es justamente lo que tiene que ser idéntico.

El flujo correcto: **generás la imagen con la franja inferior vacía**, y después
componés el texto encima — en Figma, Canva o con la plantilla que quieras. Cinco
veces el mismo bloque, sin variación.

El pie, siempre igual:

```
SAÚL HERNÁNDEZ  ·  TECH LEAD — IA APLICADA AL DESARROLLO
saul@botsmith.ai                                     DEV GENIUS  ·  1/5
```

- Izquierda: nombre y rol, en mayúsculas, con el interletrado abierto
- Debajo: el email, en un gris tenue
- Derecha: la serie y el número de episodio, en turquesa
- Sobre la franja, una línea de 1px en turquesa al 25% separándola de la imagen

---

## Prompt base

Este bloque va en **todos** los prompts. Es lo que mantiene la familia unida:

```
Wide 16:9 technical illustration, 1920x1080. Abstract, editorial, engineering
diagram aesthetic. Near-black background (#0d1117) with a single teal accent
color (#2dd4bf). Thin precise lines, generous negative space, subtle film grain,
soft volumetric glow around the accent elements. No text, no letters, no numbers,
no logos anywhere in the image. No people, no robots, no humanoid figures, no
brain imagery, no circuit-board clichés. Leave the bottom 20% of the frame empty
and uncluttered — a calm dark band with nothing in it. Cinematic, restrained,
confident. Feels like a systems diagram drawn by someone with taste.
```

---

## 1 · Mi primer intento con agentes de IA fracasó

**Concepto:** conocimiento congelado. Un grafo que fue vivo y quedó detenido.

```
[PROMPT BASE]

Subject: a network of connected nodes forming an agent graph, but frozen —
encased in translucent ice or crystal, with hairline fractures spreading across
the structure. A few connection lines have gone dark and broken, drifting apart
as fragments. The teal glow inside the crystal is dimming, as if the system is
cooling down. The impression is of something that worked once and stopped
keeping up.
```

## 2 · Por qué una feature debería vivir en un solo hilo

**Concepto:** cinco corrientes dispersas que convergen en una sola línea continua.

```
[PROMPT BASE]

Subject: five separate scattered streams of small nodes entering from the left
edge, each in a different muted color, converging and braiding into a single
bright continuous teal line that runs cleanly to the right edge. Along that
single line, five evenly spaced luminous waypoints mark stages. The left side
feels tangled and noisy; the right side feels resolved and inevitable.
```

## 3 · Un agente que corre sin pedir permisos

**Concepto:** el sandbox como frontera. Contención, no confianza.

```
[PROMPT BASE]

Subject: a single luminous cube floating in dark empty space, its edges drawn in
thin teal light, its interior filled with dense chaotic activity — sparks, rapid
motion, energy contained. The cube is sealed: no line, particle or glow escapes
its faces. Around it, absolute stillness and darkness. The contrast between the
turbulence inside and the calm outside is the whole point.
```

## 4 · El cuello de botella se corrió dos veces

**Concepto:** la restricción que se mueve. El embudo se desplaza.

```
[PROMPT BASE]

Subject: a horizontal pipeline of flowing particles moving left to right, with
two distinct narrow constriction points along its length. At the first
constriction the flow has already been widened and now passes freely, glowing
teal. At the second, particles are piling up in a dense bright cluster, waiting.
A faint ghost outline shows where the first bottleneck used to be. The sense is
of a problem that relocated rather than disappeared.
```

## 5 · Los números, y el hallazgo que no esperaba

**Concepto:** dos curvas de distinta altura que suben con la misma pendiente.

```
[PROMPT BASE]

Subject: two ascending line graphs on a dark grid, starting at clearly different
heights but rising with exactly the same slope, perfectly parallel. The lower
line is teal, the upper one a soft green. Thin measurement ticks along the
vertical axis, no labels. Subtle glow where the lines climb. The composition
should make the parallelism unmistakable — that is the finding.
```

---

## Cómo usarlos

1. Generá la imagen con el prompt correspondiente (prompt base + subject).
2. Verificá que **no haya texto** en la imagen. Si el modelo metió letras,
   regenerá — no las tapes.
3. Verificá que la franja inferior quedó despejada.
4. Componé el pie de marca encima, idéntico en las cinco.
5. Guardala como `banner.png` en la carpeta del artículo.

**Si alguna imagen sale muy cargada**, pedile *"more negative space, fewer
elements, calmer composition"*. El error más común de estos modelos es llenar el
cuadro; la contención es lo que las va a hacer ver profesionales.
