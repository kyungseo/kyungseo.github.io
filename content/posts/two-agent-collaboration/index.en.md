---
title: "What I Noticed Too Late While Making Two Agents Collaborate"
slug: two-agent-collaboration
format: essay
tags: ["agents", "collaboration", "review"]
series: []
summary: "What I learned while running two agents as Driver and Reviewer — widening the Reviewer's role from pointing out problems to falsifying independently, then solving collaboratively."
toc: false
date: 2026-08-05
translated_from: ko
original_date: 2026-07-27
original_platform: "a Korean-language Facebook group"
og_image: round9-masked.png
draft: false
---

A retrospective, I suppose? This one came out a bit long.

For a while now I've been running two agents together — Codex and Claude Code — with one as the Author/Driver and the other as the Reviewer. The Driver plans and writes; the Reviewer attacks the result independently.

Compared to working with a single agent this costs more time and money, but the effect has been clear. The pair caught omissions and self-contradictions far better than one agent alone, and it kept questioning premises the author had come to take for granted.

My standing instruction to the Reviewer went like this:

> Don't just check the content and implementation for consistency. Be a cold-blooded Red-team that doubts the direction itself.

Then today, during a fairly wide-ranging cleanup, the review rounds simply would not end. I'd fix something, a new defect would surface, I'd fix that, and another problem would appear — over and over.

At some point the Reviewer's posture started to feel odd. It often seemed to be standing right next to the cause — maybe right next to the answer — yet it would only explain, quite logically, what was wrong and why, and then stop.

That's when a very basic question finally surfaced:

> Aren't the Driver, the Reviewer, and the Owner in the same boat, bound to make the same work succeed?

This isn't an exercise in training the other agent to discover answers on its own. Once a problem is found, sharing a possible solution quickly and solving it together matters just as much as pointing it out precisely.

So I added one more requirement for the Reviewer:

> If you can see a solution, don't stop at the finding — propose a recommended direction, the minimal scope of change, and how to verify it.

From the next round on, the character of the results was clearly different. Not every problem disappeared at once, but at least the Driver no longer had to restart from abstract design every time. With causes and fix directions arriving together, disposition got much faster and the discussion became more concrete.

Looking back, the two roles are disadvantaged in different ways, and strong in different ways.

The Driver works while holding a wide load: requirements, prior decisions, change history, implementation constraints. It knows the most about the actual context — which also means high cognitive load, and it's easy to get trapped inside premises of its own making.

The Reviewer knows relatively less of the full context, but it can look at a bounded target with fresh, concentrated eyes. That makes it good at finding contradictions and counterexamples — and sometimes it can see the shape of a solution more clearly than the Driver can.

The problem was that I had defined the Red-team role too narrowly as "the one who criticizes."

Agents optimize hard for the role and output contract you give them. You shouldn't expect them to fill in, on their own, the collaborative attitude a human colleague would naturally add. Demand only findings, and they'll focus on findings; put solution proposals out of scope, and they may stop right there even when they know the answer.

In the end, what needed improving wasn't the agent. It was the prompt — more precisely, the contract of the collaboration Skill.

Going forward I intend to give the Reviewer two responsibilities together. (Not acRelay, which I'm currently building — there's a private, manual skill I've used for a long time without publishing. I'll improve that one first, and if the results are good, fold it into acRelay.)

1. Falsify independently, without inheriting the author's premises.
2. Once a problem is confirmed, present the cause, a recommended solution, the minimal scope of change, and the verification method.

There is a balance to keep, though.

Proposing solutions must not turn the Reviewer into the Driver's co-author. If it starts building fixes from the outset, it tilts toward defending the existing direction or patching locally — and the question "is this direction itself wrong?" gets weaker.

The best coordination I can think of is to split the review into two stages:

> First falsify independently; then solve collaboratively.

In the first stage, attack the direction, the premises, hidden costs, rollback, and omissions — coldly. Look first at how the work could actually be wrong, rather than accommodating the Driver's intent.

In the second stage, for each confirmed problem, provide:

- what is wrong
- what the root cause is
- what direction you most recommend
- how far, at minimum, the fix needs to reach
- which fixtures verify the normal path and the failure path
- what requires a scope expansion or an Owner decision

Even when there are several options, present one preferred recommendation whenever possible. That's what keeps the Driver from re-running the same abstract design loop. The final disposition still belongs to the Driver — `accept`, `revise`, `defend`, or `needs-user` — and choices that change scope or authority go up to the Owner.

And when the same class of defect repeats for two rounds or more, the Reviewer should signal that it's time to re-examine the design axis itself rather than keep refining locally. A growing round count doesn't always mean the review is going deep. Sometimes it means we're polishing the wrong abstraction ever more precisely.

Perhaps I've been running two or three times more review rounds than I needed to. As the Owner, I also had to make an unnecessary number of intermediate judgment calls along the way.

A bit late — but better to have learned it now.

The Red-team's critical eye and cooperative solution-sharing were never opposing attitudes. They're closer to two responsibilities that need to be properly separated and performed in order.

> Find coldly; once found, propose the fastest path to resolution together, as the same team.

The collaboration Skill I build next will encode this principle explicitly. Keep the Red-team's sharpness — but the ultimate measure of success is not the number of findings. It's converging the work to a correct state, safely and quickly.

'Coordination principles, summarized'

The final balance I'd recommend:

- The Reviewer stays independent during the judgment stage.
- After judgment, it always presents an actionable recommended solution.
- Solutions are concretized: one preferred option, minimal fix scope, verification fixtures.
- The Driver keeps the disposition and the responsibility for actual changes.
- Owner decisions and scope expansions are marked separately.
- When the same defect repeats, stop the local fixes and re-question the design axis.
- Review performance is judged by time to safe convergence and recurrence — not by blocker count.

I think this is the most realistic balance between "a Reviewer grown too kind, losing its edge" and "one that knows the answer yet only repeats criticism."

Nothing about this is easy.

![Closing summary of a Claude Code session after nine review rounds — per-round blocking counts converging from 7 to 0, with a note that the turning point was the request to share solutions, not just findings.](round9-masked.png)
