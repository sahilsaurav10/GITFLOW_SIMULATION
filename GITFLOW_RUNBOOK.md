# Gitflow Runbook: Feature → PR → Release → Hotfix

Run commands from the project root. Replace `YOUR_USERNAME` with your GitHub username.

## 1. Push the starter project
```bash
git init
git add .
git commit -m "chore: add Gitflow simulation starter"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/week-7-gitflow-simulation.git
git push -u origin main
```

If the GitHub repository was initialized with a README, clone that repository first or reconcile the histories before pushing.

## 2. Create `develop`
```bash
git switch -c develop
git push -u origin develop
```

## 3. Feature branch and pull request
```bash
git switch develop
git switch -c feature/add-greeting
# Edit src/app.py or tests/test_app.py.
python -m pip install -r requirements-dev.txt
pre-commit run --all-files
pytest -q
git add .
git commit -m "feat: improve greeting behavior"
git push -u origin feature/add-greeting
```
Open a pull request on GitHub: `feature/add-greeting` → `develop`. Review the diff, wait for the CI checks, then merge the PR using GitHub. Delete the remote feature branch after merging if desired.

## 4. Release branch and release tag
```bash
git switch develop
git pull
git switch -c release/1.0.0
# Update release notes or version metadata if needed.
git add .
git commit -m "chore: prepare release 1.0.0"
git push -u origin release/1.0.0
```
Open a PR: `release/1.0.0` → `main`. After review and successful CI, merge it. Then tag the release:
```bash
git switch main
git pull
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin v1.0.0
```
Merge the release changes back into `develop` with a PR (`main` → `develop`) or a local merge:
```bash
git switch develop
git pull
git merge --no-ff main -m "chore: merge release 1.0.0 back to develop"
git push
```

## 5. Hotfix lifecycle
```bash
git switch main
git pull
git switch -c hotfix/1.0.1
```
Make a small fix in `src/app.py` or a test, run checks, then:
```bash
pre-commit run --all-files
pytest -q
git add .
git commit -m "fix: resolve production greeting issue"
git push -u origin hotfix/1.0.1
```
Open a PR: `hotfix/1.0.1` → `main`. After review and green CI, merge it and tag:
```bash
git switch main
git pull
git tag -a v1.0.1 -m "Hotfix 1.0.1"
git push origin v1.0.1
```
Bring the fix back to `develop`:
```bash
git switch develop
git pull
git merge --no-ff main -m "chore: merge hotfix 1.0.1 back to develop"
git push
```

## 6. Demonstrate pre-commit and CI
- Change a Python file with trailing whitespace and run `pre-commit run --all-files`; the hook should fix or flag it.
- Push a branch or open a PR. In GitHub, open **Actions** and show the `Python CI` workflow running lint, formatting, and pytest.
- Optional: enable branch protection for `main` and `develop` and require status checks before merging.

## Submission evidence checklist
- [ ] Feature branch and PR targeting `develop`
- [ ] CI checks passed on the PR
- [ ] Release PR targeting `main` and tag `v1.0.0`
- [ ] Hotfix PR targeting `main` and tag `v1.0.1`
- [ ] Hotfix merged back to `develop`
- [ ] Local pre-commit hook demonstrated
