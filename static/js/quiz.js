const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('model-body-confirm')
const startBtn  = document.getElementById('modalBtn')
const url = window.location.href

console.log(modalBtns)

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click',()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestion = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficult')
    const scoreTopass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')
    

    modalBody.innerHTML = `
    <div class="h5 mb-3">Are you want to sure to begin "<b>${name}</b>?</div>
    <div class="text-muted">
        <ul>
            <li>Number Of Questions: <b>${numQuestion}</b></li>
            <li>Time: <b>${time}</b>min</li>
        </ul> 
    </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))