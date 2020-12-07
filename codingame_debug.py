
import json
import requests


email = 'a.mezhenin@gmail.com'
pw = 'Password'
userID = 1393802  # that's my userID, you have to change it
game_id = 514018475

# the session object saves cookies
with requests.Session() as s:
    # let's login first
    p = s.post('https://www.codingame.com/services/CodingamerRemoteService/loginSiteV2', json=[email, pw, True])
    # the same request as above, but with a session object
    r = s.post('https://www.codingame.com/services/gameResultRemoteService/findByGameId', json=[str(game_id), userID])
    replay = r.json()

print(replay)
with open(f'{game_id}.json', 'w+') as f:
    f.write(json.dumps(replay))

exit()


# FIXME: merge with top part
import json

# read the replay from file
with open('replay.json', 'r') as f:
    replay = json.loads(f.read())

stderr = []
for frame in replay['success']['frames']:
    if not 'stderr' in frame.keys():
        continue
    for err in frame['stderr'].split('\n'):
        # some of my stderr lines aren't referee input. I marked them with '#' to filter them
        # FIXME: write log function in special format + replace `input` with input+log
        if not err.startswith('#'):
            stderr.append(err)

# write the errorstream to the file 'input.txt'
# `< input.txt` this is how it can be used as argument`
with open('input.txt', 'w+') as f:
    f.write('\n'.join(stderr))
print('\n'.join(stderr))

