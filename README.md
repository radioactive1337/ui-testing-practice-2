# ui-testing-practice-2

Clone project from GIT with following command

```bash
git clone https://github.com/radioactive1337/ui-test-practice.git
cd ui-test-practice\tests
```

Install requirements

```bash
pip install -r requirements.txt
```

## Running tests

values for --driver=chrome/firefox

values for --headless=false/true

To run all tests with chrome

```bash
pytest
```

To run all tests with firefox and headless mode

```bash
pytest --headless=true driver=firefox
```

## Project Structure

#### Folders

| Name               | Desc                 |
|:-------------------|:---------------------|
| `pages`            | page_objects for  UI |
| `tests/`           | UI tests             |                       
| `tests/resources/` | necessary resources  |

#### Files

| Name               | Desc                                                 | 
|:-------------------|:-----------------------------------------------------|
| `conftest.py`      | pytest configuration                                 |
| `pytest.ini`       | pytest configuration                                 |
| `requirements.txt` | list of libraries which are required for the project |
