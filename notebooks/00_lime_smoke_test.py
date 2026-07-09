"""Smoke test: verify LIME works on our setup (Phase 0, Step 0.11).

Goal: confirm that the LIME library is correctly installed, can build a
tabular explainer, can explain a prediction, and can save results to
HTML for visual inspection.

Run:
    source .venv/bin/activate
    python notebooks/00_lime_smoke_test.py
"""

from __future__ import annotations

import os
import warnings

import numpy as np
from lime.lime_tabular import LimeTabularExplainer
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# LIME + sklearn emit a few deprecation warnings; silence the noisy ones.
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Resolve paths so the script works no matter where it is invoked from.
HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(PROJECT_ROOT, "results", "phase_00")
os.makedirs(OUT_DIR, exist_ok=True)


def main() -> None:
    # 1) Load a small binary classification dataset.
    data = load_breast_cancer()
    X, y = data.data, data.target
    feature_names = list(data.feature_names)
    class_names = list(data.target_names)
    print(f"[OK] Loaded dataset: {X.shape[0]} samples, {X.shape[1]} features")

    # 2) Train the same kind of tree-based model we'll use in the real thesis.
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)
    print(f"[OK] Model trained. Train accuracy: {model.score(X, y):.3f}")

    # 3) Build a LIME tabular explainer.
    #    - discretize_continuous=True: bin features (LIME's "perturbation trick")
    #    - random_state=42: reproducibility (LIME has internal randomness)
    explainer = LimeTabularExplainer(
        training_data=X,
        feature_names=feature_names,
        class_names=class_names,
        discretize_continuous=True,
        random_state=42,
    )
    print("[OK] LimeTabularExplainer created.")

    # 4) Explain instance #0 (use explicit num_samples for clarity).
    np.random.seed(42)  # LIME 0.2 uses numpy's global RNG internally
    exp = explainer.explain_instance(
        data_row=X[0],
        predict_fn=model.predict_proba,
        num_features=5,
        num_samples=5000,  # default value; explicit for documentation
    )
    top5 = exp.as_list()
    print(f"[OK] LIME explanation computed. Top 5 features (class 1):")
    for fname, weight in top5:
        print(f"        {fname:<55s} {weight:+.4f}")

    # 5) Save the explanation as an HTML file you can open in a browser.
    html_path = os.path.join(OUT_DIR, "lime_explanation_instance0.html")
    exp.save_to_file(html_path)
    print(f"[OK] LIME explanation saved -> {html_path}")

    # 6) Stability sanity check: reseed and explain the SAME instance again,
    #    then check whether the top-1 feature is stable.
    #    NOTE: LIME explanations are inherently noisy — instability is one of the
    #    metrics we'll formally measure in Phase 8 (Stability). Don't expect
    #    perfect reproducibility here; we just want to confirm two runs both run.
    np.random.seed(42)
    exp2 = explainer.explain_instance(
        data_row=X[0],
        predict_fn=model.predict_proba,
        num_features=5,
        num_samples=5000,
    )
    top1_a = top5[0][0]
    top1_b = exp2.as_list()[0][0]
    if top1_a == top1_b:
        print(f"[OK] Stability check: top-1 feature stable across runs ({top1_a})")
    else:
        print(f"[INFO] Top-1 feature varies across runs ({top1_a!r} vs {top1_b!r}).")
        print("       This is expected — LIME instability is a known property and")
        print("       will be formally measured as the 'Stability' metric in Phase 8.")

    # 7) Quick stats on the prediction that was explained.
    pred_proba = model.predict_proba(X[:1])[0]
    pred_class = class_names[int(np.argmax(pred_proba))]
    print(f"[OK] Predicted class for X[0]: {pred_class}  (p={pred_proba[int(np.argmax(pred_proba))]:.3f})")
    print(f"[OK] LIME-local prediction (class 1 probability): {exp.predict_proba[1]:.3f}")

    print("\n*** LIME SMOKE TEST PASSED ***")


if __name__ == "__main__":
    main()
