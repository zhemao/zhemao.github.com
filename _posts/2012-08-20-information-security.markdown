---
title: Information Security in the Modern Age
layout: default
category: blog
---

Most of you have probably heard about such recent IT security boondoggles as
the server break-ins at LinkedIn and Last.fm as well as the truly disastrous 
[hijacking](http://www.emptyage.com/post/28679875595/yes-i-was-hacked-hard)
of Wired reporter Mat Honan's iCloud, Gmail, and Twitter accounts. 

These are just the most publicized incidents. Many more such events occur 
without showing up on the front page of Wired or Gizmodo. 

Many of these breaches were the result of mistakes made by the companies 
trusted with safeguarding the data. However, there are some steps that anyone 
can take to increase the security of their online accounts and mitigate the 
potential damage of such electronic attacks. 

In light of these recent events, I thought I would share some of the steps I 
take to make sure that my personal information and communications are secure.

**Disclaimer:** Though I am quite knowledgable about computers and technology, 
I am by no means a computer security expert. These are just some of the 
security habits I practice. I have tried to order my suggestions here from 
simple and urgently necessary to complex and probably unnecessarily paranoid. 
It's up to you to decide whether they are worth following.  

## 1. Always log in through HTTPS

There are two protocols that make up the modern web. The first, and most widely
used, is HTTP, the Hypertext Transfer Protocol. HTTP transfers all data between 
the browser and the webserver in plaintext (i.e. unencrypted). What this means
is that, if you log in to a site over HTTP on an insecure network (such as a
public wi-fi access point), an attacker can intercept your password or your
authentication cookie and use these credentials to log in to your account.
Logging in over HTTP also exposes you to man-in-the-middle attacks, in which
an attacker presents you with a webpage that looks like the legitimate website's
login page, but which is actually served from a webserver owned by the attacker.

The second protocol of the world wide web fixes the vulnerabilities in HTTP.
This protocol is known as HTTP Secure, or HTTPS. HTTPS tunnels HTTP traffic 
over a protocol known as Secure Sockets Layer, or SSL, which ensures that all 
traffic between your browser and the server is strongly encrypted. In addition, 
every website that uses HTTPS is assigned an SSL certificate, which your 
browser uses to verify the identity of the website. This protects against 
man-in-the-middle attacks.

Therefore, if you are logging into an online account, make sure that the login 
page is sent to you over HTTPS. This is easy to determine, as the url in the 
url bar should begin with "https://". Also, make sure that the security 
certificate is valid and is assigned to the site you are actually trying to 
log in to. To do this, look at the icon to the left of the url in the
url bar. If it is a little lock, possibly with the site's name next to it, 
the SSL certificate has been verified by your browser and so can be trusted.

If the page was not sent to you over HTTPS, you can probably find the HTTPS 
page by simply changing the url scheme from "http://" to "https://". 
Many browsers will hide the scheme portion of the url if it is HTTP, in which
case just add "https://" to the beginning of the url. 

If you are using Facebook or Twitter, there are settings you can enable to 
make sure the site uses HTTPS everywhere. On Twitter, you can find the setting
under Settings -> Account -> HTTPS only. On Facebook, the option is under
Account Settings -> Security -> Secure Browsing. 

*Update:* I have now started using the EFF's
[HTTPS Everywhere](https://www.eff.org/https-everywhere) browser extension,
which will make sure I am using HTTPS on most common sites. I highly
recommend it.

## 2. Use random passwords and a password manager

Probably one of the most horribly insecure but also most widely practiced 
security habits is password reuse. Most people either use the same password
on multiple sites, in which case all of those accounts will be compromised if
the password is cracked, or they use passwords that are easy to remember and
therefore easy for attackers to guess. This is only natural of course. One can
only remember so many unique passwords. Fortunately, there is a better way.
You can generate a unique, random password for each account using services such
as [random.org](http://random.org), and then store the password using a password
manager. A password manager is basically a database that stores all your 
credentials and which is itself encrypted with a single master password. If 
you are using recent versions of Chrome or Firefox, there is already a password
manager built in to your browser. These password managers can fill in your
username and password for you automatically when you go to a website's login
page and can sync your stored password across multiple computers. 

You can find further instructions on setting up your password manager below
 * For [Google Chrome](https://support.google.com/chrome/bin/answer.py?hl=en&answer=95606)
 * For [Mozilla Firefox](http://support.mozilla.org/en-US/kb/password-manager-remember-delete-change-passwords)

Instructions for setting up browser sync can be found at the following pages
 * For [Google Chrome](http://support.google.com/chrome/bin/answer.py?hl=en&answer=185277)
 * For [Mozilla Firefox](http://support.mozilla.org/en-US/kb/firefox-sync-take-your-bookmarks-and-tabs-with-you)

Note for UNIX command-line users: you can generate a random password quickly
using the following command

    head -c 8 /dev/urandom | base64

Change the argument to the -c option to adjust the length of the generated
password. 

## 3. Use Google Two-Factor Authentication

Most sites allow you to use your email address to reset your password if you
forget it. Therefore, it is important to make sure your email account is extra
secure. Fortunately for Gmail users, Google offers two-factor authentication
for your Google account. The way two-factor authentication works is that you 
enter your Google account password in as usual, and then Google sends a 
one-time PIN to your phone. You will then be required to enter this PIN on the 
next form in order to log in. You can also set the computers you own as trusted
computers, in which case Google will only ask for the secondary login once
every 30 days. If you link third party clients to your google account (such
as email or chat clients), you can set application-specific passwords for them.
Instructions for setting up two-factor authentication for your Google account
can be found [here](http://support.google.com/accounts/bin/topic.py?hl=en&topic=1099588&parent=28786&ctx=topic).

## 4. Wipe storage drives before throwing them out

If you are throwing out an old computer, make sure that you wipe all the data 
from the hard drive. This involves more than just deleting all the files or 
formatting the partition, as this still leaves potentially recoverable data. 
To make sure the data is truly unrecoverable, you will need to overwrite the
hard drive with random data. There are many different software packages that
can do this for you. My preferred method is to boot a Linux distro from a live
USB and run the following command 

    dd if=/dev/urandom of=/dev/sda bs=1M

Where /dev/sda can be replaced with whatever drive or partition you want to
erase. If you don't have a Linux live USB handy or aren't familiar with the
command line, you should do some searching for the method that will work best
for you.

Note: this advice also holds true for external storage devices, such as USB
drives or external hard drives.

## 5. Encrypt your hard drive

One of the worst things that can happen in terms of information security is if
your computer is stolen. Since a lot of personal computing today is done on 
mobile devices and highly portable laptops, it has become increasingly important
to safeguard the data stored on one's computer from theft. 

Once criminals steal your computer, they can pull all of your personal data off 
of it. You might think you're safe because you use a password to log in to your 
computer, but, if the data is unencrypted, the thieves can always bypass your 
operating system's file permissions to obtain the data.

The best way to avoid this problem, of course, is to make sure your computer or
phone is not lost or stolen. But you can also mitigate the potential fallout
from computer theft by encrypting your hard drive. 

On Mac OSX 10.3 "Panther" and above there is a pre-installed tool for this 
called "File Vault", which you can activate by searching for File Vault in 
Spotlight and using the handy graphical wizard. 

The Linux kernel provides a system for disk encryption called LUKS 
(Linux Unified Key Setup). Activating LUKS is not as "user-friendly" as 
File Vault. You will want to install the cryptsetup package with your distro's
package manager (if it is not installed already) and follow the instructions
[here](http://david.dw-perspective.org.uk/da/index.php/computer-resources/encrypted-partitions-on-linux-with-luks/).
Note that LUKS encryption will destroy the data on the partition you are 
encrypting, so make sure to back it up first before you set up LUKS.
More detailed instructions for LUKS can be found [here](https://wiki.archlinux.org/index.php/LUKS).

If you don't want to use your operating system's built-in tools (or you are
using Windows and therefore don't have any), [Truecrypt](http://www.truecrypt.org/)
is a pretty good cross-platform software package for full-disk encryption.

I don't know much about disk encryption on mobile phones, but I've heard that
Android 3 "Honeycomb" and above are able to use LUKS encryption. iOS apparently 
has full disk encryption by default, but its disk encryption implementation is
[completely broken and useless](http://www.alertboot.com/blog/blogs/endpoint_security/archive/2010/05/28/iphone-encryption-is-for-naught-under-linux.aspx).

## 6. Encrypt your communications using PGP

If you are well and truly paranoid and worry about the NSA looking at your 
private email (which they [probably are](https://www.eff.org/issues/nsa-spying/)),
you might want to consider using PGP encryption for your email. 

PGP is a standard for encrypting messages using the RSA encryption algorithm. 
Basically, the way RSA works is that you generate a public and private key. 
You keep the private key to yourself and send the public key to your friend who 
wants to pass you a secret message. To send a secret message to you, your 
friend must encrypt the message using your public key. The message can then 
only be decrypted using your private key. 

RSA also allows signing and verification of messages. How this works is that 
you encrypt a message using your private key and send the encrypted message 
(the signature) and the plaintext message to your friend. Your friend then 
verifies the signature by decrypting the signature with your public key and 
making sure that it matches the plaintext message. Since only you possess your 
private key, your friend can then be sure that you sent the message.

The main inconvenience of using PGP to encrypt your email and other electronic
communications is that both you and the person you are corresponding with must
have PGP keypairs and possess each other's public keys. Also, in order for
PGP to be truly secure, you must be certain that the public key you are using
to communicate with your friend actually belongs to him, otherwise you could
be exposed to a man-in-the-middle attack. Therefore, you should only use PGP
encryption if you and your correspondents are serious about the privacy and
security of your communications with each other.

PGP encryption is available through many desktop mail clients, either as built
in features or plugins.

 * Microsoft Outlook 2007 has a [plugin for it](http://www.cumps.be/nl/blog/read/gpg-in-outlook-2007-outlookgnupg)
 * Apple Mail has a plugin called [GPGMail](https://www.gpgtools.org/gpgmail/index.html)
 * Mozilla Thunderbird has a plugin called [Enigmail](http://www.enigmail.net/home/index.php)
 * Evolution has it [built in](http://fedoraproject.org/wiki/Using_GPG_with_Evolution)

Most of these clients depend on a PGP implementation called GNU Privacy Guard,
or [GPG](http://www.gnupg.org/). A complete list of PGP implementations, mail
clients, and plugins can be found [here](http://www.vanheusden.com/pgp.php).

If you want to use PGP from the Gmail web interface, you will have to install
a PGP plugin for your browser. There's a PGP plugin for firefox called
[FireGPG](http://getfiregpg.org/s/home) and one for Chrome called 
[WebPG](https://chrome.google.com/webstore/detail/hhaopbphlojhnmbomffjcbnllcenbnih).
