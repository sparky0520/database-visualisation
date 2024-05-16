import React, { useState } from 'react'
import axios from 'axios'
import { useSnackbar } from 'notistack'

const Add = () => {
    const [name, setName] = useState('')
    const [position, setPosition] = useState('')
    const [salary, setSalary] = useState('')
    const { enqueueSnackbar } = useSnackbar()

    const clearInput = () => {
        setName('')
        setPosition('')
        setSalary('')
    }

    const handleSaveEmployee = () => {
        const data = {
            "position": position,
            "salary": salary
        }
        axios
            .post(`http://127.0.0.1:5000/employee/${name}`, data)
            .then(() => {
                enqueueSnackbar("Employee Created Successfully", { variant: 'success' })
                clearInput()
            })
            .catch(err => {
                enqueueSnackbar('An error occured posting data. Please check console.', { variant: 'error' })
                console.log(err)
            })
    }
    return (
        <div className='max-w-2xl'>
            <div className='px-8 pb-6 border-2 border-gray-400 rounded-md'>
                <h2 className='text-2xl my-4 font-semibold'>Add Employee</h2>
                <div className='my-2'>
                    <label className='text-xl mr-4'>Name</label>
                    <input
                        className='border-2'
                        type='text'
                        value={name}
                        onChange={(e) => { setName(e.target.value) }} />
                </div>
                <div className='my-2'>
                    <label className='text-xl mr-4'>Position</label>
                    <input
                        className='border-2'
                        type='text'
                        value={position}
                        onChange={(e) => { setPosition(e.target.value) }} />
                </div>
                <div className='my-2'>
                    <label className='text-xl mr-4'>Salary</label>
                    <input
                        className='border-2'
                        type='text'
                        value={salary}
                        onChange={(e) => { setSalary(e.target.value) }} />
                </div>
                <div className='flex justify-between mt-4'>
                    <button className='text-lg border-2 border-red-500 text-red-500 p-1 rounded-md' onClick={clearInput}>Cancel</button>
                    <button className='text-lg border-2 border-blue-500 text-blue-500 p-1 rounded-md' onClick={handleSaveEmployee}>Add</button>
                </div>
            </div>
        </div>
    )
}

export default Add