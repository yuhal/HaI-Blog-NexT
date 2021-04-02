---
title: Leecode-设计停车系统
categories: Leecode
---
![WechatIMG597.jpeg](https://upload-images.jianshu.io/upload_images/15325592-29b6e502a8fe4979.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第1603题：[设计停车系统](https://leetcode-cn.com/problems/design-parking-system/)
请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
请你实现 ParkingSystem 类：
ParkingSystem(int big, int medium, int small) 初始化 ParkingSystem 类，三个参数分别对应每种停车位的数目。
bool addCar(int carType) 检查是否有 carType 对应的停车位。 carType 有三种类型：大，中，小，分别用数字 1， 2 和 3 表示。一辆车只能停在  carType 对应尺寸的停车位中。如果没有空车位，请返回 false ，否则将该车停入车位并返回 true 。
示例 1：
输入：
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
输出：
[null, true, true, false, false]
解释：
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // 返回 true ，因为有 1 个空的大车位
parkingSystem.addCar(2); // 返回 true ，因为有 1 个空的中车位
parkingSystem.addCar(3); // 返回 false ，因为没有空的小车位
parkingSystem.addCar(1); // 返回 false ，因为没有空的大车位，唯一一个大车位已经被占据了

#  解题方法

> 模拟
[参照题解](https://leetcode-cn.com/problems/design-parking-system/solution/ru-he-she-ji-ting-che-xi-tong-fu-tuo-zha-4363/)

- 解题思路

> 创建数组`pack`当作计数器，
下标[1-3]分别记录当前剩余的大、中、小尺寸的车位数量
每停一辆车，就将对应尺寸车位的数量减1
当某个尺寸车位的数量为0时，说明车位已满

- 复杂度

> 时间复杂度：O(1)
空间复杂度：O(1)

- 代码实现

> python3

```
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.park = [0,big,medium,small]

    def addCar(self, carType: int) -> bool:
        if self.park[carType]>0:
            self.park[carType]-=1
            return True
        return False
```

> php

```
class ParkingSystem {
    function __construct($big, $medium, $small) {
        $this->park = [0,$big,$medium,$small];
    }

    function addCar($carType) {
        if($this->park[$carType]>0){
            $this->park[$carType]--;
            return true;
        }
        return false;
    }
}
```
