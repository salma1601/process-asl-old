.. _multiple_subjects:

============================================================================
Choosing the most suitable pipeline
============================================================================

.. topic:: **Page summary**

   Many pipelines are possible and the choice must be adapted to the problem to solve.

.. contents:: **Contents**
    :local:
    :depth: 1

.. topic:: **References**

   * `Smith et al, Network modelling methods for FMRI,
     NeuroImage 2011 <http://www.sciencedirect.com/science/article/pii/S1053811910011602>`_

   * `Varoquaux and Craddock, Learning and comparing functional
     connectomes across subjects, NeuroImage 2013
     <http://www.sciencedirect.com/science/article/pii/S1053811913003340>`_

Choosing the coregistration strategy
=====================================================

Coregistration can be done to target the anatomical image or the mean functional.

As shown in `[Smith 2011]
<http://www.sciencedirect.com/science/article/pii/S1053811910011602>`_,
`[Varoquaux 2010] <https://hal.inria.fr/inria-00512451>`_, it is more
interesting to use the inverse covariance matrix, ie the *precision
matrix*. It gives **only direct connections between regions**, as it
contains *partial covariances*, which are covariances between two regions
conditioned on all the others.


To recover well the interaction structure, a **sparse inverse covariance
estimator** is necessary. The GraphLasso, implemented in scikit-learn's
estimator :class:`sklearn.covariance.GraphLassoCV` is a good, simple
solution. To use it, you need to create an estimator object::

    >>> from sklearn.covariance import GraphLassoCV
    >>> estimator = GraphLassoCV()

And then you can fit it on the activation time series, for instance
extracted in :ref:`the previous section <functional_connectomes>`::

    >>> estimator.fit(time_series)  # doctest: +SKIP

The covariance matrix and inverse-covariance matrix (precision matrix)
can be found respectively in the `covariance_` and `precision_` attribute
of the estimator::

    >>> estimator.covariance_  # doctest: +SKIP
    >>> estimator.precision_  # doctest: +SKIP


.. |covariance| image:: ../auto_examples/connectivity/images/plot_inverse_covariance_connectome_001.png
    :target: ../auto_examples/connectivity/plot_inverse_covariance_connectome.html
    :scale: 40
.. |precision| image:: ../auto_examples/connectivity/images/plot_inverse_covariance_connectome_003.png
    :target: ../auto_examples/connectivity/plot_inverse_covariance_connectome.html
    :scale: 40

.. |covariance_graph| image:: ../auto_examples/connectivity/images/plot_inverse_covariance_connectome_002.png
    :target: ../auto_examples/connectivity/plot_inverse_covariance_connectome.html
    :scale: 55

.. |precision_graph| image:: ../auto_examples/connectivity/images/plot_inverse_covariance_connectome_004.png
    :target: ../auto_examples/connectivity/plot_inverse_covariance_connectome.html
    :scale: 55

.. centered:: |covariance| |precision|

.. centered:: |covariance_graph| |precision_graph|



.. topic:: **Parameter selection**

    The parameter controlling the sparsity is set by `cross-validation
    <http://scikit-learn.org/stable/modules/cross_validation.html>`_
    scheme. If you want to specify it manually, use the estimator
    :class:`sklearn.covariance.GraphLasso`.

.. topic:: **Full example**

    See the following example for a full file running the analysis:
    :ref:`example_connectivity_plot_inverse_covariance_connectome.py`

.. topic:: **Exercise: computing sparse inverse covariance**
   :class: green

   Compute and visualize a connectome on the first subject of the ADHD
   dataset downloaded with :func:`nilearn.datasets.fetch_adhd`

   **Hints:** The example above has the solution

.. topic:: **Reference**

 * The `graph lasso [Friedman et al, Biostatistics 2007] <http://biostatistics.oxfordjournals.org/content/9/3/432.short>`_ is useful to estimate one
   inverse covariance, ie to work on single-subject data or concatenate
   multi-subject data.


Putting all together
====================

Individual connectivity patterns reflect both on covariances and inverse covariances, but in different ways. For multiple subjects, mean covariance (or correlation) and group sparse inverse covariance provide different insights into the connectivity at the group level.

We can go one step further by coupling the information from total (pairwise) and direct interactions in a unique group connectome. This can be done through a geometrical framework allowing to measure interactions in a common space called **tangent space** `[Varoquaux et al, MICCAI 2010] <https://hal.inria.fr/inria-00512417/>`_.

In nilearn, this is implemented in
:class:`nilearn.connectome.ConnectivityMeasure`::

    >>> measure = ConnectivityMeasure(kind='tangent')  # doctest: +SKIP

The group connectivity is computed using all the subjects timeseries.::

    >>> connectivities = measure.fit([time_series_1, time_series_2, ...])  # doctest: +SKIP
    >>> group_connectivity = measure.mean_  # doctest: +SKIP

Deviations from this mean in the tangent space are provided in the connectivities array and can be used to compare different groups/sessions. In practice, the tangent measure can outperform the correlation and partial correlation measures, especially for noisy or heterogeneous data.


.. topic:: **Full example**

    See the following example for a full file running the analysis:
    :ref:`example_connectivity_plot_connectivity_measures.py`

.. topic:: **Exercise: computing connectivity in tangent space**
   :class: green

   Compute and visualize the tangent group connectome based on the NYU, OHSU and NeuroImage sites of the ADHD
   dataset downloaded with :func:`nilearn.datasets.fetch_adhd`

   **Hints:** The example above has the solution

.. topic:: **Reference**

 * The `tangent space for connectivity [Varoquaux et al, MICCAI 2010] <http://link.springer.com/chapter/10.1007%2F978-3-642-15705-9_25>`_


