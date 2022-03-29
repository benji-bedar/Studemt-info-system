import csv
from importlib.resources import path
from lib2to3.pytree import WildcardPattern
from optparse import Values
from tkinter import*
from tkinter import filedialog, ttk
from tkinter import messagebox as mb
import tkinter as tk



path = "list.csv"
file = open(path, 'r+', newline='')
files = open(path, 'a+', newline='')

reader = csv.reader(file)
writer = csv.writer(files)



header = next(reader)
dataset = [row for row in reader]

root = Tk()
root.title('Student Information System')
root.geometry('1000x600')


frame = Frame(root, bg = '#87ceeb')
frame.place(relwidth = 1, relheight = 1)

my_tree = ttk.Treeview(frame)

my_tree['show'] = 'headings'
s = ttk.Style(frame)
s.configure("Treeview.Heading", foreground = 'blue', font=('Helvetica', 11, "bold"))



my_tree['columns'] = ("ID Number", "Name", "Course", "Year Level", "Gender")

my_tree.column("ID Number", width = 100, minwidth=50, anchor=tk.W) 
my_tree.column("Name", width = 250, minwidth=100, anchor=tk.CENTER) 
my_tree.column("Course", width = 150, minwidth=100, anchor=tk.CENTER) 
my_tree.column("Year Level", width = 150, minwidth=50, anchor=tk.CENTER) 
my_tree.column("Gender", width = 100, minwidth=100, anchor=tk.CENTER) 

my_tree.heading("ID Number", text = "ID Number", anchor=tk.CENTER) 
my_tree.heading("Name", text = "Name", anchor=tk.CENTER) 
my_tree.heading("Course", text = "Course", anchor=tk.CENTER) 
my_tree.heading("Year Level", text = "Year Level", anchor=tk.CENTER) 
my_tree.heading("Gender", text = "Gender", anchor=tk.CENTER) 



def Display_records(my_tree):
        for record in my_tree.get_children():
                my_tree.delete(record)

        global i
        i = 0
        global f1

        for row in dataset:
                my_tree.insert('', i, text="", value=(row[0], row[1], row[2], row[3], row[4]))
                i = i + 1
        files.read()        
Display_records(my_tree)
my_tree.pack()
name = tk.StringVar()
IDNumber = tk.StringVar()
course = tk.StringVar()
YearLevel = tk.StringVar()
gender = tk.StringVar()
id_NUMBER = tk.IntVar()



def updateStud(my_tree):
        selected = my_tree.focus()
        values = my_tree.item(selected, "values")
        print(values)

        f1 = Frame(root, width = 400, height = 250, background = "wheat")
        f1.place(x = 300, y = 200)

        headings = Label(f1, text = "Enter the details below", width = 40, font = ('Times', 10, 'bold'))
        headings.place(x = 60, y = 5)

        l1 = Label(f1, text = "ID Number:", width = 10, font = ('Times', 10, 'bold'))
        e1 = Entry(f1, textvariable = IDNumber, width = 30, font = ('Times', 10, 'bold'))
        l1.place(x = 50, y = 35)
        e1.place(x = 170, y = 35)

        l2 = Label(f1, text = "Name:", width = 10, font = ('Times', 10, 'bold'))
        e2 = Entry(f1, textvariable = name, width = 30, font = ('Times', 10, 'bold'))
        l2.place(x = 50, y = 75)
        e2.place(x = 170, y = 75)

        l3 = Label(f1, text = "Course:", width = 10, font = ('Times', 10, 'bold'))
        e3 = Entry(f1, textvariable = course, width = 30, font = ('Times', 10, 'bold'))
        l3.place(x = 50, y = 115)
        e3.place(x = 170, y = 115)

        l4 = Label(f1, text = "Year Level:", width = 10, font = ('Times', 10, 'bold'))
        e4 = Entry(f1, textvariable = YearLevel, width = 30, font = ('Times', 10, 'bold'))
        l4.place(x = 50, y = 155)
        e4.place(x = 170, y = 155)

        l5 = Label(f1, text = "Gender:", width = 10, font = ('Times', 10, 'bold'))
        e5 = Entry(f1, textvariable = gender, width = 30, font = ('Times', 10, 'bold'))
        l5.place(x = 50, y = 195)
        e5.place(x = 170, y = 195)

        e1.insert(0, values[0])
        e2.insert(0, values[1])
        e3.insert(0, values[2])
        e4.insert(0, values[3])
        e5.insert(0, values[4])  
 



        def update_data():
                nonlocal e1, e2, e3, e4, e5
                                
                get_ID = IDNumber.get()
                get_name = name.get()
                get_course = course.get()
                get_YearLevel = YearLevel.get()
                get_gender = gender.get()

                outcome = my_tree.item(selected, value =  (get_ID, get_name, get_course, get_YearLevel, get_gender))
                #writer.writerow([get_ID, get_name, get_course, get_YearLevel, get_gender])
                filers = open(path, 'w+', newline='')
                writers = csv.writer(filers)

                
                rows = list()
                print(values)
                for row in dataset:
                        rows.append(row)
                for row in rows:
                        if row[0] == values[0]:
                                rows.remove(row)

                writers.writerow(["ID Number", "Name", "Course", "Year Level", "Gender"])     
                writers.writerows(rows)
                writers.writerow([get_ID, get_name, get_course, get_YearLevel, get_gender])
                

                
                mb.showinfo("Message", "You have successfully updated the student details")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                f1.destroy()
                filers.read()

                


        submit_button = tk.Button(f1, text = "Submit", width = 10, font = ('Times', 10, 'bold'), command = lambda:update_data())
        submit_button.place(x = 120, y = 220)
        cancell_button = tk.Button(f1, text = "Cancell", width = 10, font = ('Times', 10, 'bold'), command = f1.destroy)
        cancell_button.place(x = 200, y = 220)



        



