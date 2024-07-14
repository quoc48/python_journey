from pathlib import Path
import json
import sys
from time import sleep

import pygame

from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overview class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Initialize mixer
        pygame.mixer.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Set screen with specific sizes
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()

        # Set full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')

        # Create an instance to store game statistics
        # and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.easy_button = Button(self)
        self.medium_button = Button(self)
        self.hard_button = Button(self)

        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Make the Play buttons.
        self._center_button()
        self.buttons.add(self.easy_button, self.medium_button, self.hard_button)

        # Make the sounds
        self.bullet_sound = pygame.mixer.Sound('sounds/laser.wav')
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse event.
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Response to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _save_high_score(self):
        """Save high score to a file."""
        with open('high_score.json', 'w') as f:
            json.dump(self.stats.high_score, f)

    def _start_game(self):
        """Start a new game when press 's' keyboard."""
        if not self.game_active:
            # Reset the game statistics.
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if not self.game_active:
            if self.easy_button.rect.collidepoint(mouse_pos):
                # Reset the game settings.
                self.settings.initialize_dynamic_settings()
            elif self.medium_button.rect.collidepoint(mouse_pos):
                self.settings.increase_speed()
            elif self.hard_button.rect.collidepoint(mouse_pos):
                self.settings.increase_speed()
                self.settings.increase_speed()

            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._save_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_s:
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key release."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_sound.play(0, 500)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.explosion_sound.play()

        if not self.aliens:
            self._start_new_level()

    def _start_new_level(self):
        # Destroy existing bullets and create new fleet.
         self.bullets.empty()
         self._create_fleet()
         self.settings.increase_speed()

         # Increase level.
         self.stats.level += 1
         self.sb.prep_level()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update position."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the game as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ship_left > 0:
            # Decrement ship_left, and update scoreboard.
            self.stats.ship_left -= 1
            self.sb.prep_ship()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finish a row; reset x value, and increase y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _center_button(self):
        self.total_button_width = self.easy_button.rect.width + self.medium_button.rect.width + self.hard_button.rect.width
        self.spacing = 50
        self.total_width = self.total_button_width + 2 * self.spacing
        self.start_x = (self.settings.screen_width - self.total_width) // 2

        self.easy_button.rect.centerx = self.start_x + self.easy_button.rect.width // 2
        self.medium_button.rect.centerx = self.start_x + self.medium_button.rect.width + self.spacing + self.medium_button.rect.width // 2
        self.hard_button.rect.centerx = self.start_x + 2* self.hard_button.rect.width + 2 * self.hard_button.rect.width // 2

        for button in self.buttons:
            button.rect.y = self.screen_rect.centery

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.easy_button.draw_button('Easy')
            self.medium_button.draw_button('Medium')
            self.hard_button.draw_button('Hard')

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


