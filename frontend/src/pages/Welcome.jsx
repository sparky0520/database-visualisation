import React from 'react'
import Add from '../components/Add.jsx'
import Delete from '../components/Delete.jsx'
import Update from '../components/Update.jsx'
import { Link } from 'react-router-dom'

const Welcome = () => {
    return (
        <>
            <div className="flex items-center">
                <div className="text-3xl mx-auto my-6">Welcome Admin</div>
            </div>
            <div className="flex justify-end">
                <Link to="/listing" className="text-lg border-2 border-gray-500 p-2 rounded-md">View Database</Link>
            </div>
            <div className='flex justify-between items-top my-20'>
                <Add/>
                <Delete/>
                <Update/>
            </div>
            <div className='text-gray-400'>
                How to use:<br></br>
                <ul className='list-disc pl-4'>
                    <li>Add employee details and click add to add new employee to the database. Id is auto incremented.</li>
                    <li>Delete an employee from the database by adding all the details of the employee.</li>
                    <li>Update employee detail in database by adding the current employee id and the new information.</li>
                    <li>Click on “View Database” button to view the entire database on a new page.</li>
                </ul>
            </div>
        </>
    )
}

export default Welcome