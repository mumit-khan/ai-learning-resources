# Agentic AI / ML / GenAI — Curated Learning Resources

<!--
FORMAT (parsed by md_to_html.py):
  ## Category Name          -> starts a new category section
  - **Title** — Author — *Level* — Area1, Area2[, Area3] [— **NEW**]
      Description paragraph (single line).
      https://url (optional; omit the line entirely if there is none)
  > Freeform note attached to the current category (optional, repeatable)

  Level values: Foundational | Intermediate | Advanced — combine with "/", e.g. Intermediate/Advanced
  Area values (free text, matched by keyword): GenAI, Core ML, Agentic AI, MLOps, Evaluation/Governance, AI-native software development
  Append " — **NEW**" to a header line to flag it as newly added.
-->

Curated August 2026, reviewed and expanded across several follow-up passes. Every entry was checked for current activity and credibility before inclusion. This file is the source of truth — `md_to_html.py` regenerates the interactive HTML artifact from it.

---

## Twitter / X

- **Andrej Karpathy** — @karpathy — Anthropic (pretraining), ex-OpenAI founding member, ex-Tesla AI director — *Intermediate/Advanced* — Core ML, GenAI
  First-principles explainers on LLM training/inference internals and how LLMs are reshaping software engineering.
  https://twitter.com/karpathy

- **Simon Willison** — @simonw — creator of the `llm` CLI/library, co-creator of Django — *Intermediate* — GenAI, Agentic AI
  Hands-on, code-level posts on prompting, tool use, and new model capabilities the day they ship. High signal, zero hype.
  https://twitter.com/simonw

- **Harrison Chase** — @hwchase17 — co-founder/CEO, LangChain — *Intermediate* — Agentic AI
  Direct source on LangGraph roadmap, agent middleware design, and real feedback from building agent infra at production scale.
  https://twitter.com/hwchase17

- **Jerry Liu** — @jerryjliu0 — co-founder/CEO, LlamaIndex — *Intermediate* — Agentic AI, GenAI
  Practical, architecture-level posts on RAG pipeline design and agentic layers over retrieval, from someone shipping the tooling.
  https://twitter.com/jerryjliu0

- **Chip Huyen** — @chipro — author, "AI Engineering" & "Designing ML Systems" — *Advanced* — MLOps, GenAI
  Productionizing foundation-model applications, system design tradeoffs, and MLOps fundamentals from one of the field's clearest writers.
  https://twitter.com/chipro

- **Hamel Husain** — @HamelHusain — ML engineer, co-teaches AI Evals for Engineers & PMs — *Advanced* — Evaluation/Governance, GenAI
  The go-to voice for rigorous, non-hand-wavy LLM and agent evaluation methodology.
  https://twitter.com/HamelHusain

- **Arvind Narayanan** — @random_walker — Princeton CS professor, director of Princeton CITP — *Advanced* — Evaluation/Governance
  Evidence-based critiques of inflated AI claims and AI policy framing — an essential counterweight for engineers shaping technical strategy.
  https://twitter.com/random_walker

- **Sebastian Raschka** — @rasbt — LLM research engineer, author of "Build a Large Language Model From Scratch" — *Advanced* — GenAI, Core ML
  Architecture deep-dives and open-model analysis; also runs the Ahead of AI newsletter (see Newsletters).
  https://twitter.com/rasbt

- **Dex Horthy** — @dexhorthy — Founder/CEO, HumanLayer; creator of "12-Factor Agents" — *Advanced* — Agentic AI, MLOps
  Practitioner-level content on agent reliability and context engineering (see 12-Factor Agents in Blogs).
  https://twitter.com/dexhorthy

- **Aakanksha Chowdhery** — @achowdhery — Lead author on PaLM, Gemini pretraining contributor, now at Reflection AI; Stanford adjunct — *Advanced* — GenAI, Core ML, Agentic AI
  Top-tier technical content on pretraining, scaling, and RL for autonomous coding agents. One of the most credentialed voices on this list.
  https://twitter.com/achowdhery

