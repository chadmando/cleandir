import cleandir


def test_get_path(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: 'C:\\Code')
    path = cleandir.get_path()
    assert str(path) == "C:\\Code"
