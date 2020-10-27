#Income tax calculation using GUI
#creating window
from tkinter import *
myw=Tk()
#Window title and size
myw.title("Income Tax Calculation")
myw.geometry('300x250')

lbl_heading =Label(myw,text="Income tax calculation", font=("Helvatica",16))
lbl_heading.pack()

price_lbl=Label(myw, text=("Enter your Income: "))
price_lbl.pack()

price_entry=Entry(myw)
price_entry.pack()

tax_lbl=Label(myw, text=("Tax(%): "))
tax_lbl.pack()

tax_entry=Entry(myw)
tax_entry.pack()

#Using function to calculate values
def cal():
    price_val=int(price_entry.get())
    tax_val=int(tax_entry.get())
    calculation=(price_val*tax_val)/100
    cess=(price_val*0.04)

    lbl=Label(myw, text="The tax to pay is: "+str(calculation))
    lbl.pack()

    lbl=Label(myw, text="The total amount with tax is:" +str(price_val+calculation))
    lbl.pack

    lbl=Label(myw, text="The total cess tax is:"+str(cess))
    lbl.pack()

    lbl=Label(myw, text="The total amount is:" +str(price_val+calculation+cess))
    lbl.pack()

#button for calculation to print calculated values

cal_btn=Button(myw,text="Calculation",command=cal)
cal_btn.pack()
myw.mainloop()
