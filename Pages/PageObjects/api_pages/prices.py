import random

import requests

from Common.CommonFuncs.apicommon import RequestsUtility
from Common.utils import Util
from Configs.Endpoints.endpoints_prices import PRICES


class PricesService(RequestsUtility):

    @classmethod
    def set_random_name(cls, length=10):
        cls.RANDOM_NAME = Util().generate_random_string(length, prefix='Autotest_rules')
        return cls.RANDOM_NAME

    def get_user_task(self):
        api = RequestsUtility(self.env)
        endpoint = PRICES['get_tasks']
        payload = {
            "created_by_me": True,
            "is_file_task": True
        }
        rs_api = api.post(payload=payload, endpoint=endpoint, expected_status_code=200)

        return rs_api.json()

    def delete_user_task(self, task_id):
        api = RequestsUtility(self.env)
        endpoint = PRICES['delete_task'].replace("{task_id}", task_id)
        api.delete(endpoint, expected_status_code=200)

    def upload_file(self):
        api = RequestsUtility(self.env)
        endpoint = PRICES['upload_file']

        task_id = self.get_user_task()
        print(task_id)
        # if task_id:
        #     self.delete_user_task(task_id[0]['taskId'])

        rs_api = api.post(endpoint=endpoint, expected_status_code=200)
        presigned_url = rs_api.text
        print(presigned_url)

        with open('/Users/komronkhisomov/Documents/projects/bristol/Pages/PageObjects/api_pages/prices.xlsx',
                  'rb') as data_file:
            data = data_file.read()

        headers = {"Content-Type": "application/binary"}
        rs_api = requests.put(url=presigned_url, data=data, headers=headers)
        return rs_api

    def download_file(self):
        api = RequestsUtility(self.env)
        endpoint = PRICES['download_file']

        rs_api = api.get(endpoint=endpoint, expected_status_code=200)

    def get_filter_def(self):
        api = RequestsUtility(self.env)
        endpoint = PRICES['get_filter_def']

        rs_api = api.get(endpoint=endpoint, expected_status_code=200)

        return rs_api.json()

    def batchDelete(self, price_id=None):
        api = RequestsUtility(self.env)

        endpoint = PRICES['delete_prices']
        if price_id is not None:
            payload = {"ids": [price_id], "is_excluded_ids": False}
        else:
            payload = {"ids": [], "is_excluded_ids": True}

        print(payload)
        api.delete(endpoint, payload=payload, expected_status_code=204)

    def get_prices(self, task_id):
        api = RequestsUtility(self.env)
        endpoint = PRICES['get_prices'].replace("{task_id}", task_id)
        payload = {
            'offset': 0,
            'limit': 100
        }
        rs_api = api.post(endpoint=endpoint, payload=payload, expected_status_code=200)

        return rs_api.json()

    def get_rules(self):
        api = PricesService(self.env)
        endpoint = PRICES['get_rules']

        rs_api = api.get(endpoint=endpoint, expected_status_code=200)

        return rs_api.json()

    def create_rule(self):
        api = PricesService(self.env)
        endpoint = PRICES['create_rule']

        payload = {
            "rule_name": f"{self.set_random_name()}"
        }

        rs_api = api.post(endpoint=endpoint, payload=payload, expected_status_code=201)

        return rs_api.json()

    def get_filter_def_rules(self):
        api = PricesService(self.env)
        endpoint = PRICES['get_filter_def_rules']

        rs_api = api.get(endpoint=endpoint, expected_status_code=200)

        return rs_api.json()

    def get_rule(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['get_rule'].replace("{rule_id}", rule_id)

        rs_api = api.get(endpoint=endpoint, expected_status_code=200)

        return rs_api.json()

    def edit_rule(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['edit_rule'].replace("{rule_id}", rule_id)

        payload = {
            "rule_name": f"{self.set_random_name()}"
        }

        rs_api = api.put(endpoint=endpoint, payload=payload, expected_status_code=200)

        return rs_api

    def delete_rule(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['delete_rule'].replace("{rule_id}", rule_id)

        rs_api = api.delete(endpoint=endpoint, expected_status_code=200)

        return rs_api

    def get_operations(self):
        api = PricesService(self.env)
        endpoint = PRICES['get_operations']

        rs_api = api.get(endpoint=endpoint, expected_status_code=200)
        return rs_api.json()

    def get_rule_operations(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['get_rule_operations'].replace("{rule_id}", rule_id)

        rs_api = api.get(endpoint=endpoint, expected_status_code=200)
        return rs_api.json()

    def get_operation(self, rule_id, operation_id):
        api = PricesService(self.env)
        endpoint = PRICES['get_rule_operation'].replace("{rule_id}", rule_id).replace("{operation_id}", operation_id)

        rs_api = api.get(endpoint=endpoint, expected_status_code=200)
        return rs_api.json()

    def save_price_period(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['save_price_period'].replace("{rule_id}", rule_id)

        payload = {
            "end_week": "current_week",
            "end_week_day": "saturday",
            "start_date": "calculation_date"
        }

        rs_api = api.post(payload=payload, endpoint=endpoint, expected_status_code=200)
        return rs_api

    def add_operation_to_rule(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['add_operation'].replace("{rule_id}", rule_id)
        payload = {"arguments": {
            "sigma": "[  1.1  ;  2.2  ]"
                                },
                   "code": 1102,
                   "comment": None,
                   "subtitle": None,
                   "outputs": {
                           "next": [{
                            "code": 3001
                           }
                           ]
                   }
        }

        rs_api = api.post(payload=payload, endpoint=endpoint, expected_status_code=200)
        return rs_api

    def update_rule_operation(self, rule_id, operation_id, next_output_id):
        api = PricesService(self.env)
        endpoint = PRICES['edit_operation'].replace("{rule_id}", rule_id).replace("{operation_id}", operation_id)
        payload = {"arguments": {
            "sigma": "[  1.1  ;  3.3  ]"
                                },
                   "code": 1102,
                   "comment": None,
                   "subtitle": None,
                   "outputs": {
                           "next": [{
                            "code": 3001
                           }
                           ]
                   }
        }

        rs_api = api.put(payload=payload, endpoint=endpoint, expected_status_code=200)
        return rs_api

    def delete_rule_operation(self, rule_id, operation_id):
        api = PricesService(self.env)
        endpoint = PRICES['delete_operation'].replace("{rule_id}", rule_id).replace("{operation_id}", operation_id)

        payload = {
            "replace_id": operation_id
        }

        api.delete(payload=payload, endpoint=endpoint, expected_status_code=204)

    def save_price_list(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['save_price_list'].replace("{rule_id}", rule_id)

        payload = {"name": self.set_random_name(24),
                   "is_region": True,
                   "is_locality": False,
                   "priority": 10,
                   "special_appointment": True}

        rs_api = api.post(payload=payload, endpoint=endpoint, expected_status_code=200)
        return rs_api


    def commit_rule(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['commit_rule'].replace("{rule_id}", rule_id)
        rs_api = api.post(endpoint=endpoint, expected_status_code=200)

        return rs_api

    def run_rule(self, rule_id):
        api = PricesService(self.env)
        endpoint = PRICES['run_rule'].replace("{rule_id}", rule_id)
        rs_api = api.post(endpoint=endpoint, expected_status_code=200)

        return rs_api

    def upload_shops_rule(self, rule_id):
        from Configs.token import TOKENS

        api = PricesService(self.env)
        endpoint = PRICES['upload_shops'].replace("{rule_id}", rule_id)

        headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {TOKENS[self.env]['admin_nsi']}"
        }
        files = {
            'file': open('',
                         'rb')}

        rs_api = api.post(endpoint=endpoint, headers=headers, files=files, expected_status_code=200)

        return rs_api

    def upload_products_rule(self, rule_id):
        from Configs.token import TOKENS

        api = PricesService(self.env)
        endpoint = PRICES['upload_products'].replace("{rule_id}", rule_id)
        headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {TOKENS[self.env]['admin_nsi']}"
        }
        files = {'file': (
        'Products.xlsx', open("", 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}

        rs_api = api.post(endpoint=endpoint, headers=headers, files=files, expected_status_code=200)

        return rs_api