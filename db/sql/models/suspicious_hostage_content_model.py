from db.sql.models import Base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class SentenceHostage(Base):
    __tablename__ = "sentences_hostage"
    sentence_id = Column(Integer, primary_key=True, autoincrement=True)
    enemy_id = Column(Integer, ForeignKey("enemies.enemy_id"))
    sentence = Column(String(100), nullable=False)

    enemy = relationship("User", back_populates="sentences_hostage")