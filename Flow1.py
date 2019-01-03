[
    {
        "id": "c603c87d.722548",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "26532123.e60cde",
        "type": "rpi-gpio out",
        "z": "c603c87d.722548",
        "name": "Green LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 350,
        "y": 240,
        "wires": []
    },
    {
        "id": "91fa203c.91654",
        "type": "inject",
        "z": "c603c87d.722548",
        "name": "On",
        "topic": "",
        "payload": "1",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 90,
        "y": 200,
        "wires": [
            [
                "26532123.e60cde",
                "dbce5fc8.d0e54"
            ]
        ]
    },
    {
        "id": "efa2f000.08bce",
        "type": "inject",
        "z": "c603c87d.722548",
        "name": "Off",
        "topic": "",
        "payload": "0",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 90,
        "y": 280,
        "wires": [
            [
                "26532123.e60cde",
                "dbce5fc8.d0e54"
            ]
        ]
    },
    {
        "id": "dbce5fc8.d0e54",
        "type": "debug",
        "z": "c603c87d.722548",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 350,
        "y": 160,
        "wires": []
    }
]
