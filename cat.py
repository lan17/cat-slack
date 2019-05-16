#!/usr/bin/env python3.7

import getpass
import os
import random

import slack

token = getpass.getpass("Slack token:")

client = slack.WebClient(token=token)

kitty_files = list(filter(lambda x: x.endswith('png'), os.listdir('.')))

print(kitty_files)
random_kitty = kitty_files[random.randint(0, len(kitty_files) - 1)]
print("Chosen kitty " + random_kitty)

# client.users_setPhoto(image="./1.png")
