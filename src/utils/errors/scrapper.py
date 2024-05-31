class ScrapperException(Exception):
    def __init__(self, message: str = "Error scrapper in the process of scraping"):
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
