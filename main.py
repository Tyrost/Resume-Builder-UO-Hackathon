'''
Main Python File
'''
from components import *


try:
    custom_font = font.Font(family = 'Lexend', size = 12)
    WINDOW.option_add('*Font', custom_font)
except Exception as e:
    log.error(f'Error loading font: {e}')