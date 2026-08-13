---
title: "The bottleneck moved twice"
slug: el-cuello-de-botella
series: dev-genius
episode: 4
date: 2026-08-13
status: published
lang: en
summary: "Automating one stage does not speed up the system: it moves the constraint. And why nobody on the team had to learn a new tool."
banner: banner.jpg
---

# The bottleneck moved twice

I started where it hurt: **implementation**. It is the visible stage, the one everybody wants to automate first. And it worked.

Then the problem moved upstream.

## First: definition

With implementation solved, what held the line back was **definition**. An ambiguous ticket does not get less ambiguous because whoever implements it is fast: either the agent builds the wrong thing precisely, or it stops to ask and the ticket sits waiting for a human.

I had automated the fast stage and left untouched the one that decides whether that speed is worth anything.

So definition had to be modeled too: the agent investigates the code before writing the ticket, drafts the scope and the acceptance criteria, and raises its open questions with the team before touching a line. It is not a step before the work — it is part of the work.

## Then: sign-off

With that solved, the bottleneck moved again. Downstream this time.

The line started producing and tickets piled up waiting for **QA sign-off**. That is the natural result of speeding up everything before it: finished work accumulates in front of the one stage you did not touch. And a backlog of things waiting for someone to validate them is no better than a backlog of things to do. It only changed places.

That is when the question I should have asked much earlier showed up: **if the sandbox already brings up the whole environment to implement the ticket, why is it not good enough to certify it?** The environment is right there, with the repositories running and a URL you can browse. The distance between *this is where the code was written* and *this is where the case gets tested* was zero, and I was treating them as two different worlds.

The lesson cost me two rounds: **automating a stage does not speed up the system, it moves the constraint.** If you do not chase where it went, all you built is a faster funnel pointing at the same plug.

## Nobody had to learn a new tool

There is a second part to this, and it is the one that decides whether something like this gets adopted or ends up as decoration.

Every phase of the line has its own dynamic and its own tool. Definition lives in the tracker. Open questions get resolved by talking in Slack. Code and review go through GitHub. QA is done by opening a browser.

The temptation is to build an interface of your own: one panel where everything is controlled, tidy, with the whole flow in view. That is where most of these projects die — not for lack of technical ability, but because they force the team to move house. A tool that demands a move competes against the real work, and the real work wins every time.

I did the opposite: the agent enters each phase through the door that was already open. The ticket is written in the tracker the team already used, in its format. The open questions land in the thread where that conversation already happened. The Pull Request shows up in GitHub like any other and is reviewed like any other. The QA environment is a URL you open in the browser.

Nobody changed tools. What changed is how much manual work each person does inside them.

That detail is what decides adoption: **the team does not feel it is using an AI. It feels the same work has fewer steps.** There was no training, no migration, no period of getting used to the new system. From day one people worked differently without having learned anything.

Once you know where the bottleneck is, the work is not to replace that stage. It is to automate its points of friction **without taking it out of where it lives**.

The numbers go in the last article, along with the finding I did not expect.

---

*Fourth article in a series of five.*

*Comes from chapter 3: [An agent that runs without asking for permissions: how to make that safe](https://saul.botsmith.ai/en/blog/correr-sin-permisos).*
