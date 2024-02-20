from health_ai import AiHealth
from sheet_data import SheetData

health_ai = AiHealth()
data = health_ai.get_calories()

sheet_data = SheetData()
sheet_data.send_data_to_sheet(data)