def addStud(my_tree):
        f = Frame(root, width = 400, height = 250, background = "wheat")
        f.place(x = 300, y = 200)

        headings = Label(f, text = "Enter the details below", width = 40, font = ('Times', 10, 'bold'))
        headings.place(x = 60, y = 5)


        l1 = Label(f, text = "ID Number:", width = 10, font = ('Times', 10, 'bold'))
        e1 = Entry(f, textvariable = IDNumber, width = 30, font = ('Times', 10, 'bold'))
        l1.place(x = 50, y = 35)
        e1.place(x = 170, y = 35)

        l2 = Label(f, text = "Name:", width = 10, font = ('Times', 10, 'bold'))
        e2 = Entry(f, textvariable = name, width = 30, font = ('Times', 10, 'bold'))
        l2.place(x = 50, y = 75)
        e2.place(x = 170, y = 75)

        l3 = Label(f, text = "Course:", width = 10, font = ('Times', 10, 'bold'))
        e3 = Entry(f, textvariable = course, width = 30, font = ('Times', 10, 'bold'))
        l3.place(x = 50, y = 115)
        e3.place(x = 170, y = 115)

        l4 = Label(f, text = "Year Level:", width = 10, font = ('Times', 10, 'bold'))
        e4 = Entry(f, textvariable = YearLevel, width = 30, font = ('Times', 10, 'bold'))
        l4.place(x = 50, y = 155)
        e4.place(x = 170, y = 155)

        l5 = Label(f, text = "Gender:", width = 10, font = ('Times', 10, 'bold'))
        e5 = Entry(f, textvariable = gender, width = 30, font = ('Times', 10, 'bold'))
        l5.place(x = 50, y = 195)
        e5.place(x = 170, y = 195)

        

        def insertStud():
                nonlocal e1, e2, e3, e4, e5
                get_ID = IDNumber.get()
                get_name = name.get()
                get_course = course.get()
                get_YearLevel = YearLevel.get()
                get_gender = gender.get()

                writer.writerow([get_ID, get_name, get_course, get_YearLevel, get_gender])
                my_tree.insert('', 'end', text = "", value=(get_ID, get_name, get_course, get_YearLevel, get_gender))

                mb.showinfo("Message", "You have successfully added a new student")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                f.destroy()
                files.read()




        submit_button = tk.Button(f, text = "Submit", width = 10, font = ('Times', 10, 'bold'), command = lambda:insertStud())
        submit_button.place(x = 120, y = 220)
        cancell_button = tk.Button(f, text = "Cancell", width = 10, font = ('Times', 10, 'bold'), command = f.destroy)
        cancell_button.place(x = 200, y = 220)


