import pandas as pd

df = pd.read_excel('data2.xlsx', sheet_name='Sheet1')


# df["Jumlah_Penduduk"] = df["Jumlah_Penduduk"].replace({"15 juta": 10})
# df["Pendapatan_Harian"] = df["Pendapatan_Harian"].replace({"500 ribu": 9})

# print(df.head(1))
df.to_excel('saved_file.xlsx', index = False)
# for i in df.index:
#     print("Kota: "+df['Kota'][i])
#     print("Jumlah Penduduk: "+df['Jumlah_Penduduk'][i])
#     print("Pendapatan Harian: "+df['Pendapatan_Harian'][i])