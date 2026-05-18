# DATALOG

Django 기반 AWS 로그 수집 및 웹 서비스 배포 프로젝트<br>
**(ENG) AWS-based Django Log Collection and Web Service Deployment Project**

---

## 🛠 Skills

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML/CSS](https://img.shields.io/badge/HTML%2FCSS-E34F26?style=flat-square&logo=html5&logoColor=white)
![AWS Elastic Beanstalk](https://img.shields.io/badge/AWS_Elastic_Beanstalk-232F3E?style=flat-square&logo=amazonaws&logoColor=white)
![AWS API Gateway](https://img.shields.io/badge/API_Gateway-FF4F8B?style=flat-square&logo=amazonaws&logoColor=white)
![Kinesis Firehose](https://img.shields.io/badge/Kinesis_Firehose-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon_S3-569A31?style=flat-square&logo=amazons3&logoColor=white)
![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=flat-square&logo=amazonaws&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-3776AB?style=flat-square&logo=python&logoColor=white)
![C3.js](https://img.shields.io/badge/C3.js-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

---

## 📌 Project Summary

Django 기반 웹 서비스를 AWS Elastic Beanstalk 환경에 배포하고,<br>
AWS 로그 수집 파이프라인과 연동한 프로젝트입니다.<br>

API Gateway, Kinesis Firehose, S3, CloudWatch를 활용하여<br>
로그 데이터 흐름과 운영 환경 구성을 실습했습니다.

또한 C3.js 기반 데이터 시각화와<br>
BeautifulSoup 기반 데이터 수집 기능도 함께 구현했습니다.

**Eng ver.**

This project is a Django-based web service deployed using AWS Elastic Beanstalk.

It includes AWS log collection workflows using API Gateway, Kinesis Firehose, S3, and CloudWatch.

The project also includes data visualization using C3.js and web data collection using BeautifulSoup.

---

## 🎯 Purpose

- Django 기반 웹 서비스 구조 이해
- AWS Elastic Beanstalk 배포 경험
- AWS 로그 수집 흐름 학습
- 운영 환경 및 환경변수 설정 경험
- 데이터 시각화 및 데이터 처리 실습

**Eng ver.**

- Understand Django-based web application architecture
- Gain experience deploying applications using AWS Elastic Beanstalk
- Learn AWS log collection workflows
- Practice production environment and environment variable configuration
- Practice data visualization and data processing

---

## 💡 Why I Built This

웹 백엔드 구조와 클라우드 기반 운영 환경을 직접 경험해보고 싶어 진행한 프로젝트입니다.<br>

단순 기능 구현뿐 아니라,
Django 기반 프로젝트 구조와 AWS 서비스 간 연결 구조,
그리고 실제 배포 환경 구성을 경험하는 데 목적이 있었습니다.<br>

또한 로그 수집 구조와 운영 환경 문제를 직접 확인하고 해결하며
클라우드 기반 서비스 운영 흐름에 대한 이해를 높이고자 했습니다.

**Eng ver.**

I built this project to gain hands-on experience with backend web development and cloud-based deployment environments.

Beyond implementing features, I wanted to understand Django project architecture, AWS service integration, and real-world deployment workflows.

I also wanted to learn how log collection systems and production environments work in practice.

---

## 📂 Project Structure

```text
DATALOG/
├── ajaxapp/
├── log/
├── conf/
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── .ebextensions/
```

---

## ✨ Main Features

### AWS 로그 수집 구조 구성

- AWS API Gateway 연동
- Kinesis Firehose 기반 로그 전달 구성
- S3 로그 저장 구조 구성
- CloudWatch 기반 로그 확인

&nbsp;&nbsp;&nbsp;**Eng ver.**

- Integrated AWS API Gateway
- Built log delivery workflows using Kinesis Firehose
- Stored logs in Amazon S3
- Monitored logs using CloudWatch

### Django 기반 웹 서비스 구성

- Django 기반 웹 프로젝트 구조 구성
- URL Routing 및 Template 구성
- Django ORM 기반 구조 학습

&nbsp;&nbsp;&nbsp;**Eng ver.**

- Built a Django-based web application structure
- Practiced URL routing and template configuration
- Learned Django ORM-based architecture

### 데이터 시각화 실습

- C3.js 기반 Line Chart / Pie Chart 구성
- JavaScript 기반 동적 차트 구성 실습

&nbsp;&nbsp;&nbsp;**Eng ver.**

- Built Line Charts and Pie Charts using C3.js
- Practiced dynamic chart rendering using JavaScript

### 데이터 수집 실습

- BeautifulSoup 기반 데이터 수집 실습
- 데이터 가공 및 저장 처리

&nbsp;&nbsp;&nbsp;**Eng ver.**

- Practiced web data collection using BeautifulSoup
- Processed and stored collected data

### AWS 배포 환경 구성

- AWS Elastic Beanstalk 기반 배포 경험
- 환경변수 및 운영 환경 설정 경험

&nbsp;&nbsp;&nbsp;**Eng ver.**

- Deployed the application using AWS Elastic Beanstalk
- Configured environment variables and production settings

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📖 What I Learned

- Django 기반 웹 서비스 구조 이해
- AWS 클라우드 서비스 연동 경험
- Elastic Beanstalk 배포 과정 경험
- 로그 수집 파이프라인 흐름 이해
- 운영 환경 및 환경변수 설정 중요성 이해
- 데이터 시각화 및 데이터 처리 경험

**Eng ver.**

- Understanding Django web application architecture
- Experience integrating AWS cloud services
- Learning deployment workflows using Elastic Beanstalk
- Understanding log collection pipeline workflows
- Learning production environment configuration
- Experience with data visualization and data processing
