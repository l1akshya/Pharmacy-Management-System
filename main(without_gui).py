import os
import csv
import datetime
from PIL import Image
from pytesseract import pytesseract
import enum
import re
import text_extraction
from text_extraction import image_to_text
import bill_2
from bill_2 import generate_bill
import bill
from bill import pdf_creater
temp_var=""

def delete_csv_contents_except_first_line(file_path):
    # Read the first line of the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
    
    # Overwrite the file with the first line
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)

f=open("medicinerepo.csv",'r')
main_data=f.read()
main_data=main_data.split('\n')
main_data=(list(filter(None,main_data)))

class admin:
    __usernames=['Lokesh','Krishna']
    __passwords=['221010226','221010225']
    def check1(self,username):
        if username in self.__usernames:
            index=self.__usernames.index(username)
            p=input("Enter your password :")
            if p==self.__passwords[index]:
                return True
            else:
                print("Incorrect Password!")
                return False
        else:
            print("Incorrect Username!")
            return False

        
class medicine_system:
    def init(self,medicine_name='',medicine_company='',medicine_formula='',quantity=0,cost=0):
            self.quantity=quantity
            self.medicine_name = medicine_name
            self.medicine_company = medicine_company
            self.medicine_formula = medicine_formula
            self.cost=cost
    def write_file(self,list_data):
            f = open("medicinerepo.csv", "w")
            all_data = str()
            for data in list_data:
                    all_data += data+'\n'
            f.write(all_data)
            f.close()
            return True
    def show_medicine(self):
            if main_data!=[]:
                for data in main_data:
                        if data!=[]:
                            split_data=data.split(',')
                            print("Medicine_Name :",split_data[0])
                            print("Medicine_Company :",split_data[1])
                            print("Medicine_Formula :",split_data[2])
                            print("Quantity :",split_data[3])
                            print("cost:",split_data[4])
                            print("-------------------------")
            else:
                print("No Records found")
                                  
    def add_medicine(self):
            medicine_name = input("Enter Name of the medicine :")
            medicine_company =input("Enter the name of the company of the medicine :")
            medicine_formula =input("Enter the formula of the medicine :")
            quantity=input("Enter quantity :")
            cost=input("Enter cost:")
            data=medicine_name+','+medicine_company+','+medicine_formula+ ','+quantity+','+cost+'\n'
            f = open("medicinerepo.csv", "a")
            f.write(data)
            f.close()
            print("Medicine Added Succeffully")

    def search_by_medicine_company(self,no):
            for data in main_data:
                split_data=data.split(',')
                if no==split_data[1]:
                    split_data=data.split(',')
                    print("Medicine_Name :",split_data[0])
                    print("Medicine_Company :",split_data[1])
                    print("Medicine_Formula :",split_data[2])
                    print("Quantity :",split_data[3])
                    print("Cost:",split_data[4])
                    medicine_name=split_data[0]
                    medicine_company=split_data[1]
                    medicine_formula=split_data[2]
                    quantity=split_data[3]
                    cost=split_data[4]
                    dataz=medicine_name+','+medicine_company+','+medicine_formula+ ','+quantity+','+cost+'\n'
                    return dataz

    def search_by_Image(self,no):
            for data in main_data:
                split_data=data.split(',')
                if no==split_data[0]:
                    split_data=data.split(',')
                    print("Medicine_Name :",split_data[0])
                    print("Medicine_Company :",split_data[1])
                    print("Medicine_Formula :",split_data[2])
                    print("Quantity :",split_data[3])
                    print("Cost:",split_data[4])
                    medicine_name=split_data[0]
                    medicine_company=split_data[1]
                    medicine_formula=split_data[2]
                    quantity=split_data[3]
                    cost=split_data[4]
                    dataz=medicine_name+','+medicine_company+','+medicine_formula+ ','+quantity+','+cost+'\n'
                    return dataz
                    break

    def search_by_medicine_name(self,name):
            for data in main_data:
                split_data=data.split(',')
                if name==split_data[0]:
                    print("Medicine_Name :",split_data[0])
                    print("Medicine_Company :",split_data[1])
                    print("Medicine_Formula :",split_data[2])
                    print("Quantity :",split_data[3])
                    print("Cost:",split_data[4])
                    medicine_name=split_data[0]
                    medicine_company=split_data[1]
                    medicine_formula=split_data[2]
                    quantity=split_data[3]
                    cost=split_data[4]
                    dataz=medicine_name+','+medicine_company+','+medicine_formula+ ','+quantity+','+cost+'\n'
                    return dataz
                    break
    def search_by_formula(self,group):
            for data in main_data:
                split_data=data.split(',')
                if group==split_data[2]:
                    print("Medicine_Name :",split_data[0])
                    print("Medicine_Company :",split_data[1])
                    print("Medicine_Formula :",split_data[2])
                    print("Quantity :",split_data[3])
                    print("Cost:",split_data[4])
                    medicine_name=split_data[0]
                    medicine_company=split_data[1]
                    medicine_formula=split_data[2]
                    quantity=split_data[3]
                    cost=split_data[4]
                    dataz=medicine_name+','+medicine_company+','+medicine_formula+ ','+quantity+','+cost+'\n'
                    return dataz
                    print("-------------------------")
                
    def remove_medicine(self,no):        
            for data in main_data:
                split_data=data.split(',')
                if no==split_data[0]:
                    main_data.remove(data)
                    break
            if (self.write_file(main_data)):
                print("Successfully Deleted !")
            else:
                print("Try Again!! ")
                
    def search_name(self,no):
            for data in main_data:
               split_data=data.split(',')
               if no==split_data[0]:
                    return True
            return False
    
    def image(self,no):
            for data in main_data:
               split_data=data.split(',')
               if no==split_data[0]:
                    return True
            return False
    
    def search_company_name(self,name):
            for data in main_data:
               split_data=data.split(',')
               if name==split_data[1]:
                    return True
            return False
    def search_medicine_formula(self,group):
            for data in main_data:
               split_data=data.split(',')
               if group==split_data[2]:
                    return True
            return False

