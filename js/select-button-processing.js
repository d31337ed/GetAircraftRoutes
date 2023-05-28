            function selectAirline() {
                document.getElementById("aircraft-types").innerHTML="";
                document.getElementById("aircraft").innerHTML="";
                document.getElementById('progress-bar').hidden = false;
                let selectList = document.getElementById('airline-selector');
                let value = selectList.options[selectList.selectedIndex].value;
                fetch('/airlines/' + value +'/fleet/')
                    .then((response) => {
                    return response.json();
                    })
                    .then((data) => {
                    document.getElementById('progress-bar').hidden = true;
                    document.getElementById("header-step-2").hidden = false;
                    document.getElementById("label-step-2").hidden = false;
                    document.getElementById("button-step-2").hidden = false;
                    document.getElementById("aircraft-types").hidden = false;
                    document.getElementById("aircraft").hidden = false;
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