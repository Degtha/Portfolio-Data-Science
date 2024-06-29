#Import file menggunakan library Pandas, Numpy, dan seaborn 
import pandas as pd
import numpy as np
import seaborn as sns

#Perintah untuk membaca file csv 
df = pd.read_csv('Pokemon.csv')
print(df)

#Perintah untuk menjalankan 5 data awal pada data Pokemon.csv 
df.head()

#Perintah untuk menjalankan 5 data terakhir pada data Pokemon.csv
df.tail()

#Perintah untuk menjalankan dan mengetahui Type apa saja yang terdapat pada setiap pokemon
unique_types = set(df['Type 1']).union(set(df['Type 2']))
print(f"Unique types: {unique_types}")

#Perintah untuk memberikan ringkasan deskriptif pada setiap kolom pada data
df.describe()

#Perintah untuk mengetahui jumlah tiap Type Combined pada data
df['Type_Combined'] = df['Type 1'] + '-' + df['Type 2']
df['Type_Combined'].value_counts()

#Perintah untuk mengetahui jumlah pengguna pada Type/elemen pokemon tertentu
type_counts = {}
for type in unique_types:
  type_counts[type] = df[df['Type 1'] == type].shape[0] + df[df['Type 2'] == type].shape[0]
for type, count in type_counts.items():
  print(f"Type: {type}, Count: {count}")

#Perintah untuk mencari data pokemon Legendary menggunakan nilai True
legendary_pokemon = df[df['Legendary'] == True]
legendary_pokemon

#Perintah untuk mencari maximum special attack pada seluruh data pokemon
max_sp_atk = df['Sp. Atk'].max()
max_sp_atk_pokemon = df[df['Sp. Atk'] == max_sp_atk]
print(f"Pokemon with maximum special attack ({max_sp_atk}):")
print(max_sp_atk_pokemon[['Name', 'Sp. Atk']])

#Perintah untuk mencari nilai maximum HP pada seluruh data pokemon
max_hp = df['HP'].max()
max_hp_pokemon = df[df['HP'] == max_hp]
print(f"Pokemon with maximum HP ({max_hp}):")
print(max_hp_pokemon[['Name', 'HP']])

#Perintah untuk mencari jumlah data pokemon pada setiap generasi dengan menggunakan tabel diagaram batang
sns.set_theme()
sns.countplot(data=df, x='Generation', color='red')