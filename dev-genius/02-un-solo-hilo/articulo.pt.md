---
title: "Por que uma feature deveria viver em uma única thread"
slug: un-solo-hilo
series: dev-genius
episode: 2
date: 2026-08-10
status: published
lang: pt
summary: "A ideia que tirou o experimento do meu laptop, e a decisão de arquitetura que a sustenta: orquestrar o processo e delegar o ciclo."
banner: banner.jpg
---

# Por que uma feature deveria viver em uma única thread

No [artigo anterior](https://saul.botsmith.ai/pt/blog/el-primer-intento-fracaso) contei como, depois de um piloto fracassado, encontrei uma forma de o conhecimento do sistema parar de envelhecer. Funcionava — e vivia no meu laptop.

A segunda peça veio de uma apresentação da Salesforce sobre funcionalidades de IA dentro do Slack. Foi ali que a ideia estourou: **se o time inteiro já vive no Slack, por que as ferramentas do trabalho não estão lá?**

E, sobretudo: por que uma feature atravessa cinco lugares diferentes — ideia, design, construção, certificação, merge — em vez de viver em **uma única thread**, onde qualquer um pode ler a história completa do começo ao fim.

O desafio não era técnico, era de nível. As ferramentas que eu colocasse nessa thread tinham que ser **iguais ou melhores** do que as que cada área já usava. Se fossem piores, ninguém se mudava — e com razão.

Então levei o experimento para o Slack, e a implementação que rodava na minha máquina passou para sandboxes efêmeros na nuvem. Aí apareceu algo que eu não tinha ido buscar: dava para trabalhar em várias features **ao mesmo tempo**.

## A decisão de arquitetura: o agente não dirige

A tentação quando você constrói algo assim é fazer um agente autônomo. Você dá as ferramentas, explica o objetivo e que ele se vire.

Fiz o contrário. **O sistema é um orquestrador explícito.** O fluxo — assumir a tarefa, investigar o código, levantar as dúvidas, escrever a especificação, implementar, rodar os checks, abrir o PR — está codificado passo a passo. O modelo é chamado só para as tarefas atômicas em que ele realmente agrega: analisar, redigir, decidir. Ele não decide o que vem depois. Isso eu já sei.

Por quê? Porque um agente autônomo é impossível de depurar. Quando algo dá errado no passo 7 de 12, você quer poder olhar o passo 7. Com um fluxo explícito há rastro: cada fase deixa sua marca na thread daquela tarefa. Qualquer um abre e vê o que ele investigou, o que perguntou e o que fez.

A autonomia é sedutora na demo e cara em produção.

## A exceção que me fez mudar de ideia

E, ainda assim, há um lugar onde deleguei o controle por completo.

A fase de escrever o código eu também orquestrava: peça ao modelo que edite este arquivo, rode o linter, se falhar mande o erro de volta, tente de novo. Centenas de linhas coordenando um ciclo de implementar → verificar → corrigir.

Um dia caí na real de que estava reimplementando na mão — e pior, algo que já existia e bem feito: o ciclo agêntico de uma ferramenta de codificação de verdade. Tirei toda essa orquestração e a substituí por um agente de codificação rodando em modo headless **dentro do sandbox**, dono total das suas tentativas. O orquestrador ficou com uma única responsabilidade: ler o arquivo de tarefas a cada poucos segundos e refletir o progresso, de ⏳ para ✓.

Foram-se centenas de linhas. E melhorou, porque dentro do sandbox o agente lê as convenções do projeto de forma nativa em vez de recebê-las mastigadas pelo meu prompt.

A regra que levei comigo: **orquestre o processo explicitamente, delegue o ciclo.** O processo é seu porque é o seu critério de engenharia. O ciclo de implementar-e-se-corrigir não é, e competir com ele é orgulho mal investido.

A esse conjunto de princípios acabei chamando de **DEV Genius**. Não é uma ferramenta: é a forma de montar a linha de trabalho em volta do modelo.

Fica uma pergunta incômoda, que é a do próximo artigo: esse agente roda **sem pedir permissões**. Como se faz isso sem que seja uma imprudência?

---

*Segundo artigo de uma série de cinco.*

*Continua no capítulo 3: [Um agente que roda sem pedir permissões: como fazer isso com segurança](https://saul.botsmith.ai/pt/blog/correr-sin-permisos).*
