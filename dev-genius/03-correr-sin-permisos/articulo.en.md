---
title: "An agent that runs without asking for permissions: how to make it secure"
slug: correr-sin-permisos
series: dev-genius
episode: 3
date: 2026-08-11
status: published
lang: en
summary: "The five mitigations that turn a reckless idea into a defensible decision. None of them is about the model."
banner: banner.en.jpg
---

# An agent that runs without asking for permissions: how to make it secure

In [the previous article](https://saul.botsmith.ai/en/blog/un-solo-hilo) I said that the agent writing the code runs headless inside a sandbox, fully in charge of its own retries. What is missing is the detail that tends to raise an eyebrow: **it runs without asking for permissions.**

It doesn't ask before editing a file, or before running a command. And it has to be that way: a tight permission prompt in headless mode protects nothing, it only leaves the agent stuck waiting for an answer nobody is going to give.

It sounds reckless, and it would be if it stood alone. It doesn't.

## The five mitigations

**1 · The sandbox is the boundary.** A disposable room brought up for that ticket and destroyed when it ends. What happens inside stays inside. This is the primary mitigation: every other one assumes it exists.

**2 · It doesn't hold the GitHub token.** The agent only makes local commits, which need no credential. The push happens afterwards, from the outside, by the orchestrator, with a token injected per command and scoped to the repositories it should reach. By the time the token enters the scene, the agent has left.

**3 · The network is restricted.** Egress denied by default, with a short allowlist: the model's API, the repository, the package registries. With no way out there's no exfiltration, and that makes anything the agent could read far less interesting.

**4 · One single credential in its environment.** The model's, and nothing else. Not because I trust the agent, but because a credential that isn't there can't leak.

**5 · No Pull Request merges itself.** A human approves, always. It's the last barrier and the only one that doesn't depend on infrastructure.

## What these five have in common

None of them is about the model.

There's no prompt asking it to behave, no list of things it must not do. They are all constraints of the environment: what it can reach, what credentials exist around it, and who signs before anything reaches the main branch.

It's the difference between trusting and not needing to trust. A prompt asking for good behavior is a policy; a sandbox with no network egress is a guarantee. When you can choose, you choose the second.

The isolated sandbox isn't an infrastructure detail. **It's what turns a reckless idea into a defensible decision** — and it's what let me tell it in a meeting without the conversation ending right there.

With that settled, the line started producing for real. And then a problem I hadn't anticipated showed up: the bottleneck moved. Twice.

---

*Third article in a series of five.*

*Continues in chapter 4: [The bottleneck moved twice](https://saul.botsmith.ai/en/blog/el-cuello-de-botella).*
