# 📘 PHASE 0 — Foundation & Tooling (Detailed)

> **Phase Goal**: Set up your complete workspace, tools, accounts, and environment BEFORE any research work. Without this foundation, you'll waste hours later fighting setup issues instead of doing research.

> **Time Estimate**: 1 day (focused, ~6-8 hours total)

> **Exit Criteria**: All folders exist on your PC, Python environment runs, Git works, you can open Google Colab + Kaggle, Zotero library is created, and a "Hello SHAP" test runs successfully.

---

## 📑 STEP INDEX

| Step | Title | Time |
|---|---|---|
| 0.1 | Create the project folder structure | 15 min |
| 0.2 | Initialize Git + GitHub repository | 30 min |
| 0.3 | Install Python + create virtual environment | 30 min |
| 0.4 | Install all required Python libraries | 15 min |
| 0.5 | Create the 3 thesis tracking files (NOTES.md, README.md, .gitignore) | 20 min |
| 0.6 | Set up Google Colab + link to Google Drive | 20 min |
| 0.7 | Set up Kaggle account + generate API token | 20 min |
| 0.8 | Set up Zotero reference manager + Better BibTeX plugin | 30 min |
| 0.9 | Create Overleaf account (for paper writing later) | 10 min |
| 0.10 | Run the "Hello SHAP" smoke test | 30 min |
| 0.11 | Run "Hello LIME" smoke test | 20 min |
| 0.12 | Initial backup to Google Drive | 15 min |
| 0.13 | Update README.md with your project info | 15 min |
| 0.14 | Phase 0 completion checklist | 10 min |

**Total time**: ~5-7 hours (can be split across 2 days)

---

## 🧭 STEP 0.1 — Create the Project Folder Structure

### 🎯 What we want to achieve
Create the **complete, organized folder tree** that all your thesis files will live in. This prevents the "scattered files on Desktop" problem that plagues most students.

### 📂 Folder structure you will create
```
Thesis_V1/
├── 01_proposal/
├── 02_literature/
│   └── notes_per_paper/
├── 03_proposal_backup/
├── 04_data/
│   ├── raw/
│   ├── processed/
│   └── eda_figures/
├── 05_models/
│   └── saved_models/
├── 06_xai_exploration/
│   ├── shap_outputs/
│   └── lime_outputs/
├── 07_xai_output/
├── 08_comparison/
│   ├── results/
│   └── figures/
├── 09_thesis/
│   └── figures/
├── 10_paper/
├── src/
├── notebooks/
├── .git/
├── NOTES.md
├── README.md
├── .gitignore
└── THESIS_ROADMAP.md   ← already exists from previous step
```

### 🤖 What AI will do for you
- Generate the exact bash commands below
- Explain what each folder is for

### 👤 What YOU will do
1. Open a terminal (Linux: Ctrl+Alt+T, Windows: use WSL or Git Bash)
2. Navigate to your workspace:
   ```bash
   cd "/home/marajul/Desktop/ENG 672 Technical Communication and Writing/Thesis_V1"
   ```
3. Run this **single command** that creates EVERY folder at once:
   ```bash
   mkdir -p 01_proposal \
            02_literature/notes_per_paper \
            03_proposal_backup \
            04_data/raw \
            04_data/processed \
            04_data/eda_figures \
            05_models/saved_models \
            06_xai_exploration/shap_outputs \
            06_xai_exploration/lime_outputs \
            07_xai_output \
            08_comparison/results \
            08_comparison/figures \
            09_thesis/figures \
            10_paper \
            src \
            notebooks
   ```
4. Create empty placeholder files:
   ```bash
   touch NOTES.md README.md .gitignore
   ```
5. Verify structure was created:
   ```bash
   ls -la
   find . -type d | sort
   ```
   You should see all folders listed.

### ✅ Success criteria for Step 0.1
- [ ] All 18 folders visible when running `ls -la`
- [ ] `NOTES.md`, `README.md`, `.gitignore` files exist (empty for now)
- [ ] `find . -type d` command shows no missing folders

