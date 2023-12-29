import random


def handle_response(message) -> str:
    flagMessage = message.lower()

    if flagMessage == 'flip':
        side = random.randint(1, 2)
        if side == 1:
            return 'Heads'
        else:
            return 'Tails'

    if flagMessage == '!help':
        return "`This is a help message that you can modify.`"
