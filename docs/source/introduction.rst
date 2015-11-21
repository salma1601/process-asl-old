=====================
Introduction: procasl
=====================

.. contents:: **Contents**
    :local:
    :depth: 1


What is procasl: preprocessing and quantification of ASL
========================================================

.. topic:: **Why use procasl?**

    Procasl allows to perform preprocessing of ASL data.

    Procasl builds relevant **pipelines** for processing ASL data(
    :ref:`single subject pipeline <single_subject>`,
    :ref:`second level pipeline <second_level>`).

    Procasl can be used on :ref:`pulsed ASL <pulsed_asl_example.py>`,
    :ref:`pseudo-continuous ASL <pc_asl>`, or 
    :ref:`continuous ASL <continuous_asl.py>` data.


ASL: labeling arterial blood water magnetically before imaging
--------------------------------------------------------------
Magnetization is tagged sequentially to capture the flowing of the arterial blood.
Many modalities and many sequences exist, and ASL techniques is an active research field.
More on http://fmri.research.umich.edu/research/main_topics/asl.php

ASL allows weighting of the MRI signal by cerebral blood flow
-------------------------------------------------------------
The cerebral blood flow (CBF) is a fundamental physiological quantity, closely related to brain function.
:Diagnosis and prognosis:

:An accurate hemodynamics estimation:

:Assessing the neural contribution in activation BOLD signal:


Quantification: from ASL images to CBF
--------------------------------------

:General kinetic model:

:The parameters:


Installation
============
**Configuring FSL**: On an Ubuntu system, FSL is usually installed at :: /usr/share/fsl. You need to add this location to your .bashrc file. Edit this file by running the shell command:

gedit ~/.bashrc

and add the following lines:

# FSL
FSLDIR=/usr/share/fsl
. ${FSLDIR}/5.0/etc/fslconf/fsl.sh
PATH=${FSLDIR}/5.0/bin:${PATH}
export FSLDIR PATH

To test if FSL is correctly installed, open a new terminal and type in the shell command:

fsl

You should see the FSL GUI with the version number in the header.

**Configuring spm**: Add the following lines specifying the location of the spm folder to your .bashrc file:

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
