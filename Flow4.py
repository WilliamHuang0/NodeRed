[
    {
        "id": "cb183c2.b0552c",
        "type": "tab",
        "label": "Flow 5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "5e1303c.e2d3efc",
        "type": "http in",
        "z": "cb183c2.b0552c",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 130,
        "y": 180,
        "wires": [
            [
                "cb787c6c.35f15"
            ]
        ]
    },
    {
        "id": "75161f53.dbb8f",
        "type": "rpi-gpio in",
        "z": "cb183c2.b0552c",
        "name": "GPIO4",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": false,
        "x": 110,
        "y": 300,
        "wires": [
            [
                "24aeea3a.0c1786"
            ]
        ]
    },
    {
        "id": "24aeea3a.0c1786",
        "type": "function",
        "z": "cb183c2.b0552c",
        "name": "Set GPIO",
        "func": "global.set(\"GPIO\",msg.payload) \nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 280,
        "y": 260,
        "wires": [
            [
                "7a0e1ada.fd8114"
            ]
        ]
    },
    {
        "id": "cb787c6c.35f15",
        "type": "function",
        "z": "cb183c2.b0552c",
        "name": "Get GPIO",
        "func": "msg.payload = global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 180,
        "wires": [
            [
                "3d00415d.5ad14e",
                "7a0e1ada.fd8114"
            ]
        ]
    },
    {
        "id": "3d00415d.5ad14e",
        "type": "http response",
        "z": "cb183c2.b0552c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 530,
        "y": 180,
        "wires": []
    },
    {
        "id": "7a0e1ada.fd8114",
        "type": "debug",
        "z": "cb183c2.b0552c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "x": 530,
        "y": 260,
        "wires": []
    }
]
