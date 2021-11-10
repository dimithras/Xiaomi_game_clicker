# Xiaomi_game_clicker
## Overview
Xiaomi has started a [game event](https://ru.event.mi.com/ru/sales2021/xiaomi11tgame) with the acrual game found [here](https://cinemagicgame.igm.gg/).\
[RUS] _Xiaomi запустили [конкурс](https://ru.event.mi.com/ru/sales2021/xiaomi11tgame) где надо найти и пройти игру, сама игра [здесь](https://cinemagicgame.igm.gg/)._

This is a simple Selenium automation that will help you get a maximum score in 4th game without being detected.\
[RUS] _Это простая автоматизация в Selenium для последней 4-ой игры, которая поможет набрать максимальное число очков, при этом не является взломом и не нарушает правил игры в их текущей редации._

## How to get started
### Prerequisites
Assuming you've already got Python installed, you'll need a Selenium package.\
[RUS] _Вам потребуется Python, а также модуль Selenium._

[Python download](https://www.python.org/downloads/)\
In cmd or bash:\
[RUS] _В командной строке Windows или Bash:_
```cmd
pip install Selenium
```
### Selenium driver
#### Getting driver
Follow Selenium driver download link and get the driver. Brave and Chrome share the same driver. Driver version should be the same as browser.\
[RUS] _Скачайте драйвер для Selenium по ссылке ниже и сохраните его куда-нибудь. Важно, чтобы версия драйвера совпадала с версией браузера._

[Selenium drivers](https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/).

To check Browser version hit triple dot menu:\
[RUS] _Чтобы узнать версию браузера, нажмите на меню бутерброд:_
![Browser Screenshot](https://help.zenplanner.com/hc/article_attachments/360036302033/_54832bd2bba3039749cec6bc25eb4745__Image_2019-05-22_at_7.56.01_AM.png)

Than:\
[RUS] _Затем:_
* Brave
  * About Brave
* Chrome
  * Help -> About Goole Chrome

#### Care about detection
Open the downloaded driver with notepad++ / vim / sed / whatever and change every instance of `cdc_` to something else.\
[RUS] _Откройте скачанный драйвер любым редактором и замените все `свс_` на что-нибудь ещё_

[Source](https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver)

## Running the script
You'll need to pass the first three games yourself, the last one is about clicking a green button. One can run the last game multiple times. Change `driver_path` and `brave_path` to your driver and browser paths respectively. You might want to also specify `profile_path` to use your current vk.com and game auth.

[RUS] _Вам будет необходимо пройти первые три игры самостоятельно. Последнюю же, в которой надо жать на зелёную кнопку, можно перепроходить сколько угодно. Вам следует поменять пути `driver_path` и `brave_path` на те, что в Вашей системе. Также полезно указать ссылку на профиль `profile_path`, чтобы не надо было авторизовываться в vk.com и игре каждый раз запуская Selenium._

Profile path sample:\
[RUS] _Пример пути к профилю:_\
`C:/Users/Some_User_Name/AppData/Local/BraveSoftware/Brave-Browser/User Data/Selenuim`

As soon as you change the path, just run the script in cmd / bash / jupyter / PyCharm. It will cycle through the game boosting your score, cycle can be interrupted with Ctrl+C or Kernel -> Interrupt.

[RUS] _После того как вы поменяете переменные путей, запускайте скрипт в cmd / bash / jupyter / PyCharm. Он будет играть в последнюю игру и запускать её заново набивая очки. Цикл можно прервать через Ctrl+C или Kernel -> Interrupt._
