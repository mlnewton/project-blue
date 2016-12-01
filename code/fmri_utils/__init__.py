# Init for utils package
from .spm_funcs import spm_global, get_spm_globals, spm_hrf
from .model_signal import data_timecourse, create_design_matrix, event_timecourse, hrf, b_e_calc, create_contrast_img
from .detectors import mean_detector, std_detector, iqr_detector
