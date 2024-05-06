# 使用hhh本地计算万年历流程，不用更改实体ID。
if card_type == "农历卡片-hhh":
  card = {
    "type": "custom:button-card",
    "show_icon": True,
    "show_state": True,
    "show_name": False,
    "styles": {
        "grid": [
            {"grid-template-areas": ' "a b f g g"  "a c h i i"  "a d j k k"  "a e l m n"  "o p p p p"  "q r r r r" "s t t t t"  "u v v v v" "w x x x x" "y z z z z"'},
            {"grid-template-columns": "70px 20px 1fr 1fr 1fr"},
            {"grid-template-rows": ">- 75px 75px 75px 75px max-content max-content max-content max-content max-content"}
        ],
        "card": [{"padding": "8px"}]
    },
    "custom_fields": {
        "a": {
            "card": {
                "type": "custom:button-card",
                "entity": "sensor.nong_li",
                "show_icon": False,
                "show_name": False,
                "show_state": True,
                "show_label": False,
                "styles": {
                    "grid": [{"height": "300px"}],
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "state": [{"writing-mode": "vertical-lr"}, {"font-weight": "bold"}, {"font-size": "26px"}, {"letter-spacing": "10px"}]
                }
            }
        },
        "b": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['nianganzhi']; return price;",
                "styles": {
                    "card": [{"margin-top": "10px"}, {"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"writing-mode": "vertical-lr"}, {"font-weight": "lighter"}, {"font-size": "12px"}, {"letter-spacing": "5px"}]
                }
            }
        },
        "c": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['yueganzhi']; return price;",
                "styles": {
                    "card": [{"margin-top": "10px"}, {"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"writing-mode": "vertical-lr"}, {"font-weight": "lighter"}, {"font-size": "12px"}, {"letter-spacing": "5px"}]
                }
            }
        },
        "d": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['riganzhi']; return price;",
                "styles": {
                    "card": [{"margin-top": "10px"}, {"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"writing-mode": "vertical-lr"}, {"font-weight": "lighter"}, {"font-size": "12px"}, {"letter-spacing": "5px"}]
                }
            }
        },
        "e": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['week']; return price;",
                "styles": {
                    "card": [{"margin-top": "10px"}, {"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"writing-mode": "vertical-lr"}, {"font-weight": "lighter"}, {"font-size": "12px"}, {"letter-spacing": "5px"}]
                }
            }
        },
        "f": {
            "card": {
                "type": "custom:button-card",
                "name": "五行",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"justify-self": "center"}, {"font-weight": "bold"}, {"font-size": "18px"}, {"letter-spacing": "3px"}]
                }
            }
        },
        "g": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['wuxingri']; return price;",
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "15px"}, {"letter-spacing": "3px"}]
                }
            }
        },
        "h": {
            "card": {
                "type": "custom:button-card",
                "name": "冲煞",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"justify-self": "center"}, {"font-weight": "bold"}, {"font-size": "18px"}, {"letter-spacing": "3px"}]
                }
            }
        },
        "i": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['chongsha']; return price;",
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "15px"}, {"letter-spacing": "3px"}]
                }
            }
        },
        "j": {
            "card": {
                "type": "custom:button-card",
                "entity": "sensor.peng_zu_gan",
                "name": "彭祖",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"justify-self": "center"}, {"font-weight": "bold"}, {"font-size": "18px"}, {"letter-spacing": "3px"}]
                }
            }
        },
        "k": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": True,
                "name": "var price = states['sensor.nong_li'].attributes['pengzugan']; return price;",
                "label": "var price = states['sensor.nong_li'].attributes['pengzuzhi']; return price;",
                "styles": {
                    "grid": [{"grid-template-areas": '"n" "l"'}],
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "15px"}, {"letter-spacing": "5px"}, {"white-space": "normal"}],
                    "label": [{"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "15px"}, {"letter-spacing": "5px"}, {"white-space": "normal"}]
                }
            }
        },
        "l": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": True,
                "name": "var price = states['sensor.nong_li'].attributes['xishen']; return price;",
                "label": "喜神",
                "styles": {
                    "grid": [{"grid-template-areas": '"n" "l"'}],
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"font-size": "14px"}, {"font-weight": "bold"}, {"letter-spacing": "4px"}],
                    "label": [{"font-weight": "lighter"}, {"font-size": "14px"}, {"letter-spacing": "3px"}]
                }
            }
        },
        "m": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": True,
                "name": "var price = states['sensor.nong_li'].attributes['fushen']; return price;",
                "label": "福神",
                "styles": {
                    "grid": [{"grid-template-areas": '"n" "l"'}],
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"font-size": "14px"}, {"font-weight": "bold"}, {"letter-spacing": "4px"}],
                    "label": [{"font-weight": "lighter"}, {"font-size": "14px"}, {"letter-spacing": "3px"}]
                }
            }
        },
        "n": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": True,
                "name": "var price = states['sensor.nong_li'].attributes['caishen']; return price;",
                "label": "财神",
                "styles": {
                    "grid": [{"grid-template-areas": '"n" "l"'}],
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"font-size": "14px"}, {"font-weight": "bold"}, {"letter-spacing": "4px"}],
                    "label": [{"font-weight": "lighter"}, {"font-size": "14px"}, {"letter-spacing": "3px"}]
                }
            }
        },
        "o": {
            "card": {
                "type": "custom:button-card",
                "name": "宜",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"width": "30px"}, {"height": "30px"}, {"background-color": "green"}, {"border-radius": "50%"}, {"justify-self": "end"}, {"display": "flex"}, {"justify-content": "center"}, {"align-items": "center"}, {"color": "white"}, {"font-size": "20px"}, {"line-height": "30px"}]
                }
            }
        },
        "p": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['yi']; return price;",
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"margin-left": "15px"}, {"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "13px"}, {"letter-spacing": "2px"}, {"white-space": "normal"}]
                }
            }
        },
        "q": {
            "card": {
                "type": "custom:button-card",
                "name": "忌",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"width": "30px"}, {"height": "30px"}, {"background-color": "red"}, {"border-radius": "50%"}, {"justify-self": "end"}, {"display": "flex"}, {"justify-content": "center"}, {"align-items": "center"}, {"color": "white"}, {"font-size": "20px"}, {"line-height": "30px"}]
                }
            }
        },
        "r": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['ji']; return price;",
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"margin-left": "15px"}, {"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "13px"}, {"letter-spacing": "2px"}, {"white-space": "normal"}]
                }
            }
        },
        "s": {
            "card": {
                "type": "custom:button-card",
                "name": "八字",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"justify-self": "end"}, {"font-weight": "bold"}, {"font-size": "18px"}]
                }
            }
        },
        "t": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['bazi']; return price;",
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"margin-left": "15px"}, {"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "13px"}, {"letter-spacing": "2px"}]
                }
            }
        },
        "u": {
            "card": {
                "type": "custom:button-card",
                "name": "胎神",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"justify-self": "end"}, {"font-weight": "bold"}, {"font-size": "18px"}]
                }
            }
        },
        "v": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['taishen']; return price;",
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"margin-left": "15px"}, {"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "13px"}, {"letter-spacing": "2px"}]
                }
            }
        },
        "w": {
            "card": {
                "type": "custom:button-card",
                "name": "吉神",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"justify-self": "end"}, {"font-weight": "bold"}, {"font-size": "18px"}]
                }
            }
        },
        "x": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['jishen']; return price;",
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"margin-left": "15px"}, {"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "13px"}, {"letter-spacing": "1px"}, {"white-space": "normal"}]
                }
            }
        },
        "y": {
            "card": {
                "type": "custom:button-card",
                "name": "凶神",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}, {"border-radius": "0px  !important"}],
                    "name": [{"justify-self": "end"}, {"font-weight": "bold"}, {"font-size": "18px"}]
                }
            }
        },
        "z": {
            "card": {
                "type": "custom:button-card",
                "show_icon": False,
                "show_name": True,
                "show_state": False,
                "show_label": False,
                "name": "var price = states['sensor.nong_li'].attributes['xiangzhen']; return price;",
                "styles": {
                    "card": [{"background": "none"}, {"border": "none"}, {"box-shadow": "none"}],
                    "name": [{"margin-left": "15px"}, {"font-weight": "lighter"}, {"justify-self": "start"}, {"font-size": "13px"}, {"letter-spacing": "1px"}]
                }
            }
        }
    }
}
