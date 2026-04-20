# Day 1 — Tuesday, April 21, 2026

## Hours logged
- Block 1 (Python env + WSL2 detour): ~2 hrs
- Block 2 (wandb): ~1 hr
- Block 3 (Claude Code): ~1 hr
- Block 4 (GitHub): ~1 hr
- Total: ~5 hrs

## What worked
- WSL2 setup was smoother than expected once the Windows install completed
- GPU passthrough worked first try (nvidia-smi, PyTorch verify, matmul on cuda:0)
- Claude Code authenticated cleanly via OAuth

## What I got stuck on
- Ran install command for uv on PowerShell instead of Ubuntu initially
- wandb entity mismatch (logged in as sidantdev but real entity is sidantdev-code)
- npm install -g failed with EACCES; fixed by setting npm prefix to ~/.npm-global
- ssh-keygen pasted the literal placeholder email; fixed with ssh-keygen -c

## Unresolved questions
- wandb free tier storage (5 GB) — revisit when Phase 1 fine-tuning starts
- Whether to clean up the wandb "sidantdev-code" auto-org into something nicer

## Tomorrow (Day 2)
- Fast.ai Lesson 1 (fully) + skim Lessons 2-4
- Jeremy Howard's "A hackers guide to language models" talk
- First paper read: Attention Is All You Need (Section 3 focus)
- 100-word paper summary in notes/papers/
