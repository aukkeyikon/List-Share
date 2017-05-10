
import settings
api = settings.api

print("type user screen_name")
screen_name=input()
for twilist in api.lists_all(screen_name=screen_name):
    print("slug="+twilist.slug)
    print("name="+twilist.name)
