from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError
from db.sql.models.location import Location
from db.config import session_maker


def insert_location(location:Location) -> Result[Location,str]:
    with session_maker() as session:
        try:
            session.add(location)
            session.commit()
            session.refresh(location)
            return Success(location)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def get_location_by_id(l_id:int) -> Maybe[Location]:
    with session_maker() as session:
        return Maybe.from_optional(session.get(Location, l_id))