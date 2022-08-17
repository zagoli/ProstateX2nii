from pathlib import Path
import os
import subprocess as ss

dcm_dataset_path = Path("C:/Users/ML/Desktop/ProstatexJacopo/mri")
nii_dataset_path = Path("C:/Users/ML/Desktop/ProstatexJacopoNII")
converter = Path("C:/Users/ML/Downloads/dcm2niix.exe")
os.mkdir(nii_dataset_path)

assert os.path.exists(dcm_dataset_path)
assert converter.exists()
assert os.path.exists(nii_dataset_path)

dcm_folders = []
for dirpath, subdirs, files in os.walk(dcm_dataset_path):
    if files:
        dcm_folders.append(dirpath)

for dcm_folder in dcm_folders:
    patient_name = dcm_folder.split('\\')[6]
    # output directory creation
    out_path = nii_dataset_path / patient_name
    os.mkdir(out_path)
    # parameters for conversion.
    # -e : export as NRRD (y) or MGH (o) instead of NIfTI (y/n/o, default n)
    # -o : output directory (omit to save to input folder)
    # -b : BIDS sidecar (y/n/o [o=only: no NIfTI], default y)
    # -f : filename (%a=antenna (coil) name, %b=basename, %c=comments, %d=description, %e=echo number, %f=folder name,
    #   %g=accession number, %i=ID of patient, %j=seriesInstanceUID, %k=studyInstanceUID, %m=manufacturer,
    #   %n=name of patient, %o=mediaObjectInstanceUID, %p=protocol, %r=instance number, %s=series number,
    #   %t=time, %u=acquisition number, %v=vendor, %x=study ID; %z=sequence name; default '%f_%p_%t_%s')
    launch_mri = [str(converter), "-e", "n", "-b", "n", "-o", str(out_path), "-f", "MRI_%i", dcm_folder]
    ss.run(launch_mri)



