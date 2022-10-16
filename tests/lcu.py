from time import sleep
from lcu_driver import Connector
import json
from os import system as cmd

connector = Connector()

@connector.ready
async def connect(connection):
    inputs_data = inputs()
    response = await connection.request('get', inputs_data[1])
    data = await response.json()
    data_json = json.dumps(data, indent=4)
    with open(f'./lcu_responses/{inputs_data[0]}.json', 'w') as file:
        file.write(data_json)
    print(data_json)

@connector.close
async def disconnect(connection):
    print("\n\n\nConnection closed!!!")
    await connector.stop()

def inputs():
    cmd('cls')
    test_name = input('Test name: ')
    url = input('Request URL: ')
    inputs_data = [test_name, url]
    return inputs_data

def continue_check():
    c = input('Test another URL? [y/n] ')
    c = c.lower()
    if c == 'y':
        connector.start()
    elif c == 'n':
        exit()
    else:
        exit()

connector.start()

sleep(1)

continue_check()