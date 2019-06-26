#cleaning process
import pandas as pd
import numpy as np
import os

os.chdir("C:/Users/LENOVO/Documents/fyp fathiah/Program/WebScrap")
df = pd.read_csv("cars3_test_.csv")

df1 = pd.read_csv("cars3_test_.csv", names = ['Name', 'Price', 'Condition', 'Link', 'Brand', 'Mileage', 'Model', 'Seat', 'Variant', 'Type', 'Series', 'Manufactured_Yr', 'Country', 'Transmission', 'EngineCC', 'Eng_Compression', 'Eng_PeakPower', 'Eng_PeakTorque', 'Eng_Type', 'Eng_Fuel', 'Length', 'Width', 'height', 'WheelBase', 'KerbWeight', 'FuelTank', 'FrontBrake', 'RearBrake', 'FrontSusp', 'RearSusp', 'Steering', 'FrontTyres', 'RearTyres', 'FrontRim', 'RearRim'])

#preview the first 5 lines of the loaded data
df1.head()

#preview the last 5 lines of the loaded data
df1.tail()

#declaring quantitative variables
numcol=['Price','Mileage', 'Seat', 'Manufactured_Yr', 'EngineCC', 'Eng_PeakPower', 'Eng_Compression', 'Eng_PeakTorque', 'Length', 'Width', 'height', 
'WheelBase', 'KerbWeight', 'FuelTank']

