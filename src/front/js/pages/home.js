import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Login } from "../component/login.jsx";
import { Categorizador } from "../component/categorizador.jsx";
import { VisualizacionGastos } from "../component/visualizacionGastos.jsx";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			{
			!store.user ? <Login /> : <div> 
				<h1>Welcome {store.user?.email}</h1>
				<Categorizador />
				<VisualizacionGastos />
			</div>
			}
		</div>
		
	);
};
