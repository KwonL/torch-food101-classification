import os
import shutil


ORG_DATA_DIR = "./food-101/images/"
DST_DATA_DIR = "./data/"


tag_list = os.listdir(ORG_DATA_DIR)
tag_cnt = 1
for tag in tag_list:
    print(
        f"now processing {tag} and progress is.. [{tag_cnt}/{len(tag_list)}]"
    )
    os.makedirs(os.path.join(DST_DATA_DIR, f"train/{tag}"), exist_ok=True)
    os.makedirs(os.path.join(DST_DATA_DIR, f"val/{tag}"), exist_ok=True)

    file_list = os.listdir(os.path.join(ORG_DATA_DIR, tag))
    cnt = 0
    for file in file_list:
        if cnt < len(file_list) * 0.8:
            shutil.copy2(
                os.path.join(ORG_DATA_DIR, f"{tag}/{file}"),
                os.path.join(DST_DATA_DIR, f"train/{tag}"),
            )
        else:
            shutil.copy2(
                os.path.join(ORG_DATA_DIR, f"{tag}/{file}"),
                os.path.join(DST_DATA_DIR, f"val/{tag}"),
            )
        cnt += 1
    tag_cnt += 1
