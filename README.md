# automation-scripts

This is a list of scripts that I use to automate my home. It currently contains the following scripts:

* [diplo_and_friends.py](#diplo_and_friendspy)
* [music-to-subfolders.sh](#music-to-subfolderssh)
* [music-to-external-hdd.sh](#music-to-external-hddsh)

The ideas I have in my head are listed in the `ideas.md` file and may or may not be created.

## `diplo_and_friends.py`

Automatically download the latest Diplo & Friends BBC radio show by setting up a cronjob to run this script every Sunday morning. Can easily be modified to automatically download any of the BBC shows. I'm using this script on a Raspberry Pi that's always powered on and the script always downloads to a specific folder. The script tries to download every episode available from the show, but `get_iplayer` is smart enough not to download those that have already been downloaded, therefore avoiding the duplicate downloads.

**Prerequisites:** `pip install requests bs4` and [`get_iplayer`](https://github.com/get-iplayer/get_iplayer).

## `music-to-subfolders.sh`

This script only gets executed if I'm connected to my home WiFi network. It is meant to be executed every X minutes, and what it does is it moves all the music files from my Downloads folder to a specific subfolder in my Music folder. The subfolder gets named using the `<YEAR>-<MONTH>` format, and the script automatically creates that folder in case it no longer exists.

This script helps me out to keep my Downloads folder cleaner, and makes sure that the Music files are automatically imported to my music player's library. Later on, I can sync these files to an external location, either by using Nextcloud desktop client, or by using `music-to-external-hdd.sh`. It's a simple bash script with no external dependencies.

## `music-to-external-hdd.sh`

This script is similar to the one above. It only gets executed when I'm on my home WiFi network, and what it does is it automatically copies just edited subfolders from `music-to-subfolders.sh` into an external hard drive by simply `scp`-ing them to a Raspberry Pi (to which the external hard drive is connected).

Basically the only reason this script exists and is not a part of the previous one is that I don't want to run the Nextcloud client on my Raspberry Pi, but I am leaving that as an option later on.
