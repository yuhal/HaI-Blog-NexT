---
title: Java-《Java-简明教程》实验报告
categories: Java
---

![image.png](https://upload-images.jianshu.io/upload_images/15325592-eea6485be830f57c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![Java 简明教程.png](https://upload-images.jianshu.io/upload_images/15325592-8a0432a48634db9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  字符串常用提取方法

| 方法  |  返回值 | 功能描述|
| ------------ | ------------ |------------ |
|indexOf(char ch)|  int |搜索字符 ch 第一次出现的索引
|indexOf(String value)| int |搜索字符串 value 第一次出现的索引
|lastIndexOf(char ch)|  int |搜索字符 ch 最后一次出现的索引
|lastIndexOf(String value)| int |搜索字符串 value 最后一次出现的索引
|substring(int index)|  String  |提取从位置索引开始到结束的字符串
|substring(int beginindex, int endindex)|   String  |提取 beginindex 和 endindex 之间的字符串部分
|trim() |String |返回一个前后不含任何空格的调用字符串的副本

#  算术运算符

| 算术运算符  |  名称 | 描述|类型|举例|
| ------------ | ------------ | ------------ | ------------ | ------------ |
|+  |加法|    相加运算符两侧的值|  双目运算符|  a + b 等于 8
|-  |减法|    左操作数减去右操作数| 双目运算符|  a - b 等于 2
|*  |乘法|    相乘操作符两侧的值|  双目运算符|  a * b 等于 15
|/  |除法|    左操作数除以右操作数| 双目运算符|  a / b 等于 1
|%  |取余|    左操作数除右操作数的余数|   双目运算符|  a % b 等于 2
|++ |自增|    操作数的值增加 1|  单目运算符|  ++i（或 i++） 等于 2
|\-\-   |自减|    操作数的值减少 1|  单目运算符|  \-\-i（或 i\-\-）等于 0

#  位运算符

|算符 |名称 |描述 |举例
| ------------ | ------------ | ------------ | ------------ | 
|&  |按位与    |如果相对应位都是 1，则结果为 1，否则为 0    |（a＆b），得到 12，即 0000 1100
|丨  |按位或    |如果相对应位都是 0，则结果为 0，否则为 1    |（ a 丨 b ）得到 61，即 0011 1101
|^  |按位异或   |如果相对应位值相同，则结果为 0，否则为 1 |（a^b）得到 49，即 0011 0001
|~  |按位补    |翻转操作数的每一位，即 0 变成 1，1 变成 0  |（〜a）得到 -61，即 1100 0011
|<< |按位左移   |左操作数按位左移右操作数指定的位数| a<<2 得到 240，即 1111 0000
|>> |按位右移   |左操作数按位右移右操作数指定的位数| a>>2 得到 15 即 1111
|>>>    |按位右移补零 |左操作数的值按右操作数指定的位数右移，移动得到的空位以零填充|    a>>>2 得到 15 即 0000 1111

#  逻辑运算符

|逻辑运算符  |名称 |描述 |类型 |举例
| ------------ | ------------ | ------------ | ------------ | ------------ |
|&& 或 & |与  |当且仅当两个操作数都为真，条件才为真 |双目运算符| (a && b) 或 (a & b) 为假
|丨丨 或 丨 |或  |两个操作数任何一个为真，条件为真   |双目运算符  |（a 丨丨 b) 或 (a 丨 b) 为真
|!  |非  |用来反转操作数的逻辑状态。如果条件为真，则逻辑非运算符将得到假    |单目运算符| （!a）为假
|^  |异或 |如果两个操作数逻辑相同，则结果为假，否则为真 |双目运算符| (a ^ b) 为真

#  关系运算符

