import pygame as pg
vec = pg.math.Vector2
#Constants
WIDTH = 1024 # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768 # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Zombie Survival City"

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHTGREY = (100, 100, 100)
DARKGREY = (50, 50, 50)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BROWN = (106, 55, 5)

BGCOLOR = BROWN


WALL_IMG = 'tileGreen_39.png'

#Player stats
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 40, 40)
BARREL_OFFSET = vec(25, 10)

#mob stats
MOB_IMG = 'zombie1_hold.png'
SPLAT = 'splat_green.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 35, 35)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

#weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'speed' : 500,
                     'lifetime' : 1000,
                     'rate' : 250,
                     'kickback' : 200,
                     'spread' : 5,
                     'damage' : 10,
                     'size' : 'lg',
                     'bullet_count' : 1}

WEAPONS['shotgun'] = {'speed' : 400,
                     'lifetime' : 500,
                     'rate' : 900,
                     'kickback' : 300,
                     'spread' : 20,
                     'damage' : 5,
                     'size' : 'sm',
                     'bullet_count' : 12}
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

#effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png',
                    'whitePuff17.png', 'whitePuff18.png']
FLASH_DURATION = 40
DAMAGE_ALPHA = [i for i in range(0, 255, 25)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (400, 400)
LIGHT_MASK = 'light_350_med.png'

#layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

#Items
ITEM_IMAGES = {'health': "health_pack.png",
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 10
BOB_SPEED = 0.3

#Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav']}
EFFECTS_SOUNDS = {'level start': 'level_start.wav',
                  'health up' : 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}
