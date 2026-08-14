---
title: "Os números, e a descoberta que eu não esperava"
slug: los-numeros
series: dev-genius
episode: 5
date: 2026-08-14
status: published
lang: pt
summary: "Dois sprints medidos, e o dado que me surpreendeu: o aumento foi parelho entre perfis de senioridade diferente."
banner: banner.pt.jpg
---

# Os números, e a descoberta que eu não esperava

Quatro artigos de decisões de arquitetura não valem nada sem a parte que dá para questionar. Aqui vão os números, com a janela em que foram medidos, para que possam ser questionados.

## Dois sprints em produção, três desenvolvedores usando

- **50 tarefas** levadas da ideia ao merge
- **62 Pull Requests** com testes e ambiente de QA navegável
- **93%** chegou à revisão sem precisar de retrabalho
- **2,5 tarefas por dia útil**, sustentado ao longo dos dois sprints
- Cada tarefa toca em média **mais de um repositório**: backend e frontend na mesma unidade de trabalho

## Por que a meta era 3X

O objetivo nunca foi "usar IA". Era concreto e mensurável: **triplicar a capacidade de entrega do time sem contratar mais ninguém.**

Colocar um número na meta mudou todas as decisões de design. Um agente que escreve código elegante mas precisa de alguém olhando passo a passo não triplica nada: só muda o trabalho de lugar. Por isso o sistema não termina em *gerou o código*. Termina com o PR aberto, os checks rodando, o card movido e o thread contando o que aconteceu.

**O primeiro sprint com o sistema em funcionamento fechou com dois desenvolvedores entregando o dobro dos pontos com que tinham se comprometido**, medido contra o próprio histórico deles de sprints anteriores. Não contra uma média de mercado nem contra uma estimativa otimista: contra o que essas mesmas duas pessoas vinham entregando.

## A descoberta

Mas o dado que mais me interessa desse sprint não é o múltiplo. É que **o aumento foi parelho entre os dois, e eles têm níveis de senioridade diferentes.**

É o contrário do que costuma acontecer com as ferramentas de produtividade, que amplificam quem já era rápido e deixam o resto onde estava. Aqui quem sobe não é o indivíduo: **é o processo.**

O agente faz sempre os mesmos passos — investiga antes de escrever, pergunta o que não está claro, deixa a especificação por escrito, roda os checks, abre o PR — e esses passos são justamente os que um desenvolvedor com menos anos ainda está incorporando. A ferramenta não o torna mais experiente. **Ela empresta a ele o processo de alguém que é.**

Um sprint e duas pessoas não são uma amostra estatística. São um sinal. Mas é exatamente o sinal que eu estava procurando, porque significa que isso escala com o time e não com as estrelas do time.

## O que eu realmente aprendi

Comecei acreditando que o problema difícil era conseguir que o modelo escrevesse um bom código.

Não é. Isso já está resolvido.

Quando gerar uma implementação fica barato, o caro passa a ser tudo o que vem depois: revisar, testar, resolver conflitos quando cinco branches tocam o mesmo arquivo, manter o quadro em dia, não perder o rastro do que está esperando quem. Hoje a maior parte do sistema não é *a parte de IA*: são os processos de fundo que cuidam da fila.

Mas o resultado que mais me surpreende não é a velocidade. É que hoje um desenvolvedor com uma máquina que mal abra o Slack e um navegador entrega software com a qualidade e o contexto que antes exigiam anos de casa. Não porque o modelo o torne mais experiente: porque o conhecimento que antes vivia na cabeça dos seniores agora está no sistema, vivo, se atualizando a cada implementação.

É exatamente o contrário de onde comecei. Aquele primeiro piloto fracassou porque o conhecimento estava congelado e continuava vivendo nas pessoas. Tudo o que veio depois foi perseguir essa única coisa.

Construir com IA se parece muito menos com treinar um modelo e muito mais com desenhar uma linha de produção. O modelo é uma estação. O valor está no resto da linha.

Isso é DEV Genius: não uma ferramenta, mas a forma de montar essa linha em volta do modelo. É nisso que eu trabalho todos os dias.

Se você está tentando levar a IA da prova de conceito para o trabalho real do seu time, me escreva. Tenho interesse em comparar notas — é um problema em que quase todos estamos aprendendo ao mesmo tempo.

---

*Último artigo de uma série de cinco.*

*Vem do capítulo 4: [O gargalo se moveu duas vezes](https://saul.botsmith.ai/pt/blog/el-cuello-de-botella).*
