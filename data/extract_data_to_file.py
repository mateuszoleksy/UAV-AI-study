### @copyright Mateusz Oleksy 2026
# Extract your desired columns for file

import pandas as pd
from configuration import configuration

dataset = pd.read_csv(configuration.get_filepath_to_extract())
dataset_final = pd.DataFrame(dataset, columns=configuration.get_columns_to_extract())

print("Saving processed data to: ", configuration.get_filepath_to_save())
dataset_final.to_csv(configuration.get_filepath_to_save(), index=False)
