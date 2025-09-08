import pandas as pd

pd.set_option('display.max_rows', None) # show all rows
pd.set_option('display.max_colwidth', None) # no column truncation
df = pd.read_csv('Checking1.csv')
imp = df.iloc[:, [0, 1, 4]] # Only columns 1, 2, and 5
imp.columns = ["Date", "Amount", "Description"]

descriptions = imp["Description"] # column 5
descriptions_dict = {} 

# need to find keywords such as "RECURRING" or "MAVERIK" or "PETCO" that can distinguish what the puchase was
# make dictionary to hold these categories so we can categorize purchases

for desc in descriptions:
    key = ' '.join(desc.split()[:2])
    descriptions_dict[key] = desc

print(imp)


venmo_payments = {}
venmo_cashout = {}
recurring_payments = {}
purchases = {} 
online_transfers = {}
payroll = {}
student_loan = {}
