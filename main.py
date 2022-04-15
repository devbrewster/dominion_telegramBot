import logging
import sys
import os
import telegram
from telegram import Update, update
from telegram.ext import Updater, CommandHandler, CallbackContext


#####################################################################################
# this is used for logging and debugging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#####################################################################################
# Define a few command handlers. These usually take the two arguments update and
# context.

def start(update: Update, context):
    update.message.reply_text('Welcome to DominionXP')


#####################################################################################
# Send the contract address to the holder

def contract(update: Update, context):
    """Send a message when the command /contract is issued."""
    user = update.effective_user
    update.message.reply_text('0x6ADb2E268de2aA1aBF6578E4a8119b960E02928F')


#####################################################################################
# Sends the tokenomics information to the holders

def tokenomics(update: Update, context):
    """Send a message when the command /tokenomics is issued."""
    update.message.reply_text(""
                              "✅5% Reflections to Holders\n"
                              "✅5% Stacked into Our Liquidity Pool\n"
                              "✅5% Marketing Wallet To Keep us Going! ",

                              )


#####################################################################################
# Send the holder the Bitmart

def bitmart(update: Update, context):
    """Send a message when the command /bitmart is issued."""
    update.message.reply_text(
        f'https://www.bitmart.com/trade/en?symbol=SHIBDOGE%281M%29_USDT&layout=basic')


#####################################################################################

# Send the holder the Hotbit listing

def hotbit(update: Update, context):
    """Send a message when the command /hotbit is issued."""
    update.message.reply_text(
        f'https://www.hotbit.io/exchange?symbol=SHIBDOGE_nUSD')


#####################################################################################

# Send the holder the XT.com listing

def xtdotcom(update: Update, context):
    """Send a message when the command /xt is issued."""
    update.message.reply_text(
        f'https://www.xt.com/tradePro/1bshibdoge_usdt')


#####################################################################################

# Send the holder the UniSwap listing

def uniswap(update: Update, context):
    """Send a message when the command /uniswap is issued."""
    update.message.reply_text(
        f"https://app.uniswap.org/#/swap?inputCurrency=0x6adb2e268de2aa1abf6578e4a8119b960e02928f&chain=mainnet")


#####################################################################################

# Send the Etherscan information

def etherscan(update: Update, context):
    """Send a message when the command /etherscan is issued."""
    update.message.reply_text(
        f'https://etherscan.io/token/0x6adb2e268de2aa1abf6578e4a8119b960e02928f')


#####################################################################################

# Send Holder the website used for checking reflections earned.

def reflections(update: Update, context):
    """Send a message when the command /reflections is issued"""
    update.message.reply_text(
        f'https://shibadoge.life')


#####################################################################################

# Send Holder information for NFTs on Opensea

def opensea(update: Update, context):
    """Sena a message when the command /opensea is issued"""
    update.message.reply_text(f'https://opensea.io/collection/doge-army-shibadoge')


#####################################################################################

# Send Holder information for the NFTs on etherscan

def nft(update: Update, context):
    """Sena a message when the command /nft is issued"""
    update.message.reply_text(
        f'https://etherscan.io/token/0x21177c97be40b52b002fbee000a03212708bcf47')


#####################################################################################

# Send information for current Token Holders
def holders(update: Update, context):
    """Send a message when the command /holders is issued"""
    update.message.reply_text(
        f'https://etherscan.io/token/0x6adb2e268de2aa1abf6578e4a8119b960e02928f#balances'
    )


#####################################################################################

# Send Dextools information to user

def dextools(update: Update, context):
    """Send a message when the command /dextools is issued"""
    update.message.reply_text(
        f'https://www.dextools.io/app/ether/pair-explorer/0x3016a43b482d0480460f6625115bd372fe90c6bf'
    )


#####################################################################################

# Send user information on how to buy

def buy(update: Update, context):
    """Send a message when the command /buy is issued"""
    update.message.reply_text(
        f'https://www.youtube.com/watch?v=hR-uF06oHhA&t=1s'
    )


#####################################################################################


#####################################################################################
# Send the holder the help

def help_command(update: Update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Following Commands used in this Group:\n\n'
                              '/bitmart - Bitmart Listing\n'
                              '/buy = How to buy ShibaDoge'  # created
                              '/contract - Contract Address\n'  # created
                              '/dextools - DexTools Information\n'  # created
                              '/etherscan - Etherscan Information\n'
                              '/help - List of Commands\n'  # created
                              '/holders - Holder Information\n'  # created
                              '/hotbit - Hotbit Listing\n'  # created
                              '/nft - NFT Etherscan Information\n'  # created
                              '/opeansea - Doge Army NFTs\n'  # created
                              '/reflections - Check current reflections earned\n'
                              '/uniswap - Uniswap Listing\n'  # created
                              '/xt - XT Listing')  # created


#####################################################################################



# Main program to run bot!!!

def main():
    """ START the bot """
    # create the updater and pass it to your bots token.
    updater = Updater('Enter you Telegram API Key here', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("bitmart", bitmart))
    dispatcher.add_handler(CommandHandler("buy", buy))
    dispatcher.add_handler(CommandHandler("contract", contract))
    dispatcher.add_handler(CommandHandler("dextools", dextools))
    dispatcher.add_handler(CommandHandler("etherscan", etherscan))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("holders", holders))
    dispatcher.add_handler(CommandHandler("hotbit", hotbit))
    dispatcher.add_handler(CommandHandler("nft", nft))
    dispatcher.add_handler(CommandHandler("opeansea", opensea))
    dispatcher.add_handler(CommandHandler("reflections", reflections))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tokenomics", tokenomics))
    dispatcher.add_handler(CommandHandler("uniswap", uniswap))
    dispatcher.add_handler(CommandHandler("xt", xtdotcom))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
