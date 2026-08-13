---
title: "Um agente que roda sem pedir permissões: como fazer isso com segurança"
slug: correr-sin-permisos
series: dev-genius
episode: 3
date: 2026-08-11
status: published
lang: pt
summary: "As cinco mitigações que transformam uma ideia imprudente em uma decisão defensável. Nenhuma delas é sobre o modelo."
banner: banner.pt.jpg
---

# Um agente que roda sem pedir permissões: como fazer isso com segurança

No [artigo anterior](https://saul.botsmith.ai/pt/blog/un-solo-hilo) contei que o agente que escreve o código roda em modo headless dentro de um sandbox, dono total das suas tentativas. Falta o detalhe que costuma levantar uma sobrancelha: **ele roda sem pedir permissões.**

Não pergunta antes de editar um arquivo, nem antes de rodar um comando. E tem que ser assim: uma permissão apertada em modo headless não protege nada, só deixa o agente travado esperando uma resposta que ninguém vai dar.

Soa temerário, e seria se estivesse sozinho. Não está.

## As cinco mitigações

**1 · O sandbox é a fronteira.** Um quarto descartável que sobe para aquela tarefa e é destruído ao terminar. O que acontece lá dentro fica lá dentro. Esta é a mitigação primária: todas as outras assumem que ela existe.

**2 · Ele não tem o token do GitHub.** O agente só faz commits locais, que não exigem credencial. O push é feito depois pelo orquestrador, de fora, com um token injetado por comando e limitado aos repositórios que correspondem. Quando o token entra em cena, o agente já saiu.

**3 · A rede é restrita.** Saída negada por padrão, com uma lista curta de domínios permitidos: a API do modelo, o repositório, os registros de pacotes. Sem saída não há exfiltração, e isso torna muito menos interessante qualquer coisa que o agente pudesse ler.

**4 · Uma única credencial no ambiente dele.** A do modelo, e nada mais. Não porque eu confie no agente, mas porque uma credencial que não está lá não pode vazar.

**5 · Nenhum Pull Request faz merge sozinho.** Um humano aprova, sempre. É a última barreira e a única que não depende de infraestrutura.

## O que essas cinco têm em comum

Nenhuma é sobre o modelo.

Não há um prompt pedindo que ele se comporte, nem uma lista de coisas que ele não deve fazer. Todas são restrições do ambiente: o que ele pode alcançar, que credenciais existem ao redor dele, e quem assina antes de algo chegar à branch principal.

É a diferença entre confiar e não precisar confiar. Um prompt que pede bom comportamento é uma política; um sandbox sem saída de rede é uma garantia. Quando dá para escolher, você escolhe a segunda.

O sandbox isolado não é um detalhe de infraestrutura. **É o que transforma uma ideia imprudente em uma decisão defensável** — e é o que me permitiu contar isso em uma reunião sem que a conversa terminasse ali.

Com isso resolvido, a linha começou a produzir de verdade. E então apareceu um problema que eu não tinha antecipado: o gargalo mudou de lugar. Duas vezes.

---

*Terceiro artigo de uma série de cinco.*

*Continua no capítulo 4: [O gargalo se moveu duas vezes](https://saul.botsmith.ai/pt/blog/el-cuello-de-botella).*
