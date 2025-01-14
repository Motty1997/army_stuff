from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from db.sql.models import Base


class DeviceInfo(Base):
    __tablename__ = "devices_info"
    device_info_id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String, nullable=False)
    os = Column(String, nullable=False)
    device_id = Column(String, nullable=False)

    enemy = relationship("Enemy", back_populates="device_info")


    def device_info_to_dict(self):
        return {
            "device_info_id": self.device_info_id,
            "browser": self.browser,
            "os": self.os,
            "device_id": self.device_id
        }
