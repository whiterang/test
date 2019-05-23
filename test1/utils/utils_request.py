import requests


def request(url="", method="GET", headers={}, data=None, json={}):
    """
        requests.request的二次封装方法
    """
    return requests.request(url=url, method=method, headers=headers, data=data, json=json)

# def request(url="", method="POST", headers={}, data=None, json={}):
#     """
#         requests.request的二次封装方法
#     """
#     return requests.request(url=url, method=method, headers=headers, data=data, json=json)