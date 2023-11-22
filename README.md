# Python SQLite Registration App

This project is a simple Python application that uses a custom Tkinter interface to interact with an SQLite database. The application allows users to register individuals by providing their name and email, search for registered individuals, and delete records from the database. The SQLite database is created and managed by the `DateBank` class.

## How to Use

1. **Registration:**
   - Enter the name and email in the respective entry fields.
   - Click the "Save" button to add the individual to the database.

2. **Search:**
   - Enter the name in the search entry field.
   - Click the "Search" button to find and display the information of the individual.

3. **Deletion:**
   - Enter the name in the search entry field.
   - Click the "Delete" button to remove the individual from the database.

## Requirements

- Python 3.10
- `customtkinter` library (make sure to install it using `pip install customtkinter`)

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Lugzh/Python_SQLite_Registration_App.git
   cd Python_SQLite_Registration_App
   
2. Run the application:
   python main.py
   
## Project Structure
  main.py: Contains the main application code.
  customtkinter/: Directory containing the custom Tkinter library code.
  people.db: SQLite database file for storing individual information.
  
## CustomTkinter Library
  The project uses the customtkinter library, which is not a standard Tkinter library. Ensure you have it installed before running the application.

## Database Structure
  The SQLite database (people.db) has a table named costumers with the following columns:

  id (INTEGER, PRIMARY KEY): Unique identifier for each record.
  name (TEXT, NOT NULL): Name of the individual.
  email (TEXT, NOT NULL): Email of the individual.
  
## Contribution
  Feel free to contribute to the project by forking the repository and submitting pull requests. Your contributions are highly appreciated!

##License
  This project is licensed under the MIT License.

