## OWASP
Everything about: [Broken Access Control](https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control)

## Real-world Scenario
Another example is an application that allows a user to register a new account.
If the account registration functionality is designed poorly, a user may perform privilege escalation when registering.
Consider the POST request when registering a new user, which submits the data username=bjones&password=Welcome1&email=bjones@inlanefreight.local&roleid=3.
What if we can manipulate the roleid parameter and change it to 0 or 1. We have seen real-world applications where this was the case, and it was possible to quickly register an admin user and access many unintended features of the web application.