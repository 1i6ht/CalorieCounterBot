from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters,ContextTypes
import requests
import ast
token : Final="6858106104:AAG3qDGGmTmOtJ6wlk4nsYwCrrDhHmrIKFA"
bot_username: Final="Caloriecounter1bot"
db= open('db.txt','w')
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!\nThanks for using our bot! I can help you calculate differenet types of food's calories, protein and other nutritional values.")
async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Type a food name and recieve the calories,protein and other nutrional values of desired food.")
async def command_list_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are the lists of commands that you can use:\n-start: Starts the bots activites\n-help: A small explanation of what to do to use the bot\n-commands: Shows what commands you can use\n-eat: Shows nutritional values of different foods")
async def eat_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message :str = update.message.text.replace("/eat",'').strip()
    response = handle_response(message)
    if response != "Error":
        db.write(f'{update.message.chat.username} ')
        await update.message.reply_text(response)
        await update.message.reply_text(f"{update.message.text} was/were eaten".replace("/eat",''))
    else:
        await update.message.reply_text("Something isn't right")



def handle_response(text:str)->str:
    query: str = text.lower()
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': '/3ZECei8Lb83gGBmzHXtAw==rLqHDMHe3QNtPABd'})
    string_response=''
    response1=response.text
    response1=ast.literal_eval(response1)
    for i in range(len(response1)):
        print(response1[i])
        for k,v in response1[i].items():
            string_response+=str(k)+': '+str(v)+'\n'
        string_response+='\n'
    if response.status_code == requests.codes.ok:
        return(string_response)
    else:
        return"Error"
    
async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text: str =update.message.text

    print(f'User({update.message.chat.id}) in {message_type}:"{text}"')
    response:str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'update:{update} caused error {context.error}')

if __name__ == "__main__":
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('commands',command_list_command))
    app.add_handler(CommandHandler('eat',eat_command))
    app.add_error_handler(error)

    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    app.run_polling(poll_interval=1)
##from telegram import Update
##from telegram.ext import ApplicationBuilder, CommandHandler
##from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters,ContextTypes
##async def hello(update:Update,context:ContextTypes.DEFAULT_TYPE) -> None:
##    if update.message.text == "hello":
##        await update.message.reply_text(f'Hello {update.effective_user.first_name}')
##    else:
##        await update.message.reply_text("I don't understand what you say")
##app = ApplicationBuilder().token("6858106104:AAG3qDGGmTmOtJ6wlk4nsYwCrrDhHmrIKFA").build()
##app.add_handler(CommandHandler("hello", hello))
##app.run_polling()