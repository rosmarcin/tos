# Project Title

The Term Of Service api allow users to sign the agreement for the selected version of Terms of Services.
The API provides two endpoints with CRUD methods:

- /tos for Terms of Service content (a versioned dictionary of Terms). Once created ToS can not be modified - new version need to be created
- /user_Tos for User signed versions of Terms of Service. 
    - method GET for listing or details of signed terms
    
    - method POST for authenticated users allows creating or modyfing record - in each case this is equivalent of an agreement. 
        the the time of modification/creation of record is stored automatically
        request includes also first, last name, stree, and postal code that are included in the agreement
    
    - action get_agreement (GET with attribute format=html) for authenticated users renders the agreement to HTML with pre-populated user data
    - action get_agreement (POST) creates new UserTerms record - this is equivalent to agreement of the authenticated user to the Terms of Service


### Installing


Running Docker Image

```

```

Installing as a Django application

```
pip install -r requirements.txt
..

```


## Authors

* **Marcin Ros** - *Initial work* - [PurpleBooth](https://github.com/rosmarcin)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

    


