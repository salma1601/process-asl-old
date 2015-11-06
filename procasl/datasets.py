import os
import glob


def _single_glob(pattern):
    """Returns the file matching a given pattern. An error is raised if
    multiple files match the pattern.

    Parameters
    ----------
    pattern : str
        The pattern to match.

    Returns
    -------
    output : str or None
        The filename if existant.
    """
    filenames = glob.glob(pattern)
    if not filenames:
        print('Warning: non exitant file with pattern {}'.format(pattern))
        return None

    if len(filenames) > 1:
        raise ValueError('Non unique file with pattern {}'.format(pattern))

    return filenames[0]


def load_heroes_dataset(session, n_subjects=None,
                        data_dir='/volatile/asl_data/heroes/raw'):
    dataset = {}
    dataset['subjects'] = [name for name in sorted(os.listdir(data_dir)) if
                           os.path.isdir(os.path.join(data_dir, name))]
    dataset['ASL'] = []
    dataset['anat'] = []
    dataset['perfW'] = []
    dataset['CBF'] = []
    if session == 'basal':
        session_suffix = '_*.nii'
        session_prefix = 'basal*'
    elif session in ['1', '2']:
        session_suffix = session + '_*.nii'
        session_prefix = 'vismot*'
    else:
        raise ValueError('Unknown session')

    for subject_dir in dataset['subjects'][:n_subjects]:
        subject_dir = os.path.join(data_dir, subject_dir)
        dataset['anat'].append(
            _single_glob(os.path.join(subject_dir, 't1mri', 'acquisition1',
                                      'anat*.nii')))
        for key in ['ASL', 'perfW', 'CBF']:
            dataset[key].append(_single_glob(os.path.join(
                subject_dir, 'fMRI', 'acquisition1',
                session_prefix + key + session_suffix)))
    return dataset
