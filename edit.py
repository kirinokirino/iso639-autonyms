import csv

table = []

with open('iso639-autonyms.tsv', 'rt', newline='', encoding='utf-8') as f:
	reader = csv.reader(f, dialect='excel-tab')
	for row in reader:
		current_row = []
		current_row.extend(row[:3])
		current_row.append(row[3].title())
		table.append(current_row)

with open('iso639-autonyms.csv', 'wt', newline='', encoding='utf-8') as f:
    writer  = csv.writer(f)
    writer.writerows(table)