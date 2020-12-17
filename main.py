import requests
import json
import os

from prettytable import PrettyTable
from collections import Counter
from requests.exceptions import HTTPError

from helpers.utils import *

BASE_URL = "https://api.tink.com"
ACCESS_TOKEN = ""


def get_transactions(limit="10"):
    """
    Get last N transactions for a particular provider.
    Default limit set to 10.
    """

    url = BASE_URL + "/api/v1/search"
    params = {"limit": limit}
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"** HTTP error occurred: \n{http_err}")
        raise SystemExit()

    table = PrettyTable()
    table.field_names = ["Date", "Transaction Description", "Amount", "Currency"]

    for result in response.json()["results"]:
        if result["type"] == "TRANSACTION":
            table.add_row(
                [
                    timestampt_to_date(result["transaction"]["date"]),
                    result["transaction"]["description"],
                    result["transaction"]["amount"],
                    result["transaction"]["currencyDenominatedOriginalAmount"][
                        "currencyCode"
                    ],
                ]
            )
    print("\nShowing last " + str(limit) + " transactions")
    print(table)


def get_last_unique_transactions(months=6):
    """
    Gets unique transaction descriptions in last N months incluiding number of ocurrences
    and shows the most frequent ones first.
    Default months set to 6
    """

    startDate = get_current_date()
    endDate = get_relative_delta_date_in_months(months)
    transactions = []

    url = BASE_URL + "/api/v1/search"
    params = {"startDate": startDate, "endDate": endDate}
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"** HTTP error occurred: \n{http_err}")
        raise SystemExit()

    for result in response.json()["results"]:
        if result["type"] == "TRANSACTION":
            transactions.append(result["transaction"]["description"])

    total_transactions = Counter(transactions)
    table = PrettyTable()
    table.field_names = ["Description", "Count"]

    for value, count in total_transactions.most_common():
        table.add_row([value, count])

    print("\nShowing unique transactions in the last " + str(months) + " months")
    print(table)


def get_access_token():
    """
    Generates an ACCESS_TOKEN which is needed for further API calls
    Documentation: https://docs.tink.com/resources/getting-started/retrieve-access-token
    """

    print("Getting access token")
    try:
        response = requests.post(
            BASE_URL + "/api/v1/oauth/token",
            data={
                "code": os.environ.get("CODE"),
                "client_id": os.environ.get("CLIENT_ID"),
                "client_secret": os.environ.get("CLIENT_SECRET"),
                "grant_type": "authorization_code",
            },
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"** HTTP error occurred: \n{http_err}")
        print(f"Please make sure your CODE, CLIENT_ID and CLIENT_SECRET are valid ")
        raise SystemExit()

    jsonData = response.json()
    global ACCESS_TOKEN
    ACCESS_TOKEN = jsonData["access_token"]
    print("access token OK")


if __name__ == "__main__":
    get_access_token()
    # Task 1:
    get_transactions(10)
    # Task 2:
    get_last_unique_transactions(3)