import time
import firefly_iii_client
from pprint import pprint
from firefly_iii_client.api import about_api, transactions_api
from firefly_iii_client.model.cron_result import CronResult
from firefly_iii_client.model.system_info import SystemInfo
from firefly_iii_client.model.transaction_split_store import TransactionSplitStore
from firefly_iii_client.model.transaction_store import TransactionStore
from firefly_iii_client.model.transaction_type_property import TransactionTypeProperty
from firefly_iii_client.model.user_single import UserSingle

import pandas as pd

# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
from reader import BankFileReader
from transaction_element import TransactionElement

configuration = firefly_iii_client.Configuration(
    host="http://192.168.1.2:6182"
)

from datetime import datetime

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host="http://192.168.1.2:6182"
)
configuration.access_token = "XXX"
configuration.host = 'http://192.168.1.2:6182'

if __name__ == "__main__":
    #read file

    input_filepath = "/home/frivas/Downloads/10012023_1479_0001282729.txt"
    input_filepath = "/home/frivas/Downloads/23012023_1479_0001282729.txt"

    reader = BankFileReader(input_filepath)


    # Enter a context with an instance of the API client
    with firefly_iii_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = about_api.AboutApi(api_client)
        try:
            # System information end point.
            api_response = api_instance.get_about()
            pprint(api_response)
        except firefly_iii_client.ApiException as e:
            print("Exception when calling AboutApi->get_about: %s\n" % e)



        # store a new transaction

        # datetime.strptime(single_data, '%Y-%m-%d %H.%M.%S')

        for transaction in reader:
            transaction:TransactionElement = transaction

            transaction_params = {
                "book_date": None, #dateutil_parser('1970-01-01T00:00:00.00Z'),
                "date": transaction.date,
                "description": transaction.description,
                "due_date": None,
                "external_url": "",
                "interest_date": None,
                "internal_reference": "",
                "invoice_date": None,
                "notes": "",
                "payment_date": None,
                "process_date": None,
                # "source_id": "1",
                # "source_name": "Sabadell",
                "category_name": transaction.classification,
            }

            extra_args = {}
            if transaction.amount > 0:
                extra_args = {
                    "amount": str(transaction.amount),
                    "destination_id": "1",
                    "destination_name": "Sabadell",
                    "type": TransactionTypeProperty("deposit")
                }
            else:
                extra_args = {
                    "amount": str(-transaction.amount),
                    "source_id": "1",
                    "source_name": "Sabadell",
                    "type": TransactionTypeProperty("withdrawal")
                }
            transaction_params.update(extra_args)

            extra_args_tags = {}
            if len(transaction.tags) != 0:
                extra_args_tags["tags"] = transaction.tags

            transaction_params.update(extra_args_tags)


            api_transaction = transactions_api.TransactionsApi(api_client)

            transactions = [
                TransactionSplitStore(**transaction_params)
                ]


            # print(transaction)
            # print("-----")

            transaction_store = TransactionStore(
                apply_rules=False,
                error_if_duplicate_hash=False,
                fire_webhooks=True,
                group_title="Split transaction title.",
                transactions=transactions)

            try:
                # Store a new transaction
                api_response = api_transaction.store_transaction(transaction_store)
                # pprint(api_response)
            except firefly_iii_client.ApiException as e:
                print("Exception when calling TransactionsApi->store_transaction: %s\n" % e)


