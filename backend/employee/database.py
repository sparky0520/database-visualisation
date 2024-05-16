# Add, Delete, Update, View data in Database
import mysql.connector as sqlcon


def connect_to_database():
    try:
        con = sqlcon.connect(host="localhost", user="root", password="1234", database="employee_db",
                             auth_plugin="mysql_native_password")
        print("Connected to DataBase")
        return con
    except sqlcon.Error as e:
        print("Connection Error:", e)
        return None


def add(name,data):
    con = connect_to_database()
    position = data.get('position')
    salary = int(data.get('salary'))
    if con:
        try:
            cur = con.cursor(dictionary=True)
            cur.execute("insert into employees(name,position,salary) values('{}','{}',{});".format(name, position, salary))
            con.commit()
            return {'success': True, 'message': "Employee Added Successfully"}
        except sqlcon.Error as e:
            return {'success': False, 'message': "Error adding employee: {}".format(e)}
        finally:
            cur.close()
            con.close()
    else:
        return {'success': False, 'message': "Error connecting to database"}


def delete(employee_id):
    con = connect_to_database()
    if con:
        try:
            cur = con.cursor(dictionary=True)
            # Checking if employee_id exists
            cur.execute("select * from employees where employee_id={}".format(employee_id))
            if not cur.fetchall():
                return {'success': False, 'message': f"No Employee with employee_id={employee_id}"}

            cur.execute("delete from employees where employee_id={};".format(employee_id))
            con.commit()

            return {'success': True, 'message': "Employee Deleted Successfully"}
        except sqlcon.Error as e:
            return {'success': False, 'message': "Error deleting employee: {}".format(e)}
        finally:
            cur.close()
            con.close()
    else:
        return {'success': False, 'message': "Error connecting to database"}


def update(employee_id, data):
    con = connect_to_database()
    name = data.get('name')
    position = data.get('position')
    salary = int(data.get('salary'))
    if con:
        try:
            cur = con.cursor(dictionary=True)
            # Checking if employee_id exists
            cur.execute("select * from employees where employee_id={}".format(employee_id))
            if not cur.fetchall():
                return {'success': False, 'message': f"No Employee with employee_id={employee_id}"}
            cur.execute(
                "update employees set name='{}',position='{}',salary={} where employee_id={};".format(name, position,
                                                                                                      salary,
                                                                                                      employee_id))
            con.commit()
            return {'success': True, 'message': "Employee Updated Successfully"}
        except sqlcon.Error as e:
            return {'success': False, 'message': "Error updating employee: {}".format(e)}
        finally:
            cur.close()
            con.close()
    else:
        return {'success': False, 'message': "Error connecting to database"}


def view(data):
    con = connect_to_database()
    if con:
        try:
            cur = con.cursor(dictionary=True)
            command = "SELECT * FROM employees"

            name = data.get('name')
            salary = data.get('salary')

            # # pagination
            # page = int(data.get('page', 1))  # Default to page 1 if not provided
            # page_size = int(data.get('page_size', 10))  # Default page size to 10 if not provided

            # # Calculate the starting index based on the page number and page size
            # start_index = (page - 1) * page_size

            if name and salary:
                command += f" WHERE name LIKE '%{name}%' AND salary LIKE '%{salary}%'"
            elif name:
                command += f" WHERE name LIKE '%{name}%'"
            elif salary:
                command += f" WHERE salary LIKE '%{salary}%'"

            # # Add pagination to the SQL query
            # command += f" LIMIT {start_index}, {page_size}"
            command += ';'
            cur.execute(command)
            rows = cur.fetchall()
            if rows:
                # Prepare the result in a dictionary format
                return {'success': True, 'data': rows}
            else:
                return {'success': True, 'data': [], 'message': 'No records found'}
        except sqlcon.Error as e:
            return {'success': False, 'message': "Error retrieving employees: {}".format(e)}
        finally:
            cur.close()
            con.close()
    else:
        return {'success': False, 'message': "Error connecting to database"}
