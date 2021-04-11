<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Flask Notes</h3>

  <p align="center">
    This is a simple notes application written in Python3.
    <br />
    <a href="https://github.com/hanzala123/Flask_notes/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/hanzala123/Flask_notes/issues">Report Bug</a>
    ·
    <a href="https://github.com/hanzala123/Flask_notes/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![product-screenshot]](https://github.com/hanzala123/Flask_calendar)
[![product-screenshot2]](https://github.com/hanzala123/Flask_calendar)

I am making something with an integreted calender with events managment. This is not something you can find here a lot. So I made one with some [help](#built-with). It is simple to install and use. Redis was used for database. 

Note: Redis is an in-memory database program but all the versions I used do store data in the drive as well. So a system reboot won't clear the database.

### Built With

* [Nerve](https://github.com/PaytmLabs/nerve)
* [python_flask_mysql_bootstrap_calendar_events](https://github.com/roytuts/python/tree/master/python_flask_mysql_bootstrap_calendar_events)



<!-- GETTING STARTED -->
## Getting Started

To get this program up and running follow these simple steps.

### Prerequisites

Install Redis.
  ```sh
  sudo apt install -y redis
  sudo systemctl enable redis
  sudo systemctl start redis
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/hanzala123/Flask_calendar.git
   ```
2. Go to the directory
   ```sh
   cd Flask_calendar
   ```
3. Install the requirements
   ```sh
   pip3 install -r requirements.txt
   ```
4. Enter your password in the `config.py`
   ```sh
   WEB_PASSW = YOUR_PASSWORD_HERE
   ```



<!-- USAGE EXAMPLES -->
## Usage
Start the program using
   ```sh
   python3 main.py
   ```
Open your browser and visit http://localhost:8080/

Log in using the crendetials. The Default username is admin and password is 12345.
You can change the password in the config.py file.

Note: It is wise to use the Remove all events button every year to keep everything fast and optimized.


<!-- ROADMAP -->
## Roadmap

Contributions are always welcome.
See the [open issues](https://github.com/hanzala123/Flask_calendar/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - Hanzala Ibn Zahid

Project Link: [https://github.com/hanzala123/Flask_calendar](https://github.com/hanzala123/Flask_calendar)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Nerve](https://github.com/PaytmLabs/nerve)
* [python_flask_mysql_bootstrap_calendar_events](https://github.com/roytuts/python/tree/master/python_flask_mysql_bootstrap_calendar_events)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/hanzala123/Flask_notes/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/hanzala123/Flask_notes/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/Screenshot.png
[product-screenshot2]: images/Screenshot2.png
