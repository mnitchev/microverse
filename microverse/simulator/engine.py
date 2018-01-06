class Engine:
    def __init__(self, renderer=None):
        self.renderer = renderer
        self.scene = []

    def add(self, obj):
        self.scene.append(obj)

    def update(self, dt=1):
        for obj in self.scene:
            obj.update(dt)

    def render(self):
        for obj in self.scene:
            self.renderer(obj)
