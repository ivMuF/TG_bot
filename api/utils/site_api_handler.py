from typing import Dict

import requests


def _make_response(method: str, url: str, headers: Dict,
                   params: Dict, success=200):
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


def _get_locations(method: str, url: str, headers: Dict,
                   params: Dict, func=_make_response):

    response = func(method, url, headers=headers, params=params)

    return response


class SiteApiInterFace:

    @staticmethod
    def get_locations():
        return _get_locations


if __name__ == '__main__':
    _make_response()
    _get_locations()

    SiteApiInterFace()
