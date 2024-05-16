import { Link } from 'react-router-dom'
import React, { useState, useEffect } from 'react'
import Table from '../components/Table'
import axios from 'axios'
import Spinner from '../components/Spinner'

const Listing = () => {
  const [name, setName] = useState('')
  const [salary, setSalary] = useState('')
  const [totalData, setTotalData] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  useEffect(() => {
    console.log("Fetching Records...")
    setIsLoading(true)
    axios
      .get(`http://127.0.0.1:5000/employee?name=${name}&salary=${salary}`)
      .then(res => {
        console.log("recieved: ", res.data)
        setTotalData(res.data.data)
        setIsLoading(false)
      })
      .catch(err => {
        console.log("error: ", err)
        setIsLoading(false)
      })
  },[name,salary])

  return (
    <div>
      <div className="flex items-center">
        <div className="text-3xl mx-auto my-6">Employees table</div>
      </div>
      <div className="flex justify-start">
        <Link to="/" className="text-lg border-2 border-gray-500 p-2 rounded-md hover:bg-gray-500 hover:text-white transition duration-400 ease-in-out">Back</Link>
      </div>
      <div className='flex justify-around'>
        <div className='text-lg ml-10'>Filter By: </div>
        <div>
          <label htmlFor="name" className='text-xl mr-4'>Name</label>
          <input
            id='name'
            name="name"
            className='border-2'
            type='text'
            value={name}
            onChange={(e) => { setName(e.target.value) }}
          />
        </div>
        <div>
          <label htmlFor='salary' className='text-xl mr-4'>Salary</label>
          <input
            name='salary'
            id='salary'
            className='border-2'
            type='text'
            value={salary}
            onChange={(e) => { setSalary(e.target.value) }}
          />
        </div>
      </div>
      {isLoading ? (<Spinner />) : ""}
      <Table data={totalData} />
    </div>
  )
}

export default Listing