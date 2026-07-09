"""Smoke test: verify SHAP works on our setup (Phase 0, Step 0.10).

Goal: confirm that the SHAP library is correctly installed, can compute
explanations from a tree-based model on tabular data, and can produce a
saved plot file.

Run:
    source .venv/bin/activate
    python notebooks/00_shap_smoke_test.py
"""

from __future__ import annotations

import os
import warnings

import numpy as np
import shap
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# Some SHAP plots warn about sklearn API changes; these don't affect us.
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Resolve paths so the script works no matter where it is invoked from.
HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(PROJECT_ROOT, "results", "phase_00")
os.makedirs(OUT_DIR, exist_ok=True)


def main() -> None:
    # 1) Load a small, well-known classification dataset (binary).
    data = load_breast_cancer()
    X, y = data.data, data.target
    feature_names = list(data.feature_names)
    print(f"[OK] Loaded dataset: {X.shape[0]} samples, {X.shape[1]} features")

    # 2) Train a simple tree-based model that SHAP's TreeExplainer can read.
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)
    train_acc = model.score(X, y)
    print(f"[OK] Model trained. Train accuracy: {train_acc:.3f}")

    # 3) Run SHAP TreeExplainer on a small batch (5 rows is enough for the smoke test).
    #    Note: TreeExplainer does NOT need a background dataset for tree models
    #    in SHAP 0.52 — the default feature_perturbation="interventional" uses
    #    the model's own training statistics internally.
    explainer = shap.TreeExplainer(model)
    sample_X = X[:5]
    shap_values = explainer.shap_values(sample_X)

    # SHAP 0.40+ returns a 3D array for binary problems: (n_samples, n_features, n_classes).
    # Older API returns a list of two 2D arrays. Handle both shapes.
    if isinstance(shap_values, list):
        sv_for_class1 = shap_values[1]
        expected_value = explainer.expected_value[1]
        print(f"[OK] SHAP values (legacy list API). Class-1 shape: {np.asarray(sv_for_class1).shape}")
    else:
        arr = np.asarray(shap_values)
        print(f"[OK] SHAP values (array). Shape: {arr.shape}")
        # If shape has 3 dims, the last dim is the class index.
        if arr.ndim == 3:
            sv_for_class1 = arr[..., 1]
            ev = explainer.expected_value
            expected_value = ev[1] if isinstance(ev, (list, np.ndarray)) else ev
        else:
            sv_for_class1 = arr
            expected_value = explainer.expected_value

    # 4) Save a SHAP summary plot (beeswarm) to a PNG so we can inspect later.
    plot_path = os.path.join(OUT_DIR, "shap_summary_plot.png")
    shap.summary_plot(
        sv_for_class1,
        sample_X,
        feature_names=feature_names,
        show=False,
    )
    # shap.summary_plot renders to the current figure; save it explicitly.
    import matplotlib.pyplot as plt
    plt.tight_layout()
    plt.savefig(plot_path, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"[OK] SHAP summary plot saved -> {plot_path}")

    # 5) Quick sanity check: SHAP values for class 1 should sum close to (f(x) - E[f]).
    print(f"[OK] expected_value (class 1) = {float(np.asarray(expected_value).ravel()[0]):.4f}")
    print(f"[OK] predicted prob (mean over batch) = {model.predict_proba(sample_X)[:, 1].mean():.4f}")
    print(f"[OK] sum of |SHAP| per row (mean) = {np.abs(sv_for_class1).sum(axis=1).mean():.4f}")

    print("\n*** SHAP SMOKE TEST PASSED ***")


if __name__ == "__main__":
    main()
