def app(environ, start_response):
    s = environ["QUERY_STRING"]
    data = "\n".join(s.split("&"))
    data = (data + "\n").encode()
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])