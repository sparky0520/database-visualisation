import React, { useState } from 'react'
import axios from 'axios'
import { useSnackbar } from 'notistack'

const Delete = () => {
    const [employee_id, setEmployee_id] = useState('')
    const { enqueueSnackbar } = useSnackbar()

    const clearInput = () => {
        setEmployee_id('')
    }

    const handleDeleteEmployee = () => {
        axios
            .delete(`http://localhost:5000/employee/${employee_id}`)
            .then(() => {
                clearInput()
                console.log("Deleted!")
                enqueueSnackbar("Employee Deleted Successfully", { variant: 'success' })
            })
            .catch(err => {
                enqueueSnackbar('An error occured posting data. Please check console.', { variant: 'error' })
                console.log(err)
            })
    }

    return (
        <div className='max-w-2xl'>
            <div className='px-8 pb-6 border-2 border-gray-400 rounded-md'>
                <h2 className='text-2xl my-4 font-semibold'>Delete Employee</h2>
                <div className='my-2'>
                    <label className='text-xl mr-4'>Employee ID</label>
                    <input
                        className='border-2'
                        type='text'
                        value={employee_id}
                        onChange={(e) => { setEmployee_id(e.target.value) }} />
                </div>
                <div className='flex justify-between mt-4'>
                    <button className='text-lg border-2 border-red-500 text-red-500 p-1 rounded-md' onClick={clearInput}>Cancel</button>
                    <button className='text-lg border-2 border-blue-500 text-blue-500 p-1 rounded-md' onClick={handleDeleteEmployee}>Delete</button>
                </div>
            </div>
        </div>
    )
}

export default Delete