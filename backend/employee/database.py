import sqlite3

def connect_to_database():
    try:
        con = sqlite3.connect('employee_db.sqlite')
        print("Connected to DataBase")
        return con
    except sqlite3.Error as e:
        print("Connection Error:", e)
        return None


def add(name, data):
    con = connect_to_database()
    position = data.get('position')
    salary = int(data.get('salary'))
    if con:
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO employees(name, position, salary) VALUES (?, ?, ?);", (name, position, salary))
            con.commit()
            return {'success': True, 'message': "Employee Added Successfully"}
        except sqlite3.Error as e:
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
            cur = con.cursor()
            # Checking if employee_id exists
            cur.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
            if not cur.fetchall():
                return {'success': False, 'message': f"No Employee with employee_id={employee_id}"}

            cur.execute("DELETE FROM employees WHERE employee_id=?;", (employee_id,))
            con.commit()

            return {'success': True, 'message': "Employee Deleted Successfully"}
        except sqlite3.Error as e:
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
            cur = con.cursor()
            # Checking if employee_id exists
            cur.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
            if not cur.fetchall():
                return {'success': False, 'message': f"No Employee with employee_id={employee_id}"}
            cur.execute(
                "UPDATE employees SET name=?, position=?, salary=? WHERE employee_id=?;", (name, position, salary, employee_id))
            con.commit()
            return {'success': True, 'message': "Employee Updated Successfully"}
        except sqlite3.Error as e:
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
            cur = con.cursor()
            command = "SELECT * FROM employees"

            name = data.get('name')
            salary = data.get('salary')

            if name and salary:
                command += " WHERE name LIKE ? AND salary LIKE ?"
                cur.execute(command, ('%' + name + '%', '%' + salary + '%'))
            elif name:
                command += " WHERE name LIKE ?"
                cur.execute(command, ('%' + name + '%',))
            elif salary:
                command += " WHERE salary LIKE ?"
                cur.execute(command, ('%' + salary + '%',))
            else:
                cur.execute(command)

            rows = cur.fetchall()
            if rows:
                # Prepare the result in a dictionary format
                return {'success': True, 'data': rows}
            else:
                return {'success': True, 'data': [], 'message': 'No records found'}
        except sqlite3.Error as e:
            return {'success': False, 'message': "Error retrieving employees: {}".format(e)}
        finally:
            cur.close()
            con.close()
    else:
        return {'success': False, 'message': "Error connecting to database"}
