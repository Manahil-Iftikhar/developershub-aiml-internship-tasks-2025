"""Rebuild the README figure from scikit-learn's bundled Iris dataset."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

ROOT = Path(__file__).resolve().parents[1]
(ROOT / 'artifacts').mkdir(exist_ok=True)
iris = load_iris(as_frame=True)
frame = iris.frame.copy()
frame['species'] = frame['target'].map(dict(enumerate(iris.target_names)))
sns.set_theme(style='whitegrid', palette='colorblind')
fig, ax = plt.subplots(figsize=(9, 4.8), facecolor='white')
sns.scatterplot(data=frame, x='petal length (cm)', y='petal width (cm)',
                hue='species', style='species', s=65, alpha=0.85, ax=ax)
ax.set_title('Iris: how petal measurements separate species', loc='left', pad=18)
ax.legend(title='Species', loc='upper left', frameon=True)
fig.text(0.11, 0.02, '150 observations · 50 per species · scikit-learn reference dataset',
         fontsize=9, color='#4a5d69')
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(ROOT / 'assets/iris-petals.svg', bbox_inches='tight')
fig.savefig(ROOT / 'artifacts/iris-preview.png', dpi=150, bbox_inches='tight')
plt.close(fig)
