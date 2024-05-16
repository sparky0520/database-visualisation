import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Welcome from './pages/Welcome'
import Listing from './pages/Listing'

function App() {
  return (
    <div className='max-w-6xl mx-auto h-screen'>
      <BrowserRouter>
        <Routes>
          <Route index element={<Welcome />}/>
          <Route path='/listing' element={<Listing />}/>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
