import pandas as pd
from data.column_name import COL_DICT

df = pd.read_table("data/mock_data.tsv", sep="\s{2,}", engine="python")
df = df.rename(columns=COL_DICT)
print(df)
