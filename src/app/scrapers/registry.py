from typing import Dict, Type, Tuple, Optional

from app.core.models.scraper_task import ScrapingApproach
from app.scrapers.base import BaseScraper
from app.scrapers.dummy.dummy_file_scrarper import DummyFileScraper

class ScraperRegistry:
    def __init__(self):
        self.registry: Dict[str, Tuple[Type[BaseScraper], dict]] = {}

    def register(self, approach: ScrapingApproach, scraper_class: Type[BaseScraper], config: Optional[dict] = None):
        """
        Register a scraper along with its configuration.
        """
        key = self._make_key(approach)
        self.registry[key] = (scraper_class, config or {})

    def get_scraper(self, approach: ScrapingApproach) -> BaseScraper:
        """
        Instantiate the scraper with its registered configuration.
        """
        key = self._make_key(approach)
        scraper_class, config = self.registry.get(key, (DummyFileScraper, {}))
        return scraper_class(config=config)

    def _make_key(self, approach: ScrapingApproach) -> str:
        return f"{approach.platform.lower()}:{approach.mode.lower()}"
