
import csv
import io
from packages import packagesHashmap as HM

# Initialize package hashmap
packagesHashmap = HM.PackagesHashMap()

# Import data from CSV and insert into hashmap
def importFile():
    with io.open('packages/WGUPS Package File.csv', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for rowIndex, row in enumerate(readCSV):
            for cellIndex, cell in enumerate(row):
                packagesHashmap.__setitem__(rowIndex + 1, cell)
        packagesHashmap.printPackagesHash()
        packagesHashmap.__delitem__(1)
        packagesHashmap.printPackagesHash()
