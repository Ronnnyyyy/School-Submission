import csv
import os
from jinja2 import Template
from flask import url_for





if 'Output' in os.listdir():
    pass
else:
    os.mkdir('Output')

html_template= Template('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
:root {
  --primary-color: #e2c2ae;
  --secondary-color: rgb(245, 219, 211);
  --icon-size: 1.3em;
}

body {
  font-family: "Poppins", sans-serif;
  background: rgb(255, 241, 241);
  margin: 0;
}

.navbar {
  position: sticky;
  top: 0;
  z-index: 9999;
  background: rgb(250, 230, 230);
  box-shadow: rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.04) 0px 10px 10px -5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.04) 0px 10px 10px -5px;
}
.navbar .container {
  display: flex;
}
.navbar .container .logo {
  font-weight: bold;
  color: Black;
  margin: 1.2em;
  font-size: 1.8em;
}
.navbar .container .logo span {
  color: rgb(32, 43, 246);
}
.navbar .container .mobile-menu {
  cursor: pointer;
  font-size: 1.5em;
}
.navbar .container nav {
  position: absolute;
  right: 2.5em;
}
.navbar .container nav ul {
  list-style: none;
  display: flex;
}
.navbar .container nav ul li {
  margin: 1.7em 2em;
}
.navbar .container nav ul li a {
  font-size: 1.1em;
}
.navbar .container nav ul li a:hover {
  font-weight: bold;
  color: black;
}

.mobile-menu-exit {
  float: right;
  margin: 0;
  cursor: pointer;
  font-size: 1.5em;
}

@media only screen and (min-width: 950px) {
  .mobile-menu, .mobile-menu-exit {
    display: none;
  }
}
a {
  text-decoration: none;
  color: #676361;
}

section {
  padding: 2em 2em;
  display: flex;
  background: rgb(255, 241, 241);
}
section .left-col {
  background: var(--primary-color);
  width: 45%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
section .left-col .card {
  background: var(--secondary-color);
  width: 80%;
  height: auto;
  margin-right: -15em;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
  z-index: 999;
}
section .left-col .card .card-img {
  margin: 2em;
  margin-bottom: 0.2em;
}
section .left-col .card .card-img img {
  width: 15vw;
  border-radius: 50%;
  box-shadow: rgba(0, 0, 0, 0.09) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;
}
section .left-col .card .card-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 5em;
}
section .left-col .card .card-content .name {
  width: -moz-min-content;
  width: min-content;
  text-align: center;
}
section .left-col .card .card-content .name p {
  font-weight: bold;
  font-size: 2em;
  padding: 0;
  margin: 0;
  border-bottom: 2px solid #2f28ff;
}
section .left-col .card .card-footer {
  background: white;
  width: 100%;
}
section .left-col .card .card-footer ul {
  display: flex;
  list-style: none;
  margin: 0.2em;
  padding: 0;
  justify-content: space-around;
}
section .left-col .card .card-footer ul li {
  padding: 0em 0em;
}
section .left-col .card .card-footer ul li a {
  font-size: var(--icon-size);
}
section .left-col .card .card-footer ul li a:hover {
  color: black;
  font-weight: bold;
}
section .right-col {
  background: rgb(255, 241, 241);
  width: 60%;
  height: 100vh;
  display: flex;
  justify-content: center;
  flex-direction: column;
  text-align: left;
  padding-left: 7em;
}
section .right-col h1 {
  font-weight: bold;
  font-size: 7em;
  margin: 0em;
}
section .right-col h2 {
  font-weight: bold;
  font-family: 2em;
  margin: 0em;
}
section .right-col .cta {
  margin: 1em 0em;
  padding: 0;
  width: 40%;
}
section .right-col .cta ul {
  list-style: none;
  display: flex;
  padding: 0;
  justify-content: space-between;
}
section .right-col .cta ul li a {
  border: 3px solid blue;
  border-radius: 25px;
  padding: 0.4em 1.2em;
  color: black;
  font-weight: bold;
}
section .right-col .cta ul li a:hover {
  color: white;
  background: blue;
}

footer {
  margin-top: 3em;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.6em;
  background: rgb(250, 230, 230);
}
footer .claimer {
  font-weight: bold;
  font-size: 1.2em;
}
    </style>
    <script src="https://kit.fontawesome.com/4d9a9c6e9a.js" crossorigin="anonymous"></script>
</head>
<body>
    <div class="navbar">
        <div class="container">
            <a class="logo" href="#"></i> Port<span>Folio</span></a>

            <div id="mobile-cta" class="mobile-menu">
                <i class="fa-solid fa-bars"></i>
            </div>

            <nav>
                <div id="mobile-exit" class="mobile-menu-exit">
                    <i class="fa-solid fa-circle-xmark"></i>
                </div>
                
                <ul>
                    <li><a href="#">ABOUT ME</a></li>
                    <li><a href="#">RESUME</a></li>
                    <li><a href="#">PROJECTS</a></li>
                    <li><a href="#">CONTACT</a></li>
                </ul>
            </nav>
        </div>
    </div>
    <section class="hero">
        <div class="left-col">
            <div class="card">
                <div class="card-img">
                    <img src="{{ img_url }}" alt="profile-pic">
                </div>
                <div class="card-content">
                    <div class="name">
                        <p>
                        {{name}}
                        </p>
                    </div>
                    <p class="designation">
                        I am from {{country}}
                    </p>
                </div>
                <div class="card-footer">
                    <ul>
                        <li><a href="#"><i class="fa-brands fa-instagram"></i></a></li>
                        <li><a href=""><i class="fa-brands fa-github"></i></a></li>
                        <li><a href=""><i class="fa-brands fa-discord"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="right-col">
            <h1>Hello</h1>
            <h2 class="subhead">Here's who I am and what I do</h2>

            <div class="cta">
                <ul>
                    <li><a href="#">Resume</a></li>
                    <li><a href="#">Projects</a></li>
                </ul>
            </div>

            <p class="para1">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum voluptatum quae voluptatibus quas voluptas sed eum quaerat voluptatibus quae voluptatibus quas voluptas
            </p>
            <p class="para2">
                Lorem ipsum dolor sit am
            </p>
        </div>
    </section>
    <footer>
        <div class="claimer">
            <p>
                This Portfolio is made by Rohit proudly.
            </p>
        </div>
        <div class="email">
            <a href="mailto:iamwhatiwant7@gmail.com">iamwhatiwant7@gmail.com</a>
        </div>
    </footer>

    <script>

        const mobileBtn = document.getElementById('mobile-cta')
                nav = document.querySelector('nav')
                mobileBtnExit = document.getElementById('mobile-exit');

        mobileBtn.addEventListener('click', () => {
            nav.classList.add('menu-btn');
        })
        mobileBtnExit.addEventListener('click', () => {
            nav.classList.remove('menu-btn');
        })
    </script>
</body>
</html>
''')



with open('data\exported_data.csv','r') as fs:
    reader=csv.reader(fs)
    for i in reader:
        filename='Output/'+i[0]+'-'+i[1]+'.htm'
        with open(filename,'w') as f:
            template_vars={'name':i[1],'country':i[9],'img_url':'C:/Users/my pc/OneDrive/Desktop/Workspace/School submission/dummy.jpg'}
            html_content = html_template.render(template_vars)
            f.write(html_content)
        


