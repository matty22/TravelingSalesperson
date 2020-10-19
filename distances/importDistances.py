
import csv
import io
from distances import distancesHashmap as HM

# Initialize hashmap
distancesHashmap = HM.DistancesHashMap()

# Import data from CSV and insert into hashmap
def importFile():
    with io.open('distances/WGUPS Distance Table.csv', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for rowIndex, row in enumerate(readCSV):
            for cellIndex, cell in enumerate(row):
                distancesHashmap.__setitem__(rowIndex + 1, row[0], cell)
        distancesHashmap.printDistancesHash()

