# AI Curriculum 2026 — Project Context

I'm Sid. I'm working through a 24-week modern AI research engineering curriculum.
Current phase: Phase 0 (Foundations & Velocity, Weeks 1-3).
Target: MATS Autumn 2026 application by mid-curriculum checkpoint (Week 12).

## Background
- CS/DS from Virginia Tech
- Prior NLP/ML research at VT Hume Center (IC CAE Scholar)
- Prior web analytics role at Deloitte
- Currently job-seeking in data science / AI research engineering

## Environment
- OS: Ubuntu 24.04 via WSL2 on Windows
- GPU: NVIDIA RTX 4070 Ti SUPER (16GB VRAM, CUDA 12.4, compute cap 8.9)
- Python manager: uv (not pip/poetry/conda)
- Experiment tracking: wandb, project per phase, entity `sidantdev-code`
- Version control: git → github.com/sidantdev (public repo: ai-curriculum-2026)
- Shell: bash on Ubuntu

## Directory structure
~/ai-curriculum/
├── phase0-foundations/    # Fast.ai, C++ reading, Week 1-3
├── phase1-pytorch/        # Karpathy Zero-to-Hero, nanochat, LoRA
├── phase2-cuda/           # PMPP, GPU MODE, kernel writing
├── phase3-arena/          # ARENA 3.0 curriculum, mech interp, RLHF
├── phase4-agents/         # Agents, evals, Inspect framework
├── phase5-robotics/       # ETH ROS2, LeRobot, Isaac Lab
└── notes/                 # Papers, C++ notes, weekly reviews

Each phase has its own uv-managed virtualenv (.venv/).
Always `cd` into the phase directory before running commands there.

## Communication style preferences
- Direct, skip hedging — I have strong CS/DS foundations
- Explain terminal commands line-by-line to build Unix fluency
- When suggesting code, include a brief "why this approach"
- Prefer modern idioms: C++17/20 (RAII, smart pointers), Python 3.12 type hints, uv not pip
- Cite papers by name when relevant (Attention Is All You Need, Chinchilla, etc.)
- If I'm heading down a wrong path, push back rather than comply

## Code style
- Python: type hints, dataclasses/pydantic for structured data, ruff for linting
- C++: modern idioms, no raw new/delete, RAII, smart pointers
- Always suggest wandb logging for any training script
- Prefer simple scripts over complex class hierarchies unless structure is earned

## Things to avoid
- Don't suggest Jupyter notebooks when a script would do
- Don't pad answers with unnecessary preamble
- Don't propose frameworks when stdlib / small deps will do
