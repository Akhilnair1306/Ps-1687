import React from 'react';
import { Link } from 'react-router-dom'; // If you're using react-router for navigation

function SideNav() {

    const menuList = [{
        name: 'Dashboard',
        path: '/dashboard'
    },
    {
        name: 'News',
        path: '/dashboard'
    },
    {
        name: 'Alerts',
        path: '/dashboard'
    },
    {
        name: 'GeoLocation',
        path: '/dashboard'
    }
    ]
  return (
    <div className='h-screen w-56 p-8 text-black shadow-md flex flex-col'>
        <div className='flex justify-center'>
        Logo
        </div>
        <div className='mt-10'>
            {menuList.map((menu,index) => (
                <div className='flex mb-2 p-3 hover:bg-purple-600 hover:text-white rounded-lg cursor-pointer text-xl'>
                    <h2>{menu.name}</h2>
                </div>
            ))}
        </div>
    </div>
  );
}

export default SideNav;
