import plotly.express as px
import pandas as pd
import random

df = pd.DataFrame({'X': [random.random() for _ in range(100)],
                   'Y': [random.random() for _ in range(100)],
                   'Z': [random.random() for _ in range(100)],
                   'Size': [random.randint(1, 10) for _ in range(100)]})

fig = px.scatter_3d(df, x='X', y='Y', z='Z', size='Size')
fig.show()
