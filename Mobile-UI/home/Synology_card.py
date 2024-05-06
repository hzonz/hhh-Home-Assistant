# 理论，支持所有群晖，图片部分需自定义。
if card_type == "群晖卡片-hhh":
  card = {
    "type": "custom:button-card",
    "name": """
            [[[
                var icon = states['binary_sensor.10_10_10_5'].state === 'on' ? 'mdi:nas' : 'mdi:alert-circle-outline';
                var iconColor = states['binary_sensor.10_10_10_5'].state === 'on' ? 'blue' : 'red';
                return `<ha-icon icon="${icon}" style="width: 30px; color: ${iconColor};"></ha-icon> Synology NAS`;
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
                "entity": "sensor.synologynas_cpu_utilization_total",
                "name": "CPU利用率",
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
                "entity": "sensor.synologynas_memory_usage_real",
                "name": "RAM利用率",
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
                "entity": "sensor.synologynas_upload_throughput",
                "name": "上传吞吐量",
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
                "entity": "sensor.synologynas_download_throughput",
                "name": "下载吞吐量",
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
                "entity": "sensor.synologynas_volume_1_volume_used",
                "name": "Volume 1",
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
                "entity": "sensor.synologynas_volume_2_volume_used",
                "name": "Volume 2",
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
                "entity_picture": "/local/img/DS3622XS.png",
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