### 🚨 Troubleshooting
| Problem | Fix |
|---|---|
| `mkdir: permission denied` | Make sure you're in your home directory; don't run as sudo |
| Folders created in wrong place | You ran from wrong directory; delete them and re-cd |
| Some folders missing | Re-run the command — `mkdir -p` is safe (no error if exists) |

---

## 🧭 STEP 0.2 — Initialize Git + GitHub Repository

### 🎯 What we want to achieve
Set up **version control** so your code has a history and can be recovered if your PC dies. **This is MANDATORY** — never write code without Git.

### 🤖 What AI will do for you
- Generate the exact Git commands
- Explain what each command does

### 👤 What YOU will do

**Part A: Local Git setup**

1. Initialize Git in your workspace (run inside `Thesis_V1/`):
   ```bash
   git init
   ```
2. Configure your identity (so commits are attributed to you):
   ```bash
   git config user.name "MD Marajul Haque"
   git config user.email "your_github_email@example.com"
   ```
   ⚠️ Use the **same email** you'll use for GitHub account.
3. Set default branch name to `main`:
   ```bash
   git config init.defaultBranch main
   ```

**Part B: Create GitHub account (if you don't have one)**

1. Go to `https://github.com`
2. Click **Sign Up** → use your university email if possible
3. Choose Free plan
4. Verify email

**Part C: Create the GitHub repository**

1. After login, click **+** (top right) → **New repository**
2. Fill in:
   - Repository name: `thesis-comparative-xai`
   - Description: "Comparative Interpretability Analysis of Ensemble ML Models"
   - Visibility: **Private** (your work isn't public yet)
   - ❌ Do NOT initialize with README (you already have one)
3. Click **Create repository**
4. GitHub will show you commands — ignore the "push existing repo" section, use these instead:

**Part D: Connect local to remote**

1. Copy the remote URL from GitHub (looks like `https://github.com/yourusername/thesis-comparative-xai.git`)
2. Run:
   ```bash
   git remote add origin https://github.com/yourusername/thesis-comparative-xai.git
   git branch -M main
   git add .
   git commit -m "Initial commit: thesis project structure"
   git push -u origin main
   ```
3. Refresh GitHub page → you should see all your folders there

**Part E: Add `.gitignore` rules**

Overwrite your empty `.gitignore` with this content:
```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
env/

# Data (large files - use Google Drive instead)
04_data/raw/*.csv
04_data/processed/*.csv

# Models (large files - save to Drive)
05_models/saved_models/*.pkl
05_models/saved_models/*.joblib

# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/

# Notebooks
.ipynb_checkpoints/

# Credentials (NEVER commit these)
.kaggle/
.env
EOF
```

This prevents accidentally committing large data files or API keys.

4. Commit the new `.gitignore`:
   ```bash
   git add .gitignore
   git commit -m "Add gitignore"
   git push
   ```

### ✅ Success criteria for Step 0.2
- [ ] GitHub repo exists and is **private**
- [ ] Local folder structure visible on GitHub
- [ ] Your identity is configured (`git config user.name` returns your name)
- [ ] `.gitignore` is committed and active
- [ ] You can run `git status` and see clean working tree

### 🚨 Troubleshooting
| Problem | Fix |
|---|---|
| `git: command not found` | Install Git: `sudo apt install git` (Linux) or download from git-scm.com |
| `Permission denied (publickey)` | Use HTTPS URL (not SSH); add GitHub PAT token if prompted |
| `fatal: not a git repository` | You forgot to run `git init` first; run it in the workspace folder |
| `nothing to commit` | Files were already committed; that's fine, just push |

---

## 🧭 STEP 0.3 — Install Python + Create Virtual Environment

### 🎯 What we want to achieve
Install a **clean, isolated Python environment** so your project's packages don't conflict with other projects on your PC.

### 🤖 What AI will do for you
- Recommend installation method
- Explain what virtual environments do

### 👤 What YOU will do

**Part A: Install Python 3.10+**

Check if Python is already installed:
```bash
python3 --version
```
If it shows `Python 3.10.x` or higher → skip to Part B.

If NOT installed:
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt update
  sudo apt install python3.10 python3-pip python3-venv
  ```
- **Windows**:
  - Download Python 3.10+ from `https://www.python.org/downloads/`
  - ✅ Check "Add Python to PATH" during install

**Part B: Create virtual environment**

Inside `Thesis_V1/`:
```bash
python3 -m venv .venv
```

This creates a `.venv/` folder with isolated Python.

**Part C: Activate the environment**

- **Linux/Mac**:
  ```bash
  source .venv/bin/activate
  ```
- **Windows (PowerShell)**:
  ```bash
  .venv\Scripts\Activate.ps1
  ```

You should now see `(.venv)` at the start of your terminal line.

**Part D: Upgrade pip**
```bash
pip install --upgrade pip
```

**Part E: Verify isolation**
```bash
which python   # Should show path inside .venv
pip list       # Should be minimal packages (just pip, setuptools)
```

### ✅ Success criteria for Step 0.3
- [ ] Python version 3.10+ installed and accessible
- [ ] `.venv/` folder exists in workspace
- [ ] Terminal shows `(.venv)` prefix
- [ ] `pip list` is clean (no Anaconda bloat)

### 🚨 Troubleshooting
| Problem | Fix |
|---|---|
| `python3: command not found` | Install Python; ensure it's in PATH |
| `ensurepip is not available` | `sudo apt install python3.10-venv` |
| Activation doesn't work on Windows | Use Git Bash or enable PS scripts: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |
| Want to start fresh | `rm -rf .venv` and recreate |

---

## 🧭 STEP 0.4 — Install All Required Python Libraries

### 🎯 What we want to achieve
Install every library you'll need **once now**, so you don't get interrupted later.

### 🤖 What AI will do for you
- Generate a `requirements.txt` file for reproducibility
- Explain what each library does

### 👤 What YOU will do

**Part A: Create `requirements.txt`**

Inside `Thesis_V1/src/`, create a file called `requirements.txt`:
```bash
cat > src/requirements.txt << 'EOF'
# Core data science
numpy==1.24.3
pandas==2.0.3
matplotlib==3.7.3
seaborn==0.12.2

# Machine learning
scikit-learn==1.3.0
xgboost==2.0.2
lightgbm==4.1.0

# Explainability
shap==0.43.0
lime==0.2.0.1

# Optimization & utilities
optuna==3.3.0
joblib==1.3.1
tqdm==4.66.1

# Statistics
scipy==1.11.2
statsmodels==0.14.0

# Notebook
jupyter==1.0.0
ipykernel==6.25.1

# Utilities
python-dotenv==1.0.0
EOF
```

💡 *These versions were current as of mid-2026. AI note: you can remove the version pinning for newer flexibility — just `numpy pandas matplotlib ...` without `==x.y.z`.*

**Part B: Install everything**

```bash
pip install -r src/requirements.txt
```

This will take 2-5 minutes. Watch for errors.

**Part C: Verify installations**
```bash
python -c "import numpy, pandas, sklearn, xgboost, lightgbm, shap, lime; print('All libraries OK')"
```

Should output: `All libraries OK`

**Part D: Test Jupyter kernel**
```bash
python -m ipykernel install --user --name thesis-env --display-name "Python (thesis-env)"
```

This lets Jupyter Notebooks use your venv.

### ✅ Success criteria for Step 0.4
- [ ] `pip list` shows all listed libraries
- [ ] Verification command outputs "All libraries OK"
- [ ] Jupyter kernel "Python (thesis-env)" visible in VSCode/Colab dropdown

### 🚨 Troubleshooting
| Problem | Fix |
|---|---|
| `pip install` fails with version conflict | Remove `==x.y.z` and use just library names |
| SHAP installation takes long | Normal — it builds C extensions; wait 2-3 min |
| LIME install fails on Windows | Update pip first: `pip install --upgrade pip` then retry |
| "No module named X" after install | Make sure venv is activated (check `(.venv)` prefix) |

---

## 🧭 STEP 0.5 — Create the 3 Thesis Tracking Files

### 🎯 What we want to achieve
Set up **3 plain-text tracking files** that act as your thesis "external brain".

### 🤖 What AI will do for you
- Write the initial content for each file
- Suggest best practices for keeping them updated

### 👤 What YOU will do

**File 1: `NOTES.md`** — your private scratchpad
- AI will pre-fill this. This is where you save:
  - Prompts that worked well
  - Bugs you spent hours on (with fix)
  - Ideas you want to revisit
  - Advisor feedback notes

**File 2: `README.md`** — public-facing project intro
- Will be filled in Step 0.13

**File 3: `.gitignore`** — already created in Step 0.2

For now, write a starter `NOTES.md`:
```bash
cat > NOTES.md << 'EOF'
# 🧠 NOTES.md — My Thesis Scratchpad

## Setup completed
- [x] Phase 0 in progress (date: ____)

## Useful AI prompts that worked

### Prompt 1: (write here what AI prompted)
Result: (write here what worked)

## Bugs I solved
| Date | Bug | Fix |
|---|---|---|
| | | |

## Ideas to revisit
-

## Advisor feedback
-
EOF
```

### ✅ Success criteria for Step 0.5
- [ ] All 3 files exist
- [ ] `NOTES.md` has the template above

---

## 🧭 STEP 0.6 — Set Up Google Colab + Google Drive

### 🎯 What we want to achieve
Get **free GPU access** for any heavy model training that your 8 GB RAM can't handle, AND automatic cloud backup.

### 🤖 What AI will do for you
- Walk you through Colab setup
- Explain Drive integration

### 👤 What YOU will do

**Part A: Create/use Google account**

If you have Gmail already, skip. Otherwise create one at `https://accounts.google.com` (use university email if preferred).

**Part B: Open Colab**
1. Go to `https://colab.research.google.com`
2. Click **New Notebook**
3. Rename to `00_setup_test.ipynb`
4. Verify top-right shows a runtime (CPU is fine for this test)

**Part C: Test Colab**
In a cell, run:
```python
import sys
print("Python:", sys.version)
!nvidia-smi   # Will show "command not found" if no GPU — that's OK for tabular data
```

**Part D: Link Google Drive**

Add a new cell and run:
```python
from google.colab import drive
drive.mount('/content/drive')

# Create your thesis folder in Drive
!mkdir -p "/content/drive/MyDrive/Thesis_Backup/Thesis_V1"
```

Authorize when prompted.

**Part E: Test that Drive sync works**
```python
# Write a test file
with open('/content/drive/MyDrive/Thesis_Backup/test.txt', 'w') as f:
    f.write('Thesis backup working!')

# Read it back
!cat '/content/drive/MyDrive/Thesis_Backup/test.txt'
```

**Part F: Save Colab notebook in Drive**
1. File → Save a copy in Drive
2. Move it into `Thesis_Backup/Thesis_V1/notebooks/`

### ✅ Success criteria for Step 0.6
- [ ] Colab account works
- [ ] Drive mounted successfully
- [ ] Test file saved and read back
- [ ] Notebook saved in Drive folder

---

## 🧭 STEP 0.7 — Set Up Kaggle Account + API Token

### 🎯 What we want to achieve
Get a **second free GPU platform** (Kaggle gives 30 hrs/week) + direct dataset download capability.

### 🤖 What AI will do for you
- Guide through Kaggle token generation
- Show how to use Kaggle API

### 👤 What YOU will do

**Part A: Create Kaggle account**

1. Go to `https://www.kaggle.com`
2. Sign up with Google (easiest)
3. Verify phone number (required for API access)

**Part B: Generate API token**

1. Click your avatar (top right) → **Settings**
2. Scroll to **API** section → click **Create New Token**
3. A file `kaggle.json` downloads — DO NOT lose it

**Part C: Place token correctly**

```bash
# Create Kaggle config folder
mkdir -p ~/.kaggle

# Move downloaded kaggle.json there (adjust path to where it downloaded)
mv ~/Downloads/kaggle.json ~/.kaggle/

# Set permissions (REQUIRED for security)
chmod 600 ~/.kaggle/kaggle.json
```

**Part D: Install Kaggle CLI**
```bash
pip install kaggle
```

**Part E: Test it works**
```bash
kaggle datasets list | head -20
```

Should show a list of datasets.

**Part F: Test downloading a tiny dataset**
```bash
cd 04_data/raw/
kaggle datasets download -d uciml/iris -p . --unzip
ls -la
```

You should see `Iris.csv`. After verifying, delete it:
```bash
rm -rf Iris.csv iris
```

### ✅ Success criteria for Step 0.7
- [ ] Kaggle account created
- [ ] `kaggle.json` placed in `~/.kaggle/` with correct permissions
- [ ] `kaggle datasets list` returns dataset list
- [ ] Test download worked and was cleaned up

---

## 🧭 STEP 0.8 — Set Up Zotero + Better BibTeX

### 🎯 What we want to achieve
Install a **reference manager** so you can save papers, take notes, and export `.bib` files for the paper.

### 🤖 What AI will do for you
- Recommend the exact Zotero plugins
- Generate the import workflow

### 👤 What YOU will do

**Part A: Download Zotero**

1. Go to `https://www.zotero.org/download/`
2. Download **Zotero 6** (desktop app)
3. Install (Linux: download `.tar.bz2`, extract, run)

**Part B: Create your thesis library**

1. Open Zotero
2. Click **New Library** (green icon, top left)
3. Name it: `Thesis - XAI Ensemble Comparison`

**Part C: Install Better BibTeX plugin (CRITICAL for thesis writing)**

1. In Zotero: **Tools → Add-ons**
2. Click gear icon → **Install Add-on From File**
3. Download `better-bibtex.xpi` from: `https://retorque.re/zotero-better-bibtex/installation/`
4. Install it
5. Restart Zotero
6. **Edit → Settings → Better BibTeX → Export** → set format to "Citation Key: auth + year + title"

**Part D: Install Zotero Connector browser extension**

1. For Chrome/Firefox/Edge: search "Zotero Connector" in your browser's extension store
2. Install it
3. Pin it to toolbar

**Part E: Add 5 seed papers (start your literature exploration)**

1. Open Google Scholar in browser: `https://scholar.google.com`
2. Search for:
   - `"SHAP" LIME comparison ensemble learning`
   - `explainable artificial intelligence disease prediction`
   - `XGBoost stacking disease prediction interpretability`
3. For each interesting paper, click the Zotero Connector icon in your browser
4. Save with tags: `to-read, XAI, ensemble`
5. Aim for 5 papers today

**Part F: Verify Better BibTeX export**

1. In Zotero, right-click your library → **Export Library**
2. Format: **Better BibTeX**
3. Check "Export Notes"
4. Save as `02_literature/references.bib`

### ✅ Success criteria for Step 0.8
- [ ] Zotero 6 installed and library created
- [ ] Better BibTeX plugin active
- [ ] Connector extension installed in browser
- [ ] 5 seed papers saved with tags
- [ ] `.bib` file exported successfully

---

## 🧭 STEP 0.9 — Create Overleaf Account

### 🎯 What we want to achieve
Set up the **LaTeX editor** you'll use for journal paper formatting later (don't need to do anything now).

### 🤖 What AI will do for you
- Confirm Overleaf is the right tool (vs Word)
- Note: thesis itself may be in Word — depends on university

### 👤 What YOU will do

1. Go to `https://www.overleaf.com`
2. Sign up (free tier is sufficient)
3. Link to ORCID if you have one (researcher ID)
4. Click **New Project → Blank**
5. Rename to `IEEE_Access_Template` (don't fill it now)
6. Done — return to this in Phase 10

### ✅ Success criteria for Step 0.9
- [ ] Overleaf account created
- [ ] Empty IEEE template project exists (for later)

---

## 🧭 STEP 0.10 — Run the "Hello SHAP" Smoke Test

### 🎯 What we want to achieve
**Verify SHAP works on your system** so you don't waste time debugging during Phase 7.

### 🤖 What AI will do for you
- Write a self-contained smoke test script
- Explain what the output should look like

### 👤 What YOU will do

**Option A: Local script**

1. Create the file:
   ```bash
   cat > notebooks/00_shap_smoke_test.py << 'EOF'
   """Smoke test: verify SHAP works on our setup."""
   import numpy as np
   from sklearn.datasets import load_breast_cancer
   from sklearn.ensemble import RandomForestClassifier
   import shap

   # Load sample data
   X, y = load_breast_cancer(return_X_y=True)
   feature_names = load_breast_cancer().feature_names

   # Train simple model
   model = RandomForestClassifier(n_estimators=50, random_state=42)
   model.fit(X, y)
   print(f"[OK] Model trained. Accuracy: {model.score(X, y):.3f}")

   # SHAP test
   explainer = shap.TreeExplainer(model)
   shap_values = explainer.shap_values(X[:5])
   print(f"[OK] SHAP values computed. Shape: {np.array(shap_values).shape}")

   # Generate a simple plot
   shap.summary_plot(shap_values, X[:5], feature_names=feature_names, show=False)
   print("[OK] SHAP summary plot generated.")
   print("\n*** SHAP SMOKE TEST PASSED ***")
   EOF
   ```

2. Run from activated venv:
   ```bash
   python notebooks/00_shap_smoke_test.py
   ```

3. Expected output:
   - Accuracy printed (~0.99)
   - "[OK] SHAP values computed"
   - "[OK] SHAP summary plot generated"
   - Summary plot window might pop up — that's fine

**Option B: In Colab (recommended first time)**

Open Google Colab, ensure runtime is Python 3, then in a cell:
```python
!pip install shap --quiet

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import shap

X, y = load_breast_cancer(return_X_y=True)
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)
print(f"Model accuracy: {model.score(X, y):.3f}")

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X[:5])

shap.summary_plot(shap_values[1], X[:5], feature_names=load_breast_cancer().feature_names)
```

Run it. If you see a beeswarm plot → SHAP works.

### ✅ Success criteria for Step 0.10
- [ ] Smoke test script runs without errors
- [ ] SHAP values computed
- [ ] Plot generated successfully

### 🚨 Troubleshooting
| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'shap'` | Activate venv; `pip install shap==0.43.0` |
| `TreeExplainer` is slow | Reduce `X[:5]` to `X[:3]` |
| Plot doesn't display in terminal | Run in Jupyter (Colab) instead |
| SHAP version conflict | `pip install shap==0.43.0` exact version |

---

## 🧭 STEP 0.11 — Run "Hello LIME" Smoke Test

### 🎯 What we want to achieve
**Verify LIME works on your system**.

### 🤖 What AI will do for you
- Provide LIME smoke test code

### 👤 What YOU will do

Create `notebooks/00_lime_smoke_test.py`:
```bash
cat > notebooks/00_lime_smoke_test.py << 'EOF'
"""Smoke test: verify LIME works on our setup."""
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from lime.lime_tabular import LimeTabularExplainer

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Train model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)
print(f"[OK] Model trained. Accuracy: {model.score(X, y):.3f}")

# LIME setup
explainer = LimeTabularExplainer(
    X,
    feature_names=data.feature_names,
    class_names=data.target_names,
    discretize_continuous=True
)
print("[OK] LimeTabularExplainer created.")

# Explain one instance
exp = explainer.explain_instance(
    X[0],
    model.predict_proba,
    num_features=5
)
print(f"[OK] LIME explanation computed. Top features: {[f for f, w in exp.as_list()]}")

# Save as HTML (optional, for visual check)
exp.save_to_file('notebooks/lime_smoke_test_output.html')
print("[OK] LIME explanation saved to HTML.")
print("\n*** LIME SMOKE TEST PASSED ***")
EOF
```

Run:
```bash
python notebooks/00_lime_smoke_test.py
```

### ✅ Success criteria for Step 0.11
- [ ] LIME explanation computed
- [ ] HTML file generated (you can open it in a browser to view)

---

## 🧭 STEP 0.12 — Initial Backup to Google Drive

### 🎯 What we want to achieve
**Sync all your work to cloud** so nothing is lost if your PC dies.

### 🤖 What AI will do for you
- Suggest backup strategy

### 👤 What YOU will do

**Method A: Manual copy** (simplest)

Open file manager, copy your entire `Thesis_V1/` folder into:
```
Google Drive → Thesis_Backup/
```

**Method B: Using `rclone`** (auto-sync, more advanced — for later)

Skip for now if you don't know rclone.

**Method C: Git + Drive**

Already done — your GitHub repo IS a backup of code/text. Google Drive backup is for **data files** (datasets, models) which are too large for GitHub.

Create the Drive folder structure:
```
/content/drive/MyDrive/Thesis_Backup/
├── Thesis_V1_code_backup/   ← full project folder, but excluding raw data
└── datasets/                 ← raw datasets, downloaded once
    ├── diabetes.csv
    ├── heart.csv
    └── kidney.csv
```

### ✅ Success criteria for Step 0.12
- [ ] Google Drive folder created
- [ ] Project folder copied (excluding `04_data/raw/`)
- [ ] Will download datasets to Drive later (Phase 4)

---

## 🧭 STEP 0.13 — Update README.md with Project Info

### 🎯 What we want to achieve
Create a **professional project README** that explains your thesis (looks good on GitHub).

### 🤖 What AI will do for you
- Generate README template

### 👤 What YOU will do

Replace `README.md` with this content:
```bash
cat > README.md << 'EOF'
# 🎓 Comparative Interpretability Analysis of Ensemble ML Models

> **Thesis Project — BSc in CSE, 6th Semester**

## 📌 Title
**Comparative Interpretability Analysis of Ensemble Machine Learning Models Using SHAP and LIME: A Multi-Disease Tabular Data Study**

## 👥 Team
- **MD. Marajul Haque** (ID: 23701070) — Sole Executor
- Yeasmin Akter Shuchona (22701052) — Co-Author
- Gian Juti Tripura (22701073) — Co-Author
- Samira Oasela Antika (22701043) — Co-Author

## 🎯 Research Goal
Compare SHAP and LIME explanations across ensemble ML models (Random Forest, XGBoost, LightGBM, Stacking) using public disease datasets as benchmarks.

## 🛠️ Tech Stack
- Python 3.10+, scikit-learn, XGBoost, LightGBM
- SHAP, LIME (explainability)
- Google Colab + Kaggle (compute)
- Zotero (references), Overleaf (paper)

## 📊 Datasets
- PIMA Indians Diabetes
- Heart Disease UCI
- Chronic Kidney Disease

## 🗺️ Roadmap
See [`THESIS_ROADMAP.md`](./THESIS_ROADMAP.md) for the complete plan.

## 📜 Status
- [x] Phase 0: Foundation Setup (in progress)
- [ ] Phase 1: Scope Lock
- [ ] Phase 2: Literature Review
- [ ] ... (see roadmap)

## 📂 Folder Structure
See `THESIS_ROADMAP.md` Section 6.

## 📝 License
Academic use only — supervised by [Advisor Name].

---
*Last updated: July 2026*
EOF
```

Commit it:
```bash
git add README.md
git commit -m "Add project README"
git push
```

### ✅ Success criteria for Step 0.13
- [ ] `README.md` updated and visible on GitHub
- [ ] Repo looks professional

---

## 🧭 STEP 0.14 — Phase 0 Completion Checklist

### ✅ Final Verification (run these commands and verify outputs)

```bash
# 1. Folder structure
find . -type d | sort
# Expected: 18 folders listed

# 2. Git status
git status
# Expected: "nothing to commit, working tree clean"

# 3. Virtual environment active
which python
# Expected: shows path inside .venv/

# 4. Libraries installed
python -c "import numpy, pandas, sklearn, xgboost, lightgbm, shap, lime; print('OK')"
# Expected: OK

# 5. Zotero running
# (visual check — Zotero app is open)

# 6. Colab accessible
# (visual check — open colab.research.google.com)

# 7. Smoke tests passed
# (visual confirmation from Steps 0.10 & 0.11)
```

### 🎯 Phase 0 Exit Criteria (ALL must be ✅)

| # | Criterion | Verified |
|---|---|---|
| 1 | All 18 folders exist | [ ] |
| 2 | Git repo initialized + pushed to GitHub (private) | [ ] |
| 3 | `.gitignore` configured | [ ] |
| 4 | Python 3.10+ installed in `.venv` | [ ] |
| 5 | All libraries from `requirements.txt` installed | [ ] |
| 6 | `NOTES.md` and `README.md` exist | [ ] |
| 7 | Google Colab + Drive mounted successfully | [ ] |
| 8 | Kaggle account + API token working | [ ] |
| 9 | Zotero installed + Better BibTeX + 5 papers saved | [ ] |
| 10 | Overleaf account created (template project exists) | [ ] |
| 11 | SHAP smoke test passed | [ ] |
| 12 | LIME smoke test passed | [ ] |
| 13 | Google Drive backup folder created | [ ] |
| 14 | README.md committed to GitHub | [ ] |

### 🚨 If any criterion is ❌
- Re-read the relevant step
- Run the troubleshooting table
- Ask AI (paste error message here)
- Once all ✅, **move to Phase 1: Topic & Scope Lock**

---

## 📌 PHASE 0 — SUMMARY

### What you achieved today
- ✅ Built a **professional workspace** (no more file chaos)
- ✅ Set up **version control** (Git + GitHub) — code is backed up
- ✅ Installed **all required tools** — never worry about "module not found" again
- ✅ Configured **two free GPU platforms** (Colab + Kaggle)
- ✅ Set up **reference management** (Zotero) — you're ready to read papers
- ✅ **Verified SHAP & LIME work** — no surprises during Phase 7

### Time spent
~5-7 hours (one focused day, or split across two)

### What you saved in NOTES.md
(Should now contain:)
- Links to all accounts
- Your library versions
- Any issues you hit + how you fixed them

---

## 🚀 NEXT: Phase 1 — Topic & Scope Lock

Once ALL Phase 0 exit criteria are ✅, ask me: **"Create Phase 1"** and I'll build the detailed phase document for:
- Writing 5 Research Questions
- Locking datasets, models, metrics
- Advisor approval meeting prep

---

## 🧠 CHALLENGES YOU MIGHT HIT + HOW TO ASK AI FOR HELP

| Situation | What to paste to me |
|---|---|
| Terminal error during setup | The full error message + the command you ran |
| "Module not found" after install | The import line + confirmation that venv is active |
| Git push rejected | The exact error message |
| Kaggle API permission denied | Output of `ls -la ~/.kaggle/` |
| Zotero Better BibTeX not appearing | Screenshot of Add-ons page |
| Colab disconnecting | Your current Colab cell + error |

---

**🎉 Congratulations on completing Phase 0! Phase 0 is boring but CRITICAL. Most thesis failures happen because students skip setup.**

**Reply when ready: "Create Phase 1"** 🚀
