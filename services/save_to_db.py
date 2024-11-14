from typing import List
from db.sql.models.device_info import DeviceInfo
from db.sql.models.location import Location
from db.sql.models.suspicious_explosive_content_model import SentenceExplosion
from db.sql.models.suspicious_hostage_content_model import SentenceHostage
from db.sql.models.enemy import Enemy
from app.dbs.psql.repository.device_info_repository import insert_device_info
from app.dbs.psql.repository.location_repository import insert_location
from app.dbs.psql.repository.sentences_explos_repository import insert_sentence_explos, insert_many_sentences_e
from app.dbs.psql.repository.sentences_hostage_repository import insert_sentence_hostage, insert_many_sentences_h
from app.dbs.psql.repository.user_repository import insert_user


def save_to_db(message, type_sentence):
    location_id = insert_location(Location(**message['location'])).unwrap().location_id
    device_id = insert_device_info(DeviceInfo(**message['device_info'])).unwrap().device_info_id
    only_user = {k: v for k,v in message.items() if isinstance(v, str)}
    only_user.pop('id')
    only_user['location_id'] = location_id
    only_user['device_id'] = device_id
    user_id = insert_user(Enemy(**only_user)).value_or(0).user_id
    if type_sentence == 'E':
        sentences_explosion = [SentenceExplosion(sentence=sentence, user_id=user_id)
                               for sentence in message['sentences']]
        insert_many_sentences_e(sentences_explosion)

    if type_sentence == 'H':
        sentences_hostage = [SentenceHostage(sentence=sentence, user_id=user_id)for sentence in message['sentences']]
        insert_many_sentences_h(sentences_hostage)
        