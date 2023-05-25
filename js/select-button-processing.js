            function selectAirline() {
                let selectList = document.getElementById('airline-selector');
                let value = selectList.options[selectList.selectedIndex].value;
                document.getElementById("header-step-2").hidden = false;
                document.getElementById("label-step-2").hidden = false;
                document.getElementById("button-step-2").hidden = false;
                document.getElementById("aircraft-types").hidden = false;
                document.getElementById("aircraft").hidden = false;
                fetch('/airlines/' + value +'/fleet/')
                    .then((response) => {
                    return response.json();
                    })
                    .then((data) => {
                    for (let i = 0; i < data.length; i++) {
                        let newButton = document.createElement("button");
                        newButton.classList.add("planeButton")
                        newButton.setAttribute("id", data[i])
                        let buttonText = document.createTextNode(data[i]);
                        newButton.appendChild(buttonText);
                        document.getElementById("aircraft-types").appendChild(newButton);
                        newButton.addEventListener('click', function(){
                        let chosen_aircraft = this.innerText;
                        document.getElementById('aircraft').value=chosen_aircraft;
                        })
                    }
                });
                };