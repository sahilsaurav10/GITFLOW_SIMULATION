# Week 7 — Full Gitflow Simulation

A hands-on Git workflow demo covering feature branches, pull requests, release branches/tags, hotfixes, a pre-commit hook, and GitHub Actions CI.

## Workflow
```text
main
 └── develop
      └── feature/add-greeting ── PR/merge ──> develop
      └── release/1.0.0 ── merge + tag v1.0.0 ──> main and develop
main
 └── hotfix/1.0.1 ── merge + tag v1.0.1 ──> main and develop
```

## Contents
- `src/app.py`: tiny Python app used to demonstrate quality checks.
- `tests/test_app.py`: pytest tests.
- `.pre-commit-config.yaml`: Ruff linting/format checks and whitespace checks.
- `.github/workflows/ci.yml`: GitHub Actions runs lint and tests on pushes and pull requests.
- `scripts/install-hooks.sh`: installs pre-commit hooks locally.
- `docs/GITFLOW_RUNBOOK.md`: step-by-step commands for the complete simulation.

## Requirements
- Git
- Python 3.10+
- `pip`
- A GitHub repository (for real pull requests and Actions)

## Quick start
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

python -m pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
pytest -q
python -m src.app
```

## GitHub setup
1. Create an empty GitHub repository named `week-7-gitflow-simulation`.
2. Upload/push this project.
3. In GitHub, create `develop` from `main`.
4. Follow `docs/GITFLOW_RUNBOOK.md` to create feature/release/hotfix branches and PRs.
5. Ensure Actions runs on pull requests. Protect `main` and `develop` if repository settings allow it.

## Important
The project provides the code, automation, and exact commands. Actual pull requests, branch merges, releases, and CI runs happen in your own GitHub repository after you push it; they are not fabricated by this template.
