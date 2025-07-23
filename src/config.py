import os
from dotenv import load_dotenv

load_dotenv()

LEAGUES = {
    "Testliga": os.getenv("LEAGUE_TEST"),
    "NLA": os.getenv("NLA"),
    "NLB": os.getenv("NLB"),
    "NLC": os.getenv("NLC"),
    "Dinasty": os.getenv("Dinasty")
}