- **Paul Iusztin** — @pauliusztin_ — Senior AI engineer, co-author of "LLM Engineer's Handbook" — *Intermediate* — GenAI, MLOps
  Practical production-LLM-systems content. Note: modest following on X specifically — his Substack/Decoding ML carries more volume.
  https://twitter.com/pauliusztin_

- **AI Engineer** — @aiDotEngineer — official account, AI Engineer World's Fair/Summit conference series — *Intermediate* — GenAI, Agentic AI, MLOps
  Not an individual voice — a strong discovery channel for talks and community signal (see also YouTube).
  https://twitter.com/aiDotEngineer

- **Dax** — @thdxr — creator of opencode and SST — *Advanced* — Agentic AI
  Deep, hands-on agentic-tooling content — building a leading open-source AI coding agent in the open.
  https://twitter.com/thdxr

- **Salvatore Sanfilippo** — @antirez — creator of Redis — *Advanced* — Agentic AI, Evaluation/Governance
  A rare, credible skeptical/systems-engineering voice on agentic coding — argues for staying in the loop rather than over-delegating to agents.
  https://twitter.com/antirez

- **Ethan Mollick** — @emollick — Wharton professor, author of "Co-Intelligence" — *Intermediate* — GenAI, Evaluation/Governance — **NEW**
  Gets early access to frontier models and publishes hands-on, same-prompt comparisons (GPT, Claude, Gemini, open-weights) on real coding/research tasks — useful as an early capability radar, though experiential rather than a formal benchmark. Revisited and added specifically for this.
  https://twitter.com/emollick

- **Matt Pocock** — @mattpocockuk — TypeScript educator, creator of Total TypeScript and AI Hero — *Advanced* — AI-native software development, Agentic AI — **NEW**
  Publishes and maintains "Skills for Real Engineers" (mattpocock/skills, see AI-native Software Development) — Claude Code/Cursor/Codex-portable agent Skills enforcing TDD, structured debugging, and architecture review, explicitly positioned as the opposite of one-shot "vibe coding." Revisited and added specifically for this.
  https://twitter.com/mattpocockuk

> Reviewed but excluded: @summarizedml could not be verified as active or identifiable — excluded pending independent verification. @emollick and @mattpocockuk were previously excluded here as too business-focused / too narrowly TypeScript-focused respectively — revisited this round for the specific angles above (model comparisons; agent-skills tooling) and now included.

---

## Podcasts

- **Latent Space: The AI Engineer Podcast** — Shawn "swyx" Wang & Alessio Fanelli — *Intermediate/Advanced* — GenAI, Agentic AI
  Practitioner-focused interviews with engineers/researchers at OpenAI, Anthropic, Databricks and more — deep dives on foundation models, agents, inference, and evals.
  https://www.latent.space/podcast

- **The TWIML AI Podcast** — Sam Charrington — *Intermediate/Advanced* — Core ML, Agentic AI, MLOps
  Long-running (since 2016), broad researcher/practitioner interviews spanning ML fundamentals, MLOps, and agentic systems.
  https://twimlai.com/podcast/twimlai

- **MLOps Community Podcast** — Demetrios Brinkmann — *Intermediate* — MLOps, Agentic AI
  Backed by the 100k+ member MLOps Community — concrete, production-grade deployment, monitoring, and agent-ops content, no hype.
  https://podcast.mlops.community/

- **Machine Learning Street Talk** — Tim Scarfe & Keith Duggar — *Advanced* — Core ML, Evaluation/Governance
  The most technically dense show on this list — research-level discussions of ML theory, interpretability, and AI safety with top researchers.
  https://www.youtube.com/c/MachineLearningStreetTalk

- **The Cognitive Revolution** — Nathan Labenz & Erik Torenberg — *Intermediate/Advanced* — Agentic AI, Evaluation/Governance, GenAI
  Weekly deep dives with builders and safety/policy analysts; strong on agentic-AI capability analysis paired with safety and governance.
  https://www.cognitiverevolution.ai/

