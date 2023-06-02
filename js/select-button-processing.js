const handleButtonClick = (e) => {
    document.getElementById("aircraft").value = e.currentTarget.textContent;
}

function selectAirline() {
    const aircraftTypes = document.getElementById('aircraft-types')
    const aircraft = document.getElementById('aircraft')
    const progressBar = document.getElementById('progress-bar')
    const selectList = document.getElementById('airline-selector');
    const value = selectList.options[selectList.selectedIndex].value;

    aircraftTypes.textContent = "";
    aircraft.textContent = "";
    progressBar.hidden = false;

    fetch(`/airlines/${value}/fleet/`)
        .then((response) => response.json())
        .then((data) => {
            progressBar.hidden = true;
            aircraftTypes.hidden = false;
            aircraft.hidden = false;

            document.getElementById('header-step-2').hidden = false;
            document.getElementById('label-step-2').hidden = false;
            document.getElementById('button-step-2').hidden = false;

            for (let i = 0; i < data.length; i++) {
                const newButton = document.createElement('button');
                newButton.classList.add('planeButton')
                newButton.setAttribute('id', data[i])
                const buttonText = document.createTextNode(data[i]);
                newButton.appendChild(buttonText);
                aircraftTypes.appendChild(newButton);
                newButton.addEventListener('click', handleButtonClick)
            }
        })
        .catch((error) => console.error(error));
}
