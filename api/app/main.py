#!/usr/bin/env python3

from quart import Quart

app = Quart(__name__)

@app.route('/')
async def check_health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run()
