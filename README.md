# TinkLink connect

This is a python example that demonstrates how to connect to Tink API to fetch users' account and transaction data.

## Installation

The application requires a Tink API developer account.

### Prerequisites

1. Create your developer account at [Tink Console](https://console.tink.com)
2. Follow the [getting started guide](https://docs.tink.com/resources/getting-started/set-up-your-account) to retrieve your `client_id` and `client_secret`
3. Register the redirect URI for the example app (`http://localhost:3000/callback`) in the [list of redirect URIs under your app's settings](https://console.tink.com/overview)

For example:

Using a Test Provider `se-test-bankid-successful`

Replace <YOUR_CLIENT_ID> first and then run:

https://link.tink.com/1.0/authorize/credentials/se-test-bankid-successful?client_id=<YOUR_CLIENT_ID>&redirect_uri=http://localhost:3000/callback&scope=accounts:read,investments:read,transactions:read,user:read&market=SE&locale=en_US&test=true

Social Security Number: `180012121212`

On a successful authentication, your browser should redirect you to the `redirect_uri` you specified in your Tink Link URL. It should contain an authorization `code`, and your browser URL window will contain a URL similar to: `{redirect_uri}/?code={YOUR_USER_AUTHORIZATION_CODE}`


## Option 1: Running with Docker and docker-compose

Prerequisites:
- Docker & docker-compose installed

1. Run it:

```
$ CLIENT_ID=<YOUR_CLIENT_ID> CLIENT_SECRET=<YOUR_CLIENT_SECRET> CODE=<YOUR_USER_AUTHORIZATION_CODE> docker-compose up --build
```

## Option 2: Running the app locally

Prerequisites:
- Python >= 3.7 installed
- pip installed

1. Install the dependencies.

```
$ make init
```

2. Set your client identifier, client secret and authorization code into the following environment variables

```
$ export CLIENT_ID="<YOUR_CLIENT_ID>"
$ export CLIENT_SECRET="<YOUR_CLIENT_SECRET>"
$ export CODE="<YOUR_AUTHORIZATION_CODE>
```

3. Run the code:

```
$ make run
```


You will see two reports:

Showing last 10 transactions
![Alt text](img/task1.png?raw=true "Showing last 10 transactions")

Showing unique transactions in the last 3 months
![Alt text](img/task2.png?raw=true "Showing unique transactions in the last 3 months")


# Considerations and next steps:

- There's a BUG in https://docs.tink.com/api#search-query-transactions. The method should be `GET` rather than `POST`.

- As discussed with the team, it's not yet possible to obtain the `USER_AUTHORIZATION_CODE` through the API for non Enterprise users so it would be great as a "next step" to automate it. Perhaps by just using a headless browser-based solution (e.g: Selenium, activesoup).

- As `USER_AUTHORIZATION_CODE` can't be automated yet, it has to be regenerated every time this solution is executed (see Prerequisites section)