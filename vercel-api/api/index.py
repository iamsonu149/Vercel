import json

def handler(request, response):
    try:
        names = request.query.getlist("name")

        with open("q-vercel-python.json", "r") as f:
            data = json.load(f)

        marks = [data.get(name, 0) for name in names]

        response.status_code = 200
        response.headers["Content-Type"] = "application/json"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.body = json.dumps({"marks": marks})

        return response
    except Exception as e:
        response.status_code = 500
        response.body = str(e)
        return response
