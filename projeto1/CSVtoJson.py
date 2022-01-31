import json
import csv

with open("ArquivoCSV.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"names": []}
    for row in reader:
        data["names"].append(
            {"Primeiro nome": row[0], "idade": row[1], "ano de graduacao": row[2], "em que se graduou": row[3], "instituicao de ensino": row[4]})

with open("ArquivoJson.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4)


# Código executado com a ajuda do Canal Python Tutorials for Digital Humanities
