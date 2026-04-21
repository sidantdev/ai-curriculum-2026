# Setup day

## What got done

- WSL2 with Ubuntu 24.04 installed and verified
- GPU passthrough working (nvidia-smi shows RTX 4070 Ti SUPER, 17.2 GB VRAM)
- uv installed, Phase 0 workspace created
- PyTorch 2.6 + CUDA 12.4 verified, GPU matmul tested from Python
- wandb configured (entity: sidantdev-code), first run logged
- npm global install path moved to ~/.npm-global to avoid sudo
- Claude Code installed and authenticated via OAuth
- SSH key generated, added to GitHub
- Git configured (user.name, user.email)
- Repo initialized, .gitignore created, README written
- First two commits pushed to github.com/sidantdev/ai-curriculum-2026

## What got stuck on

- Ran uv install command in PowerShell initially (needed to be in Ubuntu)
- wandb entity mismatch — sidantdev display name vs sidantdev-code actual entity
- npm install -g failed with EACCES; fixed via ~/.npm-global
- ssh-keygen placeholder email pasted literally; fixed with `ssh-keygen -c`
- Paste friction into terminal for multi-line content (resolved by moving to VS Code)

## Next

- Karpathy Zero to Hero, Video 1 (micrograd from scratch)
- Implement micrograd from memory in a second notebook
- First-pass skim of DeepSeek V3 Technical Report
- Paper summary in notes/papers/

## Curriculum notes

Curriculum pivoted from alignment-track 24-week plan (original target: MATS
Autumn 2026) to capabilities-first, full-depth, no-timeline list. Knowledge
target: Master's-equivalent on focus areas, frontier depth beyond. MATS
optional. Timeline removed in favor of phase-based structured list.

Phase structure:
- Phase 0 Foundations
- Phase 1 Transformer Internals + Kernels
- Phase 3 Alignment Foundation
- Phase 4 Large Agentic Systems (deepest)
- Phase 5 Computer-Use Agents
- Phase 6 Embodied Robotics
- Phase 7 Scaling & Super-intelligence
- Phase 8 Portfolio & Recruiting

See README.md for phase detail and deliverables.