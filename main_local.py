
from models.models import User,Address 
from models.crud import select,delete,insert
from models.crud import MockSQLSession

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

# Logic_name: test add, add_all, filte_by,update, commit 
session.add_all([spongebob, sandy, patrick])
print(session.query(User).filter_by(name = "spongebob").update({"fullname" : "Super Spongebob Squarepants"}).data) 
print(session)
session.commit()
print(session)

# Logic_name: test select
print(select(User).where(User.name == 'spongebob'))

print(session.execute(insert(User),[User(name='spongebob_thongchu', fullname='Super Spongebob Squarepants')]))
session.commit()
print(session)
print("\n-----------------------------------------------:",)

print(session.execute(delete(User).where(User.id == 1)))
print(session)
print("\n-----------------------------------------------:",)

print(session.execute(select(User)).scalars())
print(session)
print("\n-----------------------------------------------:",)


# self.db.execute(insert(BacktestResultDetail), [i.model_dump() for i in trades])
# self.db.execute(delete(BacktestResultDetail)
# .where(BacktestResultDetail.backtest_results_id == result_id))
# self.db.execute(select(BacktestResult).where(BacktestResult.strategy_id == strategy_id)).scalar_one