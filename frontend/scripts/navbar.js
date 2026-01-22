const hamburger = document.getElementById("hamburger");
const sidebar = document.getElementById("sidebar");

hamburger.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed"); // slide sidebar
    hamburger.innerHTML = sidebar.classList.contains("collapsed") ? "&#9776;" : "&#10005;"; // ☰ or ✕
});
