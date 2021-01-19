from chatterbot import ChatBot
bot = ChatBot(
    "Robotin",
    trainer = "chatterbot.trainers.ChatterBotCorpusTrainers"
)
bot.train(
    "chatterbot.corpus.spanish"
)
while True:
    user = input("Ingrese")
    chatb = bot.get_response(user)
    print(chatb)
