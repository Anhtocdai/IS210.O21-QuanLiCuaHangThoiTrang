<!-- Improved compatibility of Lên đầu trang link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<div align="center">
  
  [![Stargazers][stars-shield]][stars-url]
  [![Forks][forks-shield]][forks-url]
  [![Contributors][contributors-shield]][contributors-url]
  [![Issues][issues-shield]][issues-url]
  [![License][license-shield]][license-url]
  
</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Website Cửa hàng thời trang Spring Day Clothing </h3>

  <p align="center">
    Đây là đồ án cuối kỳ môn IS210 của nhóm Spring Day tại trường Đại học Công Nghệ Thông Tin (UIT-VNUHCM).
    <br />
    <a href="https://github.com/lamisgosu11/se104-final-website"><strong>Document »</strong></a>
    <br />
    <br />
    <a href="https://github.com/lamisgosu11/se104-final-website">Xem Demo nè</a>
    ·
    <a href="https://github.com/lamisgosu11/se104-final-website/issues">Report khi gặp bug</a>
    ·
    <a href="https://github.com/lamisgosu11/se104-final-website/issues">Yêu cầu thêm tính năng</a>
  </p>
</div>

## Table of Contents

<!-- [Ý tưởng](#ý-tưởng) -->
- [Công nghệ sử dụng](#công-nghệ-sử-dụng)
- [Bắt đầu sử dụng](#bắt-đầu-sử-dụng)
  - [Yêu cầu cài đặt](#yêu-cầu-cài-đặt)
  - [Cài Đặt Project](#cài-đặt-project)
- [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
- [Đóng góp](#đóng-góp)
- [Thành viên nhóm](#thành-viên-nhóm)

<!-- ABOUT THE PROJECT -->

<!--## Ý tưởng

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) 

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) 

viết đại cái gì vô đây nè

<p align="right">(<a href="#readme-top">Lên đầu trang</a>)</p> -->

## Công nghệ sử dụng

<!-- - [![Flutter][flutter]][flutter-url]
- [![Firebase][firebase]][firebase-url] -->

![PYTHON][PYTHON]![Django][Django]![ORACLE][ORACLE]![NGROK][NGROK]
![HTML][HTML]![CSS][CSS]![SCSS][SCSS]![JAVASCRIPT][JAVASCRIPT]

<p align="right">(<a href="#readme-top">Lên đầu trang</a>)</p>

<!-- GETTING STARTED -->

## Bắt đầu sử dụng

Đây là hướng dẫn cài đặt và chạy project trên máy.

### Yêu cầu cài đặt

- Python
- Django
- Ngrok
- Oracle

### Cài Đặt Project

1. Clone lại repository sử dụng Git:
   ```shell
   git clone https://github.com/lamisgosu11/se104-final-website.git
   ```
2. Tải và cài đặt những package cần thiết cho project:
   ```shell
   pip install -r requirements.txt
   ```
3. Sử dụng Ngrok để tạo tunnel tạm thời cho localhost tới với internet:
   ```shell
    ngrok http 8000
   ```
   <p align="right">(<a href="#readme-top">Lên đầu trang</a>)</p>

<!-- USAGE EXAMPLES -->

## Hướng dẫn sử dụng

Chạy project, tạo file settings.py và chỉnh lại config nếu muốn deploy lên đường dẫn tạm thời:

```shell
 python manage.py runserver
```
Tạo super-user

```shell
 python manage.py createsuperuser
```
Migrate database

```shell
 python manage.py migrate
```

<!-- bổ sung thêm sau -->

Xem thêm tại [NGROK Document](https://ngrok.com/docs/getting-started/) và [Django Document](https://docs.djangoproject.com/en/3.2/).

<p align="right">(<a href="#readme-top">Lên đầu trang</a>)</p>

<!-- ROADMAP -->

<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
  - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">Lên đầu trang</a>)</p> -->

<!-- CONTRIBUTING -->

## Đóng góp

1. Fork project này
2. Tạo branch riêng cho bạn (`git checkout -b feature/AmazingFeature`)
3. Commit những thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch chính (`git push main feature/AmazingFeature`)
5. Mở pull request

<p align="right">(<a href="#readme-top">Lên đầu trang</a>)</p>

<!-- LICENSE -->

<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">Lên đầu trang</a>)</p> -->

<!-- ACKNOWLEDGMENTS

## Acknowledgments

- []()
- []()
- []()

<p align="right">(<a href="#readme-top">Lên đầu trang</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

## Thành viên nhóm

- [Lê Tuấn Đạt - 21520699](https://github.com/kamdaxay)

[contributors-shield]: https://img.shields.io/github/contributors/lamisgosu11/se104-final-website.svg?style=for-the-badge
[contributors-url]: https://github.com/lamisgosu11/se104-final-website/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lamisgosu11/se104-final-website.svg?style=for-the-badge
[forks-url]: https://github.com/lamisgosu11/se104-final-website/network/members
[stars-shield]: https://img.shields.io/github/stars/lamisgosu11/se104-final-website.svg?style=for-the-badge
[stars-url]: https://github.com/lamisgosu11/se104-final-website/stargazers
[issues-shield]: https://img.shields.io/github/issues/lamisgosu11/se104-final-website.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/lamisgosu11/se104-final-website.svg?style=for-the-badge
[license-url]: https://github.com/lamisgosu11/se104-final-website/blob/main/LICENSE
[product-screenshot]: md-images/screenshot.png
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[ORACLE]: https://img.shields.io/badge/Oracle-07405E?style=for-the-badge&logo=oracle&logoColor=white
[NGROK]: https://img.shields.io/badge/Ngrok-1F1E37?style=for-the-badge&logo=ngrok&logoColor=white
[HTML]: https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white
[CSS]: https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white
[SCSS]: https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white
[JAVASCRIPT]: https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E
[PYTHON]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

<!-- Nhớ thêm liscense sau -->