- **80,000 Hours Podcast** — Rob Wiblin, Luisa Rodriguez, Zershaaneh Qureshi — *Advanced* — Evaluation/Governance
  The most substantive long-form podcast on AI governance and safety — rigorous, technical interviews with people doing the alignment/policy work.
  https://80000hours.org/podcast/

- **AI Engineering Podcast** — Tobias Macey — *Intermediate* — GenAI, MLOps, Agentic AI
  Focused on architecting production AI/LLM applications — RAG pipelines, agent tooling, and MCP — practitioner-level, low on hype.
  https://www.aiengineeringpodcast.com/

---

## YouTube Channels

- **Andrej Karpathy — "Zero to Hero" / Let's Build GPT** — Andrej Karpathy — *Intermediate* — GenAI, Core ML
  The single best from-scratch, code-first path from backprop to a working GPT. Canonical resource, still the top recommendation in 2026.
  https://www.youtube.com/@AndrejKarpathy

- **Umar Jamil** — @umarjamilai — *Intermediate/Advanced* — GenAI, Core ML
  Rigorous "build it from scratch" walkthroughs — coding a Transformer from scratch in PyTorch, deriving attention math, paper breakdowns.
  https://www.youtube.com/@umarjamilai

- **LangChain (official channel)** — LangChain team — *Intermediate* — Agentic AI
  Maintained by the framework's own engineers — graph-based agent state management, tool use, and RAG evaluation for the most widely deployed agent orchestration framework.
  https://www.youtube.com/@LangChain

- **Weights & Biases** — W&B team — *Advanced* — MLOps, Evaluation/Governance
  LLM evaluation, fine-tuning workflows, and production ML monitoring taught by practitioners who build the tooling itself.
  https://www.youtube.com/@WeightsBiases

- **Robert Miles AI Safety** — Robert Miles — *Intermediate* — Evaluation/Governance
  The clearest, most technically honest explainer of AI alignment/safety concepts. Upload cadence has slowed — treat as a well-preserved back catalog rather than an actively releasing channel.
  https://www.youtube.com/@RobertMilesAI

- **3Blue1Brown — Neural Networks / Deep Learning series** — Grant Sanderson — *Foundational* — Core ML, GenAI
  Unmatched visual/geometric intuition for backprop, gradient descent, and (in the "Attention in transformers" video) attention itself. The resource practitioners most often credit for making these concepts "click."
  https://www.3blue1brown.com/topics/neural-networks

- **StatQuest with Josh Starmer** — Josh Starmer, PhD — *Foundational* — Core ML
  Strips away notation-heavy jargon to build genuine statistical/ML intuition (gradient descent, regularization, trees, transformers), then layers the math back in. Not 101 — builds real understanding fast.
  https://www.youtube.com/c/joshstarmer

- **AI Engineer World's Fair / Summit — talks** — AI Engineer conference — *Intermediate/Advanced* — GenAI, Agentic AI, MLOps
  Recorded sessions from the largest AI engineering conference — production agent case studies and AI-engineering-stack deep dives directly from teams at Anthropic, OpenAI, LangChain, and others.
  https://www.youtube.com/@aiDotEngineer

---

## Courses

- **Agentic AI** — DeepLearning.AI — Andrew Ng — *Advanced* — Agentic AI
  Builds the four foundational agent patterns (Reflection, Tool Use, Planning, Multi-Agent Collaboration) from scratch in raw Python, vendor-neutral.
  https://www.deeplearning.ai/courses/agentic-ai

- **AI Agents in LangGraph** — DeepLearning.AI — Harrison Chase & Rotem Weiss — *Intermediate* — Agentic AI
  Building an agent from scratch, then rebuilding with LangGraph — state management, agentic search, debugging agent graphs. Shorter primer; see LangChain Academy for a deeper dive.
  https://www.deeplearning.ai/courses/ai-agents-in-langgraph

- **MCP: Build Rich-Context AI Apps with Anthropic** — DeepLearning.AI — built with Anthropic — *Intermediate* — Agentic AI
  How the Model Context Protocol works under the hood, building your own MCP server, connecting it to Claude-powered apps.
  https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic

