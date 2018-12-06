
<p align="left">
  <img src="https://images.unsplash.com/photo-1508901532037-43b386822c81?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2549&q=80" width="300" height="200" title="hover text">
   Photo by Alexandra Andersson on Unsplash
</p>

# leaderboard
Leaderboard style app for gamification of interactions with results from analytics reporting

Installation
---
* If you dont have it, install python:
```
$ brew install python
```

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
$ curl -d '{"metricType": "brand", "metricName": "ctr","triggeringCriteria": ">", "baselineMetricVal": "DKNY", "triggeringMetricVal": "Young Fabulous and Broke"}' -H "Content-Type: application/json" -X POST http://localhost:8080/getLeaderboard
```
You should get the following response:
```
"{\n  \"metricType\": \"brand\",\n  \"metricName\": \"ctr\",\n  \"triggeringCriteria\": \">\",\n  \"baselineMetricVal\": \"DKNY\",\n  \"triggeringMetricVal\": \"Young Fabulous and Broke\",\n  \"triggeringTreshold\": 10,\n  \"otherMetrics\": [\n    \"ctr\",\n    \"aov\",\n    \"sales\",\n    \"attr_sales\",\n    \"items\"\n  ],\n  \"recSets\": [\n    {\n      \"value\": \"0.85\",\n      \"leaderName\": \"Adam Nielsen\"\n    },\n    {\n      \"value\": \"0.08\",\n      \"leaderName\": \"Stacy Jackson\"\n    },\n    {\n      \"value\": \"0.06\",\n      \"leaderName\": \"Trisha Firm\"\n    },\n    {\n      \"value\": \"0.06\",\n      \"leaderName\": \"Merchandiser Alan\"\n    },\n    {\n      \"value\": \"0.03\",\n      \"leaderName\": \"Marketeer Hanna\"\n    },\n    {\n      \"value\": \"0.02\",\n      \"leaderName\": \"CoffeeGuy\"\n    },\n    {\n      \"value\": \"0.02\",\n      \"leaderName\": \"Jeff Bezos\"\n    }\n  ]\n}"
"{\"num1\":{\"mean\":2.0,\"min\":1.0,\"max\":3.0},\"num2\":{\"mean\":5.0,\"min\":4.0,\"max\":6.0}}"
```
   


