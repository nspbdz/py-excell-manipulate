import pandas as pd

df = pd.DataFrame([[11, 12]], columns=["Kota", "Pendapatan_harian"])  
with pd.ExcelWriter("excels2.xlsx") as writer:
    df.to_excel(writer)  
    