- **Building and Evaluating Advanced RAG** — DeepLearning.AI — Jerry Liu & Anupam Datta — *Advanced* — GenAI
  Sentence-window and auto-merging retrieval, experiment tracking, and the "RAG triad" for rigorous evaluation. Assumes a working RAG baseline.
  https://www.deeplearning.ai/courses/building-evaluating-advanced-rag

- **Fast & Efficient LLM Inference with vLLM** — DeepLearning.AI — built with Red Hat — *Advanced* — GenAI, MLOps
  Full optimize-deploy-benchmark workflow: quantization, PagedAttention/prefix caching/continuous batching, load-testing.
  https://www.deeplearning.ai/courses/fast-and-efficient-llm-inference-with-vllm

- **Red Teaming LLM Applications** — DeepLearning.AI — built with Giskard — *Advanced* — Evaluation/Governance
  Applies cybersecurity red-teaming methodology to LLM apps — prompt injection attacks, manual and automated vulnerability testing.
  https://www.deeplearning.ai/courses/red-teaming-llm-applications

- **Full Stack Deep Learning — LLM Bootcamp** — YouTube — Sergey Karayev, Josh Tobin, Charles Frye — *Advanced* — GenAI, MLOps
  Strong on fundamentals (prompting, LLMOps, project walkthroughs), but the flagship recorded lectures are the Spring 2023 cohort — predates agents, MCP, and reasoning-model-era practice. Treat as foundations, not current-state.
  https://www.youtube.com/playlist?list=PL1T8fO7ArWleyIqOy37OVXsP4hFXymdOZ

- **Stanford CS25: Transformers United (V6)** — YouTube / Stanford University — *Advanced* — Core ML, Agentic AI
  Graduate seminar series with rotating leading researchers (Hinton, Karpathy, original Transformer authors) on transformer internals and scaling.
  https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM

- **Practical Deep Learning for Coders** — fast.ai — Jeremy Howard & Sylvain Gugger — *Foundational* — Core ML, GenAI
  Code-first, top-down pedagogy — train a real model in lesson 1, learn theory after. No PhD-level math required. Still actively taught and referenced in 2026.
  https://course.fast.ai/

- **Hugging Face — LLM Course** — Hugging Face — *Foundational* — GenAI
  Free, continuously-updated 12-chapter course on the modern open-source LLM stack. Best practical bridge from theory to shipped code.
  https://huggingface.co/learn/llm-course/chapter1/1

- **Hugging Face Agents Course** — Hugging Face (free, certified) — *Intermediate* — Agentic AI
  Certified course covering agent frameworks (LangChain, LlamaIndex, smolagents) with a benchmark assessment.
  https://huggingface.co/learn/agents-course/unit0/introduction

- **LangChain Academy** — LangChain (free, self-paced) — *Intermediate/Advanced* — Agentic AI
  ~13 hours across three courses — the deeper-dive complement to the shorter DeepLearning.AI LangGraph course above.
  https://academy.langchain.com/

- **Made With ML** — Goku Mohandas / Anyscale (free course + repo) — *Foundational/Intermediate* — MLOps
  First-principles production ML system design, from prototype to a live monitored service — one of the gentlest genuinely non-101 on-ramps into MLOps/LLMOps.
  https://madewithml.com/

- **AI Evals for Engineers & PMs** — Hamel Husain & Shreya Shankar (Maven, paid cohort) — *Advanced* — Evaluation/Governance, Agentic AI, GenAI
  The most-cited practitioner course on building rigorous LLM/agent evaluation pipelines — error analysis, synthetic data, LLM-as-judge design.
  https://maven.com/parlance-labs/evals

- **AI Safety Fundamentals** — BlueDot Impact — *Foundational* — Evaluation/Governance
  The standard on-ramp used across the AI safety field — structured reading plus cohort-based discussion. Real technical/policy depth without requiring years of research background; ~75% completion rate.
  https://bluedot.org/courses/technical-ai-safety

---

## Blogs

