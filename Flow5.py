[
    {
        "id": "6c7e0300.a3ce2c",
        "type": "tab",
        "label": "Flow 6",
        "disabled": false,
        "info": ""
    },
    {
        "id": "f6c4db41.4913e8",
        "type": "http in",
        "z": "6c7e0300.a3ce2c",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 130,
        "y": 260,
        "wires": [
            [
                "93f4e800.903f18",
                "31646dac.ab0a62"
            ]
        ]
    },
    {
        "id": "93f4e800.903f18",
        "type": "function",
        "z": "6c7e0300.a3ce2c",
        "name": "Set to 1",
        "func": "msg.payload=1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 260,
        "wires": [
            [
                "31de0aea.14b186"
            ]
        ]
    },
    {
        "id": "31de0aea.14b186",
        "type": "rpi-gpio out",
        "z": "6c7e0300.a3ce2c",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 520,
        "y": 180,
        "wires": []
    },
    {
        "id": "31646dac.ab0a62",
        "type": "function",
        "z": "6c7e0300.a3ce2c",
        "name": "Return Status",
        "func": "msg.payload =(\"GPIO5 set to HIGH\")\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 350,
        "y": 340,
        "wires": [
            [
                "fa7726eb.3979f8",
                "3a778bce.6f9d34"
            ]
        ]
    },
    {
        "id": "fa7726eb.3979f8",
        "type": "http response",
        "z": "6c7e0300.a3ce2c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 770,
        "y": 60,
        "wires": []
    },
    {
        "id": "3a778bce.6f9d34",
        "type": "debug",
        "z": "6c7e0300.a3ce2c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 790,
        "y": 180,
        "wires": []
    },
    {
        "id": "c3da1fb9.76c03",
        "type": "http in",
        "z": "6c7e0300.a3ce2c",
        "name": "Clear GPIO5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 130,
        "y": 60,
        "wires": [
            [
                "384614fb.9880ac",
                "c739e482.7d4f88"
            ]
        ]
    },
    {
        "id": "384614fb.9880ac",
        "type": "function",
        "z": "6c7e0300.a3ce2c",
        "name": "Clear to 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 120,
        "wires": [
            [
                "31de0aea.14b186"
            ]
        ]
    },
    {
        "id": "c739e482.7d4f88",
        "type": "function",
        "z": "6c7e0300.a3ce2c",
        "name": "Return Status",
        "func": "msg.payload=\"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 60,
        "wires": [
            [
                "fa7726eb.3979f8",
                "3a778bce.6f9d34"
            ]
        ]
    }
]
