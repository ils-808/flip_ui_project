import os
import pydantic_settings
from typing import Literal
from dotenv import load_dotenv

from flip_ui_project_tests.utils.resource_handler import get_path

load_dotenv(get_path('.env.mobile.credentials'))
lgn = os.getenv('login')
pwd = os.getenv('password')


class Configure(pydantic_settings.BaseSettings):
    context: Literal['local', 'remote'] = 'remote'
    deviceName: str = 'Pixel_3a_API_34_extension_level_7_x86_64'
    timeout: float = 20.0
    app: str = 'flip2.apk'
    server_url: str = 'http://127.0.0.1:4723'
    platformVersion: str = "13.0"
    login: str = lgn
    password: str = pwd


loaded_configuration = Configure(_env_file=get_path(f'.env.mobile.{Configure().context}'))
