# Database Visualisation using React/Flask

### Through this full stack application the admin will be able to manage a database (MySQL) and perform the following tasks:


- Add Employee: Adding name, position, salary. A unique id is automatically generated with every next id being an increment of the previous.

- Delete Employee: Taking complete data i.e. employee_id, name, position and salary to delete the record ensuring the correct record is deleted.

- Update Employee: Taking employee_id to change a specific record along with the new data : name, position, salary to update the record.

- View Records: Clicking on "View Database" we can see all the records in a neatly aligned table in a new page. In this new page we can filter records by name or salary of the employee. All the records with data like the filter will appear in the table.



# Features Implemented:


React Frontend:
- Created an admin panel to view, modify, add and delete employee data having two pages:

1. Welcome page with a form to add employee details (refer the sample data for form fields)
2. Listing page to display all the employees with a filter on NAME AND SALARY.

Flask Backend:
- Created a minimalistic backend (using blueprints) with basic CRUD functionalities.

Additional:
- Prefilled the database with the sample data
- Structured codebase
-  UI and Styling


# Backend - Flask App
The backend server comprises of a flask script, blueprint file and database code file all of which are written in Python.

## database.py

- Contains a SQL table connection
- Has functions add, delete, update, view which are called on from routes.py(various routes)
- Provides easy to read sql database connections and how CRUD operations are being performed on the database.

## routes.py

- Contains ___employee blueprint___ along with all routes and methods for the app.
- Has get, post, delete, and put routes on the '/' route to get all records, add a new record, delete an old record or update a record, respectively.
- Provides modularity and makes easy to understand the function calls upon hitting different routes.

## app.py

- Puts everything together neatly.
- Implement CORS
- Register blueprint with the app.
- Start app server


# Frontend - React App
The frontend of the application is written in React. This helps us work with the database without interruptions due to loading/refreshing of the page. The libraries used include:

- react-router-dom  --> For BrowserRouter, Routes, Route, Link
- axios --> To make requests and recieve data while giving us more flexibility than traditional forms.
- notistack --> To make the app more beautiful and easy to look at.
- (Tailwind) --> To write css.

The folder structure includes:

- Pages
- Components
- App.jsx
- Main.jsx

## App.jsx

- Define all routes in the app.

## Pages/Welcome.jsx

- Contains the welcome page.
- Includes three components - Add.jsx, Delete.jsx, Update.jsx
 
### Components/Add.jsx

- Add new data to the database by making post request to /employee by axios.

### Components/Delete.jsx

- Delete old data from the database by making delete request to /employee by axios.

### Components/Update.jsx

- Update old data in the database by making put request to /employee by axios.
 
## Pages/Listing.jsx

- Contains the code for rendering the database records on the webpage.
- Make get request to /employee along with query url for name and salary values.
- useEffect is dependent on the name and salary values and is called whenever these change. Giving us  a seemless user experience.
- Calls the Table.jsx and Spinner.jsx component to render the table and spinner (on loading) which creates a neat and modular code setup. 

## Main.jsx

- Main code file to put it all together and start server.
