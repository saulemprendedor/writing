---
title: "O gargalo se moveu duas vezes"
slug: el-cuello-de-botella
series: dev-genius
episode: 4
date: 2026-08-13
status: published
lang: pt
summary: "Automatizar uma etapa não acelera o sistema: move a restrição. E por que ninguém do time teve que aprender uma ferramenta nova."
banner: banner.pt.jpg
---

# O gargalo se moveu duas vezes

Comecei por onde doía: a **implementação**. É a etapa visível, a que todo mundo quer automatizar primeiro. E funcionou.

Então o problema se mudou para cima.

## Primeiro: a definição

Com a implementação resolvida, o que travava a linha era a **definição**. Um ticket ambíguo não fica menos ambíguo porque quem o implementa é rápido: ou o agente constrói com precisão a coisa errada, ou ele para para perguntar e a tarefa fica esperando um humano.

Eu tinha automatizado a etapa veloz e deixado intacta a que decide se essa velocidade serve para alguma coisa.

Então a definição também precisava ser modelada: que o agente investigue o código antes de escrever o ticket, que redija escopo e critérios de aceitação, e que levante suas dúvidas com o time antes de tocar em uma linha. Não é um passo anterior ao trabalho — é parte do trabalho.

## Depois: a certificação

Com isso resolvido, o gargalo mudou de novo. Agora para baixo.

A linha começou a produzir e as tarefas se empilharam esperando **certificação de QA**. É o resultado natural de acelerar tudo o que vem antes: o trabalho terminado se acumula na frente da única etapa que você não tocou. E um backlog de coisas esperando alguém validar não é melhor do que um backlog de coisas a fazer. Só mudou de lugar.

Aí apareceu a pergunta que eu deveria ter feito muito antes: **se o sandbox já sobe o ambiente completo para implementar o ticket, por que ele não serve para certificá-lo?** O ambiente está montado, com os repositórios rodando e uma URL navegável. A distância entre *aqui o código foi escrito* e *aqui o caso é testado* era zero, e eu estava tratando as duas coisas como mundos diferentes.

A lição me custou duas voltas: **automatizar uma etapa não acelera o sistema, move a restrição.** Se você não perseguir para onde ela foi, tudo o que construiu foi um funil mais rápido apontando para a mesma rolha.

## Ninguém teve que aprender uma ferramenta nova

Há uma segunda parte nisso, que é a que decide se algo assim é adotado ou vira enfeite.

Cada fase da linha tem sua própria dinâmica e sua própria ferramenta. A definição vive no tracker. As dúvidas se resolvem conversando no Slack. O código e a revisão passam pelo GitHub. O QA é feito abrindo um navegador.

A tentação é construir uma interface própria: um painel onde tudo é controlado, caprichado, com o fluxo inteiro à vista. É aí que a maioria desses projetos morre — não por capacidade técnica, mas porque obrigam o time a se mudar. Uma ferramenta que exige mudança compete contra o trabalho real, e o trabalho real ganha sempre.

Fiz o contrário: o agente entra em cada fase pela porta que já estava aberta. O ticket é escrito no tracker que o time já usava, no formato dele. As dúvidas chegam no thread onde aquela conversa já acontecia. O Pull Request aparece no GitHub como qualquer outro e é revisado como qualquer outro. O ambiente de QA é uma URL que se abre no navegador.

Ninguém trocou de ferramenta. O que mudou é quanta operação manual cada um faz dentro dela.

Esse detalhe é o que decide a adoção: **o time não sente que está usando uma IA. Sente que o mesmo trabalho tem menos passos.** Não houve capacitação, nem migração, nem um período de se acostumar com o sistema novo. Desde o primeiro dia se trabalhava diferente sem ter aprendido nada.

Uma vez que você sabe onde está o gargalo, o trabalho não é substituir aquela etapa. É automatizar seus pontos de fricção **sem tirá-la de onde ela vive**.

No último artigo vão os números, e a descoberta que eu não esperava.

---

*Quarto artigo de uma série de cinco.*

*Continua no capítulo 5: [Os números, e a descoberta que eu não esperava](https://saul.botsmith.ai/pt/blog/los-numeros).*

*Vem do capítulo 3: [Um agente que roda sem pedir permissões: como fazer isso com segurança](https://saul.botsmith.ai/pt/blog/correr-sin-permisos).*
