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
http://127.0.0.1:8000/friends/friend/add_friend/
http://127.0.0.1:8000/friends/friend/accept_request/
http://127.0.0.1:8000/friends/friend/remove_friend/
```

### To view sent/pending and rejected requests
```commandline
http://127.0.0.1:8000/friends/friend/requests/
http://127.0.0.1:8000/friends/friend/sent_requests/
http://127.0.0.1:8000/friends/friend/rejected_requests/
```

### T0 Signup / SignIn / SignOut
```commandline
http://127.0.0.1:8000/register/
http://127.0.0.1:8000/login/
http://127.0.0.1:8000/logout/
```

### To list all accepted friends/friend list
```commandline
http://127.0.0.1:8000/friends/friend/
```

### Search
```commandline
http://127.0.0.1:8000/friends/search/
```