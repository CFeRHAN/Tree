from django.contrib import admin
from .models import Profile, FollowersCount, Insight


admin.site.register(Profile)
admin.site.register(FollowersCount)
admin.site.register(Insight)