- **Anthropic Engineering Blog** — Anthropic engineering team — *Foundational/Advanced* — GenAI, Agentic AI
  No-fluff writeups from the team building Claude. Flagship post "Building Effective Agents" is the field's most-cited primer on agent architecture patterns (start there); other posts go much deeper.
  https://www.anthropic.com/engineering

- **Lil'Log** — Lilian Weng — Anthropic, ex-OpenAI applied AI research lead — *Advanced* — GenAI, Core ML, Agentic AI
  Long-running, paper-quality deep dives on agents, RLHF, and reasoning. Widely regarded as one of the highest signal-to-noise ML blogs in existence.
  https://lilianweng.github.io/

- **Eugene Yan** — Eugene Yan — Anthropic (ex-Amazon, Alibaba) — *Intermediate/Advanced* — MLOps, GenAI, Evaluation/Governance
  Author of "Patterns for Building LLM-based Systems"; rigorous, practitioner-first writing on production ML/LLM patterns and evals.
  https://eugeneyan.com/writing/

- **Hamel's Blog** — Hamel Husain — *Intermediate/Advanced* — Evaluation/Governance, GenAI
  The reference source for rigorous LLM evaluation methodology — "Your AI Product Needs Evals" and the widely-cited LLM-as-Judge guide.
  https://hamel.dev/

- **Interconnects** — Nathan Lambert — *Advanced* — GenAI, Core ML
  The most technically serious ongoing commentary on post-training (RLHF, DPO, reasoning-model training) from someone who ships open models.
  https://www.interconnects.ai/

- **vLLM Blog** — vLLM project (Red Hat + community) — *Advanced* — GenAI, MLOps
  Ground-truth source on LLM inference optimization internals — quantization, KV-cache management, multi-LoRA serving.
  https://blog.vllm.ai/

- **METR Blog** — Model Evaluation and Threat Research — *Advanced* — Agentic AI, Evaluation/Governance
  The most rigorous public source on frontier-model autonomous-capability evaluation — primary safety-eval research.
  https://metr.org/blog

- **Simon Willison's Weblog** — Simon Willison — *Intermediate* — GenAI, Agentic AI
  His primary output (more valuable than his tweets) — detailed technical write-ups on LLM tool releases and biannual "state of LLMs" recaps.
  https://simonwillison.net/

- **The Illustrated Transformer (+ GPT-2/BERT)** — Jay Alammar — *Foundational* — GenAI, Core ML
  The single most-recommended conceptual explainer of transformer architecture; used in course materials at Stanford, MIT, Harvard, and CMU.
  https://jalammar.github.io/illustrated-transformer/

- **Guide to All 70+ Scikit-Learn Models and When to Use Them** — Wei Ming T. / ApX Machine Learning — *Foundational/Intermediate* — Core ML — **NEW**
  Overview of 75 scikit-learn ML models grouped by task (regression, classification, ensembles, clustering, dimensionality reduction, neural nets), each with a code snippet and, more usefully, an explicit "when to avoid" section; 23 are starred as the shortlist worth actually knowing. A selection lookup table, not a course.
  https://apxml.com/posts/scikit-learn-models-guide

- **12-Factor Agents** — Dex Horthy / HumanLayer — *Advanced* — Agentic AI, MLOps
  The best-known practitioner framework for building production-grade (not toy) LLM agents — reliability, context/control-flow, human-in-the-loop design.
  https://github.com/humanlayer/12-factor-agents

- **DSPy — Docs & Papers** — Stanford / Omar Khattab — *Advanced* — Agentic AI, GenAI
  "Programming, not prompting" LLMs — the most influential alternative paradigm to manual prompt-chaining, now taught in new MIT/CMU courses.
  https://dspy.ai/

- **Apollo Research Blog** — Apollo Research — *Advanced* — Evaluation/Governance
  Companion to METR — focused specifically on scheming/deceptive-alignment evals of frontier models; partnered with OpenAI on anti-scheming work in 2026.
  https://www.apolloresearch.ai/blog

---

## Books

