const settingBtn = document.querySelectorAll('.change')
const popup = document.querySelector('.popup')

// functions
function removeClose() {
    popup.classList.toggle('closed')
}


// event listeners

settingBtn.forEach(btn => {
    btn.addEventListener('click', removeClose)
})