from json import load
from pathlib import Path

robot_name = "shopee_pinterest"

config_json = load(open(Path(Path(__file__).parent.parent, "config.json")))

email = config_json["email"]
password = config_json["password"]