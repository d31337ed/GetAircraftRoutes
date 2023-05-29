fetch('/airlines/timestamp')
    .then((response) => response.json())
    .then((data) => {
        document.getElementById('timestamp').textContent = `Airlines List updated on ${data}`;
    })
    .catch((error) => console.error(error));