from lcu_driver import Connector
from classes.riot.get_ranked_data import GetRankedData
from classes.riot.lcu import *
from psutil import process_iter


connector = Connector()
is_logged = False
is_login = False
is_first_login = False
accountId = 0
region_data = {
    "Server": ""
}
summoner_data = ''
wallet_data = ''
soloq = ''
flexq = ''


@connector.ready
async def connect(connection):
    global is_logged, accountId, summoner_data, wallet_data, soloq, flexq, region_data, is_first_login
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    summoner_data = await summoner.json()

    if is_first_login:
        while summoner.status != 200: #Check if summoner is logged into client
            summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
        
        print('Getting account data...')
        
        # Set summoner data
        summoner_data = await summoner.json()

        # Get summoner region
        region_data['Server'] = ClientInfo().region

        # Get summoner wallet data
        wallet = await connection.request('get', '/lol-store/v1/wallet')
        wallet_data = await wallet.json()

        # Get summoner ranked data
        ranked = await connection.request('get', '/lol-ranked/v1/current-ranked-stats')
        ranked_data = await ranked.json()
        ranked_data = GetRankedData(ranked_data)
        soloq = ranked_data.soloq()
        flexq = ranked_data.flexq()
        is_first_login = False
    else:
        if summoner.status != 200:
            is_logged = False
        else:
            is_logged = True

            if is_login == False:
                print('Getting account data...')

                # Get summoner region
                region_data['Server'] = ClientInfo().region

                # Get summoner wallet data
                wallet = await connection.request('get', '/lol-store/v1/wallet')
                wallet_data = await wallet.json()

                # Get summoner ranked data
                ranked = await connection.request('get', '/lol-ranked/v1/current-ranked-stats')
                ranked_data = await ranked.json()
                ranked_data = GetRankedData(ranked_data)
                soloq = ranked_data.soloq()
                flexq = ranked_data.flexq()
            else:
                print('Logging into the account...')

@connector.close
async def disconnect(connection):
    print("Connection closed!!!")
    await connector.stop()

def check_lol(islogin):
    global is_logged, is_login
    is_login = islogin
    if "LeagueClientUx.exe" in (proc.name() for proc in process_iter()):
        connector.start()
    else:
        is_logged = False

def first_login():
    global is_first_login
    is_first_login = True
    connector.start()
