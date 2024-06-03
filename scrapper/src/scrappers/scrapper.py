from time import time
from pprint import pformat
from typing import List, Type, Union
from fake_useragent import UserAgent
from requests.models import Response
from requests import Request, Session
from colorama import Fore, Style

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

        self.__total_time = 0
        self.__counter = 0

        print(
            f"{Fore.GREEN}{Style.BRIGHT}Initializing Scrapper...{Style.RESET_ALL}{Fore.RESET}"
        )

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
        start = time()

        response = self._fetch()
        response = response.json()
        result = self._json_to_entities(response)

        elapsed = time() - start
        self.__total_time += elapsed
        self.__counter += 1

        print(
            f"{Fore.MAGENTA}Item {self.__counter} | {Fore.CYAN}Scraped in {Style.BRIGHT}{elapsed:.2f}s{Style.RESET_ALL}"
        )
        return result

    # Getters and setters
    @property
    def total_time(self):
        return f"{Style.BRIGHT}{Fore.GREEN}Total time: {Fore.MAGENTA}{self.__total_time:.2f}s{Style.RESET_ALL}"

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
    def ua(self):
        return self.__ua

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
