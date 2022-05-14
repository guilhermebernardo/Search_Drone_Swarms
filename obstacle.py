import random
import pygame as pg
from constants import *
from utils import Tree

vec2 = pg.math.Vector2
random.seed(3)

class Obstacles(object):
    def __init__(self, num_of_obstacles, num_of_no_flight_zones, map_size):
        super().__init__()
        self.num_of_obstacles = num_of_obstacles
        self.num_of_no_flight_zones = num_of_no_flight_zones
        self.map_size = map_size
        self.obst = []
        self.no_fly_zone = []
        
        # Variables to draw tree using Sprites
        self.tree = Tree() 
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.tree)

    def generate_no_fly_zones(self):
        self.no_fly_zone = []
        
        for _ in range(self.num_of_no_flight_zones):
            self.no_fly_zone.append(vec2(random.uniform(0,self.map_size[0]-NO_FLIGHT_ZONE_WEIGHT),
                                         random.uniform(100,self.map_size[1]-NO_FLIGHT_ZONE_HEIGHT)))
    
    def get_coordenates_no_fly_zone(self):
        return self.no_fly_zone
        
    def generate_obstacles(self):
        self.obst = []
        
        for _ in range(self.num_of_obstacles):
            self.obst.append(vec2(random.uniform(0,self.map_size[0]-RADIUS_OBSTACLES),
                                  random.uniform(100,self.map_size[1]-RADIUS_OBSTACLES)))

        print('OBSTACLE:',  self.obst)

    def get_coordenates(self):
        return self.obst

    def draw(self):
        self.all_sprites.draw(self.window)
        self.all_sprites.update(self.location,self.rotation)