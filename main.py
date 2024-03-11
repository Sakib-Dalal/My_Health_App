from health_ai import AiHealth
from sheet_data import SheetData
from graph_data import Graphs

# https://pixe.la/@sakib5001
# https://pixe.la/v1/users/sakib5001/graphs/calo1.html
# https://pixe.la/v1/users/sakib5001/graphs/time1.html
# https://docs.google.com/spreadsheets/d/1zPfEnTH0ipmY1Hk2Q02ydNwOU6ojAOu9QHnw85SIRZI/edit#gid=0


def main():
    health_ai = AiHealth()
    health_data = health_ai.get_calories()

    sheet_data = SheetData()
    sheet_data.send_data_to_sheet(health_data)

    graph_data = Graphs()
    graph_data.send_graph_data(health_data)


main()
