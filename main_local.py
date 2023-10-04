
from models.models import User,Address 
from models.crud import Insert,Update,Delete,Query 
from models.crud import MockSQLSession
from models.crud import MockSQLSession.Select as Select

session = MockSQLSession()

spongebob = User(
    name="spongebob",
    fullname="Spongebob Squarepants",
    addresses=[Address(email_address="spongebob@sqlalchemy.org")],
)
sandy = User(
    name="sandy",
    fullname="Sandy Cheeks",
    addresses=[
        Address(email_address="sandy@sqlalchemy.org"),
        Address(email_address="sandy@squirrelpower.org"),
    ],
)
patrick = User(name="patrick", fullname="Patrick Star")

session.add_all([spongebob, sandy, patrick])
print(session.query(User).filter_by(name = "spongebob").update({"fullname" : "Super Spongebob Squarepants"}).get_data()) 
print(session)
session.commit()
print(session)