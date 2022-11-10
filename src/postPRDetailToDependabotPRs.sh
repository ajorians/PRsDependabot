cd /home/ajorians/temp

githubtoken=`cat githubtoken.txt`

cd /home/ajorians/scripts/PRsDependabot/src

python3.8 postPRDetailToDependabotPRs.py "$githubtoken"
