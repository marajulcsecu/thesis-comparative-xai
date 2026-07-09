# 🧠 NOTES.md — My Thesis Scratchpad

> Private, gitignored. The plan-defined Phase 0 tracker plus the long-term
> scratchpad sections (AI prompts, bug log, ideas, advisor feedback).
> Update this after every working session.

---

## Setup progress

- [x] Phase 0 in progress (start date: 2026-07-09)
- [x] Steps 0.1–0.7 complete
- [x] Step 0.8 deferred with full checklist in `02_literature/ZOTERO_SETUP.md`

---

## Step 0.1 — Folder Structure
- Status: ✅ complete (Jul 9)
- 20 folders + 3 placeholder files created via Step 0.1 commands in `phase_00_FOUNDATION.md`.

## Step 0.2 — Git + GitHub
- Status: ✅ complete (Jul 9)
- Git initialized, `.gitignore` filled (48 rules), first commit `c2821c8` pushed to
  `git@github.com:marajulcsecu/thesis-comparative-xai.git` (`main` branch).

## Step 0.3 — Python + venv
- Status: ✅ complete (Jul 9)
- Python 3.12.3 (system) — meets ≥3.10 requirement.
- `.venv` created at workspace root, isolated from system packages (`include-system-site-packages = false`).
- `pip` upgraded: 24.0 → **26.1.2**.
- Activation: `source .venv/bin/activate`
- Both `which python` and `which pip` resolve to `.venv/bin/`.

## Step 0.4 — Install Libraries
- Status: ✅ complete (Jul 9)
- `src/requirements.txt` created with version ranges compatible with Python 3.12.
  - Note: the original `phase_00_FOUNDATION.md` pinned mid-2023 versions that
    did **not** support Python 3.12. Replaced with mid-2025 stable ranges.
- `pip install -r src/requirements.txt` succeeded. Verification produced
  `All libraries OK` and the Jupyter kernel `Python (thesis-env)` is registered.

| Package          | Version |
|------------------|---------|
| numpy            | 2.4.6   |
| pandas           | 2.3.3   |
| matplotlib       | 3.11.0  |
| seaborn          | 0.13.2  |
| scikit-learn     | 1.9.0   |
| xgboost          | 2.1.4   |
| lightgbm         | 4.6.0   |
| shap             | 0.52.0  |
| lime             | 0.2.0.1 |
| optuna           | 4.9.0   |
| joblib           | 1.5.3   |
| tqdm             | 4.68.4  |
| scipy            | 1.18.0  |
| statsmodels      | 0.14.6  |
| imbalanced-learn | 0.14.2  |
| jupyter          | 1.1.1   |
| ipykernel        | 6.31.0  |
| notebook         | 7.6.0   |
| python-dotenv    | 1.2.2   |

## Step 0.5 — Tracking Files (NOTES, README, .gitignore)
- Status: ✅ complete (Jul 9)
- `NOTES.md` now has 11 sections: 4-step Phase 0 tracker + 7 long-term
  scratchpad sections (accounts log, tools, AI prompts, bug log, ideas,
  advisor feedback).
- `README.md` filled with a 1-paragraph stub (full version lands in Step 0.13).
- `.gitignore` already complete from Step 0.2 (no change in this step).

## Step 0.6 — Google Colab + Drive
- Status: ✅ complete (Jul 9)
- Notebook `00_setup_test.ipynb` created in Colab.
- **Colab Python version:** `3.12.13 (main, Mar  4 2026, 09:23:07) [GCC 11.4.0]`.
- **No GPU attached** — confirmed via `nvidia-smi: command not found` (acceptable
  for tabular data; switch to T4 GPU runtime only when SHAP becomes heavy).
- **Drive mounted** at `/content/drive`; thesis folder created at
  `/content/drive/MyDrive/Thesis_Backup/Thesis_V1`.
- **Drive sync verified** — wrote `test.txt` (22 bytes), read back OK.
- **Notebook saved in Drive** as `Copy of 00_setup_test.ipynb` in
  `My Drive / Colab Notebooks/`. The optional move into
  `Thesis_Backup/Thesis_V1/` was skipped — we keep originals in
  `Colab Notebooks/` and we'll export final copies from there.
