# Hacking tutorial
As a follow up to [clicker automation](../../) using Selenium, let's dive into hacking the game.

## Analysis
### XHR
It perfectly makes sense that the game has a backend to store and check the scores.\
As a first step, let's check the _Network_ tab in developer console and see what's happening there for *XHR*.\
On the home screen not that much:
`api.php?r=api-social/current-user`

Clicking on this item we can see what the response was. Given the fact you've authorized within the game, there should be:
* avatarUrl
* csrfToken
* currentStage
* id
* login
* pointsCount
* rank
* rating
* state

While most of these fields seem to be obvious, `rank` and `state` have some integer numbers not seen on the website. Let's dig deeper.

### JS
#### Understanding user vars
The website has 3 .js files in sources panel:
* main.a726623c0847e448272f.js
* polyfills.a6df4032a88deef09663.js
* runtime.9ec73600c1a3073847a1.js

Let's open them and click *pretty-print* button so that they can be read.\
Searching for rank reveals this:
```JS {r, attr.source='.numberLines startFrom="11541"'}
var Bl = (()=>(function(t) {
	t[t.RANK_SQUARE = 1] = "RANK_SQUARE",
	t[t.RANK_CROSS = 2] = "RANK_CROSS",
	t[t.RANK_TRIANGLE = 3] = "RANK_TRIANGLE"
}(Bl || (Bl = {})),
Bl))()
  , fo = (()=>(function(t) {
	t[t.STATE_IN_GAME = 1] = "STATE_IN_GAME",
	t[t.STATE_WINNER = 2] = "STATE_WINNER",
	t[t.STATE_LOOSER = 3] = "STATE_LOOSER"
}(fo || (fo = {})),
fo))();
```
This does look like the icons in overview and shows the progress through this game.\
Same goes for the state.\
![image](https://user-images.githubusercontent.com/32206956/141380915-77e30d91-e32d-42c5-afd1-9e3c9f3a1f17.png)

#### Where does the progress change
If we put an *XHR\fetch Breakpoint* and play the game, it will stop on
```JS {r, attr.source='.numberLines startFrom="11653"'}
sendResult(n, i=0) {
	Vn.headers = Vn.headers.delete("X-CSRF-Token").append("X-CSRF-Token", t.user.csrfToken);
	let o = {
		type: n
	};
	return 0 != i && (o.pointsCount = i),
	new Promise((s,a)=>{
		this.http.post("/ru/co-marketing/cinemagic-game/api.php?r=api-result/update", JSON.stringify(o), Vn).toPromise().then(l=>{
			t.user = l,
			this.broadcast.gotUser(t.user),
			s(t.user)
		}
		).catch(l=>{
			a(l)
		}
		)
	}
	)
}
```

Let's put a breakpoint on `http.post` and see what's contained in `o` variable.
```JS
{type: 2}
```
Type does not tell us anything, let's dig into the code and see what a type can be:
```JS {r, attr.source='.numberLines startFrom="11982"'}
var go = (()=>(function(t) {
	t[t.TYPE_WIN = 1] = "TYPE_WIN",
	t[t.TYPE_LOOSE = 2] = "TYPE_LOOSE",
	t[t.TYPE_INCREASE_POINTS = 3] = "TYPE_INCREASE_POINTS"
}(go || (go = {})),
go))();
```
Jeesh, feels like we've lost in this game.\
Before proceeding further let's check where this *go* variable is used:
```JS {r, attr.source='.numberLines startFrom="14809"'}
this.broadcast.$looseGameEvent.subscribe(r=>{
	this.mIsGameRunning = !1,
	this.mustShowRating = !1,
	this.sendResult(go.TYPE_LOOSE),
	this.showLoosePopup = !0
}
),
this.broadcast.$winGameEvent.subscribe(r=>{
	this.mIsGameRunning = !1,
	this.mustShowRating = !0,
	this.sendResult(go.TYPE_WIN)
}
```

## Let's win!
Now that we know that type stands for loosing and winning, we should probably change it to *1* typing `o.type = 1` in console, 
should be fine now. This result is passed to XHR and the backend gets and update that we won and can proceed with the next game.

As the 4th game ends, the `o` variable will change a bit and feature:
```JS
{type: 3, pointsCount: 58}
```
As we've seen earlier, 3 stands for increasing points and the points count is the amount of points you got in the last game.\
Let's head back to console and change the amount to something better, like:
```JS
o.pointsCount = 999999
```
Resume script execution, your score gets updated on the backend, congrats!
