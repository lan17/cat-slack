#!/usr/bin/env python3.7

import getpass
import os
import random
import time

import slack


def main():
    token = getpass.getpass("Slack token:")

    while True:
        client = slack.WebClient(token=token)

        kitty_files = list(filter(lambda x: x.endswith('png'), os.listdir('.')))
        print('Picking kitty out of ' + str(kitty_files))
        random_kitty = kitty_files[random.randint(0, len(kitty_files) - 1)]

        print('Chosen kitty ' + random_kitty)

        client.users_setPhoto(image=os.path.join('.', random_kitty))

        print("Updated the photo.  Meow!")

        time.sleep(3600 * 24)


if __name__ == '__main__':
    main()
