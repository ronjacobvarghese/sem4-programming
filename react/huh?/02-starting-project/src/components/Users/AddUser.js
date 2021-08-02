import Card from "../UI/Card";
import styles from "./adduser.module.css";
import ErrorModel from "../UI/ErrorModel";
import Button from "../UI/Button";
import { useState,Fragment, useRef } from "react";

function AddUser(props) {
  const nameInputRef = useRef();
  const ageInputRef = useRef();
  const [error,setError]= useState();

  function AddUserHandler(event) {
    const enterUsername=nameInputRef.current.value
    const enterAge=ageInputRef.current.value
    event.preventDefault();
    if(enterUsername.trim().length === 0 || enterAge.trim().length === 0){
        setError({
          title:'Invalid Input',
          message:'Please enter a valid name and age.'
        })
        return;
    }
    if(+enterAge < 1){
      setError({
        title:'Invalid Input',
        message:'Please enter a valid age'
      })
        return;
    }
    props.onAddUser(enterUsername,enterAge)
    nameInputRef.current.value=""
    ageInputRef.current.value="";
  }
  function ErrorHandler(){
    setError(null);
  }

  return (
    <Fragment>
      {error && <ErrorModel title={error.title} message={error.message} onConfirm={ErrorHandler}/>}              
      <Card className={styles.input}>
        <form onSubmit={AddUserHandler}>
          <label htmlFor="username">Username</label>
          <input
            id="username"
            type="text"
            ref={nameInputRef}
          />
          <label htmlFor="age">Age(Years)</label>
          <input
            id="age"
            type="text"
            ref={ageInputRef}
          />
          <Button type="submit">Add User</Button>
        </form>
      </Card>

    </Fragment>
  );
}

export default AddUser;
