# AI Curriculum — Project Context

I'm Sid. I'm working through a capabilities-first AI research engineering
curriculum, full depth, no compressions, no fixed timeline. Target:
frontier-lab research engineer + competent technical founder.

Current phase: Phase 0 (Foundations & Positioning).

## Background
- CS/DS from Virginia Tech
- Prior NLP/ML research at VT Hume Center (IC CAE Scholar)
- Prior web analytics role at Deloitte
- Currently job-seeking

## Trajectory

Priority-ranked focus:
1. Large agentic systems (deepest phase)
2. Computer-use agents
3. Embodied robotics
4. Scaling / superintelligence

Alignment foundation via full ARENA curriculum. Full depth everywhere;
no compromises on material. Knowledge target: Master's-equivalent depth in
focus areas plus frontier depth beyond coursework.

Target outcomes by end of curriculum:
- 4 shipped portfolio artifacts (nanochat variant, agent project,
  computer-use agent, SO-ARM101 VLA)
- 3 merged OSS PRs (vLLM/SGLang/TRL/verl/inspect_ai/lerobot/openpi tier)
- 1 MCP server published to registry
- 2 long-form essays (red-line, founder thesis)

## Environment
- OS: Ubuntu 24.04 via WSL2 on Windows
- GPU: NVIDIA RTX 4070 Ti SUPER (16GB VRAM, CUDA 12.4, compute cap 8.9)
- Python manager: uv (not pip/poetry/conda)
- Experiment tracking: wandb, project per phase, entity `sidantdev-code`
- Version control: git → github.com/sidantdev/ai-curriculum-2026
- Shell: bash on Ubuntu

## Directory structure
~/ai-curriculum/
├── phase0-foundations/           # Karpathy, Raschka, toolchain
│   └── karpathy/
│       ├── 01-micrograd/
│       ├── 02-makemore-bigram/
│       └── ...
├── phase1-transformers-kernels/  # nanochat, FlashAttention, vLLM
├── phase3-alignment/             # Full ARENA
├── phase4-agents/                # Deepest phase
├── phase5-computer-use/          # OSWorld, UI-TARS-2
├── phase6-robotics/              # LeRobot, SO-ARM101
├── phase7-scaling/               # CS336, RLHF Book
├── phase8-portfolio/             # Polish + applications
└── notes/                        # Papers, essays, phase reviews

Each phase has its own uv-managed virtualenv (.venv/).
Always `cd` into the phase directory before running commands there.

## Communication style preferences
- Direct, skip hedging — I have strong CS/DS foundations
- Explain terminal commands line-by-line to build Unix fluency
- When suggesting code, include a brief "why this approach"
- Prefer modern idioms: PyTorch 2.x, Python 3.12 type hints, uv not pip
- Cite papers by name when relevant (DeepSeek V3, FlashAttention, Helix, π0.5)
- If I'm heading down a wrong path, push back rather than comply
- For file content, prefer VS Code edit over heredoc (paste friction on Windows Terminal)
- Avoid imposing fixed timings or schedules; treat curriculum as a structured
  list, not a calendar

## Code style
- Python: type hints, dataclasses/pydantic for structured data, ruff for linting
- Always suggest wandb logging for any training script
- Prefer simple scripts over complex class hierarchies unless structure is earned
- For training code, prefer minimalism-that-works over complete-framework

## Things to avoid
- Don't suggest Jupyter notebooks for anything beyond exploratory work; prefer scripts
- Don't pad answers with unnecessary preamble
- Don't propose frameworks when stdlib / small deps will do
- Don't treat alignment concerns as irrelevant to capabilities work
- Don't assign hour estimates or day-by-day schedules unless explicitly asked