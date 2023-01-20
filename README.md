# Basic_Brute
Basic Brute is a tool to do brute force in Basic Auth HTTP 

## How to install

```
git clone https://github.com/0xGabe/Basic_Brute
```

## How to use

Basic brute is simple to use, you only need to pass the URL target, one possible user, and one wordlist with passwords. The description below shows the syntax:

```
python3 basic_brute.py http://localhost admin list.txt
```
### Testing the tool

Postman provide a valid URL with basic auth authentication, the URL and credentials is:

```
URL: https://postman-echo.com/basic-auth
User: postman
Pass: password
```

Create a list.txt with random values and the correct password, after this run the command below:

```
python3 basic_brute.py https://postman-echo.com/basic-auth postman list.txt
```
