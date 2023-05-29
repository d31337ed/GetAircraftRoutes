function fetchRoutes() {
    const link = document.getElementById('link');
    const routesList = document.getElementById('routesList');
    const aircraftList = document.getElementById('aircraftList');
    const spinner = document.getElementById('loading-spinner');
    const headerStep = document.getElementById('header-step-3');
    const headerStep1 = document.getElementById('header-step-3-1');
    const headerStep2 = document.getElementById('header-step-3-2');
    const headerStep3 = document.getElementById('header-step-3-3');

    spinner.hidden = false;
    headerStep.hidden = true;
    headerStep1.hidden = true;
    headerStep2.hidden = true;
    headerStep3.hidden = true;
    aircraftList.hidden = true;
    routesList.hidden = true;
    link.hidden = true;

    const aircraftType = document.getElementById('aircraft').value
    const selectList = document.getElementById('airline-selector');
    const airlineCode = selectList.options[selectList.selectedIndex].value;

    fetch(`/airlines/${airlineCode}/fleet/${aircraftType}/routes/`)
        .then((response) => response.json())
        .then((data) => {
            const airline = selectList.options[selectList.selectedIndex].innerText;

            headerStep2.innerText = `Routes operated by ${airline} on ${aircraftType} last week:`;
            headerStep3.innerText = `Map Link for routes operated last week on ${aircraftType} by ${airline}`;
            aircraftList.textContent = data['planes'];
            routesList.textContent = data['routes'];
            link.href = data['link'];

            spinner.hidden = true;
            headerStep.hidden = false;
            headerStep1.hidden = false;
            headerStep2.hidden = false;
            headerStep3.hidden = false;
            aircraftList.hidden = false;
            routesList.hidden = false;
            link.hidden = false;
        })
        .catch((error) => console.error(error))
}