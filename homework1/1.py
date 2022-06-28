"""
Написать метод domain_name, который вернет домен из url адреса
"""


def domain_name(url: str) -> str:
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")
    ans = url.split(".")[0]
    return ans
