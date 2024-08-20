from sqlalchemy import create_engine, Integer, String, Text, ForeignKey, DECIMAL, DATE, Boolean
from sqlalchemy.orm import DeclarativeBase, mapped_column, Session, Mapped, relationship
from engine import MYSQL_URL

engine = create_engine(MYSQL_URL, echo=True)
session = Session(engine)

class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = 'category'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_name:Mapped[str] = mapped_column(String(50), nullable=False)
    description:Mapped[str] = mapped_column(Text)

    character = relationship("Character", back_populates="category")

class Character(Base):
    __tablename__ = 'characters'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(50), nullable=False)
    description:Mapped[str] = mapped_column(Text)
    atack:Mapped[int] = mapped_column(Integer)
    defense:Mapped[int] = mapped_column(Integer)
    hp:Mapped[int] = mapped_column(Integer)
    mana:Mapped[int] = mapped_column(Integer)
    speed:Mapped[int] = mapped_column(Integer)
    intelligense:Mapped[int] = mapped_column(Integer)
    strength:Mapped[int] = mapped_column(Integer)
    agility:Mapped[int] = mapped_column(Integer)

    category_id:Mapped[int] = mapped_column(ForeignKey('category.id'))
    category = relationship("Category", back_populates='character')

class Map(Base):
    __tablename__ = 'map'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lines:Mapped[str] = mapped_column(String(10), nullable=False)
    monsters:Mapped[int] = mapped_column(Integer, nullable=True)
    roshan:Mapped[int] = mapped_column(Integer, nullable=True)
    runes:Mapped[str] = mapped_column(String(20), nullable=True)
    day:Mapped[bool] = mapped_column(Boolean, nullable=True)

class Item(Base):
    __tablename__ = 'item'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(20), nullable=False)
    price:Mapped[int] = mapped_column(Integer, nullable=True)
    passive:Mapped[str] = mapped_column(String(20), nullable=True)
    active:Mapped[str] = mapped_column(String(10), nullable=True)
    atack:Mapped[int] = mapped_column(Integer, nullable=True)
    hp:Mapped[int] = mapped_column(Integer, nullable=True)
    speed:Mapped[int] = mapped_column(Integer, nullable=True)
    atack_speed:Mapped[int] = mapped_column(Integer, nullable=True)
    intelligense:Mapped[int] = mapped_column(Integer, nullable=True)
    defense:Mapped[int] = mapped_column(Integer, nullable=True)
    


Base.metadata.create_all(engine)