document.getElementById('pmfby-form').addEventListener('submit', function (e) {
  e.preventDefault();
  alert("✅ Demo form submitted!");
  setTimeout(() => {
    window.location.href = "index.html";
  }, 1000);
});
