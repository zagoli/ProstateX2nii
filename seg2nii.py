from pathlib import Path
import os
import nibabel as nii
import pydicom as pd
import numpy as np
from skimage.transform import resize
from tqdm import tqdm

# path of DICOM segmentations
dcm_dataset_path = Path("C:/Users/ML/Desktop/ProstatexJacopo/seg")
# path of already converted MRI images and where output segmentations will go
nii_dataset_path = Path("C:/Users/ML/Desktop/ProstatexJacopoNII")

assert dcm_dataset_path.exists()
assert nii_dataset_path.exists()

segmentations = []
for dirpath, subdirs, files in os.walk(dcm_dataset_path):
    if files:
        # remember there's only one segmentation file
        segmentations.append(Path.joinpath(Path(dirpath), files[0]))

for dcm_path in tqdm(segmentations):
    patient_name = str(dcm_path).split('\\')[6]
    # open dcm segmentation
    volume_seg = pd.dcmread(dcm_path).pixel_array
    # open corresponding nii mri
    volume_mri = nii_dataset_path.joinpath(patient_name).joinpath("MRI_" + patient_name + ".nii")
    assert volume_mri.exists()
    niimri = nii.load(volume_mri)
    volume_mri = niimri.get_fdata()
    # downsample segmentation: there are more segmentation slices than mri slices,
    # so we need to pick fewer segmentation slices. Unfortunately the number of
    # segmentation slices is not always a multiple of the number of mri slices
    end = volume_seg.shape[0]
    step = end // volume_mri.shape[2]
    volume_seg = volume_seg[0:end:step, ...]
    diff = volume_seg.shape[0] - volume_mri.shape[2]
    if diff != 0:
        volume_seg = volume_seg[:-diff, ...]
    assert volume_seg.shape[0] == volume_mri.shape[2]
    volume_seg = np.rot90(volume_seg, k=-1, axes=(1, 2))
    volume_seg = np.swapaxes(volume_seg, 0, 1)
    volume_seg = np.swapaxes(volume_seg, 1, 2)
    # sometimes the mri and seg don't even have the same shape
    # resizing segmentation
    if volume_mri.shape != volume_seg.shape:
        # order = 0 is nearest neighbour interpolation
        volume_seg = resize(volume_seg, volume_mri.shape, preserve_range=True, order=0)
    assert volume_seg.shape == volume_mri.shape
    # saving segmentations
    niiobj = nii.Nifti1Image(volume_seg, niimri.affine)
    out_path = nii_dataset_path.joinpath(patient_name).joinpath("Prostate_"+patient_name+".nii")
    nii.save(niiobj, out_path)
