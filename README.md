# leaderboard
Leaderboard style app for gamification of interactions with results from analytics reporting

Installation
---
* Install python:


* Install pip:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py
```

* Install virtualenv:
```
sudo pip install -U virtualenv
```

* Create new Python virtual environment called venv and activate it
```
$ virtualenv venv
$ source venv/bin/activate
```

* Clone this repository
```
$ git clone https://github.com/mboyanna/leaderboard.git
```

Try example 
-----

* Start service
```
$ cd leaderboard
$ python ws.py
[06/Dec/2018:14:12:38] ENGINE Listening for SIGHUP.
[06/Dec/2018:14:12:38] ENGINE Listening for SIGTERM.
[06/Dec/2018:14:12:38] ENGINE Listening for SIGUSR1.
[06/Dec/2018:14:12:38] ENGINE Bus STARTING
CherryPy Checker:
The Application mounted at '' has an empty config.

[06/Dec/2018:14:12:38] ENGINE Started monitor thread 'Autoreloader'.
[06/Dec/2018:14:12:38] ENGINE Serving on http://0.0.0.0:8080
[06/Dec/2018:14:12:38] ENGINE Bus STARTED

```

* Validate service
In a different prompt try with curl
```
>> curl -d '{"metricType": "brand", "metricName": "ctr","triggeringCriteria": ">", "baselineMetricVal": "DKNY", "triggeringMetricVal": "Young Fabulous and Broke"}' -H "Content-Type: application/json" -X POST http://localhost:8080/getLeaderboard
"{\"num1\":{\"mean\":2.0,\"min\":1.0,\"max\":3.0},\"num2\":{\"mean\":5.0,\"min\":4.0,\"max\":6.0}}"
   

```

