'''
This is the main file of the bookkeeping app.
'''
import tkinter as tk
from app import BookkeepingApp
def main():
    root = tk.Tk()
    app = BookkeepingApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()