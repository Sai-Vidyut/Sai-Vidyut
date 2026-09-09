<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sai-Vidyut/Sai-Vidyut/main/assets/hero-dark.svg">
  <img alt="Sai Vidyut C — The model interprets. The code decides." src="https://raw.githubusercontent.com/Sai-Vidyut/Sai-Vidyut/main/assets/hero-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://github.com/Sai-Vidyut/SatQuery-AI">SatQuery AI</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Sai-Vidyut/RazorFlow">RazorFlow</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Sai-Vidyut/Project-DocNA">DocNA</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Sai-Vidyut/project-blueprint">BluePrint</a>
</p>

I build AI products where the model is one component, not the architecture — satellite imagery you can interrogate, a commerce agent bound by merchant policy, a document pipeline that edits Word files without regenerating them.

The interesting part is never the prompt. It's the boundary I put around it.

<br>

### `01` &nbsp;The pattern

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sai-Vidyut/Sai-Vidyut/main/assets/pattern-dark.svg">
  <img alt="One pattern, three products. RazorFlow: buyer intent in plain language, Gemini extracts a structured intent, the contract is category, budget, exclusions and mode, then a catalog engine ranks and policy caps the offer. DocNA: questions and blanks in a .docx, AI writes the answer text only, the contract is typed PlacementOp values, then an OOXML adapter edits a copy rather than the original. BluePrint: a one-line product idea, the model returns a structured plan, the contract is a Zod schema, then a Mermaid diagram is built from the plan data." src="https://raw.githubusercontent.com/Sai-Vidyut/Sai-Vidyut/main/assets/pattern-light.svg" width="100%">
</picture>

<br>

### `02` &nbsp;Selected work

<table>
<tr><td>

#### SatQuery AI &nbsp;<sup>[repo](https://github.com/Sai-Vidyut/SatQuery-AI) · [live](https://sat-query-ai-self.vercel.app)</sup>

Ask questions about satellite imagery in plain language and get answers you can inspect on the map.

**Why it exists** — Imagery tools hand analysts a summary and ask them to trust it. Before you act on "construction started here," you need to see which pixels said so.

**Key idea** — Every run emits an execution trace plus map-linked evidence regions with per-region confidence. Four analysis paths share that one evidence contract: catalog change detection over an area and date range, single-image VQA on an uploaded GeoTIFF, bi-temporal before/after comparison, and joint optical + SAR. Google Earth Engine backs it when credentialed; deterministic fixtures run the entire workstation offline, clearly labeled as such.

**Stack** — FastAPI · Pydantic · Google Earth Engine · GeoChat-7B on a GPU service · Next.js 15 · MapLibre GL

<sub>Three-person team at SRMIST. I led backend and AI systems.</sub>

</td></tr>
</table>

<table>
<tr><td>

#### RazorFlow &nbsp;<sup>[repo](https://github.com/Sai-Vidyut/RazorFlow)</sup>

A merchant commerce agent that turns buyer intent into a policy-governed sale. Not a chatbot.

**Why it exists** — A model that can name products can also invent prices, undercut margin, and sell past a merchant's order cap. No merchant can ship that.

**Key idea** — Gemini only produces a validated `StructuredIntent`: category, budget in paise, exclusions, sort, result mode. It never receives the catalog and never emits a SKU. Deterministic code owns everything downstream — exact product resolution, budget and exclusion filters, ranking — and a policy engine applies the discount ceiling, margin floor, and order cap to the final offer. Remove the API key and a deterministic parser drives the identical pipeline.

**Stack** — Next.js 16 · TypeScript · PostgreSQL + Prisma · Razorpay · Vitest · Playwright

<sub>Built for the Razorpay Buildathon, AI Growth &amp; Agentic Commerce track. Runs locally.</sub>

</td></tr>
</table>

<table>
<tr><td>

#### DocNA &nbsp;<sup>[repo](https://github.com/Sai-Vidyut/Project-DocNA)</sup>

Finds the questions and blanks in a Word document, answers them, and writes back surgically.

