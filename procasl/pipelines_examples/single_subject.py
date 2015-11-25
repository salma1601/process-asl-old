from nipype.interfaces import fsl
fsl.FSLCommand.set_default_output_type('NIFTI')
import nipype.interfaces.spm as spm
matlab_cmd = '/i2bm/local/spm8-standalone/run_spm8.sh /i2bm/local/spm8-standalone/mcr/v713 script'
spm.SPMCommand.set_mlab_paths(matlab_cmd=matlab_cmd, use_mcr=True)
from nipype.caching import Memory

from procasl import preprocessing, quantification

# Create a memory context
mem = Memory('/tmp/no_workflow')

# Data
func_file = '/tmp/func.nii'
anat_file = '/tmp/anat.nii'

# Rescale
rescale = mem.cache(preprocessing.Rescale)
out_rescale = rescale(in_file=func_file,
                      ss_tr=35.4, t_i_1=800., t_i_2=1800.)

# Realign to first scan
realign = mem.cache(preprocessing.Realign)
out_realign = realign(
    in_file=out_rescale.outputs.rescaled_file,
    register_to_mean=False,
    correct_tagging=True,
    paths=['/i2bm/local/spm12-6470/'])

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
    paths=['/i2bm/local/spm12-6470/'])

# Coregister anat to mean ASL
coregister_anat = mem.cache(spm.Coregister)
out_coregister_anat = coregister_anat(
    target=out_average.outputs.mean_file,
    source=anat_file,
    apply_to_files=[out_segment.outputs.native_gm_image,
                    out_segment.outputs.native_wm_image],
    write_interp=3,
    jobtype='estwrite',
    paths=['/i2bm/local/spm12-6470/'])

# Get M0
m0_file = preprocessing.save_first_scan(func_file)

# Coregister M0 to mean ASL
coregister_m0 = mem.cache(spm.Coregister)
out_coregister_m0 = coregister_m0(
    target=out_average.outputs.mean_file,
    source=m0_file,
    write_interp=3,
    jobtype='estwrite',
    paths=['/i2bm/local/spm12-6470/'])

# Smooth M0
smooth_m0 = mem.cache(spm.Smooth)
out_smooth_m0 = smooth_m0(
    in_files=out_coregister_m0.outputs.coregistered_source,
    fwhm=[5., 5., 5.],
    paths=['/i2bm/local/spm12-6470/'])

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
    tr=2500.)
