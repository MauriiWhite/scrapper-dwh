from pprint import pformat
from typing import List, Type, Union
from fake_useragent import UserAgent
from requests.models import Response
from requests import Request, Session

from utils.schemas.enums import Method
from utils.schemas.abc import ScrapperABC


class Scrapper(ScrapperABC):
    def __init__(
        self,
        base_url: str,
        headers: Union[dict, None],
        method: Method,
        json: Union[dict, None],
        entity_response: Type,
        mapper: Type,
    ):
        self.__entity_response = entity_response
        self.__mapper = mapper

        self.__base_url = base_url
        self.__headers = headers
        self.__method = method.upper()
        self.__json = json

        self.__ua = UserAgent()
        self.__session = Session()

    def _json_to_entities(self, json: dict) -> List[Type]:
        entity_response = self.__entity_response.from_json(json)
        entities = [
            self.__mapper.to_entity(entity) for entity in entity_response.results
        ]
        return entities

    def _fetch(self) -> Response:
        self.__headers["user-agent"] = self.__ua.random
        request = Request(
            url=self.__base_url,
            headers=self.__headers,
            method=self.__method,
            json=self.__json,
        )
        prepared_request = self.__session.prepare_request(request)
        response = self.__session.send(prepared_request)
        return response

    def scrap(self) -> List[Type]:
        response = self._fetch()
        response = response.json()
        return self._json_to_entities(response)

    # Getters and setters

    @property
    def base_url(self):
        return self.__base_url

    @base_url.setter
    def base_url(self, base_url):
        self.__base_url = base_url

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, headers):
        self.__headers = headers

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method):
        self.__method = method

    @property
    def entity_response(self):
        return self.__entity_response

    @entity_response.setter
    def entity_response(self, entity_response):
        self.__entity_response = entity_response

    @property
    def mapper(self):
        return self.__mapper

    @mapper.setter
    def mapper(self, mapper):
        self.__mapper = mapper

    @property
    def ua(self):
        return self.__ua

    @ua.setter
    def ua(self, ua):
        self.__ua = ua

    @property
    def json(self):
        return self.__json

    @json.setter
    def json(self, json):
        self.__json = json

    def __repr__(self) -> str:
        return pformat(self.__dict__)

    def __str__(self) -> str:
        return pformat(self.__dict__)
