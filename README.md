# ZalGDOS - Zalgo Gmail DOS

For a browser, the act of rendering an UTF8 combination of multiple (meta-)characters it's **hard**.

As a fact, trying to display a text with 10k or more metacharacters (such as a big Zalgo text) will almost always result in a global slow-down of the current page rendering, which slows down even the most basic operations (scrolling, zooming etc), and  even leads to unresponsiveness and page crash.
Keeping that in mind, I tried to generate a **huge** UTF8 combination of characters, hoping to produce a "*browser DOS character*", just for fun.

In order to achieve that result, I started writing a simple Python script that sends a combination of multiple metacharacters (1024^2 == 1MB) to my email, but t occurs something I may not have anticipated:

**GMail just died.**

As a fact GMail crashed with an Error 500 (**Internal Server Error**) followed by an Error 502 (**Bad Gateway**). Therefore I could not reach my email even from the GMail APP on my smartphone.

I was able to remove the email using a script written in the **Google Apps Script** language, that I used to employ to get rid of old automatic Emails in my inbox.

Even though I had deleted the email I could not still login into my GMail account for more than 1 hour.
That’s why I decided to cause more damage: I created a single-300KB-char and used it in the subject, object (HTML) and object (text) fields of the mail.

In order to reach that goal, I used the UTF8 char #857 "͙ " that has a nice "**stacking**" characteristic: a viewer tends to think to it as a single character but actually multiple characters are printed one on top of the other.

Sending the email with that character has made a test email folder unreachable (error 500) for 4 days!
The bug was promptly reported to the Google Security team who had managed to deploy the fix in a couple of weeks.
This allowed me to gain access to the [Google Vulnerability Hall Of Fame](https://bughunter.withgoogle.com/profile/31e91e86-7a21-4110-a87b-dfde58e06116).

Here you can find [ZalGDOS.py](https://github.com/ShotokanZH/ZalGDOS/blob/master/ZalGDOS.py) , the script I used to test the vulnerability.
