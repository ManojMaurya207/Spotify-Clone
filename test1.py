import customtkinter
from tkinter import messagebox

class TicketCounterQueueApp:
    def init(self):
        self.start = None
        self.last = None
    
        self.root = customtkinter.CTk()
        self.root.geometry("1920x1080")
        self.root.configure(fg_color="gray92")
        self.root.title("Queue gui")

        self.f2 = customtkinter.CTkScrollableFrame(self.root, width=800, height=480, corner_radius=20)
        self.frm = customtkinter.CTkFrame(self.f2, width=780, height=80, corner_radius=20)

        self.frame = customtkinter.CTkFrame(self.root, width=1920, height=100)
        self.frame.configure(fg_color="gold1")
        self.frame.place(x=0, y=0)

        self.lbl = customtkinter.CTkLabel(self.frame, text="Queue Representation", corner_radius=10)
        self.lbl.configure(fg_color="gold1", text_color="black",font=customtkinter.CTkFont(size=35, family='Segoe UI Black'))
        self.lbl.place(x=590, y=25)

        self.f1 = customtkinter.CTkFrame(self.root, width=550, height=620, corner_radius=20)
        self.f1.configure(fg_color="white",border_width=1, border_color='black')
        self.f1.place(x=50, y=135)

        self.line = customtkinter.CTkLabel(self.f1, text="_______________________", corner_radius=10)
        self.line.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=26, family='Segoe UI Black', weight='bold'))
        self.line.place(x=135, y=70)

        self.l1 = customtkinter.CTkLabel(self.f1, text="Ticket Counter", corner_radius=10)
        self.l1.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=26, family='Segoe UI Black'))
        self.l1.place(x=160,y=60)

        self.id_lbl = customtkinter.CTkLabel(self.f1, text="Ticket id", corner_radius=10)
        self.id_lbl.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=24, family='Segoe UI', weight='bold'))
        self.id_lbl.place(x=50, y=165)

        self.id_ety = customtkinter.CTkEntry(self.f1, width=210, height=40, placeholder_text="Ticket id", corner_radius=10)
        self.id_ety.configure(fg_color='white', font=customtkinter.CTkFont(size=15, family='Segoe UI'))
        self.id_ety.place(x=260, y=165)

        self.name_lbl = customtkinter.CTkLabel(self.f1, text="Movie Name", corner_radius=10)
        self.name_lbl.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=24, family='Segoe UI', weight='bold'))
        self.name_lbl.place(x=50, y=240)

        self.name_ety = customtkinter.CTkEntry(self.f1, width=210, height=40, placeholder_text="Name", corner_radius=10)
        self.name_ety.configure(fg_color='white', font=customtkinter.CTkFont(size=15, family='Segoe UI'))
        self.name_ety.place(x=260, y=240)

        self.price_lbl = customtkinter.CTkLabel(self.f1, text="Price", corner_radius=10)
        self.price_lbl.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=24, family='Segoe UI', weight='bold'))
        self.price_lbl.place(x=50, y=315)

        self.price_ety = customtkinter.CTkEntry(self.f1, width=210, height=40, placeholder_text="Price", corner_radius=10)
        self.price_ety.configure(fg_color='white', font=customtkinter.CTkFont(size=15, family='Segoe UI'))
        self.price_ety.place(x=260, y=315)

        self.b3 = customtkinter.CTkButton(self.f1, text="Add", width=150, corner_radius=20)
        self.b3.configure(fg_color=("gold1"), text_color="black",font=customtkinter.CTkFont(size=23, family='Segoe UI', weight='bold'), command=self.enqueue, hover_color='cornflowerblue')
        self.b3.place(x=80,y=420)

        self.b1 = customtkinter.CTkButton(self.f1, text="Update", width=150, corner_radius=20)
        self.b1.configure(fg_color=("gold1"), text_color="black",font=customtkinter.CTkFont(size=23, family='Segoe UI', weight='bold'), hover_color='cornflowerblue')
        self.b1.place(x=180, y=490)

        self.b2 = customtkinter.CTkButton( self.f1, text="Remove", width=150, corner_radius=20)
        self.b2.configure(fg_color=("gold1"), text_color="black",command=self.dequeue, font=customtkinter.CTkFont(size=23, family='Segoe UI', weight='bold'), hover_color='cornflowerblue')
        self.b2.place(x=280, y=420)

        self.f2 = customtkinter.CTkScrollableFrame(self.root, width=800, height=480, corner_radius=20)
        self.f2.configure(fg_color="white",border_width=1, border_color='black')
        self.f2.place(x=645, y=130)

        self.root.mainloop()

    def enqueue(self):
        self.id = self.id_ety.get()
        self.name = self.name_ety.get()
        self.price = self.price_ety.get()
        
        if self.id and self.name and self.price:
            if self.id!=None or self.name!=None or self.price!=None:

                special_characters = "!@#$%^&*()_+}~`-=;'/.,<>?|"
                if any(char in special_characters for char in self.name):
                    messagebox.showinfo("info", "Invalid name")
                #elif any(ch.isdigit() for ch in self.name):
                #     messagebox.showinfo("info", "Invalid name")
                elif any(char in special_characters for char in self.price):
                    messagebox.showinfo("info", "Invalid price")
                elif any(ch.isalpha() for ch in self.price):
                    messagebox.showinfo("info", "Invalid price")
                else:
                    self.frm = customtkinter.CTkFrame(self.f2, width=780, height=80, corner_radius=20)
                    self.frm.configure(fg_color="beige",border_width=1, border_color='black')
                    self.frm.pack()
                    
                    self.id_lbl = customtkinter.CTkLabel(self.frm, text="Ticket id :", corner_radius=10)
                    self.id_lbl.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=18, family='Segoe UI Black'))
                    self.id_lbl.place(x=20, y=25)
                                
                    label1 = customtkinter.CTkLabel(self.frm, text=self.id, corner_radius=10)
                    label1.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=18, family='Segoe UI', weight='bold'))
                    label1.place(x=135,y=25)

                    self.name_lbl = customtkinter.CTkLabel(self.frm, text="Name :", corner_radius=10)
                    self.name_lbl.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=18, family='Segoe UI Black'))
                    self.name_lbl.place(x=270, y=25)
                                    
                    label2 = customtkinter.CTkLabel(self.frm, text=self.name, corner_radius=10)
                    label2.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=18, family='Segoe UI', weight='bold'))
                    label2.place(x=365, y=25)

                    self.price_lbl = customtkinter.CTkLabel(self.frm, text="Price :", corner_radius=10)
                    self.price_lbl.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=18, family='Segoe UI Black'))
                    self.price_lbl.place(x=520, y=25)

                    label2 = customtkinter.CTkLabel(self.frm, text=self.price , corner_radius=10)
                    label2.configure(fg_color="white", text_color="black",font=customtkinter.CTkFont(size=18, family='Segoe UI', weight='bold'))
                    label2.place(x=605, y=25)
                    
        else:
            messagebox.showinfo("info", "Please fill all details")

    def dequeue(self):
        #self.frm.destroy()
        if self.frm.winfo_exists():
            self.frm.destroy()
        else:
            messagebox.showinfo("info","Queue is empty")


t1 = TicketCounterQueueApp()


