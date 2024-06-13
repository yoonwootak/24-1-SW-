import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from user import User
from travel_destination import TravelDestination
from budget import Budget
from album import Album
from friend import Friend  

class Main:
    def __init__(self, root):
        self.users = []
        self.current_user = None
        self.current_album = None
        self.current_budget = None
        self.root = root
        self.root.title("all-travel")

        self.create_widgets()

    def create_widgets(self):
        self.lbl_userID = tk.Label(self.root, text="UserID:")
        self.lbl_userID.grid(row=0, column=0)

        self.ent_userID = tk.Entry(self.root)
        self.ent_userID.grid(row=0, column=1)

        self.lbl_password = tk.Label(self.root, text="Password:")
        self.lbl_password.grid(row=1, column=0)

        self.ent_password = tk.Entry(self.root, show="*")
        self.ent_password.grid(row=1, column=1)

        self.btn_login = tk.Button(self.root, text="Login", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2)

        self.btn_signup = tk.Button(self.root, text="Sign Up", command=self.show_signup)
        self.btn_signup.grid(row=3, column=0, columnspan=2)

    def login(self):
        userID = self.ent_userID.get()
        password = self.ent_password.get()
        
        for user in self.users:
            if user.login(userID, password):
                self.current_user = user
                messagebox.showinfo("Login Success", f"Welcome, {self.current_user.name}")
                self.show_main_menu()
                return
        
        messagebox.showerror("Login Failed", "Invalid userID or password")

    def show_signup(self):
        self.signup_window = tk.Toplevel(self.root)
        self.signup_window.title("Sign Up")

        tk.Label(self.signup_window, text="UserID:").grid(row=0, column=0)
        self.ent_signup_userID = tk.Entry(self.signup_window)
        self.ent_signup_userID.grid(row=0, column=1)

        tk.Label(self.signup_window, text="Password:").grid(row=1, column=0)
        self.ent_signup_password = tk.Entry(self.signup_window, show="*")
        self.ent_signup_password.grid(row=1, column=1)

        tk.Label(self.signup_window, text="Name:").grid(row=2, column=0)
        self.ent_signup_name = tk.Entry(self.signup_window)
        self.ent_signup_name.grid(row=2, column=1)

        tk.Label(self.signup_window, text="Email:").grid(row=3, column=0)
        self.ent_signup_email = tk.Entry(self.signup_window)
        self.ent_signup_email.grid(row=3, column=1)

        tk.Button(self.signup_window, text="Sign Up", command=self.signup).grid(row=4, column=0, columnspan=2)

    def signup(self):
        userID = self.ent_signup_userID.get()
        password = self.ent_signup_password.get()
        name = self.ent_signup_name.get()
        email = self.ent_signup_email.get()

        new_user = User.signUp(userID, password, name, email)
        self.users.append(new_user)
        messagebox.showinfo("Sign Up Success", "You have successfully signed up!")
        self.signup_window.destroy()

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Logout", command=self.logout).grid(row=0, column=0, columnspan=2)
        tk.Button(self.root, text="Search Travel by Keyword", command=self.show_search_by_keyword).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Search Travel by Month", command=self.show_search_by_month).grid(row=2, column=0, columnspan=2)
        tk.Button(self.root, text="Budget Management", command=self.show_budget_management).grid(row=3, column=0, columnspan=2)
        tk.Button(self.root, text="Album", command=self.show_album_menu).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="Register Friend", command=self.show_register_friend).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Check Friend Information", command=self.show_check_friend_info).grid(row=6, column=0, columnspan=2)

    def show_search_by_keyword(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Select Keyword:").grid(row=0, column=0)
        self.keyword_var = tk.StringVar()
        self.keyword_var.set("beach")

        keywords = ["beach", "mountain", "city", "historical"]
        self.keyword_menu = tk.OptionMenu(self.root, self.keyword_var, *keywords)
        self.keyword_menu.grid(row=0, column=1)

        tk.Button(self.root, text="Search", command=self.search_by_keyword).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_main_menu).grid(row=2, column=0, columnspan=2)

    def search_by_keyword(self):
        keyword = self.keyword_var.get()
        destinations = TravelDestination.searchByKeyword(keyword)
        result_text = "\n".join([f"{d.name}: {d.description}" for d in destinations])
        messagebox.showinfo("Search Results", result_text)

    def show_search_by_month(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Select Month:").grid(row=0, column=0)
        self.month_var = tk.IntVar()
        self.month_var.set(1)

        months = list(range(1, 13))
        self.month_menu = tk.OptionMenu(self.root, self.month_var, *months)
        self.month_menu.grid(row=0, column=1)

        tk.Button(self.root, text="Search", command=self.search_by_month).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_main_menu).grid(row=2, column=0, columnspan=2)

    def search_by_month(self):
        month = self.month_var.get()
        destinations = TravelDestination.searchByMonth(month)
        result_text = "\n".join([f"{d.name}: {d.description}" for d in destinations])
        messagebox.showinfo("Search Results", result_text)

    def show_budget_management(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Budget ID:").grid(row=0, column=0)
        self.ent_budgetID = tk.Entry(self.root)
        self.ent_budgetID.grid(row=0, column=1)

        tk.Label(self.root, text="Total Amount:").grid(row=1, column=0)
        self.ent_totalAmount = tk.Entry(self.root)
        self.ent_totalAmount.grid(row=1, column=1)

        tk.Button(self.root, text="Create Budget", command=self.create_budget).grid(row=2, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_main_menu).grid(row=3, column=0, columnspan=2)

    def create_budget(self):
        budgetID = self.ent_budgetID.get()
        totalAmount = float(self.ent_totalAmount.get())
        self.current_budget = Budget(budgetID, totalAmount)
        messagebox.showinfo("Budget Created", "Budget has been created successfully!")
        self.show_budget_menu()

    def show_budget_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Add Expense", command=self.show_add_expense).grid(row=0, column=0, columnspan=2)
        tk.Button(self.root, text="Check Remaining Budget", command=self.check_remaining_budget).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_main_menu).grid(row=2, column=0, columnspan=2)

    def show_add_expense(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Expense Amount:").grid(row=0, column=0)
        self.ent_expenseAmount = tk.Entry(self.root)
        self.ent_expenseAmount.grid(row=0, column=1)

        tk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_budget_menu).grid(row=2, column=0, columnspan=2)

    def add_expense(self):
        amount = float(self.ent_expenseAmount.get())
        self.current_budget.addExpense(amount)
        messagebox.showinfo("Expense Added", "Expense has been added successfully!")
        self.show_budget_menu()

    def check_remaining_budget(self):
        remaining_budget = self.current_budget.getRemainingBudget()
        messagebox.showinfo("Remaining Budget", f"Remaining Budget: {remaining_budget}")

    def show_album_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if not self.current_album:
            self.current_album = Album(f"{self.current_user.userID}_album")

        tk.Button(self.root, text="Register Photo", command=self.show_register_photo).grid(row=0, column=0, columnspan=2)
        tk.Button(self.root, text="Register Memo", command=self.show_register_memo).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Check Album", command=self.check_album).grid(row=2, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_main_menu).grid(row=3, column=0, columnspan=2)

    def show_register_photo(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Select Photo", command=self.register_photo).grid(row=0, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_album_menu).grid(row=1, column=0, columnspan=2)

    def register_photo(self):
        photo_path = filedialog.askopenfilename(title="Select Photo", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if photo_path:
            self.current_album.registerPhoto(photo_path)
            messagebox.showinfo("Photo Registered", "Photo has been registered successfully!")
        self.show_album_menu()

    def show_register_memo(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Enter Memo:").grid(row=0, column=0)
        self.ent_memo = tk.Entry(self.root)
        self.ent_memo.grid(row=0, column=1)

        tk.Button(self.root, text="Register Memo", command=self.register_memo).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_album_menu).grid(row=2, column=0, columnspan=2)

    def register_memo(self):
        memo = self.ent_memo.get()
        self.current_album.registerMemo(memo)
        messagebox.showinfo("Memo Registered", "Memo has been registered successfully!")
        self.show_album_menu()

    def check_album(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        photos, memos = self.current_album.checkAlbum()

        for idx, photo in enumerate(photos):
            img = Image.open(photo)
            img.thumbnail((200, 200))
            img = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=img).grid(row=idx, column=0)
            tk.Label(self.root, text=os.path.basename(photo)).grid(row=idx, column=1)
            self.root.image = img 

        for idx, memo in enumerate(memos):
            tk.Label(self.root, text=f"Memo {idx+1}: {memo}").grid(row=len(photos) + idx, column=0, columnspan=2)

        tk.Button(self.root, text="Back", command=self.show_album_menu).grid(row=len(photos) + len(memos), column=0, columnspan=2)
        
    def show_register_friend(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Friend ID:").grid(row=0, column=0)
        self.ent_friendID = tk.Entry(self.root)
        self.ent_friendID.grid(row=0, column=1)

        tk.Label(self.root, text="Friend Name:").grid(row=1, column=0)
        self.ent_friend_name = tk.Entry(self.root)
        self.ent_friend_name.grid(row=1, column=1)

        tk.Label(self.root, text="Friend Email:").grid(row=2, column=0)
        self.ent_friend_email = tk.Entry(self.root)
        self.ent_friend_email.grid(row=2, column=1)

        tk.Button(self.root, text="Register Friend", command=self.register_friend).grid(row=3, column=0, columnspan=2)
        tk.Button(self.root, text="Back", command=self.show_main_menu).grid(row=4, column=0, columnspan=2)

    def register_friend(self):
        friendID = self.ent_friendID.get()
        name = self.ent_friend_name.get()
        email = self.ent_friend_email.get()

        new_friend = Friend(friendID, name, email)
        new_friend.registerFriend(self.current_user)
        messagebox.showinfo("Friend Registered", f"{name} has been registered as your friend!")
        self.show_main_menu()

    def show_check_friend_info(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        friends = Friend.checkFriendInfo(self.current_user)
        if not friends:
            tk.Label(self.root, text="You have no friends registered.").grid(row=0, column=0, columnspan=2)
        else:
            tk.Label(self.root, text="Your Friends:").grid(row=0, column=0, columnspan=2)
            for idx, friend in enumerate(friends, start=1):
                tk.Label(self.root, text=f"{idx}. {friend.name} - {friend.email}").grid(row=idx, column=0, columnspan=2)

        tk.Button(self.root, text="Back", command=self.show_main_menu).grid(row=len(friends) + 1, column=0, columnspan=2)

    def logout(self):
        self.current_user = None
        self.current_album = None 
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()
        messagebox.showinfo("Logout", "You have successfully logged out")

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
