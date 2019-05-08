import csv

files = ["file1", "file2", "file3"]
#files = set(["file1", "file2", "file3"])

with open("./mycsv.csv", mode='w') as c:
    writer = csv.writer(c, dialect="excel")
    writer.writerow(['File Name',])
    writer.writerows(files)
    #writer.writerows([f] for f in files)

"""
with open("./mycsv.csv", mode='w', newline='') as c:
    #writer = csv.DictWriter(c, fieldnames=["File Name"])
    #writer.writeheader()
    #for line in files:
        #writer.writerow({"File Name": line})
    
    writer = csv.writer(c)
    writer.writerow("File Name")
    for line in files:
        writer.writerow(str(line))
"""