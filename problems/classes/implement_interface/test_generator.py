from lib.testgen import TestSet
from lib.random import randint
from lib import random
import string

MAX_RAND_LEN = 20
MAX_RAND_TESTS = 20


item_names = [
        'Town_Portal_Scroll',
        'Clarity',
        'Faerie_Fire',
        'Smoke_of_Deceit',
        'Observer_and_Sentry_Wards',
        'Enchanted_Mango',
        'Healing_Salve',
        'Tango',
        'Tome_of_Knowledge',
        'Dust_of_Appearance',
        'Animal_Courier',
        'Bottle',
        'Infused_Raindrop',
        'Magic_Stick',
        'Shadow_Amulet',
        'Ghost_Scepter',
        'Blink_Dagger',
        'Magic_Wand',
        'Soul_Ring',
        'Phase_Boots',
        'Hand_of_Midas',
        'Boots_of_Travel',
        'Moon_Shard',
        'Buckler',
        'Urn_of_Shadows',
        'Medallion_of_Courage',
        'Arcane_Boots',
        'Drum_of_Endurance',
        'Mekansm',
        'Spirit_Vessel',
        'Pipe_of_Insight',
        'Guardian_Greaves',
        'Glimmer_Cape',
        'Veil_of_Discord',
        'Force_Staff',
        'Necronomicon',
        'Solar_Crest',
        'Dagon',
        'Eul\'s_Scepter_of_Divinity',
        'Rod_of_Atos',
        'Orchid_Malevolence',
        'Nullifier',
        'Refresher_Orb',
        'Scythe_of_Vyse',
        'Hood_of_Defiance',
        'Blade_Mail',
        'Crimson_Guard',
        'Aeon_Disk',
        'Black_King_Bar',
        'Lotus_Orb',
        'Shiva\'s_Guard',
        'Hurricane_Pike',
        'Linken\'s_Sphere',
        'Manta_Style',
        'Armlet_of_Mordiggian',
        'Meteor_Hammer',
        'Shadow_Blade',
        'Skull_Basher',
        'Battle_Fury',
        'Ethereal_Blade',
        'Radiance',
        'Daedalus',
        'Butterfly',
        'Silver_Edge',
        'Abyssal_Blade',
        'Bloodthorn',
        'Sange',
        'Mask_of_Madness',
        'Helm_of_the_Dominator',
        'Echo_Sabre',
        'Maelstrom',
        'Diffusal_Blade',
        'Heaven\'s_Halberd',
        'Desolator',
        'Sange_and_Yasha',
        'Satanic',
        'Mjollnir',
        'Aegis_of_the_Immortal',
        'Cheese',
        'Refresher_Shard']

hero_names = [
        'Anti-Mage',
        'Axe',
        'Crystal_Maiden',
        'Dazzle',
        'Drow_Ranger',
        'Earthshaker',
        'Lich',
        'Lina',
        'Lion',
        'Mirana',
        'Morphling',
        'Necrophos',
        'Puck',
        'Pudge',
        'Razor',
        'Sand_King',
        'Shadow_Shaman',
        'Storm_Spirit',
        'Sven',
        'Tidehunter',
        'Vengeful_Spirit',
        'Windranger',
        'Witch_Doctor',
        'Zeus',
        'Slardar',
        'Enigma',
        'Faceless_Void',
        'Tiny',
        'Viper',
        'Venomancer',
        'Clockwerk',
        'Nature\'s_Prophet',
        'Dark_Seer',
        'Sniper',
        'Pugna',
        'Beastmaster',
        'Enchantress',
        'Leshrac',
        'Shadow_Fiend',
        'Tinker',
        'Weaver',
        'Night_Stalker',
        'Ancient_Apparition',
        'Spectre',
        'Doom',
        'Chen',
        'Juggernaut',
        'Bloodseeker',
        'Kunkka',
        'Riki',
        'Queen_of_Pain',
        'Wraith_King',
        'Broodmother',
        'Huskar',
        'Jakiro',
        'Batrider',
        'Omniknight',
        'Dragon_Knight',
        'Warlock',
        'Alchemist',
        'Lifestealer',
        'Death_Prophet',
        'Ursa',
        'Bounty_Hunter',
        'Silencer',
        'Spirit_Breaker',
        'Invoker',
        'Clinkz',
        'Outworld_Devourer',
        'Bane',
        'Shadow_Demon',
        'Lycan',
        'Lone_Druid',
        'Brewmaster',
        'Phantom_Lancer',
        'Treant_Protector',
        'Ogre_Magi',
        'Gyrocopter',
        'Chaos_Knight',
        'Phantom_Assassin',
        'Rubick',
        'Luna',
        'Io',
        'Undying',
        'Disruptor',
        'Templar_Assassin',
        'Naga_Siren',
        'Nyx_Assassin',
        'Keeper_of_the_Light',
        'Visage',
        'Meepo',
        'Magnus',
        'Centaur_Warrunner',
        'Slark',
        'Timbersaw',
        'Medusa',
        'Troll_Warlord',
        'Tusk',
        'Bristleback',
        'Skywrath_Mage',
        'Elder_Titan',
        'Abaddon',
        'Ember_Spirit',
        'Earth_Spirit',
        'Legion_Commander',
        'Phoenix',
        'Terrorblade',
        'Techies',
        'Oracle',
        'Winter_Wyvern',
        'Arc_Warden',
        'Underlord',
        'Monkey_King',
        'Dark_Willow',
        'Pangolier']

class Hero:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.busy = 0
        self.inventory = []

    def __str__(self):
        if len(self.inventory) == 0:
            return self.name
        else:
            return '\n'.join([self.name, '\n'.join(map(str, self.inventory))])

class Item:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
    def __str__(self):
        return ':' + ' '.join([self.name, str(self.weight), str(self.price)])


def add_hero(heroes):
    name = random.choice(hero_names) if len(heroes) == 0 or randint(0,5) % 4 != 0 else random.choice(list(heroes))
    strength = randint(1,40)
    if name not in heroes:
        heroes[name] = Hero(name, strength)
    return ' '.join(map(str, ['add',name,strength])) 

def give_item(heroes):
    hero_name = random.choice(hero_names) if len(heroes) == 0 or randint(0,5) % 4 == 0 else random.choice(list(heroes))
    item_name = random.choice(item_names)
    weight = randint(1,10)
    price = randint(1,10)
    if hero_name in heroes:
        if heroes[hero_name].strength >= heroes[hero_name].busy + weight:
            heroes[hero_name].inventory.append(Item(item_name, weight, price))
            heroes[hero_name].busy += weight
    return ' '.join(map(str, ['give',hero_name,item_name,weight,price]))

def get_case(n):
    heroes = {}
    cmd = []
    ret = []
    for _ in range(n):
        c = add_hero(heroes) if len(heroes) == 0 or randint(0,10) % 9 == 0 else give_item(heroes)
        cmd.append(c)
        ret.append('\n'.join([str(x) for x in sorted(heroes.values(), key = lambda x : x.name)]))

    return '\n'.join(cmd), '\n\n'.join(ret)



tests = TestSet()

for i in range(MAX_RAND_LEN):
    tests.add(*get_case(1 + 3*i))