def delStud(my_tree):
        #selected_data = my_tree.selection()[0]
        #my_tree.delete(selected_data)

        selected_data = my_tree.focus()
        values = my_tree.item(selected_data, "values")
        my_tree.delete(selected_data)


        #for row in dataset:
        #        if row[2] != values[2]:
        #                writer_out.writerow(values)
        #for row in dataset:
                #if row[0] == values[0]:
                        #writer.writerow()
                        #df.drop(values([0], [1], [2], [3], [4]))
                        #row[values[0], values[1], values[2], values[3], values[4]]

        #df_s = df[:5]


        #df_s = df_s.drop(df_s[(df_s.Name == values[1]) & (df_s.Gender == values[4])].index)

        filers = open(path, 'w+', newline='')
        writers = csv.writer(filers)

                
        rows = list()
        print(values)
        for row in dataset:
                rows.append(row)
        for row in rows:
                if row[0] == values[0]:
                        rows.remove(row)

        writers.writerow(["ID Number", "Name", "Course", "Year Level", "Gender"])     
        writers.writerows(rows)

        file.read()


        #df_s = df[1:5]

        #df_s.set_index('ID Number', inplace = True)

        #df_s = df_s.drop(values[0])
        #print(df_s)

        #pd.read_csv('list.csv')
        #for row in dataset:
        #        if row[0] == values[0]:
        #                writer.writerow(values) 


        mb.showinfo("Message", "You have successfully deleted a student")

        #newData = list(selected_data)

        #for row in writer:
        #        if row != str(newData[3]):
        #                writer.writerow(row)

        #f.drop(len(newData)-1).head()
        #print(newData)
        
        #dataset.drop(subset = [selected_data]).head()
        #df.drop([selected_data], axis = 0)
        #reader = reader.drop(reader.index[selected_data[1]], axis = 0)
        #reader.read()


        #print(my_tree.item(selected_data)['value'])
        #uid = my_tree.item(selected_data)['value'][0]


def searchID(my_tree):  

        global search, search_entry
        search = Toplevel(root)
        search.title("Search for a record")
        search.geometry("400x200")


        f = LabelFrame(search, text = "ID Number", width = 400, height = 250, background = "wheat")
        f.pack(padx = 10, pady = 10)
        

        #l1 = Label(f, text = "ID Number:", width = 10, font = ('Times', 10, 'bold'))
        search_entry = Entry(f, font = ('Times', 10, 'bold'))
        #l1.place(x = 50, y = 35)
        search_entry.pack(padx = 20, pady = 20)
        
        searchButton = Button(search, text = "Search a student by ID", command = lambda:SRecordId())
        searchButton.pack(padx = 20, pady = 20)

        file.read()


        #def Id_search():




                #for rec in da:
                #        if rec[0] == id_num:
                #                id_num.get()

                #print(id_num)

        
        #submit_button = tk.Button(f, text = "Submit", width = 10, font = ('Times', 10, 'bold'), command = lambda:Id_search())
        #submit_button.place(x = 120, y = 220)
        #cancell_button = tk.Button(f, text = "Cancell", width = 10, font = ('Times', 10, 'bold'), command = f.destroy)
        #cancell_button.place(x = 200, y = 220)

def SRecordId():
        #filers = open(path, 'w+', newline='')
        #writers = csv.writer(filers)

                        
        rows = list()
        lookup_record = search_entry.get()
        search.destroy()

        for record in my_tree.get_children():
                my_tree.delete(record)


        for row in dataset:
                if row[0] == lookup_record:
                        my_tree.insert('', i, text="", value=(row[0], row[1], row[2], row[3], row[4]))


        file.read()
        files.read()
        #writers.writerow(["ID Number", "Name", "Course", "Year Level", "Gender"])     
        #writers.writerows(rows)





insert_button = tk.Button(root, text = "Add New Student", command = lambda:addStud(my_tree))
insert_button.configure(font = ("calibri", 15, "bold"), bg = "blue", fg = "white")
insert_button.place(x = 200, y = 300)

edit_button = tk.Button(root, text = "Edit Student", command = lambda:updateStud(my_tree))
edit_button.configure(font = ("calibri", 15, "bold"), bg = "green", fg = "white")
edit_button.place(x = 420, y = 300)


delete_button = tk.Button(root, text = "Delete Student", command = lambda:delStud(my_tree))
delete_button.configure(font = ("calibri", 15, "bold"), bg = "red", fg = "white")
delete_button.place(x = 600, y = 300)

search_button = tk.Button(root, text = "Search a Student", command = lambda:searchID(my_tree))
search_button.configure(font = ("calibri", 15, "bold"), bg = "orange", fg = "white")
search_button.place(x = 400, y = 450)




root.mainloop()
addStud(my_tree)
delStud(my_tree)
updateStud(my_tree)
searchID(my_tree)

Display_records(my_tree)