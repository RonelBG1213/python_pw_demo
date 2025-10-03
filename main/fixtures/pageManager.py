import logging
from main.functions.dashboard import dashboardFunctions
from main.fixtures.navigation import navigationFunctions


class PageManager:
    def __init__(self, page):
        self.page = page
        self.logger = logging.getLogger(__name__)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s [%(levelname)8s] %(name)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

        self.dashboard = dashboardFunctions(page, self.logger)
        self.navigation = navigationFunctions(page, self.logger)