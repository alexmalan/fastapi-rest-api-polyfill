FastAPI REST Polyfilling
========================

### Description
-   FastAPI REST is a service that provides polylines filling.
-   Best practices for configuration split and project structure;

## Code quality

### Static analysis
- Static code analysis used: https://deepsource.io/

### Pylint
- Pylint used to maintain code quality;
- Current status: `Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)`

### Requirements

-   It is assumed that you have Python. If not, then download the latest versions from:
    * [Python](https://www.python.org/downloads/)
    * [PostgreSQL](https://www.postgresql.org/download/)

### Installation

1. **Clone git repository**:
    ```bash
    git clone https://github.com/alexmalan/fastapi-rest-api-polyfill.git
    ```

2. **Create virtual environment**
	- You can use `virtualenv` or `venv` or conda environment for this.
    ```bash
    python -m venv $(pwd)/venv
    source venv/bin/activate
    ```

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add environment variables**
    - Create a file named `.env` in project root directory
    - Add and fill next environment variables with your local database config:
        ```.env
        DATABASE_NAME=
        DATABASE_USER=
        DATABASE_PASSWORD=
        DATABASE_HOST=
        ```

5. **Make migrations**:
    ```bash
    python make_migrations.py
    ```

## Run

-   Run APP using command:
    ```bash
    uvicorn main:app --reload
    ```
- Localhost resources:
    * localhost:<port_id>/docs/ - documentation
    * localhost:<port_id>/redoc/ - redoc documentation
    * localhost:<port_id>/api/v1/polys/   - endpoints
    
## Postman Configuration

### Library Import
* Find the fastapi-rest-polylines.postman_collection.json in the root directory
- Open Postman
   - File
      - Import
         - Upload files
            - Open

## Files
* `main` - Main application file
* `make_migrations` - Migration script
* `app/` - Back-end code
* `venv/` - Virtual environment files used to generate requirements;

## Test

- Tests are done with pytest
- Using pytest:
    - For following options are available:
        - `-v` - to have verbose tests
    
    - Windows:
    ```bash
    pytest
    ```
    
    - OS X:
    ```bash
    pytest
    ```
## Design Notes
### Reasoning

# Logic Requirements
## Exercise1 (Required)

The goal of this exercise is to understand your reasoning and see how resourceful you can be with geometrical problems.

You are given a Python .bin file that has been created using the pickle library. This will be the input of your function.

The content of that file is list with a single closed polyline, which is made from a list of 10 lists, each containing 2 point elements, also lists [x, y], representing the  x and y coordinates of said point.

Your job is to output a numpy array of the following dimensions (19200, 10800), all full of zeroes, and to represent with ones the points that are on the polyline or inside it. Effectively you will be drawing the shape on the array and colouring it in.

Be aware that the ones do not only need to be the vertices of the polyline, but also the edges and the inside of them. That is, if the shape happened to be a rectangle (which is not), then we would be expecting all points inside that rectangle to be ones:

i.e. (View on raw code to see the rectangle)

```
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
```

You will be scored both on your reasoning, clarity of code and result. Please add comments where needed and have at least 1 unit test to run the script from it. If you add more tests we will be running them too and checking the result.

## Exercise2 (Required)

For this exercise you will be creating a small microservice using FastAPI. Your aim is to create a small microservice using the mentioned library and to create and endpoint where you would post the shape from the last exercise as payload and would return the numpy array as feedback
It is up to you to determine the format of said payload and return.