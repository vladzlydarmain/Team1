const modalWrapper = document.querySelector(".modal-wrapper");
const modalWindow = document.querySelector(".modal-window");
const modalButton = document.querySelector(".send-button");
const closeButton = document.querySelector(".close-button");

function modalOpen() {
  modalWrapper.removeAttribute("hidden");
}

function modalClose() {
  modalWrapper.setAttribute("hidden","1")
}


setTimeout(modalOpen, 5000);
modalButton.addEventListener("click",modalClose);
closeButton.addEventListener("click",modalClose);