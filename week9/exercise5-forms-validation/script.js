const form = document.querySelector("#signup-form");
const nameInput = document.querySelector("#name");
const email = document.querySelector("#email");
const password = document.querySelector("#password");
const confirm = document.querySelector("#confirm");
const age = document.querySelector("#age");
const website = document.querySelector("#website");
const country = document.querySelector("#country");
const bio = document.querySelector("#bio");
const terms = document.querySelector("#terms");

const submitBtn = document.querySelector("#submit-btn");
const success = document.querySelector("#success-message");
const bioCounter = document.querySelector("#bio-counter");
const strength = document.querySelector("#password-strength");

const inputs = document.querySelectorAll("input, select, textarea");

function showError(input, msg) {
  const error = input.nextElementSibling;
  if (error) error.textContent = msg;
  input.classList.add("invalid");
  input.classList.remove("valid");
}

function clearError(input) {
  const error = input.nextElementSibling;
  if (error) error.textContent = "";
  input.classList.remove("invalid");
  input.classList.add("valid");
}

function validateName() {
  if (nameInput.value.length < 2) return showError(nameInput, "Name too short");
  clearError(nameInput);
}

function validateEmail() {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!regex.test(email.value)) return showError(email, "Invalid email");
  clearError(email);
}

function validatePassword() {
  const val = password.value;
  const strong = /[A-Z]/.test(val) && /\d/.test(val);

  if (val.length < 8) {
    strength.textContent = "Weak";
    strength.style.color = "red";
  } else if (strong) {
    strength.textContent = "Strong";
    strength.style.color = "green";
  } else {
    strength.textContent = "Fair";
    strength.style.color = "orange";
  }

  if (val.length < 8) return showError(password, "Min 8 chars");
  clearError(password);
}

function validateConfirm() {
  if (confirm.value !== password.value)
    return showError(confirm, "Passwords don't match");
  clearError(confirm);
}

function validateAge() {
  if (age.value < 18 || age.value > 120)
    return showError(age, "Age must be 18-120");
  clearError(age);
}

function validateWebsite() {
  if (website.value && !website.value.startsWith("https://"))
    return showError(website, "Must start with https://");
  clearError(website);
}

function validateCountry() {
  if (!country.value) return showError(country, "Select a country");
  clearError(country);
}

function validateTerms() {
  if (!terms.checked) return showError(terms, "Must accept terms");
  clearError(terms);
}

function validateBio() {
  bioCounter.textContent = `${bio.value.length} / 200 characters`;

  if (bio.value.length > 200) {
    bioCounter.style.color = "red";
    submitBtn.disabled = true;
  } else {
    bioCounter.style.color = "black";
    submitBtn.disabled = false;
  }
}

// Events
nameInput.addEventListener("input", validateName);
email.addEventListener("input", validateEmail);
password.addEventListener("input", validatePassword);
confirm.addEventListener("input", validateConfirm);
age.addEventListener("input", validateAge);
website.addEventListener("input", validateWebsite);
country.addEventListener("change", validateCountry);
terms.addEventListener("change", validateTerms);
bio.addEventListener("input", validateBio);

form.addEventListener("submit", (e) => {
  e.preventDefault();

  validateName();
  validateEmail();
  validatePassword();
  validateConfirm();
  validateAge();
  validateWebsite();
  validateCountry();
  validateTerms();
  validateBio();

  const invalid = document.querySelector(".invalid");

  if (invalid) {
    invalid.scrollIntoView({ behavior: "smooth" });
    return;
  }

  success.classList.remove("hidden");
  form.style.display = "none";
});
