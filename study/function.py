def calculate_sector(central_angle, radius):  # central_angle,radius是参数
    # 定义函数的代码
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇形面积为：{sector_area}")


sector_area_1 = calculate_sector(160, 30)
sector_area_2 = calculate_sector(60, 15)
sector_area_3 = calculate_sector(30, 16)
# 定义的时候不会被执行，调用的时候才会被执行
