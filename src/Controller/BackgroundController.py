import pygame
import os
from src.Common import DoubleLane, Lane
from src.Config import Config


class BackgroundController:
    def __init__(self, surface, traffic_lights):
        self.surface = surface
        self.traffic_lights = traffic_lights

        self.screen_height = Config['simulator']['screen_height']
        self.screen_width = Config['simulator']['screen_width']

        self.black = Config['colors']['black']
        self.red = Config['colors']['red']

        self.horizontal_frequency_small = None
        self.horizontal_frequency_medium = None
        self.horizontal_frequency_large = None

        self.vertical_frequency_small = None
        self.horizontal_frequency_medium = None
        self.horizontal_frequency_large = None

        self.spawn_rate = {
            Lane.left_to_right: {
                'slow': False,
                'medium': True,
                'fast': False
            },
            Lane.top_to_bottom: {
                'slow': False,
                'medium': True,
                'fast': False
            },
            Lane.right_to_left: {
                'slow': False,
                'medium': True,
                'fast': False
            },
            Lane.bottom_to_top: {
                'slow': False,
                'medium': True,
                'fast': False
            }
        }

        self.spawn_rate_buttons = {
            Lane.left_to_right: {
                'slow': None,
                'medium': None,
                'fast': None
            },
            Lane.top_to_bottom: {
                'slow': None,
                'medium': None,
                'fast': None
            },
            Lane.right_to_left: {
                'slow': None,
                'medium': None,
                'fast': None
            },
            Lane.bottom_to_top: {
                'slow': None,
                'medium': None,
                'fast': None
            }
        }

        self.switch_traffic_button = None
        self.fuzzy_button = None

    def set_spawn_rate(self, lane: Lane, target_rate):
        for rate in ['slow', 'medium', 'fast']:
            self.spawn_rate[lane][rate] = (target_rate == rate)

    def get_spawn_rate(self,lane: Lane):
        for rate in ['slow', 'medium', 'fast']:
            if self.spawn_rate[lane][rate]:
                return rate
        raise Exception('None of slow, medium, fast is true!!!')

    def refresh_screen(self):
        self.surface.fill(Config['colors']['white'])

    def draw_spawn_rate_buttons(self):
        normal_font = pygame.font.SysFont('Comic Sans MS', 16)
        underline_font = pygame.font.SysFont('Comic Sans MS', 16)
        underline_font.set_underline(True)

        # Horizontal lanes controls
        self.surface.blit(normal_font.render('Spawn Rate (Left-to-Right):', True, self.black), (5, 25))
        fonts = [normal_font, normal_font, normal_font]
        colors = [self.black, self.black, self.black]
        if self.spawn_rate[Lane.left_to_right]['slow']:
            fonts[0] = underline_font
            colors[0] = self.red
        if self.spawn_rate[Lane.left_to_right]['medium']:
            fonts[1] = underline_font
            colors[1] = self.red
        if self.spawn_rate[Lane.left_to_right]['fast']:
            fonts[2] = underline_font
            colors[2] = self.red
        self.spawn_rate_buttons[Lane.left_to_right]['slow'] = self.surface.blit(fonts[0].render('Slow', True, colors[0]), (240, 25))
        self.spawn_rate_buttons[Lane.left_to_right]['medium'] = self.surface.blit(fonts[1].render('Medium', True, colors[1]), (280, 25))
        self.spawn_rate_buttons[Lane.left_to_right]['fast'] = self.surface.blit(fonts[2].render('Fast', True, colors[2]), (340, 25))

        # Vertical lanes controls
        self.surface.blit(normal_font.render('Spawn Rate (Top-to-Bottom):', True, self.black), (5, 45))
        fonts = [normal_font, normal_font, normal_font]
        colors = [self.black, self.black, self.black]
        if self.spawn_rate[Lane.top_to_bottom]['slow']:
            fonts[0] = underline_font
            colors[0] = self.red
        if self.spawn_rate[Lane.top_to_bottom]['medium']:
            fonts[1] = underline_font
            colors[1] = self.red
        if self.spawn_rate[Lane.top_to_bottom]['fast']:
            fonts[2] = underline_font
            colors[2] = self.red
        self.spawn_rate_buttons[Lane.top_to_bottom]['slow'] = self.surface.blit(fonts[0].render('Slow', True, colors[0]), (240, 45))
        self.spawn_rate_buttons[Lane.top_to_bottom]['medium'] = self.surface.blit(fonts[1].render('Medium', True, colors[1]), (280, 45))
        self.spawn_rate_buttons[Lane.top_to_bottom]['fast'] = self.surface.blit(fonts[2].render('Fast', True, colors[2]), (340, 45))

        # Vertical lanes controls
        self.surface.blit(normal_font.render('Spawn Rate (Right-to-Left):', True, self.black), (5, 65))
        fonts = [normal_font, normal_font, normal_font]
        colors = [self.black, self.black, self.black]
        if self.spawn_rate[Lane.right_to_left]['slow']:
            fonts[0] = underline_font
            colors[0] = self.red
        if self.spawn_rate[Lane.right_to_left]['medium']:
            fonts[1] = underline_font
            colors[1] = self.red
        if self.spawn_rate[Lane.right_to_left]['fast']:
            fonts[2] = underline_font
            colors[2] = self.red
        self.spawn_rate_buttons[Lane.right_to_left]['slow'] = self.surface.blit(fonts[0].render('Slow', True, colors[0]), (240, 65))
        self.spawn_rate_buttons[Lane.right_to_left]['medium'] = self.surface.blit(fonts[1].render('Medium', True, colors[1]), (280, 65))
        self.spawn_rate_buttons[Lane.right_to_left]['fast'] = self.surface.blit(fonts[2].render('Fast', True, colors[2]), (340, 65))
        
        # Vertical lanes controls
        self.surface.blit(normal_font.render('Spawn Rate (Bottom-to-Top):', True, self.black), (5, 85))
        fonts = [normal_font, normal_font, normal_font]
        colors = [self.black, self.black, self.black]
        if self.spawn_rate[Lane.bottom_to_top]['slow']:
            fonts[0] = underline_font
            colors[0] = self.red
        if self.spawn_rate[Lane.bottom_to_top]['medium']:
            fonts[1] = underline_font
            colors[1] = self.red
        if self.spawn_rate[Lane.bottom_to_top]['fast']:
            fonts[2] = underline_font
            colors[2] = self.red
        self.spawn_rate_buttons[Lane.bottom_to_top]['slow'] = self.surface.blit(fonts[0].render('Slow', True, colors[0]), (240, 85))
        self.spawn_rate_buttons[Lane.bottom_to_top]['medium'] = self.surface.blit(fonts[1].render('Medium', True, colors[1]), (280, 85))
        self.spawn_rate_buttons[Lane.bottom_to_top]['fast'] = self.surface.blit(fonts[2].render('Fast', True, colors[2]), (340, 85))

    def draw_moving_averages(self, moving_averages):
        normal_font = pygame.font.SysFont('Comic Sans MS', 16)
        self.surface.blit(normal_font.render('Vehicles behind traffic light (L2R):', True, self.black), (5, 105))
        self.surface.blit(normal_font.render('{0:.2f}'.format(moving_averages[Lane.left_to_right]), True, self.black), (320, 105))
        self.surface.blit(normal_font.render('Vehicles behind traffic light (T2B):', True, self.black), (5, 125))
        self.surface.blit(normal_font.render('{0:.2f}'.format(moving_averages[Lane.top_to_bottom]), True, self.black), (320, 125))
        self.surface.blit(normal_font.render('Vehicles behind traffic light (R2L):', True, self.black), (5, 145))
        self.surface.blit(normal_font.render('{0:.2f}'.format(moving_averages[Lane.right_to_left]), True, self.black), (320, 145))
        self.surface.blit(normal_font.render('Vehicles behind traffic light (B2T):', True, self.black), (5, 165))
        self.surface.blit(normal_font.render('{0:.2f}'.format(moving_averages[Lane.bottom_to_top]), True, self.black), (320, 165))

    def draw_vehicle_count(self, total):
        font = pygame.font.SysFont('Comic Sans MS', 16)
        text_surface = font.render('Total Vehicles: {}'.format(total), True, self.black)
        self.surface.blit(text_surface, (5, 5))

    def draw_road_markings(self):
        bumper_distance = Config['simulator']['bumper_distance']
        vehicle_body_width = Config['vehicle']['body_width']
        road_marking_width = Config['background']['road_marking_width']
        road_marking_length, road_marking_distance = Config['background']['road_marking_alternate_lengths']
        traffic_yellow = Config['colors']['traffic_yellow']
        gap = Config['background']['road_marking_gap_from_yellow_box']

        # yellow box
        yb_top, yb_left, yb_bottom, yb_right = Config['background']['yellow_box_junction']
        yellow_box_junction_img = os.path.join(os.getcwd(), 'images', 'junction', 'yellow_box_junction.png')
        picture = pygame.image.load(yellow_box_junction_img)
        picture = pygame.transform.scale(picture, (yb_left + yb_right, yb_top + yb_bottom))
        self.surface.blit(picture, (self.screen_width / 2 - yb_left, self.screen_height / 2 - yb_top))

        # lane from bottom to top
        # lane from top to bottom
        x1 = self.screen_width / 2 - bumper_distance - vehicle_body_width / 2 - road_marking_width / 2
        x2 = self.screen_width / 2 + bumper_distance + vehicle_body_width / 2 - road_marking_width / 2
        y = self.screen_height / 2 - yb_top - road_marking_length - road_marking_distance
        while y >= 0:
            pygame.draw.rect(self.surface, traffic_yellow, (x1, y, road_marking_width, road_marking_length))
            pygame.draw.rect(self.surface, traffic_yellow, (x2, y, road_marking_width, road_marking_length))
            y -= road_marking_length + road_marking_distance
        y = self.screen_height / 2 + yb_bottom + gap
        while y <= self.screen_height:
            pygame.draw.rect(self.surface, traffic_yellow, (x1, y, road_marking_width, road_marking_length))
            pygame.draw.rect(self.surface, traffic_yellow, (x2, y, road_marking_width, road_marking_length))
            y += road_marking_length + road_marking_distance

        # lane from left to right
        # lane from right to left
        x = self.screen_width / 2 - yb_left - road_marking_length - gap
        y1 = self.screen_height / 2 - bumper_distance - vehicle_body_width / 2 - road_marking_width / 2
        y2 = self.screen_height / 2 + bumper_distance + vehicle_body_width / 2 - road_marking_width / 2
        while x >= 0:
            pygame.draw.rect(self.surface, traffic_yellow, (x, y1, road_marking_length, road_marking_width))
            pygame.draw.rect(self.surface, traffic_yellow, (x, y2, road_marking_length, road_marking_width))
            x -= road_marking_length + road_marking_distance
        x = self.screen_width / 2 + yb_right + gap
        while x <= self.screen_width:
            pygame.draw.rect(self.surface, traffic_yellow, (x, y1, road_marking_length, road_marking_width))
            pygame.draw.rect(self.surface, traffic_yellow, (x, y2, road_marking_length, road_marking_width))
            x += road_marking_length + road_marking_distance

    def within_boundary(self, x, y):
        return 0 <= x <= self.screen_width and 0 <= y <= self.screen_height

    def draw_switch_traffic_button(self):
        font = pygame.font.SysFont('Comic Sans MS', 16)
        text_surface = font.render('Switch', True, self.black)
        rect = self.surface.blit(text_surface, (self.screen_width - 100, 20))
        gap = 5
        x = rect.left - gap
        y = rect.top - gap
        w = rect.width + gap * 2
        h = rect.height + gap * 2
        pygame.draw.rect(self.surface, self.black, (x, y, w, h), 3)
        self.switch_traffic_button = rect

    def draw_fuzzy_button(self):
        font = pygame.font.SysFont('Comic Sans MS', 16)
        text_surface = font.render('Calculate Fuzzy', True, self.black)
        rect = self.surface.blit(text_surface, (self.screen_width - 150, 90))
        gap = 5
        x = rect.left - gap
        y = rect.top - gap
        w = rect.width + gap * 2
        h = rect.height + gap * 2
        pygame.draw.rect(self.surface, self.black, (x, y, w, h), 3)
        self.fuzzy_button = rect

    def draw_fuzzy_score(self, fuzzy_score, lane: Lane):
        normal_font = pygame.font.SysFont('Comic Sans MS', 16)
        #opposite_lane_name = 'Horizontal' if current_lane == DoubleLane.Vertical else 'Vertical'
        self.surface.blit(normal_font.render('Fuzzy Green Light Ext. ({} Lane): '.format(lane.name), True, self.black), (5, 185))

        score = '-'
        if fuzzy_score:
            score = '{:.2f}s'.format(fuzzy_score)
        self.surface.blit(normal_font.render(score, True, self.black), (320, 185))

    def draw_extension_notification(self, extension, current_lane, moving_averages):
        normal_font = pygame.font.SysFont('Comic Sans MS', 16)
        active = moving_averages[current_lane.value-1]
        passive = sum(moving_averages) - moving_averages[current_lane.value-1]
        
        self.surface.blit(normal_font.render('Vehicle behind Traffic Light  ', True, Config['colors']['traffic_green']), (5, 205))
        self.surface.blit(normal_font.render('     Arrival : ', True, Config['colors']['traffic_green']), (5, 225))
        self.surface.blit(normal_font.render('{:.1f}'.format(active), True, Config['colors']['traffic_green']), (100, 225))
        self.surface.blit(normal_font.render('     Queue :', True, Config['colors']['traffic_green']), (5, 245))
        self.surface.blit(normal_font.render('{:.1f}'.format(passive), True, Config['colors']['traffic_green']), (100, 245))
        self.surface.blit(normal_font.render('Green light is extended by {:.1f}!'.format(extension), True, Config['colors']['traffic_green']), (5, 265))

    def draw_light_durations(self, green_light_extension):
        normal_font = pygame.font.SysFont('Comic Sans MS', 16)
        green_duration = Config['traffic_light']['green_light_duration']
        yellow_duration = Config['traffic_light']['yellow_light_duration']
        red_duration = Config['traffic_light']['red_light_duration']

        pygame.draw.circle(self.surface, Config['colors']['traffic_red'], (self.screen_width - 180, 16), 8)
        self.surface.blit(normal_font.render('Duration: {:.1f}'.format(red_duration), True, self.black),
                          (self.screen_width - 160, 5))

        pygame.draw.circle(self.surface, Config['colors']['traffic_yellow'], (self.screen_width - 180, 36), 8)
        self.surface.blit(normal_font.render('Duration: {:.1f}'.format(yellow_duration), True, self.black),
                          (self.screen_width - 160, 25))

        pygame.draw.circle(self.surface, Config['colors']['traffic_green'], (self.screen_width - 180, 56), 8)
        if green_light_extension > 0:
            self.surface.blit(
                normal_font.render('Duration: {:.1f} + {:.1f}'.format(green_duration, green_light_extension), True,
                                   self.black),
                (self.screen_width - 160, 45))
        else:
            self.surface.blit(normal_font.render('Duration: {:.1f}'.format(green_duration), True, self.black),
                              (self.screen_width - 160, 45))
