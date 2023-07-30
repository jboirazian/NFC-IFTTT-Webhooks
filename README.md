## NFC Webhook trigger

A small proof of concept on how you can use NFC with a PWA [Flet](https://flet.dev/) app by doing using some cleaver hacks.


https://github.com/jboirazian/NFC-IFTTT-Webhooks/assets/21143405/2d78d38b-75a4-42c0-ac65-1a162c0a2f92


### Does Flet support NFC ?

**No** (at least for the moment...) , that being said you can take advantage of a feature of Progressive web applications in Android.

### PWA and Links:

When you install an PWA app on your phone , and you click a link that corresponds to the URL of your hosted web app , your phone will open your installed PWA insted of opening a browser.

This means that if you write an NFC tag with a link of your hosted web app , you can do some pretty cool things that normally are not possible by default on Android.

### To run it locally:

Install flet:

```
pip install flet
```

```
flet publish --route-url-strategy hash app.py
```

```
python -m http.server --directory dist 9092
```

### To deploy it:

There are many ways to deploy your serverless Flet app and all of them should work.

I like using [Netlify](https://www.netlify.com/) because it is really easy and the free tier is really good.

Just do this:

```
flet publish --route-url-strategy hash app.py
```

Then drag and drop the dist folder

### Writting your NFC tags

After deploying your app , you should now write an NFC tag (any NFC writting app should work , I used NXP TagWritter) with the following link:

```
https://{your_hosted_url}/#/{your_ifttt_event_name}/with/key/{webhooks_key}
```

With IFTTT you can also pass up to 3 arguments to your url:

```
https://{your_hosted_url}/#/{your_ifttt_event_name}/with/key/{webhooks_key}?value1=value1&value2=value2&value3=value3
```

### My IFTTT integration Example:

for this case I used the following automation:

![sample3](https://github.com/jboirazian/NFC-IFTTT-Webhooks/assets/21143405/7f8bf337-348d-4a40-a310-98776cd036d0)



