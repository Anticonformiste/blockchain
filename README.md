# BlockChain
A simple implementation of a Blockchain using Python, inspired by the work of [Daniel van Flymen](https://github.com/dvf/blockchain).

## Requirements :
* Python 3.6
* Django 2.0.6 
* Requests (install it via pip or pipenv)
* A text editor of your choice, the project is built using [PyCharm](https://www.jetbrains.com/pycharm/) by *JetBrains* ♥

## Content:
* A single application **chaining**, which contains :
  * the *blockchain.py* file within the *utils* package. It's the core of the implementation.
  * the *middleware.py* file which serves to disable CSRF validation while sending POST requests.
  * the *views.py* the controllers that consume the blockchain.py services.
  * the *urls.py* the routes of our app; linked to their controllers.
    * '/chain/': "get the full chain".
    * '/mine/': "mine a block".
    * '/transactions/new/': "add a new transaction to the block".
    * '/nodes/register/': "register a new node".
    * '/nodes/resolve/': "consensus(check chain's consistency)".

## Explanations :
* Please refer to Daniel's [article](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46) on Hackernoon. It has a clear explanation
for each piece of code. If there are some problems in the project setup please mention them.
* For testing, use two machines and run the server on 0.0.0.0 or you can test it locally by running the server on two different ports .
For example : 127.0.0.1:8000 & 127.0.0.1:8001.
* Run tests using [Postman](https://www.getpostman.com/) or [CURL](https://curl.haxx.se/).

# Good luck 
> ^-^ AC97 :heart:.
