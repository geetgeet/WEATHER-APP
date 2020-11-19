'''temperature, humidity,
wind speed, cloud cover and others.
Design a tkinter GUI which will allow t'''
from tkinter import*
from tkinter import messagebox
import requests
#Creating window
window=Tk()
window.geometry("500x500")
window.config(bg="teal")
window.title("Weather in my Location") #add title

#CREATE FUNCTION
def check():
    #eRRoR Handling
    try:



        url='https://api.openweathermap.org/data/2.5/weather'
        key='8b66c41375c2178c4c616922a5fa5d15'
        parameter1={"appid":key,"q":homes.get(),"units":"Metric"}
        response=requests.get(url,params=parameter1)
        weather=response.json()

        min=weather['main']['temp_min']
        max=weather['main']['temp_max']
        ave=weather['main']['temp']
        hum=weather['main']['humidity']
        wind=weather['wind']['speed']
        des=weather['weather'][0]
        con=(des['description'])


        lbl_disp.config(text="Conditions in:"+'\n'+ '***'+homes.get()+'***'+'\n'+
                           con +'\n'+ "Ave.Temp:" +str(ave)+'\n'+"Mininum Temp(C):"+ str(min) +'\n'+ "Maximun Temp(C):"+str(max) +'\n'+ "Humidity:"+str(hum)+'\n'+ "Current Windspeed:"+str(wind))
    except KeyError: #expected error
        messagebox.showinfo('Error Message','Please Enter location')




#clear function

def clear():
    lbl_disp.config(text="Conditions Display Here:")
    homes.delete(0,END)






#Creating widgets
lbl_loc=Label(window,text="Enter Location:",font=("Times",15,"bold"))
lbl_loc.grid(row=1,column=1)
homes=Entry(window)
homes.grid(row=1 , column=2)
lbl_disp=Label(window,text="Conditions Display Here:")
lbl_disp.grid(row=2,column=2)


out_button=Button(window,text="View", command=check)
out_button.grid(row=2,column=1)

clear_b=Button(window,text="Clear",command=clear)
clear_b.grid(row=3,column=1)


window.mainloop()
