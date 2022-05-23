from queue import Full


name = "misheck kibe"

#Multiple line strings 
msg =""" my name is misheck kibe
i am from kiambu
and i love playing soccer"""
print(msg)
#multiple line strings
msg ="""several challenges are facing the youth
one of the main is that many are IT illiterate
this can be rectified through joining it programs 
such as : INSPIRE IN STEM 
offered at JKUAT """
print(msg)


city ="nairobi"
#.upper() to convert to uppercase
print(city.upper())


town ="juja"
#.upper() to convert to uppercase
print(town.upper())

uni ="JKUAT"
print(uni.lower())


college ="KENYATTA"
#.lower() to convert to lowercase
print(college.lower())


fruit ="pineapple"
print(fruit[:2])
print(fruit[4:])
print(fruit[-1:])
print(fruit[-5:])
print(fruit[:-5])

# strip() removes spaces between the words
f_name ="misheck kibeh"
print(f_name.strip())

f_name ="mish eckki beh"
print(f_name.strip())

f_name ="  mish eckki beh"
print(f_name.strip())

f_name ="misheck"
s_name ="kibeh"
#string cocartination [adding the two strings]
full_name =f_name+s_name
print(full_name)


#length of strings [len(city)]
city ="mombasa"
print(len(city))


word ="abracadabra"
print(len(word))

word ="deoxyribonucleic acid"
print(len(word))

#converting an INT to  A STRING
x=100

y=3.14
#a decimal is a float
z=1

print(str(x))
print(int(y))
print(float(z))
