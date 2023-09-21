import sys

lines = []
# Reading the files into a list
for line in sys.stdin:
    lines.append(line)

for line in lines:
    line = line.strip()
    user, password, userid, groupid = line.split(":")
    if user[0] == "#":
        # User4 is skipped because it starts with a hashtag (is commented out)
        print(f"{user} is skipped because it starts with a hashtag (is commented out)")
    else:
        # The user User3 has a password of Password3 and has userid 3 and groupid 3
        print(f"The user {user} has a password of {password} and has a userid {userid} and groupid {groupid}")

print("\nEnd of User Data")
