from dotenv import load_dotenv
from os import getenv

load_dotenv(override=True)

LINKEDIN_ACCEESS_TOKEN = getenv('LINKEDIN_ACCEESS_TOKEN')
LINKEDIN_ACCEESS_TOKEN_EXP = getenv('LINKEDIN_ACCEESS_TOKEN_EXP')
HEADLESS = getenv('HEADLESS')