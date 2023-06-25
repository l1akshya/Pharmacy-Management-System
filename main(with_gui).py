from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import tkinter.font as tkfont
user=0
import csv
import sys
import text_extraction
import bill_2
from bill_2 import generate_bill
import bill
from bill import pdf_creater
from text_extraction import image_to_text
f=open("medicinerepo.csv",'r')
main_data=f.read()
main_data=main_data.split('\n')
main_data=(list(filter(None,main_data)))

def delete_csv_contents_except_first_line(file_path):
    # Read the first line of the CSV file
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
    
    # Overwrite the file with the first line
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
delete_csv_contents_except_first_line("bill_temp.csv")

def new_page(pill):
    frame=Tk()
    frame.resizable(0,0)
    frame.geometry("1168x648")
    frame.title("Pharmacy Management System")
    frame.iconbitmap('icon.ico')
    background2=ImageTk.PhotoImage(file=pill)
    background2_label=Label(frame,image=background2)
    background2_label.place(x=0,y=-20)
    normal_image2 = tk.PhotoImage(file="logout_1.png")
    hover_image2 = tk.PhotoImage(file="logout_2.png")
    def on_enter_button2(event):
        button2.config(image=hover_image2)
    def back_to_login():
        frame.destroy()
        login_page()
    def on_leave_button2(event):
        button2.config(image=normal_image2)
    button2 = tk.Button(frame, image=normal_image2, borderwidth=0, highlightthickness=0,command=back_to_login)
    button2.place(x=876+20+100+50,y=328-20-20+5+1+100+100+50)
    button2.bind("<Enter>", on_enter_button2)
    button2.bind("<Leave>", on_leave_button2)
    add_medicine=ImageTk.PhotoImage(file='add_medicine.png')
    def commander():
        frame.destroy()
        add_medicine_page(pill)
    button_add_medicine = tk.Button(frame, image=add_medicine, borderwidth=0, highlightthickness=0,command=commander)
    button_add_medicine.place(x=876-300-50-20-20,y=328-150-50)
    remove_medicine=ImageTk.PhotoImage(file='remove_medicine.png')
    def commander_remove():
        frame.destroy()
        remove_medicine_page(pill)
    def commander_show():
        frame.destroy()
        show_medicine_page(pill)
    def commander_search():
        frame.destroy()
        search_medicine_page(pill)
    def commander_bill():
        generate_bill("bill_temp.csv","bill.txt")
        messagebox.showinfo("Pharmacy Management System","Bill Generated Successfully")
        pdf_creater()
    button_remove_medicine = tk.Button(frame, image=remove_medicine, borderwidth=0, highlightthickness=0,command=commander_remove)
    button_remove_medicine.place(x=876-300-50-20-20,y=328-100)
    search_medicine=ImageTk.PhotoImage(file='search_medicine.png')
    button_search_medicine = tk.Button(frame, image=search_medicine, borderwidth=0, highlightthickness=0,command=commander_search)
    button_search_medicine.place(x=876-300-50-20-20,y=328)
    display_medicine=ImageTk.PhotoImage(file='display_medicine.png')
    button_display_medicine = tk.Button(frame, image=display_medicine, borderwidth=0, highlightthickness=0,command=commander_show)
    button_display_medicine.place(x=876-300-50-20-20,y=328+100)
    bill_medicine=ImageTk.PhotoImage(file='bill_generator.png')
    button_bill_medicine = tk.Button(frame, image=bill_medicine, borderwidth=0, highlightthickness=0,command=commander_bill)
    button_bill_medicine.place(x=876-300-50-20-20,y=328+100+50+100)
    frame.mainloop()