- Marker file `test.txt` left in `Thesis_Backup/` as proof of mount; delete
  during Step 0.12 backup if you prefer a clean folder.

---

## Accounts log

| Service   | Identifier                | Status |
|-----------|---------------------------|--------|
| GitHub    | marajulcsecu              | ✅ created, repo `thesis-comparative-xai` pushed (Jul 9) |
| Google    | (your Gmail)              | ✅ Drive mounted, `Thesis_Backup/Thesis_V1/` created (Jul 9) |
| Kaggle    | (your Kaggle username)    | ✅ token saved in `~/.kaggle/access_token` (Jul 9) |
| Zotero    | (local app)               | ⏸ deferred → install Jul 23-24 (Phase 1→2 transition) |
| Overleaf  | (your Overleaf email)     | ⏳ Step 0.9 |

---

## Tools / versions in use

- OS: Ubuntu 22.04
- Python: 3.12.3 (system + venv)
- Git: 2.43.0
- Editor: VS Code (Puku active)
- Default terminal: bash (in Puku)

---

## Useful AI prompts that worked

### Prompt 1 — _to be filled after first use_
> _paste the prompt here_

Result:
> _paste what AI produced, what you kept / rewrote_

_(add more as they earn their place — only keep ones you actually reuse)_

---

## Bugs I solved

| Date | Bug | Fix |
|------|-----|-----|
| 2026-07-09 | `pip install` cancelled by terminal 60 s timeout during long download | Run install in detached background: `nohup pip install -r src/requirements.txt > log 2>&1 &` then poll the log file with `tail`. |
| 2026-07-09 | `phase_00_FOUNDATION.md` prescribed numpy 1.24.3 / pandas 2.0.3 which don't support Python 3.12 | Replaced with mid-2025 version ranges (`numpy>=2.0,<3.0`, etc.). Documented in this file. |

_(add a row every time you spend >15 minutes debugging)_

---

## Ideas to revisit

-

---

## Advisor feedback

| Date | Source | Note |
|------|--------|------|
|      | (advisor name / meeting) | _action items + decisions_ |

_(keep brief — long discussions live in `01_proposal/meeting_notes/`)_

## Step 0.7 — Kaggle account + API token
- Status: ✅ complete (Jul 9)
- Account created via Google SSO at https://www.kaggle.com
  (no phone-verify prompt appeared — Gmail SSO was sufficient).
- Token storage uses Kaggle's 2024+ scoped-token format:
  `~/.kaggle/access_token` (38 bytes, mode 600), NOT `kaggle.json`.
- `kaggle-2.2.3` CLI installed into `.venv` along with 8 supporting
  packages (kagglesdk, jupytext, protobuf, ...).
- Authentication verified via `kaggle datasets list | head -10`
  (returned 10 real datasets, including FIFA World Cup 2026 stats).
- Iris test download **skipped** as redundant — the `datasets list`
  call already exercised the same authenticated network path.
- ⚠️ Token rotation **deliberately skipped** — `KGAT_…` is exposed in
  this chat history. Accepting low risk for now. To rotate later:
  Kaggle → Settings → API Tokens → ⋮ → Expire, then Generate New.

## Step 0.8 — Zotero + Better BibTeX
- Status: ⏸ **deferred** (not installed yet)
- **Reason for deferral:** heavy GUI install (Linux tarball, Firefox plugin,
  browser extension, 5 seed papers). No real papers to save at end of Phase 0,
  and `02_literature/` is empty so `.bib` export would land in a void.
- **Recommended install window:** Thu/Fri of Week 2 (≈ Jul 23-24, 2026) —
  the natural Phase 1 → Phase 2 transition.
- **Hard deadline:** the day before writing proposal Chapter 2 (Literature
  Review) — Phase 3.
- **Full checklist saved at:** `02_literature/ZOTERO_SETUP.md` (250+ lines,
  copy-pasteable when ready).

---

