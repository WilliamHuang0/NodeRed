[
    {
        "id": "eaac744a.418588",
        "type": "tab",
        "label": "Flow 3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "b761b190.1a0d3",
        "type": "inject",
        "z": "eaac744a.418588",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 110,
        "y": 180,
        "wires": [
            [
                "6b703653.cafb08"
            ]
        ]
    },
    {
        "id": "6b703653.cafb08",
        "type": "function",
        "z": "eaac744a.418588",
        "name": "Payload",
        "func": "msg.headers={\n  deviceKey:  \"EusYOU6bXEvf5pCb\"\n};\nmsg.payload = \"Temperature,,40\";\nreturn msg;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 330,
        "y": 260,
        "wires": [
            [
                "cd42c698.aa3d68"
            ]
        ]
    },
    {
        "id": "cd42c698.aa3d68",
        "type": "http request",
        "z": "eaac744a.418588",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/D50mpDdK/datapoints.csv",
        "tls": "",
        "x": 490,
        "y": 260,
        "wires": [
            [
                "8be11251.14593",
                "dcf52d86.acbcc"
            ]
        ]
    },
    {
        "id": "8be11251.14593",
        "type": "http response",
        "z": "eaac744a.418588",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 670,
        "y": 260,
        "wires": []
    },
    {
        "id": "dcf52d86.acbcc",
        "type": "debug",
        "z": "eaac744a.418588",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 700,
        "y": 340,
        "wires": []
    },
    {
        "id": "dc5a81fb.9fd69",
        "type": "inject",
        "z": "eaac744a.418588",
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
                "e7df3bed.757348"
            ]
        ]
    },
    {
        "id": "e7df3bed.757348",
        "type": "function",
        "z": "eaac744a.418588",
        "name": "Payload",
        "func": "msg.headers={\n  deviceKey:  \"EusYOU6bXEvf5pCb\"\n};\nmsg.payload = \"Humidity,,120\";\nreturn msg;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 310,
        "y": 400,
        "wires": [
            [
                "b39fc089.fff2a"
            ]
        ]
    },
    {
        "id": "b39fc089.fff2a",
        "type": "http request",
        "z": "eaac744a.418588",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/D50mpDdK/datapoints.csv",
        "tls": "",
        "x": 470,
        "y": 380,
        "wires": [
            [
                "8be11251.14593",
                "dcf52d86.acbcc"
            ]
        ]
    }
]
