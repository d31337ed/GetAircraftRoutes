function fetchRoutes() {
            let aircraftType = document.getElementById('aircraft').value
            let selectList = document.getElementById('airline-selector');
            let airlineCode = selectList.options[selectList.selectedIndex].value;
            document.getElementById("header-step-3").hidden = false;
            document.getElementById("header-step-3-1").hidden = false;
            document.getElementById("header-step-3-2").hidden = false;
            document.getElementById("header-step-3-3").hidden = false;
            document.getElementById("aircraftList").hidden = false;
            document.getElementById("routesList").hidden = false;
            document.getElementById("link").hidden = false;
            fetch('/airlines/' + airlineCode + '/fleet/' + aircraftType + '/routes/')
            .then((response) => {
                return response.json();
                })
                .then((data) => {
                console.log(data);
                let result = JSON.parse(JSON.stringify(data))
                console.log(result["routes"])
                document.getElementById("aircraftList").innerHTML = result["planes"];
                document.getElementById("routesList").innerHTML = result["routes"];
                document.getElementById("link").href = result["link"];
                });
            };