def add_medicine_page(pill):
    frame2=Tk()
    frame2.resizable(0,0)
    frame2.geometry("1168x648")
    frame2.title("Pharmacy Management System")
    frame2.iconbitmap('icon.ico')
    background2=ImageTk.PhotoImage(file=pill)
    background2_label=Label(frame2,image=background2)
    background2_label.place(x=0,y=-20)
    options=ImageTk.PhotoImage(file="adder_1.png")
    options_label=Label(frame2,image=options)
    options_label.place(x=100+100+150+150-80-80,y=100-15+3)
    options_2=ImageTk.PhotoImage(file="adder_2.png")
    options_2_label=Label(frame2,image=options_2)
    options_2_label.place(x=100+100+150+150-80-80,y=100-15+3+100)
    options_3=ImageTk.PhotoImage(file="adder_3.png")
    options_3_label=Label(frame2,image=options_3)
    options_3_label.place(x=100+100+150+150-80-80,y=100-15+3+100+100)
    options_4=ImageTk.PhotoImage(file="adder_4.png")
    options_4_label=Label(frame2,image=options_4)
    options_4_label.place(x=100+100+150+150-80-80,y=100-15+3+100+100+100)
    options_5=ImageTk.PhotoImage(file="adder_5.png")
    options_5_label=Label(frame2,image=options_5)
    options_5_label.place(x=100+100+150+150-80-80,y=100-15+3+100+100+100+100)
    return_button=ImageTk.PhotoImage(file='return_button.png')
    def commander_2():
        frame2.destroy()
        new_page(pill)
    button_return = tk.Button(frame2, image=return_button, borderwidth=0, highlightthickness=0,command=commander_2)
    button_return.place(x=876+20+100+50,y=328-20-20+5+1+100+100+50)
    custom_font = tkfont.Font(family="Times New Roman", size=10)
    x1=600-10
    medicine_input=Entry(frame2,width=25,bg="white",fg="purple",font=custom_font)
    medicine_input.place(x=x1,y=100)
    medicine_company=Entry(frame2,width=25,bg="white",fg="purple",font=custom_font)
    medicine_company.place(x=x1,y=200)
    medicine_formula=Entry(frame2,width=25,bg="white",fg="purple",font=custom_font)
    medicine_formula.place(x=x1,y=300)
    medicine_price=Entry(frame2,width=25,bg="white",fg="purple",font=custom_font)
    medicine_price.place(x=x1,y=400)
    medicine_quantity=Entry(frame2,width=25,bg="white",fg="purple",font=custom_font)
    medicine_quantity.place(x=x1,y=500)
    add_button=ImageTk.PhotoImage(file='adder.png')
    def commander_3():
        messagebox.showinfo("Pharmacy Management System","Medicine Added Successfully")
        medicine_name=medicine_input.get()
        medicine_company_name=medicine_company.get()
        medicine_formula_name=medicine_formula.get()
        medicine_price_name=medicine_price.get()
        medicine_quantity_name=medicine_quantity.get()
        stringer=(f"{medicine_name},{medicine_company_name},{medicine_formula_name},{medicine_quantity_name},{medicine_price_name}")
        def add_string_to_csv(filename, string):
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(string.split(","))
                writer.writerow()
        add_string_to_csv("medicinerepo.csv", stringer)
        medicine_input.delete(0, tk.END)
        medicine_company.delete(0, tk.END)
        medicine_formula.delete(0, tk.END)
        medicine_price.delete(0, tk.END)
        medicine_quantity.delete(0, tk.END)
    button_add = tk.Button(frame2, image=add_button, borderwidth=0, highlightthickness=0,command=commander_3)
    button_add.place(x=876+20+100+50-100-200-100-30-30,y=328-20-20+5+1+100+100+50+40)
    def next_entry(event):
        event.widget.tk_focusNext().focus()
    medicine_input.bind("<Return>", next_entry)
    medicine_company.bind("<Return>", next_entry)
    medicine_formula.bind("<Return>", next_entry)
    medicine_price.bind("<Return>", next_entry)
    def on_enter_press(event):
        button_add.invoke()
    medicine_quantity.bind("<Return>", on_enter_press)
    frame2.mainloop()