**Why it exists** — The obvious approach is to regenerate the document, which destroys the formatting, tables, and headers that made it a real document.

**Key idea** — Four boundaries that never blur: AI produces answer text, placement produces typed `PlacementOp` values, a DOCX adapter performs OOXML mutation, and the uploaded original is never touched. Because placement is a stored plan rather than a model call, human edits re-apply from the immutable original instead of re-running generation. A provider fallback chain keeps answering when one provider is down.

**Stack** — Python · FastAPI · OOXML · React + Vite

<sub>311 tests passing. 18 of 18 real-AI evaluation fixtures complete.</sub>

</td></tr>
</table>

<table>
<tr><td>

#### BluePrint &nbsp;<sup>[repo](https://github.com/Sai-Vidyut/project-blueprint) · [live](https://project-blueprint-eight.vercel.app)</sup>

Describe a software idea, get a developer-grade implementation plan — architecture, schema, endpoints, roadmap.

**Why it exists** — Planning is the slowest part of starting a build and the part least often written down.

**Key idea** — One Zod schema is the source of truth, and the `Blueprint` TypeScript type is inferred from it rather than hand-declared, so the runtime contract and the compile-time contract can't drift. The architecture diagram is Mermaid generated deterministically from the structured architecture data — the model is never asked for diagram syntax, so it can never return a diagram that fails to render.

**Stack** — Next.js 16 · React 19 · Zod · Gemini · Mermaid

</td></tr>
</table>

<br>

### `03` &nbsp;Currently building

**SatQuery AI** — Evidence-scoped conversation: instead of chatting about the imagery in general, you talk to a specific evidence region and the backend keeps the exchange bound to it.

**RazorFlow** — Separating what a buyer may see from what staff may change. Buyers observe policy *effects* on the desk; reading or mutating the guardrails requires a verified staff account.

<br>

### `04` &nbsp;Lab

Smaller things I build to answer a question I actually have.

**[Radio Auto](https://github.com/Sai-Vidyut/radio-auto)** — Sit in the back of a Mumbai auto-rickshaw. Same driver, same cabin, one canonical hero plate that never swaps. Time and weather are independent axes, so heavy rain works at any hour, and the radio and the weather run on separate audio elements rather than one mixed track.

**GeoChat on Colab** — A self-contained notebook that supervises a GPU inference service for the 7B vision model, hardened against OOM during model load and against stale exit-file races when the service restarts. Lives inside [SatQuery AI](https://github.com/Sai-Vidyut/SatQuery-AI).

**[Instagram Dashboard](https://github.com/Sai-Vidyut/Instagram-Dashboard)** — My first pass at keeping an integration boundary honest: routes, services, and repositories are separated so the mock Composio layer can be replaced with live SDK calls without the API contract moving. [Live](https://instagram-dashboard-pearl.vercel.app).

<br>

### `05` &nbsp;Stack

```
product surface   TypeScript · Next.js App Router · React · Tailwind
systems & ai      Python · FastAPI · Pydantic · Gemini · provider fallback chains
data              PostgreSQL · Prisma · SQLAlchemy
geospatial        MapLibre GL · Google Earth Engine · GeoTIFF, optical + SAR
correctness       Zod · Vitest · Playwright · pytest
```

<br>

### `06` &nbsp;Build log

```
2026-09-08   satquery-ai   evidence-scoped GeoChat conversation, region evidence
2026-09-06   satquery-ai   seasonality-aware Earth Engine change detection
2026-08-30   radio-auto    Mumbai playlist, glass player, weather audio
2026-08-29   razorflow     post-payment desk state, staff-only policy auth
2026-08-28   razorflow     hybrid discovery: Gemini intent, deterministic catalog
2026-08-21   docna         document workspace pipeline and review UI
2026-08-18   blueprint     in-blueprint AI assistant with chat and change flow
```

<br>

### `07` &nbsp;Contact

[saividyut4@gmail.com](mailto:saividyut4@gmail.com) &nbsp;·&nbsp; [github.com/Sai-Vidyut](https://github.com/Sai-Vidyut)
