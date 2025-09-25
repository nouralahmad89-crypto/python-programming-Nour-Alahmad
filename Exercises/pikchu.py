# Labb 2: Klassificering av Pichu och Pikachu med KNN
# importera bibliotek och create .venv file
import matplotlib.pyplot as plt
import math
import pandas as pa
import numpy as np

# Läs in datan och spara i lämplig datastruktur
dataf = pa.read_csv("datapoints.txt", skiprows=1, header=None, names=["width","height","label"])
print(dataf) # double check the dataframe , number of rows and columns
dimansion = dataf[["width", "height"]].values # alla width och height kommer spara i dimsnsion array
Labl = dataf["label"].values # alla labels (0,1) kommer spara i labl array.

# Plotta data
plt.figure(figsize=(7,5)) # skapa en ny figur
pichu = dataf.query("label==0") # filtrerar data att få pichu punkter
pikachu= dataf.query("label==1") # filtrerar data att få pikachu punkter

# plottar pichu punkter i blått
plt.scatter(pichu["width"], pichu["height"], color="blue", label="Pichu (0)", s=30, alpha=0.5)
# plottar pikachu punkter i gul
plt.scatter(pikachu["width"], pikachu["height"], color="Yellow", label="Pikachu (1)", s=60 , alpha=0.7)
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.title("Pichu vs Pikachu - Data Points")
plt.legend()
plt.grid(True)
plt.show()
# läs in test punnkter
widths = np.array([25, 24.2, 22, 20.5])
heights = np.array([32, 31.5, 34, 34])
# Combine them into a single (4,2) array
testpoints = np.column_stack((widths, heights))
# en funktion för stt beräkna avståndet mellan punkter
def euclidean(a, b):
    return np.sqrt(np.power(a[0]-b[0], 2) + np.power(a[1]-b[1], 2))
# loopa igenom testpunkterna och klassificera
for pt in testpoints:
    distances = [euclidean(pt, x) for x in dimansion]
    nearest_index = np.argmin(distances)      # index för närmaste punkt
    predicted_label = Labl[nearest_index]     # hämta label för den närmaste
    if predicted_label == 1:
        print(f"Sample with (width, height): ({pt[0]}, {pt[1]}) classified as Pikachu")
    else:
        print(f"Sample with (width, height): ({pt[0]}, {pt[1]}) classified as Pichu")
