from .marketplayer import MarketPlayer
from .arbitrageur import Arbitrageur
from .banker import Banker
from .randomizer import Randomizer
from .centralbank import CentralBank
from .nomin_shorter import NominShorter, CuritEscrowNominShorter
from .speculator import Speculator
from .merchant import Merchant, Buyer

# player names for the UI sliders
player_names = {
    # 'CentralBank': CentralBank,
    'Arbitrageur': Arbitrageur,
    'Banker': Banker,
    'Randomizer': Randomizer,
    'NominShorter': NominShorter,
    'CuritEscrowNominShorter': CuritEscrowNominShorter,
    'Speculator': Speculator,
    'Merchant': Merchant,
    'Buyer': Buyer
}
