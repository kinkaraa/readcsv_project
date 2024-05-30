import csv

# Membaca file CSV
with open('contact.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Menulis ke file CSV
# with open('contact.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Nama', 'Umur', 'Kota'])
#     writer.writerow(['Budi', '25', 'Jakarta'])
    
print("Writing Done!")

rows = []
with open('contact.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    header.append('Gender')
    rows.append(header)
    for row in reader:
        row.append('')
        rows.append(row)

# Mengubah baris yang diinginkan
for row in rows:
    if row[0] == 'Bayu':
        row[0] = 'Ilham'
        row[1] = '30'  # Misalnya juga mengubah umur
        row[2] = 'Bandung'  # Misalnya juga mengubah kota
        row[3] = 'Laki-Laki'
# Menulis kembali seluruh konten ke file
with open('contact.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)