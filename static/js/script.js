const titleSololearn = document.querySelector('#solo')
const titleMicrocamp = document.querySelector('#microcamp')
const sololearnCourses = document.querySelector('#sololearn-courses')
const microcampCourses = document.querySelector('#microcamp-courses')


function handleDisplay(title, container){
    title.addEventListener('click', () => {
        if(container.style.display != 'none'){
            container.style.display = 'none'
        } else {
            container.style.display = 'flex'
        }
    })
}

handleDisplay(titleSololearn, sololearnCourses)
handleDisplay(titleMicrocamp, microcampCourses)