import pytest
import selenium.webdriver
import json
import pytest

@pytest.fixture
def browser(config):
    #init chrome driver instance
    if config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome(executable_path=r"D:\Innowise\PY\TAU\driver\chromedriver.exe")
    elif config['browser'] == 'Headless Chrome':
        opt = selenium.webdriver.ChromeOptions()
        opt.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opt, executable_path=r"D:\Innowise\PY\TAU\driver\chromedriver.exe")
    else:
        raise Exception(f"browser {config['browser']} is not supported")
    #setup wait up to 10 sec
    driver.implicitly_wait(config['implicit'])

    #return driver instance
    yield driver

    #quit driver
    driver.quit()


@pytest.fixture()
def config(scope='session'):
    with open('config.json') as config_file:
        conf = json.load(config_file)

    assert conf['browser'] in ['Chrome', 'Firefox', 'Headless Chrome']
    assert isinstance(conf['implicit'], int)
    assert conf['implicit'] > 0
    return conf

