from .models import Work
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px

def generate_graph(p):
    newDict = {}
    newDict['Assignment'] = [i for i in p if i != "name" and i != "overall grade"]
    newDict['Grade'] = [int(p[i]["grade"]) for i in p if i != "name" and i != "overall grade"]
    fig = px.bar(newDict, x='Assignment', y='Grade')
    works = Work.objects.all()
    newWorks = []
    for work in works:
        if work.title == "overall grade": newWorks.append(work)
    class_average = 0
    for work in newWorks:
        class_average += int(work.grade)
    class_average /= len(newWorks)
    fig.add_hline(y=class_average)
    fig.update_layout(yaxis_range=[0,100])
    return plot(fig, output_type='div')