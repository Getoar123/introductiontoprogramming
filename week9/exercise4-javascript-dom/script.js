// ========================================
// EXERCISE 4 — JAVASCRIPT & THE DOM
// ========================================



// ========================================
// TASK 1 — CONSOLE WARMUP
// ========================================

// Select the h1 and change its text
const heading = document.querySelector("h1");
heading.textContent = "DOM Manipulation Complete";

// Select all cards and log how many exist
const cards = document.querySelectorAll(".card");

console.log("Total cards:", cards.length);

// Change background color of target box
const targetBox = document.querySelector("#target-box");

if (targetBox) {
    targetBox.style.backgroundColor = "#3b82f6";
}



// ========================================
// TASK 2 — CLICK COUNTER
// ========================================

const countDisplay = document.querySelector("#count");

const incrementButton = document.querySelector("#increment");
const decrementButton = document.querySelector("#decrement");
const resetButton = document.querySelector("#reset");

let count = 0;


// Update counter display + color
function updateCounter() {

    countDisplay.textContent = count;

    if (count === 0) {
        countDisplay.style.color = "red";
    }
    else if (count > 5) {
        countDisplay.style.color = "green";
    }
    else {
        countDisplay.style.color = "black";
    }
}


// Increment
incrementButton.addEventListener("click", function () {

    count++;

    updateCounter();
});


// Decrement
decrementButton.addEventListener("click", function () {

    if (count > 0) {
        count--;
    }

    updateCounter();
});


// Reset
resetButton.addEventListener("click", function () {

    count = 0;

    updateCounter();
});


// Initial update
updateCounter();



// ========================================
// TASK 3 — DYNAMIC LIST BUILDER
// ========================================

const itemInput = document.querySelector("#item-input");

const addItemButton = document.querySelector("#add-item");

const itemList = document.querySelector("#item-list");


addItemButton.addEventListener("click", function () {

    const text = itemInput.value.trim();

    // Prevent blank items
    if (text === "") {

        alert("Please enter an item.");

        itemInput.focus();

        return;
    }

    // Create li
    const li = document.createElement("li");

    li.textContent = text;


    // Create delete button
    const deleteButton = document.createElement("button");

    deleteButton.textContent = "×";

    deleteButton.classList.add("delete-btn");


    // Delete item when clicked
    deleteButton.addEventListener("click", function () {

        li.remove();
    });


    // Add button into li
    li.appendChild(deleteButton);


    // Add li into ul
    itemList.appendChild(li);


    // Clear input
    itemInput.value = "";


    // Focus input again
    itemInput.focus();
});



// ========================================
// TASK 4 — SHOW / HIDE TOGGLE
// ========================================

const toggleButton = document.querySelector("#toggle-button");

const details = document.querySelector(".details");


toggleButton.addEventListener("click", function () {

    details.classList.toggle("hidden");


    // Change button text
    if (details.classList.contains("hidden")) {

        toggleButton.textContent = "Show Details";
    }
    else {

        toggleButton.textContent = "Hide Details";
    }
});



// ========================================
// TASK 5 — COLOR MIXER
// ========================================

const redSlider = document.querySelector("#red");

const greenSlider = document.querySelector("#green");

const blueSlider = document.querySelector("#blue");

const previewBox = document.querySelector("#color-preview");

const hexDisplay = document.querySelector("#hex-display");


// Update color preview
function updateColor() {

    const r = redSlider.value;

    const g = greenSlider.value;

    const b = blueSlider.value;


    // RGB string
    const rgbColor = `rgb(${r}, ${g}, ${b})`;

    previewBox.style.backgroundColor = rgbColor;


    // Convert RGB -> HEX
    const rHex = Number(r).toString(16).padStart(2, "0");

    const gHex = Number(g).toString(16).padStart(2, "0");

    const bHex = Number(b).toString(16).padStart(2, "0");


    const hexColor = `#${rHex}${gHex}${bHex}`.toUpperCase();


    // Display HEX
    hexDisplay.textContent = hexColor;
}


// Listen for slider movement
redSlider.addEventListener("input", updateColor);

greenSlider.addEventListener("input", updateColor);

blueSlider.addEventListener("input", updateColor);


// Initial update
updateColor();
