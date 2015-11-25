

.. _example_plot_heroes_rescaling.py:


Comparing different connectivity measures
=========================================

This example shows how to extract signals from regions defined by an atlas,
and to estimate different connectivity measures based on these signals.



.. rst-class:: horizontal


    *

      .. image:: images/plot_adhd_tangent_1.png
            :scale: 47

    *

      .. image:: images/plot_adhd_tangent_2.png
            :scale: 47

    *

      .. image:: images/plot_adhd_tangent_3.png
            :scale: 47

    *

      .. image:: images/plot_adhd_tangent_4.png
            :scale: 47


**Script output**:

.. rst-class:: max_height

 ::

    -- Fetching datasets ...
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3902469/3902469_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3902469/3902469_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/7774305/7774305_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/7774305/7774305_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3699991/3699991_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3699991/3699991_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/2014113/2014113_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/2014113/2014113_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4275075/4275075_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4275075/4275075_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1019436/1019436_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1019436/1019436_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3154996/3154996_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3154996/3154996_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3884955/3884955_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3884955/3884955_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0027034/0027034_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0027034/0027034_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4134561/4134561_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4134561/4134561_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0027018/0027018_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0027018/0027018_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/6115230/6115230_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/6115230/6115230_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0027037/0027037_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0027037/0027037_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/8409791/8409791_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/8409791/8409791_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0027011/0027011_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0027011/0027011_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3007585/3007585_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3007585/3007585_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/8697774/8697774_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/8697774/8697774_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/9750701/9750701_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/9750701/9750701_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0010064/0010064_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0010064/0010064_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0021019/0021019_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0021019/0021019_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0010042/0010042_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0010042/0010042_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0010128/0010128_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0010128/0010128_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/2497695/2497695_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/2497695/2497695_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4164316/4164316_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4164316/4164316_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1552181/1552181_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1552181/1552181_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4046678/4046678_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4046678/4046678_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0023012/0023012_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0023012/0023012_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1679142/1679142_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1679142/1679142_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1206380/1206380_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1206380/1206380_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0023008/0023008_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/0023008/0023008_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4016887/4016887_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/4016887/4016887_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1418396/1418396_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1418396/1418396_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/2950754/2950754_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/2950754/2950754_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3994098/3994098_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3994098/3994098_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3520880/3520880_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3520880/3520880_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1517058/1517058_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1517058/1517058_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/9744150/9744150_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/9744150/9744150_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1562298/1562298_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/1562298/1562298_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3205761/3205761_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3205761/3205761_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  Processing file /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3624598/3624598_rest_tshift_RPI_voreg_mni.nii.gz
  -- Computing confounds ...
  -- Computing region signals ...
  [NiftiMapsMasker.fit_transform] loading regions from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/msdl_atlas/MSDL_rois/msdl_rois.nii
  [NiftiMapsMasker.fit_transform] loading images from /home/sb238920/CODE/Parietal/nilearn/nilearn_data/adhd/data/3624598/3624598_rest_tshift_RPI_voreg_mni.nii.gz
  [NiftiMapsMasker.fit_transform] resampling images to fit maps
  [NiftiMapsMasker.fit_transform] extracting region signals
  [NiftiMapsMasker.fit_transform] cleaning extracted signals
  -- Measuring connecivity ...
  -- Displaying results



**Python source code:** :download:`plot_adhd_tangent.py <plot_heroes_rescaling.py>`

.. literalinclude:: plot_heroes_rescaling.py
    :lines: 8-

**Total running time of the example:**  35.82 seconds 
( 0 minutes  35.82 seconds)
    
