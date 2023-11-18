from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px

def generate_graph(p):
    newDict = {}
    newDict['Assignments'] = [i for i in p if i != "name" and i != "overall grade"]
    newDict['Grades'] = [int(p[i]["grade"]) for i in p if i != "name" and i != "overall grade"]
    fig = px.bar(newDict, x='Assignments', y='Grades')
    return plot(fig, output_type='div')