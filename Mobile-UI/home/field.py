if card_type == "信息组卡片-hhh":
  card = {
        "type": "template",
        "entity": "sensor.wen_shi_du_chuan_gan_qi_wen_du_zu",
        "content": "{{ states(entity, 'temperature') | round(1) }} °C",
        "icon": "mdi:thermometer",
        "icon_color": """
            {% set state = states(entity)| float %}
            {% if state > 30 %} red
            {% elif state > 20 %} yellow
            {% else %} green
            {% endif %}
        """,
        "tap_action": {
            "action": "fire-dom-event",
            "browser_mod": {
                "service": "browser_mod.popup",
                "data": {
                    "title": "全屋温度统计",
                    "content": {
                        "type": "custom:mini-graph-card",
                        "entities": [
                            {"entity": "sensor.wen_shi_du_chuan_gan_qi_wen_du_zu", "name": "平均"},
                            {"entity": "sensor.a4c13864fa00_temperature", "name": "客厅"},
                            {"entity": "sensor.a4c138162cdb_temperature", "name": "主卧"},
                            {"entity": "sensor.a4c1381117d0_temperature", "name": "次卧"},
                            {"entity": "sensor.a4c1381681dc_temperature", "name": "厨房"},
                            {"entity": "sensor.a4c138473153_temperature", "name": "卫生间"}
                        ]
                    }
                }
            }
        }
    },
    {
        "type": "template",
        "entity": "sensor.wen_shi_du_chuan_gan_qi_shi_du_zu",
        "content": "{{ states(entity, 'temperature') | round(1) }} %",
        "icon": "mdi:water-percent",
        "icon_color": """
            {% set state = states(entity)| float %}
            {% if state > 40 %} blue
            {% elif state > 20 %} yellow
            {% else %} red
            {% endif %}
        """,
        "tap_action": {
            "action": "fire-dom-event",
            "browser_mod": {
                "service": "browser_mod.popup",
                "data": {
                    "title": "全屋湿度统计",
                    "content": {
                        "type": "custom:mini-graph-card",
                        "entities": [
                            {"entity": "sensor.wen_shi_du_chuan_gan_qi_shi_du_zu", "name": "平均"},
                            {"entity": "sensor.a4c13864fa00_humidity", "name": "客厅"},
                            {"entity": "sensor.a4c138162cdb_humidity", "name": "主卧"},
                            {"entity": "sensor.a4c1381117d0_humidity", "name": "次卧"},
                            {"entity": "sensor.a4c1381681dc_humidity", "name": "厨房"},
                            {"entity": "sensor.a4c138473153_humidity", "name": "卫生间"}
                        ]
                    }
                }
            }
        }
    },
    {
        "type": "template",
        "entity": "sensor.quan_wu_guang_zhao_chuan_gan_qi_zu",
        "icon": "mdi:brightness-5",
        "icon_color": "yellow",
        "content": "'%.2f' | format(states(entity) | float) + ' lux'",
        "tap_action": {
            "action": "fire-dom-event",
            "browser_mod": {
                "service": "browser_mod.popup",
                "data": {
                    "title": "全屋光照统计",
                    "content": {
                        "type": "custom:mini-graph-card",
                        "entities": [
                            {"entity": "sensor.quan_wu_guang_zhao_chuan_gan_qi_zu", "name": "平均"},
                            {"entity": "sensor.d4f0eac67b4c_illuminance", "name": "餐厅"},
                            {"entity": "sensor.649e31818690_illuminance", "name": "书房"},
                            {"entity": "sensor.c85ccca76d87_illuminance", "name": "主卧"},
                            {"entity": "sensor.dced831119d9_illuminance", "name": "次卧"},
                            {"entity": "sensor.649e31887148_illuminance", "name": "厨房"},
                            {"entity": "sensor.c85ccca76d4b_illuminance", "name": "洗漱间"},
                            {"entity": "sensor.dced83111211_illuminance", "name": "卫生间"}
                        ]
                    }
                }
            }
        }
    },
    {
        "type": "template",
        "content": """
            {% if is_state('binary_sensor.quan_wu_men_chuang_chuan_gan_qi_zu', 'on') %}
                已开启
            {% else %}
                已关闭
            {% endif %}
        """,
        "entity": "binary_sensor.quan_wu_men_chuang_chuan_gan_qi_zu",
        "icon": """
            {% if is_state('binary_sensor.quan_wu_men_chuang_chuan_gan_qi_zu', 'on') %}
                mdi:door-open
            {% else %}
                mdi:door-closed
            {% endif %}
        """,
        "icon_color": "blue",
        "tap_action": {
            "action": "fire-dom-event",
            "browser_mod": {
                "service": "browser_mod.popup",
                "data": {
                    "title": "门窗传感器",
                    "content": {
                        "type": "grid",
                        "cards": [
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.e4aaec79181d_contact", "primary_info": "state", "secondary_info": "name", "name": "阳台窗户东"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.e4aaec79178c_contact", "primary_info": "state", "secondary_info": "name", "name": "阳台窗户西"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.e4aaec78dae3_contact", "primary_info": "state", "secondary_info": "name", "name": "主卧窗户"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.e4aaec791790_contact", "primary_info": "state", "secondary_info": "name", "name": "次卧窗户"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.e4aaec7566fb_contact", "primary_info": "state", "secondary_info": "name", "name": "主卧门"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.e4aaec7551d0_contact", "primary_info": "state", "secondary_info": "name", "name": "次卧门"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.zhu_wo_opening", "primary_info": "state", "secondary_info": "name", "name": "柜门"}
                        ],
                        "columns": 2,
                        "square": False
                    }
                }
            }
        }
    },
    {
        "type": "template",
        "entity": "binary_sensor.quan_wu_ren_ti_cun_zai_chuan_gan_qi_zu",
        "content": """
            {% if is_state(entity, 'on') %}
                有人
            {% else %}
                无人
            {% endif %}
        """,
        "icon": """
            {% if is_state(entity, 'on') %}
                mdi:motion-sensor
            {% else %}
                mdi:motion-sensor-off
            {% endif %}
        """,
        "icon_color": """
            {% if is_state(entity, 'on') %}
                yellow
            {% endif %}
        """,
        "tap_action": {
            "action": "fire-dom-event",
            "browser_mod": {
                "service": "browser_mod.popup",
                "data": {
                    "title": "人体存在检测",
                    "content": {
                        "type": "grid",
                        "cards": [
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.xuan_guan_ren_ti_jian_ce", "name": "玄关", "primary_info": "state", "secondary_info": "name"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.ke_ting_ren_ti_jian_ce", "name": "客厅", "primary_info": "state", "secondary_info": "name"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.xi_shu_chi_ren_ti_jian_ce", "name": "洗漱池", "primary_info": "state", "secondary_info": "name"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.wei_sheng_jian_ren_ti_jian_ce", "name": "卫生间", "primary_info": "state", "secondary_info": "name"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.chu_fang_ren_ti_jian_ce", "name": "厨房", "primary_info": "state", "secondary_info": "name"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.shu_fang_ren_ti_jian_ce", "name": "书房", "primary_info": "state", "secondary_info": "name"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.zhu_wo_ren_ti_jian_ce", "name": "主卧", "primary_info": "state", "secondary_info": "name"},
                            {"type": "custom:mushroom-entity-card", "entity": "binary_sensor.ci_wo_ren_ti_jian_ce", "name": "次卧", "primary_info": "state", "secondary_info": "name"}
                        ],
                        "columns": 2,
                        "square": False
                    }
                }
            }
        }
    },
    {
        "type": "conditional",
        "conditions": [
            {"condition": "state", "entity": "media_player.xiaomi_s12_2c15_play_control", "state": "playing"}
        ],
        "chip": {
            "type": "entity",
            "entity": "media_player.xiaomi_s12_2c15_play_control",
            "use_entity_picture": True
        }
    }
]