- **AI Engineering: Building Applications with Foundation Models** — Chip Huyen — O'Reilly, 2025 — *Advanced* — GenAI, Evaluation/Governance
  End-to-end framework for foundation-model apps: evaluation, RAG, fine-tuning, inference optimization, guardrails. O'Reilly's most-read title since release.

- **Hands-On Large Language Models** — Jay Alammar & Maarten Grootendorst — O'Reilly, 2024 — *Intermediate* — GenAI
  ~300 custom visuals covering embeddings, RAG, fine-tuning, and multimodal LLMs. Hands-on, code-heavy, Python notebooks throughout.

- **LLM Engineer's Handbook** — Paul Iusztin & Maxime Labonne — Packt, 2024 — *Advanced* — GenAI, MLOps
  Full LLM system architecture — RAG, vector stores, fine-tuning, LLMOps integration. Hands-on, full reference project.

- **Prompt Engineering for LLMs** — John Berryman & Albert Ziegler — O'Reilly, 2024 — *Intermediate* — GenAI
  Written by two of the key architects of GitHub Copilot; prompt-crafting strategy, few-shot/chain-of-thought, RAG-as-prompting.

- **Understanding Deep Learning** — Simon J.D. Prince — MIT Press, 2023 — *Advanced* — Core ML
  Rigorously curated modern DL text covering transformers and diffusion models that older texts lack. Free legal ebook alongside the hardcover.

- **Deep Reinforcement Learning Hands-On (3rd Edition)** — Maxim Lapan — Packt, 2024 — *Advanced* — Core ML
  Adds RLHF, MuZero, and transformer-based RL on top of the established Q-learning/DQN/PPO core. Hands-on, code-heavy.

- **Building Applications with AI Agents** — Michael Albada — O'Reilly, 2025 — *Advanced* — Agentic AI
  Practical + research-grounded coverage of tool use, memory, orchestration across LangGraph, AutoGen, CrewAI. Author built large-scale multi-agent systems at Uber, ServiceNow, Microsoft.

- **Designing Multi-Agent Systems** — Victor Dibia — 2025 — *Advanced* — Agentic AI
  Framework-agnostic first-principles teaching by building an agent framework from scratch. Author is a Principal Research Software Engineer at Microsoft Research and core AutoGen maintainer.

- **Designing Machine Learning Systems** — Chip Huyen — O'Reilly, 2022 — *Intermediate* — MLOps, Core ML
  Data pipelines, feature engineering, deployment, monitoring, and iteration end to end, with real case studies.

- **Fairness and Machine Learning: Limitations and Opportunities** — Solon Barocas, Moritz Hardt, Arvind Narayanan — MIT Press, 2023 — *Advanced* — Evaluation/Governance
  Standard grad-level technical reference on algorithmic fairness — statistical/causal fairness measures plus legal/social context. Free online at fairmlbook.org.
  https://fairmlbook.org/

---

## Newsletters & Communities

- **Ahead of AI** — Sebastian Raschka (newsletter) — *Intermediate/Advanced* — GenAI, Core ML
  Deep technical dives into LLM architectures and fine-tuning, plus annual state-of-the-art roundups. 200,000+ subscribers.
  https://magazine.sebastianraschka.com/

- **Import AI** — Jack Clark (newsletter) — *Advanced* — Evaluation/Governance, GenAI
  Weekly roundup of AI research plus policy implications, written by Anthropic's co-founder and former OpenAI policy lead.
  https://jack-clark.net/

- **The Batch** — DeepLearning.AI / Andrew Ng (weekly newsletter) — *Foundational/Intermediate* — GenAI, Core ML, Agentic AI
  One of the most widely-read weekly AI newsletters — good for staying current at low time cost, and a natural companion to DeepLearning.AI's course catalog.
  https://www.deeplearning.ai/the-batch/

- **OpenAI Cookbook & Anthropic Cookbook** — GitHub repos — *Intermediate* — GenAI, Agentic AI
  Canonical, continuously-updated runnable code examples for RAG, agents, evals, and tool use — a practical complement to more conceptual content.
  https://github.com/openai/openai-cookbook

