from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from db.sql.models import Base


class Enemy(Base):
    __tablename__ = "enemies"
    enemy_id =  Column(Integer,primary_key=True, autoincrement=True)
    email  = Column(String(100),nullable=False)
    enemy_name = Column(String(100),nullable=False)
    ip_address = Column(String(100),nullable=False)
    created_at = Column(String(100),nullable=False)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    device_id = Column(Integer, ForeignKey("devices_info.device_info_id"))

    location = relationship("Location",back_populates="enemy",lazy="joined")
    device_info = relationship("DeviceInfo",back_populates="enemy",lazy="joined")
    sentences_hostage = relationship("SentenceHostage",back_populates="enemy",lazy="joined")
    sentences_explosion = relationship("SentenceExplosion",back_populates="enemy",lazy="joined")


    def enemy_to_dict(self):
        return {
            "enemy_id": self.enemy_id,
            "email": self.email,
            "enemy_name": self.enemy_name,
            "ip_address": self.ip_address,
            "created_at": self.created_at,
            'location': self.location.to_dict(),
            'device_info':self.device_info.to_dict(),
            'sentences_hostage': [sentence.sentenc for sentence in self.sentences_hostage],
            'sentences_explosion': [sentence.sentence for sentence in self.sentences_explosion]
        }
