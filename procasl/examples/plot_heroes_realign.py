"""
================
Realignment demo
================

This example compares standard realignement to realignement with tagging
correction.
"""
# Create a memory context
from nipype.caching import Memory
mem = Memory('/tmp/no_workflow')

# Give the paths to spm and to the 4D ASL image
paths = ['/i2bm/local/spm12-standalone-6472/spm12_mcr/spm12/']
raw_asl_file = '/tmp/func.nii'

# Realign with and without tagging correction
from procasl import preprocessing
import numpy as np
realign = mem.cache(preprocessing.Realign)
x_translation = {}
for correct_tagging in [True, False]:
    out_realign = realign(in_file=raw_asl_file, paths=paths,
                          correct_tagging=correct_tagging)
    x_translation[correct_tagging] = np.loadtxt(
        out_realign.outputs.realignment_parameters)[:, 2]

# Plot x-translation parameters with and without tagging correction
import matplotlib.pylab as plt
figure, (axes1, axes2) = plt.subplots(2, 1, figsize=(10, 5))
for correct_tagging, label, color in zip([True, False],
                                         ['corrected', 'uncorrected'], 'rb'):
    axes1.plot(x_translation[correct_tagging], label=label, color=color)
axes1.set_ylabel('translation in x [mm]')
axes1.legend()
axes2.plot(x_translation[True] - x_translation[False], color='g')
axes2.set_ylabel('difference [mm]')
axes2.set_xlabel('frame')
figure.suptitle('Impact of tagging correction')
figure.tight_layout()
plt.show()