class runner(medicine_system,admin):
    def init(self):
            self
    def welcome():
            print( '\n'" >>>>>>>>>>> Welcome To pharmacy Management System <<<<<<<<<<<<")
    def menu():
            my_class=medicine_system()
            print( '\n'"""
                    1.=Medicine List
                    2.=Add Medicine
                    3.=Remove Medicine
                    4.=Search Medicine
                    5.=Exit
                    """)
            user_input=int(input("Please Enter option from above (1-5) : "))
            if user_input==1:
                my_class.show_medicine()
            elif user_input==2:
                u=input("Enter username: ")
                tempobj=admin()
                c=tempobj.check1(u)
                if c==True:
                    my_class.add_medicine()
            elif user_input==3:
                u=input("Enter username: ")
                tempobj=admin()
                c=tempobj.check1(u)
                if c==True:                    
                    num1=input("Enter medicine name to delete :")
                    if my_class.medicine_name(num1):
                        my_class.remove_medicine(num1)
                    else:
                        print("Incorrect medicine name!!")
            elif user_input==4:
                ch=int(input("Search by :\n 1. Name \n 2. Company Name\n 3. Formula\n 4. Image\n"))
                if ch==1:
                    num2=input("Enter name to search :")
                    if my_class.search_name(num2):
                        a=my_class.search_by_medicine_name(num2)
                        bill_input=int(input("do you want to add the search result to bill\n if yes press 1 if no press 2:-"))
                        if bill_input==1:
                            f = open("bill_temp.csv", "a")
                            f.write(a)
                            f.close() 
                            print("content added to bill successfully")
                elif ch==4:
                    numi=input("Enter Image path :")
                    num5=image_to_text(numi)
                    print(num5)
                    if my_class.image(num5):
                        a=my_class.search_by_Image(num5)
                        bill_input=int(input("do you want to add the search result to bill\n if yes press 1 if no press 2:-"))
                        if bill_input==1:
                            f = open("bill_temp.csv", "a")
                            f.write(a)
                            f.close() 
                            print("content added to bill successfully")
                    else:
                        print("medicine not found!!")
                elif ch==2:
                    num3=input("Enter Company Name to search :")
                    if my_class.search_company_name(num3):
                        a=my_class.search_by_medicine_company(num3)
                        bill_input=int(input("do you want to add the search result to bill\n if yes press 1 if no press 2:-"))
                        if bill_input==1:
                            f = open("bill_temp.csv", "a")
                            f.write(a)
                            f.close() 
                            print("content added to bill successfully")      
                    else:
                        print("Conmpany name not found!!")
                elif ch==3:
                    grps=set()
                    for data in main_data:
                        split_data=data.split(',')
                        grps.add(split_data[3])
                    for i in grps:
                        print(i)
                    num4=input("Enter formula to search :")
                    if my_class.search_medicine_formula(num4):
                        a=my_class.search_by_formula(num4)
                        a=my_class.search_by_medicine_company(num5)
                        bill_input=int(input("do you want to add the search result to bill\n if yes press 1 if no press 2:-"))
                        if bill_input==1:
                            f = open("bill_temp.csv", "a")
                            f.write(a)
                            f.close() 
                            print("content added to bill successfully")
                    else:
                        print("Formula not found!!")
                else:
                    print("Invalid option!")
                
            elif user_input==5:
                print("Thankyou for Using Our pharmacy Management System")
                quit()
            else:
                print("Invalid Input!!")

    a=1
    welcome()
    while (a==1):
        menu()
        a=int(input("""Do you want to continue?\n 1. YES\n 2. NO\n 3.Generate Bill \n"""))
        if (a==2):
            print("Thankyou for Using Our Pharmacy Management System")
            quit()
        if ((a!=1)and(a!=2))and(a!=3):
            print("Invalid option")
        if a==3:
            generate_bill("bill_temp.csv","bill.txt")
            delete_csv_contents_except_first_line("bill_temp.csv")
            pdf_creater()
            a==1

