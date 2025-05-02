### quiero simular datos de una funcion log normal y hacer un histograma
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from random import random, seed
import math
import scipy.stats as stats

seed(1)


mu = 0.5
sigma = 0.5
n = 10000
x = np.random.lognormal(mu, sigma, n)
plt.figsize(10, 6)
sns.histplot(x, bins=30, kde=True, color='blue', alpha=0.5)
plt.title('Histograma de datos log-normales')
plt.show()


###

x = np.random.normal(mu, sigma, n)

