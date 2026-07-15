"""Step 0.10 - Hello SHAP smoke test.

Purpose: confirm SHAP is installed correctly and can produce a beeswarm
plot from a tiny toy dataset. This is the simplest possible end-to-end
SHAP pipeline - written BEFORE we touch real medical datasets so that
any install/integration issues surface here, not during thesis work.

Run: source .venv/bin/activate && python src/tests/test_shap_hello.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import shap
from sklearn.ensemble import RandomForestClassifier

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "results" / "phase_00"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> int:
    print("=" * 60)
    print("Step 0.10 - Hello SHAP smoke test")
    print("=" * 60)

    # 1. Toy dataset - 80 samples, 4 features, binary target.
    rng = np.random.default_rng(seed=42)
    X = rng.normal(size=(80, 4))
    # Make target correlated with features 0 and 1 (so SHAP has something
    # real to attribute).
    y = (X[:, 0] + 0.5 * X[:, 1] > 0).astype(int)

    feature_names = ["feat_A", "feat_B", "feat_C", "feat_D"]
    X_df = np.zeros((80, 4), dtype=float)
    X_df[:, 0] = X[:, 0]
    X_df[:, 1] = X[:, 1]
    X_df[:, 2] = X[:, 2]
    X_df[:, 3] = X[:, 3]

    # 2. Train a small Random Forest.
    print("\n[1] Training RandomForestClassifier on toy data ...")
    clf = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=1)
    clf.fit(X_df, y)
    train_acc = clf.score(X_df, y)
    print(f"    Train accuracy: {train_acc:.3f}")

    # 3. Compute SHAP values with TreeExplainer (fast, exact for trees).
    print("\n[2] Computing SHAP values with TreeExplainer ...")
    explainer = shap.TreeExplainer(clf)
    shap_values = explainer.shap_values(X_df)

    # For binary classification, TreeExplainer returns shape (n, f, 2) on
    # some versions and a list of two (n, f) arrays on others. Normalize
    # to a single (n, f) array = class-1 SHAP values.
    if isinstance(shap_values, list):
        sv = shap_values[1]
    else:
        arr = np.asarray(shap_values)
        if arr.ndim == 3:
            sv = arr[:, :, 1]
        else:
            sv = arr
    print(f"    SHAP values shape: {sv.shape}  (expected: (80, 4))")

    # 4. Verify the SHAP values look sensible - top features by mean |SHAP|
    # should be feat_A and feat_B (we made y depend on them).
    mean_abs = np.abs(sv).mean(axis=0)
    ranking = sorted(zip(feature_names, mean_abs), key=lambda t: -t[1])
    print("\n[3] Mean |SHAP| per feature (higher = more important):")
    for name, val in ranking:
        print(f"    {name:8s}  {val:.4f}")

    top1 = ranking[0][0]
    top1_ok = top1 in ("feat_A", "feat_B")
    if not top1_ok:
        print(f"\n[WARN] Expected feat_A or feat_B on top, got '{top1}'.")

    # 5. Save the beeswarm plot (the canonical SHAP summary).
    print("\n[4] Saving beeswarm plot ...")
    try:
        import matplotlib.pyplot as plt
        shap.summary_plot(sv, X_df, feature_names=feature_names,
                          show=False, plot_size=(7, 4))
        out_path = OUT_DIR / "shap_hello_beeswarm.png"
        plt.tight_layout()
        plt.savefig(out_path, dpi=120, bbox_inches="tight")
        plt.close()
        print(f"    Saved: {out_path}  ({out_path.stat().st_size} bytes)")
    except Exception as exc:
        print(f"    [WARN] Beeswarm plot failed: {exc}")
        return 2

    # 6. Final verdict.
    print("\n" + "=" * 60)
    if train_acc >= 0.9 and top1_ok and out_path.exists():
        print("PASS Step 0.10 - SHAP works end-to-end.")
        print(f"   Plot: {out_path}")
        return 0
    print("FAIL Step 0.10 - see warnings above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
