import plotly.express as px
import pandas as pd
import random

df = pd.DataFrame({'X': [random.random() for _ in range(100)],
                   'Y': [random.random() for _ in range(100)],
                   'Size': [random.randint(1, 10) for _ in range(100)]})

fig = px.scatter(df, x='X', y='Y', size='Size')
fig.show()