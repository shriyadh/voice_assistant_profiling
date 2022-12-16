import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv(r"C:\Users\shriy\Downloads\Sankey - Sheet1.csv")

df1 = df.groupby(['Questions', 'Persona'])['Tags'].count().reset_index()
df1.columns = ["source" , "target", "value"]

df2 = df.groupby(['Persona', 'Tags'])['Questions'].count().reset_index()
df2.columns = ["source" , "target", "value"]

links = pd.concat([df1,df2],axis=0)


unique_source_target = list(pd.unique(links[['source', 'target']].values.ravel('K')))
mapping_dict = {k: v for v, k in enumerate(unique_source_target)}
     
links['source'] = links['source'].map(mapping_dict)
links['target'] = links['target'].map(mapping_dict)

links_dict = links.to_dict(orient='list')   

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = unique_source_target,
      color = "blue"
    ),
    link = dict(
      source = links_dict["source"],
      target = links_dict["target"],
      value = links_dict["value"]
  ))])
     

fig.update_layout(title_text="Persona", font_size=10)
fig.show()