- **MLOps Community** — mlops.community (Slack + events) — *Intermediate/Advanced* — MLOps
  70,000+ member practitioner-run community discussing real production ML/LLM reliability and infra problems — free to join.
  https://mlops.community/

- **Stanford HAI — AI Index Report** — Stanford Human-Centered AI Institute (annual report) — *Advanced* — Evaluation/Governance
  The most rigorous, citation-grade annual dataset on AI capability, adoption, safety incidents, and global governance trends.
  https://hai.stanford.edu/ai-index

- **AI Alignment Forum / LessWrong** — Independent (LightCone Infrastructure) — *Advanced* — Evaluation/Governance
  The primary technical venue for AI safety and alignment research discourse — deep, rigorous debate on interpretability and risk.
  https://www.alignmentforum.org/

---

## GitHub Curated Lists & Repos

- **A Curated List of ML System Design Case Studies** — Engineer1999 · ★10.4k — *Intermediate* — MLOps, Core ML
  300+ real-world ML system design write-ups from 80+ companies (Netflix, Airbnb, DoorDash, etc.), organized by industry/use case. Mostly a static, high-quality snapshot rather than a frequently-refreshed list.
  https://github.com/Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies

- **Awesome Generative AI Guide** — aishwaryanr · ★28.3k — *Foundational/Intermediate/Advanced* — GenAI, Agentic AI, Evaluation/Governance
  The strongest all-around GenAI meta-resource found — organized into Use/Build/Understand "journeys" across 101/201/301 levels, with dedicated pages for RAG, agents, fine-tuning, evaluation, and safety. Actively maintained.
  https://github.com/aishwaryanr/awesome-generative-ai-guide

- **Awesome-LLM** — Hannibal046 · ★26.9k — *Intermediate/Advanced* — GenAI
  The standard academic-leaning curated list of LLM papers, training/deployment frameworks, courses, and tutorials. Actively maintained.
  https://github.com/Hannibal046/Awesome-LLM

- **Awesome LLM Apps** — Shubhamsaboo · ★128.7k — *Intermediate* — Agentic AI, GenAI
  100+ hands-on, runnable agent/RAG/multi-agent/MCP examples treated as real production patterns rather than toy demos. Very actively maintained.
  https://github.com/Shubhamsaboo/awesome-llm-apps

- **Awesome Production Machine Learning** — EthicalML · ★20.6k — *Intermediate/Advanced* — MLOps
  Curated open-source tooling map across the full production ML lifecycle — deployment, monitoring, versioning, explainability, responsible AI. Actively maintained.
  https://github.com/EthicalML/awesome-production-machine-learning

- **Awesome MLOps** — visenger · ★13.9k — *Advanced* — MLOps
  Literature/reference-heavy complement to the above — books, papers, talks, and case studies on MLOps practice, maintained by an MLOps practitioner/author.
  https://github.com/visenger/awesome-mlops

- **Awesome-LLM-Eval** — onejune2018 · ★649 — *Advanced* — Evaluation/Governance
  Tools, datasets/benchmarks, demos, leaderboards, and papers specifically for LLM evaluation. One of the more actively iterated eval-specific lists.
  https://github.com/onejune2018/Awesome-LLM-Eval

- **Awesome-LLM-Safety** — ydyjya · ★1.9k — *Advanced* — Evaluation/Governance
  Academic-style taxonomy of LLM safety — jailbreaks/attacks, privacy, truthfulness, defenses — with paper tables. Well-organized but slower-moving; verify freshness of any specific paper.
  https://github.com/ydyjya/Awesome-LLM-Safety

> Reviewed but excluded: e2b-dev/awesome-ai-agents (27.8k stars) — despite the high star count, its last release was 2023 and it has 533 open, unmerged pull requests. Also excluded a cluster of near-identical "awesome-ai-agents-2026"-style repos across unrelated accounts sharing the same templated description — a textbook SEO/content-farm pattern rather than genuine curation.

---

## AI-native Software Development

