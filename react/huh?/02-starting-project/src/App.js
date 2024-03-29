import React, { useState } from 'react';
import AddUser from './components/Users/AddUser'
import UsersList from './components/Users/UsersList';


function App() {
  const [usersList,setUsersList]= useState([])

  function addUserHandler(uName,uAge){
    setUsersList((userList)=>{
      return [...userList,{ name:uName , age:uAge , id:Math.random().toString() }];
    });
  }
  return (
    <div>
      <AddUser onAddUser={addUserHandler}/>
      <UsersList users={usersList}/>
    </div>
  );
}

export default App;
