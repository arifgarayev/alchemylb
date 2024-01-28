import os
import sys
from flow import Flow


from src.utils.common import Utils

os.path.dirname(__file__)


def main(argv):
    if len(argv) == 1:
        print(
            "Please enter a city flag [option]\nTBLISI: -t\nBATUMI: -b\nKUTAISI: -k\n"
        )
        sys.exit(1)

    if argv[1] == "-t":
        flow = Flow(
            Utils.get_json_to_dict("/config/sys/driver.json"),
            Utils.get_json_to_dict("/config/routes/routes_TBLS.json"),
            "./config/gsheetserviceacc/ServiceAccountToken.json",
        )

    elif argv[1] == "-b":
        flow = Flow(
            Utils.get_json_to_dict("/config/sys/driver.json"),
            Utils.get_json_to_dict("/config/routes/routes_BAT.json"),
            "./config/gsheetserviceacc/ServiceAccountToken.json",
        )

    elif argv[1] == "-k":
        flow = Flow(
            Utils.get_json_to_dict("/config/sys/driver.json"),
            Utils.get_json_to_dict("/config/routes/routes_KUT.json"),
            "./config/gsheetserviceacc/ServiceAccountToken.json",
        )

    flow.start()


if __name__ == "__main__":
    main(sys.argv)
