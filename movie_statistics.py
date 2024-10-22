import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('NetflixOriginals.csv', encoding='ISO-8859-1')

# Obtener estadísticas principales de la columna 'IMDB Score'
imdb_stats = df['IMDB Score'].describe()
mean_imdb = df['IMDB Score'].mean()
std_imdb = df['IMDB Score'].std()

# Mostrar las estadísticas
print("Estadísticas principales de IMDB Score:")
print(imdb_stats)
print(f"\nPromedio de IMDB Score: {mean_imdb}")
print(f"Desviación estándar de IMDB Score: {std_imdb}")

# Obtener estadísticas principales de la columna 'Runtime'
imdb_stats = df['Runtime'].describe()
mean_imdb = df['Runtime'].mean()
std_imdb = df['Runtime'].std()
median_runtime = df['Runtime'].median()
iqr_runtime = df['Runtime'].quantile(0.75) - df['Runtime'].quantile(0.25)


# Mostrar las estadísticas
print("Estadísticas principales de Runtime:")
print(imdb_stats)
print(f"\nPromedio de Runtime: {mean_imdb}")
print(f"Desviación estándar de Runtime: {std_imdb}")
print(f"Mediana de Runtime: {median_runtime}")
print(f"Rango intercuartílico (IQR) de Runtime: {iqr_runtime}")


fig, axs = plt.subplots(2, 1, figsize=(10, 10))

axs[0].hist(df['IMDB Score'], bins=20, edgecolor='black')

# Añadir título y etiquetas
axs[0].set_title('Frecuencia de IMDB Score')
axs[0].set_xlabel('IMDB Score')
axs[0].set_ylabel('Frecuencia')


axs[1].hist(df['Runtime'], bins=20, edgecolor='orange')

# Añadir título y etiquetas
axs[1].set_title('Frecuencia de Runtime')
axs[1].set_xlabel('Runtime')
axs[1].set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()