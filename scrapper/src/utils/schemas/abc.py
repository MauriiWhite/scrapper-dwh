from abc import ABCMeta, abstractmethod


class Mapper(metaclass=ABCMeta):
    @abstractmethod
    def to_entity(self) -> "Entity":
        pass


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def to_dict(self) -> dict:
        pass


class EntityResponse(metaclass=ABCMeta):
    @abstractmethod
    def from_json(self, json) -> "EntityResponse":
        pass

    @abstractmethod
    def results(self):
        pass


class ScrapperABC(metaclass=ABCMeta):
    @abstractmethod
    def scrap(self):
        pass
