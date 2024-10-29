import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv("https://github.com/appmarestaing/image_host/blob/main/visited_states.csv?raw=true")

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z = df['number students'].astype(float),
    locationmode = 'USA-states',
    colorscale = 'turbid', 
    colorbar_title = 'Most to least visited states'
))

fig.update_layout(
    title_text="give your map a title",
    geo_scope="usa"
)

fig.show()