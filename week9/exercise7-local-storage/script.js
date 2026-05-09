let notes = JSON.parse(localStorage.getItem("notes")) || [];
let editingId = null;

// ==========================
// DOM ELEMENTS
// ==========================

const form = document.querySelector("#note-form");
const titleInput = document.querySelector("#title");
const bodyInput = document.querySelector("#body");
const notesContainer = document.querySelector("#notes-container");
const searchInput = document.querySelector("#search");
const submitBtn = document.querySelector("#submit-btn");
const cancelBtn = document.querySelector("#cancel-btn");

// ==========================
// SAVE TO LOCALSTORAGE
// ==========================

function saveNotes() {
  localStorage.setItem("notes", JSON.stringify(notes));
}

// ==========================
// RENDER NOTES
// ==========================

function renderNotes(filter = "") {
  notesContainer.innerHTML = "";

  let filtered = notes.filter(note =>
    (note.title + note.body).toLowerCase().includes(filter.toLowerCase())
  );

  if (filtered.length === 0) {
    notesContainer.innerHTML = `<p>No notes found</p>`;
    return;
  }

  // pinned first
  filtered.sort((a, b) => b.pinned - a.pinned);

  filtered.forEach(note => {
    const card = document.createElement("div");
    card.classList.add("note");

    const date = new Date(note.createdAt).toLocaleDateString();

    card.innerHTML = `
      <h3>${note.pinned ? "📌 " : ""}${note.title}</h3>
      <p>${note.body.slice(0, 100)}</p>
      <small>${date}</small>

      <div class="actions">
        <button class="pin">Pin</button>
        <button class="edit">Edit</button>
        <button class="delete">Delete</button>
      </div>
    `;

    // ==========================
    // DELETE
    // ==========================
    card.querySelector(".delete").addEventListener("click", () => {
      if (!confirm("Delete this note?")) return;

      notes = notes.filter(n => n.id !== note.id);
      saveNotes();
      renderNotes(searchInput.value);
    });

    // ==========================
    // PIN
    // ==========================
    card.querySelector(".pin").addEventListener("click", () => {
      const target = notes.find(n => n.id === note.id);
      target.pinned = !target.pinned;

      saveNotes();
      renderNotes(searchInput.value);
    });

    // ==========================
    // EDIT
    // ==========================
    card.querySelector(".edit").addEventListener("click", () => {
      titleInput.value = note.title;
      bodyInput.value = note.body;

      editingId = note.id;
      submitBtn.textContent = "Update Note";
    });

    notesContainer.appendChild(card);
  });
}

// ==========================
// CREATE / UPDATE NOTE
// ==========================

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const title = titleInput.value.trim();
  const body = bodyInput.value.trim();

  if (!title || !body) return;

  if (editingId) {
    const note = notes.find(n => n.id === editingId);
    note.title = title;
    note.body = body;

    editingId = null;
    submitBtn.textContent = "Save Note";
  } else {
    const newNote = {
      id: Date.now(),
      title,
      body,
      createdAt: new Date().toISOString(),
      pinned: false
    };

    notes.push(newNote);
  }

  saveNotes();
  renderNotes(searchInput.value);

  form.reset();
});

// ==========================
// CANCEL EDIT
// ==========================

cancelBtn.addEventListener("click", () => {
  editingId = null;
  submitBtn.textContent = "Save Note";
  form.reset();
});

// ==========================
// SEARCH FILTER
// ==========================

searchInput.addEventListener("input", (e) => {
  renderNotes(e.target.value);
});

// ==========================
// INIT
// ==========================

renderNotes();
