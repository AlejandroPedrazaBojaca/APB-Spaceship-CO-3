class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self):
        if not self.enemies : 
            self.enemies.append(Enemy())    

        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
