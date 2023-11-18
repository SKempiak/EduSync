import matplotlib.pyplot as plt
def generate_graph(p):
    overall_grade = p["overall grade"]["grade"]
    name = p["name"]

    fig, ax = plt.subplots()
    average = ax.axhline(y=overall_grade, color='r', linestyle='--', label=f"{name}'s Overall Grade")
    ax.set_title("Grades for " + name)
    ax.set_ylabel("Grade")
    ax.set_xticklabels([i for i in p if i != "name" and i != "overall grade"])
    ax.set_xticks(range(len(p) - 2))
    names = []
    values = []
    for key in p:
        if key == "name" or key == "overall grade": continue
        names.append(key)
        values.append(p[key]["grade"])
    ax.bar(range(len(p) - 2), values, label=names)
    plt.setp( ax.xaxis.get_majorticklabels(), rotation=10, ha="right" )
    plt.gcf().subplots_adjust(bottom=0.2)
    ax.legend(handles=[average])
    fig.savefig(f"graphs/{name}")

# person = {"name": "John", "overall grade": 83, "grade1": {"description": "blank", "grade": 100}, "grade2": {"description": "blank", "grade": 90}, "grade3": {"description": "blank", "grade": 60}, "grade4": {"description": "blank", "grade": 30}, "grade5": {"description": "blank", "grade": 80}, "grade6": {"description": "blank", "grade": 2}}