---
title: Sony MZ-NE410 MiniDisc Walkman
date: 2023-01-31 11:05:00
categories: [Blog]
tags: [blog, mini disc, mini, disc, sony, net md, net, md]
---

I recently found my MiniDisc Walkman, the Sony MZ-NE410  
![Sony MZ-NE410 Walkman](/assets/mz-ne410.jpeg)  
It's been many a year since I last used it, and as they do Operating Systems have moved on and software for them have been left behind. Luckily, there seems to be quite a few people that still enjoy the MiniDisc, and it only took me a little while to find a way to be able to find out what is on the discs I found with the Walkman and also update what I have on them.  

So, let's get on with how I got it working.  
To begin with, I had to download a program called [Zadig](https://zadig.akeo.ie).  
![Zadig](/assets/zadig.png)  
Once I had downloaded this, I connected my Walkman to my computer with a USB cable for Windows to discover it. I then ran the zadig software, from the drop-down menu I chose the Walkman and the clicked on the install driver button (Reinstall WCID Driver in the image).  

Then, after some searching, I discovered a web app called [Web MiniDisc Pro](https://web.minidisc.wiki/) that can connect to the Walkman to update the contents of the disc. This web app only works with a chromium based browser, so sadly not in Firefox as I'd prefer.  

You just need to connect the Walkman to the computer, click connect a dialogue box will open, select your Walkman, and the contents of the disc should load. From here you can add, delete, or rename the contents.  
![Web MiniDisc Pro](/assets/webmd-connect.png){: .normal w="350" h:"349"}
 ![Select device](/assets/webmd-connecting.png){: .normal w="336" h:"319"}
 ![Contents of disc](/assets/webmd-loaded.png){: .normal w="352" h:"349"}  

 While searching, I also found a repository on GitHub for a program written by [Gavin Benda](https://github.com/gavinbenda) called [Platinum-MD](https://github.com/gavinbenda/platinum-md). This looks nice, and I'll be giving it a go in the next few days.  

I have been very surprised as to how easy it has been to get the Walkman working on a more modern system, and thanks to what seems like a very active community around these older audio players they could have a greater life than I thought they had.  
