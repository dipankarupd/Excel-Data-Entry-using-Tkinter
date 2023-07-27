import tkinter
from tkinter import ttk
from tkinter import messagebox
from data_processor import DataProcessor

class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")
        self.data_processor = DataProcessor()

         # Initialize variables
        self.accept_var = tkinter.StringVar(value="Not Accepted")
        self.reg_status_var = tkinter.StringVar(value="Not registered")  # Add this line


        # Create the main frame
        self.frame = tkinter.Frame(root)
        self.frame.pack()

        # Create user information widgets
        self.create_user_info_widgets()

        # Create course information widgets
        self.create_course_info_widgets()

        # Create terms and conditions widgets
        self.create_terms_widgets()

    def create_user_info_widgets(self):
        user_info_frame = tkinter.LabelFrame(self.frame, text="User Information")
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        # Labels and entry fields for first name and last name
        first_name_label = tkinter.Label(user_info_frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        last_name_label = tkinter.Label(user_info_frame, text="Last Name")
        last_name_label.grid(row=0, column=1)

        self.first_name_entry = tkinter.Entry(user_info_frame)
        self.last_name_entry = tkinter.Entry(user_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)

        # Combobox for title, Spinbox for age, and Combobox for nationality
        title_label = tkinter.Label(user_info_frame, text="Title")
        self.title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
        title_label.grid(row=0, column=2)
        self.title_combobox.grid(row=1, column=2)

        age_label = tkinter.Label(user_info_frame, text="Age")
        self.age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
        age_label.grid(row=2, column=0)
        self.age_spinbox.grid(row=3, column=0)

        nationality_label = tkinter.Label(user_info_frame, text="Nationality")
        self.nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
        nationality_label.grid(row=2, column=1)
        self.nationality_combobox.grid(row=3, column=1)

        # Adjust padding for all widgets in user_info_frame
        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_course_info_widgets(self):
        courses_frame = tkinter.LabelFrame(self.frame)
        courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        # Checkbox and Spinboxes for course registration
        registered_label = tkinter.Label(courses_frame, text="Registration Status")
        registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                               variable=self.reg_status_var, onvalue="Registered", offvalue="Not registered")

        registered_label.grid(row=0, column=0)
        registered_check.grid(row=1, column=0)

        numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
        self.numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
        numcourses_label.grid(row=0, column=1)
        self.numcourses_spinbox.grid(row=1, column=1)

        numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
        self.numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
        numsemesters_label.grid(row=0, column=2)
        self.numsemesters_spinbox.grid(row=1, column=2)

        # Adjust padding for all widgets in courses_frame
        for widget in courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_terms_widgets(self):
        terms_frame = tkinter.LabelFrame(self.frame, text="Terms & Conditions")
        terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                          variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        terms_check.grid(row=0, column=0)

        # Create a button to enter data
        button = tkinter.Button(self.frame, text="Enter data", command=self.enter_data)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def enter_data(self):
        accepted = self.accept_var.get()

        if accepted == "Accepted":
            # Fetch user information
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()

            if firstname and lastname:
                title = self.title_combobox.get()
                age = self.age_spinbox.get()
                nationality = self.nationality_combobox.get()

                # Fetch course information
                registration_status = self.reg_status_var.get()
                numcourses = self.numcourses_spinbox.get()
                numsemesters = self.numsemesters_spinbox.get()

                data_dict = {
                    "first name": firstname,
                    "last name": lastname,
                    "title": title,
                    "age": age,
                    "nationality": nationality,
                    "courses": numcourses,
                    "semesters": numsemesters,
                    "registration status": registration_status
                }

                # Save data to CSV using DataProcessor
                self.data_processor.save_data_to_csv(data_dict)
            else:
                tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
        else:
            tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

if __name__ == "__main__":
    window = tkinter.Tk()
    data_entry_form = DataEntryForm(window)
    window.mainloop()
