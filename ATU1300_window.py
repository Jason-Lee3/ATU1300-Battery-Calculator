'''0.0.0 5/6/2022 J.L
 1. Initial Release 
0.0.1 5/9/2022 J.L
 1. Fixed a bug regarding placing the result from calculating values A and B
1.0.0 5/10/2022 J.L
 1. Updated the UI window size to fit the new implemented features
 2. Implemented new formula to calculate battery life and derated battery life of ATU1300 
 3. Replaced old labels with new labels 
 4. Updated the UI layout of ATU1300 Battery Life Calculator v1.0.0
'''

# Developed an application of GUI battery calculator for a tracking device (ATU-1300) using tkinter in python 
# used calculation formula given by an actual hardware engineer at CalAmp
from tkinter import *
from tokenize import String
from unittest import result 

main = Tk()
main.title("ATU1300 Battery Life Calculator v1.0.0")
main.geometry("725x625")

def Calculate():    
    #amount=float(batt_cap_mah_entry.get())+float(eff_entry.get())
    #result_value.set(amount)
    derate1 = 0.25
    derate2 = 120
    batt_cap_day = float(batt_cap_mah_entry.get())*(float(eff_entry.get())/100)*1000/24
    lmu_avg_day = float(lmu_run_ma_entry.get())*float(lmu_run_time_entry.get())*1000/3600/24
    batt_life_day_round = round(batt_cap_day/(lmu_avg_day+float(lmu_bot_uA_entry.get())))
    batt_life_day.set(batt_life_day_round)
    batt_life_years_round = round(((batt_cap_day/(lmu_avg_day+float(lmu_bot_uA_entry.get())))/365), 2)
    batt_life_years.set(batt_life_years_round)
    batt_life_day_value = batt_cap_day/(lmu_avg_day+float(lmu_bot_uA_entry.get()))
    batt_life_derate_day_value = batt_life_day_value - (batt_life_day_value*derate1) - derate2
    batt_life_derate_day_round = round(batt_life_derate_day_value)
    batt_life_derate_day.set(batt_life_derate_day_round)
    batt_life_derate_yrs_round = round(batt_life_derate_day_value/365, 1)
    batt_life_derate_yrs.set(batt_life_derate_yrs_round)

batt_cap_mah = StringVar()
eff = StringVar()
lmu_run_ma = StringVar()
lmu_run_time = StringVar()
lmu_bot_uA = StringVar()
batt_life_day = StringVar()
batt_life_years = StringVar()
batt_life_derate_day = StringVar()
batt_life_derate_yrs = StringVar()

#Input Labels
Label(main, text="Battery Capacity:", font ="arial 16").place(x=120,y=86)
Label(main, text="Efficiency:", font ="arial 16").place(x=120,y=116)
Label(main, text="Lmu Running Current:", font ="arial 16").place(x=120,y=146)
Label(main, text="Lmu Running Time:", font ="arial 16").place(x=120,y=176)
Label(main, text="Lmu Bottom Current:", font ="arial 16").place(x=120,y=206)

#Units
Label(main, text="(mAh)", font ="arial 16").place(x=450,y=86)
Label(main, text="(%)", font ="arial 16").place(x=450,y=116)
Label(main, text="(mA)", font ="arial 16").place(x=450,y=146)
Label(main, text="(sec)", font ="arial 16").place(x=450,y=176)
Label(main, text="(uA)", font ="arial 16").place(x=450,y=206)

#Output Labels
Label(main, text="Battery Life:", font ="arial 16").place(x=120,y=370)
Label(main, text="Derated Battery Life:", font ="arial 16").place(x=120,y=430)

Label(main, text="(days)", font ="arial 16").place(x=450,y=370)
Label(main, text="(years)", font ="arial 16").place(x=450,y=400)
Label(main, text="(days)", font ="arial 16").place(x=450,y=430)
Label(main, text="(years)", font ="arial 16").place(x=450,y=460)

batt_cap_mah_entry = Entry(main, textvariable=batt_cap_mah,font="arial 16", width = 8)
eff_entry = Entry(main, textvariable=eff,font="arial 16", width = 8)
lmu_run_ma_entry = Entry(main, textvariable=lmu_run_ma,font="arial 16", width = 8)
lmu_run_time_entry = Entry(main, textvariable=lmu_run_time,font="arial 16", width = 8)
lmu_bot_uA_entry = Entry(main, textvariable=lmu_bot_uA,font="arial 16", width = 8)

#User Enter Box for Input
batt_cap_mah_entry.place(x=335,y=86)
eff_entry.place(x=335,y=116)
lmu_run_ma_entry.place(x=335,y=146)
lmu_run_time_entry.place(x=335,y=176)
lmu_bot_uA_entry.place(x=335,y=206)

#Output result 
Label(main, text="", textvariable=batt_life_day, font="arial 16").place(x=330,y=370)
Label(main, text="", textvariable=batt_life_years, font="arial 16").place(x=330,y=400)
Label(main, text="", textvariable=batt_life_derate_day, font="arial 16").place(x=330,y=430)
Label(main, text="", textvariable=batt_life_derate_yrs, font="arial 16").place(x=330,y=460)

Button(main,text="Calculate",font="arial 35",command=Calculate,width=9,height=1).place(x=240,y=260)

main.mainloop()



