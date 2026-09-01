# Task 02 — JSON User Processor

## Context

In this task you will build a small command-line application that reads user data from a JSON file, validates it, processes it and produces a summary.

The goal of this task is not only to practice Python syntax.

You are expected to understand the full data flow:

```text
file on disk
    ↓
JSON
    ↓
Python data structures
    ↓
validation
    ↓
Python objects
    ↓
processing
    ↓
JSON output
```

You are free to search for information, read documentation and use external resources.

However, you must be able to explain every meaningful part of your solution during the review.

---

## Repository location

Task description:

```text
tasks/02-json-user-processor/TASK.md
```

Your solution must be placed in:

```text
solutions/02-json-user-processor/
```

The solution must follow all repository rules described in the root `README.md`.

---

# Requirements

Implement a command-line Python application that processes a JSON file containing users.

The application must:

1. Read user data from a JSON file.
2. Validate the input structure.
3. Validate individual users.
4. Convert valid users into Python objects.
5. Skip invalid users without stopping the whole program.
6. Calculate statistics for valid users.
7. Support basic filtering and lookup.
8. Export valid users back to JSON.
9. Produce understandable errors for invalid input.

Use only the Python standard library for the initial implementation.

Do not use validation frameworks such as:

* Pydantic
* Marshmallow
* Pandas

---

# Input data

Create the following file inside your solution directory:

```text
users.json
```

Use this data:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alex",
      "birth_date": "2000-05-10",
      "email": "alex@example.com",
      "active": true
    },
    {
      "id": 2,
      "name": "Maria",
      "birth_date": "1996-11-21",
      "email": "maria@example.com",
      "active": true
    },
    {
      "id": 3,
      "name": "John",
      "birth_date": "1988-02-13",
      "email": "john@example.com",
      "active": false
    },
    {
      "id": 4,
      "name": "Kate",
      "birth_date": "2003-08-02",
      "email": "kate@example.com",
      "active": true
    },
    {
      "id": 5,
      "name": "Michael",
      "birth_date": "1992-04-17",
      "email": "michael@example.com",
      "active": false
    }
  ]
}
```

---

# User model

Every user contains the following fields:

```text
id
name
birth_date
email
active
```

You must represent a valid user using a Python class.

You may use a regular class or a `dataclass`.

After parsing and validation, valid users should no longer be represented only as raw dictionaries.

---

## Validation rules

### `id`

Must:

* be an integer;
* be greater than zero;
* be unique across all users in the input file.

Note that in Python:

```python
isinstance(True, int)
```

returns `True`.

Your validation should still treat boolean values as invalid user IDs.

---

### `name`

Must:

* be a string;
* not be empty;
* contain at least one non-whitespace character.

For example, this value is invalid:

```json
{
  "name": "   "
}
```

---

### `birth_date`

Must:

* be a string;
* use the format `YYYY-MM-DD`;
* represent a real calendar date.

For example:

```text
2000-05-10
```

is valid.

This is not:

```text
2000-15-90
```

---

### `email`

Must:

* be a string;
* not be empty;
* contain the `@` character.

A full RFC-compliant email validator is not required.

---

### `active`

Must be a boolean value.

Valid:

```json
true
```

```json
false
```

Invalid examples:

```json
"true"
```

```json
1
```

```json
"yes"
```

---

# Running the application

The program should support the following basic command:

```bash
python main.py users.json
```

The exact internal implementation is up to you.

You may use `argparse` or another solution from the Python standard library.

---

# Statistics

After processing the file, print statistics for valid users.

The output must include:

* total number of valid users;
* number of active users;
* number of inactive users;
* youngest user;
* oldest user;
* average age.

Example:

```text
Valid users: 5
Active users: 3
Inactive users: 2
Youngest user: Kate
Oldest user: John
Average age: 30.4
```

The exact formatting may differ.

Average age should be rounded to one decimal place.

Age must be calculated relative to the current date.

---

# User lookup

Add support for finding a user by ID.

Example:

```bash
python main.py users.json --user-id 3
```

Example output:

```text
ID: 3
Name: John
Birth date: 1988-02-13
Email: john@example.com
Active: False
```

If the user does not exist, return a clear message such as:

```text
User with id 100 not found
```

The program should not crash.

---

# Active users filter

Add support for displaying only active users.

Example:

```bash
python main.py users.json --active
```

Possible output:

```text
1 Alex
2 Maria
4 Kate
```

---

# Export

Add support for exporting valid users into another JSON file.

Example:

```bash
python main.py users.json --output valid_users.json
```

The resulting file should have the same general structure as the original input:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alex",
      "birth_date": "2000-05-10",
      "email": "alex@example.com",
      "active": true
    }
  ]
}
```

