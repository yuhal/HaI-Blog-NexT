---
title: Laravel-Homestead下的环境配置和安装
categories: Laravel
---
![WechatIMG3.jpeg](https://upload-images.jianshu.io/upload_images/15325592-9fe3e3933bc42ecb.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- VirtualBox 6.1.10

> VitrualBox 是一个非常强大的免费虚拟机软件。

- Vagrant 2.2.9

> Vagrant 是一个用于创建和部署虚拟化开发环境的工具，依赖于 VirtualBox 虚拟机。

- Homestead 0.6.0

> HomesteadBox 是一个 Laravel 官方预装的适合 Laravel 开发的 Vagrant box。其中内置了  Laravel 开发时所需要用到的各种软件，例如 Ubuntu 14.04、Git、PHP 5.6 / 7.0、Xdebug、HHVM、Nginx、MySQL、Sqlite3、Postgres、Composer......

#  安装VirtualBox

- 下载 

![www.virtualbox.org_wiki_Downloads.png](https://upload-images.jianshu.io/upload_images/15325592-ca7d3130b55ef99c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 访问 [VirtualBox 官网](https://www.virtualbox.org/wiki/Downloads "VirtualBox 官网")，选择当前操作系统相对应的安装包进行下载。当前的操作系统是 macOS，这里选择的是 OS X hosts。

- 安装 

![Screen Shot 2020-07-14 at 2.48.22 PM.png](https://upload-images.jianshu.io/upload_images/15325592-0ef2d9a57f6beb46.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 下载完成后，双击打开按照提示完成安装即可。

#  安装Vagrant

- 下载 

![www.vagrantup.com_downloads.html.png](https://upload-images.jianshu.io/upload_images/15325592-d721d78396716020.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 访问 [Vagrant 官网](https://www.vagrantup.com/downloads.html "Vagrant 官网")，选择当前操作系统相对应的安装包进行下载。这里选择的是 Mac OS X 64-bit。

- 安装 

![Screen Shot 2020-07-14 at 2.56.45 PM.png](https://upload-images.jianshu.io/upload_images/15325592-fcbd7d920258b3d2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 下载完成后，双击打开按照提示完成安装即可。

#  安装HomesteadBox

- 下载

![pan.baidu.com_s_1hrN55w4.png](https://upload-images.jianshu.io/upload_images/15325592-be9a565761ac7990.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 这里手动安装 HomesteadBox ，访问 [大佬的网盘](http://pan.baidu.com/s/1hrN55w4  "大佬的网盘")，选择最新的版本进行下载。这里选择的是 homestead-virtualbox-0.6.0.box。

- 创建 metadata.json，内容如下：

```
{
    "name": "laravel/homestead",
    "versions": 
    [
        {
            "version": "0.6.0",
            "providers": [
                {
                  "name": "virtualbox",
                  "url": "homestead-virtualbox-0.6.0.box"
                }
            ]
        }
    ]
}
```

> 这里创建的 metadata.json 要与下载的 homestead-virtualbox-0.6.0.box 在同一级目录。

- 添加

> 进入 metadata.json 所在目录，执行`vagrant box add metadata.json`把 homestead-virtualbox-0.6.0.box 添加到 vagrant box。

- 查看

```
$ vagrant box list
laravel/homestead (virtualbox, 0.6.0)
```

#  安装Homestead

- 克隆

```
$ git clone https://github.com/laravel/homestead.git Homestead
```

> 克隆完后，会生成一个 Homestead 文件夹，进入该目录执行`bash init.sh`会在根目录生成 Homestead.yaml 配置文件。

- 修改 Homestead.yaml 内容如下：

```
---
ip: "192.168.10.10"
#  虚拟机的 ip

version: "0.6.0"
#  虚拟机对应 HomesteadBox 版本

memory: 2048
#  虚拟机的内存

cpus: 2
#  虚拟机的 CPU

provider: virtualbox
#  虚拟机的默认提供者

authorize: ~/.ssh/id_rsa.pub
#  公钥

keys:
    - ~/.ssh/id_rsa
#  私钥

folders:
    - map: /private/var/HaI
      to: /home/vagrant/Code
      type: "nfs"
#  共享本地的目录和虚拟机的目录
#  map 本地的目录
#  to 虚拟机的目录
#  nfs 开启解决站点响应缓慢

sites:
    - map: homestead.test
      to: /home/vagrant/Code/Laravel/public
#  域名映射到虚拟机中项目目录
#  map 域名
#  to 虚拟机中项目目录

databases:
    - homestead
#  数据库

features:
    - mariadb: false
    - ohmyzsh: false
    - webdriver: false

#  ports:
#      - send: 50000
#        to: 5000
#      - send: 7777
#        to: 777
#        protocol: udp
```

> 这里新增了 version 配置，修改了 folders 和 sites 配置。

#  创建项目

- 启动虚拟机

> 在 Homestead 根目录下执行`vagrant up`启动虚拟机。

- 加载配置

> 每次更新 Homestead.yaml 文件夹后，需要执行`vagrant provision`让新的配置生效。

- 登录虚拟机

> 虚拟机启动后，再执行 `vagrant ssh` 登录虚拟机。

- 修改 php.ini

```
memory_limit = -1
```
> 因为 composer 下载的依赖包超过了 php 默认内存限制，所以这里改为 -1（不做限制）后面记得改回来.

- 重启 php

```
sudo service php7.0-fpm restart
```

- 修改 homestead.test

```
fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
```
> 找到 nginx 目录下的 sites-available，修改 homestead.test。因为 fastcgi 默认运行的是 php7.4-fpm，这里改为 7.0。

- 重启 nginx

```
sudo service nginx restart
```


- 下载 Laravel 源码

```
$ composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
$ composer create-project laravel/laravel Laravel --prefer-dist "5.1.*"
```

> 在 /home/vagrant/Code 目录下使用 composer 下载。下载完后，会生成一个 Laravel 文件夹。

- 修改 app.php 内容如下：

```
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Application Debug Mode
    |--------------------------------------------------------------------------
    |
    | When your application is in debug mode, detailed error messages with
    | stack traces will be shown on every error that occurs within your
    | application. If disabled, a simple generic error page is shown.
    |
    */

    'debug' => env('APP_DEBUG', true),
    // 进行本地开发时，你应该配置 APP_DEBUG 环境变量为 true。 在上线环境，这个值应该永远为 false

    /*
    |--------------------------------------------------------------------------
    | Application URL
    |--------------------------------------------------------------------------
    |
    | This URL is used by the console to properly generate URLs when using
    | the Artisan command line tool. You should set this to the root of
    | your application so that it is used when running Artisan tasks.
    |
    */

    'url' => 'http://localhost',

    /*
    |--------------------------------------------------------------------------
    | Application Timezone
    |--------------------------------------------------------------------------
    |
    | Here you may specify the default timezone for your application, which
    | will be used by the PHP date and date-time functions. We have gone
    | ahead and set this to a sensible default for you out of the box.
    |
    */

    'timezone' => 'UTC',

    /*
    |--------------------------------------------------------------------------
    | Application Locale Configuration
    |--------------------------------------------------------------------------
    |
    | The application locale determines the default locale that will be used
    | by the translation service provider. You are free to set this value
    | to any of the locales which will be supported by the application.
    |
    */

    'locale' => 'en',

    /*
    |--------------------------------------------------------------------------
    | Application Fallback Locale
    |--------------------------------------------------------------------------
    |
    | The fallback locale determines the locale to use when the current one
    | is not available. You may change the value to correspond to any of
    | the language folders that are provided through your application.
    |
    */

    'fallback_locale' => 'en',

    /*
    |--------------------------------------------------------------------------
    | Encryption Key
    |--------------------------------------------------------------------------
    |
    | This key is used by the Illuminate encrypter service and should be set
    | to a random, 32 character string, otherwise these encrypted strings
    | will not be safe. Please do this before deploying an application!
    |
    */

    'key' => env('APP_KEY', 'lgfaRyY25gtDF5FGqLbRc6pKOnJ6rUKz'),
    // 应用程序密钥是一个 32 位字符的随机字符串，存储在根目录 .env 文件中的 APP_KEY 密钥。也可以执行 php artisan key:generate 来生成。

    'cipher' => 'AES-256-CBC',

    /*
    |--------------------------------------------------------------------------
    | Logging Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may configure the log settings for your application. Out of
    | the box, Laravel uses the Monolog PHP logging library. This gives
    | you a variety of powerful log handlers / formatters to utilize.
    |
    | Available Settings: "single", "daily", "syslog", "errorlog"
    |
    */

    'log' => env('APP_LOG', 'single'),

    /*
    |--------------------------------------------------------------------------
    | Autoloaded Service Providers
    |--------------------------------------------------------------------------
    |
    | The service providers listed here will be automatically loaded on the
    | request to your application. Feel free to add your own services to
    | this array to grant expanded functionality to your applications.
    |
    */

    'providers' => [

        /*
         * Laravel Framework Service Providers...
         */
        Illuminate\Foundation\Providers\ArtisanServiceProvider::class,
        Illuminate\Auth\AuthServiceProvider::class,
        Illuminate\Broadcasting\BroadcastServiceProvider::class,
        Illuminate\Bus\BusServiceProvider::class,
        Illuminate\Cache\CacheServiceProvider::class,
        Illuminate\Foundation\Providers\ConsoleSupportServiceProvider::class,
        Illuminate\Routing\ControllerServiceProvider::class,
        Illuminate\Cookie\CookieServiceProvider::class,
        Illuminate\Database\DatabaseServiceProvider::class,
        Illuminate\Encryption\EncryptionServiceProvider::class,
        Illuminate\Filesystem\FilesystemServiceProvider::class,
        Illuminate\Foundation\Providers\FoundationServiceProvider::class,
        Illuminate\Hashing\HashServiceProvider::class,
        Illuminate\Mail\MailServiceProvider::class,
        Illuminate\Pagination\PaginationServiceProvider::class,
        Illuminate\Pipeline\PipelineServiceProvider::class,
        Illuminate\Queue\QueueServiceProvider::class,
        Illuminate\Redis\RedisServiceProvider::class,
        Illuminate\Auth\Passwords\PasswordResetServiceProvider::class,
        Illuminate\Session\SessionServiceProvider::class,
        Illuminate\Translation\TranslationServiceProvider::class,
        Illuminate\Validation\ValidationServiceProvider::class,
        Illuminate\View\ViewServiceProvider::class,

        /*
         * Application Service Providers...
         */
        App\Providers\AppServiceProvider::class,
        App\Providers\AuthServiceProvider::class,
        App\Providers\EventServiceProvider::class,
        App\Providers\RouteServiceProvider::class,

    ],

    /*
    |--------------------------------------------------------------------------
    | Class Aliases
    |--------------------------------------------------------------------------
    |
    | This array of class aliases will be registered when this application
    | is started. However, feel free to register as many as you wish as
    | the aliases are "lazy" loaded so they don't hinder performance.
    |
    */

    'aliases' => [

        'App'       => Illuminate\Support\Facades\App::class,
        'Artisan'   => Illuminate\Support\Facades\Artisan::class,
        'Auth'      => Illuminate\Support\Facades\Auth::class,
        'Blade'     => Illuminate\Support\Facades\Blade::class,
        'Bus'       => Illuminate\Support\Facades\Bus::class,
        'Cache'     => Illuminate\Support\Facades\Cache::class,
        'Config'    => Illuminate\Support\Facades\Config::class,
        'Cookie'    => Illuminate\Support\Facades\Cookie::class,
        'Crypt'     => Illuminate\Support\Facades\Crypt::class,
        'DB'        => Illuminate\Support\Facades\DB::class,
        'Eloquent'  => Illuminate\Database\Eloquent\Model::class,
        'Event'     => Illuminate\Support\Facades\Event::class,
        'File'      => Illuminate\Support\Facades\File::class,
        'Gate'      => Illuminate\Support\Facades\Gate::class,
        'Hash'      => Illuminate\Support\Facades\Hash::class,
        'Input'     => Illuminate\Support\Facades\Input::class,
        'Lang'      => Illuminate\Support\Facades\Lang::class,
        'Log'       => Illuminate\Support\Facades\Log::class,
        'Mail'      => Illuminate\Support\Facades\Mail::class,
        'Password'  => Illuminate\Support\Facades\Password::class,
        'Queue'     => Illuminate\Support\Facades\Queue::class,
        'Redirect'  => Illuminate\Support\Facades\Redirect::class,
        'Redis'     => Illuminate\Support\Facades\Redis::class,
        'Request'   => Illuminate\Support\Facades\Request::class,
        'Response'  => Illuminate\Support\Facades\Response::class,
        'Route'     => Illuminate\Support\Facades\Route::class,
        'Schema'    => Illuminate\Support\Facades\Schema::class,
        'Session'   => Illuminate\Support\Facades\Session::class,
        'Storage'   => Illuminate\Support\Facades\Storage::class,
        'URL'       => Illuminate\Support\Facades\URL::class,
        'Validator' => Illuminate\Support\Facades\Validator::class,
        'View'      => Illuminate\Support\Facades\View::class,

    ],

];
```

> 在 /home/vagrant/Code/Laravel/config 目录修改 app.php，这里修改了 APP_DEBUG  和 APP_KEY 配置。

#  访问项目

- 配置 hosts

> 修改本地hosts 文件，新增`192.168.10.10  homestead.test`。

- 访问

![homestead.test_.png](https://upload-images.jianshu.io/upload_images/15325592-88de7703849b53ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 浏览器打开  [http://homestead.test/](http://homestead.test/) ，如上图所示，成功访问。
