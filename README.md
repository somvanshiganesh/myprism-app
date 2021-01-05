# Django-Ecommerce

Ecommerce website built with Django 2.2.3, Python 3.7.3, and AWS

![image](https://user-images.githubusercontent.com/29988949/65267147-499fc580-dac9-11e9-90e8-eccbc93c7c3a.png)

`Product Slide`

![image](https://user-images.githubusercontent.com/29988949/65999313-ff67fe00-e451-11e9-9ed9-fc7bce704f17.png)

`Shop Page`
![image](https://user-images.githubusercontent.com/29988949/66098968-923f9000-e559-11e9-8691-cd5c2b181ca1.png)

`Product Detail Page`
![image](https://user-images.githubusercontent.com/29988949/66291084-bff84200-e895-11e9-8d53-3aa23b29dbae.png)

`Cart Page`
![image](https://user-images.githubusercontent.com/29988949/66291144-f0d87700-e895-11e9-8545-b8f93f799063.png)

`BillingAddress Page`
![image](https://user-images.githubusercontent.com/29988949/66291542-013d2180-e897-11e9-8ea9-40afcb90cee2.png)

`Stripe Payment Page`
![image](https://user-images.githubusercontent.com/29988949/66291610-29c51b80-e897-11e9-8b47-20de35d6c1d0.png)

`Order Success Page`
![image](https://user-images.githubusercontent.com/29988949/66291657-3e091880-e897-11e9-830b-6cf44e72a995.png)

# Installation

`pip install django`

`virtualenv env`

# For Mac/ Linux

`source env/bin/activate`

# For Window

`env\scripts\activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

# For Admin Login

```python
python manage.py createsuperuser
Username : admin
Password : 12345678
```

# Test login
Username : ganesh
Password : test123

# Demo

http://djangoecommerce.pythonanywhere.com

# HTML Template

https://colorlib.com/etc/fashe/index.html

# TEST ROUND 1 (item to develop)
1. All
forgot password + email alert
email confirmation on sign-up
product details page 
    - related products/ recommendations
    - more than 1 image
    - price in dollar
    - size-cms 
    - remove footer 
category/vest/
    - add to cart from image does nothing
checkout-form
    - checkout should redirect to place order and confirm page
    - save address for billing and shipping

User profile page
    - new create
    - all details

2. UI
home page UI name *
sign-out
checkout-form format
    - top title
    - remove payment options
    - remove page bottom tags - company name, privacy etc
    - remove redeem feature
shop page 
    - missing image at top
    - search product feature
    - filters etc

Mobile view