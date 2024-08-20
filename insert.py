from models import *
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session

with Session(engine) as session:
    # tank = Category(category_name='Support', description='Tanks is main category in the game')
    # session.add(tank)
    # session.commit()

    # category = session.query(Category).all()
    # for cat in category:
    #     print(f'{cat.id}. name :{cat.category_name} - des {cat.description}')

    # catt = select(Category).where(Category.category_name == 'Tank')
    # for result in session.scalars(catt):
    #     print(result.category_name)

    # catt = select(Category)
    # for user in session.scalars(catt):
    #     print(user.category_name)

    # catt = select(Category)
    # n = session.scalar(catt)
    # print(n.description)
    
    # inwoker = Character(name='Inwoker', description='Support', atack=10, defense=20, hp=123, mana=321, speed=12, intelligense=12, strength=123, agility=123, category_id=2)
    # session.add(inwoker)
    # session.commit()
    # pudge = Character(name='Pudge', description='Tank', atack=10, defense=20, hp=123, mana=321, speed=12, intelligense=12, strength=123, agility=123, category_id=2)
    # session.add(pudge)
    # session.commit()

    # char = session.query(Character).all()
    # for c in char:
    #     print(c.name, c.description, c.category.category_name)

    # a_1 = Map(lines='2', monsters=2, roshan=2, runes='qwer2', day=True)
    # session.add(a_1)
    # a_2 = Map(lines='2', monsters='2', roshan='2')
    # session.add(a_2)
    # a_3 = Map(lines='3', monsters='3', roshan='3', runes='qwer3', day=False)
    # session.add(a_3)
    # b_1 = Item(name='abc', price='10', passive='abc123', active='qwert', atack=1234, hp=1000, speed=123, atack_speed=21345, intelligense=1234, defense=35543)
    # session.add(b_1)
    # b_2 = Item(name='abc', price='20', passive='abc123123', active='qwert2', atack=1234, hp=1000, speed=123, atack_speed=21345, intelligense=1234, defense=35543)
    # session.add(b_2)
    # b_3 = Item(name='abc', price='30', passive='abc1233212', active='qwert3', atack=1234, hp=1000, speed=123, atack_speed=21345, intelligense=1234, defense=35543)
    # session.add(b_3)
    # session.commit()
