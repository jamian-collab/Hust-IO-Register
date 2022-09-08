# Hust-IO-Register
# (仅供参考学习Python，如果有相关需要申请出入校，请认真报备)
## 华中科技大学出入校门每日自动登记


### 一、使用方法(按照图示中红色方框操作)

#### 1、Fork到自己的仓库中

![1ca193c60f6c4dfc90cec1750e28bdb](https://user-images.githubusercontent.com/67460808/188874980-5dd4a08d-0053-4821-89ed-137cecbc8fd8.png)

#### 2、创建Actions

![21038a441cf9d014fd5fabd62ae2cef](https://user-images.githubusercontent.com/67460808/188875086-1aa78c1a-2f52-4e17-9612-4cc695fe0eca.png)
![9796882c15e6e1d4fff87a966877385](https://user-images.githubusercontent.com/67460808/188875129-237bdede-2b97-4975-9fcd-108fb03feb2e.png)

#### 3、创建Actions的Secrets
Actions的密钥有三个，分别是USERNAME，PASSWORD，和REGISTERURL(密钥是专属于每个Github账号的，因此不必担心泄漏)

![6a0d7c3332a6e71857aaa175fb0bafe](https://user-images.githubusercontent.com/67460808/189065053-97784597-629d-4052-b64f-73cbc89683c0.png)

##### ①USERNAME：表示华中大统一门户的学号

![5d2ebfa6f5eb239a14bcd7e8b1a361e](https://user-images.githubusercontent.com/67460808/188875555-bb8310e5-db8c-4beb-83b9-4ee98c444c75.png)

##### ②PASSWORD：表示华中大统一门户的密码

![9bb1959db7f10767b272e8cbdfdb4e6](https://user-images.githubusercontent.com/67460808/188875645-8fb3086e-a330-45de-9af3-e9b656b90f2a.png)

##### ③REGISTERURL：表示华中大出入登记的网址，每个人的网址是不同的，需要通过华科的企业微信获得

###### 获得方式：打开企业微信中的出入登记界面，选择上方的三个点，然后可以看到复制链接的选项，这个链接就是每个人的网址。

![image](https://user-images.githubusercontent.com/67460808/188878568-0457813c-3199-4c17-8b11-c12bd67cedf5.png)

###### 之后复制到Actions的密钥中，这样就可以使用了。
![b867045dc288c5336ef1cf22819a870](https://user-images.githubusercontent.com/67460808/188876322-b1b04673-06a1-43ed-9d6d-7b7842362254.png)

## 二、验证是否可以成功运行

#### 在GitHub Actions的yml文件中定义了两种触发方式，分别是手动和定时，这里的手动触发我们用作测试使用。

### 按下面的几张图操作，最后的Python运行结果为“登记成功🚗”则表示可以成功运行。

![image](https://user-images.githubusercontent.com/67460808/188892119-342506eb-9d83-455d-b29f-05d2dbedd17f.png)

![image](https://user-images.githubusercontent.com/67460808/188891699-7341f12c-4e27-422b-a3b9-53639e0cd89f.png)

![image](https://user-images.githubusercontent.com/67460808/188891774-c435729c-be04-4f1b-8ee1-0020627abe85.png)

![image](https://user-images.githubusercontent.com/67460808/188891822-edf306f7-0e71-46df-b630-7297efbe1345.png)


### 三、关于修改执行的时间

#### 修改执行的时间可以在workflow文件夹中修改yml文件。

![image](https://user-images.githubusercontent.com/67460808/188891920-e77e77e6-1990-4dd9-bb9d-7030c36f5981.png)

#### 注意的是GitHub Action使用的是UTC时间，比北京时间要迟上8个小时，譬如北京时间6点就是UTC的22点。

