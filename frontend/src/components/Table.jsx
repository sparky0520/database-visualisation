import React from 'react'
import './Table.css'

const Table = (props) => {
    let totalData = props.data
    return (
        <div className='my-10'>
            <table className='mx-auto border-2 border-gray-700'>
                <thead className='bg-gray-200 border border-gray-700'>
                    <tr>
                        <th>Employee ID</th>
                        <th>Name</th>
                        <th>Position</th>
                        <th>Salary</th>
                    </tr>
                </thead>
                <tbody>
                    {totalData.map((record, index) => (
                        <tr key={index}>
                            <td>{record.employee_id}</td>
                            <td>{record.name}</td>
                            <td>{record.position}</td>
                            <td>{record.salary}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Table