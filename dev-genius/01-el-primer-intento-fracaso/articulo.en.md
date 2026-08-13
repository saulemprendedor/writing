---
title: "My first attempt at AI agents failed. The model was not the problem"
slug: el-primer-intento-fracaso
series: dev-genius
episode: 1
date: 2026-08-09
status: published
lang: en
summary: "A pilot built on agent orchestrators that helped and depreciated on its own. Why frozen knowledge was the real problem, and what I did after walking away from it."
banner: banner.jpg
---

# My first attempt at AI agents failed. The model was not the problem

A year ago I started a pilot, backed by the company, to build autonomous AI tooling around development work.

A year later, two developers on the team delivered twice the points they had committed to in a sprint — and the jump did not come from their seniority.

Between those two things there was a complete failure. I am starting there, because it is the part nobody tells.

## The pilot that depreciated on its own

I used what everyone used back then: agent orchestrators, roles, chained tools. Each agent with its prompt, its responsibility and its place in the chain.

It helped. And it depreciated on its own.

The problem was not the model or the framework — both did what they promised. It was that the knowledge I gave them was **frozen**. Each agent knew what I had written in its prompt the day I wrote it, and nothing else.

And most of what it takes to touch a real system is not written down anywhere. It lives in people's heads: why that table has an odd column, what breaks if you touch that service, what was decided two years ago and why nobody reversed it. That knowledge sits mostly with the senior engineers, and it does not transfer by writing a longer prompt.

The system aged while the product moved on. Every week it knew a little less about the code it was working on.

I dropped it.

## A month without building automation

I took a month to reset. I did not stop working: I kept shipping my tickets as always, with Cursor and Claude Code, the everyday tools. What I stopped was building — I did not write another line of automation that month.

I spent it reading and refocusing. It was the stretch when Anthropic was publishing almost every week, and I used it to understand what was actually changing underneath the noise.

The question I came back with was a different one. Not *how do I make a smarter agent*, but **how do I stop losing the knowledge**.

## Documentation that does not age

I found a way to document the history of the business decisions. Not the documentation nobody updates and that lies within three months — but the record of *why* things are the way they are: what was decided, against which alternatives, and what constraint drove it.

And I added the piece that changes everything: **when each implementation finishes, that documentation is updated with the outcome.**

It is a small detail and it is the whole difference. Knowledge stops being a snapshot and becomes a living record. Context stops being my assumption about what the agent needs to know, and becomes something the work itself keeps current.

## The experiment

I tried it on myself. On my machine, on my own tickets for the day, without telling anyone.

The results were out of proportion: the time difference between a small ticket and a large one came to be measured in minutes, not hours or days. Not because I wrote code faster — because I stopped spending the time rebuilding the context every time.

But it still lived on my laptop.

Which is where almost everything we developers build for ourselves lives: the tool that makes you twice as productive and that nobody else uses, because it never left your scripts folder.

Getting it out of there was the next problem. And it turned out to be a design problem, not a code problem.

---

*First article in a series of five on how I built an agent system that ships software to production.*

*Continues in chapter 2: [Por qué una feature debería vivir en un solo hilo](https://saul.botsmith.ai/en/blog/un-solo-hilo) — in Spanish for now.*
