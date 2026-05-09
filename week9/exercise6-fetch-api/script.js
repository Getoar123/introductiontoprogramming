// ==========================
// TASK 1 — QUOTE FETCH
// ==========================

const quoteDisplay = document.querySelector("#quote-display");
const quoteBtn = document.querySelector("#new-quote-btn");

async function fetchQuote() {
  quoteDisplay.innerHTML = "Loading...";

  try {
    const res = await fetch("https://api.quotable.io/random");

    if (!res.ok) throw new Error("HTTP " + res.status);

    const data = await res.json();

    quoteDisplay.innerHTML = `
      <p>"${data.content}"</p>
      <small>- ${data.author}</small>
    `;
  } catch (err) {
    quoteDisplay.innerHTML = "❌ Failed to load quote";
    console.error(err);
  }
}

if (quoteBtn) {
  quoteBtn.addEventListener("click", fetchQuote);
}

fetchQuote(); // load on start


// ==========================
// TASK 2 — GITHUB USER SEARCH
// ==========================

const input = document.querySelector("#github-input");
const searchBtn = document.querySelector("#github-search-btn");
const userDisplay = document.querySelector("#github-user");

async function searchUser() {
  const username = input.value.trim();
  if (!username) return;

  userDisplay.innerHTML = "Loading...";

  try {
    const res = await fetch(`https://api.github.com/users/${username}`);

    if (res.status === 404) {
      userDisplay.innerHTML = "❌ User not found";
      return;
    }

    if (!res.ok) throw new Error("HTTP " + res.status);

    const data = await res.json();

    userDisplay.innerHTML = `
      <img src="${data.avatar_url}" width="80" />
      <h3>${data.name || data.login}</h3>
      <p>${data.bio || "No bio"}</p>
      <p>Followers: ${data.followers}</p>
      <p>Repos: ${data.public_repos}</p>
      <a href="${data.html_url}" target="_blank">Profile</a>
    `;
  } catch (err) {
    userDisplay.innerHTML = "❌ Error loading user";
    console.error(err);
  }
}

searchBtn.addEventListener("click", searchUser);

input.addEventListener("keypress", (e) => {
  if (e.key === "Enter") searchUser();
});


// ==========================
// TASK 3 — POSTS + PAGINATION
// ==========================

const postsContainer = document.querySelector("#posts");
const loadMoreBtn = document.querySelector("#load-more");

let start = 0;
const limit = 10;

async function loadPosts() {
  try {
    const res = await fetch(
      `https://jsonplaceholder.typicode.com/posts?_start=${start}&_limit=${limit}`
    );

    if (!res.ok) throw new Error("HTTP " + res.status);

    const posts = await res.json();

    posts.forEach(post => {
      const div = document.createElement("div");
      div.classList.add("post");
      div.innerHTML = `
        <h4>${post.title}</h4>
        <p>${post.body}</p>
        <small>Click to load comments</small>
      `;

      div.addEventListener("click", () => loadComments(post.id, div));

      postsContainer.appendChild(div);
    });

    start += limit;
  } catch (err) {
    console.error(err);
    postsContainer.innerHTML += "<p>❌ Failed to load posts</p>";
  }
}

async function loadComments(postId, element) {
  try {
    const res = await fetch(
      `https://jsonplaceholder.typicode.com/posts/${postId}/comments`
    );

    const comments = await res.json();

    const commentHTML = comments
      .map(c => `<p><strong>${c.email}</strong>: ${c.body}</p>`)
      .join("");

    element.innerHTML += `<div class="comments">${commentHTML}</div>`;
  } catch (err) {
    console.error(err);
  }
}

loadMoreBtn.addEventListener("click", loadPosts);

loadPosts();


// ==========================
// TASK 5 — Promise.all
// ==========================

const multiBtn = document.querySelector("#multi-fetch-btn");
const multiDisplay = document.querySelector("#multi-fetch-result");

async function loadAll() {
  multiDisplay.innerHTML = "Loading...";

  try {
    const [quoteRes, userRes, todoRes] = await Promise.all([
      fetch("https://api.quotable.io/random"),
      fetch("https://jsonplaceholder.typicode.com/users/1"),
      fetch("https://jsonplaceholder.typicode.com/todos/1")
    ]);

    const quote = await quoteRes.json();
    const user = await userRes.json();
    const todo = await todoRes.json();

    multiDisplay.innerHTML = `
      <h3>Quote</h3>
      <p>${quote.content}</p>

      <h3>User</h3>
      <p>${user.name}</p>

      <h3>Todo</h3>
      <p>${todo.title}</p>
    `;
  } catch (err) {
    multiDisplay.innerHTML = "❌ Failed to load data";
  }
}

if (multiBtn) {
  multiBtn.addEventListener("click", loadAll);
}
