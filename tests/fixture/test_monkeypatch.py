import json
import os

config = {
    'mirrors': ['https://xxxx.mirrors.ustc.edu.cn/']
}


def dump_config(config):
    path = os.path.expanduser('~/.conf.json')
    with open(path, 'w', encoding='utf-8') as wr:
        json.dump(config, wr, indent=4)


# def test_config():
#     dump_config(config)
#     path = os.path.expanduser('~/.conf.json')
#     expected = json.load(open(path, 'r', encoding='utf-8'))
#     assert expected == config


def test_config_monkeypatch(tmpdir, monkeypatch):
    monkeypatch.setenv('HOME', tmpdir.mkdir('home'))

    dump_config(config)
    path = os.path.expanduser('~/.conf.json')
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config

def test_config_monkeypatch2(tmpdir, monkeypatch):
    fake_home = tmpdir.mkdir('home')
    monkeypatch.setattr(os.path, 'expanduser',
                        lambda x: x.replace('~', str(fake_home)))
    dump_config(config)
    path = os.path.expanduser('~/.conf.json')
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config
