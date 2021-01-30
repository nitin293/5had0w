import os


csv_files = []

for file in os.listdir():
    if file.split('.')[-1] == 'csv':
        csv_files.append(file)

row_data = []

if 'merged' not in os.listdir():
    os.mkdir('merged')

f = open('./merged/merged_data.csv', 'w')
f.close()

for csv_file in csv_files:
    try:
        d_file = open(csv_file, encoding='utf-8')

        for row in d_file:
            if row and row not in row_data:
                row_data.append(row)

                merge_file = open('./merged/merged_data.csv', 'ab')
                merge_file.write(row.encode("utf-8"))
                merge_file.close()

        d_file.close()

    except UnicodeDecodeError:
        d_file = open(csv_file)

        for row in d_file:
            if row and row not in row_data:
                row_data.append(row)

                merge_file = open('./merged/merged_data.csv', 'ab')
                merge_file.write(row.encode("utf-8"))
                merge_file.close()

        d_file.close()
