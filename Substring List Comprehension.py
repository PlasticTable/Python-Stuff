new_row = ["Datedsdad", "lasjdlakjd", "1790/1780", "1780/1790"]
new_row = [''.join(new_row[i][0:4]) if "/" in new_row[i] else new_row[i] for i in range(0, len(new_row))]

print(new_row)

#This is a part of a scripting project that reformats a CSV file
