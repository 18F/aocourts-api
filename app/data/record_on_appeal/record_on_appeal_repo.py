from typing import Optional, Any
from sqlalchemy.orm import Session  # , contains_eager

from app.entities import RecordOnAppeal, RecordOnAppealDocketEntry
from .record_on_appeal import run_mappers


run_mappers()


class CrudRoa:
    '''
    Create, read, update, and delete cases
    '''
    def get(self, db: Session, id: Any) -> Optional[RecordOnAppeal]:
        return db.query(RecordOnAppeal).filter(RecordOnAppeal.id == id).one_or_none()

    def add(self, db: Session, roa):
        db.add(roa)

    def create(self, db: Session, roa: RecordOnAppeal) -> RecordOnAppeal:
        db.add(roa)
        return roa


record_on_appeal = CrudRoa()


class CrudRoaDocketEntry:
    '''
    Create, read, update, and delete cases
    '''
    def get(self, db: Session, id: Any) -> Optional[RecordOnAppealDocketEntry]:
        return db.query(RecordOnAppealDocketEntry).filter(RecordOnAppealDocketEntry.id == id).one_or_none()

    def add(self, db: Session, roa_docket):
        db.add(roa_docket)

    def create(self, db: Session, roa_docket: RecordOnAppealDocketEntry) -> RecordOnAppealDocketEntry:
        db.add(roa_docket)
        return roa_docket


record_on_appeal_docket_entry = CrudRoaDocketEntry()
