import random

from helpers.sentence_clovis import hello_sentence, escouades_sentence


def build_msg(new_channel):
    msg = ""
    msg += random.choice(hello_sentence) + "\n"
    msg += random.choice(escouades_sentence) + f" dans le salon {new_channel.mention}"
    return msg
