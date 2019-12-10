import os
# cropped address
dir_ = r"E:\2_DCGAN_project\cropped"

delete_image = ["0.png", "242.png", "691.png", "697.png", "772.png", "803.png", "1327.png", "1336.png", "1338.png", "1339.png", "1340.png", "1341.png", "1342.png", "1343.png", "1355.png", "1357.png", "1479.png", "1743.png", "1746.png", "1748.png", "1749.png", "1760.png", "1940.png", "1943.png", "2056.png", "2429.png", "2433.png", "2435.png", "2707.png", "2708.png", "2709.png", "2710.png", "2711.png", "2712.png", "2946.png", "2950.png", "3211.png", "3361.png", "3362.png", "3363.png", "3393.png", "3889.png", "3894.png", "3949.png", "4047.png", "4086.png", "4132.png", "4139.png", "4308.png", "4363.png", "4465.png", "4785.png", "4791.png", "4848.png", "6142.png", "6170.png", "6171.png", "6172.png", "6406.png", "6496.png", "6949.png", "6960.png", "6961.png", "6962.png", "6963.png", "7011.png", "7064.png", "7715.png", "7724.png", "7761.png", "7762.png", "7957.png", "7958.png", "8008.png", "8583.png", "8584.png", "9250.png", "9251.png", "9252.png", "9307.png", "9466.png", "9468.png", "9475.png", "9510.png", "9541.png", "9584.png", "9746.png"]
for del_image in delete_image:
    image_add = os.path.join(dir_, del_image)
    if os.path.exists(image_add):
        os.remove(image_add)
print("Complete")
