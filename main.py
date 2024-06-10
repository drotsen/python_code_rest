# I want to create a python program using a GUI that can search in a REST API in the Paris Olympic Games 2024 database
# The user will be able to search for athletes, sports, events, etc.
# The user will be able to see the results in a list
# The user will be able to click on a result to see more details about it

# Importing the necessary libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
import json

# Creating the main window
root = Tk()
root.title("Paris 2024 Olympic Games Database")
root.geometry("800x600")

# Creating the search bar
search_bar = Entry(root, width=50)
search_bar.pack(pady=20)

# Creating the search button
def search():
    search_term = search_bar.get()
    search_term = search_term.replace(" ", "%20")
    url = f"https://api.paris2024.org/v1/olympic-games/athletes?search={search_term}"
    response = requests.get(url)
    data = response.json()
    athletes = data["data"]
    for athlete in athletes:
        athlete_name = athlete["name"]
        athlete_id = athlete["id"]
        athlete_label = Label(root, text=athlete_name)
        athlete_label.pack()
        def athlete_details(athlete_id):
            # Add your code here to display more details about the athlete
            pass
        
        athlete_label.bind("<Button-1>", lambda e, athlete_id=athlete_id: athlete_details(athlete_id))
        
    
    
search_button = Button(root, text="Search", command=search)

search_button.pack(pady=20)

# Running the main loop
root.mainloop()

# End of the program

# The program is not finished yet. I will continue to work on it in the next days.
# I will add more features and improve the user interface.
# I will also add more comments to explain the code better.
# I will also test the program to make sure it works correctly.
# I will also add error handling to handle exceptions and display error messages to the user.
# I will also add more functionality to display more details about the athletes, sports, events, etc.
# I will also add functionality to search for other types of data in the database.

        
        