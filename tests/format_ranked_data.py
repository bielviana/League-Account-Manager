import json

with open("./lcu_responses/ranked.json", "r") as file:
    ranked_data = json.load(file)

if ranked_data['queueMap']['RANKED_SOLO_5x5']['wins'] + ranked_data['queueMap']['RANKED_SOLO_5x5']['losses'] == 0:
    wr_soloq = 0
else:
    wr_soloq = round(ranked_data['queueMap']['RANKED_SOLO_5x5']['wins'] * 100 / (ranked_data['queueMap']['RANKED_SOLO_5x5']['wins'] + ranked_data['queueMap']['RANKED_SOLO_5x5']['losses']), 2)

if ranked_data['queueMap']['RANKED_FLEX_SR']['wins'] + ranked_data['queueMap']['RANKED_FLEX_SR']['losses'] == 0:
    wr_flexq = 0
else:
    wr_flexq = round(ranked_data['queueMap']['RANKED_FLEX_SR']['wins'] * 100 / (ranked_data['queueMap']['RANKED_FLEX_SR']['wins'] + ranked_data['queueMap']['RANKED_FLEX_SR']['losses']), 2)

if ranked_data['queueMap']['RANKED_SOLO_5x5']['tier'].lower() != "none":
    soloq = "{} {} LP:{} {}%(W:{} | L:{})".format(
        ranked_data['queueMap']['RANKED_SOLO_5x5']['tier'].capitalize(),
        ranked_data['queueMap']['RANKED_SOLO_5x5']['division'],
        ranked_data['queueMap']['RANKED_SOLO_5x5']['leaguePoints'],
        wr_soloq,
        ranked_data['queueMap']['RANKED_SOLO_5x5']['wins'],
        ranked_data['queueMap']['RANKED_SOLO_5x5']['losses']
    )
else:
    soloq = ""

if ranked_data['queueMap']['RANKED_FLEX_SR']['tier'].lower() != "none":
    flexq = "{} {} (W:{} | L:{})".format(
        ranked_data['queueMap']['RANKED_FLEX_SR']['tier'].capitalize(),
        ranked_data['queueMap']['RANKED_FLEX_SR']['division'],
        ranked_data['queueMap']['RANKED_FLEX_SR']['leaguePoints'],
        wr_flexq,
        ranked_data['queueMap']['RANKED_FLEX_SR']['wins'],
        ranked_data['queueMap']['RANKED_FLEX_SR']['losses']
    )
else:
    flexq = ""

print('SoloQ: {}\nFlexQ: {}'. format(soloq, flexq))
