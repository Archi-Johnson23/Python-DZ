# from datetime import datetime
# def main():
#     now = datetime.now()
#     print(now.strftime("%H:%M:%S"))
#     print("\r", end="", flush=True)
    
# #     t = datetime.time(datetime.now())
# #     print('текущее время',t)
# if __name__=="__main__":
#     main()


# import time
# from datetime import datetime
# while True:   
#     now = datetime.now()
#     print (now.strftime("%H""\u25A0""%M""\u25A0""%S"), end="", flush=True),
#     print("\r", end="", flush=True),
#     time.sleep(1)
# if __name__=="__main__":
#     main()
  
from tkinter import *
import time
chas = ""
stranitca = Tk()
statusbar = Frame(stranitca)
statusbar.pack(side="top",expand=False)
clock = Label(stranitca, font=('times', 160), bg='white')
def clock_dm():
       global chas
       time2 = time.strftime('%H\u25A0%M\u25A0%S')
       if time2 != chas:
           chas = time2
           clock.config(text=time2)
       clock.after(200, clock_dm)
print(clock_dm())
clock.pack(in_=statusbar,expand=False)
print(stranitca.mainloop(  ))