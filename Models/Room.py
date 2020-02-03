class Room():
    @staticmethod
    def all_rooms():
        return ['Arlington', 'Marblehead', 'Wayland', 'Weston', 'Wellesley', 'Newton', 'Framingham', 'Cambridge',
                'Somerville', 'Waltham', 'Salem', 'Gloucester', 'Manchester', 'Beverley']

    def __init__(self, name):
        self.name = name
