# Dashboard development.

---
# About the Project.

Prueba de ingreso para el BID. Se debe desarrollar un dashboard #TODO: traducir

## Dependencies.

Third party API: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-api-documentation

## Technologies that are used.

- Python
- Docker

---

# Initializing the project.

## Requirements

### Technologies.


- **Docker Installation**

    [Docker Desktop](https://www.docker.com/products/docker-desktop/)

---

### Environment Variables.


- **API_URL:** Documentation: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information


| ENV_VARs | Summary of variable |
| --- | --- |
| API_URL | API Url that is going to be used to make requests, in this case the API of the World Bank. http://api.worldbank.org/v2/ |

---

# Execution of Project.

### Run Project.


- **First step:**
Be sure to have docker installed and running. Check docker installation.

- **Second step:**
Run the next command:

    ```bash
    docker-compose up --build
    ```
    This command will create the docker container and run the proyect.

- **Third step:**
Go to your browser and type:
    ```bash
    http://localhost:8050
    ```

---

# Contact

alejandro.uribe35@gmail.com