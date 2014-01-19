#!/usr/bin/env python

from __future__ import division, absolute_import

import frames

def main():
    game = frames.GameFrame()
    main_menu = frames.MainMenuFrame()
    level_select = frames.LevelSelectFrame()
    
    frame_map = {
        'game': game, 
        'main_menu': main_menu,
        'level_select': level_select
    }
    
    frame_manager = frames.FrameManager(frame_map, 'main_menu')
    frame_manager.run()
    
if __name__ == '__main__':
    main()
    