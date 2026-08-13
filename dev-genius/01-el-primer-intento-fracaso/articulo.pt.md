---
title: "Minha primeira tentativa com agentes de IA fracassou. O problema não era o modelo"
slug: el-primer-intento-fracaso
series: dev-genius
episode: 1
date: 2026-08-09
status: published
lang: pt
summary: "Um piloto com orquestradores de agentes que ajudava e se depreciava sozinho. Por que o conhecimento congelado era o problema real, e o que fiz depois de abandoná-lo."
banner: banner.pt.jpg
---

# Minha primeira tentativa com agentes de IA fracassou. O problema não era o modelo

Há um ano comecei um piloto, com o respaldo da empresa, para construir ferramentas autônomas de IA sobre o trabalho de desenvolvimento.

Um ano depois, dois desenvolvedores do time entregaram o dobro dos pontos com que tinham se comprometido em uma sprint — e o aumento não veio da senioridade deles.

Entre essas duas coisas houve um fracasso completo. Começo por aí, porque é a parte que ninguém conta.

## O piloto que se depreciava sozinho

Usei o que se usava na época: orquestradores de agentes, papéis, ferramentas encadeadas. Cada agente com seu prompt, sua responsabilidade e seu lugar na cadeia.

Ajudava. E se depreciava sozinho.

O problema não era o modelo nem o framework — os dois faziam o que prometiam. Era que o conhecimento que eu dava a eles estava **congelado**. Cada agente sabia o que eu tinha escrito no prompt dele no dia em que escrevi, e nada mais.

E a maior parte do que é preciso para mexer em um sistema real não está escrita em lugar nenhum. Está na cabeça das pessoas: por que aquela tabela tem um campo estranho, o que quebra se você mexer naquele serviço, o que foi decidido há dois anos e por que ninguém reverteu. Esse conhecimento vive sobretudo nos seniores, e não se transfere escrevendo um prompt mais longo.

O sistema envelhecia enquanto o produto avançava. A cada semana sabia um pouco menos sobre o código em que trabalhava.

Larguei.

## Um mês sem construir automação

Tirei um mês de reinício. Não parei de trabalhar: segui entregando meus tickets como sempre, com Cursor e Claude Code, as ferramentas do dia a dia. O que parei foi de construir — não escrevi mais uma linha de automação naquele mês.

Usei esse tempo para ler e reorientar. Foi o período em que a Anthropic publicava praticamente toda semana, e me dediquei a entender o que estava mudando de verdade por baixo do barulho.

A pergunta com que voltei era outra. Não *como faço um agente mais esperto*, e sim **como paro de perder o conhecimento**.

## Documentação que não envelhece

Encontrei uma forma de documentar o histórico de decisões do negócio. Não a documentação que ninguém atualiza e que em três meses mente — mas o registro do *porquê* das coisas serem como são: o que foi decidido, contra quais alternativas e qual restrição motivou aquilo.

E acrescentei a peça que muda tudo: **ao terminar cada implementação, essa documentação é atualizada com o resultado.**

É um detalhe pequeno e é toda a diferença. O conhecimento deixa de ser uma foto e passa a ser um registro vivo. O contexto deixa de ser uma suposição minha sobre o que o agente precisa saber, e passa a ser algo que o próprio trabalho mantém em dia.

## O experimento

Testei em mim mesmo. Na minha máquina, nos meus tickets do dia, sem contar para ninguém.

Os resultados foram desproporcionais: a diferença de tempo entre um ticket pequeno e um grande passou a ser medida em minutos, não em horas nem em dias. Não porque eu escrevesse código mais rápido — porque parei de gastar o tempo reconstruindo o contexto toda vez.

Mas continuava vivendo no meu laptop.

Que é onde vive quase tudo o que nós, desenvolvedores, construímos para nós mesmos: a ferramenta que te deixa duas vezes mais produtivo e que ninguém mais usa, porque nunca saiu da sua pasta de scripts.

Tirar aquilo dali foi o problema seguinte. E acabou sendo um problema de design, não de código.

---

*Primeiro artigo de uma série de cinco sobre como construí um sistema de agentes que entrega software em produção.*

*Continua no capítulo 2: [Por que uma feature deveria viver em um único thread](https://saul.botsmith.ai/pt/blog/un-solo-hilo).*
