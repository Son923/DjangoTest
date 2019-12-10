from membership.badges.base import Badge, BadgeAwarded
from membership.badges.registry import badges

class PointsBadge(Badge):
    slug = "Membership"
    levels = [
        "Bronze",
        "Silver",
        "Gold",
    ]
    events = [
        "points_awarded",
    ]
    multiple = False

    def award(self, **state):
        user = state["user"]
        # points = user.get_profile().points
        points = int(user.meta['Membership']['Point']['point'])
        print(points)
        if points > 10000:
            print("level 3")
            return BadgeAwarded(level=3)
        elif points > 7500:
            print("level 2")
            return BadgeAwarded(level=2)
        elif points > 5000:
            print("level 1")
            return BadgeAwarded(level=1)


badges.register(PointsBadge)