Your Python user objects cannot be written directly using `json.dump()`.

You are expected to determine how to convert them into JSON-compatible values.

---

# Invalid users

The application must not terminate when one individual user contains invalid data.

Instead:

1. detect validation errors;
2. skip the invalid user;
3. continue processing the remaining users;
4. include the error in the final report.

A user may contain more than one error.

Try to report all detected validation errors for that user instead of stopping after the first one.

Example:

```text
Processing finished

Valid users: 3
Invalid users: 2

Errors:

User at index 2:
- active is required

User at index 4:
- invalid birth_date
- invalid email
```

---

# Invalid dataset

After the basic version works, test your implementation using the following file.

Create:

```text
users_invalid.json
```

with the following content:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alex",
      "birth_date": "2000-05-10",
      "email": "alex@example.com",
      "active": true
    },
    {
      "id": 2,
      "name": "Maria",
      "birth_date": "1996-11-21",
      "email": "maria@example.com"
    },
    {
      "id": "3",
      "name": "John",
      "birth_date": "1988-02-13",
      "email": "john@example.com",
      "active": true
    },
    {
      "id": 4,
      "name": null,
      "birth_date": "2003-08-02",
      "email": "kate@example.com",
      "active": true
    },
    {
      "id": 5,
      "name": "Michael",
      "birth_date": "1992-15-90",
      "email": "michael@example.com",
      "active": false
    },
    {
      "id": 6,
      "name": "",
      "birth_date": "2001-01-01",
      "email": "test@example.com",
      "active": true
    },
    {
      "id": 7,
      "name": "Anna",
      "birth_date": "1999-06-15",
      "email": "anna.example.com",
      "active": true
    },
    {
      "id": 8,
      "name": "Peter",
      "birth_date": "1990-12-20",
      "email": "peter@example.com",
      "active": "yes"
    },
    {
      "id": 1,
      "name": "Duplicate Alex",
      "birth_date": "2002-03-03",
      "email": "duplicate@example.com",
      "active": true
    }
  ]
}
```

Your application is expected to detect at least the following problems:

* missing `active`;
* invalid `id` type;
* `name` is `null`;
* invalid calendar date;
* empty `name`;
* invalid email;
* invalid `active` type;
* duplicate `id`.

---

# Invalid file structure

Your program must also handle errors on the file level.

## File does not exist

Example:

```bash
python main.py missing.json
```

The program must provide an understandable error.

It should not expose an unhandled traceback to the user.

---

## Invalid JSON syntax

Create:

```text
broken.json
```

with:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alex",
      "birth_date": "2000-05-10",
      "email": "alex@example.com",
      "active": true
    },
    {
      "id": 2,
      "name": "Maria"
      "birth_date": "1996-11-21",
      "email": "maria@example.com",
      "active": true
    }
  ]
}
```

The file intentionally contains invalid JSON.

The program should produce an understandable error.

Bonus: include the line and column where parsing failed.

---

## Wrong root type

Your program should handle input such as:

```json
[
  {
    "id": 1,
    "name": "Alex"
  }
]
```

The expected root structure is an object containing a `users` field.

---

## Missing `users`

Example:

```json
{
  "data": []
}
```

This should produce a clear error.

---

## Invalid `users` value

Example:

```json
{
  "users": "Alex"
}
```

The `users` field must contain a list.

---

# Unknown fields

Test the program with:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alex",
      "birth_date": "2000-05-10",
      "email": "alex@example.com",
      "active": true,
      "favorite_color": "blue"
    },
    {
      "id": 2,
      "name": "Maria",
      "birth_date": "1996-11-21",
      "email": "maria@example.com",
      "active": true,
      "role": "admin",
      "salary": 5000
    }
  ]
}
```

There is intentionally no predefined requirement for unknown fields.

Decide how your program should handle them.

Possible approaches include:

* ignore them;
* reject the user;
* preserve them separately.

Document your decision in the solution README and be ready to explain why you chose it.

---

# Nested data

After the previous requirements are completed, extend the user format with an address.

Example:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alex",
      "birth_date": "2000-05-10",
      "email": "alex@example.com",
      "active": true,
      "address": {
        "country": "Spain",
        "city": "Madrid",
        "postal_code": "28001"
      }
    },
    {
      "id": 2,
      "name": "Maria",
      "birth_date": "1996-11-21",
      "email": "maria@example.com",
      "active": true,
      "address": {
        "country": "Germany",
        "city": "Berlin",
        "postal_code": "10115"
      }
    },
    {
      "id": 3,
      "name": "John",
      "birth_date": "1988-02-13",
      "email": "john@example.com",
      "active": false,
      "address": null
    }
  ]
}
```

