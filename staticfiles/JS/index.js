const menuIcon = document.querySelector(".hamburger");
const navbar = document.querySelector(".navbar");

menuIcon.addEventListener("click", () => {
  navbar.classList.toggle("change");
});
