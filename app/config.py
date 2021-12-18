import os
import dotenv
from dataclasses import dataclass


dotenv.load_dotenv()


@dataclass
class Config:
    # TODO bool cast

    CHROME_DRIVER_PATH: str
    MAX_WAIT_ELEMENT_APPEARANCE_SEC: int

    NIKE_SITE_URL: str
    NIKE_SNEAKERS_SITE_PATH: str
    NIKE_SITE_LOGIN: str
    NIKE_SITE_PASSWORD: str
    NIKE_SNEAKERS_FULL_URL: str
    NIKE_SNEAKERS_DESIRED_SIZE: str
    NIKE_SNEAKERS_SIZE_PATTERN: str
    NIKE_SNEAKERS_LOWEST_SIZE: str

    @property
    def SITE_URL(self):  # noqa
        return self.NIKE_SITE_URL + self.NIKE_SNEAKERS_SITE_PATH


config = Config(**{k: v for k, v in os.environ.items() if k in Config.__annotations__})
