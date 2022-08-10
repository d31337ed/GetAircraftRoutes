
# ✈️ Routes Finder

A small web-app to find out routes operating by certain aircraft types by certain airline. Helps to catch some rare aircraft or wisely choose business class miles redemption 

## 🖥 Demo

https://airoutes.de1337ed.ru/

## 🛠 Tech Stack

**Back:** Python 3.9, Flask, requests, bs4

**Client:** HTML5, CSS, JS




## 💭 General logic

- For choosen airline app parses Flightradar24 page with list of aircrafts
- User prompted to choose one of aircrafts type used by airline
- For choosen aircraft type app looks for unique routes operated by all of the aircrafts of this type
- A gcmap link is generated to visualise those unique routes


## 👨‍💻 Run Locally

Clone the project

```bash
  git clone https://github.com/d31337ed/GetAircraftRoutes.git
```

- Go to the project directory

```bash
  cd GetAircraftRoutes
```

- Run the app

```bash
  >python3 index.py
```

- Open the client 

```bash
  localhost:5000
```
   (default flask port, change if necessary)

## 🛣 Roadmap

- Catch exeptions after temporarily ban by flightradar. Add adaptive time-out for outcome requests. 

- Add text filtering in airline selector

- Fix Aircraft Types buttons shifts 

- Improve appearence 


## 📬 Feedback

If you have any feedback, please reach out to me at anton -at- de1337ed.ru

