# WAP to print a result
result = str()
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    physics = int(input("Enter physics = "))
    chemistry = int(input("Enter chemistry = "))
    math = int(input("Enter math = "))
    total = physics+chemistry+math
    per = total/3
    if per>=80:
        grade = "A"
    elif per>=60:
        grade = "B"
    elif per>=45:
        grade = "C"
    else:
        grade = "F"
    result = result + name+ "\t"+str(physics)+"\t"+str(chemistry)+"\t"+str(math)+"\t"+str(total)+"\t"+str(per)+"\t"+str(grade)+"\n"
    
    print('name, physics, chemistry, math,total,grade,per')
    print(result)

