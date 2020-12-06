import tkinter as tk
import datetime as dt


def time_conversion():
    """
    Does all time related calculations
    """
    age = date.get()
    deadlineDate= dt.datetime.strptime(age,'%Y/%m/%d')
    difference = current_time - deadlineDate

    years = ((difference.total_seconds()) / (365.2421897 * 24 * 3600))
    years_int = int(years)

    months = (years - years_int) * 12
    months_int = int(months)

    days = (months - months_int) * (365.2421897 / 12)
    days_int = int(days)

    hours = ((difference.total_seconds()) / 3600)
    hours_int = int(hours)

    minutes = ((difference.total_seconds()) / 60)
    minutes_int = int(minutes)
    
    seconds = (difference.total_seconds())
    seconds_int = int(seconds)


    popup_text = tk.Text(master=window,height=5,width=35)
    popup_text.grid(column=1,row=5) 
    results = "You're "+str(years_int)+" years , "+str(months_int)+" months, "+ \
    str(days_int)+" days old or, "+str(hours_int)+" hours old or, "+str(minutes_int)+" minutes old or, "+\
    str(seconds_int)+" seconds old."


    popup_text.insert(tk.END,results)



if __name__ == "__main__":
    """
    window,button and label setups
    """
    window = tk.Tk()
    window.geometry("600x250")
    window.title("Age Calculator")
    date = tk.Label(text = "Date of Birth (YYYY/MM/DD) ")
    date.grid(column=0,row=1)
    date = tk.Entry()
    date.grid(column=1,row=1)
    current_time = dt.datetime.now()
    button=tk.Button(window,text="Calculate Age",command=time_conversion,bg="Red")
    button.grid(column=1,row=4)
    window.mainloop()
