from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from db.sql.models import Base


class SentenceExplosion(Base):
    __tablename__ = "sentences_explosion"
    sentence_id = Column(Integer, primary_key=True, autoincrement=True)
    enemy_id = Column(Integer, ForeignKey("enemies.enemy_id"))
    sentence = Column(String(100), nullable=False)

    enemy = relationship("Enemy", back_populates="sentences_explosion")