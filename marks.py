
import csv
f1 = open("mark1.csv","r")
line1 = f1.next()
total = 0
for line in f1:
    
    columns = line.split(",")
    if len(columns) >= 2:
        tv = columns[1]
        er = columns[2]
        
        rp = int(er)
        print(tv,rp)
      #  print(type(rp)) 
        
        total += rp
       # we = sum(rp)
per = total * 100 / 500
print(total)
print(per)
f1.close()

# import csv
# f1 = open("marj.csv","r")
# print(f1[2].sum())

