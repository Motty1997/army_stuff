from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .enemy import Enemy
from .suspicious_hostage_content_model import SentenceHostage
from .location import Location
from .suspicious_explosive_content_model import SentenceExplosion
from .device_info import DeviceInfo