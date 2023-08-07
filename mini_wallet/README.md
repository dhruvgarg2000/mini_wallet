# mini_wallet

Problem Statement

Create wallet services for a wallet feature. For authentication to this wallet service, pass it as a header called Authorization with the content in the format of Token <my token>.


Solution

Create user account to access the services of wallet
Enable/Disable the wallet
Add/Withdraw the amount from the wallet


Steps to Setup

1. Clone the project from github
    git clone https://github.com/dhruvgarg2000/mini_wallet.git

2. Create a virtual environment
    virtualenv venv

3. Activate the virtual environment and install the requirements
    pip install -r requirements.txt

4. Run Migrations
    python manage.py migrate

5. Start the server and hit the APIs
    python manage.py runserver <port>