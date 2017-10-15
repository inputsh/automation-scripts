# automation-scripts

This is a list of scripts that I use to automate my home. It currently contains the following scripts:

* [diplo_and_friends.py](#diplo_and_friendspy)
* [goodreads_to_md_list.py](#goodreads_to_md_listpy)
* [music-to-subfolders.sh](#music-to-subfolderssh)
* [music-to-external-hdd.sh](#music-to-external-hddsh)

The ideas I have in my head are listed in the `ideas.md` file and may or may not be created.

## `diplo_and_friends.py`

Automatically download the latest Diplo & Friends BBC radio show by setting up a cronjob to run this script every Sunday morning. Can easily be modified to automatically download any of the BBC shows. The script tries to download every episode available from the show, but `get_iplayer` is smart enough not to download those that have already been downloaded, therefore avoiding the duplicate downloads.

**Bonus points:** this script is executed on my [Nextcloud](https://nextcloud.com/) server, so there's a `php occ files:scan` command that re-scans the files in the directory the `.mp3` files are placed in. This script is also integrated with [Simplepush](https://simplepush.io/), so that I would get an Android notification that the new episode is currently being downloaded on my server.

* **Scripting language:** Python 2
* **Prerequisites:** `pip install requests bs4` and [`get_iplayer`](https://github.com/get-iplayer/get_iplayer). [Nextcloud](https://nextcloud.com/) and [Simplepush](https://simplepush.io/) for bonus points.

## `goodreads_to_md_list.py`

This script works with the Goodreads API. It fetches the list of books from a public Goodreads shelf, and then outputs the list as a Markdown file. The point of this list is to have it synced in some external file, which could later be backed up (by using Git, as you can [see here](https://github.com/aleksandar-todorovic/notes/blob/master/00_books.md)).

Note that each book in your year needs to have a valid `read_at` field filled out for the lines 53-65 to work. I could have added a small try/except to fix this, but I specifically wanted it to make sure that every book has a `read_at` field filled out before continuing.

* **Scripting language:** Python 3
* **Prerequisites:** `pip install requests`

## `music-to-subfolders.sh`

This script only gets executed if I'm connected to my home WiFi network. It is meant to be executed every X minutes, and what it does is it moves all the music files from my Downloads folder to a specific subfolder in my Music folder. The subfolder gets named using the `<YEAR>-<MONTH>` format, and the script automatically creates that folder in case it no longer exists.

This script helps me out to keep my Downloads folder cleaner, and makes sure that the Music files are automatically imported to my music player's library. Later on, I can sync these files to an external location, either by using Nextcloud desktop client, or by using `music-to-external-hdd.sh`.

* **Scripting language:** bash
* **Prerequisites:** N/A

## `music-to-external-hdd.sh`

This script is similar to the one above. It only gets executed when I'm on my home WiFi network, and what it does is it automatically copies just edited subfolders from `music-to-subfolders.sh` into an external hard drive by simply `scp`-ing them to a Raspberry Pi (to which the external hard drive is connected).

Basically the only reason this script exists and is not a part of the previous one is that I don't want to run the Nextcloud client on my Raspberry Pi, but I am leaving that as an option later on.

* **Scripting language:** bash
* **Prerequisites:** N/A
