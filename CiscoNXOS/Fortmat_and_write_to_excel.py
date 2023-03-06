import pandas as pd
import json

output = json.loads(register["nxos_prefix_list"])
                    
## create a dataframe from the output of the ansible script
                    
                  
# set the colun names

df.clumns ="[prefix]"

# format the document 

df["prefix"] = df["prefix"].apply(lambda x: x.upper())
df.style.applymap( lambda val: 'colour: red' if val < 10 else '', subnet=['prefix'])

df.to_excel('output.xlsx
                                  
