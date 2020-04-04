from psychopy import visual, core, event
import time


def sin_grating(sf, cont):
    win0 = visual.Window([800,600], allowGUI=True, screen=0, monitors=None, units='pix', fullscr=False)
    grat_stim = visual.GratingStim(win=win0, tex='sin', units='pix', pos=(0.0,0.0), size=800, sf=sf, ori=0.0, phase=(0.0,0.0))
    #sf is the important parameter here because it changes spatial frequency
    #tex can be sin or sqr
    elapsed_time = 0
    past_time = time.perf_counter()
    while(elapsed_time < 5):
        elapsed_time = time.perf_counter() - past_time
        grat_stim.setPhase(0.01,'+')
        #numeric value here will change speed that it moves across the screen
        #+ means left to right and - means right to left
        grat_stim.contrast = cont
        #range between -1 and 1
        grat_stim.draw()
        win0.flip()
        if len(event.getKeys())>0:
            break
        event.clearEvents()
    win0.close()

sin_grating(0.02, 1)
sin_grating(0.02, 0.25)
