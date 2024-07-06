document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("form").onsubmit = function () {
    // Getting the accessKey variable from the HTML context
    const accessKey = document
      .querySelector("script")
      .innerText.match(/"([^"]+)"/)[1];
    const url = `https://api.freecurrencyapi.com/v1/latest?apikey=${accessKey}`;

    // Send a GET request to the URL
    fetch(url)
      // Put response into json form
      .then((response) => response.json())
      .then((data) => {
        // Log data to the console
        console.log(data);

        // Get currency from user input and convert to upper case
        const currency = document
          .querySelector("#currency")
          .value.toUpperCase();

        // Get rate from data
        const rate = data.data[currency];

        // Check if currency is valid:
        if (rate !== undefined) {
          // Display exchange on the screen
          document.querySelector(
            "#result"
          ).innerHTML = `1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
        } else {
          // Display error on the screen
          document.querySelector("#result").innerHTML = "Invalid Currency.";
        }
      })
      // Catch any errors and log them to the console
      .catch((error) => {
        console.log("Error:", error);
      });
    return false;
  };
});
