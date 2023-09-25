## OWASP
Insecure Direct Object Reference Prevention Cheat Sheet: [Insecure Direct Object Referencing (IDOR)](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)

## Real-world Scenario
When combined with a flaw such as broken access control, this can often be used to access another user's files or functionality.
An example would be editing your user profile browsing to a page such as /user/701/edit-profile.
If we can change the 701 to 702, we may edit another user's profile!