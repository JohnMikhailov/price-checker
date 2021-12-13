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
    NIKE_SITE_LOGIN: str
    NIKE_SITE_PASSWORD: str


config = Config(**{k: v for k, v in os.environ.items() if k in Config.__annotations__})
