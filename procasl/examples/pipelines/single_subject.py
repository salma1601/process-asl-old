import nipype.interfaces.spm as spm
matlab_cmd = '/i2bm/local/spm8-standalone/run_spm8.sh ' +\
    '/i2bm/local/spm8-standalone/mcr/v713 script'
spm.SPMCommand.set_mlab_paths(matlab_cmd=matlab_cmd, use_mcr=True)
from nipype.caching import Memory

from procasl import preprocessing, quantification

# Create a memory context
mem = Memory('/tmp/no_workflow')

# Data
func_file = '/tmp/func.nii'
anat_file = '/tmp/anat.nii'
paths = ['/i2bm/local/spm8-standalone/spm8_mcr/spm8/']  # TODO: check needed

# Rescale
rescale = mem.cache(preprocessing.Rescale)
out_rescale = rescale(in_file=func_file, ss_tr=35.4, t_i_1=800., t_i_2=1800.)

# Realign to first scan
realign = mem.cache(preprocessing.Realign)
out_realign = realign(
    in_file=out_rescale.outputs.rescaled_file,
    register_to_mean=False,
    correct_tagging=True,
    paths=paths)

# Compute mean ASL
average = mem.cache(preprocessing.Average)
out_average = average(in_file=out_realign.outputs.realigned_files)

# Segment anat
segment = mem.cache(spm.Segment)
out_segment = segment(
    data=anat_file,
    gm_output_type=[False, False, True],
    wm_output_type=[False, False, True],
    save_bias_corrected=True,
    paths=paths)

# Coregister anat to mean ASL
coregister_anat = mem.cache(spm.Coregister)
out_coregister_anat = coregister_anat(
    target=out_average.outputs.mean_file,
    source=anat_file,
    apply_to_files=[out_segment.outputs.native_gm_image,
                    out_segment.outputs.native_wm_image],
    write_interp=3,
    jobtype='estwrite',
    paths=paths)

# Get M0
m0_file = preprocessing.save_first_scan(func_file)

# Coregister M0 to mean ASL
coregister_m0 = mem.cache(spm.Coregister)
out_coregister_m0 = coregister_m0(
    target=out_average.outputs.mean_file,
    source=m0_file,
    write_interp=3,
    jobtype='estwrite',
    paths=paths)

# Smooth M0
smooth_m0 = mem.cache(spm.Smooth)
out_smooth_m0 = smooth_m0(
    in_files=out_coregister_m0.outputs.coregistered_source,
    fwhm=[5., 5., 5.],
    paths=paths)

# Compute perfusion
n_scans = preprocessing.get_scans_number(out_realign.outputs.realigned_files)
ctl_scans = range(1, n_scans, 2)
tag_scans = range(0, n_scans, 2)
perfusion_file = quantification.compute_perfusion(
    out_realign.outputs.realigned_files,
    ctl_scans=ctl_scans,
    tag_scans=tag_scans)

# Compute CBF
quantify = mem.cache(quantification.QuantifyCBF)
out_quantify = quantify(
    perfusion_file=perfusion_file,
    m0_file=out_smooth_m0.outputs.smoothed_files,
    tr=2500.,
    t1_gm=1331.)

# Mask CBF map with brain mask
brain_mask_file = preprocessing.compute_brain_mask(
    out_coregister_anat.outputs.coregistered_source, frac=.2)
cbf_map = preprocessing.apply_mask(out_quantify.outputs.cbf_file,
                                   brain_mask_file)

# Plot CBF map on top of anat
import matplotlib.pylab as plt
from nilearn import plotting
plotting.plot_stat_map(
    cbf_map,
    bg_img=out_coregister_anat.outputs.coregistered_source,
    threshold=.1, vmax=150.,
    display_mode='z')
plt.show()
