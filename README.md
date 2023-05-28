
# ✈️ Routes Finder

A small web-app to find out routes operating by certain aircraft types by certain airline. Helps to catch some rare aircraft or wisely choose business class miles redemption 

## 🖥 Demo

https://routes.de1337ed.ru/

<img width="600" alt="Screenshot 2023-05-28 at 21 58 28" src="https://github.com/d31337ed/GetAircraftRoutes/assets/75523805/100128cf-40a3-4152-962f-10c99e054e24">

## 🛠 Tech Stack

**Back:** Python 3.9, FastAPI, requests, bs4

**Client:** HTML5, CSS, JS, Select2




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

- Run the web-server

```bash
  > uvicorn index:app  
```

- Open the client in browser

```bash
  http://localhost:8000
```

## 🛣 Roadmap

- Catch exeptions after temporarily ban by flightradar. Add adaptive time-out for outcome requests. 

- Fix Aircraft Types buttons shifts 

- Improve appearence 


## 📬 Feedback

If you have any feedback, please reach out to me at anton -at- de1337ed.ru

