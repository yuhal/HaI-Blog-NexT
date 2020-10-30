---
title: Java-观察者模式
categories: Java
---
![WechatIMG147.jpeg](https://upload-images.jianshu.io/upload_images/15325592-575e99fc5121aa64.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  介绍
> shiyanlou:在此种模式中，一个目标对象管理所有相依于它的观察者对象，并且在它本身的状态改变时主动发出通知。这通常透过呼叫各观察者所提供的方法来实现。此种模式通常被用来实时事件处理系统。观察者模式又叫做发布-订阅（Publish/Subscribe）模式、模型-视图（Model/View）模式、源-监听器（Source/Listener）模式或从属者（Dependents）模式。


#  角色 

|角色|    说明|
| ------------ | ------------ |
|Subject|抽象目标类，一般至少提供三个接口：<br/>添附(attach)<br/>解附(detach)<br/>通知(notify)|
|ConcreteSubject|具体目标，提供了观察者欲追踪的状态，也可设置目标状态|
|Observer| 抽象观察者，定义观察者的更新操作接口|
|ConcreteObserver|具体观察者，实现抽象观察者的接口，做出自己的更新操作|

#  角色示例

|类名 |担任角色|  说明|
| ------------ | ------------ |------------ |
|OfficialAccount|Subject|微信公众号，提供三个接口：<br/>关注(follow)<br/>取关(unFollow)<br/>推送(send)|
|MyOfficialAccount|ConcreteSubject|我的微信公众号|
|User|Observer|用户|
|Developer|ConcreteObserver|开发者|

#  UML类图


![观察者模式.png](https://upload-images.jianshu.io/upload_images/15325592-ade1f0ddf5817046.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->



#  代码

- 创建 User.java，代码如下

```
abstract class User {
    abstract public String receive(OfficialAccount officialAccount);
    abstract public String getUsername();
}
```

- 创建 Developer.java，代码如下

```
public class Developer extends User {
    protected String name;

    public Developer(String name){
        this.name = name;
    }

    @Override
    public String receive(OfficialAccount officialAccount) {
        return this.name+"接收到推送的文章："+officialAccount.getArticle()+"\n";
    }

    @Override
    public String getUsername(){
        return this.name;
    }
}
```

- 创建 OfficialAccount.java，代码如下

```
import java.util.ArrayList;

abstract class OfficialAccount {
    private ArrayList<User> userList;

    public OfficialAccount(){
        userList = new ArrayList<User>();
    }
    
    public String follow(User user) {
        userList.add(user);
        return user.getUsername()+" 关注了公众号";
    }

    public String unFollow(User user) {
        userList.remove(user);
        return user.getUsername()+" 取关了公众号";
    }

    public String send() {
        String sendLog = "";
        for (User user: userList) {
            sendLog += user.receive(this);
        }
        return sendLog;
    }

    abstract public void setArticle(String article);

    abstract public String getArticle();
}
```

- 创建 MyOfficialAccount.java，代码如下

```
public class MyOfficialAccount extends OfficialAccount{

    private String article;

    public void setArticle(String article) {
        this.article = article;
    }

    public String getArticle() {
        return this.article;
    }
}
```

- 创建 OfficialAccountTest.java，代码如下

```
public class OfficialAccountTest {
    public static void main(String[] args) {
        OfficialAccount myOfficialAccount = new MyOfficialAccount();

        User alan = new Developer("Alan");
        User bob = new Developer("Bob");
        
        System.out.println(myOfficialAccount.follow(alan));
        System.out.println(myOfficialAccount.follow(bob));

        myOfficialAccount.setArticle("《关于作者》");
        System.out.println(myOfficialAccount.send());
        
        myOfficialAccount.setArticle("《Java 观察者模式》");
        System.out.println(myOfficialAccount.unFollow(bob));
        System.out.println(myOfficialAccount.send());
    }
}
```

#  执行

```
$ javac OfficialAccountTest.java
$ java OfficialAccountTest
Alan 关注了公众号
Bob 关注了公众号
Alan 接收到推送的文章：《关于作者》
Bob 接收到推送的文章：《关于作者》
Bob 取关了公众号
Alan 接收到推送的文章：《设计模式 观察者模式》
```
