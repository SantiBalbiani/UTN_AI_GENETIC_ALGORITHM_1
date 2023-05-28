from commons import task_durations
from commons import task_priorities
from commons import task_earnedValues
from commons import task_names
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


class Helper:

    def get_names(chromosomes):
        task_names_final = []
        for i, chromosome in enumerate(chromosomes):
            if chromosome == 1:
                task_names_final.append(task_names[i])
        return task_names_final

    def get_total(chromosome, attribute):
        task_final = []
        match attribute:
            case "task_durations":
                for i, chromosome in enumerate(chromosome):
                    if chromosome == 1:
                        task_final.append(task_durations[i])
            case "earned_value":
                for i, chromosome in enumerate(chromosome):
                    if chromosome == 1:
                        task_final.append(task_earnedValues[i])
            case "priorities":
                for i, chromosome in enumerate(chromosome):
                    if chromosome == 1:
                        task_final.append(task_priorities[i])
            case _:
                return None
        return sum(task_final)

    def graph(title_text, subgraphs_titles, selection_methods, subgraph_x_values, subgraphs_y_values):

        figure = make_subplots(rows=1, cols=len(
            selection_methods), subplot_titles=subgraphs_titles)
        for idx, selection_method in enumerate(selection_methods):
            figure.add_trace(go.Scatter(x=subgraph_x_values,
                             y=subgraphs_y_values[idx]), row=1, col=idx+1)

        figure.update_layout(
            height=600, width=1300, title_text="Comparación de Métodos de Selección", showlegend=False)
        figure.show()

        # figure = px.line(x=range(0, CONFIG.NUMBER_OF_GENERATIONS),
        #              y=solutions, title=graph_title)
