
import csv
import io
from distances import distancesHashmap as HM

# Initialize distances hashmap
# See space and time complexity in hashmap definition file
# --------------------------
distancesHashmap = HM.DistancesHashMap()

# Import data from CSV and insert distances into hashmap
# Space complexity: O(n^2)
# Time complexity: O(n^2)
# --------------------------
def importFile():
    with io.open('distances/WGUPS Distance Table.csv', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for rowIndex, row in enumerate(readCSV):
            for cellIndex, cell in enumerate(row):
                distancesHashmap.__setitem__(rowIndex + 1, row[0], cell)
    return distancesHashmap
