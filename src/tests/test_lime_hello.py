"""Step 0.11 - Hello LIME smoke test.

Purpose: confirm LIME is installed correctly and can explain a single
prediction from a tiny toy classifier. Companion to test_shap_hello.py.

Run: source .venv/bin/activate && python src/tests/test_lime_hello.py
"""
from __future__ import annotations

import sys
from importlib.metadata import version
from pathlib import Path

import numpy as np
import lime
import lime.lime_tabular
from sklearn.ensemble import RandomForestClassifier

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "results" / "phase_00"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> int:
    print("=" * 60)
    print("Step 0.11 - Hello LIME smoke test")
    print("=" * 60)
    print(f"  lime version: {version('lime')}")

    # 1. Toy dataset - same structure as the SHAP test for parity.
    rng = np.random.default_rng(seed=42)
    X = rng.normal(size=(80, 4))
    y = (X[:, 0] + 0.5 * X[:, 1] > 0).astype(int)

    feature_names = ["feat_A", "feat_B", "feat_C", "feat_D"]
    class_names = ["class_0", "class_1"]

    # 2. Train RF on the toy data.
    print("\n[1] Training RandomForestClassifier ...")
    clf = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=1)
    clf.fit(X, y)
    train_acc = clf.score(X, y)
    print(f"    Train accuracy: {train_acc:.3f}")

    # 3. Build a LIME Tabular explainer.
    print("\n[2] Building LimeTabularExplainer ...")
    explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=X,
        feature_names=feature_names,
        class_names=class_names,
        mode="classification",
        random_state=42,
    )
    print(f"    explainer type: {type(explainer).__name__}")

    # 4. Explain the first sample (instance 0).
    print("\n[3] Explaining instance 0 ...")
    instance = X[0]
    pred = clf.predict(instance.reshape(1, -1))[0]
    proba = clf.predict_proba(instance.reshape(1, -1))[0]
    print(f"    True label: {y[0]} | Predicted: {pred} | Proba: {proba}")

    exp = explainer.explain_instance(
        data_row=instance,
        predict_fn=clf.predict_proba,
        num_features=4,
        num_samples=200,  # keep small for fast smoke test
    )

    # 5. Inspect the explanation list - LIME returns (feature_desc, weight) tuples.
    as_list = exp.as_list()
    print("\n[4] LIME feature attributions for instance 0:")
    for desc, weight in as_list:
        print(f"    {weight:+.4f}  {desc}")

    # 6. Save the LIME figure as HTML (native LIME output) and as PNG via matplotlib.
    html_path = OUT_DIR / "lime_hello_explanation.html"
    exp.save_to_file(str(html_path))
    print(f"\n[5] Saved HTML: {html_path}  ({html_path.stat().st_size} bytes)")

    png_path = OUT_DIR / "lime_hello_explanation.png"
    try:
        # lime >=0.2 supports as_pyplot_to_file(); fall back gracefully.
        if hasattr(exp, "as_pyplot_to_file"):
            exp.as_pyplot_to_file(str(png_path), figsize=(7, 4))
        else:
            import matplotlib.pyplot as plt
            fig = exp.as_pyplot_figure(figsize=(7, 4))
            fig.tight_layout()
            fig.savefig(png_path, dpi=120, bbox_inches="tight")
            plt.close(fig)
        print(f"    Saved PNG:  {png_path}  ({png_path.stat().st_size} bytes)")
    except Exception as exc:
        print(f"    [WARN] PNG export failed (HTML still saved): {exc}")

    # 7. Sanity checks.
    print("\n[6] Sanity checks:")
    html_ok = html_path.exists() and html_path.stat().st_size > 1000
    list_ok = len(as_list) >= 2  # LIME returns up to num_features tuples
    # Top-weighted feature for instance 0 should be A or B (those are real drivers).
    top_feature_desc = max(as_list, key=lambda kv: abs(kv[1]))[0]
    top_ok = ("feat_A" in top_feature_desc) or ("feat_B" in top_feature_desc)
    print(f"    HTML file present (>1KB): {html_ok}")
    print(f"    Explanation list has >=2 entries: {list_ok}")
    print(f"    Top feature is A or B: {top_ok}  (top: '{top_feature_desc}')")

    print("\n" + "=" * 60)
    if train_acc >= 0.9 and html_ok and list_ok and top_ok:
        print("PASS Step 0.11 - LIME works end-to-end.")
        print(f"   HTML: {html_path}")
        if png_path.exists():
            print(f"   PNG:  {png_path}")
        return 0
    print("FAIL Step 0.11 - see warnings above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
