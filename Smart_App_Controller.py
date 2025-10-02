def aantal_dagen(inputFile):
    with open(inputFile, "r") as file:
        regels = file.readlines()
    aantal_dagen = len(regels) -1
    return aantal_dagen
resultaat = aantal_dagen("test.txt")
print(resultaat)