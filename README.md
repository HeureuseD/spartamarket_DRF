# spartamarket_DRF

&nbsp;

## Features
- **Accounts Management:** User registration, login, logout, withdrawal from membership and userprofile feature.
- **Product Management:** Write, delete, edit and read a product sales post.

&nbsp;

## Requirements
- asgiref==3.8.1
- Django==4.2
- django-seed==0.3.1
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- Faker==28.4.1
- pillow==10.4.0
- psycopg2==2.9.9
- PyJWT==2.9.0
- python-dateutil==2.9.0.post0
- six==1.16.0
- sqlparse==0.5.1
- toposort==1.10
- typing_extensions==4.12.2
- tzdata==2024.1


&nbsp;

## Getting started
#### Installation

```python
git clone https://github.com/HeureuseD/spartamarket_DRF.git
cd spartamarket_DRF
```


#### Install Dependencies
```python
pip install -r requirements.txt
```

#### Run Migrations

```python
python manage.py makemigrations
python manage.py migrate
```


#### Start the Servers
```python
python manage.py runserver
```
&nbsp;
&nbsp;
&nbsp;
&nbsp;

## ERD
![Untitled](https://github.com/user-attachments/assets/0d54922b-e1f0-496d-aaeb-2da43911a9f0)
&nbsp;
&nbsp;
&nbsp;
&nbsp;

## Project Structure
```
📦 
├─ .gitignore
├─ README.md
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_user_bio_user_birth_date_user_gender_user_nickname_and_more.py
│  │  ├─ 0003_alter_user_birth_date_alter_user_nickname.py
│  │  ├─ 0004_profile.py
│  │  ├─ 0005_delete_profile.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ signals.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ products
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ requirements.txt
└─ spartamarket_DRF
   ├─ __init__.py
   ├─ asgi.py
   ├─ settings.py
   ├─ urls.py
   └─ wsgi.py
```

&nbsp;
&nbsp;
&nbsp;
&nbsp;


## 기능점검

#### 회원가입
![image](https://github.com/user-attachments/assets/04fcbe2a-c261-4ced-883f-62f607330c3b)

&nbsp;
&nbsp;


#### 같은 username 또는 email로 가입하려 할 시, 400 Bad Request.
![image](https://github.com/user-attachments/assets/5d28bed1-72a0-42ee-a30a-0df4322a212b)

&nbsp;
&nbsp;


#### 로그인
![image](https://github.com/user-attachments/assets/549cbea4-4a02-41f4-bee9-844bcc2fabaf)


&nbsp;
&nbsp;

#### Refresh Token
![image](https://github.com/user-attachments/assets/86fa8db0-b85d-4b90-a6ae-ae5a948c913a)


&nbsp;
&nbsp;

#### 유저 프로필
![image](https://github.com/user-attachments/assets/0dd82383-8766-4cec-975d-189b3ec9219a)
&nbsp;
&nbsp;



#### 로그아웃
![image](https://github.com/user-attachments/assets/4eac425d-5572-4584-8f46-78c0db9133a8)
&nbsp;
&nbsp;



#### 로그인되지 않으면 프로필 조회 불가
![image](https://github.com/user-attachments/assets/a7c3b3c1-ba05-4864-9465-c5a4fd504277)
&nbsp;
&nbsp;


#### 회원탈퇴. 비밀번호 입력 필요.
![image](https://github.com/user-attachments/assets/d6af8edf-3934-4b59-90b8-80bbacf4a5f5) 
&nbsp;
![image](https://github.com/user-attachments/assets/bd7986d7-ea11-4015-813c-b9361028fd06)


&nbsp;
&nbsp;


------

&nbsp;
&nbsp;


#### 상품 등록
![image](https://github.com/user-attachments/assets/d38fb8c3-4b23-48ad-9033-3675c8c781e9)
&nbsp;
&nbsp;


#### 상품목록 조회 - 페이지네이션
![image](https://github.com/user-attachments/assets/38984650-0a6b-4aae-83be-d8ad0a845bb6)
&nbsp;
&nbsp;



#### 상품 수정
![image](https://github.com/user-attachments/assets/58d1c13e-2072-40e8-87ae-b90c66c6b3da)


&nbsp;
&nbsp;

#### 상품 삭제
![image](https://github.com/user-attachments/assets/8b47fea9-dd9f-4632-bffc-c48d74d6d0c0)
&nbsp;
&nbsp;

