fetch('/airlines/timestamp')
    .then((response) => {
    return response.json();
    })
    .then((data) => {
    document.getElementById("timestamp").innerHTML = '  Airlines List updated on ' + data;
    });