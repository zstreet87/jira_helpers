import argparse

from jira import JIRA


def search_jira_issues(jira_url, username, password, pattern, status):
    jira = JIRA(server=jira_url, basic_auth=(username, password))

    jql_query = f'summary ~ "{pattern}"'

    issues = jira.search_issues(
        jql_query, maxResults=False
    )  # Set maxResults to False to get all issues

    anything_printed = False
    print(f"Looking for {status} {pattern} Issues...")
    for issue in issues:
        if str(issue.fields.status) == status:
            print(
                f"Issue Key: {issue.key}, Summary: {issue.fields.summary}, Status: {issue.fields.status}"
            )
            anything_printed = True

    if not anything_printed:
        print(f"Couldn't find any {status} {pattern} Issues!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search for Jira issues with titles matching a specified pattern."
    )
    parser.add_argument("jira_url", help="The Jira instance URL")
    parser.add_argument("username", help="Your Jira username")
    parser.add_argument("password", help="Your Jira password")
    parser.add_argument(
        "--pattern",
        help="The pattern to search for in issue titles. Format 'pattern=Issue', for example",
        nargs=1,
    )
    parser.add_argument(
        "--status",
        help="Specify the status as of ticket",
        choices=[
            "Implemented",
            "Analyzed",
            "Assessed",
            "Closed",
            "Rejected",
            "Opened",
            "Done",
            # TODO: should also have an "ALL" status that prints all statuses
        ],
        nargs=1,
    )
    args = parser.parse_args()
    pattern = args.pattern[0]
    status = args.status[0]
    search_jira_issues(args.jira_url, args.username, args.password, pattern, status)
