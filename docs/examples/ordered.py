#emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
#ex: set sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See the COPYING file distributed along with the smile package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##

# load all the states
from smile.common import *

# create an experiment
exp = Experiment()

Wait(1.0)

# create stims
with Parallel():
    stimB = Label(text="B", x=exp.screen.center_x + 25,
                  font_size=64,
                  color='blue')
    stimF = Label(text="F", x=exp.screen.center_x - 25,
                  font_size=64,
                  color='orange')
with UntilDone():

    Wait(1.0)
    with Parallel():
        stimB.slide(x=exp.screen.center_x - 25, duration=3.0)
        stimF.slide(x=exp.screen.center_x + 25, duration=3.0)

Wait(1.0)

if __name__ == '__main__':
    exp.run()
