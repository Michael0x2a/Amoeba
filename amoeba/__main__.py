#!/usr/bin/env python

import frames

def main():
    game = frames.GameFrame()
    frame_manager = frames.FrameManager([game])
    frame_manager.run()
    
if __name__ == '__main__':
    main()
    