from typing import Callable

from sqlalchemy.orm import Session

from .typed import DataTyped


def load_data(session: Session, transform: DataTyped, mapper: Callable) -> None:
    for _, row in transform:
        entity = mapper(row)
        session.add(entity)
