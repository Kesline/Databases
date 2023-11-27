### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is an open-source relational database management system (RDBMS) known for its extensibility and standards compliance. It supports SQL queries and is ACID-compliant, making it suitable for a wide range of applications.

- What is the difference between SQL and PostgreSQL?
SQL (Structured Query Language) is a standard language for managing relational databases, while PostgreSQL is a specific relational database management system that supports SQL. PostgreSQL extends SQL and adds additional features, functions, and capabilities beyond the standard SQL specifications.

- In `psql`, how do you connect to a database?
using the code:
\c database_name

- What is the difference between `HAVING` and `WHERE`?
The WHERE clause is used in SQL to filter rows before they are grouped and aggregated. The HAVING clause, on the other hand, is used with the GROUP BY clause to filter the results of aggregate functions after grouping.

- What is the difference between an `INNER` and `OUTER` join?
An INNER JOIN retrieves rows where there is a match in both tables being joined. An OUTER JOIN retrieves all rows from one table and the matched rows from another table. Rows without matches in the second table contain NULL values.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
In a 'LEFT OUTER JOIN', all rows from the left table and matched rows from the right table are retrieved. In a 'RIGHT OUTER JOIN', all rows from the right table and matched rows from the left table are retrieved. Rows without matches in the other table contain NULL values.

- What is an ORM? What do they do?
An ORM (Object-Relational Mapping) is a programming technique that converts data between incompatible type systems in object-oriented programming languages. It maps database tables to classes and objects in the application, allowing developers to interact with the database using a higher-level, object-oriented syntax.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  AJAX (Asynchronous JavaScript and XML) is used for making asynchronous requests from the client-side, typically in a web browser. The requests library, on the server side, is used for making synchronous HTTP requests. AJAX requests are initiated from within a web page, while requests are made by the server.

- What is CSRF? What is the purpose of the CSRF token?
CSRF (Cross-Site Request Forgery) is a type of attack where a malicious website tricks a user's browser into making an unintended request to a different site where the user is authenticated. A CSRF token is a security measure added to forms to verify that the form submission is intentional and originated from the same site, preventing CSRF attacks.

- What is the purpose of `form.hidden_tag()`?
In Flask, form.hidden_tag() generates a hidden input field within a WTForms form. This hidden field includes a CSRF token, which enhances security by protecting against CSRF attacks. The token is used to validate that the form submission originated from the same site.
