# Brute-force-for-login-bypass-on-a-local-website

## Description - Sample Website Backstory
- A-Z Education website offers courses related to React Development, Amazon Web Services and Cyber Security algorithms.
- The website has a login page through which users create an account to purchase and view videos related to the course. 
- A-Z Education does not utilize multi factor authentication methods like One Time Passwords, Security Questions, or email verification which leaves it vulnerable to a variety of attacks.

## Bruteforce Attack
In this case, I, the attacker, try to access the administrator panel of the website using a list of common usernames and passwords. To carry out the attack, Burp Intruder is used to find firstly the admin username and after finding the username finding the respective admin password to view the dashboard for the website.

### Prerequisites
1. Python
2. Burp Suite
   
### Steps to Carry Out the Attack

1. Clone this repositroy and start the flaks app.
```
git clone https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website.git
cd Brute-force-for-login-bypass-on-a-local-website
pip install flask
python app.py
```
2. Launch Burp Suite and access the login panel in Burp Browser.
![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/509c47e6-260a-4407-81cc-5281d7ab06cb)

3. Make sure the intercept is on in Burp Suite and use any credentials to post a request.
![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/24905b8e-e123-49e3-948e-7d6b3fe23448)

![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/bcbb7685-51b2-4068-8807-bd019b6b077a)

4. Send this request to Burp Repeater, Choose the attack type to Sniper and add a payload position to username.
![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/0fff17cc-f64a-4deb-94b4-4f22dc10c6d9)

![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/203d0d32-8a0b-446d-837c-dad06789d1fa)

5. Using the common `usernames.txt` of this repostiory, add this to the payload as a simple list and start the attack.
![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/fd1593f7-d692-429c-89cc-e6cab39af142)
![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/9e69c6c2-12ed-472a-9170-82ebe8825a25)

6. Sample bruteforce attack on username.
![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/5f6bef40-b1d6-4c37-b746-da5a8583f56c)

7. Observe that one status code is different than the others.
![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/bce81bb1-efb7-42a0-85fe-d3051ec60c42)

8. After finding out that “admin” is the admin username, we change the payload to the password parameter and apply brute force using password list to find the password.

![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/c1855621-f49d-43d2-b802-7bb51daa4df1)

![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/53b07e39-c587-467d-ad62-5318b80a2044)

![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/2d2817c0-3668-42dc-a725-619d1a3c3ab3)

9. Now we come to know the password and username for the admin (because of the status codes) and thus we login in to the admin panel using these credentials.

![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/5899e8a7-1aa5-4917-b3b9-5f50999450b5)

10. Accessed the admin panel.

![image](https://github.com/akshatmiglani/Brute-force-for-login-bypass-on-a-local-website/assets/120178102/243342a6-248d-4bd2-b8c0-8d3c6feda657)

## Prevention Techniques
1. Use Strong Passwords.
2. Limit Login Attempts.
3. Monitor IP addresses.  
4. Use Two-Factor Authentication (2FA).   
5. Use CAPTCHAs.  
6. Use Unique Login URLs
7. Disable Root SSH Logins
8. Use Web Application Firewalls (WAFs)