def show_medicine_page(pill):
    frame2=Tk()
    frame2.resizable(0,0)
    frame2.geometry("1168x648")
    frame2.title("Pharmacy Management System")
    frame2.iconbitmap('icon.ico')
    background2=ImageTk.PhotoImage(file=pill)
    background2_label=Label(frame2,image=background2)
    background2_label.place(x=0,y=-20)
    return_button=ImageTk.PhotoImage(file='return_button.png')
    options=ImageTk.PhotoImage(file="inventory.png")
    options_label=Label(frame2,image=options)
    options_label.place(x=100+100+150+150-80-80+10+100,y=100-15+3+20+30)
    def commander_2():
        frame2.destroy()
        new_page(pill)
    def display_csv_data(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        canvas = tk.Canvas(frame2)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.place(x=300+100,y=300-100)
        for row_index, row in enumerate(data):
            for col_index, value in enumerate(row):
                label = tk.Label(canvas, text=value, borderwidth=1, relief="solid")
                label.grid(row=row_index, column=col_index, padx=5, pady=5)
    
    csv_file = 'medicinerepo.csv'
    display_csv_data(csv_file)
    button_return = tk.Button(frame2, image=return_button, borderwidth=0, highlightthickness=0,command=commander_2)
    button_return.place(x=876+20+100+50,y=328-20-20+5+1+100+100+50)
    frame2.mainloop()

def search_medicine_page(pill):
    frame2=Tk()
    frame2.resizable(0,0)
    frame2.geometry("1168x648")
    frame2.title("Pharmacy Management System")
    frame2.iconbitmap('icon.ico')
    background2=ImageTk.PhotoImage(file=pill)
    background2_label=Label(frame2,image=background2)
    background2_label.place(x=0,y=-20)
    return_button=ImageTk.PhotoImage(file='return_button.png')
    a=-1
    def command_name():
        a=0
        frame2.destroy()
        search_page(pill,a)
    def command_company():
        a=1
        frame2.destroy()
        search_page(pill,a)
    def command_formula():
        a=2
        frame2.destroy()
        search_page(pill,a)
    def command_image():
        a=3
        frame2.destroy()
        search_page(pill,a)
    def commander_2():
        frame2.destroy()
        new_page(pill)
    button_return = tk.Button(frame2, image=return_button, borderwidth=0, highlightthickness=0,command=commander_2)
    button_return.place(x=876+20+100+50,y=328-20-20+5+1+100+100+50)
    search_medicine_name=ImageTk.PhotoImage(file='search_name.png')
    button_search_medicine_name = tk.Button(frame2, image=search_medicine_name, borderwidth=0, highlightthickness=0,command=command_name)
    button_search_medicine_name.place(x=876-300-50-20-20-100-50-30,y=328+100-200-50+30)
    search_medicine_company=ImageTk.PhotoImage(file='search_company.png')
    button_search_medicine_company = tk.Button(frame2, image=search_medicine_company, borderwidth=0, highlightthickness=0,command=command_company)
    button_search_medicine_company.place(x=876-300-50-20-20-100-50-30+300+70,y=328+100-200-50+30)
    search_medicine_formula=ImageTk.PhotoImage(file='search_formula.png')
    button_search_medicine_formula = tk.Button(frame2, image=search_medicine_formula, borderwidth=0, highlightthickness=0,command=command_formula)
    button_search_medicine_formula.place(x=876-300-50-20-20-100-50-30,y=328+100-200-50+30+200-100)
    search_medicine_image=ImageTk.PhotoImage(file='search_image.png')
    button_search_medicine_image = tk.Button(frame2, image=search_medicine_image, borderwidth=0, highlightthickness=0,command=command_image)
    button_search_medicine_image.place(x=876-300-50-20-20-100-50-30+300+70,y=328+100-200-50+30+200-100)
    frame2.mainloop()

def search_page(pill,a):
    frame2=Tk()
    frame2.resizable(0,0)
    frame2.geometry("1168x648")
    frame2.title("Pharmacy Management System")
    frame2.iconbitmap('icon.ico')
    background2=ImageTk.PhotoImage(file=pill)
    background2_label=Label(frame2,image=background2)
    background2_label.place(x=0,y=-20)
    return_button=ImageTk.PhotoImage(file='return_button.png')
    x1=600
    custom_font = tkfont.Font(family="Times New Roman", size=10)
    medicine_search=Entry(frame2,width=25,bg="white",fg="purple",font=custom_font)
    medicine_search.place(x=x1,y=100)
    def commander_2():
        frame2.destroy()
        search_medicine_page(pill)
    button_return = tk.Button(frame2, image=return_button, borderwidth=0, highlightthickness=0,command=commander_2)
    button_return.place(x=876+20+100+50,y=328-20-20+5+1+100+100+50)
    x1=340
    y1=88
    searcher=ImageTk.PhotoImage(file="export_name.png")
    search_label=Label(frame2,image=searcher)
    search_label.place(x=x1,y=y1)
    if a==0:
        searcher=ImageTk.PhotoImage(file="export_name.png")
        search_label=Label(frame2,image=searcher)
        search_label.place(x=x1,y=y1)
    if a==1:
        searcher=ImageTk.PhotoImage(file="export_company.png")
        search_label=Label(frame2,image=searcher)
        search_label.place(x=x1,y=y1)
    if a==2:
        searcher=ImageTk.PhotoImage(file="export_formula.png")
        search_label=Label(frame2,image=searcher)
        search_label.place(x=x1,y=y1)
    if a==3:
        searcher=ImageTk.PhotoImage(file="export_image.png")
        search_label=Label(frame2,image=searcher)
        search_label.place(x=x1,y=y1)

    def commander_search():
        if a==1 or a==0 or a==2:
            search_and_copy_csv(input_filename, output_filename, medicine_search.get())
        if a==3:
            search=image_to_text(medicine_search.get())
            search_and_copy_csv(input_filename, output_filename, search)
        display_csv_data(csv_file2)

    def display_csv_data(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        canvas = tk.Canvas(frame2)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.place(x=300+100,y=300-100)
        for row_index, row in enumerate(data):
            for col_index, value in enumerate(row):
                label = tk.Label(canvas, text=value, borderwidth=1, relief="solid")
                label.grid(row=row_index, column=col_index, padx=5, pady=5)
    
    csv_file2 = 'temp.csv'
    search_medicine_image=ImageTk.PhotoImage(file='search.png')
    button_search_medicine_image = tk.Button(frame2, image=search_medicine_image, borderwidth=0, highlightthickness=0,command=commander_search)
    button_search_medicine_image.place(x=x1+420,y=y1+3)

    if a==0 or a==1 or a==2:
        def search_and_copy_csv(input_file, output_file, search_value):
            with open(input_file, 'r') as file_in:
                reader = csv.reader(file_in)
                entry_searched=False
                with open(output_file, 'w', newline='') as file_out:
                    writer = csv.writer(file_out)
                    for row in reader:
                        if row and row[a] == search_value:
                            entry_searched=True
                            writer.writerow(row)
    if a==3:
        def search_and_copy_csv(input_file, output_file, search_value):
            with open(input_file, 'r') as file_in:
                reader = csv.reader(file_in)
                with open(output_file, 'w', newline='') as file_out:
                    entry_searched=False
                    writer = csv.writer(file_out)
                    for row in reader:
                        if row and row[0] == search_value:
                            entry_searched=True
                            writer.writerow(row)

    def add_csv_contents(source_file, destination_file, delimiter=','):
        with open(source_file, 'r', newline='') as file_in:
            reader = csv.reader(file_in, delimiter=delimiter)
            with open(destination_file, 'a', newline='') as file_out:
                writer = csv.writer(file_out, delimiter=delimiter)
                for row in reader:
                    writer.writerow(row)
    def billing():
        add_csv_contents('temp.csv', 'bill_temp.csv')

    biller_image=ImageTk.PhotoImage(file='biller.png')
    button_biller = tk.Button(frame2, image=biller_image, borderwidth=0, highlightthickness=0,command=billing)
    button_biller.place(x=x1,y=y1+3+300)
    def on_enter_press(event):
        button_search_medicine_image.invoke()
    medicine_search.bind("<Return>", on_enter_press)
    input_filename = 'medicinerepo.csv'
    output_filename = 'temp.csv'
    frame2.mainloop()

def remove_medicine_page(pill):
    frame2=Tk()
    frame2.resizable(0,0)
    frame2.geometry("1168x648")
    frame2.title("Pharmacy Management System")
    frame2.iconbitmap('icon.ico')
    background2=ImageTk.PhotoImage(file=pill)
    background2_label=Label(frame2,image=background2)
    background2_label.place(x=0,y=-20)
    options=ImageTk.PhotoImage(file="adder_1.png")
    options_label=Label(frame2,image=options)
    options_label.place(x=100+100+150+150-80-80,y=100-15+3+100)
    custom_font = tkfont.Font(family="Times New Roman", size=10)
    medicine_input=Entry(frame2,width=25,bg="white",fg="purple",font=custom_font)
    medicine_input.place(x=100+100+150+150-80-80+200+50,y=100-15+3+100+20-10)
    return_button=ImageTk.PhotoImage(file='return_button.png')
    def commander_2():
        frame2.destroy()
        new_page(pill)
    def remove_command():
        remove_medicine=medicine_input.get()
        def remove_entry_from_csv(filename, search_value):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)

            entry_removed = False

            for row in data:
                if search_value in row:
                    data.remove(row)
                    entry_removed = True

            if entry_removed:
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)

                messagebox.showinfo("Pharmacy Management System","Medicine removed Successfully")
            else:
                messagebox.showinfo("Pharmacy Management System","Medicine not found")
        medicine_input.delete(0, tk.END)
        remove_entry_from_csv("medicinerepo.csv", remove_medicine)

    remove_button=ImageTk.PhotoImage(file='remove.png')
    button_remove = tk.Button(frame2, image=remove_button, borderwidth=0, highlightthickness=0,command=remove_command)
    button_remove.place(x=100+100+150+150-80-80+200+50+25+50+50+30,y=100-15+3+100+20-10-10)
    button_return = tk.Button(frame2, image=return_button, borderwidth=0, highlightthickness=0,command=commander_2)
    button_return.place(x=876+20+100+50,y=328-20-20+5+1+100+100+50)
    def on_enter_press(event):
        button_remove.invoke()
    medicine_input.bind("<Return>", on_enter_press)
    frame2.mainloop()

