import json
import csv
from distutils.util import strtobool

STRUCTURE_FILE = "structure.csv"
OUTPUT_DIR = "_adventuring_time"

NAME = "minecraft:"
ROOT_NAME = "advancement_supports:_adventuring_time/"


with open(STRUCTURE_FILE, "r", encoding='utf-8') as f:
    s = csv.DictReader(f)
    structure = [ss for ss in s]

# criterias = original["criteria"]
# criterias2 = original2["criteria"]

for s in structure:
    name = s["name"]
    title = s["title"]
    if s["nbt"] == "":
        icon = {
            "item": s["item"]
        }
    else:
        icon = {
            "item": s["item"],
            "nbt": s["nbt"]
        }
    description = s["description"]

    show_toast = False
    if "show_toast" in s:
        show_toast = bool(strtobool(s["show_toast"]))

    announce = False
    if "announce_to_chat" in s:
        announce = bool(strtobool(s["announce_to_chat"]))

    hidden = False

    output = {
        "display": {
            "icon": icon,
            "title": {"text": title},
            "description": {"text": description},
            "show_toast": show_toast,
            "announce_to_chat": announce,
            "hidden": False
        }
    }
    if s["criteria"] != "":

        output["criteria"] = {
            "dummy": {
                "conditions": {
                    "player": [
                        {
                            "condition": "minecraft:entity_properties",
                            "entity": "this",
                            "predicate": {
                                "location": {
                                    "biome": "minecraft:"+s["criteria"]
                                }
                            }
                        }
                    ]
                },
                "trigger": "minecraft:location"
            }
        }

    else:
        output["criteria"] = {
            "slept_in_bed": {
                "conditions": {},
                "trigger": "minecraft:slept_in_bed"
            }
        }

    if s["parent"] != "":
        output["parent"] = ROOT_NAME+s["parent"]

    print(output)

    with open("{}/{}.json".format(OUTPUT_DIR, name), "w", encoding='utf-8') as w:
        json.dump(output, w, indent=4, ensure_ascii=False)
