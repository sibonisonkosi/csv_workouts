import csv

old_data = '/Users/nkosi/Desktop/Metadata/combined_csv.txt'
new_data = '/Users/nkosi/Desktop/Metadata/MeasuresColumns.txt'



with open(old_data,'r') as file1:
    existingLines = [line for line in csv.reader(file1, delimiter=',')]
count = 0
new = []
with open(new_data,'r') as file2:
    reader2 = csv.reader(file2,delimiter='\t')
    for row in reader2:
        if row not in new and row not in existingLines:
            writer = csv.writer(open('/Users/nkosi/Desktop/Metadata/combined_csv.txt','a'))
            writer.writerow(row)
            count = count + 1
        

print(count)