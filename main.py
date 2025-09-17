import pymysql.cursors
import tkinter as tk


def main(mood, comment):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='socialmood',
                                cursorclass=pymysql.cursors.DictCursor)
    
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `mood_entries` (`rating`, `comment`) VALUES (%s, %s)"
            cursor.execute(sql, (mood, comment))

        connection.commit()

        with connection.cursor() as cursor:
            sql = "SELECT `id`, `rating` FROM `mood_entries`"
            cursor.execute(sql)
            return cursor.fetchone()
        
class Info():
    def __init__(self):
        self.mood_input = ""
        self.comment_input = ""
    def submit(self):
        self.mood_input = radio_button.get()
        self.comment_input = entry_comment.get()
        print(self.mood_input, self.comment_input)
        main(self.mood_input, self.comment_input)
        
root = tk.Tk()
root.geometry("600x300")
radio_button = tk.StringVar(root)
entry_comment = tk.StringVar(root)
moods = [
    "Barely holding on",
    "Worse than usual",
    "Meh",
    "Pretty good",
    "Good",
    "Perfect"
]
for m in moods:
    tk.Radiobutton(root, text=m, variable=radio_button, value=m).pack(anchor="w")

tk.Entry(root, textvariable=entry_comment).pack(fill="x", padx=8, pady=8)

info = Info() 
tk.Button(root, text="Submit", command=info.submit).pack(pady=8)
tk.Button(root, text="Exit", command=quit).pack()


root.mainloop()
