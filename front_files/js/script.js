const API_URL = "http://127.0.0.1:8000/brainrots";

async function loadBrainrots() {
  const response = await fetch(API_URL);
  const data = await response.json();

  const list = document.getElementById("brainrot-list");
  list.innerHTML = "";

  data.forEach(item => {
    const li = document.createElement("li");
    li.innerHTML = `
      <h3>@${item.title}</h3>
      <p>${item.content}</p>
      ${item.image ? `<img src="assets/images/${item.image}" alt="${item.title}" class="post-img">` : ""}
    `;
    list.appendChild(li);
  });
}

window.addEventListener("DOMContentLoaded", loadBrainrots);