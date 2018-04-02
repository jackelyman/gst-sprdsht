import xlwt
import string
import names
import random
from random import getrandbits

print ("")
print (" --------------------------------------------")
print ("          Ghost Spreadsheet creator            ")
print ("           Developed by @Hypebeast2277              ")
print (" --------------------------------------------\n")

#user input
times = int(input("Enter the number of times you would like to fill: "))
profilename = str(input("Enter Profile Name: "))
addy1 = str(input("Enter Address 1: "))
city = str(input("Enter City: "))
state = str(input("Enter State (ex. NY) : "))
area = str(input("Enter Zip Code: "))
country = str(input("Enter Country (ex. US) : "))
phone = input("Phone Number Prefix: ")

book = xlwt.Workbook(encoding="utf-8")
#create sheet
sheet1 = book.add_sheet("Sheet 1")
#create columns
sheet1.write(0, 0, "Profile Name")
sheet1.write(0, 1, "First Name")
sheet1.write(0, 2, "Last Name")
sheet1.write(0, 3, "Address")
sheet1.write(0, 4, "Apt")
sheet1.write(0, 5, "City")
sheet1.write(0, 6, "State")
sheet1.write(0, 7, "Zip")
sheet1.write(0, 8, "Country")
sheet1.write(0, 9, "Phone")
sheet1.write(0, 10, "Card Number")
sheet1.write(0, 11, "Card Type")
sheet1.write(0, 12, "CVV")
sheet1.write(0, 13, "Expiry Month")
sheet1.write(0, 14, "Expiry Year")


#start under column titles
i=2
#write data
for i in range(times):
	i = i+1
	#ProfileName
	paste = profilename+str(i)
	sheet1.write(i, 0, paste)
	#firstname
	#names = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]
	firstName = names.get_first_name()
	sheet1.write(i, 1, firstName)
	#lastname
	lastName = names.get_last_name()
	sheet1.write(i, 2, lastName)
	#address line 1
	size = 4
	chars1 = string.ascii_uppercase + string.digits
	chars2 = ''.join(random.choice(chars1) for _ in range(size))
	addy2 = chars2+" "+addy1
	sheet1.write(i, 3, addy2)
	#City
	sheet1.write(i, 5, city)
	#state
	sheet1.write(i, 6, state)
	#zip
	sheet1.write(i, 7, area)
	#country
	sheet1.write(i, 8, country)
	#phone
	number5 = random.sample(range(10), 7)
	num2 = str((''.join(map(str, number5))))
	phone_num = phone+num2
	sheet1.write(i, 9, phone_num)
	#Cardtyoe
	site = "Visa"
	sheet1.write(i, 11, site)


print("SUCCESSFULLY SAVED TO SPREADSHEET")
book.save("GhostSnkrsscript.xls")
