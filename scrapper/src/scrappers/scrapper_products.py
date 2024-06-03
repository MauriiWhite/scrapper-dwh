from typing import List, Type, Optional

from scrappers.scrapper import Scrapper
from utils.errors.scrapper import ScrapperException


class ScrapperProducts(Scrapper):
    def __init__(
        self,
        base_url,
        headers,
        method,
        json,
        entity_response,
        mapper,
    ):
        super().__init__(
            base_url=base_url,
            headers=headers,
            method=method,
            json=json,
            entity_response=entity_response,
            mapper=mapper,
        )

    def scrap(
        self,
        page: Optional[int] = None,
        amount: Optional[int] = None,
        category: Optional[str] = None,
    ) -> List[Type]:

        if page is not None:
            self.json["page"] = page
        if amount is not None:
            self.json["hitsPerPage"] = amount
        if category is not None:
            self.json["categories"] = category

        try:
            return super().scrap()
        except ScrapperException as e:
            raise ScrapperException(f"Scrap failed: {e}")