|比较运算符  |名称 |描述|    举例|
| ------------ | ------------ | ------------ | ------------ |
|== |等于 |判断两个操作数的值是否相等，如果相等则条件为真    |(a == b） 为 false
|!= |不等于    |判断两个操作数的值是否相等，如果值不相等则条件为真  |(a != b) 为 true
|>  |大于 |判断左操作数的值是否大于右操作数的值，如果是那么条件为真   |(a > b) 为 false
|<  |小于 |判断左操作数的值是否小于右操作数的值，如果是那么条件为真   |(a < b) 为 true
|>= |大于等于   |判断左操作数的值是否大于或等于右操作数的值，如果是那么条件为真|   (a >= b) 为 false
|<= |小于等于   |判断左操作数的值是否小于或等于右操作数的值，如果是那么条件为真|   (a <= b) 为 true

#  Arrays 常用方法

|  方法 | 描述   |
| ------------ | ------------ |
|<T> List<T> asList(T... a) |返回由指定数组构造的 List
|void sort(Object[] a)  |对数组进行排序
|void fill(Object[] a, Object val)  |为数组的所有元素都赋上相同的值
|boolean equals(Object[] a, Object[] a2)    |检查两个数组是否相等
|int binarySearch(Object[] a, Object key)   |对排序后的数组使用二分法查找数据

#  StringBuilder 的构造方法

|构造方法   |说明
| ------------ | ------------ |
|StringBuilder()    |构造一个其中不带字符的 StringBuilder，其初始容量为 16 个字符
|StringBuilder(CharSequence seq)    |构造一个 StringBuilder，它包含与指定的 CharSequence 相同的字符
|StringBuilder(int capacity)    |构造一个具有指定初始容量的 StringBuilder
|StringBuilder(String str)  |并将其内容初始化为指定的字符串内容

#  StringBuilder 类的常用方法

|方法 |返回值    |功能描述
| ------------ | ------------ |------------ |
|insert(int offsetm,Object obj) |StringBuilder  |在 offsetm 的位置插入字符串 obj
|append(Object obj) |StringBuilder  |在字符串末尾追加字符串 obj
|length()   |int    |确定 StringBuilder 对象的长度
|setCharAt(int index,char ch)   |void   |使用 ch 指定的新值设置 index 指定的位置上的字符
|toString() |String |转换为字符串形式
|reverse()  |StringBuilder  |反转字符串
|delete(int start, int end) |StringBuilder  |删除调用对象中从 start 位置开始直到 end 指定的索引（end-1）位置的字符序列
|replace(int start, int end, String str)    |StringBuilder  |使用一组字符替换另一组字符。将用替换字符串从 start 指定的位置开始替换，直到 end 指定的位置结束

#  GregorianCalendar 类的构造函数

|构造方法   |说明
| ------------ | ------------ |
|GregorianCalendar()    |创建的对象中的相关值被设置成指定时区，缺省地点的当前时间，即程序运行时所处的时区、地点的当前时间
|GregorianCalendar(TimeZone zone)   |创建的对象中的相关值被设置成指定时区 zone，缺省地点的当前时间
|GregorianCalendar(Locale aLocale)  |创建的对象中的相关值被设置成缺省时区，指定地点 aLocale 的当前时间
|GregorianCalendar(TimeZone zone,Locale aLocale)    |year - 创建的对象中的相关值被设置成指定时区，指定地点的当前时间

#  Date 中定义的未过时的构造方法

|构造方法   |说明
| ------------ | ------------ |
|Date() |构造一个 Date 对象并对其进行初始化以反映当前时间
|Date(long date)    |构造一个 Date 对象，并根据相对于 GMT 1970 年 1 月 1 日 00:00:00 的毫秒数对其进行初始化

#  Math 常见方法

|方法 |返回值    |功能描述
| ------------ | ------------ |------------ |
|sin(double numvalue)   |double|    计算角 numvalue 的正弦值
|cos(double numvalue)   |double|    计算角 numvalue 的余弦值
|acos(double numvalue)  |double|    计算 numvalue 的反余弦
|asin(double numvalue)  |double|    计算 numvalue 的反正弦
|atan(double numvalue)  |double|    计算 numvalue 的反正切
|pow(double a, double b)    |double|    计算 a 的 b 次方
|sqrt(double numvalue)  |double|    计算给定值的正平方根
|abs(int numvalue)  |int|   计算 int 类型值 numvalue 的绝对值，也接收 long、float 和 double 类型的参数
|ceil(double numvalue)  |double|    返回大于等于 numvalue 的最小整数值
|floor(double numvalue) |double|    返回小于等于 numvalue 的最大整数值
|max(int a, int b)  |int|   返回 int 型 a 和 b 中的较大值，也接收 long、float 和 double 类型的参数
|min(int a, int b)  |int|   返回 a 和 b 中的较小值，也可接受 long、float 和 double 类型的参数
|rint(double numvalue)  |double|    返回最接近 numvalue 的整数值
|round(T arg)   |arg| 为 double 时返回 long，为 float 时返回 int 返回最接近 arg 的整数值
|random()   |double|    返回带正号的 double 值，该值大于等于 0.0 且小于 1.0

#  Collection 操作 List、Set 和 Queue 的方法

| 方法  | 返回值  |说明
| ------------ | ------------ |------------ |
|add(E e)   |boolean    |向 collection 的尾部追加指定的元素（可选操作）
|addAll(Collection<? extend E> c)   |boolean|   将指定 collection 中的所有元素都添加到此 collection 中（可选操作）
|clear()    |void|  移除此 collection 中的所有元素（可选操作）
|contains(Object o) |boolean|   如果此 collection 包含指定的元素，则返回 true
|containsAll(Collection<?> c)   |boolean|   如果此 collection 包含指定 collection 的所有元素，则返回 true
|equals(Object o)   |boolean|   比较此 collection 与指定对象是否相等
|hashCode() |int|   返回此 collection 的哈希码值
|isEmpty()  |boolean|   如果此 collection 不包含元素，则返回 true
|iterator() |Iterator|  返回在此 collection 的元素上进行迭代的迭代器
|remove(Object o)   |boolean|   移除此 collection 中出现的首个指定元素（可选操作）
|removeAll(Collection<?> c) |boolean|   移除此 collection 中那些也包含在指定 collection 中的所有元素（可选操作）
|retainAll(Collection<?> c) |boolean|   仅保留此 collection 中那些也包含在指定 collection 的元素（可选操作）
|size() |int|   返回此 collection 中的元素数
|toArray()  |Object[]|  返回包含此 collection 中所有元素的数组
|toArray(T[] a) |T[]|   返回包含此 collection 中所有元素的数组；返回数组的运行时类型与指定数组的运行时类型相同

#  List 在 Collection 基础上增加的方法

|方法 |返回值|   说明
| ------------ | ------------ |------------ |
|add(int index, E element)  |void|  在列表的指定位置插入指定元素（可选操作）
|addAll(int index, Collection<? extends E> c)   |boolean|   将指定 collection 中的所有元素都插入到列表中的指定位置（可选操作）
|get(int index) |E| 返回列表中指定位置的元素
|indexOf(Object o)  |int|   返回此列表中第一次出现的指定元素的索引；如果此列表不包含该元素，则返回 -1
|lastIndexOf(Object o)  |int|   返回此列表中最后出现的指定元素的索引；如果列表不包含此元素，则返回 -1
|listIterator() |ListIterator|  返回此列表元素的列表迭代器（按适当顺序）
|listIterator(int index)    |ListIterator|  返回此列表元素的列表迭代器（按适当顺序），从列表的指定位置开始
|remove(int index)  |E| 移除列表中指定位置的元素（可选操作）
|set(int index, E element)  |E| 用指定元素替换列表中指定位置的元素（可选操作）
|subList(int fromIndex, int toIndex)    |List|  返回列表中指定的 fromIndex（包括 ）和 toIndex（不包括）之间的部分视图

#  Map 中的方法

|方法 |返回值|   说明|
| ------------ | ------------ |------------ |
|clear()    |void|  从此映射中移除所用映射关系（可选操作）
|containsKey(Object key)    |boolean|   如果此映射包含指定键的映射关系，则返回 true
|containsValue(Object value)    |boolean|   如果此映射将一个或多个键映射到指定值，则返回 true
|entrySet() |Set<Map.Entry<K,V>>|   返回此映射中包含的映射关系的 Set 视图
|equals(Object o)   |boolean|   比较指定的对象与此映射是否相等
|get(Object key)    |V| 返回指定键所映射的值；如果此映射不包含该键的映射关系，则返回 null
|hashCode() |int|   返回此映射的哈希码值
|isEmpty()  |boolean|   如果此映射未包含键 - 值映射关系，则返回 true
|keySet()   |Set|   返回此映射中包含的键的 Set 视图
|put(K key, V value)    |V| 将指定的值与此映射中的指定键关联（可选操作）
|putAll(Map<? extends K, ? extends V> m)    |void|  从指定映射中将所有映射关系复制到此映射中（可选操作）
|remove(Object key) |V| 如果存在一个键的映射关系，则将其从此映射中移除（可选操作）
|size   |int|   返回此映射中的键 - 值映射关系数
|values()   |Collection|    返回此映射中包含的值的 Collection 视图

#  Collections 中对集合进行操作的静态方法

|方法名    |描述|
| ------------ | ------------ |
|void sort(List list)   |按自然升序排序
|void sort(List list, Comparator c) |自定义排序规则排序
|void shuffle(List list)    |随机排序，用于打乱顺序
|void reverse(List list)    |反转，将列表元素顺序反转
|void swap(List list, int i , int j)    |交换处于索引 i 和 j 位置的元素
|int binarySearch(List list, Object key)    |二分查找，列表必须有序，返回找到的元素索引位置
|int max(Collection coll)   |查找最大值
|int min(Collection coll)   |查找最小值
|void fill(List list, Object obj)   |使用 obj 填充 list 所有元素
|boolean replaceAll(List list, Object oldVal, Object newVal)    |使用用 newVal 替换所有的 oldVal。
|<K,V> Map<K,V> synchronizedMap(Map<K,V> m) |将 m 包装为线程安全的 Map
|List synchronizedList(List list)   |将 list 包装为线程安全的 List

#  常用函数式接口

| 接口      | 描述  |
| ------------ | ------------ |
|BiConsumer<T,U>    |该接口代表了接收两个输入参数 T、U，并且没有返回的操作
|BiFunction<T,U,R>  |该接口代表提供接收两个参数 T、U，并且产生一个结果 R 的方法
|BinaryOperator |代表了基于两个相同类型的操作数，产生仍然是相同类型结果的操作
|BiPredicate<T,U>   |代表了对两个参数的断言操作（基于 Boolean 值的方法）
|BooleanSupplier    |代表了一个给出 Boolean 值结果的方法
|Consumer   |代表了接受单一输入参数并且没有返回值的操作
|DoubleBinaryOperator   |代表了基于两个 Double 类型操作数的操作，并且返回一个 Double 类型的返回值
|DoubleConsumer |代表了一个接受单个 Double 类型的参数并且没有返回的操作
|DoubleFunction |代表了一个接受 Double 类型参数并且返回结果的方法
|DoublePredicate    |代表了对一个 Double 类型的参数的断言操作
|DoubleSupplier |代表了一个给出 Double 类型值的方法
|DoubleToIntFunction    |代表了接受单个 Double 类型参数但返回 Int 类型结果的方法
|DoubleToLongFunction   |代表了接受单个 Double 类型参数但返回 Long 类型结果的方法
|DoubleUnaryOperator    |代表了基于单个 Double 类型操作数且产生 Double 类型结果的操作
|Function<T,R>  |代表了接受一个参数并且产生一个结果的方法
|IntBinaryOperator  |代表了对两个 Int 类型操作数的操作，并且产生一个 Int 类型的结果
|IntConsumer    |代表了接受单个 Int 类型参数的操作，没有返回结果
|IntFunction    |代表了接受 Int 类型参数并且给出返回值的方法
|IntPredicate   |代表了对单个 Int 类型参数的断言操作

#  File 类的构造方法

| 方法  | 说明|
| ------------ | ------------ |
| File(File parent, String child)  |  根据 parent 抽象路径名和 child 路径名字符串创建一个新 File 实例 |
| File(String pathname)  | 通过将给定路径名字符串转换为抽象路径名来创建一个新 File 实例  |
| File(String parent, String child) | 根据 parent 路径名字符串和 child 路径名字符串创建一个新 File 实例  |
| File(URI uri) | 通过将给定的 file: URI 转换为一个抽象路径名来创建一个新的 File 实例  |

#  File 类的常用方法

| 方法  | 说明|
| ------------ | ------------ |
|boolean canExecute()   |测试应用程序是否可以执行此抽象路径名表示的文件
|boolean canRead()  |测试应用程序是否可以读取此抽象路径名表示的文件
|boolean canWrite() |测试应用程序是否可以修改此抽象路径名表示的文件
|int compareTo(File pathname)   |按字母顺序比较两个抽象路径名
|boolean createNewFile()    |当且仅当不存在具有此抽象路径名指定名称的文件时，不可分地创建一个新的空文件
|static File createTempFile(String prefix, String suffix)   |在默认临时文件目录中创建一个空文件，使用给定前缀和后缀生成其名称
|static File createTempFile(String prefix, String suffix, File directory)   |在指定目录中创建一个新的空文件，使用给定的前缀和后缀字符串生成其名称
|boolean delete()   |删除此抽象路径名表示的文件或目录
|void deleteOnExit()    |在虚拟机终止时，请求删除此抽象路径名表示的文件或目录
|boolean equals(Object obj) |测试此抽象路径名与给定对象是否相等
|boolean exists()   |测试此抽象路径名表示的文件或目录是否存在
|File getAbsoluteFile() |返回此抽象路径名的绝对路径名形式
|String getAbsolutePath()   |返回此抽象路径名的绝对路径名字符串
|File getCanonicalFile()    |返回此抽象路径名的规范形式
|String getCanonicalPath()  |返回此抽象路径名的规范路径名字符串
|long getFreeSpace()    |返回此抽象路径名指定的分区中未分配的字节数
|String getName()   |返回由此抽象路径名表示的文件或目录的名称
|String getParent() |返回此抽象路径名父目录的路径名字符串；如果此路径名没有指定父目录，则返回 null
|File getParentFile()   |返回此抽象路径名父目录的抽象路径名；如果此路径名没有指定父目录，则返回 null
|String getPath()   |将此抽象路径名转换为一个路径名字符串
|long getTotalSpace()   |返回此抽象路径名指定的分区大小
|long getUsableSpace()  |返回此抽象路径名指定的分区上可用于此虚拟机的字节数
|int hashCode() |计算此抽象路径名的哈希码
|boolean isAbsolute()   |测试此抽象路径名是否为绝对路径名
|boolean isDirectory()  |测试此抽象路径名表示的文件是否是一个目录
|boolean isFile()   |测试此抽象路径名表示的文件是否是一个标准文件
|boolean isHidden() |测试此抽象路径名指定的文件是否是一个隐藏文件
|long lastModified()    |返回此抽象路径名表示的文件最后一次被修改的时间
|long length()  |返回由此抽象路径名表示的文件的长度
|String[] list()    |返回一个字符串数组，这些字符串指定此抽象路径名表示的目录中的文件和目录
|String[] list(FilenameFilter filter)   |返回一个字符串数组，这些字符串指定此抽象路径名表示的目录中满足指定过滤器的文件和目录
|File[] listFiles() |返回一个抽象路径名数组，这些路径名表示此抽象路径名表示的目录中的文件
|File[] listFiles(FileFilter filter)    |返回抽象路径名数组，这些路径名表示此抽象路径名表示的目录中满足指定过滤器的文件和目录
|File[] listFiles(FilenameFilter filter)    |返回抽象路径名数组，这些路径名表示此抽象路径名表示的目录中满足指定过滤器的文件和目录
|static File[] listRoots()  |列出可用的文件系统根
|boolean mkdir()    |创建此抽象路径名指定的目录
|boolean mkdirs()   |创建此抽象路径名指定的目录，包括所有必需但不存在的父目录
|boolean renameTo(File dest)    |重新命名此抽象路径名表示的文件
|boolean setExecutable(boolean executable)  |设置此抽象路径名所有者执行权限的一个便捷方法
|boolean setExecutable(boolean executable, boolean ownerOnly)   |设置此抽象路径名的所有者或所有用户的执行权限
|boolean setLastModified(long time) |设置此抽象路径名指定的文件或目录的最后一次修改时间
|boolean setReadable(boolean readable)  |设置此抽象路径名所有者读权限的一个便捷方法
|boolean setReadable(boolean readable, boolean ownerOnly)   |设置此抽象路径名的所有者或所有用户的读权限
|boolean setReadOnly()  |标记此抽象路径名指定的文件或目录，从而只能对其进行读操作
|boolean setWritable(boolean writable)  |设置此抽象路径名所有者写权限的一个便捷方法
|boolean setWritable(boolean writable, boolean ownerOnly)   |设置此抽象路径名的所有者或所有用户的写权限
|String toString()  |返回此抽象路径名的路径名字符串
|URI toURI()    |构造一个表示此抽象路径名的 file: URI

#  RandomAccessFile 随机文件操作的方法

| 方法  | 说明|
| ------------ | ------------ |
|int skipBytes(int n)| 将指针向下移动若干字节。
|int length()| 返回文件长度。
|long getFilePointer()| 返回指针当前位置。
|void seek(long pos)| 将指针调用所需位置。

#  InputStream 类方法

|方法 |说明
| ------------ | ------------ |
|read()throws IOException   |从输入流中读取数据的下一个字节（抽象方法）
|skip(long n) throws IOException    |跳过和丢弃此输入流中数据的 n 个字节
|available()throws IOException  |返回流中可用字节数
|mark(int readlimit)throws IOException  |在此输入流中标记当前的位置
|reset()throws IOException  |将此流重新定位到最后一次对此输入流调用 mark 方法时的位置
|markSupport()throws IOException    |测试此输入流是否支持 mark 和 reset 方法
|close()throws IOException  |关闭流

#  OutputStream 类方法

|方法 |说明
| ------------ | ------------ |
|write(int b)throws IOException |将指定的字节写入此输出流（抽象方法）
|write(byte b[])throws IOException  |将字节数组中的数据输出到流中
|write(byte b[], int off, int len)throws IOException    |将指定 byte 数组中从偏移量 off 开始的 len 个字节写入此输出流
|flush()throws IOException  |刷新此输出流并强制写出所有缓冲的输出字节
|close()throws IOException  |关闭流
 
 #  Reader 类方法
 
| 方法    |返回值
 | ------------ | ------------ |
|close()    |void
|mark (int readAheadLimit)  |void
|markSupported()    |boolean
|read() |int
|read(char[] cbuf, int off,int len) |int
|ready()    |boolean
|reset()    |void
|skip(long n)   |long

 #  Writer  类方法

|方法  |返回值
| ------------ | ------------ |
|close()     |void
|flush()     |void
|write(char[] cbuf)  |void
|write(char[] cbuf, int off,int len)     |void
|write(int c)    |void
|write(String str)   |void
|write(String str, int off, int len)     |void

#  InetAddress 类常用方法

|  方法 | 作用  |
| ------------ | ------------ |
|getLocalHost()|返回本地主机地址
|getAllByName（String host）|从指定的主机名返回 InetAddress 对象的数组，因为主机名可以与多个 IP 地址相关联。
|getByAddress（byte [] addr）|从原始 IP 地址的字节数组中返回一个 InetAddress 对象。
|getByName（String host）|根据提供的主机名创建一个 InetAddress 对象。
|getHostAddress()|返回文本表示的 IP 地址字符串。
|getHostname()|获取主机名。

#  TCP 和 UDP 的区别

|   |  TCP |UDP|
| ------------ | ------------ |------------ |
| 是否连接  | 面向连接  |面向非连接|
| 传输可靠性  | 可靠  |不可靠|
| 应用场合  |  少量数据 |传输大量数据|
| 速度  |  慢 |快|

#  Socket  和 ServerSocket 的区别

|   |  Socket |ServerSocket|
| ------------ | ------------ |------------ |
| 运行环境 | 客户端  |服务端|
| 作用  | 向服务器发送和接受数据  |等待客户端网络连接之后，然后将结果返回给客户端|

#  ArrayBlockingQueue 构造方法

|构造方法   |描述|
| ------------ | ------------ |
|public ArrayBlockingQueue(int capacity)    |构造大小为 capacity 的队列
|public ArrayBlockingQueue(int capacity, boolean fair)  |指定队列大小，以及内部实现是公平锁还是非公平锁
|public ArrayBlockingQueue(int capacity, boolean fair, Collection<? extends E> c)   |指定队列大小，以及锁实现，并且在初始化是加入集合 c

#  ArrayBlockingQueue 入队常用方法

|入队方法    |队列已满   |队列未满 |
| ------------ | ------------ | ------------ |
|add    |抛出异常   |返回 true|
|offer  |返回 false   |返回 true|
|put    |阻塞直到插入 |没有返回值|

#  ArrayBlockingQueue 出队常用方法

|出队方法   |队列为空   |队列不为空|
| ------------ | ------------ | ------------ |
|remove |抛出异常   |移出并返回队首|
|poll   |返回 null    |移出并返回队首|
|take   |阻塞直到返回 |移出并返回队首|

#  常用数据库的连接 URL

|RDBMS  |JDBC 驱动程序的名称   |URL
| ------------ | ------------ |------------ |
|Mysql  |com.mysql.jdbc.Driver  |jdbc:mysql://hostname/ databaseName
|Oracle |oracle.jdbc.driver.OracleDriver    |jdbc:oracle:thin:@hostname:port Number:databaseName
|DB2    |COM.ibm.db2.jdbc.net.DB2Driver |jdbc:db2:hostname:port Number/databaseName
|Sybase |com.sybase.jdbc.SybDriver  |jdbc:sybase:Tds:hostname: port Number/databaseName

#  CollableStatement

|参数 | 描述
 | ------------ |------------ |
|IN |它的值是在创建 SQL 语句时未知的参数，将 IN 参数传给 CallableStatement 对象是通过 setXXX() 方法完成的
|OUT    |其值由它返回的 SQL 语句提供的参数。从 OUT 参数的 getXXX() 方法检索值
|INOUT  |同时提供输入和输出值的参数，绑定的 setXXX() 方法的变量，并使用 getXXX() 方法检索值

#  Statement 

|方法  |说明
 | ------------ |------------ |
 |boolean execute(String SQL)    |如果 ResultSet 对象可以被检索返回布尔值 true，否则返回 false。使用这个方法来执行 SQL DDL 语句，或当需要使用真正的动态 SQL
 |int executeUpdate(String SQL)  |用于执行 INSERT、UPDATE 或 DELETE 语句以及 SQLDDL（数据定义语言）语句。返回值是一个整数，指示受影响的行数（即更新计数）
 |ResultSet executeQuery(String SQL)     |返回 ResultSet 对象。用于产生单个结果集的语句，例如 SELECT 语句
 
#  ResultSet 导航方法

|方法 |说明
 | ------------ |------------ |
|public void beforeFirst() throws SQLException  |将光标移动到正好位于第一行之前
|public void afterLast() throws SQLException    |将光标移动到刚刚结束的最后一行
|public boolean first() throws SQLException |将光标移动到第一行
|public void last() throws SQLException |将光标移动到最后一行
|public boolean absolute(int row) throws SQLException   |将光标移动到指定的行
|public boolean relative(int row) throws SQLException   |从它目前所指向向前或向后移动光标行的给定数量
|public boolean previous() throws SQLException  |将光标移动到上一行。上一行关闭的结果集此方法返回 false
|public boolean next() throws SQLException  |将光标移动到下一行。如果没有更多的行结果集中的此方法返回 false
|public int getRow() throws SQLException    |返回的行号，该光标指向的行
|public void moveToInsertRow() throws SQLException  |将光标移动到一个特殊的行，可以用来插入新行插入到数据库中的结果集。当前光标位置被记住
|public void moveToCurrentRow() throws SQLException |移动光标返回到当前行，如果光标在当前插入行，否则，这个方法不执行任何操作

#  ResultSet 获取方法

|方法 |说明
 | ------------ |------------ |
|public int getInt(String columnName) throws SQLException   |当前行中名为 ColumnName 列的值
|public int getInt(int columnIndex) throws SQLException |当前行中指定列的索引的值。列索引从 1 开始，意味着一个行的第一列是 1，行的第二列是 2，依此类推

#  ResultSet 更新方法

|方法 |说明
 | ------------ |------------ |
|public void updateString(int columnIndex, String s) throws SQLException    |指定列中的字符串更改为 s 的值
|public void updateString(String columnName, String s) throws SQLException  |类似于前面的方法，不同之处在于由它的名称，而不是它的索引指定的列
|public void updateRow()    |通过更新数据库中相应的行更新当前行
|public void deleteRow()    |从数据库中删除当前行
|public void refreshRow()   |刷新在结果集的数据，以反映最新变化在数据库中
|public void cancelRowUpdates() |取消所做的当前行的任何更新
|public void insertRow()    |插入一行到数据库中。当光标指向插入行此方法只能被调用

#  Class 类常用方法

|方法 |描述|
| ------------ | ------------ |
|Field getField(String name)    |获取指定的域对象
|Field[] getFields()    |返回所有的公有域对象数组
|Method getDeclaredMethod(String name, Class<?>... parameterTypes)  |返回指定的方法对象
|Method[] getMethods()  |返回所有的公有方法对象数组
|Method[] getDeclaredMethods()  |返回所有方法对象数组
