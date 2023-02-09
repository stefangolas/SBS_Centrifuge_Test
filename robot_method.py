# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, 
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging,
 centrifuge_initialize, centrifuge_set_run)


lmgr = LayoutManager('deck.lay')
liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'


if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        centrifuge_initialize(ham_int, label = 'a', node_name = '00', simulate = True, always_init = True)
        
        centrifuge_set_run(ham_int, label = 'a', array_speed = [400], array_acceleration = [1200],
                           array_duration = [3], deceleration = 1200, close_cover = True, 
                           direction = 1, present_position = 4)