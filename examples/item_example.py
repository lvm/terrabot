from terrabot import TerraBot
from terrabot.events import Events

bot = TerraBot("127.0.0.1")
event = bot.get_event_manager()


@event.on_event(Events.ItemOwnerChanged)
def logged_in(event_id, data):
    print(data)


@event.on_event(Events.ItemDropped)
def drop_update(event_id, data):
    print("New item dropped")


@event.on_event(Events.ItemDropUpdate)
def drop_update(event_id, data):
    print("Update on item")
    print("X: " + str(data.x) + " Y: " + str(data.y))


bot.start()

while bot.client.running:
    pass
