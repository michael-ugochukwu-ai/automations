import os
from jira import JIRA
from jira.resources import Issue

def main():
    jira_user = os.environ["JIRA_USER"]
    jira_url = os.environ["JIRA_URL"]
    jira_key = os.environ["JIRA_TICKET_KEY"]
    jira_token = os.environ["JIRA_TOKEN"]
    jira_client= JIRA(server=jira_url, basic_auth=(jira_user, jira_token))
    issue = jira_client.search_issues(f"key = '{jira_key}'")[0]
    change_status(jira_client, issue, )


def change_status(client: JIRA, issue: Issue, destination_status:str = "complete"):
    transitions = client.transitions(issue)
    transition_id = 0
    for transition in transitions:
        if destination_status in transition['name'].lower():
            transition_id = transition['id']
            break
    client.transition_issue(issue, transition_id)

    

if __name__ == "__main__":
    # pass # do nothing
    # main()
    jira_user = os.environ["JIRA_USER"]
    jira_url = os.environ["JIRA_URL"]
    jira_key = os.environ["JIRA_TICKET_KEY"]
    jira_token = os.environ["JIRA_TOKEN"] # Hasn't been set ever even at this point
    print(jira_url)
    print(jira_user)
    print(jira_token)
    print(jira_key)