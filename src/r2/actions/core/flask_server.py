import json
import logging
from json.decoder import JSONDecodeError
from os import makedirs
from os.path import join, exists, abspath
from typing import Union, Any

import requests
import urllib3
from flask import Flask, request, abort, jsonify
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from actions.core.package import Package
from configuration import Configuration
from install import Installation

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FlaskServer:
    app = Flask(__name__)

    def __init__(self, target: str, package: str = 'default', save: bool = True, overwrite: bool = False):
        if not target:
            print("Target is empty")
            raise

        self.target = target
        self.package = package
        self.save = save
        self.overwrite = overwrite

        self._download_dir = abspath(Installation.DOWNLOAD_DIR)
        self.abs_package_path = join(self._download_dir, package)
        if not exists(self.abs_package_path):
            makedirs(self.abs_package_path, exist_ok=True)

    def __call__(self):
        self.app.run()

    def serve(self):
        self.__call__()

    @staticmethod
    def dump_content(endpoint, response_body):
        package = Package(Configuration.read()["package_name"], True)
        package.save(endpoint, response_body)

    @staticmethod
    @app.route('/favicon.ico')
    def favicon():
        return abort(404, description="Resource not found")

    @staticmethod
    @app.route('/', defaults={'path': ''}, methods=["GET", "POST", "PATCH", "DELETE"], strict_slashes=False)
    @app.route('/<path:path>', methods=["GET", "POST", "PATCH", "DELETE"], strict_slashes=False)
    def catch_traffic(path):
        headers = request.headers
        request_data = request.get_data().decode("utf-8")
        payload = None
        if request.content_type and request.content_type.lower() == 'application/json':
            try:
                payload = json.loads(request_data)
            except json.JSONDecodeError as err:
                print(err)
                payload = {}

        return FlaskServer.release_traffic(path, "GET", payload, headers)

    @staticmethod
    def release_traffic(path, method, payload, headers) -> Union[bytes, Any]:
        target = Configuration().read()["target"]

        endpoint = f'{target}/{path}'
        if request.query_string:
            endpoint = f'{endpoint}?{request.query_string.decode("utf-8")}'

        # kwargs = {'verify': False,
        #           'headers': headers}
        kwargs = {'verify': False}
        if payload:
            if headers['Content-Type'] == "application/json":
                kwargs['data'] = json.dumps(payload)
            else:
                kwargs['data'] = payload

        request_method = {'GET': requests.get,
                          'POST': requests.post,
                          'PATCH': requests.patch,
                          'DELETE': requests.delete}[method.upper()]
        response = request_method(endpoint, **kwargs)

        status_code, response_body, headers = response.status_code, response.content.decode("utf-8"), response.headers
        logging.info(endpoint)
        try:
            json_response_body = json.loads(response_body)
            FlaskServer.dump_content(path, json_response_body)
            return json_response_body
        except JSONDecodeError:
            logging.error("JSON response is corrupted")
            print(jsonify({"error": "JSON response is corrupted"}))


if __name__ == "__main__":
    f = FlaskServer(target="http://api.plos.org/", package='default')
    f()
