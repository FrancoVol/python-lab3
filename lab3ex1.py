from sys import argv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, bot):
    update.message.reply_text("Hello!")


def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I can't do that, that's not a command!")


def show(update, context):
    tasks.sort()
    context.bot.send_message(chat_id=update.message.chat_id, text="The tasks are:\n{}" .format(tasks))


def new(update, context):
    word = " ".join(context.args)
    tasks.append(word)
    context.bot.send_message(chat_id=update.message.chat_id, text="Successfully added {} to the list" .format(word))


def save(update, context):
    tasks.sort()
    savef = open(file, "w")
    for task in tasks:
        savef.write(task + "\n")
    savef.close()
    context.bot.send_message(chat_id= update.message.chat_id, text="List successfully saved")


def rmv(update, context):
    search = " ".join(context.args)
    flag=False
    for task in tasks:
        if search == task:
            tasks.remove(search)
            context.bot.send_message(chat_id=update.message.chat_id, text="{} successfully removed" .format(search))
            flag=True
    if not flag:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="I didn't found this tasks!\nUse /showTasks to see current tasks")


def rmvkey(update, context):
    search = "".join(context.args)
    flag = False
    for task in tasks:
        for word in task.split():
            if word == search:
                if not flag:
                    context.bot.send_message(chat_id=update.message.chat_id,
                                             text="Tasks removed:")
                tasks.remove(task)
                flag = True
                context.bot.send_message(chat_id=update.message.chat_id, text=task)

    if not flag:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="I didn't found any task!\nUse /showTasks to see current tasks")


tasks = []
file = argv[1]
txt = open(file)
for line in txt.read().splitlines():
    tasks.append(line)
txt.close()


def main():
    updater = Updater(token='FAKETOKEN', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(CommandHandler('showTasks', show))
    dispatcher.add_handler(CommandHandler('addTask', new, pass_args=True))
    dispatcher.add_handler(CommandHandler('save', save))
    dispatcher.add_handler(CommandHandler('removeTask', rmv, pass_args=True))
    dispatcher.add_handler(CommandHandler('removeAllTasks', rmvkey, pass_args=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


'''
tasks=[]
flag=True
file = argv[1]
txt = open(file)
for line in txt.read().splitlines():
    tasks.append(line)
txt.close()
while flag==True:
    print(Choose one task:
[1. insert a new task
 2. remove a task
 3. show all existing tasks
 4. close the program])
    a=int(input())
    if a==1:
        print("Insert the task you want to add:")
        tasks.append(input())
    elif a==2:
        print ("Insert a word of the tasks you want to remove:")
        rmv=input()
        for search in tasks:
            for word in  search.split():
                if word==rmv:
                    tasks.remove(search)
    elif a==3:
        
    elif a==4:
        flag=False
    else:
        print ("Wrong command. Retry.")
tasks.sort()
txt = open(file, "w")
for task in tasks:
    txt.write(task + "\n")
txt.close()
'''