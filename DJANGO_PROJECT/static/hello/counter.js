// Check if there is already a vlaue in local storage
if (!localStorage.getItem("counter")) {
  // If not, set the counter to 0 in local storage
  localStorage.setItem("counter", 0);
}

function count() {
  // Retrieve counter value from local storage
  let counter = localStorage.getItem("counter");

  // update counter
  counter++;
  document.querySelector("h2").innerHTML = counter;

  // Store counter in local storage
  localStorage.setItem("counter", counter);
}

document.addEventListener("DOMContentLoaded", function () {
  // Set heading to the current value inside local storage
  document.querySelector("h2").innerHTML = localStorage.getItem("counter");
  document.querySelector("button").onclick = count;
});

// let counter = 0;

// function count() {
//   counter++;
//   document.querySelector("h2").innerHTML = counter;

//   if (counter % 10 === 0) {
//     alert(`Count is now ${counter}`);
//   }
// }

// document.addEventListener("DOMContentLoaded", function () {
//   document.querySelector("button").onclick = count;
// });
