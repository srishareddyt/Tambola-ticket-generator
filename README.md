TAMBOLA TICKET GENERATOR PROJECT REPORT

OVERVIEW:

This project develops a web application that generates unique Tambola tickets, stores them in a database, and retrieves them for viewing. It adheres to the specific rules of Tambola ticket generation.

TECHNOLOGIES USED:

● Python: Primary programming language.
● FastAPI: Web framework for building APIs.
● Peewee: Object-relational mapper (ORM) for database interactions.
● PostgreSQL: Database for storing generated tickets.

APIS WRITTEN:

● POST /generate_tickets: Generates specified number of ticket sets and returns them as JSON with key as its ID in Database.
● GET /get_tickets: Retrieves paginated ticket sets with pagination information.

FILE STRUCTURE:

● create_tambola_ticket.py: Core logic for generating Tambola tickets.
● database.py: Database connection setup.
● helpers.py: Helper functions for generating Tambola tickets.
● main.py: FastAPI application entry point and routing.
● tambola_ticket.py: Database model for Tambola tickets.
● get_all_tambola_tickets.py: Function for retrieving paginated tickets from the database.

TAMBOLA TICKET GENERATION RULES:

● The numbers 1 to 90 are used once only.
● In the first column are the numbers 1 to 9, the second column has numbers 10 to
19, etc, all the way to the 9th column which has numbers 80 to 90 in it.
● Every row must have exactly 5 numbers in it.
● In a specific column, numbers must be arranged in ascending order from top to
bottom.
● Each column must have at least 1 number.
● All the numbers 1 to 90 are used only once in each set of 6 tickets.
● Blank Cell fill by zero.
● Each ticket must be unique and not exist in the database.

Working of API's Screen Recording: https://drive.google.com/file/d/1KtvVTbOQNsSS04gOGRNce2G06MtW6CF-/view?usp=sharing