---
title: "Why a feature should live in a single thread"
slug: un-solo-hilo
series: dev-genius
episode: 2
date: 2026-08-10
status: published
lang: en
summary: "The idea that got the experiment off my laptop, and the architecture decision that holds it up: orchestrate the process, delegate the loop."
banner: banner.jpg
---

# Why a feature should live in a single thread

In [the previous article](https://saul.botsmith.ai/en/blog/el-primer-intento-fracaso) I told how, after a failed pilot, I found a way to stop the system's knowledge from aging. It worked — and it lived on my laptop.

The second piece came from a Salesforce presentation about AI features inside Slack. That is where the idea hit me: **if the whole team already lives in Slack, why are the tools of the job not there?**

And above all: why does a feature go through five different places — idea, design, build, sign-off, merge — instead of living in **a single thread**, where anyone can read the whole story from beginning to end.

The challenge was not technical, it was one of standard. The tools I put in that thread had to be **as good as or better than** the ones each area already used. If they were worse, nobody would move — and rightly so.

So I took the experiment to Slack, and the implementation that ran on my machine moved to ephemeral sandboxes in the cloud. And something showed up that I had not gone looking for: I could work on several features **at once**.

## The architecture decision: the agent does not drive

The temptation when you build something like this is to make an autonomous agent. You hand it the tools, you explain the goal, and it figures the rest out.

I did the opposite. **The system is an explicit orchestrator.** The flow — claim the ticket, investigate the code, raise the open questions, write the spec, implement, run the checks, open the PR — is coded step by step. The model is called only for the atomic tasks where it genuinely adds something: analyzing, drafting, deciding. It does not decide what comes next. I already know that part.

Why? Because an autonomous agent is impossible to debug. When something goes wrong at step 7 of 12, you want to be able to look at step 7. With an explicit flow there is a trace: every phase leaves its mark on that ticket's thread. Anyone can open it and see what it investigated, what it asked and what it did.

Autonomy is seductive in the demo and expensive in production.

## The exception that changed my mind

And yet, there is one place where I handed over control completely.

I used to orchestrate the code-writing phase as well: ask the model to edit this file, run the linter, if it fails send the error back, retry. Hundreds of lines coordinating an implement → verify → fix loop.

One day it hit me that I was hand-rolling — and worse, hand-rolling something that already existed and was done well: the agentic loop of a real coding tool. I pulled all that orchestration out and replaced it with a coding agent running headless **inside the sandbox**, fully in charge of its own retries. The orchestrator was left with one responsibility: read the task file every few seconds and mirror the progress, from ⏳ to ✓.

Hundreds of lines went away. And it got better, because inside the sandbox the agent reads the project's conventions natively instead of getting them pre-chewed by my prompt.

The rule I took from it: **orchestrate the process explicitly, delegate the loop.** The process is yours because it is your engineering judgment. The implement-and-fix-itself loop is not, and competing with it is misplaced pride.

That set of principles is what I ended up calling **DEV Genius**. It is not a tool: it is the way the line of work is built around the model.

One uncomfortable question is left, and it is the one for the next article: that agent runs **without asking for permissions**. How do you do that without it being reckless?

---

*Second article in a series of five.*

*Continues in chapter 3: [An agent that runs without asking for permissions: how to make that safe](https://saul.botsmith.ai/en/blog/correr-sin-permisos).*
