# Backend - Python + FastAPI

Retrieves and manipulates 'equipment sensors' data from `postgreSQL` database.  
Created with Python 3.12.

<br>

## How to run
1. Make sure you have [Docker](https://docs.docker.com/engine/install/) installed.
2. Run `docker compose up` on a terminal in the root of the `services` folder.
3. Check Docker Desktop > Containers or run `docker ps` to see if all containers are running.
> The backend service depends on the db service
3. Access [http://localhost:8000/docs](http://localhost:8000/docs) to see the Interactive API documentation.
4. You can try out these methods (you can also use API platforms like Postman or Insomnia):

    <br>
    <table>
    <tr>
    <td>GET</td>
    <td><code>/readings/{reading_id: int}`</code></td>
    </tr>
    <tr>
    <td>PUT</td>
    <td><code>`/readings/{reading_id: int}`</code></td>
    </tr>
    <tr>
    <td>DELETE</td>
    <td><code>`/readings/{reading_id: int}`</code></td>
    </tr>
    <tr>
    <td>GET</td>
    <td><code>`/readings/average/{period: '24h'|'48h'|'1w'|'1m'}`</code></td>
    </tr>
    <tr>
    <td>POST</td>
    <td><code>`/readings/`</code></td>
    </tr>
    </table>

<br> 