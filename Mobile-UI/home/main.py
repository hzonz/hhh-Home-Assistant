#天气图标只支持和风天气iocn,可前往下载"https://github.com/qwd/Icons/releases/download/v1.6.0/QWeather-Icons-1.6.0.zip"
#把icon文件夹 放入www文件夹下，具体路径/local/weather_icons
if card_type == "主要信息卡片-hhh":
  card = {
        "type": "custom:button-card",
        "show_icon": False,
        "show_state": False,
        "show_name": False,
        "styles": {
            "grid": [
                {"grid-template-areas": '"a a b b" "c c c c" "d e f g"'},
                {"grid-template-columns": "1fr 1fr 1fr 1fr"},
                {"grid-template-rows": "45px min-content max-content"}
            ],
            "card": [{"padding": "10px"}]
        },
        "custom_fields": {
            "a": {
                "card": {
                    "type": "custom:mushroom-chips-card",
                    "chips": [
                        {
                            "type": "entity",
                            "entity": "person.zonzlee",
                            "content_info": "none",
                            "use_entity_picture": True,
                            "tap_action": {
                                "action": "fire-dom-event",
                                "browser_mod": {
                                    "service": "browser_mod.popup",
                                    "data": {
                                        "title": "Sarah",
                                        "content": {
                                            "type": "vertical-stack",
                                            "cards": [
                                                {
                                                    "type": "custom:mushroom-person-card",
                                                    "entity": "person.zonzlee",
                                                    "icon_type": "entity-picture"
                                                }
                                            ]
                                        }
                                    }
                                }
                            },
                            "card_mod": {
                                "style": """
                                    /* Show colored border around avatar based on person state */
                                    ha-card {
                                        --chip-background: 
                                        {% if is_state(config.entity, ['home', 'not_home', 'unknown']) %}
                                            rgb(var(--rgb-state-person-{{ states(config.entity) | replace('_', '-') }} ))
                                        {% else %}
                                            rgb(var(--rgb-state-person-zone))
                                        {% endif %};
                                    }
                                    /* Enlarge slightly and bring to front on hover */
                                    ha-card:hover {
                                        transform: scale(1.2);
                                        transform-origin: top center;
                                        z-index: 1;
                                        transition: all 1s;
                                    }
                                """
                            }
                        }
                    ],
                    "alignment": "end",
                    "card_mod": {
                        "style": """
                            ha-card { 
                                /* Overlap avatars */
                                margin-left: 1%;
                                --chip-spacing: calc(-1 * var(--mush-chip-spacing, 8px));
                                /* Set border size around avatars */
                                --chip-avatar-padding: 1px;
                                /* Decrease width to fit chips and leave maximum space for weather */
                                width: fit-content;
                                transition: all 0s;
                            }
                        """
                    }
                }
            },
            "b": {
                "card": {
                    "type": "custom:button-card",
                    "entity": "weather.tian_qi",
                    "name": """
                        [[[
                            var temperature = states['weather.tian_qi'].attributes['temperature'];
                            return temperature.toFixed(1) + '℃';
                        ]]]
                    """,
                    "entity_picture": """
                        [[[
                            var iconCode = states['weather.tian_qi'].attributes.qweather_icon;
                            var iconPath = '/local/weather_icons/icons/' + iconCode + '.svg';
                            return iconPath;
                        ]]]
                    """,
                    "show_icon": True,
                    "show_state": True,
                    "show_name": True,
                    "show_label": False,
                    "show_entity_picture": True,
                    "styles": {
                        "grid": [{"grid-template-areas": '"n i" "s i"'}],
                        "card": [
                            {"background": "none"},
                            {"border": "none"},
                            {"box-shadow": "none"},
                            {"margin-left": "'-5%'"},
                            {"border-radius": "0px  !important"}
                        ],
                        "name": [
                            {"align-self": "center"},
                            {"justify-self": "end"},
                            {"font-size": "15px"},
                            {"font-weight": "bold"},
                            {"letter-spacing": "1px"}
                        ],
                        "state": [
                            {"align-self": "end"},
                            {"justify-self": "end"},
                            {"font-size": "13px"},
                            {"margin-bottom": "10px"}
                        ],
                        "entity_picture": [
                            {"justify-self": "center"},
                            {"width": "35px"},
                            {"margin-left": "10px"},
                            {"margin-bottom": "10px"}
                        ]
                    }
                }
            },
            "c": {
                "card": {
                    "type": "custom:mushroom-title-card",
                    "title": """
                        {% set time = now().hour %}
                        {% if (time >= 18) %} 
                            晚上好,{{ user }}!
                        {% elif (time >= 12) %}
                            下午好,{{ user }}!
                        {% elif (time >= 5) %}
                            上午好,{{ user }}!
                        {% else %}
                            你好,{{ user }}!
                        {% endif %}
                    """,
                    "subtitle": """
                        {% set date_str = states('sensor.date') %}
                        {% set date_obj = strptime(date_str, '%Y-%m-%d') %}
                        {{ date_obj.month }}月{{ date_obj.day }}号
                        {{ state_attr('sensor.nong_li', 'week') }}
                        {{ states('sensor.nong_li') }}  
                        {{ state_attr('sensor.nong_li', 'nianganzhi') }}
                        {{ state_attr('sensor.nong_li', 'yueganzhi') }}
                        {{ state_attr('sensor.nong_li', 'riganzhi') }}
                    """,
                    "alignment": "start",
                    "subtitle_tap_action": {
                        "action": "navigate",
                        "navigation_path": "/dashboard-cellphone/Lunar",
                        "scroll_target": "card_1"
                    },
                    "card_mod": {
                        "style": """
                            ha-card {
                                --title-font-size: 20px;
                                --title-font-weight: bold;
                                --subtitle-font-size: 13px;
                            }
                        """
                    }
                }
            },
            "d": {
                "card": {
                    "type": "custom:mushroom-template-card",
                    "icon": "mdi:home-account",
                    "secondary": "模式",
                    "layout": "vertical",
                    "tap_action": {
                        "action": "navigate",
                        "navigation_path": "/dashboard-cellphone/device"
                    },
                    "card_mod": {
                        "style": """
                            ha-card { 
                                /* background: var(--card-background-color) !important; */
                                box-shadow: var(--ha-card-box-shadow) !important;
                                width: 62px;
                                --spacing: 8px;
                                {{ 'padding-bottom: calc(var(--spacing) * 1.618) !important;' if config.secondary != '' }}
                                border-radius: calc(var(--ha-card-border-radius, 12px) * 2) !important;
                                margin-left: auto;
                                margin-right: auto;
                            }
                        """
                    }
                }
            },
            "e": {
                "card": {
                    "type": "custom:mushroom-template-card",
                    "entity": "light.living_room_lamp",
                    "secondary": """
                        {% set all = expand('light.living_room_lamp')| list -%}
                        {% set ND1 = all | selectattr('state','eq','on')|list|count %}
                        {% set D1 = all | selectattr('state','eq','off')|list|count %}
                        {{ ND1 }}盏灯
                    """,
                    "icon": "mdi:lightbulb-group-outline",
                    "layout": "vertical",
                    "icon_color": "orange",
                    "tap_action": {
                        "action": "navigate",
                        "navigation_path": "/dashboard-cellphone/light"
                    },
                    "card_mod": {
                        "style": """
                            ha-card { 
                                /* background: var(--card-background-color) !important; */
                                box-shadow: var(--ha-card-box-shadow) !important;
                                width: 62px;
                                --spacing: 8px;
                                {{ 'padding-bottom: calc(var(--spacing) * 1.618) !important;' if config.secondary != '' }}
                                border-radius: calc(var(--ha-card-border-radius, 12px) * 2) !important;
                                margin-left: auto;
                                margin-right: auto;
                            }
                        """
                    }
                }
            },
            "f": {
                "card": {
                    "type": "custom:mushroom-template-card",
                    "primary": "",
                    "secondary": "设备",
                    "icon": "mdi:nas",
                    "layout": "vertical",
                    "icon_color": "indigo",
                    "tap_action": {
                        "action": "navigate",
                        "navigation_path": "/dashboard-cellphone/device"
                    },
                    "card_mod": {
                        "style": """
                            ha-card { 
                                /* background: var(--card-background-color) !important; */
                                box-shadow: var(--ha-card-box-shadow) !important;
                                width: 62px;
                                --spacing: 8px;
                                {{ 'padding-bottom: calc(var(--spacing) * 1.618) !important;' if config.secondary != '' }}
                                border-radius: calc(var(--ha-card-border-radius, 12px) * 2) !important;
                                margin-left: auto;
                                margin-right: auto;
                            }
                        """
                    }
                }
            },
            "g": {
                "card": {
                    "type": "custom:mushroom-template-card",
                    "primary": "",
                    "secondary": "网络",
                    "icon": "mdi:network-outline",
                    "layout": "vertical",
                    "icon_color": "cyan",
                    "tap_action": {
                        "action": "navigate",
                        "navigation_path": "/dashboard-cellphone/lan"
                    },
                    "card_mod": {
                        "style": """
                            ha-card { 
                                /* background: var(--card-background-color) !important; */
                                box-shadow: var(--ha-card-box-shadow) !important;
                                width: 62px;
                                --spacing: 8px;
                                {{ 'padding-bottom: calc(var(--spacing) * 1.618) !important;' if config.secondary != '' }}
                                border-radius: calc(var(--ha-card-border-radius, 12px) * 2) !important;
                                margin-left: auto;
                                margin-right: auto;
                            }
                        """
                    }
                }
            }
        }
    }
]

