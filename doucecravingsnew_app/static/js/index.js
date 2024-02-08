//Slide Show feature using DOM Traversal methods add(), remove()

document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".mySlides");
    const dotsContainer = document.querySelector(".dots-container");
    const prevButton = document.querySelector(".prev");
    const nextButton = document.querySelector(".next");

    let currentSlide = 0;

    // Create dots for each slide
    slides.forEach((_, index) => {
        const dot = document.createElement("span");
        dot.classList.add("dot");
        dot.addEventListener("click", () => {
            showSlide(index);
        });
        dotsContainer.appendChild(dot);
    });
    showSlide(currentSlide);

    // Function to display a specific slide
    function showSlide(index) {
        if (index < 0) {
            index = slides.length - 1;
        } else if (index >= slides.length) {
            index = 0;
        }
        slides.forEach((slide) => {
            slide.style.display = "none";
        });
        slides[index].style.display = "block";
        currentSlide = index;
        updateDots();
    }

    // Function to update the active dot
    function updateDots() {
        const dots = document.querySelectorAll(".dot");
        dots.forEach((dot, index) => {
            if (index === currentSlide) {
                dot.classList.add("active");
            } else {
                dot.classList.remove("active");
            }
        });
    }

    //previous and next slide buttons
    prevButton.addEventListener("click", () => {
        showSlide(currentSlide - 1);
    });
    nextButton.addEventListener("click", () => {
        showSlide(currentSlide + 1);
    });
    setInterval(() => {
        showSlide(currentSlide + 1);
    }, 10000);
});

//JS functionality for Add an Item
/*
function showPopup() {
    document.getElementById("add-item-popup").style.display = "block";
}

function hidePopup() {
    document.getElementById("add-item-popup").style.display = "none";
}

/*
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("add-item-button").addEventListener("click", showPopup);
    const form = document.querySelector("form");
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        form.submit();
        hidePopup();
    });
});

 */

