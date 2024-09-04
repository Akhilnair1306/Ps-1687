import React from 'react'
import SideNav from './SideNav'
import CardInfo from './CardInfo'

function Dashboard() {
  return (
    <>
    <div className='md:width-64 hidden md:block fixed'>
    <SideNav/>
    </div>
    <div className='ml-64 mt-10'>
    <div className='flex'>
      <CardInfo/>
    </div>
    </div>
    </>
  )
}

export default Dashboard