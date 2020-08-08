import sys
import pygame
import game_functions as gf
from Settings import Settings
from Ship import Ship
from pygame.sprite import Group
from Alien import Alien
from GameStats import GameStats
from Button import Button
from Scoreboard import Scoreboard


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode ((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(settings, screen, "Play")
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)



run_game()
