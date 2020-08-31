import pandas as pd
import matplotlib.pyplot as plt
from datapackage import Package
package = Package('https://datahub.io/core/s-and-p-500-companies/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    resource.tabular # true
resource.read(keyed=True)


