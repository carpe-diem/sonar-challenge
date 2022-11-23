import React, {useState, useEffect} from 'react';
import { useRouter } from "next/router";
import axios from 'axios';


export default function LoginPage() {
    const router = useRouter();
    const [credentials, setCredentials] = useState({
        username:"",
        password:""
    })

    useEffect(() => {
        if (sessionStorage.getItem('token')){
          router.push('/');
        }
      }, []);
    const handleChange = (e)=>{
        setCredentials({
            ...credentials,
            [e.target.name]: e.target.value
        })
    };

    const handleSumbit = async (e)=>{
        e.preventDefault(); 
         const response = await axios.post('http://127.0.0.1:8000/login', credentials);
         console.log(response);
         if(response.status == 200){
            sessionStorage.setItem('token', response.data.access_token)
            router.push('/');
         }

    }; 
    return (
        <form onSubmit={handleSumbit}>
            <input type={"username"} name={'username'} placeholder={'Username'} onChange={handleChange}/>
            <input type={"password"} name={'password'} placeholder={'Password'} onChange={handleChange} />
        <button>Login</button>

        </form>
    )
};
