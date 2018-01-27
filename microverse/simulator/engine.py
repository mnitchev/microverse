class Engine:
    def __init__(self, renderer=None):
        self.renderer = renderer
        self.scene = []

    def add(self, *obj):
        self.scene.extend(obj)

    def update(self, dt=1):
        for obj in self.scene:
            obj.update(dt)
        self.renderer.update()

    def render(self):
        for obj in self.scene:
            obj.render(self.renderer)
