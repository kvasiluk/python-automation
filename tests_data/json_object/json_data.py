from api_tests.utils.config import Config


def create_issue_json(summary, description, type):
    return {
        "fields": {
            "project":
                {
                    "key": Config.project_key
                },
            "summary": summary,
            "description": description,
            "issuetype": {
                "name": type
            }
        }
    }


def update_issue_json(field, value):
    if field != 'summary':
        value = {"name": value}

    return {
             "fields": {
                 field: value
             }
         }
