import os
from jira import JIRA

def main():
    jira_user = os.environ["JIRA_USER"]
    jira_url = os.environ["JIRA_URL"]
    jira_key = os.environ["JIRA_TICKET_KEY"]
    jira_token = os.environ["JIRA_TOKEN"]

    jira_client= JIRA(server=jira_url, auth=(jira_user, jira_token))

    issue = jira_client.search_issues(f"key = '{jira_key}'")[0]
    issue.update(status="COMPLETE")
    

if __name__ == "__main__":
    pass # do nothing