from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///phones.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phones = relationship("Phone", back_populates="user")

    def __str__(self):
        return self.name

    @classmethod
    def add(cls, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def all(cls):
        return session.query(cls).all()


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="phones")

    def __str__(self):
        return self.phone

    @classmethod
    def add(cls, phone, user):
        phone = cls(phone=phone, user=user)
        session.add(phone)
        session.commit()
        return phone

# ---------------------------------------------------------------------Adres


class Adres(Base):
    __tablename__ = 'adress'
    id = Column(Integer, primary_key=True)
    adres = Column(String)
    adr = relationship("Adres", back_populates="adress")

    def __str__(self):
        return self.adres

    @classmethod
    def add(cls, adres):
        adres = cls(adres=adres)
        session.add(adres)
        session.commit()
        return adres

# ---------------------------------------------------------------------City


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    citys = relationship("City", back_populates="city")

    def __str__(self):
        return self.city

    @classmethod
    def add(cls, city, user):
        city = cls(city=city, user=user)
        session.add(city)
        session.commit()
        return city


Base.metadata.create_all(engine)