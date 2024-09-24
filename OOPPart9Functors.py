import random


class BotPlayer:
    def __init__(self):
        self.__name = random.choice(["SuperBot", "MegaBot", "Bot-player"])
        self.__walletSetter = WalletFunctor(50)
        self.__wallet = self.__walletSetter()

    def updateWallet(self, coins=0):
        self.__wallet = self.__walletSetter(coins)

    def showWallet(self):
        print(f"{self.__name}! You have {self.__wallet} coins now.")


class UserPlayer:
    def __init__(self, name):
        self.name = name
        self.wallet = 100
        self.walletSetter = WalletFunctor()
        self.wallet = self.walletSetter()

    def updateWallet(self, coins):
        self.wallet += coins
        self.wallet = self.walletSetter(coins)

    def showWallet(self):
        print(f"You have {self.wallet} coins now.")
        print(f"{self.name}! You have {self.wallet} coins now.")


class WalletFunctor:
    def __init__(self, startCoins=100):
        self.startCoins = startCoins

    def __call__(self, coins=0):
        return self.startCoins + coins


user1 = UserPlayer("Joe")
user1.updateWallet(50)
user1.showWallet()
userWallet = WalletFunctor()
print(f"Start state of user wallet: {userWallet()} coins")
print(f"State of user wallet after updating to 50 coins: {userWallet(50)} coins")
botWallet = WalletFunctor(50)
print(f"Start state of bot wallet: {botWallet()} coins")
print(f"State of user bot after updating to 20 coins: {botWallet(20)} coins")
user1 = UserPlayer("Joe")
user1.showWallet()
user1.updateWallet(50)
user1.showWallet()
bot1 = BotPlayer()
bot1.showWallet()
bot1.updateWallet(20)
bot1.showWallet()
