import './style.css'

let string = ""
let taskElements = []
for(let i = 0; i < 70; i++) {
  taskElements.push(document.getElementById("task"+(i+1)));
}

let emptyChar = " "
let fillChar = "*"
let globalProgress = 0

setInterval(() => {
  globalProgress++
  let progress = globalProgress % 100
  taskElements[Math.floor(globalProgress/100)].innerHTML = 'Loading loadingbar '+Math.floor(1+globalProgress/100)+' ['+fillChar.repeat(progress/7.5)+emptyChar.repeat(13-Math.floor((progress/7.5)))+'] '+(progress+1)+'/100' 
}, 40)