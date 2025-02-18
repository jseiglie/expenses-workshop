import React, { useContext } from "react";
import { Context } from "../store/appContext";

export const CardExpense = ({ description, amount, category, eid }) => {

    const {store, actions} = useContext(Context);

    const expenseTypes = {
        foodAndBeverages: 'food & beverages',
        entertainment: 'entertainment'
    }
    const isCategoryValid = Object.values(expenseTypes).includes(category);

    return (
        <div className="card" style={{ width: "18rem", background: category == 'entertainment' ? 'darkkhaki' : 'green' }} >
            <img src="..." className="card-img-top" alt="..." />
            <div className="card-body">
                <h5 className="card-title">{category}</h5>
                <p className="card-text">{description}</p>
                <p className="card-text">${amount}</p>

                <button onClick={()=>actions.deleteExpense(eid)} className="btn btn-danger">delete</button>
            </div>
        </div>
    )
}