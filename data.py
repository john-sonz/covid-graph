import json
from datetime import date, datetime
import requests

CASES_HISTORY_URI = "https://pomber.github.io/covid19/timeseries.json"
CASES_CURRENT_URI = "https://coronavirus-19-api.herokuapp.com/countries/poland"


def fetch_data():
    res_curr = requests.get(CASES_CURRENT_URI)
    res_hist = requests.get(CASES_HISTORY_URI)

    if not res_curr.ok:
        raise Exception(f'Fetching current data failed: \n {res_curr.status_code}: {res_curr.text()}')
    if not res_hist.ok:
        raise Exception(f'Fetching history data failed: \n {res_hist.status_code}: {res_hist.text()}')

    cases_current = res_curr.json()
    cases_history = res_hist.json()["Poland"]

    cases_history = list(filter(lambda data: data["confirmed"] > 0 ,cases_history))
    today = date.today()
    last_history_date = datetime.strptime(cases_history[-1]["date"], "%Y-%m-%d").date()

    if last_history_date is not today:
        cases_history.append(
            {
                "date": str(today),
                "confirmed": cases_current["cases"],
                "deaths": cases_current["deaths"],
                "recovered": cases_current["recovered"]
            }
        )

    return cases_history


if __name__ == "__main__":
    print(fetch_data())