# ProstateX2nii
I used these scripts to convert the [PROSTATEx-Seg-HiRes](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=61080779)
DICOM dataset to a more friendly nii format. This dataset is not straightforward to convert for various reasons,
for example, you can use [dcm2niix](https://github.com/rordenlab/dcm2niix) to convert the mri images but not the
segmentations, there isn't a one-to-one relation between segmentation slices and mri slices and so on. 
__Remember: this code is far from perfect, it's not well engineered, and it was written for personal necessity.__

## Usage
1. Download the dataset with classic directory names option (both mri and segmentations).
2. Create a new folder (for example named ProstateX) with two sub-folders in it, one for the mri images and one for the segmentations.
3. Place all the folders (ProstateX-0004, ecc...) in the respective sub-folder.
    Do this for both the mri images and the segmentations. Your folder structure should look like this (truncated for clarity):
    ```text
    ProstateX
    ├───mri
    │   ├───ProstateX-0004
    │   ├───ProstateX-0007
    │   ├───ProstateX-0009
    │   └───ProstateX-...
    └───seg
        ├───ProstateX-0004
        ├───ProstateX-0007
        ├───ProstateX-0009
        └───ProstateX-...
    ```

4. Run rename_all_folders.py two times: the first time the _dcm_path_ variable
    should point to the mri sub-folder, the second time it should point to the segmentations sub-folder.
5. Download the [dcm2niix](https://github.com/rordenlab/dcm2niix) executable (dcm2niix.exe) and store it
    where you can use it.
6. Run mri2nii.py adjusting the various paths in it. _dcm_dataset_path_ should
    point to the mri sub-folder, _nii_dataset_path_ to your preferred output folder
    and _converter_ to dcm2niix.exe.
7. Run seg2nii.py adjusting the various paths in it. _dcm_dataset_path_ should
    point to the segmentations sub-folder, and _nii_dataset_path_ should point
    to the same location as before.
8. Enjoy the converted dataset!