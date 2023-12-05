import json
import os

import requests
from loguru import logger

from Configs.hosts_config import API_HOSTS
from Configs.token import TOKENS
from Common.urls import URL_CONFIG


class RequestsUtility(object):

    def __init__(self, env):
        self.env = os.environ.get('ENV', env)
        self.base_url = API_HOSTS[self.env]
        self._url = URL_CONFIG['_url']

    @staticmethod
    def assert_status_code(status_code: int, expected_status_code: int):
        assert status_code == expected_status_code, f"Bad status code. Expected {expected_status_code}," \
                    f"Actual status code: {status_code}"

    def post(self, endpoint, payload=None, files=None, headers=None, token='admin_nsi',
             expected_status_code=201):
        if not headers:
            headers = {"Content-Type": "application/json",
                       "Authorization": f"Bearer {TOKENS[self.env][token]}"}

        url = self.base_url + self._url + endpoint.replace('{', '').replace('}', '')
        logger.info(f"POST URL: {url}")
        rs_api = requests.post(url=url, data=json.dumps(payload), files=files,  headers=headers, timeout=20)
        status_code = rs_api.status_code
        expected_status_code = expected_status_code

        try:
            self.assert_status_code(status_code, expected_status_code)
        except AssertionError as e:
            logger.error(f'POST ERROR MESSAGE:: {rs_api.text}')
            logger.error(e)
            raise AssertionError

        return rs_api

    def get(self, endpoint, params=None, headers=None, token='admin_nsi', allow_redirects=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json",
                       "Authorization": f"Bearer {TOKENS[self.env][token]}"}

        if allow_redirects == False:
            allow_redirects = False
        else:
            allow_redirects = True

        url = self.base_url + self._url + endpoint.replace('{', '').replace('}', '')
        if params:
            logger.info(f"GET URL: {url} with parameters {params}")
        else:
            logger.info(f"GET URL: {url}")

        rs_api = requests.get(url=url, params=params, headers=headers, timeout=20, allow_redirects=allow_redirects)
        status_code = rs_api.status_code
        expected_status_code = expected_status_code

        try:
            self.assert_status_code(status_code, expected_status_code)
        except AssertionError as e:
            logger.error(f'GET ERROR MESSAGE:: {rs_api.text}')
            logger.error(e)
            raise AssertionError

        return rs_api

    def put(self, endpoint, payload=None, headers=None, token='admin_nsi', expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json",
                       "Authorization": f"Bearer {TOKENS[self.env][token]}"}

        url = self.base_url + self._url + endpoint.replace('{', '').replace('}', '')
        logger.info(f"PUT url: {url}")

        rs_api = requests.put(url=url, data=json.dumps(payload), headers=headers, timeout=20)
        status_code = rs_api.status_code
        expected_status_code = expected_status_code

        try:
            self.assert_status_code(status_code, expected_status_code)
        except AssertionError as e:
            logger.error(f'PUT ERROR MESSAGE:: {rs_api.text}')
            logger.error(e)
            raise AssertionError

        return rs_api

    def patch(self, endpoint, payload=None, headers=None, token='admin_nsi', params=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json",
                       "Authorization": f"Bearer {TOKENS[self.env][token]}"}

        url = self.base_url + self._url + endpoint.replace('{', '').replace('}', '')
        logger.info(f"PATCH URL: {url}")

        rs_api = requests.patch(url=url, data=json.dumps(payload), headers=headers, timeout=20, params=params)
        status_code = rs_api.status_code
        expected_status_code = expected_status_code

        try:
            self.assert_status_code(status_code, expected_status_code)
        except AssertionError as e:
            logger.error(f'PATCH ERROR MESSAGE:: {rs_api.text}')
            logger.error(e)
            raise AssertionError

        return rs_api

    def delete(self, endpoint, payload=None, headers=None, token='admin_nsi', expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json",
                       "Authorization": f"Bearer {TOKENS[self.env][token]}"}

        url = self.base_url + self._url + endpoint.replace('{', '').replace('}', '')
        logger.info(f"DELETE URL: {url}")

        rs_api = requests.delete(url=url, data=json.dumps(payload), headers=headers, timeout=20)
        # status_code = rs_api.status_code
        # expected_status_code = expected_status_code
        #
        # try:
        #     self.assert_status_code(status_code, expected_status_code)
        # except AssertionError:
        #     logger.error(f'DELETE ERROR MESSAGE:: {rs_api.text}')
        #     raise AssertionError
        #
        # return rs_api

    @staticmethod
    def pp_json_print(response):
        logger.info(response.json())

