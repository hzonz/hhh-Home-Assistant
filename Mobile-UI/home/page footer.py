if card_type == "dock栏卡片-hhh":
  card = {
    "type": "custom:mod-card",
    "card": {
        "type": "custom:button-card",
        "show_icon": False,
        "show_state": False,
        "show_name": False,
        "shoe_label": False,
        "styles": {
            "grid": [
                {"grid-template-areas": '"a b c" '},
                {"grid-template-columns": "1fr 1fr 1fr"},
                {"grid-template-rows": "50px"}
            ],
            "card": [{"padding": "px"}]
        },
        "custom_fields": {
            "a": {
                "card": {
                    "type": "custom:button-card",
                    "name": "主页",
                    "icon": "mdi:home-outline",
                    "show_icon": True,
                    "show_name": True,
                    "show_state": False,
                    "show_label": False,
                    "tap_action": {
                        "action": "navigate",
                        "navigation_path": "/dashboard-cellphone/home"
                    },
                    "styles": {
                        "grid": [{"grid-template-areas": '"i" "n"'}],
                        "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                        "img_cell": [{"align-self": "start"}, {"justify-self": "center"}, {"height": "25px"}],
                        "name": [{"align-self": "start"}, {"justify-self": "center"}, {"font-size": "12px"}]
                    }
                }
            },
            "b": {
                "card": {
                    "type": "custom:button-card",
                    "name": "区域",
                    "icon": "mdi:door",
                    "show_icon": True,
                    "show_name": True,
                    "show_state": False,
                    "show_label": False,
                    "tap_action": {
                        "action": "navigate",
                        "navigation_path": "/dashboard-cellphone/region"
                    },
                    "styles": {
                        "grid": [{"grid-template-areas": '"i" "n"'}],
                        "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                        "img_cell": [{"align-self": "start"}, {"justify-self": "center"}, {"height": "25px"}],
                        "name": [{"align-self": "start"}, {"justify-self": "center"}, {"font-size": "12px"}]
                    }
                }
            },
            "c": {
                "card": {
                    "type": "custom:button-card",
                    "name": "我的",
                    "icon": "mdi:account-outline",
                    "show_icon": True,
                    "show_name": True,
                    "show_state": False,
                    "show_label": False,
                    "tap_action": {
                        "action": "navigate",
                        "navigation_path": "/dashboard-cellphone/More"
                    },
                    "styles": {
                        "grid": [{"grid-template-areas": '"i" "n"'}],
                        "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                        "img_cell": [{"align-self": "start"}, {"justify-self": "center"}, {"height": "25px"}],
                        "name": [{"align-self": "start"}, {"justify-self": "center"}, {"font-size": "12px"}]
                    }
                }
            }
        }
    },
    "card_mod": {
        "style": """
:host {
  z-index: 5;
  position: sticky;
  bottom: 0;
}
ha-card {    
  padding-bottom: 0px;
  margin: 0px auto;  /*居中*/
  width: calc(100% - 40px); /* 适应屏幕并在左右两侧留有 20px 的预留空间 */
  border-radius: 16px;
}
"""
    }
}
