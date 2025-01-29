import openai
import os
import json

# Obtener la clave de API de OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("La clave API de OpenAI no está configurada")

# Crear cliente de OpenAI
client = openai.OpenAI(api_key=api_key)

def categorize_expense(description):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente que categoriza gastos."},
            {"role": "user", "content": f'Categoriza el siguiente gasto: {description}. Solo devuelve un diccionario en formato JSON con la estructura {{"categoria": "", "subcategoria": ""}}.'}
        ]
    )

    # Convertir el string JSON en un diccionario de Python
    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        return {"error": "No se pudo procesar la respuesta"}

# Ejemplo de uso
expense = "Compra de un libro de programación"
print(categorize_expense(expense))
