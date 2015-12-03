=====================
Introduction: procasl
=====================

.. contents:: **Contents**
    :local:
    :depth: 1


What is procasl: preprocessing and quantification of ASL
========================================================

.. topic:: **Why use procasl?**

    Procasl builds relevant **pipelines** for processing ASL data(
    :ref:`single subject pipeline <single_subject>`,
    :ref:`second level pipeline <second_level>`).

    Procasl can be used on :ref:`pulsed ASL <pulsed_asl_example.py>`,
    :ref:`pseudo-continuous ASL <pc_asl>`, or 
    :ref:`continuous ASL <continuous_asl.py>` data.

Whetting Your Appetite
----------------------
Blood flows from carotid arteries to capilleray bed. The volume of arterial blood (mL) delivered to 100 g of tissue per minute is called the Cerebral Blood Flow (CBF). In human brain, it has a typical value of CBF is 60 mL/100 g-minute. CBF is an important indicator of tissue health [] as well as neuronal activity [].

Prior to ASL, the techniques used for determining cerebral blood flow were rather invasive and involved the 
of exogenous contrast agents, such as like the 15O H2O radiotracer in Positron Emission Tomography (PET).


Ideally, scientists would like to measure neural activity directly. However, as this is nearly impossible under normal circumstances, most researchers have chosen to observe the changes in the metabolic activity that follow mental work using techniques such as BOLD. 


Though measuring changes in blood flow as a consequence of neural activity would be the next most direct approach, this was formerly only obtainable through the use of invasive imaging techniques utilizing exogenous contrast agents. 

Thus, most researchers opted to use the BOLD technique, which though dependent on cerebral blood flow (CBF), does not give a direct measure of it. However, due to recent advances in MR imaging, it is now possible to capture CBF measurements entirely non-invasively.

Prior to ASL, the techniques used for determining cerebral blood flow were rather invasive and involved the use of exogenous contrast agents, such as like the 15O H2O radiotracer in Positron Emission Tomography (PET). In this technique, researchers inject a radiotracer (which was essentially radioactively labeled water) into the participant. This radiotracer would then circulate through the body's vascular system, ultimately diffusing freely into brain tissue along with the blood. The radioactive tracer would begin to decay almost immediately, emitting tiny positively charged particles (called positrons) which could then be detected using specialized equipment. As the radiotracer travels with the blood, the amount of radioactvity detected reflects blood flow. That is to say, areas which received a lot of blood should also have received a lot of radioactively labeled water and consequently shown higher levels of radioactive positron emissions. Thus, in for each region of brain tissue, uptake of the radiotracer would be proportional to blood flow.

Similar to PET techniques, ASL utilizes a tracer of sorts. In ASL, arterial blood water is magnetically labeled then imaged. First, arterial blood water is magnetically labeled just below the region (slice) of interest by applying a 180 degree radiofrequency (RF) inversion pulse. The result of this pulse is inversion of the net magnetization of the blood water. In other words, the water molecules within the arterial blood are labeled magnetically. After a period of time (called the transit time), this 'paramagnetic tracer’ flows into slice of interest where it exchanges with tissue water. The inflowing inverted spins within the blood water alter total tissue magnetization, reducing it and, consequently, the MR signal & image intensity. During this time, an image is taken (called the tag image).

The experiment is then repeated without labeling the arterial blood to create another image (called the control image). The control image and the tag image are subtracted to produce a perfusion image. This image will reflect the amount of arterial blood delivered to each voxel within the slice within the transit time.

ASL: labeling arterial blood water magnetically before imaging
--------------------------------------------------------------
Magnetization is tagged sequentially to capture the flowing of the arterial blood.
Many modalities and many sequences exist, and ASL techniques is an active research field.
More on http://fmri.research.umich.edu/research/main_topics/asl.php

ASL allows weighting of the MRI signal by cerebral blood flow
-------------------------------------------------------------
The cerebral blood flow (CBF) is a fundamental physiological quantity, closely related to brain function.

:Diagnosis:

:An accurate hemodynamics estimation:

:Assessing the neural contribution in activation BOLD signal:


Quantification: from ASL images to CBF
--------------------------------------

:General kinetic model:

:The parameters:


Installation
============
**Configuring FSL**: On an Ubuntu system, FSL is usually installed at :: /usr/share/fsl. You need to add this location to your .bashrc file. Edit this file by running the shell command::

    gedit ~/.bashrc

and add the following lines::

    # FSL
    FSLDIR=/usr/share/fsl
    . ${FSLDIR}/5.0/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/5.0/bin:${PATH}
    export FSLDIR PATH

To test if FSL is correctly installed, open a new terminal and type in the shell command::

    fsl

You should see the FSL GUI with the version number in the header.

**Configuring SPM**: Add the following lines specifying the location of the spm folder to your .bashrc file::

    # SPM8
    export SPM_PATH=/i2bm/local/spm8-standalone/spm8_mcr/spm8

**Downloading procasl:** Run the shell command::

    git clone https://github.com/salma1601/process-asl


**Installing procasl:** In the ``process-asl`` directory created by the previous step, run
(again, as a shell command)::

    python setup.py install --user

**Testing the installation:** To check whether everything is set up correctly, open IPython and type
in the following line::

    In [1]: import procasl

If no error occurs, you have installed procasl correctly.
