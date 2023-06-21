# Dashboard development.

---
# About the Project.

Macro-Fiscal Dashboard that shows data grabbed from an API.

## Dependencies.

Third party API: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-api-documentation

## Technologies that are used.

- Python
- Dash (Python)
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

## Run Project.

Configure the .env file first. As showed Above, the env.example is a great help for this.

### Docker

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

### Venv

- **First step:**
Run

    ```bash
    python -m venv venv
    ```
    OR

    ```bash
    virtualenv venv
    ```

- **Second step:**
Run the next command:

    ```bash
    source venv/bin/activate
    ```
    This command will enter inside the virtual environment.
    To exit just type in your bash.

    ```bash
    deactivate
    ```

- **Third step:**
Install the requirements inside the virtualenv with

    ```bash
    pip install -r requirements.txt
    ```

- **Fourth step:**
Run the project

    ```bash
    python app/app.py
    ```


- **Fifth step:**
Go to your browser and type:

    ```bash
    http://localhost:8050
    ```


---

# Contact

alejandro.uribe35@gmail.com