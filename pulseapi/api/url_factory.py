import urllib.parse

class URLFactory:
    def __init__(self, base):
        self.base = base

    def make_webapi(self, page, args, format="json"):
        query = '&'.join([
            f'{k}={urllib.parse.quote(v)}' for k,v in args.items()
        ])
        return f"{self.base}/{page}.php?format={format}&{query}"

    def make_clientapi(self, page):
        return f"http://localhost:3490/v1/{page}"
