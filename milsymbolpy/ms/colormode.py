class ColorMode:
    def __init__(self, civilian, friend, hostile, neutral, unknown, suspect):
        self.Civilian = civilian
        self.Friend = friend
        self.Hostile = hostile
        self.Neutral = neutral
        self.Unknown = unknown
        self.Suspect = suspect

    def __getitem__(self, item):
        return getattr(self, item)

    def get(self, item, default=None):
        return getattr(self, item, default)
