class GetRankedData():
    def __init__(self, ranked_data) -> None:
        self.ranked_data = ranked_data

    def soloq(self):
        if self.ranked_data['queueMap']['RANKED_SOLO_5x5']['wins'] + self.ranked_data['queueMap']['RANKED_SOLO_5x5']['losses'] == 0:
            wr_soloq = 0
        else:
            wr_soloq = round(self.ranked_data['queueMap']['RANKED_SOLO_5x5']['wins'] * 100 / (self.ranked_data['queueMap']['RANKED_SOLO_5x5']['wins'] + self.ranked_data['queueMap']['RANKED_SOLO_5x5']['losses']), 2)

        if self.ranked_data['queueMap']['RANKED_SOLO_5x5']['tier'].lower() != "none":
            soloq = "{} {} LP:{} {}%(W:{} | L:{})".format(
                self.ranked_data['queueMap']['RANKED_SOLO_5x5']['tier'].capitalize(),
                self.ranked_data['queueMap']['RANKED_SOLO_5x5']['division'],
                self.ranked_data['queueMap']['RANKED_SOLO_5x5']['leaguePoints'],
                wr_soloq,
                self.ranked_data['queueMap']['RANKED_SOLO_5x5']['wins'],
                self.ranked_data['queueMap']['RANKED_SOLO_5x5']['losses']
            )
        else:
            soloq = "Unranked"
        
        return soloq

    def flexq(self):
        if self.ranked_data['queueMap']['RANKED_FLEX_SR']['wins'] + self.ranked_data['queueMap']['RANKED_FLEX_SR']['losses'] == 0:
            wr_flexq = 0
        else:
            wr_flexq = round(self.ranked_data['queueMap']['RANKED_FLEX_SR']['wins'] * 100 / (self.ranked_data['queueMap']['RANKED_FLEX_SR']['wins'] + self.ranked_data['queueMap']['RANKED_FLEX_SR']['losses']), 2)

        if self.ranked_data['queueMap']['RANKED_FLEX_SR']['tier'].lower() != "none":
            flexq = "{} {} (W:{} | L:{})".format(
                self.ranked_data['queueMap']['RANKED_FLEX_SR']['tier'].capitalize(),
                self.ranked_data['queueMap']['RANKED_FLEX_SR']['division'],
                self.ranked_data['queueMap']['RANKED_FLEX_SR']['leaguePoints'],
                wr_flexq,
                self.ranked_data['queueMap']['RANKED_FLEX_SR']['wins'],
                self.ranked_data['queueMap']['RANKED_FLEX_SR']['losses']
            )
        else:
            flexq = "Unranked"
        
        return flexq