def login_page():
    def login():
        if login_name_input.get()=="Lokesh":
            if password_input.get()=="221010226":
                #print('Login Successful')
                user=1
                root.destroy()
                new_page('pill2.png')
            else:
                messagebox.showinfo("Pharmacy Management System","Incorrect Password")
                password_input.delete(0, tk.END)
        elif login_name_input.get()=="Krishna":
            if password_input.get()=="221010225":
                #print('Login Successful')
                user=2
                root.destroy()
                new_page('pill2b.png')
            else:
                print('Incorrect Password')
                messagebox.showinfo("Pharmacy Management System","Incorrect Password")
                password_input.delete(0, tk.END)
        else:
            messagebox.showinfo("Pharmacy Management System","Invalid Username")
            login_name_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
    root = Tk()
    root.resizable(0,0)
    root.geometry("1168x648")
    background=ImageTk.PhotoImage(file='pill.png')
    background_label=Label(root,image=background)
    background_label.place(x=0,y=0)
    root.title("Pharmacy Management System")
    root.iconbitmap('icon.ico')
    custom_font = tkfont.Font(family="Times New Roman", size=10)
    def on_enter_button1(event):
        button.config(image=hover_image1)

    def on_leave_button1(event):
        button.config(image=normal_image1)

    def on_enter_button2(event):
        button2.config(image=hover_image2)

    def on_leave_button2(event):
        if pressed==0:
            button2.config(image=normal_image2)
    normal_image1 = tk.PhotoImage(file="button_normal.png")
    hover_image1 = tk.PhotoImage(file="button_hover.png")
    button = tk.Button(root, image=normal_image1, borderwidth=0, highlightthickness=0,command=login)
    button.place(x=776,y=328)

    button.bind("<Enter>", on_enter_button1)
    button.bind("<Leave>", on_leave_button1)

    pressed=0
    normal_image2 = tk.PhotoImage(file="button_normal_1.png")
    hover_image2 = tk.PhotoImage(file="button_hover_1.png")

    def oni():
        if password_input['show'] == '*':
            password_input.config(show="")
        else:
            password_input.config(show="*")

    login_name_input=Entry(root,width=25,bg="white",fg="purple",font=custom_font)
    login_name_input.place(x=730,y=250)
    password_input=Entry(root,width=25,bg="white",fg="purple",font=custom_font,show="*")
    password_input.place(x=730,y=295)
    def next_entry(event):
        event.widget.tk_focusNext().focus()
    login_name_input.bind("<Return>", next_entry)
    def on_enter_press(event):
        button.invoke()
    password_input.bind("<Return>", on_enter_press)

    button2 = tk.Button(root, image=normal_image2, borderwidth=0, highlightthickness=0,command=oni)
    button2.place(x=876+20,y=328-20-20+5+1)

    button2.bind("<Enter>", on_enter_button2)
    button2.bind("<Leave>", on_leave_button2)
    normal_image3 = tk.PhotoImage(file="close_normal.png")
    hover_image3 = tk.PhotoImage(file="close_hover.png")
    def shut_down():
        root.destroy()
        sys.exit()
    button3 = tk.Button(root, image=normal_image3, borderwidth=0, highlightthickness=0,command=shut_down)
    button3.place(x=876+20+100+20+100-20+5+5,y=328-20-20+5+1+100+100+50+20)
    def on_enter_button3(event):
        button3.config(image=hover_image3)

    def on_leave_button3(event):
        if pressed==0:
            button3.config(image=normal_image3)
    button3.bind("<Enter>", on_enter_button3)
    button3.bind("<Leave>", on_leave_button3)

    root.mainloop()

login_page()