from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError
from db.sql.models.device_info import DeviceInfo
from db.config import session_maker


def insert_device_info(device_info:DeviceInfo) -> Result[DeviceInfo,str]:
    with session_maker() as session:
        try:
            session.add(device_info)
            session.commit()
            session.refresh(device_info)
            return Success(device_info)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def get_device_info_by_id(d_id: int) -> Maybe[DeviceInfo]:
    with session_maker() as session:
        return Maybe.from_optional(session.get(DeviceInfo, d_id))
