import React from 'react'
import './Table.css'

const Table = (props) => {
    let totalData = props.data
    // employee_id = record [0]
    // name = record [1]
    // position = record [2]
    // salary = record [3] 
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
                            <td>{record[0]}</td>
                            <td>{record[1]}</td>
                            <td>{record[2]}</td>
                            <td>{record[3]}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Table