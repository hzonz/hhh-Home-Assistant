#支持ikuai。
if card_type == "网络信息卡片-hhh":
  card = {
    "type": "vertical-stack",
    "cards": [
        {
            "type": "custom:button-card",
            "name": "设备信息",
            "show_icon": true,
            "show_state": true,
            "show_name": true,
            "styles": {
                "grid": [
                    {"grid-template-areas": '"n n" "a a" "b b" "c c" "d d" '},
                    {"grid-template-columns": "1fr 1fr"},
                    {"grid-template-rows": "40px 1fr 1fr 1fr max-content"}
                ],
                "name": [
                    {"font-size": "18px"},
                    {"align-self": "start"},
                    {"justify-self": "start"},
                    {"margin-left": "8px"}
                ],
                "card": [{"padding": "6px"}]
            },
            "custom_fields": {
                "a": "ikuai Router",
                "b": "制造商：ikuai",
                "c": "开机时长: </span><span>{{states('sensor.ikuai_uptime')}}</span>",
                "d": "固件:"
            }
        },
        {
            "type": "horizontal-stack",
            "cards": [
                {
                    "type": "custom:mushroom-entity-card",
                    "layout": "vertical",
                    "fill_container": false,
                    "entity": "switch.ikuai_arp_filter",
                    "icon": "mdi:account-lock",
                    "icon_color": "yellow",
                    "secondary_info": "none",
                    "tap_action": {
                        "action": "call-service",
                        "service": "switch.toggle",
                        "target": {"entity_id": "switch.ikuai_arp_filter"},
                        "data": {}
                    }
                },
                {
                    "type": "custom:mushroom-entity-card",
                    "layout": "vertical",
                    "entity": "button.ikuai_reconnect_wan",
                    "icon": "mdi:restart",
                    "icon_color": "green",
                    "secondary_info": "none"
                },
                {
                    "type": "custom:mushroom-entity-card",
                    "layout": "vertical",
                    "entity": "button.ikuai_restart",
                    "icon": "mdi:restore",
                    "secondary_info": "none"
                }
            ]
        },
        {
            "type": "custom:tabbed-card",
            "tabs": [
                {
                    "attributes": {"label": "实时"},
                    "card": {
                        "type": "vertical-stack",
                        "cards": [
                            {
                                "type": "custom:button-card",
                                "show_icon": false,
                                "show_state": false,
                                "show_name": false,
                                "styles": {
                                    "grid": [
                                        {"grid-template-areas": '"a b" "c c"'},
                                        {"grid-template-columns": "1fr 1fr"},
                                        {"grid-template-rows": "60px 1fr"}
                                    ],
                                    "card": [{"padding": "6px"}]
                                },
                                "custom_fields": {
                                    "a": {
                                        "card": {
                                            "type": "custom:mushroom-template-card",
                                            "primary": "{{states('sensor.ikuai_cpu')}} %",
                                            "secondary": "CPU",
                                            "icon": "mdi:cpu-64-bit",
                                            "icon_color": "green",
                                            "entity": "sensor.synology_nas_cpu_utilization_total",
                                            "card_mod": {"style": "ha-card { background: none; border: none; box-shadow: none; } :host { text-align: left; }"}
                                        }
                                    },
                                    "b": {
                                        "card": {
                                            "type": "custom:mushroom-template-card",
                                            "primary": "{{states('sensor.ikuai_memory')}}%",
                                            "secondary": "Memory",
                                            "icon": "mdi:memory",
                                            "entity": "sensor.synology_nas_memory_usage_real",
                                            "icon_color": "indigo",
                                            "card_mod": {"style": "ha-card { background: none; border: none; box-shadow: none; } :host { text-align: left; }"}
                                        }
                                    },
                                    "c": {
                                        "card": {
                                            "type": "custom:mini-graph-card",
                                            "entities": [
                                                {"entity": "sensor.ikuai_cpu", "name": "CPU", "icon": "mdi:cpu-64-bit", "color": "var(--green-color)"},
                                                {"entity": "sensor.ikuai_memory", "name": "Memory", "icon": "mdi:memory", "color": "var(--indigo-color)"}
                                            ],
                                            "line_width": 3,
                                            "font_size": 50,
                                            "hours_to_show": 1,
                                            "points_per_hour": 4,
                                            "show": {"name_adaptive_color": true, "icon": false, "name": false, "state": false, "legend": false, "fill": "fade"}
                                        }
                                    }
                                }
                            },
                            {
                                "type": "vertical-stack",
                                "cards": [
                                    {
                                        "type": "horizontal-stack",
                                        "cards": [
                                            {
                                                "type": "custom:mushroom-entity-card",
                                                "entity": "sensor.ikuai_connect_num",
                                                "icon": "mdi:lan-connect",
                                                "icon_color": "deep-orange",
                                                "layout": "horizontal",
                                                "primary_info": "state",
                                                "secondary_info": "name",
                                                "fill_container": false
                                            },
                                            {
                                                "type": "custom:mushroom-entity-card",
                                                "entity": "sensor.ikuai_online_user",
                                                "icon": "mdi:console-network-outline",
                                                "primary_info": "state",
                                                "secondary_info": "name"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "horizontal-stack",
                                        "cards": [
                                            {
                                                "type": "custom:mini-graph-card",
                                                "entities": [{"entity": "sensor.ikuai_upload"}]
                                            },
                                            {
                                                "type": "custom:mini-graph-card",
                                                "entities": [{"entity": "sensor.ikuai_download"}]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                },
                {
                    "attributes": {"label": "总量"},
                    "card": {
                        "type": "vertical-stack",
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "primary": "{% set total_ap = 3 %}\n{% set online_ap = states('sensor.ikuai_ap_online') | int %}\n{% set offline_ap = total_ap - online_ap %}\n{% if offline_ap > 0 %}\n  {{ states('sensor.ikuai_ap_online') }} 台，注意：{{ offline_ap }} 台设备已掉线\n{% else %}\n  {{ states('sensor.ikuai_ap_online') }} 台设备，全部在线\n{% endif %}",
                                "secondary": "AP数量",
                                "icon": "mdi:access-point",
                                "entity": "sensor.ikuai_ap_online",
                                "icon_color": "blue"
                            },
                            {
                                "type": "custom:button-card",
                                "show_icon": false,
                                "show_state": false,
                                "show_name": false,
                                "styles": {
                                    "grid": [
                                        {"grid-template-areas": '"a b" "c c"'},
                                        {"grid-template-columns": "1fr 1fr"},
                                        {"grid-template-rows": "60px 1fr"}
                                    ],
                                    "card": [{"padding": "6px"}]
                                },
                                "custom_fields": {
                                    "a": {
                                        "card": {
                                            "type": "custom:mushroom-template-card",
                                            "primary": "{% set total_up = states('sensor.ikuai_totalup') | float %}\n\n{% if total_up < 1024 %}\n  {{ '%.2f GB' | format(total_up) }}\n{% else %}\n  {{ '%.2f TB' | format(total_up / 1024) }}\n{% endif %}",
                                            "secondary": "上传总量",
                                            "icon": "mdi:upload-network",
                                            "icon_color": "green",
                                            "entity": "sensor.ikuai_totalup",
                                            "card_mod": {"style": "ha-card { background: none; border: none; box-shadow: none; } :host { text-align: left; }"}
                                        }
                                    },
                                    "b": {
                                        "card": {
                                            "type": "custom:mushroom-template-card",
                                            "primary": "{% set total_up = states('sensor.ikuai_totaldown') | float %}\n\n{% if total_up < 1024 %}\n  {{ '%.2f GB' | format(total_up) }}\n{% else %}\n  {{ '%.2f TB' | format(total_up / 1024) }}\n{% endif %}",
                                            "secondary": "下载总量",
                                            "icon": "mdi:download-network",
                                            "icon_color": "indigo",
                                            "entity": "sensor.ikuai_totaldown",
                                            "card_mod": {"style": "ha-card { background: none; border: none; box-shadow: none; } :host { text-align: left; }"}
                                        }
                                    },
                                    "c": {
                                        "card": {
                                            "type": "custom:mini-graph-card",
                                            "entities": [
                                                {"entity": "sensor.ikuai_totalup", "name": "上传", "icon": "mdi:cpu-64-bit", "color": "var(--green-color)"},
                                                {"entity": "sensor.ikuai_totaldown", "name": "下载", "icon": "mdi:memory", "color": "var(--indigo-color)"}
                                            ],
                                            "line_width": 3,
                                            "font_size": 50,
                                            "show": {"name_adaptive_color": true, "icon": false, "name": false, "state": false, "legend": false, "fill": "fade"}
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    ]
}
