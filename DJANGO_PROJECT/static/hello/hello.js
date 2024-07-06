function hello() {
  const header = document.querySelector("h1");
  if (header.innerHTML === "Hello, Andrey!") {
    header.innerHTML = "Goodbye, see you soon!";
  } else {
    header.innerHTML = "Hello, Andrey!";
  }
}

document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("button").onclick = hello;
});
