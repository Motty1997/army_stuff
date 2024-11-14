from returns.maybe import Maybe
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from db.sql.models.enemy import Enemy
from db.config import session_maker


def insert_user(user: Enemy) -> Result[Enemy, str]:
    with session_maker() as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return Success(user)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def get_enemy_by_id(e_id: int) -> Maybe[Enemy]:
    with session_maker() as session:
        return Maybe.from_optional(session.get(Enemy, e_id))


def get_enemy_by_email(email: str) -> Maybe[Enemy]:
    with session_maker() as session:
        return Maybe.from_optional(
            session.query(Enemy)
            .filter(Enemy.email == email)
            .options(
                joinedload(Enemy.device_info),
                joinedload(Enemy.sentences_explos),
                joinedload(Enemy.sentences_hostage)
            )
            .first()
        )