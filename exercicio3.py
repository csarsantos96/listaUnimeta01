import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO

#  Carrega os dados diretamente do GitHub
url = "https://raw.githubusercontent.com/alura-cursos/numpy/refs/heads/dados/bytebank.csv"
csv_text = requests.get(url).text
# Coluna 1 = mês, coluna 2 = faturamento (string -> float, valores inválidos viram NaN)
data = np.genfromtxt(
    StringIO(csv_text),
    delimiter=",",
    skip_header=1,
    usecols=1,
    dtype=float,
    invalid_raise=False
)

# Encontra mês de maior e menor faturamento (ignorando NaN)
mes_maior = np.nanargmax(data) + 1
mes_menor = np.nanargmin(data) + 1

#  Corrige valor inválido (NaN) pelo vizinho anterior e posterior
nan_idx = np.where(np.isnan(data))[0]
if nan_idx.size > 0:
    i = nan_idx[0]
    data[i] = (data[i-1] + data[i+1]) / 2

#  Calcula médias
media_ano = np.mean(data)
media_1t = np.mean(data[0:3])
media_2t = np.mean(data[3:6])
media_3t = np.mean(data[6:9])
media_4t = np.mean(data[9:12])

#  Imprime resultados
print(f"Mês com maior faturamento: {mes_maior}")
print(f"Mês com menor faturamento: {mes_menor}")
print(f"Média anual: {media_ano:.2f}")
print(f"1º trimestre: {media_1t:.2f}")
print(f"2º trimestre: {media_2t:.2f}")
print(f"3º trimestre: {media_3t:.2f}")
print(f"4º trimestre: {media_4t:.2f}")

#  Gráfico de linha – faturamento mensal
meses = np.arange(1, 13)
plt.figure()
plt.plot(meses, data, marker='o')
plt.title("Faturamento Mensal ByteBank")
plt.xlabel("Mês")
plt.ylabel("Faturamento")
plt.grid(True)
plt.savefig("faturamento_mensal.png", dpi=300, bbox_inches="tight")
plt.show()

#7) Gráfico de barras – média por trimestre
trimestres = ["1T", "2T", "3T", "4T"]
medias = [media_1t, media_2t, media_3t, media_4t]
plt.figure()
plt.bar(trimestres, medias)
plt.title("Média de Faturamento por Trimestre")
plt.xlabel("Trimestre")
plt.ylabel("Média de Faturamento")
plt.grid(axis='y')
plt.savefig("media_trimestres.png", dpi=300, bbox_inches="tight")
plt.show()
