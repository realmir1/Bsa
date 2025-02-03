from customtkinter import *
import numpy as np 
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import PhotoImage
import math
def hesapla():
    try:
        kilo = float(entr1.get())
        boy = float(entr2.get())        
        if kilo <= 0 or boy <= 0:
            messagebox.showerror("Hata", "Kilo ve boy değerleri sıfırdan büyük olmalıdır!")
            return
        bsa = math.sqrt((kilo * boy) / 3600)
        if bsa :
            sonuc=f"BSA: {bsa:.2f} m²"
        messagebox.showinfo(" Vücut yüzey alanı sonucu", sonuc)
    except ValueError:
        # Eğer giriş geçerli bir sayı değilse hata mesajı göster
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz!")





glas= CTk()
glas.title("Vücut Yüzey Alanı Hesaplama Programı")
glas.geometry("400x500")

canvas = CTkCanvas(master=glas, width=500, height=760)
canvas.grid(row=0, column=0)
background_image = PhotoImage(file="/Users/aliemirsertbas/Desktop/VSCO1prjct/CustomTKprjct.py/ımage/BSA.png")
canvas.create_image(0, 0, image=background_image, anchor="nw")

entr1=CTkEntry(master=glas, placeholder_text="lütfen kilonuzu giriniz", border_width=6,
                width=300,
                height=50,
                border_color="#8CDD1D",
               corner_radius=10,
                fg_color="white",
                bg_color="white",
               text_color="black"
               , placeholder_text_color="black")
entr1.place(relx=0.5, rely=0.5, anchor="center")

entr2=CTkEntry(master=glas, placeholder_text="lütfen boyunuzu giriniz", border_width=6,
                width=300,
                height=50,
                border_color="#8CDD1D",
               corner_radius=10,
                fg_color="white",
                bg_color="white",
               text_color="black",
                placeholder_text_color="black")
entr2.place(relx=0.5, rely=0.63, anchor="center")


button1= CTkButton(master=glas, 
                   width=200,
                   height=40,
                   fg_color="white",
                   bg_color="white",
                   hover_color="#8CDD1D",
                   text_color="black",
                   border_width=5,
                   border_color="black",
                   text="hesapla",
                   corner_radius=10,
                   command=hesapla)
button1.place(relx=0.5, 
              rely=0.75, 
              anchor="center"
              )






glas.resizable(0,0)
glas.mainloop()



