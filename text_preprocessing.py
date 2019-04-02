from umap import UMAP
from sklearn.datasets import load_digits
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



digits = load_digits()

embedding = UMAP(n_neighbors=10, min_dist=0.001).fit_transform(digits.data)
output = pd.DataFrame(embedding,columns=('x','y'))
