from health_ai import AiHealth
from sheet_data import SheetData
from graph_data import Graphs


def main():
    health_ai = AiHealth()
    health_data = health_ai.get_calories()

    sheet_data = SheetData()
    sheet_data.send_data_to_sheet(health_data)

    graph_data = Graphs()
    graph_data.send_graph_data(health_data)


main()
