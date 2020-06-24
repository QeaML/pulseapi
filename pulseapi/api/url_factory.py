class URLFactory:
    def __init__(self, base):
        self.base = base

    def make_webapi(self, page, args, format="json"):
        return (
            f"{self.base}/{page}.php?format={format}"
            f"&{'&'.join([f'{k}={args[k]}' for k in args])}"
        )

    def make_clientapi(self, page):
        return f"http://localhost:3490/v1/{page}"
