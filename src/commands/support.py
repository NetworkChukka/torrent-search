from src.objs import *

#: Support menu
@bot.message_handler(commands=['support'])
def support(message, userLanguage=None):
    userLanguage = userLanguage or dbSql.getSetting(message.chat.id, 'language')

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text=language['joinChannelBtn'][userLanguage], url='https://t.me/anonymousbotz'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['shareWithFriendsBtn'][userLanguage], url=f"https://t.me/share/url?url=t.me/torrentsrh_bot&text={language['shareText'][userLanguage]}"), telebot.types.InlineKeyboardButton(text=language['joinDiscussionBtn'][userLanguage], url='https://t.me/anonymousbotzchat'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['subscribeChannelBtn'][userLanguage], url='https://www.youtube.com/channel/UCm90WQutvuDC32qCjQ60NCw'), telebot.types.InlineKeyboardButton(text=language['followGithubBtn'][userLanguage], url='https://github.com/NetworkChukka'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['donateBtn'][userLanguage], url=f"https://buymeacoffee.com/NetworkChukka"))
    
    bot.send_message(message.chat.id, language['support'][userLanguage].format(language['supportBtn'][userLanguage]), reply_markup=markup, disable_web_page_preview=True)