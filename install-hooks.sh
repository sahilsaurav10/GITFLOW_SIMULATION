#!/usr/bin/env bash
set -euo pipefail
python -m pip install -r requirements-dev.txt
pre-commit install
echo "pre-commit hook installed. Try: pre-commit run --all-files"
