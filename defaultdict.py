import csv,json
my_dict = {}
with open("mark1.csv","r") as file1:
    reader = csv.reader(file1)
    # next(reader)
    line1 = file1.next()
    for row in reader:
        student_name = row[0]
        marks = int(row[3])
        
        if student_name not in my_dict:
             my_dict[student_name] = 0
             
        my_dict[student_name] += marks
       

    print(my_dict)
with open('result1.json',"w") as jsonfile:
    jsonfile.write(json.dumps(my_dict, indent=4))