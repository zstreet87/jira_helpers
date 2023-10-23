from bs4 import BeautifulSoup
import argparse
from jira import JIRA


def search_jira_key(jira_url, username, password, issue_key):
    jira = JIRA(server=jira_url, basic_auth=(username, password))

    try:
        issue = jira.issue(issue_key)

        print(f"Issue Key: {issue.key}")
        print(f"Type: {issue.fields.issuetype}")
        print(f"Priority: {issue.fields.priority}")
        print(f"Summary: {issue.fields.summary}")
        print(f"Assignee: {issue.fields.assignee}")
        description = BeautifulSoup(str(issue.fields.description), "html.parser")
        print(description.prettify())
        # Add more fields as needed

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for Jira issues by key.")
    parser.add_argument("jira_url", help="The Jira instance URL")
    parser.add_argument("username", help="Your Jira username")
    parser.add_argument("password", help="Your Jira password")
    parser.add_argument(
        "issue_key",
        help="The issue key to search for. For example, SWDEV-404384",
    )
    args = parser.parse_args()
    search_jira_key(args.jira_url, args.username, args.password, args.issue_key)
