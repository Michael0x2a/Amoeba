#!/usr/bin/env python

from __future__ import division, absolute_import

import frames

def main():
    game = frames.GameFrame()
    frame_manager = frames.FrameManager({'game': game}, 'game')
    frame_manager.run()
    
if __name__ == '__main__':
    main()
    