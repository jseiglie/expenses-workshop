import React, { useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { CardExpense } from "./cardExpense.jsx";

export const VisualizacionGastos = () => {
    const { store, actions } = useContext(Context);

    useEffect(() => {
        actions.fetchExpenses();
    }, []);


    return (
        <div className="row container">
            {store.expenses?.map(expense => (
                <CardExpense className='col-sm-4 col-md-3 col-lg-3' key={expense.id}
                    category = {expense.category}
                    description={expense.description}
                    amount={expense.amount}
                    eid={expense.id}
                />

            ))}
        </div>
    )

};