import pandas as pd 
from IPython.display import display
import plotly.express as px

table = pd.read_csv("cancellations.csv")
table = table.drop("CustomerID", axis=1)

#display(table.groupby("duracao_contrato").mean(numeric_only=True))

#for column in table.columns:
    #graphic = px.histogram(table, x=column, color="cancelou", width=600)
    #graphic.show()

table = table[table["duracao_contrato"] != "Monthly"]
table = table[table["ligacoes_callcenter"] < 5]
table = table[table["dias_atraso"] <= 20]
table = table[table["idade"] <= 50]

display(table["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

