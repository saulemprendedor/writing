# Banners — especificación y prompts

Cada artículo lleva una imagen de portada. La coherencia entre las cinco importa
más que lo lindo de cada una: si se ven como una familia, la serie parece una
serie. Si cada una tiene su estilo, parecen cinco artículos sueltos.

> **Esta especificación se reescribió desde el banner del capítulo 1**, que es
> el único de la nueva dirección que existe. Describe lo que esa portada es, no
> lo que se planeó antes. El prompt base de abajo está reconstruido a partir de
> la imagen: si el prompt real que la generó dice otra cosa, gana el real y este
> archivo se corrige.

---

## La dirección, en una línea

Render cinematográfico oscuro con el título compuesto encima. No es el diagrama
plano y abstracto de la versión anterior: acá hay profundidad, materia y una
escena. El texto va **dentro** de la imagen, no aparte.

## Formato común

| Parámetro | Valor |
|---|---|
| Medidas | Ancho apaisado, entre 3:2 y 16:9. El capítulo 1 es 1712 × 1152 |
| Ancho mínimo | **1200 px** — abajo de eso LinkedIn y Open Graph recomprimen feo |
| Fondo | Casi negro con tinte azul profundo |
| Acento principal | Azul cian brillante — el grafo, los nodos, las líneas de luz |
| Acento de tensión | Rojo, solo donde el concepto lo pide (alertas, roturas, fallas) |
| Estilo | Render 3D cinematográfico, profundidad de campo, glow volumétrico |
| Figuras | Permitidas: siluetas robóticas o humanoides, apenas insinuadas al fondo |
| Texto | **Compuesto dentro de la imagen** (ver abajo) |

El sitio **mide la imagen y respeta su proporción**, así que el tamaño exacto no
es crítico — no hay recorte que se coma nada. Lo que sí importa es que el pie no
quede pegado al borde.

## La composición

Tres zonas, siempre en el mismo lugar:

```
┌─────────────────────────────────────────────────────────┐
│  Título del artículo                                    │
│  en dos o tres líneas                    [ el motivo ]  │
│                                                         │
│  SAÚL HERNÁNDEZ                                         │
│  TECH LEAD — IA APLICADA AL DESARROLLO                  │
│                                                         │
│                                                         │
│  │ saul@botsmith.ai                     DEV GENIUS      │
│                                          ─────────      │
│                                              1 / 5      │
└─────────────────────────────────────────────────────────┘
```

- **Izquierda arriba:** el título, en blanco, condensada pesada, dos o tres
  líneas. Es lo primero que se lee en el feed.
- **Debajo:** el nombre en mayúsculas grandes, y el rol en gris con el
  interletrado abierto.
- **Derecha:** el motivo visual del capítulo, con aire alrededor.
- **Abajo izquierda:** una línea vertical fina y el email, en gris tenue.
- **Abajo derecha:** `DEV GENIUS`, una regla horizontal, y `N / 5`.

El pie y el bloque de nombre son **idénticos en las cinco**. El título y el
motivo son lo único que cambia.

---

## Prompt base

Este bloque va en **todos** los prompts. Es lo que mantiene la familia unida:

```
Wide cinematic 3D render, dark editorial tech illustration. Near-black
background with a deep blue tint. Bright cyan-blue as the light source: glowing
wireframe geometry, luminous nodes, thin light-traced connections. Volumetric
glow, shallow depth of field, fine grain. Faint robotic or humanoid silhouettes
far back in the darkness, barely readable, never the subject. Floating dark
panels and fragments catching the light. Leave the entire left half calm and
uncluttered — the title is composed there — and keep the bottom edge quiet.
Restrained, expensive, a little ominous. No text, no letters, no numbers, no
logos anywhere in the image.
```

Cuando el concepto lo pida, se le suma la tensión en rojo:

```
Red warning glyphs glowing on some of the fragments, and hairline red fracture
lines where the structure has broken. Red is the only warm color in the frame
and stays a minority against the blue.
```

---

## 1 · Mi primer intento con agentes de IA fracasó

**Concepto:** conocimiento congelado. Un grafo que fue vivo y quedó detenido.

```
[PROMPT BASE] + [TENSIÓN EN ROJO]

Subject: a bright cyan wireframe polyhedron of connected nodes floating at the
center-right, intact and glowing, surrounded by dark cracked panels drifting
apart. Chains hang broken from some of the fragments. Screens at the edges show
dense unreadable code, a few lines in red. The structure still holds, but
everything around it has failed.
```

## 2 · Por qué una feature debería vivir en un solo hilo

**Concepto:** cinco corrientes dispersas que convergen en una sola línea continua.

```
[PROMPT BASE]

Subject: five separate scattered streams of small nodes entering from the left
edge, each in a different muted color, converging and braiding into a single
bright continuous cyan line that runs cleanly to the right edge. Along that
single line, five evenly spaced luminous waypoints mark stages. The left side
feels tangled and noisy; the right side feels resolved and inevitable.
```

## 3 · Un agente que corre sin pedir permisos

**Concepto:** el sandbox como frontera. Contención, no confianza.

```
[PROMPT BASE]

Subject: a single luminous cube floating in dark empty space, its edges drawn in
thin cyan light, its interior filled with dense chaotic activity — sparks, rapid
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
cyan. At the second, particles are piling up in a dense bright cluster, waiting.
A faint ghost outline shows where the first bottleneck used to be. The sense is
of a problem that relocated rather than disappeared.
```

## 5 · Los números, y el hallazgo que no esperaba

**Concepto:** dos curvas de distinta altura que suben con la misma pendiente.

```
[PROMPT BASE]

Subject: two ascending line graphs on a dark grid, starting at clearly different
heights but rising with exactly the same slope, perfectly parallel. Thin
measurement ticks along the vertical axis, no labels. Subtle glow where the
lines climb. The composition should make the parallelism unmistakable — that is
the finding.
```

---

## Cómo usarlos

1. Generá la imagen con el prompt correspondiente (prompt base + subject),
   dejando la mitad izquierda despejada.
2. Verificá que **no haya texto** en la imagen generada. Si el modelo metió
   letras, regenerá — no las tapes.
3. Componé encima el título, el bloque de nombre y el pie. El pie y el nombre
   se copian tal cual del capítulo anterior: es lo que no puede variar.
4. Guardala en la carpeta del artículo y nombrala en el frontmatter (`banner:`).
   El sitio sirve el archivo que ahí diga, con el formato que tenga.

**Si alguna imagen sale muy cargada**, pedile *"more negative space, fewer
elements, calmer composition"*. El error más común de estos modelos es llenar el
cuadro; la contención es lo que las va a hacer ver profesionales.