Create an `Address` Python class.

A `User` should contain either:

```python
Address
```

or:

```python
None
```

for its address.

After conversion to the domain model, do not keep the address as an unprocessed nested dictionary inside the `User` object.

---

# User tags

Extend the model with:

```text
tags
```

Example:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alex",
      "birth_date": "2000-05-10",
      "email": "alex@example.com",
      "active": true,
      "tags": [
        "python",
        "backend",
        "student"
      ]
    },
    {
      "id": 2,
      "name": "Maria",
      "birth_date": "1996-11-21",
      "email": "maria@example.com",
      "active": true,
      "tags": [
        "backend",
        "sql"
      ]
    },
    {
      "id": 3,
      "name": "John",
      "birth_date": "1988-02-13",
      "email": "john@example.com",
      "active": false,
      "tags": []
    }
  ]
}
```

Add the following statistics:

```text
Most popular tag: backend
```

and:

```text
Users without tags: 1
```

Consider what should happen if several tags have the same maximum frequency.

Document the chosen behavior.

---

# Large input

Assume that instead of 5 users the input file contains:

```text
5,000,000 users
```

and is several gigabytes in size.

You do not have to fully solve this problem in the initial implementation.

Add a section to the solution README answering the following questions:

1. What happens when `json.load()` reads such a file?
2. Why can this become a problem?
3. What resource will most likely become the limiting factor?
4. Can JSON data be processed without loading the whole dataset into memory?
5. Would the current JSON structure make streaming easy or difficult?

As an additional exercise, write a script that generates a JSON dataset containing at least:

```text
100,000 users
```

Run your program against it and note:

* approximate execution time;
* approximate memory behavior;
* anything unexpected you observe.

Exact benchmarking is not required.

---

# Solution README

Your solution directory must contain its own:

```text
README.md
```

It MAY be written in RUSSIAN
It must describe at least:

* supported Python version;
* how to install/run the project;
* how to run the application;
* expected input format;
* validation rules;
* error-handling behavior;
* your decision regarding unknown fields;
* important implementation decisions;
* known limitations.

Do not describe only *what* the code does.

For non-obvious decisions, explain *why* you chose that approach.

---

# Project structure

You are free to design the internal project structure.

Do not put the whole application into one large function or one large file.

The following is only an example:

```text
solutions/02-json-user-processor/
├── README.md
├── requirements.txt
├── main.py
├── models.py
├── validation.py
└── ...
```

You do not have to follow this exact structure.

Choose a structure you can explain.

---

# Dependencies

This solution does not require external runtime dependencies.

However, according to repository rules, the solution must contain its own dependency configuration.

You may provide either:

```text
requirements.txt
```

or:

```text
pyproject.toml
```

If there are no external dependencies, an empty `requirements.txt` is acceptable.

Development dependencies may be added if you decide to use them.

---

# Git workflow

Do not implement this task directly on `main`.

Follow the repository workflow.

Create a separate branch.

A reasonable branch name could be:

```text
task/02-json-user-processor
```

Commit your changes and push the branch.

Create a Pull Request when the task is ready for review.

Your Pull Request description must explain:

* what was implemented;
* how the solution is structured;
* how to run it;
* important implementation decisions;
* anything that is incomplete or uncertain.

Do not write a PR description that only says:

```text
Done task 01
```

---

# Definition of Done

The task is considered ready for review when:

* the application can process the valid dataset;
* invalid users do not crash the whole application;
* input-level errors are handled;
* valid users are represented using Python objects;
* required statistics are calculated;
* lookup by user ID works;
* active-user filtering works;
* JSON export works;
* nested data is supported;
* error reporting is understandable;
* the solution has its own README;
* the solution has its own dependency configuration;
* the implementation is committed to a separate branch;
* a Pull Request has been created;
* the PR contains a meaningful description.

---

# Review expectations

During the review, you may be asked to explain:

* what JSON actually is;
* the difference between JSON and a Python dictionary;
* what `json.load()` returns;
* when JSON becomes a Python object;
* why a separate `User` class exists;
* how validation is organized;
* which exceptions may happen while reading the input;
* how invalid users are handled;
* how duplicate IDs are detected;
* how dates are parsed;
* how Python objects are converted back to JSON;
* what would happen with a multi-gigabyte input file;
* why you chose the current project structure.

---
