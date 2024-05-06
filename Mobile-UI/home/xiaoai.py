if card_type == "小爱音响卡片-hhh":
  card = {
        "type": "custom:mushroom-media-player-card",
        "entity": "media_player.xiaomi_s12_2c15_play_control",
        "use_media_info": True,
        "show_volume_level": True,
        "media_controls": ["on_off", "shuffle", "previous", "play_pause_stop", "next", "repeat"],
        "volume_controls": ["volume_mute"],
        "collapsible_controls": True,
        "icon_type": "entity-picture",
        "fill_container": False
    },
    {
        "type": "entities",
        "entities": [
            {"entity": "text.xiaomi_s12_2c15_execute_text_directive"}
        ],
        "show_header_toggle": False
    }
]
