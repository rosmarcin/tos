The Term Of Service api allow users to sign the agreement for the selected version of Terms of Services.
The API provides two endpoints with CRUD methods:

- /tos for Terms of Service content (a versioned dictionary of Terms). Once created ToS can not be modified - new version need to be created
- /user_Tos for User signed versions of Terms of Service. 
    > method GET for listing or details of signed terms
    
    > method POST for authenticated users allows creating or modyfing record - in each case this is equivalent of an agreement. 
        the the time of modification/creation of record is stored automatically
        request includes also first, last name, stree, and postal code that are included in the agreement
    
    > action sign (GET with attribute format=html) for authenticated users renders the agreement to HTML with pre-populated user data
    

If any of the user data changes there should be no changes to the agreement.
If the agreement template changes, the agreements already signed should remain unchanged.
There should be an API to fetch the agreement for a user (html)


Assumptions
- Terms of Service need to be protected from changes using permissions on the application level,
and additionally logging changes made by authorized users. 
So, I am adding just simple constraint on the model level (e.g. overrinding save method)