import sys
import subprocess
import re
from github import Github, Issue

githubAPIToken = sys.argv[1]

g = Github(githubAPIToken)
repo = g.get_repo("TechSmith/CamtasiaWin")
pulls = repo.get_pulls(state='open', sort='created', base='develop')

for pr in pulls:
    if "dependabot" in pr.user.login: 
        print(pr.number)
        issuecomments = pr.get_issue_comments()
        if issuecomments.totalCount == 0:
            x = re.findall(r"Bump CommonCpp from `(.......)` to `(.......)`", pr.title)
            print(pr.title)
            if len(x) > 0:
                result = subprocess.run(['/usr/bin/pwsh', '-Command', './prsSinceCommit.ps1', 'CommonCpp', x[0][0], x[0][1], '-FindRisk' ], universal_newlines=True, stdout=subprocess.PIPE)
                message = "A.J. here.  This is an automated comment. :smiley:\n" + result.stdout
                print(message)
                issuecomment = pr.create_issue_comment(message)
                issuecomment.create_reaction("laugh")
                issuecomment.create_reaction("heart")
                issuecomment.create_reaction("hooray")
                issuecomment.create_reaction("rocket")

sys.exit("done testing")


