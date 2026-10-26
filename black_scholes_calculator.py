import numpy as np
from black_scholes import BS
from tkinter import *
root = Tk()
root.configure(background = 'black')
root.title('Black Scholes Calculator')
root.geometry('550x630')

call_price = Label()
call_delta= Label()
call_gamma= Label()
call_vega = Label()
call_theta = Label()
call_rho = Label()

put_price = Label()
put_delta= Label()
put_gamma= Label()
put_vega = Label()
put_theta = Label()
put_rho = Label()

multyplier = Label()

def bs_calc(event=None):
    global call_price,call_delta,call_gamma,call_vega,call_theta,call_rho, \
            put_price,put_delta,put_gamma,put_vega,put_theta,put_rho,multyplier

    call_price.pack_forget()
    call_delta.pack_forget()
    call_gamma.pack_forget()
    call_vega.pack_forget()
    call_theta.pack_forget()
    call_rho.pack_forget()

    put_price.pack_forget()
    put_delta.pack_forget()
    put_gamma.pack_forget()
    put_vega.pack_forget()
    put_theta.pack_forget()
    put_rho.pack_forget()

    multyplier.pack_forget()

    option = BS(float(spot.get()),int(strike.get()),float(rate.get()),int(days.get()),float(Vol.get()),float(multy.get()))

    call_price=Label(call_frame,text=option.call_price(),fg='yellow',bg='black',font=25,pady=5)
    call_delta = Label(call_frame, text=option.call_delta(), fg='yellow', bg='black',font=25,pady=5)
    call_gamma = Label(call_frame, text=option.call_gamma(), fg='yellow', bg='black',font=25,pady=5)
    call_vega = Label(call_frame, text=option.call_vega(), fg='yellow', bg='black',font=25,pady=5)
    call_theta = Label(call_frame, text=option.call_theta(), fg='yellow', bg='black',font=25,pady=5)
    call_rho = Label(call_frame, text=option.call_ro(), fg='yellow', bg='black',font=25,pady=5)

    put_price = Label(put_frame, text=option.put_price(), fg='yellow', bg='black', font=25, pady=5)
    put_delta = Label(put_frame, text=option.put_delta(), fg='yellow', bg='black', font=25, pady=5)
    put_gamma = Label(put_frame, text=option.put_gamma(), fg='yellow', bg='black', font=25, pady=5)
    put_vega = Label(put_frame, text=option.put_vega(), fg='yellow', bg='black', font=25, pady=5)
    put_theta = Label(put_frame, text=option.put_theta(), fg='yellow', bg='black', font=25, pady=5)
    put_rho = Label(put_frame, text=option.put_ro(), fg='yellow', bg='black', font=25, pady=5)

    call_price.pack()
    call_delta.pack()
    call_gamma.pack()
    call_vega.pack()
    call_theta.pack()
    call_rho.pack()

    put_price.pack()
    put_delta.pack()
    put_gamma.pack()
    put_vega.pack()
    put_theta.pack()
    put_rho.pack()

root.bind('<Return>',bs_calc)

#Spot
spot_name = Label(root,text = 'spot', bg ='purple',fg = 'white', font =('Arial',25), padx = 30)
spot_name.grid(row=0,column=0)

spot = Entry(root,fg = 'red', bg = 'yellow', borderwidth = 5, font =('arial',25), width = 23)
spot.grid(row=0,column=1)
spot.insert(0,1800)

#strike
strike_name = Label(root,text='strike',bg='black',fg='white',font=25)
strike_name.grid(row=1,column=0,padx=3,pady=10)

strike = Entry(root,fg='white',bg='black',borderwidth=5,font=25,width=23)
strike.grid(row=1,column=1)
strike.insert(0,1800)

#risk free rate
rate_name = Label(root,text='rate',bg='black',fg='white',font=25)
rate_name.grid(row=2,column=0,padx=3,pady=10)

rate = Entry(root,fg = 'white',bg='black',borderwidth=5,font=25,width=23)
rate.grid(row=2,column=1)
rate.insert(0,0.01)
#days to maturity
days_name = Label(root,text='days',bg='black',fg='white',font=25)
days_name.grid(row=3,column=0,padx=3,pady=10)

days = Entry(root,fg = 'white',bg='black',borderwidth=5,font=25,width=23)
days.grid(row=3,column=1)
days.insert(0,30)

#vol
Vol_name = Label(root,text='volatility',bg='black',fg='white',font=25)
Vol_name.grid(row=4,column=0,padx=3,pady=10)

Vol = Entry(root,fg = 'white',bg='black',borderwidth=5,font=25,width=23)
Vol.grid(row=4,column=1)
Vol.insert(0,0.2)

#multyplier
multy_name = Label(root,text='multyplier',bg='black',fg='white',font=25)
multy_name.grid(row=5,column=0,padx=3,pady=10)

multy = Entry(root,fg = 'white',bg='black',borderwidth=5,font=25,width=23)
multy.grid(row=5,column=1)
multy.insert(0,100)
#button
calculate_btn = Button(root,text='calculate',fg='yellow',bg='purple',font=25,command=bs_calc)
calculate_btn.grid(row=6,column=1,pady=6)

#frame
frame1=LabelFrame(root,padx=5,pady=5)
frame1.grid(row=7,column=1,rowspan=6)

call = Label(frame1,text='CALL',width=5,font=('Arial',15,'underline'),fg='white',bg='purple')
call.grid(row=0,column=0)

put = Label(frame1,text='PUT',width=5,font=('Arial',15,'underline'),fg='white',bg='purple')
put.grid(row=0,column=3)

call_frame = LabelFrame(frame1,width=120,height=200,bg='black')
call_frame.grid(row=1,column=0,rowspan=6)

put_frame = LabelFrame(frame1,width=120,height=200,bg='black')
put_frame.grid(row=1,column=3,rowspan=6)

price = Label(frame1,text='PRICE',font=25,fg='white',bg='purple')
price.grid(row=1,column=2)

delta = Label(frame1,text = 'DELTA',font=25,fg='white',bg='purple')
delta.grid(row=2,column=2)

gamma = Label(frame1,text = 'GAMMA',font = 25, fg = 'white',bg='purple')
gamma.grid(row=3,column=2)

vega= Label(frame1,text = 'VEGA',font = 25, fg = 'white',bg='purple')
vega.grid(row=4,column=2)

theta = Label(frame1,text = 'THETA',font=25, fg = 'white',bg='purple')
theta.grid(row=5,column=2)

ro=Label(frame1,text = 'RO',font=25, fg = 'white',bg='purple')
ro.grid(row=6,column=2)

marking = Label(root,text='made by ...',fg='white',bg='black',font=('georgia',15),pady=12)
marking.grid(row=14,column=1)


root.mainloop()
