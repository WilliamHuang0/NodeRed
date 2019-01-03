[
    {
        "id": "65a16ac5.122fa4",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "f0704ef7.427b4",
        "type": "inject",
        "z": "65a16ac5.122fa4",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 130,
        "y": 180,
        "wires": [
            [
                "d065f596.2f13e8"
            ]
        ]
    },
    {
        "id": "d065f596.2f13e8",
        "type": "function",
        "z": "65a16ac5.122fa4",
        "name": "Payload",
        "func": "msg.headers={\n  deviceKey:  \"EusYOU6bXEvf5pCb\"\n};\nreturn msg;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 330,
        "y": 260,
        "wires": [
            [
                "961bb10f.88f9a"
            ]
        ]
    },
    {
        "id": "961bb10f.88f9a",
        "type": "http request",
        "z": "65a16ac5.122fa4",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/D50mpDdK/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "x": 530,
        "y": 260,
        "wires": [
            [
                "24c53968.d0b6d6",
                "c2124758.3649b8"
            ]
        ]
    },
    {
        "id": "24c53968.d0b6d6",
        "type": "http response",
        "z": "65a16ac5.122fa4",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 730,
        "y": 260,
        "wires": []
    },
    {
        "id": "c2124758.3649b8",
        "type": "debug",
        "z": "65a16ac5.122fa4",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 730,
        "y": 340,
        "wires": []
    },
    {
        "id": "c2c81041.8ab5a",
        "type": "inject",
        "z": "65a16ac5.122fa4",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 130,
        "y": 400,
        "wires": [
            [
                "9ecad342.cf01c"
            ]
        ]
    },
    {
        "id": "9ecad342.cf01c",
        "type": "function",
        "z": "65a16ac5.122fa4",
        "name": "Payload",
        "func": "msg.headers={\n  deviceKey:  \"EusYOU6bXEvf5pCb\"\n};\nreturn msg;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 330,
        "y": 400,
        "wires": [
            [
                "d71c8767.e635c8"
            ]
        ]
    },
    {
        "id": "d71c8767.e635c8",
        "type": "http request",
        "z": "65a16ac5.122fa4",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/D50mpDdK/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 525,
        "y": 400,
        "wires": [
            [
                "24c53968.d0b6d6",
                "c2124758.3649b8"
            ]
        ]
    }
]
