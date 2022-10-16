
# League Account Manager
[![Support Me on Ko-fi](https://i.imgur.com/7Cm07AZ.png)](https://ko-fi.com/siriusbeck)

## What is this
Account manager to make life easier for those who have a lot of smurfs in League of Legends.

## Why did I?
I decided to develop this app because I was too lazy to copy and paste usernames and passwords all the time while switching between my lol accounts.

## Build guide
**First I recommend creating a virtual env to get started.**

1. Copy the **`scripts\build.py`** file to the **`leagueaccountmanager`** folder.
2. Install the necessary libraries with **`pip install -r scripts\requirements.txt`**
3. Through the command prompt (or powershell, whatever), go to the **`leagueaccountmanager`** folder and execute the command **`python build.py build`**, for some you will need to use **` python3 build.py build`**.
PS: All assets you add must be listed in the **`files`** variable of the **`build.py`** file
4. Your executable will be in the **`leagueaccountmanager\build`** folder along with the necessary libraries.