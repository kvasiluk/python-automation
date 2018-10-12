## python-automation

#### Status badge
[![CircleCI](https://circleci.com/gh/kvasiluk/python-automation/tree/master.svg?style=svg)](https://circleci.com/gh/kvasiluk/python-automation/tree/master)

#### Intro
Project for Lohika Python automation training course

#### Technologies

- **pytest**: Main testing tool
- **Requests**: HTTP library for Python
- **Jsonschema**: Vocabulary that allows to annotate and validate JSON documents
- **pytest-rerunfailures**: Plugin for py.test that re-runs tests to eliminate intermittent failures
- **pytest-xdist**: Test run parallelization
- **Selenium** : Framework for UI testing
- **webdriver-manager**: A selenium server and browser driver manager for end to end tests
- **Allure** : framework designed to create test execution reports that are clear to everyone in the team

#### Running automation tests locally

##### Pre-requisites:

Access to `http://jira.hillel.it:8080/`  
Google Chrome installed on local host 

```
➜ python --version
Python 3.6.5

➜ pip --version
pip 10.0.1 from [...] (python 3.6)

```

```
➜ pip install -r ./requirements.txt
```

```
➜ sudo apt-add-repository ppa:qameta/allure
➜ sudo apt-get update 
➜ sudo apt-get install allure
```

##### Run UI tests:

```
➜ python -m pytest ui_tests -v --alluredir=test_results/allure
```

##### Run API tests:

```
➜ python -m pytest api_tests -v
```

##### Open report:

```
➜ allure serve ./test-results/allure
```
