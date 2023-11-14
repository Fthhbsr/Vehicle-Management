from sqlalchemy import String, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
engine = create_engine("sqlite:///VehicleMan.db", echo=True)

class Base(DeclarativeBase):
    pass

# Kullanıcılar Tablosu
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))

    companies = relationship("Company", back_populates="users")


# Holding Tablosu
class Holding(Base):
    __tablename__ = 'holding'

    id = Column(Integer, primary_key=True)
    holding_name = Column(String)

    companies = relationship("Company", back_populates="holding")
    # user_id = Column(Integer, ForeignKey('users.id'))
    # company_id = Column(Integer, ForeignKey('companies.id'))

    # user = relationship("User", back_populates="companies")
    # vehicles = relationship("Vehicle", back_populates="company")

# Şirketler Tablosu
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    holding_id = Column(Integer, ForeignKey('holding.id'))
    # user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="companies")
    vehicle = relationship("Vehicle", back_populates="companies")
    holding = relationship("Holding", back_populates="companies")
    # vehicles = relationship("Vehicle", back_populates="company")



# Araçlar Tablosu
class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))
    maintenance_date = Column(DateTime)
    maintenance_detail = Column(String)

    company = relationship("Company", back_populates="vehicles")



Base.metadata.create_all(bind=engine)


# Session = sessionmaker(bind=engine)
# session = Session()

# print("DB will create")
# session.add_all(
#     [
#         User(id=1, name="Ali", last_name="Alkan", email="ali@mail.com", password="12345"),
#         User(id=2, name="Veli", last_name="Balkan", email="veli@mail.com", password="12345"),
#         User(id=2, name="Hafsa", last_name="Tekin", email="hafsa@mail.com", password="12345"),
#         User(id=4, name="Ayşe", last_name="Yılmaz", email="ayse@mail.com", password="12345"),
#         Holding(id=1, holding_name="Holding A"),
#         Company(id=1, company_name="Company Holding", holding_id=1), 
#         Company(id=2, company_name="Company A", holding_id=1), 
#         Company(id=3, company_name="Company B", holding_id=1), 
#         Company(id=4, company_name="Company C", holding_id=1), 
#         Vehicle(id=1, vehicle_name="Skoda", company_id=1), 
        
#     ]
# )
# # with Session(engine) as session:
# #     session.add(students)
# session.commit()


# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     surname: Mapped[str] = mapped_column(String(30))
#     email_address: Mapped[str] = mapped_column(unique=True)
#     password: Mapped[str] = mapped_column(String(10))
#     addresses: Mapped[List["Address"]] = relationship(
#         back_populates="user", cascade="all, delete-orphan"
#     )
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"