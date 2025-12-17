const API_URL = "http://127.0.0.1:8000/brainrots";

async function loadBrainrots() {
  const response = await fetch(API_URL);
  const data = await response.json();

  const list = document.getElementById("brainrot-list");
  list.innerHTML = "";

  data.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.title} - ${item.content} (Image: ${item.image})`;
    list.appendChild(li);
  });
}

loadBrainrots();