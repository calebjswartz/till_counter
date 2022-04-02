
import tkinter as tk

frame = tk.Tk()
frame.title("Till Counter")
frame.geometry('400x400')


def getInput():
    hun = huntext.get()
    if hun == '':
        hun = 0.0
    hun = float(hun)
    output.config(text="Hundreds: " + str(format(hun*100, '.2f')))
    fif = fiftext.get()
    if fif == '':
        fif = 0.0
    fif = float(fif)
    output2.config(text="Fifties: " + str(format(fif*50, '.2f')))
    twe = twetext.get()
    if twe == '':
        twe = 0.0
    twe = float(twe)
    output3.config(text="Twenties: " + str(format(twe*20, '.2f')))
    ten = tentext.get()
    if ten == '':
        ten = 0.0
    ten = float(ten)
    output4.config(text="Tens: " + str(format(ten*10, '.2f')))
    fiv = fivtext.get()
    if fiv == '':
        fiv = 0.0
    fiv = float(fiv)
    output5.config(text="Fives: " + str(format(fiv*5, '.2f')))
    one = onetext.get()
    if one == '':
        one = 0.0
    one = float(one)
    output6.config(text="Ones: " + str(format(one, '.2f')))
    rq = rqtext.get()
    if rq == '':
        rq = 0.0
    rq = float(rq)
    output7.config(text="Rolled quarters: " + str(format(rq * 10.00, '.2f')))
    rd = rdtext.get()
    if rd == '':
        rd = 0.0
    rd = float(rd)
    output8.config(text="Rolled dimes: " + str(format(rd * 5.00, '.2f')))
    rn = rntext.get()
    if rn == '':
        rn = 0.0
    rn = float(rn)
    output9.config(text="Rolled nickels: " + str(format(rn * 2.00, '.2f')))
    rp = rptext.get()
    if rp == '':
        rp = 0.0
    rp = float(rp)
    output10.config(text="Rolled pennies: " + str(format(rp * 0.50, '.2f')))
    q = qtext.get()
    if q == '':
        q = 0.0
    q = float(q)
    output11.config(text="Loose quarters: " + str(format(q * 0.25, '.2f')))
    d = dtext.get()
    if d == '':
        d = 0.0
    d = float(d)
    output12.config(text="Loose dimes: " + str(format(d * 0.10, '.2f')))
    n = ntext.get()
    if n == '':
        n = 0.0
    n = float(n)
    output13.config(text="Loose nickels: " + str(format(n * 0.05, '.2f')))
    p = ptext.get()
    if p == '':
        p = 0.0
    p = float(p)
    output14.config(text="Loose pennies: " + str(format(p * 0.01, '.2f')))
    other = othertext.get()
    if other == '':
        other = 0.0
    other = float(other)
    output15.config(text="Other: " + str(format(other, '.2f')))
    total = (hun*100.00) + (fif*50.00) + (twe*20.00) + (ten*10.00) + (fiv*5.00) + one + (rq*10.00) + (rd*5.00) + (rn*2.00) + (rp*0.50) + (q*0.25) + (d*0.10) + (n*0.05) + (p*0.01) + other

    output16.config(text="Total: " + str(format(total, '.2f')))

# 100s
hunlabel = tk.Label(frame, text="Hundreds")
hunlabel.grid(row=0, column=0)
huntext = tk.Entry(frame)
huntext.grid(row=0, column=1)
# 50s
fiflabel = tk.Label(frame, text="Fifties")
fiflabel.grid(row=1, column=0)
fiftext = tk.Entry(frame)
fiftext.grid(row=1, column=1)
# 20s
twelabel = tk.Label(frame, text="Twenties")
twelabel.grid(row=2, column=0)
twetext = tk.Entry(frame)
twetext.grid(row=2, column=1)
# 10s
tenlabel = tk.Label(frame, text="Tens")
tenlabel.grid(row=3, column=0)
tentext = tk.Entry(frame)
tentext.grid(row=3, column=1)
# 5s
fivlabel = tk.Label(frame, text="Fives")
fivlabel.grid(row=4, column=0)
fivtext = tk.Entry(frame)
fivtext.grid(row=4, column=1)
# 1s
onelabel = tk.Label(frame, text="Ones")
onelabel.grid(row=5, column=0)
onetext = tk.Entry(frame)
onetext.grid(row=5, column=1)
# RQs
rqlabel = tk.Label(frame, text="Rolled Quarters")
rqlabel.grid(row=6, column=0)
rqtext = tk.Entry(frame)
rqtext.grid(row=6, column=1)
# RDs
rdlabel = tk.Label(frame, text="Rolled Dimes")
rdlabel.grid(row=7, column=0)
rdtext = tk.Entry(frame)
rdtext.grid(row=7, column=1)
# RNs
rnlabel = tk.Label(frame, text="Rolled Nickels")
rnlabel.grid(row=8, column=0)
rntext = tk.Entry(frame)
rntext.grid(row=8, column=1)
# RPs
rplabel = tk.Label(frame, text="Rolled Pennies")
rplabel.grid(row=9, column=0)
rptext = tk.Entry(frame)
rptext.grid(row=9, column=1)
# Qs
qlabel = tk.Label(frame, text="Loose Quarters")
qlabel.grid(row=10, column=0)
qtext = tk.Entry(frame)
qtext.grid(row=10, column=1)
# Ds
dlabel = tk.Label(frame, text="Loose Dimes")
dlabel.grid(row=11, column=0)
dtext = tk.Entry(frame)
dtext.grid(row=11, column=1)
# Ns
nlabel = tk.Label(frame, text="Loose Nickels")
nlabel.grid(row=12, column=0)
ntext = tk.Entry(frame)
ntext.grid(row=12, column=1)
# Ps
plabel = tk.Label(frame, text="Loose Pennies")
plabel.grid(row=13, column=0)
ptext = tk.Entry(frame)
ptext.grid(row=13, column=1)
# Other
otherlabel = tk.Label(frame, text="Other")
otherlabel.grid(row=14, column=0)
othertext = tk.Entry(frame)
othertext.grid(row=14, column=1)

button = tk.Button(frame, text="Calculate", command=getInput)
button.grid()
output = tk.Label(frame, text="")
output.grid(row=0, column=3)
output2 = tk.Label(frame, text="")
output2.grid(row=1, column=3)
output3 = tk.Label(frame, text="")
output3.grid(row=2, column=3)
output4 = tk.Label(frame, text="")
output4.grid(row=3, column=3)
output5 = tk.Label(frame, text="")
output5.grid(row=4, column=3)
output6 = tk.Label(frame, text="")
output6.grid(row=5, column=3)
output7 = tk.Label(frame, text="")
output7.grid(row=6, column=3)
output8 = tk.Label(frame, text="")
output8.grid(row=7, column=3)
output9 = tk.Label(frame, text="")
output9.grid(row=8, column=3)
output10 = tk.Label(frame, text="")
output10.grid(row=9, column=3)
output11 = tk.Label(frame, text="")
output11.grid(row=10, column=3)
output12 = tk.Label(frame, text="")
output12.grid(row=11, column=3)
output13 = tk.Label(frame, text="")
output13.grid(row=12, column=3)
output14 = tk.Label(frame, text="")
output14.grid(row=13, column=3)
output15 = tk.Label(frame, text="")
output15.grid(row=14, column=3)
output16 = tk.Label(frame, text="")
output16.grid(row=15, column=3)

frame.mainloop()