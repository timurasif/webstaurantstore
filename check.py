import csv

l1 = ['My']
l2 = ['Name']
l3 = ['is', 'Timur', 'Asif']

l2.insert(0, ' ')
l3.insert(0, ' ')
l3.insert(0, ' ')

with open('check.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(l1)

with open('check.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(l2)

with open('check.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(l3)