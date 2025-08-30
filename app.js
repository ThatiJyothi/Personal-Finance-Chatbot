// app.js - used by student.html and professional.html
// sendMessage(mode) is called by the form onsubmit attribute

async function sendMessage(mode) {
  // form submission should not reload page
  event.preventDefault?.();

  const input = document.getElementById("messageInput");
  if (!input) return false;

  const text = input.value.trim();
  if (!text) return false;

  appendMessage("user", text);
  input.value = "";
  input.focus();

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text, mode: mode })
    });

    const data = await res.json();
    const reply = data.reply || data.response || "No reply.";

    appendMessage("bot", reply);
  } catch (err) {
    appendMessage("bot", "Network error. Please try again.");
    console.error(err);
  }

  // keep form from submitting / page reload
  return false;
}

function appendMessage(sender, text) {
  const windowEl = document.getElementById("chatWindow");
  if (!windowEl) return;

  const div = document.createElement("div");
  div.className = "msg " + (sender === "user" ? "user" : "bot");
  div.textContent = text;
  windowEl.appendChild(div);
  windowEl.scrollTop = windowEl.scrollHeight;
}

// Small helper: add a greeting prompt when the page loads
document.addEventListener("DOMContentLoaded", () => {
  // If chatWindow exists, show greeting
  const w = document.getElementById("chatWindow");
  if (w && w.children.length === 0) {
    appendMessage("bot", "Heyy 👋,How can I help you");
  }
});
