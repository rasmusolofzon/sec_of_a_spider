# Lab, Advanced Web Security

# Preparatory assignments

## Preparatory assignment 1
If one enters something like `user" or 1=2` in the username field, an error message is given.
This makes the SQL query FALSE.
What one could accomplish with this could possibly be to:
* dump list of users (username field: `" OR 1=1 --`)
* login without giving password (u: `[USERNAME] --` or same u, p: `" or 1=1`)
* drop database tables or executing other arbitrary queries (`[WHATEVER] ; DROP TABLE Users`)

## Preparatory assignment 2
The code forms a SQL query with an input `username`. 
The query retrieves the password from the database for the user w/ username `username`.
The retrieved password is compared with the `old` password entered by the user.
If the passwords do not match, "Incorrect password" is echo'ed and the script is exited.
If they do match, a new SQL query is formed that updates the password entry in the database
for the user w/ username `username` with the new password given by the user,
and echoes "Password changed successfully".
With both SQL queries, they are checked to see if they are valid,
otherwise it is echo'ed that the "query: [echo query verbatim] failed".

* "The `die()` function prints a message and exits the current script"

---

## Preparatory assignment 3
* Basics of XSS attacks, especially persistent XSS attacks
* Write two javascripts
	* test for XSS vulnerabilities
	<?php passthru('ls'); ?> ..but JavaScript..
	* steal a user's cookie


## Preparatory assignment 4
* Get knowledge about FireBug, especially how to edit cookies w/ it

## Preparatory assignment 5
* Read up on ModSecurity

---

# Problems

## Problem 1
* Vulnerability scanning
(Based on a user with u: `user` and p: `pass` is registered.)
	* Login: If one enters something like `user" or 1=2` in the username field, 
	an error message is given. This makes the SQL query FALSE.

	* Login: Entering `" or 1=1` in both username and password field, an error is given. 
	Here also ` LIMIT 1` is appended to the query.
	
	* Login: Entering `1" or "1"="1` in both u and p fields, login page says:
	"Something went wrong with your authentication attempt"

* Attack vectors
	* Firstly, we see that the query uses quotes: "

## Problem 2
## Problem 3

---

## Problem 4
## Problem 5
* Abilities of admin account vs normal account

## Problem 6
## Problem 7
## Problem 8
## Problem 9
## Problem 10
## Problem 11
## Problem 12
## Problem 13
## Problem 14
## Problem 15
## Problem 16
## Problem 17
