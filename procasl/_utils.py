import os
import glob

import numpy as np
import nibabel


def _single_glob(pattern):
    filenames = glob.glob(pattern)
    if not filenames:
        print('Warning: non exitant file with pattern {}'.format(pattern))
        return None

    if len(filenames) > 1:
        raise ValueError('Non unique file with pattern {}'.format(pattern))

    return filenames[0]


def _list_to_4d(input_files):
    """Form a 4D data from a list of 3d images.
    """
    data = []
    for f in input_files:
        image = nibabel.load(f)
        data.append(image.get_data())
    data = np.array(data)
    data = np.transpose(data, (1, 2, 3, 0))


def get_vox_dims(in_file):
    if isinstance(in_file, list):
        in_file = in_file[0]
    img = nibabel.load(in_file)
    header = img.get_header()
    voxdims = header.get_zooms()
    return [float(voxdims[0]), float(voxdims[1]), float(voxdims[2])]


def threshold(in_file, threshold_min, threshold_max):
    img = nibabel.load(in_file)
    data = img.get_data()
    data[data > threshold_max] = threshold_max
    data[data < threshold_min] = threshold_min
    img = nibabel.Nifti1Image(data, img.get_affine(), img.get_header())
    os.remove(in_file)
    nibabel.save(img, in_file)
    return in_file


def remove_nan(in_file, fill_value=0.):
    img = nibabel.load(in_file)
    data = img.get_data()
    if np.any(np.isnan(data)):
        data[np.isnan(data)] = fill_value
    img = nibabel.Nifti1Image(data, img.get_affine(), img.get_header())
    os.remove(in_file)
    nibabel.save(img, in_file)
    return in_file
