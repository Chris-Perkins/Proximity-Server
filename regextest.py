import re

urlRegex = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

print(urlRegex.match('htps://answers.yahoo.com/question/index?qid=20110712025012AAto9sv'))