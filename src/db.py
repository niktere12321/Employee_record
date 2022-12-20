from sqlalchemy import (DATE, TEXT, VARCHAR, BigInteger, Column, Integer,
                        create_engine)
from sqlalchemy.dialects import sqlite
from sqlalchemy.orm import (Session, declarative_base, declared_attr,
                            sessionmaker)
from sqlalchemy.schema import ForeignKey

BigIntegerType = BigInteger()
BigIntegerType = BigIntegerType.with_variant(sqlite.INTEGER(), 'sqlite')


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=PreBase)


class Roles(Base):
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50))


class Users(Base):
    id = Column(BigIntegerType, primary_key=True)
    fio = Column(TEXT)
    datar = Column(DATE)
    id_role = Column(Integer, ForeignKey(Roles.id))


engine = create_engine(
    'sqlite:///../sqlite.db',
    connect_args={'check_same_thread': False}
)
