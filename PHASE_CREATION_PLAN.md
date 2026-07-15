# 📝 PHASE CREATION PLAN
## Meta-Document: How & Why Each Phase Document Will Be Created

> **Purpose**: This file tracks the **process** of creating each phase's detailed `.md` document — not the content of the phases themselves. It exists so that:
> 1. **No context is lost** between sessions, even if the AI is "reset"
> 2. **The order and rationale** for each phase doc is preserved
> 3. **The user's stated reasons** ("why I told you to create the phase") are documented
> 4. **Status tracking** — which phase docs are done, pending, or in-progress

> **Maintainer**: AI Assistant (Claude Opus 4.8) creates phase docs → User updates status → AI references this file when context is unclear

> **Created**: July 9, 2026

---

## 🎯 CORE WORKFLOW RULE (User-Defined)

> **"I will use you (Claude Opus 4.8) for everything. But if you dive in one phase for longer, you may forget and don't understand if I tell you to create next phase detail. So I want you first to create a phase creating plan doc that you write all the phases we will create one after another and also you remember why I told you to create the phase."**

**Translation**:
- ✅ User wants ONE AI (Claude Opus 4.8) for everything
- ✅ User is aware of context-window limits
- ✅ User wants pre-planned phase creation order with rationale preserved
- ✅ This file solves context loss between sessions

---

## 📋 PHASE CREATION ORDER

The 11 phases from `THESIS_ROADMAP.md` §4 will be converted into **detailed `.md` documents** in this order:

| # | Phase Doc Filename | Phase Name | User's Reason to Create | Status |
|---|---|---|---|---|
| 0 | `phase_00_FOUNDATION.md` | Foundation & Tooling | First phase; setup is the foundation | ✅ Created (July 7) |
| 1 | `phase_01_SCOPE_LOCK.md` | Topic Finalization & Scope Lock | Required before any work; locks RQs | ✅ Created (July 9) |
| 2 | `phase_02_LITERATURE_REVIEW.md` | Literature Review | Largest research phase; needs detail | ⏳ Pending |
| 3 | `phase_03_PROPOSAL.md` | Proposal Writing & Defense | First major writing milestone | ⏳ Pending |
| 4 | `phase_04_EDA.md` | Data Acquisition & EDA | Before any modeling work | ⏳ Pending |
| 5 | `phase_05_PREPROCESSING.md` | Data Preprocessing Pipeline | Must come before model training | ⏳ Pending |
| 6 | `phase_06_MODELS.md` | Model Development | Core engineering work | ⏳ Pending |
| 7 | `phase_07_XAI.md` | XAI Implementation (SHAP + LIME) | Core research novelty | ⏳ Pending |
| 8 | `phase_08_COMPARISON.md` | Comparative Analysis (NOVELTY) | Where research contribution lives | ⏳ Pending |
| 9 | `phase_09_THESIS_WRITING.md` | Thesis Document Writing | Major writing milestone | ⏳ Pending |
| 10 | `phase_10_PAPER.md` | Journal Paper Writing & Submission | University requires publication | ⏳ Pending |
| 11 | `phase_11_REVISION_DEFENSE.md` | Revisions, Defense & Final Submission | Last phase; closes the loop | ⏳ Pending |

**Status legend**: ✅ Created | ⏳ Pending | 🚧 In Progress | ❌ Skipped

---

## 🧠 WHY EACH PHASE DOC WILL BE CREATED (User's Reasoning)

> These are the **stated or implicit reasons** the user wants each phase document generated as a standalone, detailed `.md` file.

