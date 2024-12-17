"""
Curl command test:
- Get all libs
```curl -X GET http://localhost:5000/libraries/occupancy```

- get lib 1
```curl -X GET http://localhost:5000/libraries/1/occupancy```

- get top 3 most mostFree libs
```curl -X GET http://localhost:5000/libraries/top-available```

- get least occupied library
```curl -X GET http://localhost:5000/libraries/least-occupied```

- get second least occupied library
```curl -X GET http://localhost:5000/libraries/second-least-occupied```

- get third least occupied library
```curl -X GET http://localhost:5000/libraries/third-least-occupied```
"""

from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/libraries/*": {"origins": ["http://custudyseat.local"]}})

libraries = [{
        "id": 1,
        "name": "Avery Library",
        "floors": 3,
        "hours": "9am - 11pm",
        "occupancy": {
            "00:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "01:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "02:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "03:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "04:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "05:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "06:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "07:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "08:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"},
            "09:00": {"status": "Open", "occupancyAvg": "15", "1F": "20", "2F": "10", "3F": "15", "mostFree": "2F"},
            "10:00": {"status": "Open", "occupancyAvg": "35", "1F": "40", "2F": "30", "3F": "35", "mostFree": "2F"},
            "11:00": {"status": "Open", "occupancyAvg": "55", "1F": "60", "2F": "50", "3F": "55", "mostFree": "2F"},
            "12:00": {"status": "Open", "occupancyAvg": "75", "1F": "80", "2F": "70", "3F": "75", "mostFree": "2F"},
            "13:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "80", "3F": "85", "mostFree": "2F"},
            "14:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "85", "3F": "90", "mostFree": "2F"},
            "15:00": {"status": "Open", "occupancyAvg": "95", "1F": "100", "2F": "90", "3F": "95", "mostFree": "2F"},
            "16:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "85", "3F": "90", "mostFree": "2F"},
            "17:00": {"status": "Open", "occupancyAvg": "80", "1F": "85", "2F": "75", "3F": "80", "mostFree": "2F"},
            "18:00": {"status": "Open", "occupancyAvg": "65", "1F": "70", "2F": "60", "3F": "65", "mostFree": "2F"},
            "19:00": {"status": "Open", "occupancyAvg": "75", "1F": "80", "2F": "70", "3F": "75", "mostFree": "2F"},
            "20:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "80", "3F": "85", "mostFree": "2F"},
            "21:00": {"status": "Open", "occupancyAvg": "70", "1F": "75", "2F": "65", "3F": "70", "mostFree": "2F"},
            "22:00": {"status": "Open", "occupancyAvg": "45", "1F": "50", "2F": "40", "3F": "45", "mostFree": "2F"},
            "23:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "mostFree": "Not open"}
        }
    },
    {
        "id": 2,
        "name": "Barnard Library",
        "floors": 6,
        "hours": "9am - 11pm",
        "occupancy": {
            "00:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "01:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "02:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "03:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "04:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "05:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "06:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "07:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "08:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "09:00": {"status": "Open", "occupancyAvg": "25", "1F": "35", "2F": "25", "3F": "20", "4F": "20", "5F": "15", "6F": "35", "mostFree": "5F"},
            "10:00": {"status": "Open", "occupancyAvg": "45", "1F": "55", "2F": "45", "3F": "40", "4F": "40", "5F": "35", "6F": "55", "mostFree": "5F"},
            "11:00": {"status": "Open", "occupancyAvg": "65", "1F": "75", "2F": "65", "3F": "60", "4F": "60", "5F": "55", "6F": "75", "mostFree": "5F"},
            "12:00": {"status": "Open", "occupancyAvg": "85", "1F": "95", "2F": "85", "3F": "80", "4F": "80", "5F": "75", "6F": "95", "mostFree": "5F"},
            "13:00": {"status": "Open", "occupancyAvg": "95", "1F": "100", "2F": "95", "3F": "90", "4F": "90", "5F": "85", "6F": "100", "mostFree": "5F"},
            "14:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "90", "3F": "85", "4F": "85", "5F": "80", "6F": "95", "mostFree": "5F"},
            "15:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "85", "3F": "80", "4F": "80", "5F": "75", "6F": "90", "mostFree": "5F"},
            "16:00": {"status": "Open", "occupancyAvg": "80", "1F": "85", "2F": "80", "3F": "75", "4F": "75", "5F": "70", "6F": "85", "mostFree": "5F"},
            "17:00": {"status": "Open", "occupancyAvg": "70", "1F": "75", "2F": "70", "3F": "65", "4F": "65", "5F": "60", "6F": "75", "mostFree": "5F"},
            "18:00": {"status": "Open", "occupancyAvg": "60", "1F": "65", "2F": "60", "3F": "55", "4F": "55", "5F": "50", "6F": "65", "mostFree": "5F"},
            "19:00": {"status": "Open", "occupancyAvg": "75", "1F": "80", "2F": "75", "3F": "70", "4F": "70", "5F": "65", "6F": "80", "mostFree": "5F"},
            "20:00": {"status": "Open", "occupancyAvg": "65", "1F": "70", "2F": "65", "3F": "60", "4F": "60", "5F": "55", "6F": "70", "mostFree": "5F"},
            "21:00": {"status": "Open", "occupancyAvg": "45", "1F": "50", "2F": "45", "3F": "40", "4F": "40", "5F": "35", "6F": "50", "mostFree": "5F"},
            "22:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "23:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"}
        }
    },
    {
        "id": 3,
        "name": "Burke Library",
        "floors": 6,
        "hours": "9am - 11pm",
        "occupancy":{
            "00:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "01:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "02:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "03:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "04:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "05:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "06:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "07:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "08:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "09:00": {"status": "Open", "occupancyAvg": "20", "1F": "25", "2F": "20", "3F": "15", "4F": "20", "5F": "15", "6F": "25", "mostFree": "5F"},
            "10:00": {"status": "Open", "occupancyAvg": "40", "1F": "45", "2F": "40", "3F": "35", "4F": "40", "5F": "35", "6F": "45", "mostFree": "5F"},
            "11:00": {"status": "Open", "occupancyAvg": "60", "1F": "65", "2F": "60", "3F": "55", "4F": "60", "5F": "55", "6F": "65", "mostFree": "5F"},
            "12:00": {"status": "Open", "occupancyAvg": "80", "1F": "85", "2F": "80", "3F": "75", "4F": "80", "5F": "75", "6F": "85", "mostFree": "5F"},
            "13:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "90", "3F": "85", "4F": "90", "5F": "85", "6F": "95", "mostFree": "5F"},
            "14:00": {"status": "Open", "occupancyAvg": "95", "1F": "100", "2F": "95", "3F": "90", "4F": "95", "5F": "90", "6F": "100", "mostFree": "5F"},
            "15:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "90", "3F": "85", "4F": "90", "5F": "85", "6F": "95", "mostFree": "5F"},
            "16:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "85", "3F": "80", "4F": "85", "5F": "80", "6F": "90", "mostFree": "5F"},
            "17:00": {"status": "Open", "occupancyAvg": "75", "1F": "80", "2F": "75", "3F": "70", "4F": "75", "5F": "70", "6F": "80", "mostFree": "5F"},
            "18:00": {"status": "Open", "occupancyAvg": "65", "1F": "70", "2F": "65", "3F": "60", "4F": "65", "5F": "60", "6F": "70", "mostFree": "5F"},
            "19:00": {"status": "Open", "occupancyAvg": "80", "1F": "85", "2F": "80", "3F": "75", "4F": "80", "5F": "75", "6F": "85", "mostFree": "5F"},
            "20:00": {"status": "Open", "occupancyAvg": "70", "1F": "75", "2F": "70", "3F": "65", "4F": "70", "5F": "65", "6F": "75", "mostFree": "5F"},
            "21:00": {"status": "Open", "occupancyAvg": "50", "1F": "55", "2F": "50", "3F": "45", "4F": "50", "5F": "45", "6F": "55", "mostFree": "5F"},
            "22:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"},
            "23:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "3F": "0", "4F": "0", "5F": "0", "6F": "0", "mostFree": "Not open"}
        }
    },
    {
        "id": 4,
        "name": "Business Library",
        "floors": 2,
        "hours": "9am - 11pm",
        "occupancy": {
            "00:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "01:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "02:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "03:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "04:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "05:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "06:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "07:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "08:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "09:00": {"status": "Open", "occupancyAvg": "30", "1F": "35", "2F": "25", "mostFree": "2F"},
            "10:00": {"status": "Open", "occupancyAvg": "50", "1F": "55", "2F": "45", "mostFree": "2F"},
            "11:00": {"status": "Open", "occupancyAvg": "70", "1F": "75", "2F": "65", "mostFree": "2F"},
            "12:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "80", "mostFree": "2F"},
            "13:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "85", "mostFree": "2F"},
            "14:00": {"status": "Open", "occupancyAvg": "95", "1F": "100", "2F": "90", "mostFree": "2F"},
            "15:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "85", "mostFree": "2F"},
            "16:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "80", "mostFree": "2F"},
            "17:00": {"status": "Open", "occupancyAvg": "75", "1F": "80", "2F": "70", "mostFree": "2F"},
            "18:00": {"status": "Open", "occupancyAvg": "65", "1F": "70", "2F": "60", "mostFree": "2F"},
            "19:00": {"status": "Open", "occupancyAvg": "80", "1F": "85", "2F": "75", "mostFree": "2F"},
            "20:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "80", "mostFree": "2F"},
            "21:00": {"status": "Open", "occupancyAvg": "70", "1F": "75", "2F": "65", "mostFree": "2F"},
            "22:00": {"status": "Open", "occupancyAvg": "45", "1F": "50", "2F": "40", "mostFree": "2F"},
            "23:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"}
        }
    },
    {
        "id": 5,
        "name": "Butler Library",
        "floors": 6,
        "hours": "24hrs",
        "occupancy": {
            "00:00": {"status": "Open", "occupancyAvg": "10", "1F": "20", "2F": "15", "3F": "10", "4F": "5", "5F": "0", "6F": "0", "mostFree": "4F"},
            "01:00": {"status": "Open", "occupancyAvg": "8", "1F": "15", "2F": "10", "3F": "8", "4F": "5", "5F": "0", "6F": "0", "mostFree": "4F"},
            "02:00": {"status": "Open", "occupancyAvg": "5", "1F": "10", "2F": "8", "3F": "5", "4F": "3", "5F": "0", "6F": "0", "mostFree": "4F"},
            "03:00": {"status": "Open", "occupancyAvg": "4", "1F": "8", "2F": "5", "3F": "4", "4F": "2", "5F": "0", "6F": "0", "mostFree": "4F"},
            "04:00": {"status": "Open", "occupancyAvg": "3", "1F": "5", "2F": "4", "3F": "3", "4F": "1", "5F": "0", "6F": "0", "mostFree": "4F"},
            "05:00": {"status": "Open", "occupancyAvg": "3", "1F": "5", "2F": "4", "3F": "3", "4F": "1", "5F": "0", "6F": "0", "mostFree": "4F"},
            "06:00": {"status": "Open", "occupancyAvg": "5", "1F": "10", "2F": "8", "3F": "5", "4F": "3", "5F": "0", "6F": "0", "mostFree": "4F"},
            "07:00": {"status": "Open", "occupancyAvg": "10", "1F": "15", "2F": "12", "3F": "10", "4F": "5", "5F": "0", "6F": "0", "mostFree": "4F"},
            "08:00": {"status": "Open", "occupancyAvg": "25", "1F": "30", "2F": "25", "3F": "20", "4F": "15", "5F": "0", "6F": "0", "mostFree": "4F"},
            "09:00": {"status": "Open", "occupancyAvg": "35", "1F": "40", "2F": "35", "3F": "30", "4F": "25", "5F": "10", "6F": "10", "mostFree": "5F"},
            "10:00": {"status": "Open", "occupancyAvg": "50", "1F": "60", "2F": "50", "3F": "45", "4F": "40", "5F": "20", "6F": "20", "mostFree": "5F"},
            "11:00": {"status": "Open", "occupancyAvg": "65", "1F": "70", "2F": "65", "3F": "60", "4F": "55", "5F": "30", "6F": "30", "mostFree": "5F"},
            "12:00": {"status": "Open", "occupancyAvg": "80", "1F": "85", "2F": "80", "3F": "75", "4F": "70", "5F": "40", "6F": "40", "mostFree": "5F"},
            "13:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "85", "3F": "80", "4F": "75", "5F": "50", "6F": "50", "mostFree": "5F"},
            "14:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "90", "3F": "85", "4F": "80", "5F": "60", "6F": "60", "mostFree": "5F"},
            "15:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "85", "3F": "80", "4F": "75", "5F": "55", "6F": "55", "mostFree": "5F"},
            "16:00": {"status": "Open", "occupancyAvg": "75", "1F": "80", "2F": "75", "3F": "70", "4F": "65", "5F": "50", "6F": "50", "mostFree": "5F"},
            "17:00": {"status": "Open", "occupancyAvg": "65", "1F": "70", "2F": "65", "3F": "60", "4F": "55", "5F": "40", "6F": "40", "mostFree": "5F"},
            "18:00": {"status": "Open", "occupancyAvg": "50", "1F": "55", "2F": "50", "3F": "45", "4F": "40", "5F": "30", "6F": "30", "mostFree": "5F"},
            "19:00": {"status": "Open", "occupancyAvg": "35", "1F": "40", "2F": "35", "3F": "30", "4F": "25", "5F": "0", "6F": "0", "mostFree": "4F"},
            "20:00": {"status": "Open", "occupancyAvg": "25", "1F": "30", "2F": "25", "3F": "20", "4F": "15", "5F": "0", "6F": "0", "mostFree": "4F"},
            "21:00": {"status": "Open", "occupancyAvg": "15", "1F": "20", "2F": "15", "3F": "10", "4F": "8", "5F": "0", "6F": "0", "mostFree": "4F"},
            "22:00": {"status": "Open", "occupancyAvg": "10", "1F": "15", "2F": "10", "3F": "8", "4F": "5", "5F": "0", "6F": "0", "mostFree": "4F"},
            "23:00": {"status": "Open", "occupancyAvg": "5", "1F": "10", "2F": "5", "3F": "3", "4F": "2", "5F": "0", "6F": "0", "mostFree": "4F"}
        }
    },
    {
        "id": 6,
        "name": "Lehman Library",
        "floors": 1,
        "hours": "8am - 12am",
        "occupancy": {
            "00:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "01:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "02:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "03:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "04:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "05:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "06:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "07:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "08:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "09:00": {"status": "Open", "occupancyAvg": "20", "1F": "20", "mostFree": "1F"},
            "10:00": {"status": "Open", "occupancyAvg": "40", "1F": "40", "mostFree": "1F"},
            "11:00": {"status": "Open", "occupancyAvg": "60", "1F": "60", "mostFree": "1F"},
            "12:00": {"status": "Open", "occupancyAvg": "75", "1F": "75", "mostFree": "1F"},
            "13:00": {"status": "Open", "occupancyAvg": "85", "1F": "85", "mostFree": "1F"},
            "14:00": {"status": "Open", "occupancyAvg": "90", "1F": "90", "mostFree": "1F"},
            "15:00": {"status": "Open", "occupancyAvg": "85", "1F": "85", "mostFree": "1F"},
            "16:00": {"status": "Open", "occupancyAvg": "80", "1F": "80", "mostFree": "1F"},
            "17:00": {"status": "Open", "occupancyAvg": "70", "1F": "70", "mostFree": "1F"},
            "18:00": {"status": "Open", "occupancyAvg": "65", "1F": "65", "mostFree": "1F"},
            "19:00": {"status": "Open", "occupancyAvg": "75", "1F": "75", "mostFree": "1F"},
            "20:00": {"status": "Open", "occupancyAvg": "80", "1F": "80", "mostFree": "1F"},
            "21:00": {"status": "Open", "occupancyAvg": "70", "1F": "70", "mostFree": "1F"},
            "22:00": {"status": "Open", "occupancyAvg": "55", "1F": "55", "mostFree": "1F"},
            "23:00": {"status": "Open", "occupancyAvg": "40", "1F": "40", "mostFree": "1F"}
        }
    },
    {
        "id": 7,
        "name": "Science Library",
        "floors": 2,
        "hours": "9am - 11pm",
        "occupancy": {
            "00:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "01:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "02:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "03:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "04:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "05:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "06:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "07:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "08:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"},
            "09:00": {"status": "Open", "occupancyAvg": "25", "1F": "30", "2F": "20", "mostFree": "2F"},
            "10:00": {"status": "Open", "occupancyAvg": "45", "1F": "50", "2F": "40", "mostFree": "2F"},
            "11:00": {"status": "Open", "occupancyAvg": "65", "1F": "70", "2F": "60", "mostFree": "2F"},
            "12:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "80", "mostFree": "2F"},
            "13:00": {"status": "Open", "occupancyAvg": "95", "1F": "100", "2F": "90", "mostFree": "2F"},
            "14:00": {"status": "Open", "occupancyAvg": "90", "1F": "95", "2F": "85", "mostFree": "2F"},
            "15:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "80", "mostFree": "2F"},
            "16:00": {"status": "Open", "occupancyAvg": "80", "1F": "85", "2F": "75", "mostFree": "2F"},
            "17:00": {"status": "Open", "occupancyAvg": "70", "1F": "75", "2F": "65", "mostFree": "2F"},
            "18:00": {"status": "Open", "occupancyAvg": "60", "1F": "65", "2F": "55", "mostFree": "2F"},
            "19:00": {"status": "Open", "occupancyAvg": "75", "1F": "80", "2F": "70", "mostFree": "2F"},
            "20:00": {"status": "Open", "occupancyAvg": "85", "1F": "90", "2F": "80", "mostFree": "2F"},
            "21:00": {"status": "Open", "occupancyAvg": "70", "1F": "75", "2F": "65", "mostFree": "2F"},
            "22:00": {"status": "Open", "occupancyAvg": "45", "1F": "50", "2F": "40", "mostFree": "2F"},
            "23:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "2F": "0", "mostFree": "Not open"}
        }
    },
    {
        "id": 8,
        "name": "Teachers Library",
        "floors": 1,
        "hours": "9am - 11pm",
        "occupancy": {
            "00:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "01:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "02:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "03:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "04:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "05:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "06:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "07:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "08:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "09:00": {"status": "Open", "occupancyAvg": "15", "1F": "15", "mostFree": "1F"},
            "10:00": {"status": "Open", "occupancyAvg": "35", "1F": "35", "mostFree": "1F"},
            "11:00": {"status": "Open", "occupancyAvg": "55", "1F": "55", "mostFree": "1F"},
            "12:00": {"status": "Open", "occupancyAvg": "75", "1F": "75", "mostFree": "1F"},
            "13:00": {"status": "Open", "occupancyAvg": "85", "1F": "85", "mostFree": "1F"},
            "14:00": {"status": "Open", "occupancyAvg": "80", "1F": "80", "mostFree": "1F"},
            "15:00": {"status": "Open", "occupancyAvg": "75", "1F": "75", "mostFree": "1F"},
            "16:00": {"status": "Open", "occupancyAvg": "70", "1F": "70", "mostFree": "1F"},
            "17:00": {"status": "Open", "occupancyAvg": "60", "1F": "60", "mostFree": "1F"},
            "18:00": {"status": "Open", "occupancyAvg": "50", "1F": "50", "mostFree": "1F"},
            "19:00": {"status": "Open", "occupancyAvg": "45", "1F": "45", "mostFree": "1F"},
            "20:00": {"status": "Open", "occupancyAvg": "35", "1F": "35", "mostFree": "1F"},
            "21:00": {"status": "Open", "occupancyAvg": "25", "1F": "25", "mostFree": "1F"},
            "22:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"},
            "23:00": {"status": "Closed", "occupancyAvg": "0", "1F": "0", "mostFree": "Not open"}
        }
    }
]

def get_current_hour():
    return datetime.now().strftime("%H:00")

@app.route('/libraries/occupancy', methods=['GET'])
def get_libraries_with_occupancy():
    current_hour = get_current_hour()
    result = []

    for library in libraries:
        occupancy_data = library['occupancy'].get(current_hour, None)
        if occupancy_data:
            result.append({
                "id": library["id"],
                "name": library["name"],
                "floors": library["floors"],
                "hours": library["hours"],
                "current_hour_occupancy": occupancy_data
            })

    return jsonify(result)

@app.route('/libraries/<int:library_id>/occupancy', methods=['GET'])
def get_library_occupancy_by_id(library_id):
    current_hour = get_current_hour()
    library = next((lib for lib in libraries if lib["id"] == library_id), None)

    if not library:
        return jsonify({"error": "Library not found"}), 404

    occupancy_data = library['occupancy'].get(current_hour, None)
    if not occupancy_data:
        return jsonify({"error": "No data available for the current hour"}), 404

    return jsonify({
        "id": library["id"],
        "name": library["name"],
        "floors": library["floors"],
        "hours": library["hours"],
        "current_hour_occupancy": occupancy_data
    })

@app.route('/libraries/top-available', methods=['GET'])
def get_top_available_libraries():
    current_hour = get_current_hour()
    library_availabilities = []

    for library in libraries:
        occupancy_data = library['occupancy'].get(current_hour, None)
        if occupancy_data and occupancy_data['status'] == 'Open':
            available_space = sum(int(v) for k, v in occupancy_data.items() if k.endswith('F') and v.isdigit())
            library_availabilities.append({
                "id": library["id"],
                "name": library["name"],
                "floors": library["floors"],
                "hours": library["hours"],
                "current_hour_occupancy": occupancy_data,
                "available_space": available_space
            })

    top_libraries = sorted(library_availabilities, key=lambda x: x['available_space'], reverse=True)[:3]
    return jsonify(top_libraries)

@app.route('/libraries/least-occupied', methods=['GET'])
def get_least_occupied_library():
    current_hour = get_current_hour()
    library_occupancies = []

    for library in libraries:
        occupancy_data = library['occupancy'].get(current_hour, None)
        if occupancy_data and occupancy_data['status'] == 'Open':
            occupancy_avg = float(occupancy_data['occupancyAvg'])
            library_occupancies.append({
                "id": library["id"],
                "name": library["name"],
                "floors": library["floors"],
                "hours": library["hours"],
                "current_hour_occupancy": occupancy_data
            })

    if not library_occupancies:
        return jsonify({"error": "No open libraries found"}), 404

    # Sort by occupancy average and get the least occupied
    least_occupied = sorted(library_occupancies, 
                          key=lambda x: float(x['current_hour_occupancy']['occupancyAvg']))[0]
    return jsonify(least_occupied)

@app.route('/libraries/second-least-occupied', methods=['GET'])
def get_second_least_occupied_library():
    current_hour = get_current_hour()
    library_occupancies = []

    for library in libraries:
        occupancy_data = library['occupancy'].get(current_hour, None)
        if occupancy_data and occupancy_data['status'] == 'Open':
            occupancy_avg = float(occupancy_data['occupancyAvg'])
            library_occupancies.append({
                "id": library["id"],
                "name": library["name"],
                "floors": library["floors"],
                "hours": library["hours"],
                "current_hour_occupancy": occupancy_data
            })

    if len(library_occupancies) < 2:
        return jsonify({"error": "Not enough open libraries found"}), 404

    # Sort by occupancy average and get the second least occupied
    sorted_libraries = sorted(library_occupancies, 
                            key=lambda x: float(x['current_hour_occupancy']['occupancyAvg']))
    return jsonify(sorted_libraries[1])

@app.route('/libraries/third-least-occupied', methods=['GET'])
def get_third_least_occupied_library():
    current_hour = get_current_hour()
    library_occupancies = []

    for library in libraries:
        occupancy_data = library['occupancy'].get(current_hour, None)
        if occupancy_data and occupancy_data['status'] == 'Open':
            occupancy_avg = float(occupancy_data['occupancyAvg'])
            library_occupancies.append({
                "id": library["id"],
                "name": library["name"],
                "floors": library["floors"],
                "hours": library["hours"],
                "current_hour_occupancy": occupancy_data
            })

    if len(library_occupancies) < 3:
        return jsonify({"error": "Not enough open libraries found"}), 404

    # Sort by occupancy average and get the third least occupied
    sorted_libraries = sorted(library_occupancies, 
                            key=lambda x: float(x['current_hour_occupancy']['occupancyAvg']))
    return jsonify(sorted_libraries[2])

if __name__ == '__main__':
    app.run(debug=True)