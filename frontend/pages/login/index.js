import React, {useState
} from 'react';
import axios from 'axios';
import { useRouter } from "next/router";


export default function LoginPage() {
  const router = useRouter();
    const [credentials, setCredentials] = useState({
        username:"",
        password:""
    })
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
