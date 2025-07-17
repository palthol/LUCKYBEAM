from lbeam import presets

def test_webdev_preset_defined():
    p = presets.PRESETS.get("WebDev")
    assert isinstance(p, dict)
    assert "keywords" in p
    assert "extensions" in p
    assert isinstance(p["keywords"], list)
