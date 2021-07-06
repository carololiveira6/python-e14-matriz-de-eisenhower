from flask import request, current_app, jsonify

from app.services.helper_service import verify_required_key, verify_missing_key

from app.models.tasks_model import TasksModel
from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError

def verify_values():
    
    required_key = ["name", "description", "duration", "importance", "urgency"]

    session = current_app.db.session

    """
    O usuário insere o JSON:
    {
        "name": "Lavar roupa",
        "description": "",
        "duration": 100,
        "importance": 2,
        "urgency": 1
    }
    """
    data = request.get_json()

    # Verificação entre as chaves inseridas com as chaves corretas
    if verify_missing_key(data, required_key):
        raise MissingKeyError(data, required_key)

    if verify_required_key(data, required_key):
        raise RequiredKeyError(data, required_key)

    # Preenche a tabela mas é preciso fazer agora?
    tasks = TasksModel(**data)

    # Pega os valores das chaves de "importance" e "urgency"
    importance = TasksModel.importance.values()
    urgency = TasksModel.urgency.values()

    """
    Faz as verificações entre os valores de "importance" e "urgency"

    Caso o valor seja menor que 1 ou maior que 2 retornar o erro:

    if (data["importance"].values() < 1 or data["importance"].values() > 2) or (data["urgency"].values() < 1 or data["urgency"].values() > 2):

    {
        "error": {
            "valid options": {
                "importance": [1, 2],
                "urgency": [1,2]
            },
            "recieved options": {
                "importance": data.values(),
                "urgency": data.values()
            }
        }
    }

    Como puxar o valor correspondente na tabela Eisenhower?

    Como preencher a tabela?

    Como retornar 3 dados inseridos e transformar "importance" e "urgency" em "eisenhower_classification" com valor correspondente?
    """
    if importance == 1 and urgency == 1:
        
        return {}
    
    elif importance == 1 and urgency == 2:

        return {}

    elif importance == 2 and urgency == 1:

        return {}

    elif importance == 2 and urgency == 2:

        return {}