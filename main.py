import pandas as pd

df = pd.read_csv('Checking1.csv')
imp = df.iloc[:, [0, 1, 4]]
descriptions = imp.iloc[:, 2]
descriptions_dict = {}

# need to find keywords such as "RECURRING" or "MAVERIK" or "PETCO" that can distinguish what the puchase was
# make dictionary to hold these categories so we can categorize purchases

for desc in descriptions:
    key = ' '.join(desc.split()[:2])
    descriptions_dict[key] = desc

print(descriptions_dict)
