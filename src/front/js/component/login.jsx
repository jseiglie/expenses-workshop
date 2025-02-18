import React, {useContext, useState} from "react";
import { Context } from "../store/appContext";


export const Login = () => {
    const {actions} = useContext(Context);

    const [formData, setFormData] = useState({
        email: "",
        password: "",
     });

     const handleChange = (e) => { 
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
     }


    const handleSubmit = e => { 
        e.preventDefault();
        actions.login(formData);
    }

    return (

        <form className="form w-50 mx-auto" onSubmit={handleSubmit}>
            <h3>Login</h3>
            <input className="form-control" type="text" value={formData.email} name="email" onChange={handleChange} />
            <input className="form-control" type="password" value={formData.password} name="password" onChange={handleChange}/>
            <input className="btn btn-success" type="submit" />
        </form>
    )
}