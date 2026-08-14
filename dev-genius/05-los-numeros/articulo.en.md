---
title: "The numbers, and the finding I didn't expect"
slug: los-numeros
series: dev-genius
episode: 5
date: 2026-08-14
status: published
lang: en
summary: "Two measured sprints, and the figure that surprised me: the gain was even across profiles with different seniority."
banner: banner.en.jpg
---

# The numbers, and the finding I didn't expect

Four articles of architecture decisions are worth nothing without the part you can argue with. Here are the numbers, with the window they were measured in, so they can be questioned.

## Two sprints in production, three developers using it

- **50 tickets** taken from idea to merge
- **62 Pull Requests** with tests and a browsable QA environment
- **93%** reached review without needing rework
- **2.5 tickets per working day**, sustained across both sprints
- Each ticket touches **more than one repository** on average: backend and frontend in the same unit of work

## Why the goal was 3X

The goal was never "use AI". It was concrete and measurable: **triple the team's delivery capacity without hiring anyone else.**

Putting a number on the goal changed every design decision. An agent that writes elegant code but needs someone watching it step by step triples nothing: it moves the work somewhere else. That's why the system doesn't end at *it generated the code*. It ends with the PR open, the checks running, the card moved and the thread telling what happened.

**The first sprint with the system running closed with two developers delivering twice the points they had committed to**, measured against their own history of previous sprints. Not against an industry average, and not against an optimistic estimate: against what those same two people had been delivering.

## The finding

But the figure that interests me most from that sprint isn't the multiple. It's that **the gain was even across the two of them, and they're at different seniority levels.**

That's the opposite of what usually happens with productivity tools, which amplify whoever was already fast and leave everyone else where they were. Here what goes up isn't the individual: **it's the process.**

The agent always takes the same steps — investigate before writing, ask what isn't clear, leave the spec in writing, run the checks, open the PR — and those steps are exactly the ones a developer with fewer years is still building. The tool doesn't make them more expert. **It lends them the process of someone who is.**

One sprint and two people aren't a statistical sample. They're a signal. But it's exactly the signal I was looking for, because it means this scales with the team and not with the team's stars.

## What I actually learned

I started out believing the hard problem was getting the model to write good code.

It isn't. That part is solved.

Once generating an implementation becomes cheap, what gets expensive is everything that comes after: reviewing, testing, resolving conflicts when five branches touch the same file, keeping the board current, not losing track of what is waiting on whom. Today most of the system isn't *the AI part*: it's the background processes that look after the queue.

But the result that surprises me most isn't the speed. It's that today a developer on a machine that barely opens Slack and a browser ships software with the quality and the context that used to take years inside the company. Not because the model makes them more expert: because the knowledge that used to live in the senior engineers' heads is now in the system, alive, updating itself with every implementation.

It's the exact opposite of where I started. That first pilot failed because the knowledge was frozen and kept living in the people. Everything that came after was chasing that one thing.

Building with AI looks far less like training a model and far more like designing a production line. The model is one station. The value is in the rest of the line.

That's DEV Genius: not a tool, but the way that line is built around the model. It's what I work on every day.

If you're trying to move AI from the proof of concept to your team's real work, write to me. I'd like to compare notes — it's a problem where almost all of us are learning at the same time.

---

*Last article in a series of five.*

*Comes from chapter 4: [The bottleneck moved twice](https://saul.botsmith.ai/en/blog/el-cuello-de-botella).*
