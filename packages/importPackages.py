
import csv
import io
from packages import packagesHashmap as HM
from Package import Package

# Initialize package hashmap
packagesHashmap = HM.PackagesHashMap()

# Import data from CSV and insert into hashmap
def importFile():
    with io.open('packages/WGUPS Package File.csv', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for rowIndex, row in enumerate(readCSV):
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], '')
            packagesHashmap.__setitem__(rowIndex + 1, package)
    return packagesHashmap