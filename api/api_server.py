import sqlite3
from fastapi import FastAPI, HTTPException

from config_util import config


DB_PATH = config['database']['path']
app = FastAPI(
    title="Parts Catalog API",
    description="An API to fetch and manage data related to various machine parts scraped from different manufacturers. \
                It provides endpoints to query parts based on manufacturer, category, model, and other related fields.",
        version="1.0.0"
)

def query_database(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in rows]


@app.get("/parts/")
async def get_parts(manufacturer: str = None):
    base_query = "SELECT * FROM parts_data"
    params = ()
    
    if manufacturer:
        base_query += " WHERE manufacturer=?"
        params = (manufacturer, )
    
    results = query_database(base_query, params)
    
    if not results:
        raise HTTPException(status_code=404, detail="No parts found")

    return results

@app.get("/favicon.ico")
def get_favicon():
    return {}, 204

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# This will start the FastAPI server. You can then access your API at http://127.0.0.1:8000/parts/ and filter results by adding a manufacturer query parameter, e.g., http://127.0.0.1:8000/parts/?manufacturer=Ammann.
# Swagger UI is enabled by default in FastAPI, so you can access the interactive API documentation at http://127.0.0.1:8000/docs.
