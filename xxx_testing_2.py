class Cryptocurrency:
    def __init__(self, name, symbol, minable=True, rate_to_usd=1, anonymous=False):
        self.name = name
        self.symbol = symbol
        self.minable = minable
        self.rate_to_usd = rate_to_usd
        self.anonymous = anonymous

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def mining_reward(self):
        return None


def minable_required(func):
    def wrapper(crypto):
        if not crypto.minable:
            print("Эту криптовалюту не майнят")
            return None
        return func(crypto)

    return wrapper


class Nano(Cryptocurrency):
    def __init__(self, block_lattice=False, rate_to_usd=5, anonymous=True):
        super().__init__("Nano", "NANO", True, rate_to_usd, anonymous)
        self.block_lattice = block_lattice

    @minable_required
    def mining_reward(self):
        return 0.02 if self.block_lattice else 0.01


class Iota(Cryptocurrency):
    def __init__(self, tangle=False, rate_to_usd=0.3, anonymous=False):
        super().__init__("Iota", "IOTA", True, rate_to_usd, anonymous)
        self.tangle = tangle

    @minable_required
    def mining_reward(self):
        return 0.001 if self.tangle else 0.002


class Stellar(Cryptocurrency):
    def __init__(self, distributed=False, rate_to_usd=0.1, anonymous=True):
        super().__init__("Stellar", "XLM", False, rate_to_usd, anonymous)
        self.distributed = distributed

    def mining_reward(self):
        print("Stellar is not minable")
        return None


def print_info(crypto):
    minable_str = 'добывают майнингом' if crypto.minable else 'не майнится'
    anonymity_str = 'анонимные транзакции' if crypto.anonymous else \
        'только публичные транзакции'
    block_lattice_str = 'блок-решетка' if hasattr(crypto, 'block_lattice') \
                                          and crypto.block_lattice else ''

    if block_lattice_str:
        print(f"{crypto}: {minable_str}, "
              f"курс к USD: {crypto.rate_to_usd}, {anonymity_str}, "
              f"{block_lattice_str}")
    else:
        print(f"{crypto}: {minable_str}, "
              f"курс к USD: {crypto.rate_to_usd}, {anonymity_str}")


cryptocurrencies = [Nano(block_lattice=True, rate_to_usd=6, anonymous=False),
                    Iota(tangle=True, rate_to_usd=0.4, anonymous=False),
                    Stellar(distributed=False, rate_to_usd=0.15, anonymous=True)]

for crypto in cryptocurrencies:
    print_info(crypto)
    if crypto.minable:
        print(f"Награда за майнинг: {crypto.mining_reward()} {crypto.symbol}\n")