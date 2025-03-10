import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";

export const Categorizador = () => {
    
    const {store, actions} = useContext(Context);

    const [formData, setFormData] = useState({
        price: "",
        description: ""
     });
     const [loading, setLoading] = useState(false);
     const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
      };

      const handleSubmit = async e => {
        e.preventDefault();
        setLoading(true);
        await actions.categorize(formData);
        setFormData({
            price: "",
            description: "" 
       });
         setLoading(false);
    };

    return (
        <div>
            {loading  && <div className="spinner-border text-primary" role="status"></div>}
            <form className="form mx-auto w-50" onSubmit={handleSubmit}>
                <input className="form-control" type="number" name="price" value={formData.price} onChange={handleChange} />
                <textarea className="form-control" name="description" value={formData.description} onChange={handleChange} cols={50}/>
                <input className="btn btn-success" type="submit" />
            </form>
        </div>
    )
};
