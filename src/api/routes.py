"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Category, Expense
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

from api.services.categorizer import categorize_expense  
api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200



@api.route('/categorize_expense', methods=['POST'])
def categorize_expenses():
    data = request.get_json()
    expense_id = data.get('expense_id')
    description = data.get('description')

    # categorizer = Categorizer()
    # categorizer.categorize_expense(description)
    # Llamar a la API de ChatGPT para obtener la categoría
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=f'Categoriza el siguiente gasto: {description}. Solo devuelve una categoría y su subcategoria en formato diccionario de python con la estructura  
    #                 {"categoria": "",
    #                 "subcategoria": "Libros"} .',
    #                 max_tokens=10
    #                     )
    # category = response.choices[0].text.strip()

    # Actualizar la categoría del gasto en la base de datos
    category =categorize_expense(description)
    print(category)
    expense = Expense.query.get(expense_id)
    if expense:
        expense.category = category
        db.session.commit()
        return jsonify(expense.serialize()), 200
    else:
        return jsonify({"error": "Expense not found"}), 404