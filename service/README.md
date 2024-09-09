# Backend - Python + FastAPI

Retrieves and manipulates 'equipment sensors' data from `postgreSQL` database.  
Created with Python 3.12.

<br>

## How to run

> The backend service depends on the db service

1. Access [http://localhost:8000/docs](http://localhost:8000/docs) to see the Interactive API documentation.
2. You can try out these methods (you can also use API platforms like Postman or Insomnia):

    <br>
    <table>
    <tr>
    <td>GET</td>
    <td><code>/readings/{reading_id: int}</code></td>
    </tr>
    <tr>
    <td>PUT</td>
    <td><code>/readings/{reading_id: int}</code></td>
    </tr>
    <tr>
    <td>DELETE</td>
    <td><code>/readings/{reading_id: int}</code></td>
    </tr>
    <tr>
    <td>GET</td>
    <td><code>/readings/average/{period: '24h'|'48h'|'1w'|'1m'}</code></td>
    </tr>
    <tr>
    <td>POST</td>
    <td><code>/readings/</code></td>
    </tr>
    </table>


<br>

- Note: You can run the backend by itself using [uvicorn](https://www.uvicorn.org/).  
<br>
Create a Virtual Environment using `python -m venv .venv` and activate it using `cd .venv/Scripts && ./activate`.  
<br>
Install the dependencies with `pip install -r requirements.txt` and execute `uvicorn app.main:app --host 0.0.0.0 --port 8000`