import re
phone_num=re.compile(r'''
          # This one is country code(+91) which is optional. So we are not checking with the starting point.
(\d{3})   # This is starting three numbers of the mobile number.
\D*       #This is for non numeric character hyphen('-') which occur after first three numbers. This may occur or not in mobile number.
(\d{3})   #This is the last middle numbers of the mobile number
\D*       #This is another non numeric character hyphen('-') after middle three numbers. This may occur or not in mobile number.
 (\d{4})  #This is the last four digits of the mobile number.
 $        # This is the end of the String.
 ''',re.VERBOSE)

print(phone_num.search("8500189645").groups())
print(phone_num.search("+918500189645").groups())
print(phone_num.search("+91850-018-9645").groups())
print(phone_num.search("+91-850-018-9645").groups())
print(phone_num.search("+91-8500189645").groups())




