class Room:
    @staticmethod
    def get_all_rooms():
        return ['Arlington', 'Marblehead', 'Wayland', 'Weston', 'Wellesley', 'Newton', 'Framingham', 'Cambridge',
                'Somerville', 'Waltham', 'Salem', 'Gloucester', 'Manchester', 'Beverley']

    def __init__(self, name: str):
        self.name = name
