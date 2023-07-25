# Django rest framework - Login, signup, friend model

## Installation steps
```commandline
pip install -r requirements.txt
```

## Run
```commandline
python manage.py runserver
```


## Api's

### To send/accept/reject friend requests
```commandline
http://127.0.0.1:8000/friends/friend/add_friend/-H'Authorization:Token 158aba1cb35cced19092c5b2e0d909502c'
http://127.0.0.1:8000/friends/friend/accept_request/-H'Authorization:Token 158aba1cb35cced19092c5b2e0d909502c'
http://127.0.0.1:8000/friends/friend/remove_friend/-H'Authorization:Token 158aba1cb35cced19092c5b2e0d909502c'
```

### To view sent/pending and rejected requests
```commandline
http://127.0.0.1:8000/friends/friend/requests/-H'Authorization:Token 158aba1cb35cced19092c5b2e0d909502c'
http://127.0.0.1:8000/friends/friend/sent_requests/-H'Authorization:Token 158aba1cb35cced19092c5b2e0d909502c'
http://127.0.0.1:8000/friends/friend/rejected_requests/-H'Authorization:Token 158aba1cb35cced19092c5b2e0d909502c'
```

### T0 Signup / SignIn / SignOut
```commandline
http://127.0.0.1:8000/register/
http://127.0.0.1:8000/login/
http://127.0.0.1:8000/logout/
```

### To list all accepted friends/friend list
```commandline
http://127.0.0.1:8000/friends/friend/-H'Authorization:Token 158aba1cb35cced19092c5b2e0d90950'
```

### Search
```commandline
http://127.0.0.1:8000/friends/search/
```