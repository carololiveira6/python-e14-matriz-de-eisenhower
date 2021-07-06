from app.models.eisenhowers_model import EisenhowerModel

from flask import session


"""
Função que verifica se existe dados na tabela Eisenhower e a partir disso...

Primeira opção: utilizando ORM
query fetch all na model eisenhower

Segunda opção: utilizando psycopg2
query simples do SQL
select all from eisenhower

Caso nao tenha dados: 

Primeira opção:
fazer inserção dos dados utilizando ORM

Segunda Opção:
fazer inserção dos dados utilizando psycopg2
insert..
values...(....)
"""


def verify_eisenhower() -> None:

    types = ["Do It First", "Delegate It", "Schedule It", "Delete It"]

    if not EisenhowerModel.query.fetchall():

        insert_type = [EisenhowerModel(type=type) for type in types]

        session.add_all(insert_type)
        session.commit()

"""
Outra maneira:

do_it_first = EisenhowerModel(id=1, type="Do It First")
delegate_it = EisenhowerModel(id=2, type="Delegate It")
schedule_it = EisenhowerModel(id=3, type="Schedule It")
delete_it = EisenhowerModel(id=4, type="Delete It")

session.add(do_it_first)
session.add(delegate_it)
session.add(schedule_it)
session.add(delete_it)

session.commit()
"""
    