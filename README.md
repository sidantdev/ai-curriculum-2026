# AI Curriculum

A capabilities-first AI research engineering curriculum.

## Background

CS/DS from Virginia Tech. Prior NLP/ML research at VT Hume Center (IC CAE Scholar).
Built sidant.dev and ResumeForge. Currently job-seeking with a focus on AI research
engineering and founder/builder opportunities at the frontier of AGI/ASI work.

## End goals

Knowledge target: Frontier depth on agentic systems,
computer-use, embodied robotics, and scaling.

Priority focus areas, ranked:
1. Large agentic systems (scaffolding, planning, multi-agent, orchestration)
2. Computer-use agents (browser/OS automation, GUI grounding)
3. Embodied robotics (VLAs, sim-to-real, humanoid policies)
4. Scaling / super-intelligence (pre-training, post-training, test-time compute)

## Phases

- [ ] **Phase 0: Foundations & Positioning** — Karpathy Zero to Hero, Raschka LLM book, 2026 builder toolchain
- [ ] **Phase 1: Transformer Internals + Kernels** — Distributed training, FlashAttention, nanochat speedrun, vLLM/SGLang
- [ ] **Phase 3: Alignment Foundation** — Full ARENA chapters, Inspect AI evals, red-line essay
- [ ] **Phase 4: Large Agentic Systems (deepest)** — Anthropic patterns, LangGraph/OpenAI Agents SDK/Claude Agent SDK, RLVR, agent portfolio sprint
- [ ] **Phase 5: Computer-Use Agents** — UI-TARS-2, OSWorld, Stagehand/Browser Use, prompt-injection defense
- [ ] **Phase 6: Embodied Robotics** — LeRobot, SO-ARM101, SmolVLA, π0.5, Isaac Lab, humanoid RL reading
- [ ] **Phase 7: Scaling & Superintelligence Study** — CS336, DeepSeek V3/R1, RLHF Book, scaling capstone
- [ ] **Phase 8: Portfolio & Recruiting** — Artifact polish, OSS PRs, frontier lab applications, founder-track motion

## Portfolio targets

Four shipped artifacts, three merged OSS PRs, one published MCP server, two
long-form essays (red-line + founder thesis).

1. nanochat + architectural variant (MLA, MTP, or MoE)
2. Agent scaffold / eval / RL recipe
3. Computer-use agent OR prompt-injection red team OR domain-specific computer-use product
4. SO-ARM101 + SmolVLA or π0.5 fine-tune

## Environment

- Ubuntu 24.04 (WSL2) on Windows
- NVIDIA RTX 4070 Ti SUPER (16GB, CUDA 12.4)
- Python via `uv` (not pip/conda)
- Experiment tracking: wandb (entity `sidantdev-code`)
- Editor: VS Code with WSL remote + Claude Code

## Phase 0 — Week 1 task list

- [x] Environment setup (WSL2, uv, PyTorch, wandb, Claude Code, git/GitHub)
- [ ] Karpathy Video 1 (micrograd from scratch), DeepSeek V3 first-pass read
- [ ] Karpathy Video 2 (makemore bigram), Raschka Ch. 1-2
- [ ] Karpathy Video 3 (makemore MLP), Raschka Ch. 3
- [ ] Karpathy Video 4 (BatchNorm, activations)
- [ ] Karpathy Videos 5-6 (backprop ninja, WaveNet)
- [ ] Karpathy Video 7 (build GPT from scratch)

## Phase 0 deliverables

- Own 124M-param nanoGPT trained on TinyShakespeare + FineWeb-Edu sample, W&B report, blog post
- GQA or MLA attention variant implemented in your nanoGPT
- Modern LLM toolkit comparison post (Modal vs Replicate vs Together vs Baseten)

## Notes

See [notes/](notes/) for paper summaries, reading notes, phase reviews, and
the two long-form essays (Phase 3 red-line, Phase 7 founder thesis).

## License

Personal learning artifacts. Code is MIT-licensed where noted.