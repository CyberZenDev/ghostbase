# Ghostbase  

## Introduction

Ghostbase is a Python library that provides a simple interface for interacting with a Flask server that manages user databases. With Ghostbase, you can create databases, add users, validate user credentials, and edit user pro status.

## Getting Started

### Installation

To use Ghostbase, you will need to have the `requests` library installed. You can install it using pip:

```bash
pip install requests
```

### Setting up the Flask Server

Before using Ghostbase, you will need to set up the Flask server that it interacts with. You will need to set the `base_url` variable to the URL of the Flask server, and you will need to obtain an API key to use for authentication.
The default base url that you can set is  - `https://db.ghostai.me/` you will need to contact `cyberzendev@gmail.com` if you want to use the api key

### Importing the Library

To use Ghostbase, simply import it into your Python script:

```python
import ghostbase
```

## Setting the Base URL and API Key

Before making any requests, you will need to set the `base_url` and `apikey` variables:

```python
ghostbase.url = "your_flask_server_url" # Or you can use https://db.ghostai.me/
ghostbase.apikey = "your_api_key_here" # You can get this by writing an email to cyberzendev@gmail.com
```

## Functions

### Creates a new database with the given name

```python
ghostbase.create_database(db_name)
```

### Validates a user's credentials and returns a success message if they are valid

```python
ghostbase.validate_user(db_name, username, password)
```

### Adds a new user to the database

```python
ghostbase.add_user(db_name, username, email, password, pro_status)
```

### Deletes a user from the database

```python
ghostbase.delete_user(db_name, username)
```

### Edits a user's pro status

```python
ghostbase.edit_user_pro_status(db_name, username, pro_status)
```

### Returns a user's pro status as a boolean value (True or False)

```python
ghostbase.return_pro_status(db_name, username)
```
