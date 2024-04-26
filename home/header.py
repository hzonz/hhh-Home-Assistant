if card_type == "页眉卡片1":
  card = {
    "type": "custom:mod-card",
    "card": {
        "type": "custom:button-card",
        "show_icon": False,
        "show_state": False,
        "show_name": False,
        "styles": {
            "grid": [
                {"grid-template-areas": '"a a b c"'},
                {"grid-template-columns": "1fr 3fr 1fr 1fr"},
                {"grid-template-rows": "1fr"}
            ],
            "card": [{"padding": "8px"}]
        },
        "custom_fields": {
            "a": {
                "card": {
                    "type": "custom:mushroom-chips-card",
                    "chips": [
                        {"type": "menu"}
                    ]
                }
            },
            "b": {
                "card": {
                    "type": "custom:mushroom-chips-card",
                    "chips": [
                        {
                            "type": "template",
                            "entity": "sensor.time",
                            "content": "{{ states(entity) }}",
                            "tap_action": {"action": "more-info"}
                        }
                    ]
                }
            },
            "c": {
                "card": {
                    "type": "custom:mushroom-chips-card",
                    "chips": [
                        {
                            "type": "template",
                            "entity": "sensor.shi_chen",
                            "content": "{{ states(entity) }}",
                            "tap_action": {"action": "more-info"}
                        }
                    ]
                }
            }
        }
    },
    "card_mod": {
        "style": """
            :host {
                z-index: 5;
                position: sticky;
                position: -webkit-sticky;
                top: 0;
            }
        """
    }
}
