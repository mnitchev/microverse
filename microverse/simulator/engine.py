class Engine:
    def __init__(self, renderer=None):
        self.renderer = renderer
        self.scene = set()

    def add(self, *obj):
        self.scene.update(obj)

    def update(self, dt=1):
        for obj in self.scene:
            obj.update(dt)
        self.renderer.update()
        self._recycle()

    def render(self):
        for obj in self.scene:
            obj.render(self.renderer)

    def _recycle(self, *obj):
        self.scene = {obj for obj in self.scene if not obj.is_dead()}