- **Agentic Coding Recommendations** — Armin Ronacher (lucumr.pocoo.org) — *Advanced* — AI-native software development — **NEW**
  Creator of Flask; unusually candid field notes from shifting his entire workflow to Claude Code — agent loops, context/back-pressure management, what didn't work. High signal, no hype.
  https://lucumr.pocoo.org/tags/ai/

- **ghuntley.com — agent-loop engineering** — Geoffrey Huntley — *Advanced* — AI-native software development, Agentic AI — **NEW**
  Creator of the "Ralph Wiggum" brute-force autonomous-agent-loop technique, plus a free "build your own coding agent" workshop. Deep practitioner content on agent internals and spec-through-conversation workflows.
  https://ghuntley.com/

- **Beyond Vibe Coding** — Addy Osmani (O'Reilly, 2025) — *Foundational/Intermediate* — AI-native software development — **NEW**
  Former Google Chrome engineering lead. Argues for being "editor-in-chief" of AI-generated code rather than a passenger — a credible, non-hyped framing of the vibe-coding-vs-engineering-discipline tension. Free companion updates on his blog.
  https://addyosmani.com/blog/ai-assisted-engineering/

- **Skills for Real Engineers (mattpocock/skills)** — Matt Pocock — *Intermediate/Advanced* — AI-native software development, Agentic AI — **NEW**
  Portable Claude Code/Cursor/Codex Skills enforcing TDD, structured debugging, domain modeling, and architecture review — one of the most rapidly-adopted third-party Claude Code skills packs, explicitly positioned against one-shot "vibe coding." See also Matt Pocock on Twitter/X.
  https://github.com/mattpocock/skills

- **spec-kit** — GitHub (spec-driven development toolkit) — *Intermediate* — AI-native software development, Agentic AI — **NEW**
  GitHub's own open-source reference implementation of spec-driven development — spec as source of truth, agent generates code from structured phases. Works across Copilot, Claude Code, Gemini CLI, and 30+ agents. Institutionally backed and actively maintained.
  https://github.com/github/spec-kit

- **awesome-claude-code** — hesreallyhim (GitHub curated list) — *Foundational/Intermediate* — AI-native software development — **NEW**
  Broad, actively curated collection of Claude Code skills, agents, status lines, and plugins — a good single entry point to the ecosystem without wading through SEO blogspam.
  https://github.com/hesreallyhim/awesome-claude-code

- **Effective Context Engineering for AI Agents** — Anthropic Engineering — *Intermediate/Advanced* — AI-native software development, Agentic AI — **NEW**
  Primary-source engineering writing on context-window management, when to use CLAUDE.md-style instructions vs. just-in-time retrieval, and skill design — the definitive reference on this specific topic (complements the general Anthropic Engineering Blog entry above).
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

- **IndyDevDan** — YouTube + agenticengineer.com — *Intermediate/Advanced* — AI-native software development — **NEW**
  "Tactical Agentic Coding" / "Principled AI Coding" — teaches "Model, Prompt, Context" as language-agnostic first principles for agentic engineering rather than tool-of-the-week hype.
  https://www.youtube.com/@indydevdan

- **The Pragmatic Engineer — AI coverage** — Gergely Orosz (newsletter) — *Intermediate* — AI-native software development, MLOps — **NEW**
  Large, well-regarded engineering-management newsletter's dedicated AI track — interviews (Steve Yegge on agent orchestration, Kent Beck on TDD + AI agents) at the org/workflow level, not just tool tips.
  https://newsletter.pragmaticengineer.com/t/ai

> Also highly relevant to this category and already listed elsewhere to avoid duplication: Simon Willison (Twitter/Blogs), 12-Factor Agents (Blogs), and Latent Space (Podcasts/Newsletters) all cover AI-native/agentic coding in depth. Star counts and follower figures in this fast-moving niche should be treated as approximate.

---

## Notes

> Fresh-grad/101-level content (Stanford CS229, generic intro material) remains excluded — CS229 got a 2026 refresh but reviewers still describe it as more mathematically demanding than a true on-ramp, so it stays out even at the Foundational tier. Papers with Code (shut down 2025) and AutoGen-specific blogs (AutoGen now in maintenance mode) remain excluded.
