#理论，适用于所有设备，图片部分需自定义。
if card_type == "设备卡片-hhh":
  card = {
    "type": "custom:button-card",
    "name": """
            [[[
                var icon = states['binary_sensor.10_10_10_3'].state === 'on' ? 'mdi:server-network' : 'mdi:server-network-off';
                var iconColor = states['binary_sensor.10_10_10_3'].state === 'on' ? 'cyan' : 'red';
                return `<ha-icon icon="${icon}" style="width: 30px; color: ${iconColor};"></ha-icon> Proxmox VE IPMI`;
            ]]]
            """,
    "show_icon": true,
    "show_state": true,
    "show_name": true,
    "styles": {
        "grid": [
            {"grid-template-areas": '"n n n" "a b g" "c d g" "e f g" '},
            {"grid-template-columns": "1fr 1fr 1.5fr"},
            {"grid-template-rows": "auto 1fr 1fr 1fr"}
        ],
        "name": [
            {"font-weight": "bold"},
            {"font-size": "20px"},
            {"align-self": "start"},
            {"justify-self": "start"},
            {"margin": "6%"}
        ],
        "card": [{"padding": "6px"}]
    },
    "custom_fields": {
        "a": {
            "card": {
                "type": "custom:button-card",
                "entity": "sensor.server_cpu_temp",
                "name": "CPU温度",
                "show_icon": false,
                "show_name": true,
                "show_state": true,
                "show_label": true,
                "styles": {
                    "grid": [{"grid-template-areas": '"s" "n"'}],
                    "card": [
                        {"background": "none"},
                        {"border": "none"},
                        {"box-shadow": "none"},
                        {"margin-left": "10%"},
                        {"border-radius": "0px !important"}
                    ],
                    "name": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-size": "10px"}
                    ],
                    "state": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-weight": "bold"},
                        {"font-size": "15px"}
                    ]
                }
            }
        },
        "b": {
            "card": {
                "type": "custom:button-card",
                "entity": "sensor.ipmi_ramwen_du",
                "name": "RAM温度",
                "show_icon": false,
                "show_name": true,
                "show_state": true,
                "styles": {
                    "grid": [{"grid-template-areas": '"s" "n"'}],
                    "card": [
                        {"background": "none"},
                        {"border": "none"},
                        {"box-shadow": "none"},
                        {"border-radius": "0px !important"}
                    ],
                    "name": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-size": "10px"}
                    ],
                    "state": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-weight": "bold"},
                        {"font-size": "15px"}
                    ]
                }
            }
        },
        "c": {
            "card": {
                "type": "custom:button-card",
                "entity": "sensor.server_pch_temp",
                "name": "PCH温度",
                "show_icon": false,
                "show_name": true,
                "show_state": true,
                "show_label": false,
                "styles": {
                    "grid": [{"grid-template-areas": '"s" "n"'}],
                    "card": [
                        {"background": "none"},
                        {"border": "none"},
                        {"box-shadow": "none"},
                        {"margin-left": "10%"},
                        {"border-radius": "0px !important"}
                    ],
                    "name": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-size": "10px"}
                    ],
                    "state": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-weight": "bold"},
                        {"font-size": "15px"}
                    ]
                }
            }
        },
        "d": {
            "card": {
                "type": "custom:button-card",
                "entity": "sensor.server_system_temp",
                "name": "NVME温度",
                "show_icon": false,
                "show_name": true,
                "show_state": true,
                "show_label": true,
                "styles": {
                    "grid": [{"grid-template-areas": '"s" "n"'}],
                    "card": [
                        {"background": "none"},
                        {"border": "none"},
                        {"box-shadow": "none"},
                        {"border-radius": "0px !important"}
                    ],
                    "name": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-size": "10px"}
                    ],
                    "state": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-weight": "bold"},
                        {"font-size": "15px"}
                    ]
                }
            }
        },
        "e": {
            "card": {
                "type": "custom:button-card",
                "entity": "sensor.server_fan1",
                "name": "CPU FAN",
                "show_icon": false,
                "show_name": true,
                "show_state": true,
                "show_label": true,
                "styles": {
                    "grid": [{"grid-template-areas": '"s" "n"'}],
                    "card": [
                        {"background": "none"},
                        {"border": "none"},
                        {"box-shadow": "none"},
                        {"margin-left": "10%"},
                        {"border-radius": "0px !important"}
                    ],
                    "name": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-size": "10px"}
                    ],
                    "state": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-weight": "bold"},
                        {"font-size": "15px"}
                    ]
                }
            }
        },
        "f": {
            "card": {
                "type": "custom:button-card",
                "entity": "sensor.server_fan2",
                "name": "机箱FAN",
                "show_icon": false,
                "show_name": true,
                "show_state": true,
                "show_label": true,
                "styles": {
                    "grid": [{"grid-template-areas": '"s" "n"'}],
                    "card": [
                        {"background": "none"},
                        {"border": "none"},
                        {"box-shadow": "none"},
                        {"border-radius": "0px !important"}
                    ],
                    "name": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-size": "10px"}
                    ],
                    "state": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"font-weight": "bold"},
                        {"font-size": "15px"}
                    ]
                }
            }
        },
        "g": {
            "card": {
                "type": "custom:button-card",
                "name": "图片",
                "show_entity_picture": true,
                "entity_picture": "/local/img/server.png",
                "show_icon": false,
                "show_name": false,
                "show_state": false,
                "styles": {
                    "card": [
                        {"background": "none"},
                        {"border": "none"},
                        {"box-shadow": "none"}
                    ],
                    "entity_picture": [
                        {"align-self": "start"},
                        {"justify-self": "start"},
                        {"width": "120px"},
                        {"padding": "0px"}
                    ]
                }
            }
        }
    }
}
