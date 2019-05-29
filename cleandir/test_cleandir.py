from pathlib import Path

from cleandir import cleandir


@pytest.mark.skip(reason=​'integration test'​)
def test_get_path_abs(monkeypatch):
    """Test the get_path_to_clean func using an absolute path"""
    monkeypatch.setattr("builtins.input", lambda x: 'C:\\')
    abs_path = cleandir.get_path_to_clean()
    assert str(abs_path) == "C:\\"
    assert abs_path.is_absolute()

@pytest.mark.skip(reason=​'integration test'​)
def test_get_path_rel(monkeypatch):
    """Test the get_path_to_clean func using a relative path"""
    monkeypatch.setattr("builtins.input", lambda x: r'.\cleandir\fortests')
    rel_path = cleandir.get_path_to_clean()
    assert str(rel_path) == r'cleandir\fortests'


def test_get_path_exit(monkeypatch):
    """test that no input exits the program"""
    monkeypatch.setattr("builtins.input", lambda x: '')
    try:
        cleandir.get_path_to_clean()
    except SystemExit as e:
        assert e == 'user initiated exit'


def test_get_extensions_on_fortests():
    """Test hte get extension function on the fortests directory.  It should return a set that includes csv and txt"""
    p = Path(r'.\cleandir\fortests')
    files_in_p = list()
    for i in p.iterdir():
        if i.is_file():
            files_in_p.append(i)
    ext_list1 = ['csv', 'txt']
    ext_list2 = cleandir.get_extensions(files_in_p)
    assert set(ext_list1) == ext_list2
