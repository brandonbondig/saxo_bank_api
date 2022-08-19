
# Saxo Bank Token Retriever

Script to retrieve and store the `access_token` and `refresh_token` to use for Saxo Banks Api.
 
## Step-By-Step Guide
Using Microsofts [playwright](https://playwright.dev/) to interact with the activation and token endpoint from Saxo Bank. Then using `ExpressJs` to setup a callback api to grab the `access_token`. The `access_token` and `refresh_token` are both stored in the `token.json`. This is all handled by `get_token.py`

1. Clone this repository

2. Install [Node.js](https://nodejs.org/en/)

3. Run `pip install -r requirements.txt`

4. Run `playwright install`

5. cd into `.\callback` and run `npm install express`

6. Fill out `.\userInfo.json`

7. Run `npm run start` in `.\callback`

8. Run `get_token.py`

9. Enjoy, you can now use the `access_token` stored in `token.json`, the python script will refresh the token by itself.




    
## Contributing

Contributions are always welcome!

If you have any issues or questions, please contact me with provided information.

