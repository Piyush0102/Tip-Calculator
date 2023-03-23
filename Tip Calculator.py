#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to the Tip Calculator!")
bill=float(input("What is the total bill?\n$"))
tip=int(input("What percentage tip would you like to give?? 10, 12 or 15??\n$"))
people=int(input("How many people to split the bill?\n"))

total=bill*tip/100+bill
each_bill=total/people
#final_amt=round(each_bill,2)
final_amt="{:.2f}".format(each_bill)

print(f"Each person should pay :${final_amt}")


# In[ ]:




