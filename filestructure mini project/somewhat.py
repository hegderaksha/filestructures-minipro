import os
import re
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




def book_A_ride(id):
    print("booked")
    op='5'
    nv='NotAvailable'
    idd=id

    def modify(id,op,nv):
        print("mod starts")
        print("mod starts")
        ch=int(op)
        check=[id,ch,nv]
        temp=[]
        f=open('DriverData.txt','r')
        f.seek(0)
        lines=f.readlines()
        data=[]
        print(check)
    
        for l in lines:
            data.append(l.split(' '))
            for user in range(len(data)):
    
        
                if(data[user][0]== id):
                    if(ch==1):
                        data[user][1]=nv
                        break
                    if(ch==2):
                        data[user][2]=nv
                        break

                    if(ch==3):
                        data[user][3]=nv
                        break
                    if(ch==4):
                        data[user][4]=nv
                        break

                    if(ch==5):
                        data[user][5]=nv
                        break
                
            print(data)            
       
            with open('DriverData.txt', 'w') as f:
        
                print(len(data))
                for i in range(len(data)):
                    line=[]
            
                    for j in range(6):
                        line.append(data[i][j])
                        if (j<5):
                            line.append(' ')
                            #break
                             
                    
                    f.writelines(line)
                    #f.write("\n")

        messagebox.showinfo("Hurray", "Ride booked")  
    modify(idd,op,nv)

def complete_A_ride(id):
    print("booked")
    op='5'
    nv='Available'
    idd=id

    def modify(id,op,nv):
        print("mod starts")
        print("mod starts")
        ch=int(op)
        check=[id,ch,nv]
        temp=[]
        f=open('DriverData.txt','r')
        f.seek(0)
        lines=f.readlines()
        data=[]
        print(check)
    
        for l in lines:
            data.append(l.split(' '))
            for user in range(len(data)):
    
        
                if(data[user][0]== id):
                    if(ch==1):
                        data[user][1]=nv
                        break
                    if(ch==2):
                        data[user][2]=nv
                        break

                    if(ch==3):
                        data[user][3]=nv
                        break
                    if(ch==4):
                        data[user][4]=nv
                        break

                    if(ch==5):
                        data[user][5]=nv
                        break
                
            print(data)            
       
            with open('DriverData.txt', 'w') as f:
        
                print(len(data))
                for i in range(len(data)):
                    line=[]
            
                    for j in range(6):
                        line.append(data[i][j])
                        if (j<6):
                            line.append(' ')
                            #break
                             
               
                    f.writelines(line)
                    #f.write("\n")

        messagebox.showinfo("Hurray", "Ride completed")  
    modify(idd,op,nv)

"""def complete_A_ride(id):
    print("booked")
    op='5'
    nv='Available'
    idd=id
    def modify(id,op,nv):
            print("mod starts")

            ch=int(op)
            check=[id,ch,nv]
            temp=[]
            f=open('DriverData.txt','r')
            f.seek(0)
            lines=f.readlines()
            data=[]
            print(check)
    
            for l in lines:
        
                data.append(l.split(' '))
    
            for user in range(len(data)):
    
        
                if(data[user][0]== id):
                    if(ch==1):
                        data[user][1]=nv
                
                        #break
                    if(ch==2):
                        data[user][2]=nv
                
                        #break

                    if(ch==3):
                        data[user][3]=nv
                
                #break
                    if(ch==4):
                        data[user][4]=nv

                    if(ch==5):
                        data[user][5]=nv
                #break
            print(data)            
       
            with open('DriverData.txt', 'w') as f:
        
                print(len(data))
                for i in range(len(data)):
                    line=[]
            
                    for j in range(6):
                        line.append(data[i][j])
                        if (j<5):
                             line.append(' ')
               
                    f.writelines(line)
                    f.write("\n")

            messagebox.showinfo("Hurray", "Ride Completed")  
    modify(idd,op,nv)"""





def DisplayandSearch_D():
    def idataT(l1):
        tv.delete(*tv.get_children())
        print(l1)
        for i in l1:
            tv.insert('', 'end', values=i)
    def idataS(i):
        tv.delete(*tv.get_children())
    #for i in l1:
        tv.insert('', 'end', values=i)
    def search(IDD):
        print("search")
        
        #IDD = ID.get()
        print(IDD)
        with open ('DriverData.txt', 'r+') as f1:
            print("ish")
            lines=f1.readlines()
            l1=[line.strip() for line in lines]
            print(l1)
            for i in l1:
                """if i[0:3] == IDD:
                    l1=i
                    idataS(i)"""
                if i.startswith(IDD):
                    l1=i
                    print(i)
                    idataS(i)
        #print(l1)
            #idataS(l1)
        
    def display():
        global tv #, ID
        root=Tk()
        #ID=StringVar()   
    #ID=Stringvar()
    
        w1=LabelFrame(root, text="DT")
        w1.pack(fill="both", expand="yes", padx=20, pady=10)
        w2=LabelFrame(root, text="search")
        w2.pack(fill="both", expand="yes", padx=20, pady=10)
        w3=LabelFrame(root, text="bOOK")
        w3.pack(fill="both", expand="yes", padx=20, pady=10)
    

        tv = ttk.Treeview(w1, columns=(1,2,3,4,5,6), show="headings", height="6")
    
        tv.pack(expand="yes")

        tv.heading(1, text="ID")
        tv.heading(2, text="Name")
        tv.heading(3, text="Vtype")
        tv.heading(4, text="Vnum")
        tv.heading(5, text="Phnum")
        tv.heading(6, text="Availability")
        with open ('DriverData.txt', 'r+') as f1:
            lines=f1.readlines()
            l1=[line.strip() for line in lines]
            idataT(l1)
        print(l1)

        lbl=Label(w2, text="search")
        lbl.pack(side=tk.LEFT, padx=10)
        ent= Entry(w2, text="ID")
        ent.pack(side=tk.LEFT, padx=6)
        but= Button(w2, text="search", command= lambda:search(ent.get()))
        but.pack(side=tk.LEFT, padx=6)
        ent1= Entry(w3, text="Book")
        ent1.pack(side=tk.LEFT, padx=6)
        but1= Button(w3, text="Book", command= lambda:book_A_ride(ent1.get()))
        but1.pack(side=tk.LEFT, padx=6)
        ent2= Entry(w3, text="complete")
        ent2.pack(side=tk.LEFT, padx=6)
        but2= Button(w3, text="END", command= lambda:complete_A_ride(ent2.get()))
        but2.pack(side=tk.LEFT, padx=6)
    
    
        root.title("Display")
        root.mainloop()


    display()

def DisplayandSearch_P():
    def idataT(l1):
        tv.delete(*tv.get_children())
        print(l1)
        for i in l1:
            tv.insert('', 'end', values=i)
    def idataS(i):
        tv.delete(*tv.get_children())
    #for i in l1:
        tv.insert('', 'end', values=i)
    def search(IDD):
        print("search")
        
        #IDD = ID.get()
        print(IDD)
        with open ('PassengerData.txt', 'r+') as f1:
            print("ish")
            lines=f1.readlines()
            l1=[line.strip() for line in lines]
            print(l1)
            for i in l1:
                """if i[0:3] == IDD:
                    l1=i
                    idataS(i)"""
                if i.startswith(IDD):
                    l1=i
                    print(i)
                    idataS(i)
        #print(l1)
            #idataS(l1)
        
    def display():
        global tv #, ID
        root=Tk()
        #ID=StringVar()   
    #ID=Stringvar()
    
        w1=LabelFrame(root, text="DT")
        w1.pack(fill="both", expand="yes", padx=20, pady=10)
        w2=LabelFrame(root, text="search")
        w2.pack(fill="both", expand="yes", padx=20, pady=10)
    #w3=LabelFrame(root, text="DR")
    #w3.pack(fill="both", expand="yes", padx=20, pady=10)
    

        tv = ttk.Treeview(w1, columns=(1,2,3,4,5), show="headings", height="6")
    
        tv.pack(expand="yes")

        tv.heading(1, text="ID")
        tv.heading(2, text="Name")
        tv.heading(3, text="Age")
        tv.heading(4, text="Gender")
        tv.heading(5, text="Phnum")
        with open ('PassengerData.txt', 'r+') as f1:
            lines=f1.readlines()
            l1=[line.strip() for line in lines]
            idataT(l1)
        print(l1)

        lbl=Label(w2, text="search")
        lbl.pack(side=tk.LEFT, padx=10)
        ent= Entry(w2, text="ID")
        ent.pack(side=tk.LEFT, padx=6)
        but= Button(w2, text="search", command= lambda:search(ent.get()))
        but.pack(side=tk.LEFT, padx=6)
        ent1= Entry(w2, text="ID")
        ent1.pack(side=tk.RIGHT, padx=6)
        but1= Button(w2, text="Book", command= lambda:book_A_ride(ent1.get()))
        but1.pack(side=tk.RIGHT, padx=6)
    
    
        root.title("Display")
        root.mainloop()


    display()




def registerwin_D():
    def register():
        global register_screen
        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("300x300")
 
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
 
        Label(register_screen, text="Please enter details below", bg="pink").pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="pink", command = register_user).pack()
    

# login 
    def login():
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("300x300")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()
 
        global username_verify
        global password_verify
 
        username_verify = StringVar()
        password_verify = StringVar()
 
        global username_login_entry
        global password_login_entry
 
        Label(login_screen, text="Username * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

 
#  register button
 
    def register_user():
 
        username_info = username.get()
        password_info = password.get()
 
        file = open("Drivername_info.txt", "a")
        file.write(username_info +"|")
        file.write(password_info)
        file.write("\n")
        file.close()
 
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
 
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

        DriverStuffs()




 
#  login button 
    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
   # username_login_entry.delete(0, END)
   # password_login_entry.delete(0, END)
 
    #list_of_files = os.listdir()

   
        with open("Drivername_info.txt", "r+") as f1:
            list_of_files = f1.readlines()
            l1=[line.strip() for line in list_of_files]
            #print(l1)
        d={}
        x=[]
        for lx in l1:
            x=lx.split("|")
            #print(x)
      
            d[x[0]]=x[1]
        
        for key in d:
            if(username1 == key):
                if(password1 == d[key]):
                    login_sucess()
                    DriverStuffs()
                #print("login successful")
                    break
                else:
                    password_not_recognised()
                 # print("not successful")
                    break
                if(username1 != key):
                    user_not_found()
                    break
             
               
            
                        
 
#  popup for login success
 
    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=delete_login_success).pack()





 
#popup for login invalid password
    
    def password_not_recognised():
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# popup for user not found
 
    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
    def delete_login_success():
        login_success_screen.destroy()
 
 
    def delete_password_not_recognised():
        password_not_recog_screen.destroy()
 
 
    def delete_user_not_found_screen():
        user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
    def main_account_screen():
        mw.destroy()
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(text="Select Your Choice", bg="pink", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=register).pack()
 
        main_screen.mainloop()
 
 
    main_account_screen()

def registerwin_P():
    def register():
        global register_screen
        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("300x300")
 
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
 
        Label(register_screen, text="Please enter details below", bg="pink").pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="pink", command = register_user).pack()
    

# login 
    def login():
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("300x300")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()
 
        global username_verify
        global password_verify
 
        username_verify = StringVar()
        password_verify = StringVar()
 
        global username_login_entry
        global password_login_entry
 
        Label(login_screen, text="Username * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

 
#  register button
 
    def register_user():
 
        username_info = username.get()
        password_info = password.get()
 
        file = open("Passengername_info.txt", "a")
        file.write(username_info +"|")
        file.write(password_info)
        file.write("\n")
        file.close()
 
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
 
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        
        PassengerStuffs()




 
#  login button 
    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
   # username_login_entry.delete(0, END)
   # password_login_entry.delete(0, END)
 
    #list_of_files = os.listdir()

   
        with open("Passengername_info.txt", "r+") as f1:
            list_of_files = f1.readlines()
            l1=[line.strip() for line in list_of_files]
            #print(l1)
        d={}
        x=[]
        for lx in l1:
            x=lx.split("|")
            #print(x)
      
            d[x[0]]=x[1]
        
        for key in d:
            if(username1 == key):
                if(password1 == d[key]):
                    login_sucess()
                    PassengerStuffs()
                #print("login successful")
                    break
                else:
                    password_not_recognised()
                 # print("not successful")
                    break
                if(username1 != key):
                    user_not_found()
                    break
             
               
            
                        
 
#  popup for login success
 
    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=delete_login_success).pack()





 
#popup for login invalid password
    
    def password_not_recognised():
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# popup for user not found
 
    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
    def delete_login_success():
        login_success_screen.destroy()
 
 
    def delete_password_not_recognised():
        password_not_recog_screen.destroy()
 
 
    def delete_user_not_found_screen():
        user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
    def main_account_screen():
        mw.destroy()
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(text="Select Your Choice", bg="pink", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=register).pack()
 
        main_screen.mainloop()
 
 
    main_account_screen()
 
    
def DriverStuffs():
        
        def addData(ID, Name, Seater, Vnum, PHno):
                ind=[]
                DT=[ID, Name, Seater, Vnum, PHno, 'Available']
                
                with open('DriverData.txt', 'a') as f:
                        pos = f.tell()
                        f.writelines(' '.join(DT))
                        f.write('\n')
                messagebox.showinfo("Hurray", "Record ADDED") 
                with open('indexD.txt','a') as f2:
                        ind.append(ID)
                        ind.append(pos)
                        dump=map(str, ind)
                        print(ind)
                        f2.writelines("|".join(dump))
                        f2.write('\n')
        def delData(n):
            with open('indexD.txt','r+') as  f1, open('DriverData.txt','r+') as f2:
                lines = f1.readlines()
                lines_2 = f2.readlines()
                l1 = [line.strip() for line in lines]
                l2 = [line.strip() for line in lines_2]
       
    
            l1 = list(map(str, l1))
            l2 = list(map(str, l2))
            print(l1)
            print(l2)
            kv=[]
            dic={}
            for x in l1:
                kv=x.split('|')
                print(kv)
                #dic[kv[0]].append(kv[1])
                dic[kv[0]]=kv[1]
                print(dic)
            for key in dic:
                if (int(key)==int(n)):
                    for s in l2:
                        print(s)
                        if (int(s[0:3]) == int(n)):
                            l2.remove(s)
                        else:
                            print("not found")
                        with open('DriverData.txt','w') as f2:
                            f2.writelines('\n'.join(l2))
                            f2.write('\n')
                        
            """with open('indexD.txt','r+') as  f1:
                lines = f1.readlines()
                l1 = [line.strip() for line in lines]
                for x in l1:
                    kv=x.split('|')
                    print(kv)
                    my_dict[kv[0]].append(kv[1])"""
                
                
                
                        
                   
                
            
            #n =int(input('Enter a number: '))
            
                
                  

            

        def modify(id,op,nv):
            print("mod starts")

            ch=int(op)
            check=[id,ch,nv]
            temp=[]
            f=open('DriverData.txt','r')
            lines=f.readlines()
            data=[]
            print(check)
    
            for l in lines:
        
                data.append(l.split(' '))
    
            for user in range(len(data)):
    
        
                if(data[user][0]== id):
                    if(ch==1):
                        data[user][1]=nv
                
                        #break
                    if(ch==2):
                        data[user][2]=nv
                
                        #break

                    if(ch==3):
                        data[user][3]=nv
                
                #break
                    if(ch==4):
                        data[user][4]=nv

                    #if(ch==5):
                        #data[user][5]=1
                #break
            print(data)            
       
            with open('DriverData.txt', 'w') as f:
        
                print(len(data))
                for i in range(len(data)):
                    line=[]
            
                    for j in range(6):
                        line.append(data[i][j])
                        if (j<5):
                             line.append(' ')
               
                    f.writelines(line)
                    #f.write("\n")

            messagebox.showinfo("Hurray", "Record UPDATED")     
                
                
                           
        #f.write('\n')


        def modUI_D():
            master = tk.Tk()

            master.title("Update Data")
    
            tk.Label(master, text="ID").grid(row=1)
            tk.Label(master, text="Choose Value for op 1=name 2=Seater 3=VNUM 4=PHno").grid(row=2)
            tk.Label(master, text="OP").grid(row=4)
            tk.Label(master, text="New Value").grid(row=5)

            e1 = tk.Entry(master)
            e2 = tk.Entry(master)
            e3 = tk.Entry(master)
    

            e1.grid(row=1, column=1)
            e2.grid(row=4, column=1)
            e3.grid(row=5, column=1)
  
            tk.Button(master, text='update', command= lambda: modify(e1.get(), e2.get(), e3.get())).grid(row=7, column=0, pady=4)

    

            master.mainloop()

        def AddUI_D():
            master = tk.Tk()

            master.title("Drivers Data")
            tk.Label(master, text="Enter the details").grid(row=0)
            tk.Label(master, text="ID").grid(row=1)
            tk.Label(master, text=" Name").grid(row=2)
            tk.Label(master, text="Seater").grid(row=3)
            tk.Label(master, text="Vnum").grid(row=4)
            tk.Label(master, text="PhNO").grid(row=5)

            e1 = tk.Entry(master)
            e2 = tk.Entry(master)
            e3 = tk.Entry(master)
            e4 = tk.Entry(master)
            e5 = tk.Entry(master)

            e1.grid(row=1, column=1)
            e2.grid(row=2, column=1)
            e3.grid(row=3, column=1)
            e4.grid(row=4, column=1)
            e5.grid(row=5, column=1)
            tk.Button(master, text='Submit', command= lambda: addData(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())).grid(row=7, column=0, pady=4)

    

            master.mainloop()
        def DelUI_D():
            master = tk.Tk()

            master.title("Delete Data")
            tk.Label(master, text="Enter the ID to be Deleted").grid(row=0)
            tk.Label(master, text="ID").grid(row=1)
            e1 = tk.Entry(master)
            e1.grid(row=1, column=1)
            tk.Button(master, text='DELETE', command= lambda: delData(e1.get())).grid(row=3, column=0, pady=4)
            
        def main():
            mw=Tk()
            mw.title("DD")
            ml= Label(mw, text=" Welcome ")
            ml.pack()
            A =Button(mw, text ="add", height = 2, width = 25, bg='pink',command=AddUI_D)
            A.pack()
            D =Button(mw, text ="del", height = 2, width = 25, bg='pink',command=DelUI_D)
            D.pack()
            M =Button(mw, text ="mod", height = 2, width = 25,bg='pink', command=modUI_D)
            M.pack()
            S_D =Button(mw, text ="DispalyandSearch", height = 2, width = 25,bg='pink', command=DisplayandSearch_D)
            S_D.pack()
            mw.mainloop()
        main()


def PassengerStuffs():
        
        def addDataP(ID, Name, Age, Gender, PHno):
                ind=[]
                DT=[ID, Name, Age, Gender, PHno]
                with open('PassengerData.txt', 'a') as f:
                        pos = f.tell()
                        f.writelines(' '.join(DT))
                        f.write('\n')
                messagebox.showinfo("Hurray", "Record ADDED") 
                with open('indexP.txt','a') as f2:
                        ind.append(ID)
                        ind.append(pos)
                        dump=map(str, ind)
                        print(ind)
                        f2.writelines("|".join(dump))
                        f2.write('\n')
        def delDataP(n):
            with open('indexP.txt','r+') as  f1, open('PassengerData.txt','r+') as f2:
                lines = f1.readlines()
                lines_2 = f2.readlines()
                l1 = [line.strip() for line in lines]
                l2 = [line.strip() for line in lines_2]
       
    
            l1 = list(map(str, l1))
            l2 = list(map(str, l2))
            print(l1)
            print(l2)
            kv=[]
            dic={}
            for x in l1:
                kv=x.split('|')
                print(kv)
                #dic[kv[0]].append(kv[1])
                dic[kv[0]]=kv[1]
                print(dic)
            for key in dic:
                if (int(key)==int(n)):
                    for s in l2:
                        print(s)
                        if (int(s[0:3]) == int(n)):
                            l2.remove(s)
                        else:
                            print("not found")
                        with open('PassengerData.txt','w') as f2:
                            f2.writelines('\n'.join(l2))
                            f2.write('\n')
                        
            """with open('indexD.txt','r+') as  f1:
                lines = f1.readlines()
                l1 = [line.strip() for line in lines]
                for x in l1:
                    kv=x.split('|')
                    print(kv)
                    my_dict[kv[0]].append(kv[1])"""
                
                
                
                        
                   
                
            
            #n =int(input('Enter a number: '))
            
                
                  

            

        def modifyP(id,op,nv):
            print("mod starts")

            ch=int(op)
            check=[id,ch,nv]
            temp=[]
            f=open('PassengerData.txt','r')
            lines=f.readlines()
            data=[]
            print(check)
    
            for l in lines:
        
                data.append(l.split(' '))
    
            for user in range(len(data)):
    
        
                if(data[user][0]== id):
                    if(ch==1):
                        data[user][1]=nv
                
                        #break
                    if(ch==2):
                        data[user][2]=nv
                
                        #break

                    if(ch==3):
                        data[user][3]=nv
                
                #break
                    if(ch==4):
                        data[user][4]=nv
                
                #break
            print(data)            
       
            with open('PassengerData.txt', 'w') as f:
        
                print(len(data))
                for i in range(len(data)):
                    line=[]
            
                    for j in range(5):
                        line.append(data[i][j])
                        if (j<4):
                             line.append(' ')
               
                    f.writelines(line)

            messagebox.showinfo("Hurray", "Record UPDATED")     
                
                
                           
        #f.write('\n')


        def modUI_P():
            master = tk.Tk()

            master.title("Update Data")
    
            tk.Label(master, text="ID").grid(row=1)
            tk.Label(master, text="Choose Value for op 1=name 2=Age 3=Gender 4=PHno").grid(row=2)
            tk.Label(master, text="OP").grid(row=4)
            tk.Label(master, text="New Value").grid(row=5)

            e1 = tk.Entry(master)
            e2 = tk.Entry(master)
            e3 = tk.Entry(master)
    

            e1.grid(row=1, column=1)
            e2.grid(row=4, column=1)
            e3.grid(row=5, column=1)
  
            tk.Button(master, text='update', command= lambda: modifyP(e1.get(), e2.get(), e3.get())).grid(row=7, column=0, pady=4)

    

            master.mainloop()

        def AddUI_P():
            master = tk.Tk()

            master.title("Drivers Data")
            tk.Label(master, text="Enter the details").grid(row=0)
            tk.Label(master, text="ID").grid(row=1)
            tk.Label(master, text=" Name").grid(row=2)
            tk.Label(master, text="Age").grid(row=3)
            tk.Label(master, text="Gender").grid(row=4)
            tk.Label(master, text="PhNO").grid(row=5)

            e1 = tk.Entry(master)
            e2 = tk.Entry(master)
            e3 = tk.Entry(master)
            e4 = tk.Entry(master)
            e5 = tk.Entry(master)

            e1.grid(row=1, column=1)
            e2.grid(row=2, column=1)
            e3.grid(row=3, column=1)
            e4.grid(row=4, column=1)
            e5.grid(row=5, column=1)
            tk.Button(master, text='Submit', command= lambda: addDataP(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())).grid(row=7, column=0, pady=4)

    

            master.mainloop()
        def DelUI_P():
            master = tk.Tk()

            master.title("Delete Data")
            tk.Label(master, text="Enter the ID to be Deleted").grid(row=0)
            tk.Label(master, text="ID").grid(row=1)
            e1 = tk.Entry(master)
            e1.grid(row=1, column=1)
            tk.Button(master, text='DELETE', command= lambda: delDataP(e1.get())).grid(row=3, column=0, pady=4)
            
        def main():
            mw=Tk()
            mw.title("DD")
            ml= Label(mw, text=" Welcome ")
            ml.pack()
            A =Button(mw, text ="add", height = 2, width = 25, bg='pink',command=AddUI_P)
            A.pack()
            D =Button(mw, text ="del", height = 2, width = 25, bg='pink',command=DelUI_P)
            D.pack()
            M =Button(mw, text ="mod", height = 2, width = 25,bg='pink', command=modUI_P)
            M.pack()
            S_D =Button(mw, text ="DispalyandSearch", height = 2, width = 25,bg='pink', command=DisplayandSearch_D)
            S_D.pack()
            mw.mainloop()
        main()




def Eui():
    global mw
    mw=Tk()
    mw.title("RA Management System")
    ml= Label(mw, text=" Welcome ")
    ml.pack()
    D =Button(mw, text ="Driver", height = 2, width = 25, bg='pink', fg='black', command=registerwin_D)
    D.pack()
    P =Button(mw, text ="Passenger", height = 2, width = 25, bg='pink', fg='black', command=registerwin_P)
    P.pack()
    """A =Button(mw, text ="Admin", height = 2, width = 25,bg='pink', fg='black')#, command=registerwin)
    A.pack()"""
    mw.mainloop()



Eui()





