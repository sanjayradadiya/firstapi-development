
import csv
import json

my_dict = {}
with open("mark1.csv","r") as file1:
    reader = csv.reader(file1)
    next(reader)
    # line1 = file1.next()
    for row in list(reader):
        student_name = row[0]
        marks = int(row[3])
        if student_name not in my_dict:
            my_dict[student_name] = 0
        # append the new number to the existing array at this slot
        my_dict[student_name] += marks
        my_dict[student_name]
        
        
        # print(type(marks))
        # result1 = total * 100 / 500
    
        
        # my_dict.setdefault(row[0],[]).append(row[4])
     
    # my_dict[student_name] = result1
    print(my_dict)
    for row in my_dict:
         print(row, my_dict[row])
         result = my_dict[row] * 100 / 500
         print(result)

    print(my_dict)
        #  student_name1 = row[0]
        #  total = row[1]
        #  print(student_name1)
        #  print(total)
             


           