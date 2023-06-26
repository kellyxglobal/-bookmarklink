# Link Bookmarking API [Save your links for future reference]
The Link Bookmarking API is a platform that allows users to save links for future reference. It provides a simple and efficient way to manage bookmarks, allowing users to create accounts, log in, and save links securely. The API is built with Python and Flask framework and leverages Postman for testing and Swagger for API documentation.

## Table of Contents
* -Installations
* -Usage

* -API Documentation
* -Authentication
* -Endpoints
    * User Registration
    * User Login
    * Create Bookmark link
    * Edit bookmark link
    * Delete Bookmark link
    * Get Bookmark details
    * Get All Bookmarks
    * Link Shortening
    * Number of visits per user
    * Meta Data for Bookmarks and Pages
* -Contributing
* -Licensing

### Installation
1. Clone the repository:
git clone https://github.com/kellyxglobal/bookmarklink.git

2. Navigate to the project directory:
cd bookmarklink

3. Install the required dependencies: pip install -r requirements.txt

4. Set up the environment variables:
-Create a .env file in the root directory of the project and define the following variables:
**export FLASK_ENV=development**
**export FLASK_APP=src**
**export SQLALCHEMY_DATABASE_URI=sqlite:///bookmarks.db**
**export JWT_SECRET_KEY='JWT_SECRET_KEY'**

### Run the API:
python -m flask run --port=8000
The API should now be running locally on http://localhost:5000.

### Usage
Before using the API, make sure it is running locally by following the installation instructions.

To interact with the API, you can use tools like Postman or cURL.

### API Documentation
The API is documented using Swagger. To access the API documentation, open your browser and navigate to http://localhost:5000/api/docs. This will provide a detailed overview of the available endpoints, request/response formats, and example requests.

### Authentication
The Link Bookmarking API uses token-based authentication to protect certain endpoints. To access protected endpoints, you need to obtain an access token.

To authenticate, send a POST request to the /auth/login endpoint with your credentials (username and password). The response will include an access token, which should be included in the Authorization header of subsequent requests:
Authorization: Bearer <access_token>

### Endpoints
The Link Bookmarking API provides the following endpoints:

   **-User Registration**
   *Endpoint:* /auth/register
   *Method:* POST
   Description: Register a new user.
   *Request Body:*
   *username (string):* User's desired username.
   *password (string):* User's desired password.
   *email (string):* User's desired Email
   *Response:*
   *message (string):* Success message.

   **-User Login**
   *Endpoint:* /auth/login
   *Method:* POST
   *Description:* Log in with an existing user account and obtain an access token.
   *Request Body:*
   *Email(string):* User's email
   *password (string):* User's password.
   *Response:*
   *access_token (string):* Access token for authentication.

   **-Create Bookmark**
   *Endpoint: /bookmarks
   *Method: POST
   *Description: Create a new bookmark.
   *Request Body:
   *Description (string): Title of the bookmark.
   *url (string): URL of the bookmark.
   *Response:*
   *id (integer):* Unique identifier of the created bookmark.
   *url (string):* url of the bookmark.
   *short_url (string):* Short URL of the bookmark.
   *visits (string):* Number of visits of the bookmark
   *created_at (string):* Creation timestamp of the bookmark.
   *updated_at (string):* updating timestamp of the bookmark.

   **-Edit Bookmark**
   *Endpoint:* /bookmarks/{bookmark_id}
   *Method:* PUT
   *Description:* Edit a bookmark by its ID.
   *Request Parameters:*
   *bookmark_id (integer):* ID of the bookmark to edit.
   *Request Body:*
   *Description (string):* Updated title of the bookmark.
   *url (string):* Updated URL of the bookmark.
   *Response:*
   *message (string):* Success message.

   **-Delete Bookmark**
   *Endpoint:* /bookmarks/{bookmark_id}
   *Method:* DELETE
   *Description:* Delete a bookmark by its ID.
   *Request Parameters:*
   *bookmark_id (integer):* ID of the bookmark to delete.
   *Response:*
   *message (string):* Success message.

   **Get Bookmark Details**
   *Endpoint:* /bookmarks/{bookmark_id}
   *Method:* GET
   *Description:* Retrieve details of a bookmark by its ID.
   *Request Parameters:*
   *bookmark_id (integer):* ID of the bookmark.
   *Response:*
   *id (integer):* Unique identifier of the bookmark.
   *title (string):* Title of the bookmark.
   *url (string):* URL of the bookmark.
   *created_at (string):* Creation timestamp of the bookmark.
   *updated_at (string):* Updating timestamp of the bookmark.

   **Get All Bookmarks**
   *Endpoint:* /bookmarks
   *Method:* GET
   *Description:* Retrieve all bookmarks.
   *Response:*
   *bookmarks (list):* List of bookmarks.
   *id (integer):* Unique identifier of the bookmark.
   *title (string):* Title of the bookmark.
   *url (string):* URL of the bookmark.
   *created_at (string):* Creation timestamp of the bookmark.

   **Link Shortening**
   *Endpoint:* /shorten
   *Method:* POST
   *Description:* Shorten a given URL.
   *Request Body:*
   *url (string):* URL to be shortened.
   *Response:*
   *original_url (string):* Original URL.
   *shortened_url (string):* Shortened URL.

   **Number of Visits**
   *Endpoint:* http://127.0.0.1:8000/api/v1/bookmarks/
   *Method:* GET
   *Description:* Retrieve the number of bookmark link pages for a bookmark found in the meta data.
   *Request Parameters:*
   *bookmark_id (integer):* ID of the bookmark.
   *Response:*
   *bookmark_id (integer):* ID of the bookmark.
   *visits (integer):* Number of visits for the bookmark.

   **Number of Bookmark Link Pages**
   *Endpoint:* http://127.0.0.1:8000/api/v1/bookmarks/
   *Method:* GET
   *Description:* Retrieve the number of bookmark link pages for a bookmark i the meta data.
   *Request Parameters:*
   *bookmark_id (integer):* ID of the bookmark.
   *Response:*
   *bookmark_id (integer):* ID of the bookmark.
   *pages (integer):* Number of bookmark link pages.

### Contributing
Contributions to the Link Bookmarking API project are welcome. If you find any issues or have suggestions for improvements, please submit an issue or a pull request to the GitHub repository.

### License
The Link Bookmarking API is open-source software released under the [MIT License]
