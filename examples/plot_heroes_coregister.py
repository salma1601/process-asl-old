"""
===================
Coregistration demo
===================

This example shows a basic coregistration step from anatomical to mean
functional.
"""
# Create a memory context
from nipype.caching import Memory
mem = Memory('/tmp')

# Compute mean functional
from procasl import preprocessing
average = mem.cache(preprocessing.Average)
out_average = average(in_file='/tmp/func.nii')
mean_func = out_average.outputs.mean_file

# Coregister anat to mean functional
from nipype.interfaces import spm
coregister = mem.cache(spm.Coregister)
out_coregister = coregister(
    target=mean_func,
    source='/tmp/anat.nii',
    write_interp=3)

# Check coregistration
import matplotlib.pylab as plt
from nilearn import plotting
figure = plt.figure(figsize=(5, 4))
display = plotting.plot_anat(mean_func, figure=figure, display_mode='z',
                             cut_coords=(-7, 32),
                             title='anat edges on mean functional')
display.add_edges(out_coregister.outputs.coregistered_source)
figure.suptitle('Impact of tagging correction')
plt.show()
