from typing import List
from returns.maybe import Maybe
from returns.result import Failure, Success, Result
from sqlalchemy.exc import SQLAlchemyError
from db.sql.models import SentenceExplosion
from db.config import session_maker


def insert_many_sentences_e(sentences: List[SentenceExplosion]):
    return all(map(lambda x: isinstance(x, Success), map(lambda x: insert_sentence_explosion(x), sentences)))


def insert_sentence_explosion(sentence: SentenceExplosion) -> Result[SentenceExplosion, str]:
    with session_maker() as session:
        try:
            session.add(sentence)
            session.commit()
            session.refresh(sentence)
            return Success(sentence)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def get_sentence_explosion_by_id(e_id:int) -> Maybe[SentenceExplosion]:
    with session_maker() as session:
        return Maybe.from_optional(session.get(SentenceExplosion, e_id))

def get_all_sentences_explosion():
    with session_maker() as session:
        return session.query(SentenceExplosion).all()
