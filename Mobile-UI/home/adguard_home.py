#正常情况无需更改任何实体ID。
if card_type == "AdGuard HOME-hhh":
  card = {
    "type": "custom:button-card",
    "name": """
            [[[ 
                var icon = states['binary_sensor.10_10_10_10'].state === 'on' ? 'mdi:shield-check' : 'mdi:shield-off';
                var iconColor = states['binary_sensor.10_10_10_10'].state === 'on' ? 'green' : 'red';
                return `<ha-icon icon="${icon}" style="width: 30px; color: ${iconColor};"></ha-icon> AdGuard HOME`;
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
                "entity": "sensor.adguard_home_average_processing_speed",
                "name": "平均处理速度",
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
                "entity": "sensor.adguard_home_dns_queries_blocked_ratio",
                "name": "DNS查询阻塞率",
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
                "entity": "sensor.adguard_home_dns_queries",
                "name": "DNS查询",
                "show_icon": false,
                "show_name": true,
                "show_state": false,
                "show_label": true,
                "label": """
                        [[[ 
                            var value = states['sensor.adguard_home_dns_queries'].state.split(' ')[0];
                            return (parseFloat(value) / 10000).toFixed(2) + ' 万';
                        ]]]
                        """,
                "styles": {
                    "grid": [{"grid-template-areas": '"l" "n"'}],
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
                    "label": [
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
                "entity": "sensor.adguard_home_dns_queries_blocked",
                "name": "DNS查询被阻止",
                "show_icon": false,
                "show_name": true,
                "show_state": false,
                "show_label": true,
                "label": """
                        [[[ 
                            var value = states['sensor.adguard_home_dns_queries_blocked'].state.split(' ')[0];
                            return (parseFloat(value) / 10000).toFixed(2) + ' 万';
                        ]]]
                        """,
                "styles": {
                    "grid": [{"grid-template-areas": '"l" "n"'}],
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
                    "label": [
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
                "entity": "switch.adguard_home_safe_browsing",
                "name": "安全浏览",
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
                        {"font-size": "15px"},
                        {"color": """
                                [[[ 
                                    return states["switch.adguard_home_safe_browsing"].state === "on" ? "blue" : ""; 
                                ]]]
                                """
                        }
                    ]
                }
            }
        },
        "f": {
            "card": {
                "type": "custom:button-card",
                "entity": "switch.adguard_home_parental_control",
                "name": "家长控制",
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
                        {"font-size": "15px"},
                        {"color": """
                                [[[ 
                                    return states["switch.adguard_home_parental_control"].state === "on" ? "blue" : ""; 
                                ]]]
                                """
                        }
                    ]
                }
            }
        },
        "g": {
            "card": {
                "type": "custom:button-card",
                "name": "图片",
                "show_entity_picture": true,
                "entity_picture": "/local/img/agnar.png",
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
