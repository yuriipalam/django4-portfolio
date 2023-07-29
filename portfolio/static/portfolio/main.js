// pop up
let openModalButtons = document.querySelectorAll('[data-modal-target]')
let closeModalButtons = document.querySelectorAll('[data-close-button]')
let overlay = document.getElementById('overlay')

openModalButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault()
        let modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})

overlay.addEventListener('click', () => {
    let modals = document.querySelectorAll('.modal.active')
    modals.forEach(modal => {
        closeModal(modal)
    });
})

closeModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        let modal = button.closest('.modal')
        closeModal(modal)
    })
})

function openModal(modal) {
    if (modal === null) {
        return
    }

    modal.classList.add('active')
    overlay.classList.add('active')
    modal.style.display = 'block'
    setTimeout(() => {
        modal.style.opacity = 1;
    }, 10);
}

function closeModal(modal) {
    if (modal === null) {
        return
    }
    modal.style.opacity = 0;
    setTimeout(() => {
        modal.style.display = 'none'
    }, 400);
    modal.classList.remove('active')
    overlay.classList.remove('active')
}

// header

let header = document.querySelector("#header")

document.addEventListener('scroll', (e) => {
    if (window.scrollY > 0) {
        header.classList.add('active')
    }
    else {
        header.classList.remove('active')
    }
})

let hamburger = document.querySelector(".hamburger")
let nav__links = document.querySelector(".nav__links")

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active")
    nav__links.classList.toggle("active")
})