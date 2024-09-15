#The Escape Sequences 
print("Hello World") 
print("Hello \n World") #with the escape sequence
print("Hello \\n World") #without the escape sequence it shows as it is 

'''when we use the backslash as an escape sequence in the output its not vissible if we take backslash with 
backslash then only one is prompted'''

print("8 backslash \\\\\\\\") #only 4 will be prompted
#output : \\\\

print("\'\"")
#output : '" 


#we can restrict escape sequences by using raw methods
print(r"The escape sequence is now \n restricted")