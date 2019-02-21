###!/usr/bin/env python3

import tkinter as tk
window = tk.Tk()

window.title("jointControl")
window.geometry('550x400')
# window.resizable(False, False)

headline_lable = tk.Label(window,text= " write the robot name here",font=("Arial Bold", 20))
headline_lable.pack(padx =5 ,pady=20,side ="top")

btn_connect = tk.Button(bottomFrame,window, text="connect")
btn_connect.pack(padx=10,pady=200,side="left")

btn_Disconnect =tk.Button(bottomFrame,window,text ="Disconnect")
btn_Disconnect.pack(padx=15,pady=200,side="left")


j1_val ,j2_val,j3_val,j4_val,j5_val,j6_val,j7_val=0,0,0,0,0,0,0

joint1 = tk.Scale(window,variable = j1_val)
joint1.pack(padx=4, pady=10, side="left")
joint2 = tk.Scale(window,variable = j2_val)
joint2.pack(padx=7, pady=10, side="left")
joint3 = tk.Scale(window,variable = j3_val)
joint3.pack(padx=10, pady=10, side="left")
joint4 = tk.Scale(window,variable = j4_val)
joint4.pack(padx=13, pady=10, side="left")
joint5 = tk.Scale(window,variable = j5_val)
joint5.pack(padx=16, pady=10, side="left")
joint6 = tk.Scale(window,variable = j6_val)
joint6.pack(padx=19, pady=10, side="left")
joint7 = tk.Scale(window,variable = j7_val)
joint7.pack(padx=22, pady=10, side="left")


window.mainloop()