### Why Detailed Per-Phase `.md` Files?
*(User's explicit feedback captured from previous conversations)*

1. **"each phase it short and not so detailed"** → Original roadmap was too high-level
2. **"i want detailed of each phase (each phase in .md file)"** → User wants one file per phase
3. **"so how each phase you should write: you write the phase into many steps and each step you write in detailed what we are going to do with everything"** → Step-by-step granularity
4. **"and you may also write like this what i have to do (i mean human), what ai have to do for the step or combined"** → Clear human/AI division per step
5. **"as this (4.PHASE ROADMAP (11 PHASES)) build by you in one turn so you may made mistake (i am not sure), so now the clear phase detailed steps you will create, you should make it robust and correct with detailed way"** → Robustness required; verify correctness
6. **"i will tell you one by one to create for all other phases"** → User controls the creation pace (on-demand, not auto-generated)

### Per-Phase Creation Reasons

| Phase | Specific Reason |
|---|---|
| **Phase 0** | Set up tools; verified in `phase_00_FOUNDATION.md` (1064 lines, 14 steps) |
| **Phase 1** | Cannot write RQs without knowing what the user has chosen; Phase 1 locks the scope for ALL future phases |
| **Phase 2** | Literature review is the most content-heavy phase; needs structured daily tasks; 25-30 papers to track |
| **Phase 3** | Proposal is the contract with advisor; needs detailed writing + defense prep; one-shot creation insufficient |
| **Phase 4** | EDA on 3 different datasets needs per-dataset guidance; each dataset has different quirks (missing values in CKD, etc.) |
| **Phase 5** | Preprocessing pipeline is the foundation for ALL modeling; needs bulletproof code template |
| **Phase 6** | Model training has many configurations (RF, XGBoost, LightGBM, Stacking); each needs separate detailed sub-steps |
| **Phase 7** | SHAP and LIME each have multiple visualization types; case studies need structured selection |
| **Phase 8** | **The novelty phase** — must define comparison metrics rigorously; statistical analysis needs careful explanation |
| **Phase 9** | Thesis writing is 30+ pages; chapter-by-chapter breakdown essential; thesis-specific (university format) |
| **Phase 10** | Journal paper has DIFFERENT format from thesis; needs journal-specific guidance (IEEE Access template, cover letter, response to reviewers) |
| **Phase 11** | Reviewer responses require careful diplomacy; thesis defense has its own slide prep |

---

## 🔄 THE PHASE CREATION TRIGGER PROTOCOL

> **This is the contract between User and AI for phase doc creation.**

### How User Triggers Phase Doc Creation

User pastes one of these exact phrases:

| Trigger Phrase | What AI Does |
|---|---|
| `"Create Phase [N]"` | Creates `phase_0N_[NAME].md` with full detailed steps |
| `"Make Phase [N]"` | Same as above |
| `"Next phase"` | Creates the next sequential phase doc |
| `"Generate phase [N] doc"` | Same as above |
| `"Continue"` | Creates next pending phase doc |

### What AI Does on Each Trigger

1. **Read** `THESIS_ROADMAP.md` §4 (brief phase overview)
2. **Read** `AGENT.md` §1-6 (current user context)
3. **Read** `AGENT.md` §8 (current progress)
4. **Read** `phase_00_FOUNDATION.md` (reference for format/depth)
5. **Read** `PHASE_CREATION_PLAN.md` §"Why Per-Phase Creation Reasons" (this file)
6. **Generate** `phase_0N_[NAME].md` with:
   - Phase goal (1-2 sentences)
   - Time estimate
   - Step-by-step breakdown (10-20 steps typical)
   - For each step:
     - 🎯 Goal
     - 🤖 What AI does
     - 👤 What YOU do
     - ✅ Success criteria
     - 🚨 Troubleshooting
     - Time estimate
7. **Update** this file's Status table (✅ Created for that phase)
8. **Append** new decision to `AGENT.md` §11 (Decisions Log)
9. **Confirm** to user with file path + line count + "ready to execute"

### Format Reference (from Phase 0)

Phase 0 used this format (all subsequent phases should follow):
- Step index at top
- Time estimates per step
- 3-character emoji sections (🎯 🤖 👤 ✅ 🚨)
- Code blocks for commands/scripts
- Success criteria as checkboxes
- Troubleshooting tables

---

## 📊 PHASE DOC FILE FORMAT TEMPLATE

To be used by AI for every phase doc:

```markdown
# 📘 PHASE [N] — [Name] (Detailed)

> **Phase Goal**: [1-2 sentences]

> **Time Estimate**: [X hours/days]

> **Exit Criteria**: [List of conditions that must be true to leave this phase]

---

## 📑 STEP INDEX

| Step | Title | Time |
|---|---|---|---|
| [N.1] | [First step] | [X min] |
| ... | ... | ... |

**Total time**: [X hours]

---

## 🧭 STEP [N.1] — [Title]

### 🎯 What we want to achieve
[1-2 sentences]

### 🤖 What AI will do for you
[Bulleted list]

### 👤 What YOU will do
1. [Step 1]
2. [Step 2]
[Code blocks if applicable]

### ✅ Success criteria for Step [N.1]
- [ ] Criterion 1
- [ ] Criterion 2

### 🚨 Troubleshooting
| Problem | Fix |
|---|---|
| [Problem] | [Fix] |

---

## 📌 PHASE [N] — SUMMARY

### What you achieved
- ✅ [Achievement 1]
- ✅ [Achievement 2]

### Time spent
[Estimated]

### What's next
[Reference to next phase]

---

## 🚀 NEXT: Phase [N+1] — [Name]

Once ALL exit criteria are ✅, ask me: **"Create Phase [N+1]"**
```

---

## 📏 QUALITY STANDARDS FOR EVERY PHASE DOC

> These rules are mandatory. AI must verify before delivering any phase doc.

### Content Requirements
| # | Rule |
|---|---|
| 1 | Length: 500-1500 lines (detailed but not bloated) |
| 2 | Step count: 8-20 steps per phase |
| 3 | Every step has: 🎯 Goal, 🤖 AI does, 👤 YOU do, ✅ Success, 🚨 Troubleshooting |
| 4 | Every step has time estimate |
| 5 | Code blocks where applicable, fully working (no TODOs) |
| 6 | At least 1 troubleshooting table per step |
| 7 | References to specific file paths with backticks |
| 8 | AI-usage section per phase (which AI tools help at each step) |

### Verification Before Delivery
AI must check:
- [ ] All user constraints respected (read `AGENT.md` §6)
- [ ] No fabricated citations
- [ ] No medical/clinical claims (CS focus only)
- [ ] Bash commands work on Linux (user's OS)
- [ ] Code matches user's skill level (Intermediate Python)
- [ ] No references to AI infra/policies (per project rules)
- [ ] Ending includes "Create Phase [N+1]" trigger phrase

### Tone Requirements
- Professional, concise, direct
- Encouraging but not patronizing
- Treats user as capable beginner learning to expert
- Bilingual friendly (user's English is fluent but not native)

---

## 🔗 INTER-PHASE DEPENDENCIES

> What each phase produces that the next phase consumes.

| Phase | Produces | Consumed By |
|---|---|---|
| **Phase 0** | Working environment + accounts | All subsequent phases |
| **Phase 1** | `01_proposal/rq_scope.md` (RQs, hypotheses, metrics list) | Phase 2 (lit review focus), Phase 3 (proposal), Phase 8 (metrics design) |
| **Phase 2** | `02_literature/literature_matrix.xlsx`, `02_literature/references.bib` | Phase 3 (proposal lit review section), Phase 9 (thesis lit review), Phase 10 (paper related work) |
| **Phase 3** | `01_proposal/Final_Proposal.pdf` | Advisor approval → unlocks Phase 4+ |
| **Phase 4** | `04_data/raw/*.csv`, `04_data/EDA_REPORT.md` | Phase 5 (preprocessing input) |
| **Phase 5** | `04_data/processed/*.csv`, `src/preprocessing.py` | Phase 6 (model training input) |
| **Phase 6** | `05_models/saved_models/*.pkl`, `05_models/results.csv` | Phase 7 (XAI input models), Phase 9 (Results chapter), Phase 10 (Paper Results section) |
| **Phase 7** | `06_xai_exploration/{shap,lime}_outputs/` | Phase 8 (comparison input), Phase 9 (Results chapter figures), Phase 10 (Paper figures) |
| **Phase 8** | `08_comparison/results/comparison_table.csv`, `08_comparison/figures/` | Phase 9 (Discussion chapter), Phase 10 (Paper Discussion) |
| **Phase 9** | `09_thesis/Thesis_Final.pdf` | Defense prep (Phase 11), source material for Phase 10 |
| **Phase 10** | `10_paper/IEEE_Access_Paper_v1.pdf` | Submitted to journal → enters review cycle |
| **Phase 11** | Defended thesis + accepted paper | Graduation, publication record |

**🔑 Critical insight**: If any upstream deliverable is missing, downstream phases will stall. Phase discipline is mandatory.

---

## 📊 PROGRESS TRACKER

> Updated by AI after each phase doc creation.

### Phase Docs Created
| # | File | Lines | Created Date | Status |
|---|---|---|---|---|
| 0 | `phase_00_FOUNDATION.md` | 1064 | 2026-07-07 | ✅ Complete |
| 1 | `phase_01_SCOPE_LOCK.md` | — | — | ⏳ Pending |

### Phase Docs In Progress
*(None currently)*

### Phase Docs Pending
*(See Status table at top)*

---

## 🛡️ CONTEXT-LOSS PREVENTION PROTOCOL

> Specific steps AI should take when context window is at risk or session is long.

### When AI suspects context loss (conversation is very long):
1. **Re-read** this file (`PHASE_CREATION_PLAN.md`)
2. **Re-read** `AGENT.md` §1-6, §8
3. **Ask user** to confirm current phase status before generating new content
4. **Quote back** the relevant existing phase doc format

### When user starts new session:
1. User pastes this file's content (or just the Status table) into new chat
2. AI reads and resumes phase creation
3. AI should NEVER ask user to re-explain topic, datasets, or constraints (all in `AGENT.md`)

### Emergency: If user pastes only "Create Phase 5":
1. AI must read `THESIS_ROADMAP.md` §4 for Phase 5 details
2. AI must read `AGENT.md` §1-6 for user context
3. AI must read `phase_00_FOUNDATION.md` for format reference
4. AI must read THIS file's "Why Per-Phase Creation Reasons" section
5. Then create Phase 5 with full context

---

## 🎯 CRITICAL REMINDERS FOR AI (Self-Reminders)

These are the user's explicit preferences. **Do not violate these**.

### User Says
- ✅ "I will use you for everything"
- ✅ "Phase discipline is critical"
- ✅ "Detailed step-by-step required"
- ✅ "Show what human does vs what AI does"
- ✅ "I will tell you one by one" — on-demand creation
- ❌ Never fabricate citations or papers
- ❌ Never make medical claims (CS-only framing)
- ❌ Never promise paper acceptance or funding
- ❌ Never skip verifying Phase 0 outputs before generating Phase 1

### User's Tone Preferences
- Professional, direct
- Tables for comparisons
- Code blocks for commands
- Short forward-looking sentences at end
- No "Want me to..." questions

---

## 📝 CHANGE LOG

| Date | Change | Author |
|---|---|---|
| 2026-07-09 | Created phase creation plan document | Claude Opus 4.8 (per user request) |
| 2026-07-09 | Status updated: Phase 0 marked ✅, others ⏳ | Claude Opus 4.8 |

---

## 🚀 IMMEDIATE NEXT ACTION

**User executes Phase 0 setup** using `phase_00_FOUNDATION.md` as the guide.

When user returns:
- They will say "Create Phase 1" (or similar)
- AI will generate `phase_01_SCOPE_LOCK.md`
- This file's status table will be updated
- `AGENT.md` §11 will get new decision entry

---

**🎯 This file is now the AI's "memory aid" for the phase-creation process. Without it, AI loses track of WHY phase docs are being created in this specific order with this specific format. Keep it updated.**