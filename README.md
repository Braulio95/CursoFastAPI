#CourseFastAPI
Project that is part of a basic and advanced FastAPI course where all the CRUD methods are used and MySQLAlchemy is used to store the information

## Installation
First execute your virtual enviroment for the project so you do not have any trouble. This project is built in Python 3.11

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.txt file wich contents all the modules and libraries needed to run the project.

```bash
pip install requirements.txt
```

## Usage

```python
# runs the local server project, copy the direction given in your prefered web browser
unvicorn main:app --reload

# lets you choose the port for the local server
unvicorn main:app --reload --port 5000
```
Once you paste the direction in your browser, add /docs in order to access to the documentation of the application.

```
localhost:5000/docs
```




## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
