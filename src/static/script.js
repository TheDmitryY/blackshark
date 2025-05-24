async function sendRequest(buttonId) {
    const responseDiv = document.getElementById("response");
    responseDiv.textContent = "Відправка запроса...";

    try {
        const response = await fetch("/api/button_click", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ button_id: buttonId }),
        });

        const data = await response.json();
        responseDiv.textContent = data.message;
    } catch (error) {
        responseDiv.textContent = "Помилка: " + error.message;
    }
}
